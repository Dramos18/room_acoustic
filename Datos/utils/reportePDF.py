"""
Generación de reportes PDF de Room Acoustic (ReportLab, Helvetica estándar).

Un único sistema visual para todos los reportes: encabezado y pie comunes,
jerarquía de títulos, tablas, tarjetas y bloque de %ALCONS compartidos.
Estructura, patrón visual y reglas: docs/REPORTS.md.

Tipos de reporte (métodos de ReportePDF, firmas sin cambios):
  - reporte_tiempo_reverberacion: RT60 (3 páginas) + %ALCONS opcional (4).
  - reporte_inteligibiliad: solo %ALCONS (1 página).
"""
import io
import os
import unicodedata
from datetime import datetime
from functools import lru_cache

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QFileDialog, QMessageBox

from Recursos.estilos import paleta
from Recursos.estilos.estilo import estiloWarning


# ─────────────────────────────────────────────
#  PALETA DE COLORES DEL PROYECTO
# ─────────────────────────────────────────────

def _rgb(color_hex):
    """'#00458C' -> (0.0, 0.27, 0.55) (formato de ReportLab)."""
    h = color_hex.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


# Identidad institucional: mismos valores que Recursos/estilos/paleta.py.
COLOR_PRIMARIO      = _rgb(paleta.AZUL_UA)       # Azul UA  (#00458C)
COLOR_SECUNDARIO    = _rgb(paleta.NARANJA_UA)    # Naranja UA (#DE7019)
COLOR_FONDO_TABLA_H = COLOR_PRIMARIO             # Encabezado de tabla

# Específicos del PDF (más oscuros que los de pantalla, para impresión).
COLOR_FONDO_HEADER  = (0.94, 0.96, 0.99)   # Azul muy claro
COLOR_FILA_PAR      = (0.95, 0.97, 1.00)
COLOR_FILA_IMPAR    = (1.00, 1.00, 1.00)
COLOR_FILA_REFERENCIA = (0.82, 0.89, 0.97)  # Bandas de referencia del Tr MID
COLOR_VERDE         = (0.13, 0.62, 0.30)
COLOR_ROJO          = (0.82, 0.11, 0.11)
COLOR_AMARILLO_BORDE= (0.70, 0.50, 0.10)
COLOR_FONDO_CONCLU  = (0.95, 0.95, 0.85)
COLOR_TEXTO         = (0.15, 0.15, 0.15)
COLOR_TEXTO_SEC     = (0.35, 0.35, 0.35)
COLOR_ENCABEZADO_SEC = (0.85, 0.91, 0.98)  # Texto secundario sobre la banda azul


# ─────────────────────────────────────────────
#  TIPOGRAFÍA, GEOMETRÍA Y ESPACIADOS (una sola fuente de verdad)
# ─────────────────────────────────────────────

FUENTE   = "Helvetica"
FUENTE_B = "Helvetica-Bold"
FUENTE_I = "Helvetica-Oblique"

T_ENCABEZADO = 13   # título en la banda superior
T_ENC_SEC    = 8    # subtítulo y fecha de la banda superior
T_H1         = 16   # título de página
T_SECCION    = 12   # título de sección
T_CUERPO     = 10   # texto de cuerpo
T_TABLA      = 8    # filas de tablas
T_TABLA_RT   = 9    # tabla de RT60 (cifras principales)
T_AUX        = 8    # notas y textos auxiliares
T_VALOR      = 13   # cifra dentro de una tarjeta

ANCHO_PAG, ALTO_PAG = letter
MARGEN     = inch
ANCHO_UTIL = ANCHO_PAG - 2 * MARGEN     # 468 pt: ancho común de todo el contenido
ALTO_ENCABEZADO = 48
Y_INICIO   = ALTO_PAG - ALTO_ENCABEZADO - 36   # inicio del contenido en cada página
Y_MIN      = 56                                 # límite inferior (sobre el pie)
GAP_BLOQUE = 16                                 # espacio entre bloques
ALTO_SECCION = 30                               # título de sección + separación
LOGO_TAM   = 34

_DIR_RECURSOS = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "Recursos"))
# Logo blanco para la banda azul (identidad institucional en el encabezado).
LOGO_ENCABEZADO = os.path.join(_DIR_RECURSOS, "iconos", "logoBN.png")
# Marca de agua: ya no se usa en los reportes (ver _marca_agua).
LOGO_MARCA_AGUA = os.path.join(_DIR_RECURSOS, "iconos", "isotipoUA.png")

SUBTITULO_POR_DEFECTO = "Room Acoustic · Universidad del Atlántico"


# ─────────────────────────────────────────────
#  ESCALA DE %ALCONS (contrato: docs/ACOUSTIC_MODEL.md §5)
#  Mismos límites e inclusión que AlconsCalculator.evaluar_alcons.
# ─────────────────────────────────────────────

NIVELES_ALCONS = [
    # (límite superior inclusivo, color, nombre, rango)
    (1.4,  (0.07, 0.53, 0.25), "Excelente", "0 – 1.4"),
    (5,    (0.13, 0.72, 0.35), "Buena",     "1.4 – 5"),
    (11.4, (0.93, 0.75, 0.08), "Regular",   "5 – 11.4"),
    (24.4, (0.93, 0.48, 0.08), "Pobre",     "11.4 – 24.4"),
    (47,   (0.82, 0.11, 0.11), "Mala",      "24.4 – 47"),
    (None, (0.55, 0.07, 0.07), "Crítico",   "> 47"),
]


