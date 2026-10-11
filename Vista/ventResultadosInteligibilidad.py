"""
Pantalla de resultados de Inteligibilidad del Habla (%ALCons).

Reemplaza el QMessageBox que mostraba antes
VentanaInteligibiliad.mostrar_resumen_reporte (bloque M2-UX, ver
docs/CHANGELOG.md y la auditoría UX/UI del Módulo 2). Reutiliza el mismo
lenguaje visual que VentanaGraficaRT (Módulo 1): estiloBarraSuperior,
estiloBotonAtras, estiloBarraInferior, estiloTarjeta y estiloTexto de
Recursos/estilos/estilo.py; sin estilos paralelos nuevos.

La escala de 6 niveles se toma directamente de
Datos.utils.reportePDF.NIVELES_ALCONS (la misma que usa el PDF ya
aprobado), para que esta pantalla y el PDF no puedan desincronizarse si la
clasificación operativa (D-019, docs/DECISIONS.md) cambia en el futuro.
"""

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton,
    QScrollArea, QSizePolicy,
)

from Datos.utils.reportePDF import ReportePDF, NIVELES_ALCONS, _nivel_alcons
from Recursos.estilos import paleta, tipografia
from Recursos.estilos.estilo import (
    estiloBotonAtras, estiloBarraSuperior, estiloBarraInferior,
    estiloTarjeta, estiloTexto,
)

_ICONO_INTELIGIBILIDAD = "../Recursos/iconos/terapia-musical.png"
_ANCHO_MAXIMO_TARJETA = 640

# Unidad y decimales por parámetro de "Detalles" (mismo criterio visual que
# Datos/utils/reportePDF.py::_FORMATO_PARAMETROS, para que la cifra se vea
# igual aquí y en el PDF; claves tal como las devuelve
# Modelo/alcons2.py::AlconsCalculator.generar_reporte).
_FORMATO_DETALLE = {
    "Distancia al oyente":            ("m", 2),
    "Tiempo de Reverberación":        ("s", 2),
    "Volumen de la sala":             ("m³", 2),
    "Factor de Directividad":         ("", 1),
    "Superficie Total":               ("m²", 2),
    "Coeficiente Medio de Absorción": ("", 3),
}


def _hex(rgb_float):
    """Convierte un color (r, g, b) en floats 0-1 (formato ReportLab/NIVELES_ALCONS) a '#rrggbb'."""
    r, g, b = rgb_float
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


def _num(valor, decimales=2, unidad=""):
    try:
        texto = f"{float(valor):.{decimales}f}"
    except (TypeError, ValueError):
        return str(valor)
    return f"{texto} {unidad}" if unidad else texto


