from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QFileDialog, QMessageBox
import os
from datetime import datetime

from Recursos.estilos.estilo import estiloWarning

# ─────────────────────────────────────────────
#  PALETA DE COLORES DEL PROYECTO
# ─────────────────────────────────────────────
COLOR_PRIMARIO      = (0.00, 0.27, 0.55)   # Azul UA  (#00458C)
COLOR_SECUNDARIO    = (0.87, 0.44, 0.10)   # Naranja UA (#DE7019)
COLOR_FONDO_HEADER  = (0.94, 0.96, 0.99)   # Azul muy claro
COLOR_FONDO_TABLA_H = (0.00, 0.27, 0.55)   # Azul para encabezado de tabla
COLOR_FILA_PAR      = (0.95, 0.97, 1.00)
COLOR_FILA_IMPAR    = (1.00, 1.00, 1.00)
COLOR_VERDE         = (0.13, 0.62, 0.30)
COLOR_ROJO          = (0.82, 0.11, 0.11)
COLOR_AMARILLO_BORDE= (0.70, 0.50, 0.10)
COLOR_FONDO_CONCLU  = (0.95, 0.95, 0.85)

MARGEN = inch


# ─────────────────────────────────────────────
#  HELPERS VISUALES
# ─────────────────────────────────────────────

def _marca_agua(c, width, height, logo_path):
    """Añade isotipo UA como marca de agua centrada y muy tenue."""
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


def _header(c, width, height, titulo_pagina: str, fecha_hora: str, logo_path: str = None):
    """
    Banda superior con color primario, título de página y fecha.
    Opcionalmente coloca el logo de la UA a la derecha.
    """
    band_h = 42
    band_y = height - band_h

    # Fondo de banda
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.rect(0, band_y, width, band_h, fill=True, stroke=False)

    # Título de la página
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(MARGEN, band_y + 14, titulo_pagina)

    # Fecha (derecha)
    c.setFont("Helvetica-Oblique", 8)
    c.drawRightString(width - MARGEN, band_y + 14, f"Generado: {fecha_hora}")

    # Logo (si existe)
    if logo_path:
        try:
            img = ImageReader(logo_path)
            c.drawImage(img, width - MARGEN - 36, band_y + 4,
                        width=32, height=32, mask='auto')
        except Exception:
            pass


def _footer(c, width, numero_pagina: int, total_paginas: int):
    """Línea inferior con número de página."""
    c.setStrokeColorRGB(*COLOR_SECUNDARIO)
    c.setLineWidth(0.8)
    c.line(MARGEN, 30, width - MARGEN, 30)
    c.setFont("Helvetica", 8)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.drawCentredString(width / 2, 18,
                        f"Software de Evaluacion Acustica — Universidad del Atlantico  |  Pagina {numero_pagina} de {total_paginas}")


def _seccion_titulo(c, x, y, texto: str, ancho: int = 480):
    """Encabezado de sección con línea de acento naranja."""
    c.setFillColorRGB(*COLOR_SECUNDARIO)
    c.rect(x, y - 2, 4, 18, fill=True, stroke=False)
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x + 10, y, texto)
    c.setStrokeColorRGB(0.85, 0.85, 0.85)
    c.setLineWidth(0.5)
    c.line(x, y - 6, x + ancho, y - 6)


def _mini_card(c, x, y, etiqueta: str, valor: str, ancho: float = 130, alto: float = 46):
    """Card compacto con etiqueta arriba y valor abajo."""
    # Sombra suave
    c.setFillColorRGB(0.88, 0.88, 0.88)
    c.roundRect(x + 2, y - 2, ancho, alto, 6, fill=True, stroke=False)
    # Fondo blanco
    c.setFillColor(colors.white)
    c.roundRect(x, y, ancho, alto, 6, fill=True, stroke=False)
    # Borde
    c.setStrokeColorRGB(*COLOR_PRIMARIO)
    c.setLineWidth(0.8)
    c.roundRect(x, y, ancho, alto, 6, fill=False, stroke=True)
    # Etiqueta
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.setFont("Helvetica", 8)
    c.drawCentredString(x + ancho / 2, y + alto - 14, etiqueta)
    # Valor
    c.setFillColorRGB(*COLOR_PRIMARIO)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(x + ancho / 2, y + 12, valor)