def _nivel_alcons(porcentaje):
    """Índice (0-5) del nivel de %ALCONS, con la misma regla que el modelo."""
    for i, (limite, _, _, _) in enumerate(NIVELES_ALCONS):
        if limite is None or porcentaje <= limite:
            return i
    return len(NIVELES_ALCONS) - 1


# ─────────────────────────────────────────────
#  UTILIDADES DE TEXTO Y FORMATO
# ─────────────────────────────────────────────

def _recortar(texto, fuente, tam, ancho):
    """Recorta con '...' solo si el texto no cabe en `ancho` (medido, no por nº de caracteres)."""
    if stringWidth(texto, fuente, tam) <= ancho:
        return texto
    while texto and stringWidth(texto + "...", fuente, tam) > ancho:
        texto = texto[:-1]
    return texto + "..."


def _lineas(texto, fuente, tam, ancho, max_lineas=None):
    """Divide `texto` en líneas que caben en `ancho` (simpleSplit); nunca desborda."""
    lineas = [_recortar(l, fuente, tam, ancho) for l in simpleSplit(str(texto), fuente, tam, ancho)]
    if max_lineas and len(lineas) > max_lineas:
        lineas = lineas[:max_lineas]
        lineas[-1] = _recortar(lineas[-1] + "...", fuente, tam, ancho)
    return lineas or [""]


def _num(valor, decimales=2, unidad=""):
    """Número con decimales fijos y unidad; si no es numérico devuelve el texto tal cual."""
    try:
        texto = f"{float(valor):.{decimales}f}"
    except (TypeError, ValueError):
        return str(valor)
    return f"{texto} {unidad}" if unidad else texto


def _cantidad(valor):
    """Cantidad de objetos: sin decimales cuando es un entero (42.0 -> 42)."""
    try:
        f = float(valor)
    except (TypeError, ValueError):
        return str(valor)
    return str(int(f)) if f.is_integer() else str(f)


def _sin_acentos(texto):
    return "".join(ch for ch in unicodedata.normalize("NFD", str(texto))
                   if unicodedata.category(ch) != "Mn").lower()


# Unidad y decimales por parámetro del cálculo de %ALCONS (claves del modelo).
_FORMATO_PARAMETROS = {
    "distancia al oyente":            ("m", 2),
    "tiempo de reverberacion":        ("s", 2),
    "volumen de la sala":             ("m³", 2),
    "factor de directividad":         ("", 1),
    "superficie total":               ("m²", 2),
    "coeficiente medio de absorcion": ("", 3),
}


def _formato_parametro(clave, valor):
    unidad, decimales = _FORMATO_PARAMETROS.get(_sin_acentos(clave), ("", 3))
    if isinstance(valor, (int, float)):
        return _num(valor, decimales, unidad)
    return str(valor)


def _identificacion_salon(salon):
    """(tipo, aulas) del salón si existen en los datos; None en los que no vengan."""
    tipo = str(salon.get("Tipo", "")).strip() or None
    aulas = str(salon.get("aulas", "")).strip() or None
    return tipo, aulas


def _subtitulo_reporte(salon):
    tipo, aulas = _identificacion_salon(salon or {})
    partes = [p for p in (tipo, f"Aulas {aulas}" if aulas else None) if p]
    if not partes:
        return SUBTITULO_POR_DEFECTO
    return "Room Acoustic · " + " · ".join(partes)


@lru_cache(maxsize=4)
def _imagen(ruta):
    return ImageReader(ruta)


# ─────────────────────────────────────────────
#  COMPONENTES VISUALES COMPARTIDOS
# ─────────────────────────────────────────────

def _marca_agua(c, width, height, logo_path):
    """
    Añade el isotipo UA como marca de agua centrada y muy tenue.
    SIN USO desde 2026-09-19: atravesaba tablas y tarjetas dejando manchas;
    la identidad institucional la da el logo del encabezado. Se conserva
    como recurso documentado (docs/REPORTS.md).
    """
    try:
        logo = ImageReader(logo_path)
        lw = lh = 280
        x = (width - lw) / 2
        y = (height - lh) / 2
        c.saveState()
        c.setFillAlpha(0.07)
        c.drawImage(logo, x, y, width=lw, height=lh, mask='auto')
        c.restoreState()
    except Exception:
        pass


def _header(c, width, height, titulo_pagina: str, fecha_hora: str, logo_path: str = None,
            subtitulo: str = None):
    """
    Banda superior única para todos los reportes y páginas.

        [logo]  Título del reporte                      (13 pt, negrita)
                Subtítulo ..................  Generado: fecha (8 pt)

    Título y (subtítulo + fecha) van en líneas distintas, por lo que nunca se
    pisan; el título se reduce hasta 10 pt o se recorta si no cabe.
    """
    band_y = height - ALTO_ENCABEZADO
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.rect(0, band_y, width, ALTO_ENCABEZADO, fill=True, stroke=False)

    try:
        c.drawImage(_imagen(logo_path or LOGO_ENCABEZADO), MARGEN,
                    band_y + (ALTO_ENCABEZADO - LOGO_TAM) / 2,
                    width=LOGO_TAM, height=LOGO_TAM, mask='auto')
    except Exception:
        pass

    x_texto = MARGEN + LOGO_TAM + 12
    ancho_texto = width - MARGEN - x_texto

    tam = T_ENCABEZADO
    while tam > 10 and stringWidth(titulo_pagina, FUENTE_B, tam) > ancho_texto:
        tam -= 0.5
    c.setFillColor(colors.white)
    c.setFont(FUENTE_B, tam)
    c.drawString(x_texto, band_y + 28, _recortar(titulo_pagina, FUENTE_B, tam, ancho_texto))

    c.setFillColorRGB(*COLOR_ENCABEZADO_SEC)
    c.setFont(FUENTE_I, T_ENC_SEC)
    fecha = f"Generado: {fecha_hora}"
    c.drawRightString(width - MARGEN, band_y + 12, fecha)
    c.setFont(FUENTE, T_ENC_SEC)
    ancho_sub = ancho_texto - stringWidth(fecha, FUENTE_I, T_ENC_SEC) - 14
    c.drawString(x_texto, band_y + 12,
                 _recortar(subtitulo or SUBTITULO_POR_DEFECTO, FUENTE, T_ENC_SEC, ancho_sub))