class VentanaResultadosInteligibilidad(QWidget):
    """Pantalla de resultados de %ALCons, construida en Python puro (sin
    `.ui` nuevo), con el mismo criterio que VentanaGraficaRT."""

    def __init__(self, stacked_widget, indice_anterior, reporte, parent=None):
        super().__init__(parent)
        self.stacked_widget = stacked_widget
        self.indice_anterior = indice_anterior
        self.reporte = reporte

        # Mismo degradado de fondo que el resto de pantallas del flujo.
        self.setStyleSheet(
            "QWidget { background-color: qlineargradient("
            "spread:pad, x1:0.488, y1:0, x2:0.495, y2:1,"
            "stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255)); }"
            "QFrame { background-color: transparent; }"
        )

        layout_general = QVBoxLayout(self)
        layout_general.setContentsMargins(0, 0, 0, 0)
        layout_general.setSpacing(0)

        layout_general.addWidget(self._crear_cabecera())
        layout_general.addWidget(self._crear_contenido(), 1)
        layout_general.addWidget(self._crear_pie())

        self.setup_events()

    # ── Helpers de construcción (mismo patrón que VentanaGraficaRT) ─────

    @staticmethod
    def _tarjeta(nombre, layout_cls=QVBoxLayout, margenes=(16, 14, 16, 16), espaciado=10, **estilo):
        frame = QFrame()
        frame.setObjectName(nombre)
        frame.setStyleSheet(estiloTarjeta(nombre, **estilo))
        layout = layout_cls(frame)
        layout.setContentsMargins(*margenes)
        layout.setSpacing(espaciado)
        return frame, layout

    @staticmethod
    def _etiqueta(texto, tamano_pt, color=paleta.TEXTO_PRINCIPAL, negrita=False):
        lbl = QLabel(texto)
        lbl.setStyleSheet(estiloTexto(tamano_pt, color, negrita))
        lbl.setWordWrap(True)
        return lbl

    @staticmethod
    def _separador():
        linea = QFrame()
        linea.setFixedHeight(1)
        linea.setStyleSheet("QFrame { background-color: rgba(255,255,255,0.10); border: none; }")
        return linea

    def _fila_parametro(self, etiqueta, valor):
        fila = QHBoxLayout()
        fila.setSpacing(8)
        lbl = self._etiqueta(etiqueta, tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO)
        val = self._etiqueta(valor, tipografia.CUERPO, "white", negrita=True)
        val.setWordWrap(False)
        val.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        fila.addWidget(lbl, 1)
        fila.addWidget(val)
        return fila

    # ── Cabecera ──────────────────────────────────────────────────────

    def _crear_cabecera(self):
        frame = QFrame()
        frame.setObjectName("frameTop")
        frame.setStyleSheet(estiloBarraSuperior("frameTop"))
        frame.setMinimumHeight(72)
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(12, 8, 12, 8)

        self.botonAtras = QPushButton()
        self.botonAtras.setObjectName("botonAtras")
        self.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))
        self.botonAtras.setMinimumSize(QSize(42, 42))
        self.botonAtras.setMaximumSize(QSize(42, 42))
        self.botonAtras.setIconSize(QSize(22, 22))
        self.botonAtras.setStyleSheet(estiloBotonAtras)
        self.botonAtras.setToolTip("Volver al formulario")
        lay.addWidget(self.botonAtras)
        lay.addStretch(1)

        titulo = QLabel()
        titulo.setStyleSheet("QLabel { background: transparent; border: none; }")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setText(
            '<html><body><p align="center">'
            f'<span style="font-size:{tipografia.TITULO_PANTALLA}pt; font-weight:700; color:#ffffff;">'
            # Mismo título que VentanaGraficaRT ("Resultados del análisis";
            # ventGraficaRT.py), el subtítulo distingue el módulo — evita
            # que un título más largo desborde en ventanas angostas.
            'Resultados del análisis</span><br>'
            f'<span style="font-size:{tipografia.AUXILIAR}pt; color:{paleta.TEXTO_SECUNDARIO};">'
            'Inteligibilidad del Habla · %ALCONS (Peutz)</span></p></body></html>'
        )
        lay.addWidget(titulo)
        lay.addStretch(1)

        # Espaciador invisible del mismo ancho que "Atrás", para que el
        # título quede centrado respecto al ancho total de la barra.
        equilibrio = QWidget()
        equilibrio.setFixedSize(42, 42)
        lay.addWidget(equilibrio)

        return frame

    # ── Contenido ─────────────────────────────────────────────────────

    def _crear_contenido(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")

        contenedor = QWidget()
        contenedor.setStyleSheet("QWidget { background: transparent; }")
        fila_centrado = QHBoxLayout(contenedor)
        fila_centrado.setContentsMargins(16, 20, 16, 20)

        tarjeta, lay_tarjeta = self._tarjeta(
            "tarjetaResultadoIH", margenes=(20, 18, 20, 20), espaciado=14)
        tarjeta.setMaximumWidth(_ANCHO_MAXIMO_TARJETA)
        tarjeta.setMinimumWidth(320)
        tarjeta.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self._construir_resultado_principal(lay_tarjeta)
        lay_tarjeta.addWidget(self._separador())
        self._construir_escala(lay_tarjeta)
        lay_tarjeta.addWidget(self._separador())
        self._construir_parametros(lay_tarjeta)

        fila_centrado.addStretch(1)
        fila_centrado.addWidget(tarjeta)
        fila_centrado.addStretch(1)

        scroll.setWidget(contenedor)
        return scroll

    def _construir_resultado_principal(self, layout):
        # Icono de módulo + título de sección (mismo patrón que RT).
        cab = QHBoxLayout()
        cab.setSpacing(8)
        lbl_icono = QLabel()
        lbl_icono.setStyleSheet("QLabel { background: transparent; border: none; }")
        lbl_icono.setPixmap(QIcon(_ICONO_INTELIGIBILIDAD).pixmap(QSize(20, 20)))
        lbl_titulo = self._etiqueta("Inteligibilidad del Habla", tipografia.SUBTITULO, "white", negrita=True)
        lbl_titulo.setWordWrap(False)
        cab.addWidget(lbl_icono)
        cab.addWidget(lbl_titulo, 1)
        layout.addLayout(cab)

        alcons_val = float(self.reporte["%ALCONS"])
        evaluacion = str(self.reporte["Evaluación"]).strip()
        categoria, _, detalle = evaluacion.partition(":")
        categoria = categoria.strip()
        detalle = detalle.strip()

        idx = _nivel_alcons(alcons_val)
        _, rgb, nombre_nivel, _rango = NIVELES_ALCONS[idx]
        self._color_nivel = _hex(rgb)

        valor = self._etiqueta(f"{alcons_val:.2f} %", 32, self._color_nivel, negrita=True)
        valor.setAlignment(Qt.AlignCenter)
        valor.setWordWrap(False)
        layout.addWidget(valor)

        nombre = self._etiqueta(categoria or nombre_nivel, tipografia.TITULO, self._color_nivel, negrita=True)
        nombre.setAlignment(Qt.AlignCenter)
        layout.addWidget(nombre)

        if detalle:
            desc = self._etiqueta(detalle, tipografia.CUERPO, paleta.TEXTO_SECUNDARIO)
            desc.setAlignment(Qt.AlignCenter)
            layout.addWidget(desc)

    def _construir_escala(self, layout):
        layout.addWidget(self._etiqueta(
            "Escala %ALCONS (6 niveles)", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))

        alcons_val = float(self.reporte["%ALCONS"])
        idx_activo = _nivel_alcons(alcons_val)

        fila = QHBoxLayout()
        fila.setSpacing(3)
        nombres = QHBoxLayout()
        nombres.setSpacing(3)

        for i, (_limite, rgb, nombre_nivel, _rango) in enumerate(NIVELES_ALCONS):
            color = _hex(rgb)
            activo = i == idx_activo
            seg = QFrame()
            seg.setFixedHeight(28)
            seg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            if activo:
                seg.setStyleSheet(
                    f"QFrame {{ background-color: {color}; border-radius: 4px; "
                    f"border: 1px solid white; }}"
                )
                seg_lay = QVBoxLayout(seg)
                seg_lay.setContentsMargins(0, 0, 0, 0)
                valor_lbl = QLabel(f"{alcons_val:.1f}%")
                valor_lbl.setAlignment(Qt.AlignCenter)
                valor_lbl.setStyleSheet(
                    "QLabel { color: white; font-weight: bold; font-size: 8pt; "
                    "background: transparent; border: none; }"
                )
                seg_lay.addWidget(valor_lbl)
            else:
                # QSS no soporta `opacity` sobre QFrame; se atenúa mezclando
                # el color del nivel con el fondo oscuro de la pantalla.
                seg.setStyleSheet(
                    f"QFrame {{ background-color: {self._atenuar(color)}; border-radius: 4px; }}"
                )
            fila.addWidget(seg)

            lbl_nombre = QLabel(nombre_nivel)
            lbl_nombre.setAlignment(Qt.AlignCenter)
            lbl_nombre.setStyleSheet(
                f"QLabel {{ color: {'white' if activo else paleta.TEXTO_SECUNDARIO}; "
                f"font-size: 7pt; font-weight: {'bold' if activo else 'normal'}; "
                f"background: transparent; border: none; }}"
            )
            nombres.addWidget(lbl_nombre)

        layout.addLayout(fila)
        layout.addLayout(nombres)

    @staticmethod
    def _atenuar(color_hex, fondo=(0, 0, 45), factor=0.35):
        """Mezcla `color_hex` con el fondo oscuro de la pantalla, para los
        segmentos no activos de la escala (atenuados sin usar `opacity`,
        que QSS no soporta sobre QFrame)."""
        h = color_hex.lstrip("#")
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        fr, fg, fb = fondo
        mezcla = lambda c, f: round(c * factor + f * (1 - factor))
        return "#%02x%02x%02x" % (mezcla(r, fr), mezcla(g, fg), mezcla(b, fb))

    def _construir_parametros(self, layout):
        layout.addWidget(self._etiqueta(
            "Parámetros utilizados", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO, negrita=True))

        detalles = self.reporte.get("Detalles", {})
        for clave, valor in detalles.items():
            unidad, decimales = _FORMATO_DETALLE.get(clave, ("", 2))
            texto_valor = _num(valor, decimales, unidad) if isinstance(valor, (int, float)) else str(valor)
            layout.addLayout(self._fila_parametro(clave, texto_valor))

        layout.addWidget(self._separador())
        layout.addWidget(self._etiqueta(
            "Resultado acústico", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO, negrita=True))
        layout.addLayout(self._fila_parametro(
            "Distancia crítica (Dc)", _num(self.reporte.get("Distancia Crítica (Dc)", 0), 2, "m")))
        layout.addLayout(self._fila_parametro(
            "Constante del recinto (R)", _num(self.reporte.get("Constante del Recinto (R)", 0), 2, "m²")))

    # ── Pie ───────────────────────────────────────────────────────────

    def _crear_pie(self):
        frame = QFrame()
        frame.setObjectName("frameBottom")
        frame.setMinimumHeight(64)
        frame.setStyleSheet(estiloBarraInferior("frameBottom", "botonGuardarPDF"))
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(16, 8, 16, 8)
        lay.setSpacing(12)
        lay.addStretch(1)

        self.botonGoHome = QPushButton("Ir al Inicio")
        self.botonGoHome.setObjectName("botonGoHome")
        self.botonGoHome.setToolTip("Volver a la pantalla principal")
        lay.addWidget(self.botonGoHome)

        self.botonGuardarPDF = QPushButton("Guardar Reporte PDF")
        self.botonGuardarPDF.setObjectName("botonGuardarPDF")
        self.botonGuardarPDF.setToolTip("Guardar este resultado en un archivo PDF")
        lay.addWidget(self.botonGuardarPDF)

        return frame

    # ── Eventos / navegación ─────────────────────────────────────────

    def setup_events(self):
        self.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)
        self.botonGoHome.clicked.connect(self.ir_ventana_home)
        self.botonGuardarPDF.clicked.connect(self.guardar_pdf)

    def regresar_a_ventana_anterior(self):
        if self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)

    def ir_ventana_home(self):
        if self.stacked_widget:
            self.stacked_widget.setCurrentIndex(0)

    def guardar_pdf(self):
        ReportePDF.reporte_inteligibiliad(self, self.reporte)