def _semaforo(c, x, y, es_optimo: bool, radio: float = 9):
    """Círculo semáforo (verde/rojo) con texto de estado."""
    color = COLOR_VERDE if es_optimo else COLOR_ROJO
    texto = "OPTIMO" if es_optimo else "NO OPTIMO"
    c.setFillColorRGB(*color)
    c.circle(x + radio, y + radio, radio, fill=True, stroke=False)
    c.setFillColorRGB(*color)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x + radio * 2 + 8, y + 5, texto)


def _barra_nivel(c, x, y, porcentaje: float, ancho: float = 340, alto: float = 18):
    """
    Barra de progreso de 5 niveles para %ALCons.
    0-2%: Excelente (verde oscuro)
    2-5%: Buena (verde)
    5-10%: Regular (amarillo)
    10-15%: Pobre (naranja)
    >15%: Mala (rojo)
    """
    niveles = [
        (2,   (0.07, 0.53, 0.25), "Excelente"),
        (5,   (0.13, 0.72, 0.35), "Buena"),
        (10,  (0.93, 0.75, 0.08), "Regular"),
        (15,  (0.93, 0.48, 0.08), "Pobre"),
        (100, (0.82, 0.11, 0.11), "Mala"),
    ]

    # Fondo gris
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.roundRect(x, y, ancho, alto, alto / 2, fill=True, stroke=False)

    # Determinar color y ancho de relleno
    fill_color = (0.82, 0.11, 0.11)
    for limite, color, _ in niveles:
        if porcentaje <= limite:
            fill_color = color
            break

    fill_w = min(porcentaje / 20, 1.0) * ancho   # escala hasta 20% = 100%
    c.setFillColorRGB(*fill_color)
    c.roundRect(x, y, fill_w, alto, alto / 2, fill=True, stroke=False)

    # Etiquetas de escala
    c.setFont("Helvetica", 7)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    for lim, _, lab in niveles[:-1]:
        lx = x + (lim / 20) * ancho
        c.setStrokeColorRGB(0.7, 0.7, 0.7)
        c.setLineWidth(0.5)
        c.line(lx, y - 2, lx, y + alto + 2)
        c.drawCentredString(lx, y - 10, f"{lim}%")