def _footer(c, width, numero_pagina: int, total_paginas: int):
    """Línea inferior con texto institucional y número de página."""
    c.setStrokeColorRGB(*COLOR_SECUNDARIO)
    c.setLineWidth(0.8)
    c.line(MARGEN, 30, width - MARGEN, 30)
    c.setFont(FUENTE, 8)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.drawCentredString(width / 2, 18,
                        f"Software de Evaluación Acústica — Universidad del Atlántico  |  "
                        f"Página {numero_pagina} de {total_paginas}")


def _seccion_titulo(c, x, y, texto: str, ancho: float = ANCHO_UTIL):
    """Título de sección con marca naranja y filete inferior; `y` es la línea base del texto."""
    c.setFillColorRGB(*COLOR_SECUNDARIO)
    c.rect(x, y - 3, 4, 17, fill=True, stroke=False)
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.setFont(FUENTE_B, T_SECCION)
    c.drawString(x + 10, y, texto)
    c.setStrokeColorRGB(0.85, 0.85, 0.85)
    c.setLineWidth(0.5)
    c.line(x, y - 7, x + ancho, y - 7)


def _mini_card(c, x, y, etiqueta: str, valor: str, ancho: float = 130, alto: float = 46):
    """Tarjeta compacta con etiqueta arriba y valor abajo (contenida en `ancho`)."""
    w = ancho - 2                       # la sombra queda dentro del ancho asignado
    c.setFillColorRGB(0.88, 0.88, 0.88)
    c.roundRect(x + 2, y - 2, w, alto, 6, fill=True, stroke=False)
    c.setFillColor(colors.white)
    c.roundRect(x, y, w, alto, 6, fill=True, stroke=False)
    c.setStrokeColorRGB(*COLOR_PRIMARIO)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, alto, 6, fill=False, stroke=True)
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.setFont(FUENTE, T_AUX)
    c.drawCentredString(x + w / 2, y + alto - 14, _recortar(etiqueta, FUENTE, T_AUX, w - 8))
    tam = T_VALOR
    while tam > 9 and stringWidth(valor, FUENTE_B, tam) > w - 10:
        tam -= 0.5
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.setFont(FUENTE_B, tam)
    if stringWidth(valor, FUENTE_B, tam) <= w - 10:
        c.drawCentredString(x + w / 2, y + 12, valor)
    else:
        # Valor muy largo: hasta dos líneas de 9 pt dentro de la tarjeta.
        lineas = _lineas(valor, FUENTE_B, 9, w - 10, 2)
        for i, linea in enumerate(lineas):
            c.drawCentredString(x + w / 2, y + 17 - i * 11 + (5 if len(lineas) == 1 else 0), linea)


def _semaforo(c, x, y, es_optimo: bool, radio: float = 9):
    """
    Estado de la condición acústica: círculo de color con ✓ o ✗ (dibujados con
    trazos, sin imágenes) y texto; no depende solo del color.
    """
    color = COLOR_VERDE if es_optimo else COLOR_ROJO
    texto = "ÓPTIMA" if es_optimo else "NO ÓPTIMA"
    cx, cy = x + radio, y + radio
    c.setFillColorRGB(*color)
    c.circle(cx, cy, radio, fill=True, stroke=False)

    c.saveState()
    c.setStrokeColor(colors.white)
    c.setLineWidth(radio * 0.22)
    c.setLineCap(1)
    c.setLineJoin(1)
    k = radio / 11
    trazo = c.beginPath()
    if es_optimo:
        trazo.moveTo(cx - 5 * k, cy + 0.5 * k)
        trazo.lineTo(cx - 1.5 * k, cy - 3.5 * k)
        trazo.lineTo(cx + 5.5 * k, cy + 4 * k)
    else:
        trazo.moveTo(cx - 4 * k, cy - 4 * k)
        trazo.lineTo(cx + 4 * k, cy + 4 * k)
        trazo.moveTo(cx - 4 * k, cy + 4 * k)
        trazo.lineTo(cx + 4 * k, cy - 4 * k)
    c.drawPath(trazo, stroke=1, fill=0)
    c.restoreState()

    c.setFillColorRGB(*color)
    c.setFont(FUENTE_B, 11)
    c.drawString(x + radio * 2 + 8, y + radio - 4, texto)


def _barra_nivel(c, x, y, porcentaje: float, ancho: float = ANCHO_UTIL, alto: float = 16):
    """
    Escala de %ALCONS de 6 niveles (NIVELES_ALCONS, igual que el modelo):
    segmentos de igual ancho con nombre y rango; el nivel actual va a color
    completo y con un marcador sobre su posición. Devuelve la `y` inferior
    ocupada por las etiquetas.
    """
    n = len(NIVELES_ALCONS)
    seg = ancho / n
    activo = _nivel_alcons(porcentaje)

    for i, (limite, color, nombre, rango) in enumerate(NIVELES_ALCONS):
        if i == activo:
            relleno = color
        else:
            relleno = tuple(0.55 * k + 0.45 for k in color)   # mismo tono, atenuado
        c.setFillColorRGB(*relleno)
        c.rect(x + i * seg + 0.75, y, seg - 1.5, alto, fill=True, stroke=False)

        c.setFillColorRGB(*(COLOR_PRIMARIO if i == activo else (0.4, 0.4, 0.4)))
        c.setFont(FUENTE_B if i == activo else FUENTE, T_AUX)
        c.drawCentredString(x + i * seg + seg / 2, y - 11, nombre)
        c.setFont(FUENTE, 7)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawCentredString(x + i * seg + seg / 2, y - 21, rango)

    # Posición del valor dentro de su segmento (lineal entre sus límites).
    inferior = 0 if activo == 0 else NIVELES_ALCONS[activo - 1][0]
    superior = NIVELES_ALCONS[activo][0]
    if superior is None:
        superior = 100
    fraccion = min(max((porcentaje - inferior) / (superior - inferior), 0), 1)
    mx = x + activo * seg + fraccion * seg

    c.setFillColorRGB(*COLOR_TEXTO)
    marcador = c.beginPath()
    marcador.moveTo(mx - 5, y + alto + 9)
    marcador.lineTo(mx + 5, y + alto + 9)
    marcador.lineTo(mx, y + alto + 2)
    marcador.close()
    c.drawPath(marcador, stroke=0, fill=1)
    etiqueta = f"{porcentaje:.2f} %"
    mitad = stringWidth(etiqueta, FUENTE_B, T_AUX) / 2
    c.setFont(FUENTE_B, T_AUX)
    c.drawString(min(max(mx - mitad, x), x + ancho - 2 * mitad), y + alto + 12, etiqueta)
    return y - 24


def _tabla_rt(c, x, y, frecuencias, sabine, eyring, col_width, row_height):
    """
    Tabla de RT60 con encabezado coloreado y filas alternas. Las bandas de
    referencia del Tr MID (500, 1000 y 2000 Hz) se resaltan con un tinte suave
    en toda la fila. Devuelve la `y` inferior de la tabla.
    """
    encabezados = ["Frecuencia (Hz)", "Sabine RT60 (s)", "Eyring RT60 (s)"]
    n_cols = len(encabezados)

    c.setFont(FUENTE_B, T_TABLA_RT)
    for i, texto in enumerate(encabezados):
        cx = x + i * col_width
        c.setFillColorRGB(*COLOR_FONDO_TABLA_H)
        c.rect(cx, y - row_height, col_width, row_height, fill=True, stroke=False)
        c.setFillColor(colors.white)
        c.drawCentredString(cx + col_width / 2, y - row_height + 6, texto)

    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(0.4)
    c.rect(x, y - row_height, col_width * n_cols, row_height, fill=False, stroke=True)

    for fila_idx, f in enumerate(frecuencias):
        fy = y - (fila_idx + 2) * row_height
        referencia = f in (500, 1000, 2000)
        if referencia:
            bg = COLOR_FILA_REFERENCIA
        else:
            bg = COLOR_FILA_PAR if fila_idx % 2 == 0 else COLOR_FILA_IMPAR
        valores = [str(f), _num(sabine[f]), _num(eyring.get(f, 0))]

        for col_idx, val in enumerate(valores):
            cx = x + col_idx * col_width
            c.setFillColorRGB(*bg)
            c.rect(cx, fy, col_width, row_height, fill=True, stroke=False)
            c.setStrokeColorRGB(0.85, 0.85, 0.85)
            c.setLineWidth(0.3)
            c.rect(cx, fy, col_width, row_height, fill=False, stroke=True)
            c.setFillColor(colors.black)
            c.setFont(FUENTE_B if referencia else FUENTE, T_TABLA_RT)
            c.drawCentredString(cx + col_width / 2, fy + 6, val)

    return y - (len(frecuencias) + 1) * row_height


# ─────────────────────────────────────────────
#  DOCUMENTO: cursor vertical, paginación y bloques reutilizables
# ─────────────────────────────────────────────

class _Doc:
    """
    Contexto de un reporte. `y` es el borde superior del próximo elemento.
    Si un bloque no cabe, `asegurar` abre una página de continuación con el
    mismo encabezado y pie, de modo que ningún contenido pisa el pie ni sale
    del área imprimible. `total` se obtiene con una pasada previa
    (_contar_paginas) para que el pie diga "Página N de M" correctamente.
    """

    def __init__(self, c, fecha_hora, total_paginas, subtitulo=None):
        self.c = c
        self.fecha_hora = fecha_hora
        self.total = total_paginas
        self.subtitulo = subtitulo
        self.n = 0
        self.y = Y_INICIO
        self.titulo = ""

    def pagina(self, titulo, continuacion=False):
        if self.n:
            self.c.showPage()
        self.n += 1
        self.titulo = titulo
        _header(self.c, ANCHO_PAG, ALTO_PAG,
                titulo + (" (continuación)" if continuacion else ""),
                self.fecha_hora, subtitulo=self.subtitulo)
        _footer(self.c, ANCHO_PAG, self.n, self.total)
        self.y = Y_INICIO

    def asegurar(self, alto):
        if self.y - alto < Y_MIN:
            self.pagina(self.titulo, continuacion=True)

    def cerrar(self):
        self.c.showPage()