def _tabla_rt(c, x, y, frecuencias, sabine, eyring, col_width, row_height):
    """Tabla de RT60 con encabezado coloreado y filas alternas."""
    encabezados = ["Frecuencia (Hz)", "Sabine RT60 (s)", "Eyring RT60 (s)"]
    n_cols = len(encabezados)

    # Encabezado
    c.setFont("Helvetica-Bold", 9)
    for i, texto in enumerate(encabezados):
        cx = x + i * col_width
        c.setFillColorRGB(*COLOR_FONDO_TABLA_H)
        c.rect(cx, y - row_height, col_width, row_height, fill=True, stroke=False)
        c.setFillColor(colors.white)
        c.drawCentredString(cx + col_width / 2, y - row_height + 6, texto)

    # Borde exterior encabezado
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(0.4)
    c.rect(x, y - row_height, col_width * n_cols, row_height, fill=False, stroke=True)

    # Filas de datos
    c.setFont("Helvetica", 9)
    for fila_idx, f in enumerate(frecuencias):
        fy = y - (fila_idx + 2) * row_height
        bg = COLOR_FILA_PAR if fila_idx % 2 == 0 else COLOR_FILA_IMPAR
        valores = [str(f), f"{sabine[f]:.2f}", f"{eyring.get(f, 0):.2f}"]

        for col_idx, val in enumerate(valores):
            cx = x + col_idx * col_width
            c.setFillColorRGB(*bg)
            c.rect(cx, fy, col_width, row_height, fill=True, stroke=False)
            c.setStrokeColorRGB(0.85, 0.85, 0.85)
            c.setLineWidth(0.3)
            c.rect(cx, fy, col_width, row_height, fill=False, stroke=True)
            c.setFillColor(colors.black)
            # Resaltar frecuencias de referencia (500, 1000, 2000)
            if col_idx == 0 and f in (500, 1000, 2000):
                c.setFont("Helvetica-Bold", 9)
            else:
                c.setFont("Helvetica", 9)
            c.drawCentredString(cx + col_width / 2, fy + 6, val)

    return y - (len(frecuencias) + 2) * row_height


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
            fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            c = canvas.Canvas(nombre_archivo, pagesize=letter)
            width, height = letter
            LOGO = "../Recursos/iconos/isotipoUA.png"
            TOTAL_PAGINAS = 1

            # ── Página única: resultados %ALCONS ──
            _marca_agua(c, width, height, LOGO)
            _header(c, width, height, "Evaluacion de Inteligibilidad del Habla — %ALCONS",
                    fecha_hora, LOGO)
            _footer(c, width, 1, TOTAL_PAGINAS)

            y = height - MARGEN - 30

            # Título principal
            c.setFont("Helvetica-Bold", 16)
            c.setFillColorRGB(*COLOR_PRIMARIO)
            c.drawString(MARGEN, y, "Resultado de Inteligibilidad del Habla")
            y -= 8
            c.setStrokeColorRGB(*COLOR_SECUNDARIO)
            c.setLineWidth(2)
            c.line(MARGEN, y, MARGEN + 320, y)
            y -= 24

            # ── Cards de resultados principales ──
            alcons_val = float(reporte.get('%ALCONS', 0))
            evaluacion = str(reporte.get('Evaluacion', reporte.get('Evaluación', '')))
            # limpiar texto con cuadradito unicode
            evaluacion = evaluacion.replace('■ ', '').replace('■', '').strip()
            dc_val = reporte.get('Distancia Critica (Dc)', reporte.get('Distancia Crítica (Dc)', 'N/A'))
            r_val = reporte.get('Constante del Recinto (R)', 'N/A')

            _mini_card(c, MARGEN,       y - 46, "%ALCONS",         f"{alcons_val:.2f} %", 140, 52)
            _mini_card(c, MARGEN + 155, y - 46, "Dist. Critica (Dc)", f"{dc_val} m",          140, 52)
            _mini_card(c, MARGEN + 310, y - 46, "Constante R",      f"{r_val} m2",          140, 52)
            y -= 80

            # ── Barra de nivel ──
            _seccion_titulo(c, MARGEN, y, "Nivel de Inteligibilidad")
            y -= 30
            _barra_nivel(c, MARGEN, y, alcons_val, ancho=width - 2 * MARGEN - 20)
            y -= 36

            # Clasificación textual
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(*COLOR_PRIMARIO)
            c.drawString(MARGEN, y, f"Clasificacion:  {evaluacion}")
            y -= 28

            # ── Explicacion del parametro ──
            _seccion_titulo(c, MARGEN, y, "Que es el %ALCONS?")
            y -= 20
            explicacion = [
                "El %ALCONS (Porcentaje de Perdida de Articulacion de Consonantes) mide que tan bien",
                "se entiende la voz humana dentro de un espacio cerrado.",
                "",
                "Valores cercanos al 0% indican una excelente comprension del habla.",
                "Valores altos (>15%) indican que el oyente tiene dificultades para entender al hablante.",
                "",
                "Escala de referencia:",
                "   0 - 2%  : Excelente  — Comprension casi perfecta",
                "   2 - 5%  : Buena      — Ligeras perdidas, aceptable para aulas",
                "   5 - 10% : Regular    — Se notan dificultades de comprension",
                "  10 - 15% : Pobre      — Comunicacion claramente afectada",
                "  > 15%    : Mala       — Comunicacion muy deficiente",
            ]
            c.setFont("Helvetica", 10)
            c.setFillColorRGB(0.15, 0.15, 0.15)
            for linea in explicacion:
                c.drawString(MARGEN + 6, y, linea)
                y -= 15
            y -= 10

            # ── Detalles tecnicos ──
            _seccion_titulo(c, MARGEN, y, "Parametros utilizados en el calculo")
            y -= 22
            detalles = reporte.get("Detalles", {})
            c.setFont("Helvetica", 10)
            for clave, valor in detalles.items():
                c.setFillColorRGB(0.3, 0.3, 0.3)
                c.drawString(MARGEN + 10, y, f"•  {clave}:")
                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold", 10)
                c.drawString(MARGEN + 210, y, f"{round(float(valor), 3) if isinstance(valor, (int, float)) else valor}")
                c.setFont("Helvetica", 10)
                y -= 16

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

        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter
        LOGO = "../Recursos/iconos/isotipoUA.png"

        # ── Datos del salón ──
        salon            = resultados.get("salon", {})
        dimensiones      = salon.get("dimensiones", {})
        largo            = dimensiones.get("largo", "N/A")
        ancho            = dimensiones.get("ancho", "N/A")
        altura           = dimensiones.get("altura", "N/A")
        alcons           = resultados.get("reporte_inteligibilidad")
        materiales       = salon.get("materiales", {})
        objetos_adicionales = salon.get("objetos_adicionales") or []

        sabine     = resultados.get("sabine_rt", {})
        eyring     = resultados.get("eyring_rt", {})
        frecuencias = sorted(sabine.keys())

        alcons_present = alcons is not None
        TOTAL_PAGINAS  = 4 if alcons_present else 3

        # ════════════════════════════════════════
        #  PÁGINA 1 — Detalle del salón
        # ════════════════════════════════════════
        _marca_agua(c, width, height, LOGO)
        _header(c, width, height, "Resumen del Salon Evaluado", fecha_hora, LOGO)
        _footer(c, width, 1, TOTAL_PAGINAS)

        y = height - MARGEN - 30

        # Título
        c.setFont("Helvetica-Bold", 16)
        c.setFillColorRGB(*COLOR_PRIMARIO)
        c.drawString(MARGEN, y, "Ficha del Salon")
        y -= 6
        c.setStrokeColorRGB(*COLOR_SECUNDARIO)
        c.setLineWidth(2.5)
        c.line(MARGEN, y, MARGEN + 200, y)
        y -= 24

        # ── Cards de dimensiones ──
        _seccion_titulo(c, MARGEN, y, "Dimensiones")
        y -= 14

        # Calcular volumen
        try:
            vol = float(largo) * float(ancho) * float(altura)
            vol_str = f"{vol:.2f} m3"
        except Exception:
            vol_str = "N/A"

        card_w, card_h = 100, 52
        gap = 18
        cards_dim = [
            ("Largo", f"{largo} m"),
            ("Ancho", f"{ancho} m"),
            ("Altura", f"{altura} m"),
            ("Volumen", vol_str),
        ]
        cx_start = MARGEN
        for etiq, val in cards_dim:
            _mini_card(c, cx_start, y - card_h, etiq, val, card_w, card_h)
            cx_start += card_w + gap
        y -= card_h + 28

        # ── Tabla de materiales ──
        _seccion_titulo(c, MARGEN, y, "Materiales de las Superficies")
        y -= 18

        col_sup   = 90
        col_mat   = 200
        col_area  = 70
        col_obs   = 130
        row_h_tab = 18
        table_x   = MARGEN

        # Encabezado tabla materiales
        headers_mat = ["Superficie", "Material base", "Area (m2)", "Objetos adheridos"]
        widths_mat  = [col_sup, col_mat, col_area, col_obs]
        for i, (hdr, ww) in enumerate(zip(headers_mat, widths_mat)):
            hx = table_x + sum(widths_mat[:i])
            c.setFillColorRGB(*COLOR_FONDO_TABLA_H)
            c.rect(hx, y - row_h_tab, ww, row_h_tab, fill=True, stroke=False)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(hx + ww / 2, y - row_h_tab + 5, hdr)
        c.setStrokeColorRGB(0.75, 0.75, 0.75)
        c.setLineWidth(0.3)
        c.rect(table_x, y - row_h_tab, sum(widths_mat), row_h_tab, fill=False, stroke=True)
        y -= row_h_tab

        # Filas de materiales
        sup_nombres = {
            "frontal":   "Frontal",
            "trasera":   "Trasera",
            "izquierda": "Izquierda",
            "derecha":   "Derecha",
            "piso":      "Piso",
            "techo":     "Techo",
        }
        for idx, (sup_key, datos) in enumerate(materiales.items()):
            bg = COLOR_FILA_PAR if idx % 2 == 0 else COLOR_FILA_IMPAR
            mat    = datos.get("material", "N/A")
            area   = datos.get("area", "N/A")
            objetos = datos.get("objetos_adheridos") or []
            obj_texto = "; ".join([f"{o['nombre']} ({o['material']})" for o in objetos]) if objetos else "—"

            # Truncar material si es muy largo
            mat_disp = mat if len(mat) <= 28 else mat[:25] + "..."
            obj_disp = obj_texto if len(obj_texto) <= 22 else obj_texto[:19] + "..."

            sup_label = sup_nombres.get(sup_key.lower(), sup_key.capitalize())
            area_disp = f"{float(area):.2f}" if isinstance(area, (int, float)) else str(area)

            fila_vals = [sup_label, mat_disp, area_disp, obj_disp]
            fila_widths = widths_mat

            for ci, (val, ww) in enumerate(zip(fila_vals, fila_widths)):
                fx = table_x + sum(fila_widths[:ci])
                c.setFillColorRGB(*bg)
                c.rect(fx, y - row_h_tab, ww, row_h_tab, fill=True, stroke=False)
                c.setStrokeColorRGB(0.88, 0.88, 0.88)
                c.setLineWidth(0.3)
                c.rect(fx, y - row_h_tab, ww, row_h_tab, fill=False, stroke=True)
                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold" if ci == 0 else "Helvetica", 8)
                c.drawString(fx + 4, y - row_h_tab + 5, val)

            y -= row_h_tab

        y -= 14

        # ── Objetos adicionales ──
        if objetos_adicionales:
            _seccion_titulo(c, MARGEN, y, "Objetos Adicionales en el Salon")
            y -= 18

            headers_obj = ["Objeto", "Material", "Cantidad"]
            widths_obj  = [160, 200, 80]
            for i, (hdr, ww) in enumerate(zip(headers_obj, widths_obj)):
                hx = table_x + sum(widths_obj[:i])
                c.setFillColorRGB(*COLOR_FONDO_TABLA_H)
                c.rect(hx, y - row_h_tab, ww, row_h_tab, fill=True, stroke=False)
                c.setFillColor(colors.white)
                c.setFont("Helvetica-Bold", 8)
                c.drawCentredString(hx + ww / 2, y - row_h_tab + 5, hdr)
            c.setStrokeColorRGB(0.75, 0.75, 0.75)
            c.setLineWidth(0.3)
            c.rect(table_x, y - row_h_tab, sum(widths_obj), row_h_tab, fill=False, stroke=True)
            y -= row_h_tab

            for idx, obj in enumerate(objetos_adicionales):
                bg = COLOR_FILA_PAR if idx % 2 == 0 else COLOR_FILA_IMPAR
                nombre_obj   = obj.get("nombre", "N/A")
                material_obj = obj.get("material", "N/A")
                cantidad_obj = str(obj.get("cantidad", "N/A"))

                mat_disp = material_obj if len(material_obj) <= 30 else material_obj[:27] + "..."
                fila_vals = [nombre_obj, mat_disp, cantidad_obj]

                for ci, (val, ww) in enumerate(zip(fila_vals, widths_obj)):
                    fx = table_x + sum(widths_obj[:ci])
                    c.setFillColorRGB(*bg)
                    c.rect(fx, y - row_h_tab, ww, row_h_tab, fill=True, stroke=False)
                    c.setStrokeColorRGB(0.88, 0.88, 0.88)
                    c.setLineWidth(0.3)
                    c.rect(fx, y - row_h_tab, ww, row_h_tab, fill=False, stroke=True)
                    c.setFillColor(colors.black)
                    c.setFont("Helvetica", 8)
                    c.drawString(fx + 4, y - row_h_tab + 5, val)
                y -= row_h_tab

        c.showPage()

        # ════════════════════════════════════════
        #  PÁGINA 2 — Gráfica + Tabla RT60
        # ════════════════════════════════════════
        _marca_agua(c, width, height, LOGO)
        _header(c, width, height, "Tiempo de Reverberacion RT60 — Resultados", fecha_hora, LOGO)
        _footer(c, width, 2, TOTAL_PAGINAS)

        y = height - MARGEN - 20

        # Explicación breve antes de la gráfica
        _seccion_titulo(c, MARGEN, y, "Comparacion grafica: Sabine vs Eyring")
        y -= 16
        explicacion_rt = (
            "La grafica muestra el Tiempo de Reverberacion (RT60) calculado con dos metodos: Sabine (rojo) y Eyring (azul)."
            " Cada punto corresponde a una banda de frecuencia. La linea horizontal punteada roja indica el limite"
            " recomendado de 0.8 s segun la norma BB93 para aulas escolares."
        )
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColorRGB(0.35, 0.35, 0.35)
        # Wrap manual (cada ~110 caracteres)
        palabras = explicacion_rt.split()
        linea_actual = ""
        ey = y
        for p in palabras:
            prueba = linea_actual + (" " if linea_actual else "") + p
            if len(prueba) > 112:
                c.drawString(MARGEN + 4, ey, linea_actual)
                ey -= 12
                linea_actual = p
            else:
                linea_actual = prueba
        if linea_actual:
            c.drawString(MARGEN + 4, ey, linea_actual)
            ey -= 12
        y = ey - 8

        # Gráfica
        grafica = resultados.get("grafica")
        if grafica:
            grafica.seek(0)
            imagen = ImageReader(grafica)
            img_w, img_h = imagen.getSize()
            alt_img = 250
            escala  = alt_img / img_h
            anch_img = img_w * escala
            xi = (width - anch_img) / 2
            yi = y - alt_img
            c.drawImage(imagen, xi, yi, width=anch_img, height=alt_img)
            y = yi - 22
        else:
            y -= 10

        # ── Tabla de RT60 ──
        _seccion_titulo(c, MARGEN, y, "Tabla de Resultados Numericos")
        y -= 18

        nota_frec = (
            "Nota: las frecuencias resaltadas (500, 1000 y 2000 Hz) son las de referencia para el calculo del Tr MID."
        )
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        c.drawString(MARGEN + 4, y, nota_frec)
        y -= 14

        col_w   = (width - 2 * MARGEN) / 3
        row_h_t = 20
        _tabla_rt(c, MARGEN, y, frecuencias, sabine, eyring, col_w, row_h_t)

        c.showPage()

        # ════════════════════════════════════════
        #  PÁGINA 3 — Interpretación RT60
        # ════════════════════════════════════════
        _marca_agua(c, width, height, LOGO)
        _header(c, width, height, "Interpretacion del Tiempo de Reverberacion", fecha_hora, LOGO)
        _footer(c, width, 3, TOTAL_PAGINAS)

        y = height - MARGEN - 30

        # Título
        c.setFont("Helvetica-Bold", 16)
        c.setFillColorRGB(*COLOR_PRIMARIO)
        c.drawString(MARGEN, y, "Analisis Acustico — Tiempo de Reverberacion")
        y -= 6
        c.setStrokeColorRGB(*COLOR_SECUNDARIO)
        c.setLineWidth(2.5)
        c.line(MARGEN, y, MARGEN + 350, y)
        y -= 24

        # Calcular TrMID
        sabine_mid = [sabine[f] for f in [500, 1000, 2000] if f in sabine]
        eyring_mid = [eyring[f] for f in [500, 1000, 2000] if f in eyring]
        trmid_sabine = sum(sabine_mid) / len(sabine_mid) if sabine_mid else 0
        trmid_eyring = sum(eyring_mid) / len(eyring_mid) if eyring_mid else 0
        es_optimo    = trmid_sabine <= 0.8 and trmid_eyring <= 0.8

        # ── Cards Tr MID ──
        _seccion_titulo(c, MARGEN, y, "Tr MID — Tiempo de Reverberacion Medio (500, 1000 y 2000 Hz)")
        y -= 16

        _mini_card(c, MARGEN,       y - 52, "Tr MID Sabine", f"{trmid_sabine:.2f} s", 155, 56)
        _mini_card(c, MARGEN + 172, y - 52, "Tr MID Eyring", f"{trmid_eyring:.2f} s", 155, 56)
        _mini_card(c, MARGEN + 344, y - 52, "Limite BB93",   "0.80 s",               130, 56)
        y -= 80

        # ── Indicador semáforo ──
        _seccion_titulo(c, MARGEN, y, "Evaluacion de la Condicion Acustica")
        y -= 28
        _semaforo(c, MARGEN + 4, y, es_optimo, radio=11)
        y -= 30

        # ── Explicación Tr MID ──
        _seccion_titulo(c, MARGEN, y, "Como interpretar estos resultados")
        y -= 16
        explicacion_trmid = [
            "El Tr MID es el promedio del tiempo de reverberacion a 500 Hz, 1000 Hz y 2000 Hz.",
            "Estas frecuencias son las mas relevantes para la comprension de la voz humana.",
            "",
            "Un Tr MID <= 0.8 s se considera OPTIMO para aulas segun la norma BB93 (Reino Unido),",
            "la cual es adoptada como referencia internacional en diseno acustico educativo.",
            "",
            "Si el Tr MID supera 0.8 s, las palabras del docente pueden solaparse entre si,",
            "dificultando la comprension y aumentando el esfuerzo auditivo de los estudiantes.",
        ]
        c.setFont("Helvetica", 10)
        c.setFillColorRGB(0.15, 0.15, 0.15)
        for linea in explicacion_trmid:
            c.drawString(MARGEN + 6, y, linea)
            y -= 15
        y -= 8

        # ── Box de conclusión ──
        conclusion_texto = (
            "La condicion acustica de este salon es OPTIMA. El Tr MID se encuentra dentro del\n"
            "rango recomendado (<= 0.8 s), lo que garantiza adecuada inteligibilidad del habla\n"
            "y confort auditivo para docentes y estudiantes."
        ) if es_optimo else (
            "La condicion acustica de este salon NO es OPTIMA. El Tr MID supera el limite de 0.8 s\n"
            "establecido por la norma BB93. Esto puede afectar la claridad del habla y reducir la\n"
            "calidad del entorno de aprendizaje. Se recomienda evaluar el uso de materiales absorbentes."
        )

        lineas_conclusion = conclusion_texto.split('\n')
        box_h = 22 + len(lineas_conclusion) * 16
        box_y = y - box_h - 6

        color_borde = COLOR_VERDE if es_optimo else COLOR_ROJO
        color_fondo = (0.93, 0.99, 0.94) if es_optimo else (0.99, 0.94, 0.94)

        c.setFillColorRGB(*color_fondo)
        c.roundRect(MARGEN, box_y, width - 2 * MARGEN, box_h, 8, fill=True, stroke=False)
        c.setStrokeColorRGB(*color_borde)
        c.setLineWidth(1.5)
        c.roundRect(MARGEN, box_y, width - 2 * MARGEN, box_h, 8, fill=False, stroke=True)

        # Franja de color en el lado izquierdo
        c.setFillColorRGB(*color_borde)
        c.roundRect(MARGEN, box_y, 5, box_h, 4, fill=True, stroke=False)

        c.setFont("Helvetica-Bold", 11)
        c.setFillColorRGB(*color_borde)
        c.drawString(MARGEN + 14, box_y + box_h - 16, "Conclusion:")

        c.setFont("Helvetica", 10)
        c.setFillColorRGB(0.1, 0.1, 0.1)
        ty = box_y + box_h - 32
        for linea in lineas_conclusion:
            c.drawString(MARGEN + 14, ty, linea.strip())
            ty -= 16

        c.showPage()

        # ════════════════════════════════════════
        #  PÁGINA 4 (opcional) — %ALCons
        # ════════════════════════════════════════
        if alcons_present:
            _marca_agua(c, width, height, LOGO)
            _header(c, width, height, "Inteligibilidad del Habla — %ALCONS", fecha_hora, LOGO)
            _footer(c, width, 4, TOTAL_PAGINAS)

            y = height - MARGEN - 30

            # Título
            c.setFont("Helvetica-Bold", 16)
            c.setFillColorRGB(*COLOR_PRIMARIO)
            c.drawString(MARGEN, y, "Evaluacion de la Inteligibilidad — %ALCONS")
            y -= 6
            c.setStrokeColorRGB(*COLOR_SECUNDARIO)
            c.setLineWidth(2.5)
            c.line(MARGEN, y, MARGEN + 340, y)
            y -= 24

            # ── Obtener valores ──
            alcons_val = float(alcons.get('%ALCONS', alcons.get('%ALCons', 0)))
            evaluacion = str(alcons.get('Evaluacion', alcons.get('Evaluación', '')))
            evaluacion = evaluacion.replace('■ ', '').replace('■', '').strip()
            dc_val = alcons.get('Distancia Critica (Dc)', alcons.get('Distancia Crítica (Dc)', 'N/A'))
            r_val  = alcons.get('Constante del Recinto (R)', 'N/A')

            # ── Cards ──
            _seccion_titulo(c, MARGEN, y, "Resultados Principales")
            y -= 16
            _mini_card(c, MARGEN,       y - 52, "%ALCONS",          f"{alcons_val:.2f} %", 140, 56)
            _mini_card(c, MARGEN + 158, y - 52, "Dist. Critica Dc",  f"{dc_val} m",         140, 56)
            _mini_card(c, MARGEN + 316, y - 52, "Constante R",       f"{r_val} m2",         140, 56)
            y -= 84

            # ── Barra de nivel ──
            _seccion_titulo(c, MARGEN, y, "Nivel de Inteligibilidad")
            y -= 30
            _barra_nivel(c, MARGEN, y, alcons_val, ancho=width - 2 * MARGEN - 20)
            y -= 40

            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(*COLOR_PRIMARIO)
            c.drawString(MARGEN, y, f"Clasificacion:  {evaluacion}")
            y -= 26

            # ── Explicación ──
            _seccion_titulo(c, MARGEN, y, "Que significa el %ALCONS?")
            y -= 16
            descripcion = [
                "El %ALCONS (Porcentaje de Perdida de Articulacion de Consonantes) indica",
                "que proporcion de las consonantes habladas se pierde antes de llegar al oyente.",
                "",
                "Las consonantes son las responsables de distinguir palabras como 'pero' de 'perro'",
                "o 'bala' de 'vala'. Si se pierden, el mensaje se vuelve confuso o incomprensible.",
                "",
                "Un %ALCONS bajo (cercano al 0%) significa que casi nada se pierde — excelente.",
                "Un %ALCONS alto (>15%) indica serias dificultades para entender al docente.",
            ]
            c.setFont("Helvetica", 10)
            c.setFillColorRGB(0.15, 0.15, 0.15)
            for linea in descripcion:
                c.drawString(MARGEN + 6, y, linea)
                y -= 15
            y -= 10

            # ── Detalles técnicos ──
            _seccion_titulo(c, MARGEN, y, "Parametros de Calculo")
            y -= 18
            detalles = alcons.get("Detalles", {})
            c.setFont("Helvetica", 10)
            for idx, (clave, valor) in enumerate(detalles.items()):
                bg = COLOR_FILA_PAR if idx % 2 == 0 else COLOR_FILA_IMPAR
                row_w = width - 2 * MARGEN
                c.setFillColorRGB(*bg)
                c.rect(MARGEN, y - 16, row_w, 16, fill=True, stroke=False)
                c.setFillColorRGB(0.3, 0.3, 0.3)
                c.drawString(MARGEN + 8, y - 12, f"{clave}:")
                val_str = f"{round(float(valor), 3)}" if isinstance(valor, (int, float)) else str(valor)
                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold", 10)
                c.drawString(MARGEN + 230, y - 12, val_str)
                c.setFont("Helvetica", 10)
                y -= 18

            c.showPage()

        c.save()