def _contar_paginas(dibujar, fecha_hora, subtitulo=None):
    """Ejecuta `dibujar(doc)` sobre un canvas descartable y devuelve el nº de páginas."""
    doc = _Doc(canvas.Canvas(io.BytesIO(), pagesize=letter), fecha_hora, 0, subtitulo)
    dibujar(doc)
    return doc.n


def _titulo_pagina(doc, texto):
    """Título principal de la página (16 pt) con filete naranja del largo del texto."""
    c = doc.c
    base = doc.y - T_H1
    c.setFont(FUENTE_B, T_H1)
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.drawString(MARGEN, base, texto)
    c.setStrokeColorRGB(*COLOR_SECUNDARIO)
    c.setLineWidth(2.5)
    c.line(MARGEN, base - 6, MARGEN + min(stringWidth(texto, FUENTE_B, T_H1), ANCHO_UTIL), base - 6)
    doc.y = base - 6 - 18


def _seccion(doc, texto, reservar=40):
    """Título de sección; evita dejarlo huérfano al final de una página."""
    doc.asegurar(ALTO_SECCION + reservar)
    _seccion_titulo(doc.c, MARGEN, doc.y - 14, texto)
    doc.y -= ALTO_SECCION


def _parrafos(doc, textos, tam=T_CUERPO, leading=14, fuente=FUENTE, color=COLOR_TEXTO,
              sangria=6, espacio=6):
    """Párrafos ajustados al ancho útil con simpleSplit (sin saltos de línea manuales)."""
    c = doc.c
    for texto in textos:
        for linea in _lineas(texto, fuente, tam, ANCHO_UTIL - sangria):
            doc.asegurar(leading)
            c.setFont(fuente, tam)
            c.setFillColorRGB(*color)
            c.drawString(MARGEN + sangria, doc.y - tam, linea)
            doc.y -= leading
        doc.y -= espacio
    doc.y -= GAP_BLOQUE - espacio


def _fila_cards(doc, items, alto=56, columnas=None):
    """Fila de tarjetas de igual ancho que ocupa exactamente el ancho útil."""
    n = columnas or len(items)
    gap = 14
    ancho = (ANCHO_UTIL - gap * (n - 1)) / n
    doc.asegurar(alto + 4)
    for i, (etiqueta, valor) in enumerate(items):
        _mini_card(doc.c, MARGEN + i * (ancho + gap), doc.y - alto, etiqueta, valor, ancho, alto)
    doc.y -= alto + GAP_BLOQUE


def _tabla(doc, columnas, filas, tam=T_TABLA, primera_bold=False, max_lineas=24):
    """
    Tabla al ancho útil con columnas proporcionales, encabezado azul, filas
    alternas, texto ajustado a la celda (varias líneas, sin recortar por nº
    de caracteres) y continuación en otra página con el encabezado repetido.

    columnas: [(título, proporción, alineación 'l'|'c'|'r'), ...]
    filas: lista de filas; cada celda es str y puede contener '\\n'.
    """
    c = doc.c
    total = sum(p for _, p, _ in columnas)
    anchos = [ANCHO_UTIL * p / total for _, p, _ in columnas]
    xs = [MARGEN + sum(anchos[:i]) for i in range(len(anchos))]
    lead, pad, h_enc = tam + 2, 4, 18

    def dibujar_encabezado():
        top = doc.y
        for i, (titulo, _, _) in enumerate(columnas):
            c.setFillColorRGB(*COLOR_FONDO_TABLA_H)
            c.rect(xs[i], top - h_enc, anchos[i], h_enc, fill=True, stroke=False)
            c.setFillColor(colors.white)
            c.setFont(FUENTE_B, tam)
            c.drawCentredString(xs[i] + anchos[i] / 2, top - h_enc / 2 - 0.3 * tam, titulo)
        c.setStrokeColorRGB(0.75, 0.75, 0.75)
        c.setLineWidth(0.3)
        c.rect(MARGEN, top - h_enc, ANCHO_UTIL, h_enc, fill=False, stroke=True)
        doc.y = top - h_enc

    def preparar(fila):
        celdas = []
        for i, valor in enumerate(fila):
            fuente = FUENTE_B if (primera_bold and i == 0) else FUENTE
            celdas.append((fuente, _lineas(valor, fuente, tam, anchos[i] - 2 * pad, max_lineas)))
        return celdas

    preparadas = [preparar(f) for f in filas]
    primera = max([len(l) for _, l in preparadas[0]], default=1) if preparadas else 1
    doc.asegurar(h_enc + max(18, primera * lead + 2 * pad))
    dibujar_encabezado()

    for idx, celdas in enumerate(preparadas):
        n = max(len(lineas) for _, lineas in celdas)
        h = max(18, n * lead + 2 * pad - 2)
        if doc.y - h < Y_MIN:
            doc.pagina(doc.titulo, continuacion=True)
            dibujar_encabezado()
        top = doc.y
        bg = COLOR_FILA_PAR if idx % 2 == 0 else COLOR_FILA_IMPAR
        inicio = top - (h - n * lead) / 2
        for i, (fuente, lineas) in enumerate(celdas):
            c.setFillColorRGB(*bg)
            c.rect(xs[i], top - h, anchos[i], h, fill=True, stroke=False)
            c.setStrokeColorRGB(0.88, 0.88, 0.88)
            c.setLineWidth(0.3)
            c.rect(xs[i], top - h, anchos[i], h, fill=False, stroke=True)
            c.setFillColor(colors.black)
            c.setFont(fuente, tam)
            alin = columnas[i][2]
            for k, linea in enumerate(lineas):
                base = inicio - (k + 0.5) * lead - 0.3 * tam
                if alin == 'c':
                    c.drawCentredString(xs[i] + anchos[i] / 2, base, linea)
                elif alin == 'r':
                    c.drawRightString(xs[i] + anchos[i] - pad, base, linea)
                else:
                    c.drawString(xs[i] + pad, base, linea)
        doc.y = top - h
    doc.y -= GAP_BLOQUE


def _caja_conclusion(doc, titulo, texto, es_positivo):
    """
    Recuadro de conclusión con relleno uniforme: alto calculado a partir del
    texto ajustado al ancho, con el mismo espacio arriba y abajo.
    """
    c = doc.c
    pad, lead = 12, 14
    lineas = _lineas(texto, FUENTE, T_CUERPO, ANCHO_UTIL - 2 * pad - 6)
    alto = 2 * pad + lead + len(lineas) * lead
    doc.asegurar(alto + 6)

    color_borde = COLOR_VERDE if es_positivo else COLOR_ROJO
    color_fondo = (0.93, 0.99, 0.94) if es_positivo else (0.99, 0.94, 0.94)
    base_y = doc.y - alto
    c.setFillColorRGB(*color_fondo)
    c.roundRect(MARGEN, base_y, ANCHO_UTIL, alto, 8, fill=True, stroke=False)
    c.setStrokeColorRGB(*color_borde)
    c.setLineWidth(1.5)
    c.roundRect(MARGEN, base_y, ANCHO_UTIL, alto, 8, fill=False, stroke=True)
    c.setFillColorRGB(*color_borde)
    c.roundRect(MARGEN, base_y, 5, alto, 4, fill=True, stroke=False)

    tope = doc.y - pad
    c.setFont(FUENTE_B, 11)
    c.setFillColorRGB(*color_borde)
    c.drawString(MARGEN + 14, tope - lead / 2 - 0.3 * 11, titulo)
    c.setFont(FUENTE, T_CUERPO)
    c.setFillColorRGB(0.1, 0.1, 0.1)
    for i, linea in enumerate(lineas):
        c.drawString(MARGEN + 14, tope - lead - (i + 0.5) * lead - 0.3 * T_CUERPO, linea)
    doc.y -= alto + GAP_BLOQUE


_EXPLICACION_ALCONS = [
    "El %ALCONS (Porcentaje de Pérdida de Articulación de Consonantes) indica qué proporción de "
    "las consonantes habladas se pierde antes de llegar al oyente; mide qué tan bien se entiende "
    "la voz humana dentro de un espacio cerrado.",
    "Las consonantes son las responsables de distinguir palabras como 'pero' de 'perro' o 'bala' "
    "de 'vala'. Si se pierden, el mensaje se vuelve confuso o incomprensible.",
    "Un %ALCONS bajo (cercano a 0 %) significa que casi nada se pierde; valores altos indican que "
    "el oyente tiene dificultades para entender al hablante. La escala de arriba muestra los seis "
    "niveles de clasificación que utiliza la aplicación.",
]


def _bloque_alcons(doc, alcons):
    """
    Bloque de %ALCONS compartido por el reporte independiente de Inteligibilidad
    y la página 4 del reporte RT: mismas tarjetas, escala, clasificación,
    explicación y tabla de parámetros. Solo cambian los datos.
    """
    alcons_val = float(alcons.get('%ALCONS', alcons.get('%ALCons', 0)))
    evaluacion = str(alcons.get('Evaluacion', alcons.get('Evaluación', '')))
    evaluacion = evaluacion.replace('■ ', '').replace('■', '').strip()
    dc_val = alcons.get('Distancia Critica (Dc)', alcons.get('Distancia Crítica (Dc)', 'N/A'))
    r_val = alcons.get('Constante del Recinto (R)', 'N/A')

    _seccion(doc, "Resultados Principales", reservar=60)
    _fila_cards(doc, [
        ("%ALCONS", _num(alcons_val, 2, "%")),
        ("Distancia crítica (Dc)", _num(dc_val, 2, "m")),
        ("Constante del recinto (R)", _num(r_val, 2, "m²")),
    ])

    _seccion(doc, "Nivel de Inteligibilidad", reservar=110)
    doc.asegurar(100)
    _barra_nivel(doc.c, MARGEN, doc.y - 42, alcons_val)
    doc.y -= 42 + 16 + 24 + 4
    _parrafos(doc, [f"Clasificación: {evaluacion}"], tam=11, leading=15, fuente=FUENTE_B,
              color=COLOR_PRIMARIO, sangria=0, espacio=0)

    _seccion(doc, "¿Qué Significa el %ALCONS?", reservar=50)
    _parrafos(doc, _EXPLICACION_ALCONS)

    detalles = alcons.get("Detalles", {})
    if detalles:
        _seccion(doc, "Parámetros de Cálculo", reservar=50)
        _tabla(doc, [("Parámetro", 0.62, 'l'), ("Valor", 0.38, 'l')],
               [[f"{clave}", _formato_parametro(clave, valor)] for clave, valor in detalles.items()],
               tam=T_CUERPO - 1)


# ─────────────────────────────────────────────
#  CONTENIDO DE CADA REPORTE
# ─────────────────────────────────────────────

_NOMBRES_SUPERFICIE = {
    "frontal": "Frontal", "trasera": "Trasera", "izquierda": "Izquierda",
    "derecha": "Derecha", "piso": "Piso", "techo": "Techo",
}


def _dibujar_reporte_rt(doc, resultados):
    """Reporte RT60 (3 páginas) + %ALCONS opcional (4.ª página)."""
    salon = resultados.get("salon", {}) or {}
    dimensiones = salon.get("dimensiones", {})
    largo = dimensiones.get("largo", "N/A")
    ancho = dimensiones.get("ancho", "N/A")
    altura = dimensiones.get("altura", "N/A")
    alcons = resultados.get("reporte_inteligibilidad")
    materiales = salon.get("materiales", {})
    objetos_adicionales = salon.get("objetos_adicionales") or []

    sabine = resultados.get("sabine_rt", {})
    eyring = resultados.get("eyring_rt", {})
    frecuencias = sorted(sabine.keys())

    # ════════════════════════════════════════
    #  PÁGINA 1 — Detalle del salón
    # ════════════════════════════════════════
    doc.pagina("Resumen del Salón Evaluado")
    _titulo_pagina(doc, "Ficha del Salón")

    tipo, aulas = _identificacion_salon(salon)
    ident = [(et, v) for et, v in (("Tipo de salón", tipo), ("Aulas", aulas)) if v]
    if ident:
        _seccion(doc, "Identificación del Salón", reservar=60)
        _fila_cards(doc, ident, columnas=3)

    try:
        vol_str = _num(float(largo) * float(ancho) * float(altura), 2, "m³")
    except (TypeError, ValueError):
        vol_str = "N/A"
    _seccion(doc, "Dimensiones", reservar=60)
    _fila_cards(doc, [
        ("Largo", _num(largo, 2, "m")),
        ("Ancho", _num(ancho, 2, "m")),
        ("Altura", _num(altura, 2, "m")),
        ("Volumen", vol_str),
    ])

    filas = []
    for sup_key, datos in materiales.items():
        objetos = datos.get("objetos_adheridos") or []
        obj_texto = "\n".join(
            f"{o.get('nombre', '')} ({o.get('material', '')}) · {_num(o.get('area', ''), 2, 'm²')}"
            for o in objetos) if objetos else "—"
        filas.append([
            _NOMBRES_SUPERFICIE.get(str(sup_key).lower(), str(sup_key).capitalize()),
            datos.get("material", "N/A"),
            _num(datos.get("area", "N/A")),
            obj_texto,
        ])
    _seccion(doc, "Materiales de las Superficies", reservar=60)
    _tabla(doc, [("Superficie", 0.14, 'l'), ("Material base", 0.34, 'l'),
                 ("Área (m²)", 0.12, 'r'), ("Objetos adheridos", 0.40, 'l')],
           filas, primera_bold=True)

    if objetos_adicionales:
        _seccion(doc, "Objetos Adicionales en el Salón", reservar=60)
        _tabla(doc, [("Objeto", 0.34, 'l'), ("Material", 0.50, 'l'), ("Cantidad", 0.16, 'r')],
               [[str(o.get("nombre", "N/A")), str(o.get("material", "N/A")),
                 _cantidad(o.get("cantidad", "N/A"))] for o in objetos_adicionales])

    # ════════════════════════════════════════
    #  PÁGINA 2 — Gráfica + Tabla RT60
    # ════════════════════════════════════════
    doc.pagina("Tiempo de Reverberación RT60 — Resultados")
    _titulo_pagina(doc, "Resultados de RT60")

    _seccion(doc, "Comparación Gráfica: Sabine vs Eyring", reservar=280)
    _parrafos(doc, [
        "La gráfica muestra el Tiempo de Reverberación (RT60) calculado con dos métodos: Sabine (rojo) "
        "y Eyring (azul). Cada punto corresponde a una banda de frecuencia. La línea horizontal punteada "
        "roja indica el límite recomendado de 0.8 s según la norma BB93 para aulas escolares."
    ], tam=T_AUX, leading=11, fuente=FUENTE_I, color=COLOR_TEXTO_SEC)

    grafica = resultados.get("grafica")
    if grafica:
        grafica.seek(0)
        imagen = ImageReader(grafica)
        img_w, img_h = imagen.getSize()
        alt_img = 250
        anch_img = img_w * alt_img / img_h
        doc.asegurar(alt_img + GAP_BLOQUE)
        doc.c.drawImage(imagen, (ANCHO_PAG - anch_img) / 2, doc.y - alt_img,
                        width=anch_img, height=alt_img)
        doc.y -= alt_img + GAP_BLOQUE

    _seccion(doc, "Tabla de Resultados Numéricos", reservar=190)
    _parrafos(doc, [
        "Nota: las frecuencias resaltadas (500, 1000 y 2000 Hz) son las de referencia para el "
        "cálculo del Tr MID."
    ], tam=T_AUX, leading=11, fuente=FUENTE_I, color=COLOR_TEXTO_SEC)
    row_h_t = 20
    doc.asegurar((len(frecuencias) + 1) * row_h_t)
    doc.y = _tabla_rt(doc.c, MARGEN, doc.y, frecuencias, sabine, eyring, ANCHO_UTIL / 3, row_h_t) - GAP_BLOQUE

    # ════════════════════════════════════════
    #  PÁGINA 3 — Interpretación RT60
    # ════════════════════════════════════════
    doc.pagina("Interpretación del Tiempo de Reverberación")
    _titulo_pagina(doc, "Análisis Acústico — Tiempo de Reverberación")

    sabine_mid = [sabine[f] for f in [500, 1000, 2000] if f in sabine]
    eyring_mid = [eyring[f] for f in [500, 1000, 2000] if f in eyring]
    trmid_sabine = sum(sabine_mid) / len(sabine_mid) if sabine_mid else 0
    trmid_eyring = sum(eyring_mid) / len(eyring_mid) if eyring_mid else 0
    es_optimo    = trmid_sabine <= 0.8 and trmid_eyring <= 0.8

    _seccion(doc, "Tr MID — Tiempo de Reverberación Medio (500, 1000 y 2000 Hz)", reservar=60)
    _fila_cards(doc, [
        ("Tr MID Sabine", _num(trmid_sabine, 2, "s")),
        ("Tr MID Eyring", _num(trmid_eyring, 2, "s")),
        ("Límite BB93", "0.80 s"),
    ])

    _seccion(doc, "Evaluación de la Condición Acústica", reservar=40)
    doc.asegurar(30)
    _semaforo(doc.c, MARGEN + 4, doc.y - 24, es_optimo, radio=11)
    doc.y -= 24 + GAP_BLOQUE

    _seccion(doc, "Cómo Interpretar estos Resultados", reservar=60)
    _parrafos(doc, [
        "El Tr MID es el promedio del tiempo de reverberación a 500 Hz, 1000 Hz y 2000 Hz. Estas "
        "frecuencias son las más relevantes para la comprensión de la voz humana.",
        "Un Tr MID menor o igual a 0.8 s se considera óptimo para aulas según la norma BB93 (Reino "
        "Unido), la cual es adoptada como referencia internacional en diseño acústico educativo.",
        "Si el Tr MID supera 0.8 s, las palabras del docente pueden solaparse entre sí, dificultando "
        "la comprensión y aumentando el esfuerzo auditivo de los estudiantes.",
    ])

    if es_optimo:
        conclusion = (
            "La condición acústica de este salón es ÓPTIMA. El Tr MID se encuentra dentro del rango "
            "recomendado (menor o igual a 0.8 s), lo que garantiza adecuada inteligibilidad del habla "
            "y confort auditivo para docentes y estudiantes."
        )
    else:
        conclusion = (
            "La condición acústica de este salón NO es ÓPTIMA. El Tr MID supera el límite de 0.8 s "
            "establecido por la norma BB93. Esto puede afectar la claridad del habla y reducir la "
            "calidad del entorno de aprendizaje. Se recomienda evaluar el uso de materiales absorbentes."
        )
    _caja_conclusion(doc, "Conclusión:", conclusion, es_optimo)

    # ════════════════════════════════════════
    #  PÁGINA 4 (opcional) — %ALCons
    # ════════════════════════════════════════
    if alcons is not None:
        doc.pagina("Inteligibilidad del Habla — %ALCONS")
        _titulo_pagina(doc, "Evaluación de la Inteligibilidad — %ALCONS")
        _bloque_alcons(doc, alcons)


def _dibujar_ih_independiente(doc, reporte):
    """Reporte de solo inteligibilidad: mismo encabezado, título y bloque que la página 4 del RT."""
    doc.pagina("Inteligibilidad del Habla — %ALCONS")
    _titulo_pagina(doc, "Evaluación de la Inteligibilidad — %ALCONS")
    _bloque_alcons(doc, reporte)


# ─────────────────────────────────────────────
#  CLASE PRINCIPAL
# ─────────────────────────────────────────────

class ReportePDF:

    @staticmethod
    def reporte_inteligibiliad(self, reporte):
        """
        Genera un reporte de solo inteligibilidad (%ALCONS) en PDF.
        Mantiene la firma original del método.
        """
        nombre_archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Reporte PDF", os.getenv('HOME', '/'), "Archivos PDF (*.pdf)"
        )
        if not nombre_archivo:
            return

        try:
            fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            total = _contar_paginas(lambda d: _dibujar_ih_independiente(d, reporte), fecha_hora)
            c = canvas.Canvas(nombre_archivo, pagesize=letter)
            doc = _Doc(c, fecha_hora, total)
            _dibujar_ih_independiente(doc, reporte)
            doc.cerrar()

            c.save()

            msgOk = QMessageBox(self)
            msgOk.setIcon(QMessageBox.Information)
            msgOk.setWindowTitle("Reporte Generado")
            msgOk.setText(f"El reporte PDF se ha guardado correctamente en:\n{nombre_archivo}")
            msgOk.setStyleSheet(estiloWarning)
            msgOk.exec()

        except Exception as e:
            msgError = QMessageBox(self)
            msgError.setIcon(QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText(f"Hubo un error al generar el PDF:\n{str(e)}")
            msgError.setStyleSheet(estiloWarning)
            msgError.exec()

    # ─────────────────────────────────────────
    @staticmethod
    def reporte_tiempo_reverberacion(self, resultados):
        """
        Genera reporte completo RT60 + opcionalmente %ALCONS.
        Mantiene la firma original del método.
        """
        nombre_archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Reporte PDF", os.getenv('HOME', '/'), "Archivos PDF (*.pdf)"
        )
        if not nombre_archivo:
            return

        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        subtitulo = _subtitulo_reporte(resultados.get("salon", {}))
        total = _contar_paginas(lambda d: _dibujar_reporte_rt(d, resultados), fecha_hora, subtitulo)
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        doc = _Doc(c, fecha_hora, total, subtitulo)
        _dibujar_reporte_rt(doc, resultados)
        doc.cerrar()

        c.save()
