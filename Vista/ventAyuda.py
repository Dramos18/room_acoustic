"""
Pantalla de Ayuda del Inicio (botón `botonAyuda`, antes sin conectar a
nada; ver auditoría en docs/UI_INVENTORY.md). Construida en Python puro
(sin `.ui` nuevo), mismo criterio que VentanaGraficaRT /
VentanaResultadosInteligibilidad: cabecera (estiloBarraSuperior),
contenido con QScrollArea, pie (estiloBarraInferior).

Decisión técnica (Python vs. Qt Designer) tomada comparando ambas
alternativas, no por costumbre: Ayuda necesita 6 páginas internas con un
`QStackedWidget` propio, una grilla que cambia de 3 a 1 columnas y un
stepper que cambia de horizontal a vertical según el ancho disponible —
lógica de layout en tiempo de ejecución que un `.ui` no puede expresar
por sí solo (terminaría igual en Python). Un `.ui` nuevo añadiría además
el riesgo ya documentado en D-011 (`pyside6-uic` 6.11.2 del entorno
frente a 6.5.2 con el que se generaron los `.ui` existentes) sin ningún
beneficio real, porque no hay formularios ni combos que Qt Designer
resuelva mejor que el código.

Segunda iteración de diseño (tras auditoría visual con capturas reales,
ver conversación): la primera versión navegaba correctamente pero se
veía como una lista de tarjetas y párrafos con demasiado espacio vacío.
Esta versión reutiliza el lenguaje visual real más refinado de la app
—los mosaicos de acento lateral de VentanaGraficaRT (`_tile_trmid`), no
`estiloTarjeta` plano—, acota el ancho del contenido, lo centra
vertical y horizontalmente, y reemplaza los bloques de texto de cada
módulo por un único componente de flujo (Entrada → Procesamiento →
Resultado) reutilizado en Tiempo de Reverberación, Inteligibilidad,
Base de Datos y Resultados/PDF.

El contenido (qué pide/devuelve cada módulo, los 6 niveles de %ALCons)
se apoya en docs/REQUIREMENTS.md y reutiliza
Datos.utils.reportePDF.NIVELES_ALCONS como única fuente de los nombres y
colores de la clasificación D-019, para no duplicar esos valores aquí.
No se usa `logoBN.png` como icono de Base de Datos (se ve ilegible a
tamaño de icono pequeño, ya señalado en docs/RESOURCES.md/UI_INVENTORY.md
para "Iniciar análisis"): esa sección y "Cómo empezar", "Resultados y
PDF" y "Acerca del proyecto" quedan sin icono, mismo criterio de D-013
(no forzar un icono que no representa bien la entidad).
"""

from PySide6.QtCore import Qt, QSize, QRect, QPoint, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton,
    QScrollArea, QSizePolicy, QLayout, QGridLayout, QStackedWidget,
)

from Datos.utils.reportePDF import NIVELES_ALCONS
from Recursos.estilos import paleta, tipografia
from Recursos.estilos.estilo import (
    estiloBotonAtras, estiloBarraSuperior, estiloBarraInferior, estiloTexto,
)

_ANCHO_MAX_CONTENIDO = 1040  # ancho máximo del contenido, centrado (desktop)
_ANCHO_GRID_3COL = 980   # >= esto: 3 columnas en el menú
_ANCHO_GRID_2COL = 640   # >= esto: 2 columnas; si no, 1
_ANCHO_FLUJO_HORIZONTAL = 560  # ancho propio del componente de flujo


def _hex(rgb_float):
    """(r, g, b) en floats 0-1 (formato de NIVELES_ALCONS) -> '#rrggbb'."""
    r, g, b = rgb_float
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


# ─────────────────────────────────────────────────────────────
#  Flow layout — envuelve chips cortos ("Dimensiones", "Materiales", ...)
#  a una segunda fila cuando no caben, en vez de forzar scroll horizontal
#  a 500 px. Receta estándar de Qt (Qt Flow Layout Example).
# ─────────────────────────────────────────────────────────────
class _FlowLayout(QLayout):
    def __init__(self, parent=None, spacing=8):
        super().__init__(parent)
        self.setSpacing(spacing)
        self._items = []

    def addItem(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        return self._items[index] if 0 <= index < len(self._items) else None

    def takeAt(self, index):
        return self._items.pop(index) if 0 <= index < len(self._items) else None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self._hacer_layout(QRect(0, 0, width, 0), test_only=True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._hacer_layout(rect, test_only=False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        m = self.contentsMargins()
        return size + QSize(m.left() + m.right(), m.top() + m.bottom())

    def _hacer_layout(self, rect, test_only):
        m = self.contentsMargins()
        efectivo = rect.adjusted(m.left(), m.top(), -m.right(), -m.bottom())
        x, y = efectivo.x(), efectivo.y()
        alto_fila = 0
        espacio = self.spacing()
        for item in self._items:
            siguiente_x = x + item.sizeHint().width() + espacio
            if siguiente_x - espacio > efectivo.right() and alto_fila > 0:
                x = efectivo.x()
                y += alto_fila + espacio
                siguiente_x = x + item.sizeHint().width() + espacio
                alto_fila = 0
            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))
            x = siguiente_x
            alto_fila = max(alto_fila, item.sizeHint().height())
        return y + alto_fila - rect.y() + m.bottom()


def _chip(texto):
    lbl = QLabel(texto)
    lbl.setStyleSheet(
        "QLabel { background-color: rgba(126,200,247,0.14); "
        f"border: 1px solid rgba(126,200,247,0.45); border-radius: 12px; "
        f"padding: 5px 12px; color: {paleta.ACENTO}; "
        f"font-size: {tipografia.AUXILIAR}pt; font-weight: 600; }}"
    )
    return lbl


def _fila_chips(textos):
    cont = QWidget()
    flujo = _FlowLayout(cont, spacing=8)
    for t in textos:
        flujo.addWidget(_chip(t))
    return cont


def _etiqueta(texto, tamano_pt, color=paleta.TEXTO_PRINCIPAL, negrita=False, centrado=False):
    lbl = QLabel(texto)
    lbl.setStyleSheet(estiloTexto(tamano_pt, color, negrita))
    lbl.setWordWrap(True)
    if centrado:
        lbl.setAlignment(Qt.AlignCenter)
    return lbl


def _separador():
    linea = QFrame()
    linea.setFixedHeight(1)
    linea.setStyleSheet("QFrame { background-color: rgba(255,255,255,0.10); border: none; }")
    return linea


def _mosaico_acento(nombre, titulo, color_acento, contenido=None, texto_valor=None):
    """
    Mosaico con borde de acento izquierdo — el lenguaje visual real más
    refinado de la app (ver `_tile_trmid` en Vista/ventGraficaRT.py),
    reutilizado aquí en vez de `estiloTarjeta` plano. `contenido`: widget
    opcional debajo del título (p. ej. una fila de chips); `texto_valor`:
    cifra/label corta en vez de contenido libre.
    """
    tile = QFrame()
    tile.setObjectName(nombre)
    tile.setStyleSheet(
        f"QFrame#{nombre} {{ background-color: rgba(255,255,255,0.05); border: none; "
        f"border-left: 3px solid {color_acento}; border-radius: 4px; }}"
    )
    lay = QVBoxLayout(tile)
    lay.setContentsMargins(14, 10, 14, 10)
    lay.setSpacing(4)
    lay.addWidget(_etiqueta(titulo, tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO, negrita=True))
    if texto_valor is not None:
        lay.addWidget(_etiqueta(texto_valor, tipografia.CUERPO, "white", negrita=True))
    if contenido is not None:
        lay.addWidget(contenido)
    return tile


# ─────────────────────────────────────────────────────────────
#  Tarjeta clicable del menú — jerarquía: insignia opcional (icono en
#  círculo) + título + descripción + flecha de navegación. Tres estados
#  reales (normal / hover / pressed), altura fija para que la grilla se
#  vea alineada tenga o no icono.
# ─────────────────────────────────────────────────────────────
_ALTO_TARJETA_TEMA = 112


class _TarjetaTema(QFrame):
    clicked = Signal()

    def __init__(self, nombre, titulo, descripcion, icono=None, parent=None):
        super().__init__(parent)
        self.setObjectName(nombre)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(_ALTO_TARJETA_TEMA)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self._estilo_normal = self._estilo("rgba(255,255,255,0.055)", "rgba(255,255,255,0.14)")
        self._estilo_hover = self._estilo("rgba(255,255,255,0.09)", paleta.ACENTO)
        self._estilo_pressed = self._estilo("rgba(126,200,247,0.16)", paleta.ACENTO)
        self.setStyleSheet(self._estilo_normal)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(16, 14, 14, 14)
        lay.setSpacing(12)

        if icono:
            insignia = QFrame()
            insignia.setFixedSize(QSize(38, 38))
            insignia.setStyleSheet(
                "QFrame { background-color: rgba(126,200,247,0.14); "
                "border: 1px solid rgba(126,200,247,0.35); border-radius: 19px; }"
            )
            insignia_lay = QHBoxLayout(insignia)
            insignia_lay.setContentsMargins(0, 0, 0, 0)
            lbl_icono = QLabel()
            lbl_icono.setAlignment(Qt.AlignCenter)
            lbl_icono.setStyleSheet("QLabel { background: transparent; border: none; }")
            lbl_icono.setPixmap(QIcon(icono).pixmap(QSize(20, 20)))
            insignia_lay.addWidget(lbl_icono)
            lay.addWidget(insignia, 0, Qt.AlignVCenter)

        col_texto = QVBoxLayout()
        col_texto.setSpacing(3)
        lbl_titulo = _etiqueta(titulo, tipografia.SUBTITULO, "white", negrita=True)
        lbl_titulo.setWordWrap(False)
        col_texto.addWidget(lbl_titulo)
        col_texto.addWidget(_etiqueta(descripcion, tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        lay.addLayout(col_texto, 1)

        flecha = QLabel()
        flecha.setStyleSheet("QLabel { background: transparent; border: none; }")
        flecha.setPixmap(QIcon("../Recursos/iconos/angulo-derecho.png").pixmap(QSize(14, 14)))
        lay.addWidget(flecha, 0, Qt.AlignVCenter)

    @staticmethod
    def _estilo(fondo, borde):
        return (
            f"QFrame {{ background-color: {fondo}; border: 1px solid rgba(255,255,255,0.12); "
            f"border-left: 3px solid {borde}; border-radius: 8px; }}"
        )

    def enterEvent(self, event):
        self.setStyleSheet(self._estilo_hover)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self._estilo_normal)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setStyleSheet(self._estilo_pressed)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            dentro = self.rect().contains(event.position().toPoint())
            self.setStyleSheet(self._estilo_hover if dentro else self._estilo_normal)
            if dentro:
                self.clicked.emit()
        super().mouseReleaseEvent(event)


# ─────────────────────────────────────────────────────────────
#  Componente de flujo (Entrada → Procesamiento → Resultado) — se
#  reutiliza en Tiempo de Reverberación, Inteligibilidad, Base de Datos
#  y Resultados/PDF, para que las 4 páginas de módulo compartan una
#  misma composición en vez de bloques de texto distintos cada una.
#  Cambia de fila horizontal (con flechas "→") a columna vertical (con
#  flechas "↓") según el ancho real de contenido que VentanaAyuda le
#  informa (`fijar_ancho`) — NO según su propio `self.width()`: dentro
#  de un QScrollArea con `widgetResizable`, un widget puede terminar
#  más ancho que el viewport real (el scroll area deja crecer el
#  contenido en vez de forzarlo a encoger), así que medirse a sí mismo
#  llevaba a decidir "horizontal" con un ancho que en realidad no cabía
#  y producía scroll horizontal a 500 px. VentanaAyuda sí conoce el
#  ancho real disponible (el mismo que usa para la grilla del menú) y
#  se lo pasa directamente.
# ─────────────────────────────────────────────────────────────
class _FlujoEtapas(QWidget):
    def __init__(self, etapas, parent=None):
        """`etapas`: lista de (titulo_etapa, widget_contenido)."""
        super().__init__(parent)
        self._etapas = etapas
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._horizontal = None
        self._reconstruir(True)

    def fijar_ancho(self, ancho):
        # setMaximumWidth es una restricción dura que el motor de layout
        # de Qt siempre respeta; sin ella, aunque se reconstruya en modo
        # vertical, un QLabel con wordWrap dentro de una etapa puede
        # seguir pidiendo su ancho de una sola línea como sizeHint() y
        # terminar más ancho que `ancho` (el síntoma era overflow a
        # 500 px incluso con el stepper/flujo ya "en modo vertical").
        self.setMaximumWidth(ancho)
        self._reconstruir(ancho >= _ANCHO_FLUJO_HORIZONTAL)

    def _reconstruir(self, horizontal):
        if horizontal == self._horizontal:
            return
        self._horizontal = horizontal
        while self._layout.count():
            item = self._layout.takeAt(0)
            w = item.widget()
            if w:
                w.setParent(None)

        fila = QWidget()
        lay = QHBoxLayout(fila) if horizontal else QVBoxLayout(fila)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(10)
        for i, (titulo, contenido) in enumerate(self._etapas):
            etapa, lay_etapa = self._etapa(titulo)
            lay_etapa.addWidget(contenido)
            lay.addWidget(etapa, 1)
            if i < len(self._etapas) - 1:
                flecha = QLabel("→" if horizontal else "↓")
                flecha.setAlignment(Qt.AlignCenter)
                flecha.setStyleSheet(
                    f"QLabel {{ color: {paleta.TEXTO_SECUNDARIO}; font-size: 14pt; "
                    f"background: transparent; border: none; }}"
                )
                lay.addWidget(flecha, 0, Qt.AlignCenter)
        self._layout.addWidget(fila)

    @staticmethod
    def _etapa(titulo):
        frame = QFrame()
        frame.setStyleSheet(
            "QFrame { background-color: rgba(255,255,255,0.045); "
            "border: 1px solid rgba(255,255,255,0.14); border-radius: 8px; }"
        )
        lay = QVBoxLayout(frame)
        lay.setContentsMargins(12, 10, 12, 10)
        lay.setSpacing(6)
        etiqueta = QLabel(titulo.upper())
        etiqueta.setStyleSheet(
            f"QLabel {{ color: {paleta.ACENTO}; font-size: {tipografia.AUXILIAR}pt; "
            f"font-weight: 700; letter-spacing: 1px; background: transparent; border: none; }}"
        )
        lay.addWidget(etiqueta)
        return frame, lay


class VentanaAyuda(QWidget):
    """Guía interactiva de uso, construida en Python puro. Se crea una
    sola vez desde VentanaPrincipal y se reutiliza (no se reconstruye en
    cada clic, a diferencia de las pantallas de resultados: su contenido
    es siempre el mismo)."""

    def __init__(self, stacked_widget, parent=None):
        super().__init__(parent)
        self.stacked_widget = stacked_widget

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

        # Stepper y componentes de flujo creados por las páginas de abajo
        # (necesitan que VentanaAyuda les informe el ancho real de
        # contenido, ver resizeEvent).
        self._piezas_responsivas = []

        self._paginas = QStackedWidget()
        self._pagina_menu = self._crear_menu()
        self._paginas.addWidget(self._en_scroll_centrado(self._pagina_menu))
        for constructor in (
            self._crear_pagina_como_empezar,
            self._crear_pagina_rt,
            self._crear_pagina_ih,
            self._crear_pagina_bd,
            self._crear_pagina_resultados,
            self._crear_pagina_acerca,
        ):
            self._paginas.addWidget(self._en_scroll_centrado(constructor()))
        layout_general.addWidget(self._paginas, 1)

        layout_general.addWidget(self._crear_pie())

        self.setup_events()

    # ── Helpers de construcción ──────────────────────────────────────

    @staticmethod
    def _en_scroll_centrado(widget_contenido):
        """
        Centra `widget_contenido` horizontal y verticalmente (acotado a
        _ANCHO_MAX_CONTENIDO) dentro de un QScrollArea vertical-only. Si
        el contenido es más alto que la ventana, los `addStretch` ceden
        y aparece scroll en vez de forzar el centrado — así ni queda
        pegado arriba en 1920×1080 ni se corta en 500×800.
        """
        widget_contenido.setMaximumWidth(_ANCHO_MAX_CONTENIDO)
        widget_contenido.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        fila = QWidget()
        lay_fila = QHBoxLayout(fila)
        lay_fila.setContentsMargins(24, 0, 24, 0)
        lay_fila.addStretch(1)
        # Factor de stretch del widget >> el de los spacers (1): un
        # QBoxLayout reparte el espacio sobrante EN PROPORCIÓN a los
        # factores de stretch, no según sizePolicy por sí sola — con
        # stretch igual (1:1:1) el widget solo recibía un tercio del
        # ancho disponible y nunca llegaba a _ANCHO_MAX_CONTENIDO (el
        # stepper y los componentes de flujo, que deciden
        # horizontal/vertical según su propio ancho real, se quedaban
        # angostos incluso en 1920 px). Con un stretch mucho mayor el
        # widget reclama casi todo el espacio hasta chocar con su
        # maximumWidth, y solo entonces el sobrante pasa a los spacers
        # (centrado). En ventanas más angostas que _ANCHO_MAX_CONTENIDO
        # los spacers quedan en ~0 y el contenido ocupa todo el ancho.
        lay_fila.addWidget(widget_contenido, 1000)
        lay_fila.addStretch(1)

        contenedor = QWidget()
        lay_contenedor = QVBoxLayout(contenedor)
        lay_contenedor.setContentsMargins(0, 0, 0, 0)
        lay_contenedor.addStretch(1)
        lay_contenedor.addWidget(fila)
        lay_contenedor.addStretch(1)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        # Defensa adicional: el ancho de contenido lo decide VentanaAyuda
        # explícitamente (fijar_ancho), nunca debería desbordar — pero si
        # algo lo hiciera, mejor que el contenido se ajuste al viewport
        # (el único scroll de esta pantalla es vertical) a que aparezca
        # una barra horizontal.
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")
        scroll.setWidget(contenedor)
        return scroll

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
        self.botonAtras.setStyleSheet(estiloBotonAtras + "QPushButton { background: transparent; }")
        self.botonAtras.setToolTip("Volver al menú de Ayuda")
        self.botonAtras.setVisible(False)
        lay.addWidget(self.botonAtras)
        lay.addStretch(1)

        self._titulo_cabecera = QLabel()
        self._titulo_cabecera.setStyleSheet("QLabel { background: transparent; border: none; }")
        self._titulo_cabecera.setAlignment(Qt.AlignCenter)
        lay.addWidget(self._titulo_cabecera)
        lay.addStretch(1)

        equilibrio = QWidget()
        equilibrio.setFixedSize(42, 42)
        equilibrio.setStyleSheet("QWidget { background: transparent; border: none; }")
        equilibrio.setAttribute(Qt.WA_TranslucentBackground)
        lay.addWidget(equilibrio)

        self._actualizar_cabecera("Ayuda", "Guía rápida para usar room_acoustic")
        return frame

    def _actualizar_cabecera(self, titulo, subtitulo):
        self._titulo_cabecera.setText(
            '<html><body><p align="center">'
            f'<span style="font-size:{tipografia.TITULO_PANTALLA}pt; font-weight:700; color:#ffffff;">'
            f'{titulo}</span><br>'
            f'<span style="font-size:{tipografia.AUXILIAR}pt; color:{paleta.TEXTO_SECUNDARIO};">'
            f'{subtitulo}</span></p></body></html>'
        )

    # ── Menú principal de Ayuda ─────────────────────────────────────

    # índice de página en self._paginas -> título de cabecera (migas "Ayuda › …")
    _SECCIONES = {
        1: "Cómo empezar",
        2: "Tiempo de Reverberación",
        3: "Inteligibilidad",
        4: "Base de Datos",
        5: "Resultados y PDF",
        6: "Acerca del proyecto",
    }

    def _crear_menu(self):
        contenedor = QWidget()
        lay = QVBoxLayout(contenedor)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(20)

        titulo = _etiqueta("¿Cómo podemos ayudarte?", tipografia.TITULO, "white", negrita=True, centrado=True)
        lay.addWidget(titulo)
        subtitulo = _etiqueta(
            "Explora el funcionamiento de room_acoustic por secciones.",
            tipografia.CUERPO, paleta.TEXTO_SECUNDARIO, centrado=True)
        lay.addWidget(subtitulo)

        self._grid_menu = QGridLayout()
        self._grid_menu.setSpacing(14)
        lay.addLayout(self._grid_menu)

        datos_tarjetas = [
            ("tarjetaComoEmpezar", "Cómo empezar", "El flujo general de la aplicación.", None),
            ("tarjetaRT", "Tiempo de Reverberación", "Sabine, Eyring y RT60.",
             "../Recursos/iconos/ondas-de-audio.png"),
            ("tarjetaIH", "Inteligibilidad", "%ALCons, Peutz y la clasificación.",
             "../Recursos/iconos/terapia-musical.png"),
            ("tarjetaBD", "Base de Datos", "Las 23 aulas del Bloque H.", None),
            ("tarjetaResultados", "Resultados y PDF", "Qué obtienes al finalizar un análisis.", None),
            ("tarjetaAcerca", "Acerca del proyecto", "Universidad del Atlántico · proyecto de grado.", None),
        ]
        self._tarjetas_menu = []
        for i, (nombre, titulo_t, descripcion, icono) in enumerate(datos_tarjetas):
            tarjeta = _TarjetaTema(nombre, titulo_t, descripcion, icono)
            indice_pagina = i + 1
            tarjeta.clicked.connect(lambda idx=indice_pagina: self._mostrar_tema(idx))
            self._tarjetas_menu.append(tarjeta)

        self._distribuir_menu(_ANCHO_MAX_CONTENIDO)
        return contenedor

    def _distribuir_menu(self, ancho_disponible):
        """3 columnas si hay espacio de sobra, 2 en tamaños medios, 1
        apilada en pantallas angostas."""
        for i in reversed(range(self._grid_menu.count())):
            self._grid_menu.takeAt(i)
        if ancho_disponible >= _ANCHO_GRID_3COL:
            columnas = 3
        elif ancho_disponible >= _ANCHO_GRID_2COL:
            columnas = 2
        else:
            columnas = 1
        for i, tarjeta in enumerate(self._tarjetas_menu):
            fila, col = divmod(i, columnas)
            self._grid_menu.addWidget(tarjeta, fila, col)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._actualizar_ancho_contenido()

    def _actualizar_ancho_contenido(self):
        """
        Empuja el ancho real de contenido al grid del menú y a cada
        stepper/componente de flujo. Se llama desde resizeEvent, pero
        TAMBIÉN desde _mostrar_tema: una página dentro de un
        QStackedWidget que no es la actual no siempre vuelve a calcular
        su layout solo porque cambió `self.width()` (Qt difiere el
        layout de páginas ocultas) — sin este segundo disparo, una
        página visitada por primera vez podía mostrar el stepper/flujo
        con el ancho que tenía en construcción, no el real.
        """
        ancho_contenido = min(self.width() - 48, _ANCHO_MAX_CONTENIDO)
        if hasattr(self, "_grid_menu"):
            self._distribuir_menu(ancho_contenido)
        for pieza in getattr(self, "_piezas_responsivas", []):
            pieza.fijar_ancho(ancho_contenido)

    # ── Página "Cómo empezar" (stepper) ──────────────────────────────

    _PASOS = [
        ("01", "Selecciona un módulo",
         "Desde el Inicio, elige Tiempo de Reverberación, Inteligibilidad o Base de Datos."),
        ("02", "Ingresa los datos",
         "Dimensiones, materiales y objetos — o selecciona un aula ya caracterizada en Base de Datos."),
        ("03", "Analiza",
         "El software calcula el resultado acústico con el modelo correspondiente."),
        ("04", "Revisa el resultado",
         "Tabla, gráfico (cuando aplica) y clasificación, en una pantalla dedicada."),
        ("05", "Guarda el PDF",
         "Un reporte con los mismos datos del resultado, listo para conservar o compartir."),
    ]

    def _crear_pagina_como_empezar(self):
        cont = QWidget()
        lay = QVBoxLayout(cont)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(18)

        lay.addWidget(_etiqueta("El flujo de la aplicación", tipografia.TITULO, "white", negrita=True))

        self._stepper = _Stepper(self._PASOS)
        self._piezas_responsivas.append(self._stepper)
        lay.addWidget(self._stepper)

        self._descripcion_paso = _mosaico_acento(
            "descripcionPaso", "PASO 1 · SELECCIONA UN MÓDULO", paleta.ACENTO,
            texto_valor=self._PASOS[0][2])
        lay.addWidget(self._descripcion_paso)

        self._stepper.paso_seleccionado.connect(self._actualizar_descripcion_paso)
        return cont

    def _actualizar_descripcion_paso(self, indice):
        numero, titulo, descripcion = self._PASOS[indice]
        self._descripcion_paso.setObjectName("descripcionPaso")
        label_titulo = self._descripcion_paso.findChildren(QLabel)[0]
        label_valor = self._descripcion_paso.findChildren(QLabel)[1]
        label_titulo.setText(f"PASO {numero} · {titulo.upper()}")
        label_valor.setText(descripcion)

    # ── Página Tiempo de Reverberación (M1) ──────────────────────────

    def _crear_pagina_rt(self):
        cont = QWidget()
        lay = QVBoxLayout(cont)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(16)

        lay.addWidget(_etiqueta("RT60", tipografia.VALOR, paleta.ACENTO, negrita=True))
        lay.addWidget(_etiqueta(
            "Tiempo que tarda el nivel sonoro en disminuir 60 dB después de detenerse la fuente.",
            tipografia.CUERPO, paleta.TEXTO_SECUNDARIO))
        lay.addWidget(_separador())

        metodos = QWidget()
        lay_metodos = QVBoxLayout(metodos)
        lay_metodos.setContentsMargins(0, 0, 0, 0)
        lay_metodos.setSpacing(6)
        lay_metodos.addWidget(_mosaico_acento(
            "metodoSabine", "SABINE", paleta.SERIE_SABINE,
            texto_valor="Uno de los dos métodos de cálculo que aplica el software."))
        lay_metodos.addWidget(_mosaico_acento(
            "metodoEyring", "EYRING", paleta.SERIE_EYRING,
            texto_valor="El segundo método, calculado en paralelo para comparar."))

        flujo = _FlujoEtapas([
            ("Entrada", _fila_chips(["Dimensiones", "Materiales", "Objetos"])),
            ("Procesamiento", metodos),
            ("Resultado", _fila_chips(["Tabla por banda", "Gráfico", "Veredicto", "PDF"])),
        ])
        self._piezas_responsivas.append(flujo)
        lay.addWidget(flujo)
        return cont

    # ── Página Inteligibilidad (M2) ──────────────────────────────────

    def _crear_pagina_ih(self):
        cont = QWidget()
        lay = QVBoxLayout(cont)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(16)

        lay.addWidget(_etiqueta("%ALCons", tipografia.VALOR, paleta.ACENTO, negrita=True))
        lay.addWidget(_etiqueta(
            "Mide la pérdida de articulación de consonantes: qué tan bien se entiende la "
            "voz en el aula.", tipografia.CUERPO, paleta.TEXTO_SECUNDARIO))
        lay.addWidget(_separador())

        proceso = _fila_chips(["Modelo de Peutz", "Distancia crítica"])
        flujo = _FlujoEtapas([
            ("Entrada", _fila_chips(["Distancia", "TR", "Volumen", "Coeficientes"])),
            ("Procesamiento", proceso),
            ("Resultado", _fila_chips(["Categoría", "PDF"])),
        ])
        self._piezas_responsivas.append(flujo)
        lay.addWidget(flujo)

        lay.addWidget(_separador())
        lay.addWidget(_etiqueta("Clasificación", tipografia.SUBTITULO, "white", negrita=True))
        lay.addWidget(self._escala_alcons())
        lay.addWidget(_etiqueta(
            "Clasificación operativa utilizada por el software.",
            tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        return cont

    def _escala_alcons(self):
        """6 niveles de D-019, tomados directamente de NIVELES_ALCONS
        (Datos/utils/reportePDF.py) — mismos nombres y colores que ve el
        usuario en el resultado real y en el PDF; sin repetir aquí los
        umbrales numéricos."""
        cont = QWidget()
        fila = QHBoxLayout(cont)
        fila.setSpacing(3)
        for _limite, rgb, nombre_nivel, _rango in NIVELES_ALCONS:
            color = _hex(rgb)
            seg = QFrame()
            seg.setFixedHeight(26)
            seg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            seg.setStyleSheet(f"QFrame {{ background-color: {color}; border-radius: 4px; }}")
            seg_lay = QVBoxLayout(seg)
            seg_lay.setContentsMargins(2, 0, 2, 0)
            lbl = QLabel(nombre_nivel)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet(
                "QLabel { color: white; font-weight: bold; font-size: 7pt; "
                "background: transparent; border: none; }"
            )
            seg_lay.addWidget(lbl)
            fila.addWidget(seg)
        return cont

    # ── Página Base de Datos (M3) ─────────────────────────────────────

    def _crear_pagina_bd(self):
        cont = QWidget()
        lay = QVBoxLayout(cont)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(16)

        fila_hero = QHBoxLayout()
        fila_hero.setSpacing(12)
        fila_hero.addWidget(_etiqueta("23", tipografia.VALOR, paleta.ACENTO, negrita=True))
        texto_hero = QVBoxLayout()
        texto_hero.setSpacing(0)
        texto_hero.addWidget(_etiqueta("tipos de aula", tipografia.CUERPO, "white", negrita=True))
        texto_hero.addWidget(_etiqueta("del Bloque H, ya caracterizadas", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        fila_hero.addLayout(texto_hero)
        fila_hero.addStretch(1)
        lay.addLayout(fila_hero)
        lay.addWidget(_separador())

        caracteristicas = _fila_chips(["Largo", "Ancho", "Alto", "Materiales", "Objetos"])
        flujo = _FlujoEtapas([
            ("Entrada", _etiqueta("Selecciona un aula", tipografia.CUERPO, "white", negrita=True)),
            ("Procesamiento", caracteristicas),
            ("Resultado", _fila_chips(["Mismo análisis que RT", "PDF"])),
        ])
        self._piezas_responsivas.append(flujo)
        lay.addWidget(flujo)
        return cont

    # ── Página Resultados y PDF ───────────────────────────────────────

    def _crear_pagina_resultados(self):
        cont = QWidget()
        lay = QVBoxLayout(cont)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(16)

        lay.addWidget(_etiqueta(
            "Cada análisis abre una pantalla de resultados con el valor calculado y su "
            "interpretación.", tipografia.CUERPO, paleta.TEXTO_SECUNDARIO))

        destinos = QWidget()
        lay_destinos = QHBoxLayout(destinos)
        lay_destinos.setContentsMargins(0, 0, 0, 0)
        lay_destinos.setSpacing(8)
        lay_destinos.addWidget(_mosaico_acento(
            "destinoGrafico", "GRÁFICO", paleta.SERIE_EYRING,
            texto_valor="Comparación visual (Tiempo de Reverberación)."))
        lay_destinos.addWidget(_mosaico_acento(
            "destinoPdf", "PDF", paleta.ACENTO,
            texto_valor="El mismo resultado, listo para guardar o compartir."))

        flujo = _FlujoEtapas([
            ("Datos", _etiqueta("Dimensiones, materiales u aula seleccionada", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO)),
            ("Análisis", _etiqueta("Cálculo acústico del módulo correspondiente", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO)),
            ("Resultado", destinos),
        ])
        self._piezas_responsivas.append(flujo)
        lay.addWidget(flujo)
        return cont

    # ── Página Acerca del proyecto ─────────────────────────────────────

    def _crear_pagina_acerca(self):
        cont = QWidget()
        lay = QVBoxLayout(cont)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(16)

        lay.addWidget(_etiqueta("Room Acoustic", tipografia.VALOR, "white", negrita=True))
        lay.addWidget(_etiqueta(
            "Software para evaluación acústica de aulas.",
            tipografia.CUERPO, paleta.TEXTO_SECUNDARIO))
        lay.addWidget(_separador())
        lay.addWidget(_mosaico_acento(
            "institucion", "PROYECTO", paleta.ACENTO,
            texto_valor="Universidad del Atlántico — Ingeniería Industrial, proyecto de grado."))
        return cont

    # ── Pie ───────────────────────────────────────────────────────────

    def _crear_pie(self):
        frame = QFrame()
        frame.setObjectName("frameBottom")
        frame.setMinimumHeight(64)
        frame.setStyleSheet(estiloBarraInferior("frameBottom", "botonVolverInicio"))
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(16, 8, 16, 8)
        lay.addStretch(1)

        self.botonVolverInicio = QPushButton("Volver al Inicio")
        self.botonVolverInicio.setObjectName("botonVolverInicio")
        self.botonVolverInicio.setToolTip("Volver a la pantalla principal")
        lay.addWidget(self.botonVolverInicio)

        return frame

    # ── Navegación interna ────────────────────────────────────────────

    def setup_events(self):
        self.botonAtras.clicked.connect(self._mostrar_menu)
        self.botonVolverInicio.clicked.connect(self.ir_ventana_home)

    def _mostrar_tema(self, indice_pagina):
        self._paginas.setCurrentIndex(indice_pagina)
        self._actualizar_cabecera("Ayuda", f"Ayuda › {self._SECCIONES[indice_pagina]}")
        self.botonAtras.setVisible(True)
        self._actualizar_ancho_contenido()

    def _mostrar_menu(self):
        self._paginas.setCurrentIndex(0)
        self._actualizar_cabecera("Ayuda", "Guía rápida para usar room_acoustic")
        self.botonAtras.setVisible(False)

    def ir_ventana_home(self):
        self._mostrar_menu()  # para que la próxima vez que se abra Ayuda, se vea el menú
        if self.stacked_widget:
            self.stacked_widget.setCurrentIndex(0)


# ─────────────────────────────────────────────────────────────
#  Stepper de "Cómo empezar" — fila de círculos numerados conectados
#  (horizontal en desktop, columna en pantallas angostas, según su
#  propio ancho). Seleccionar un paso solo cambia cuál está activo y
#  emite la señal; el texto de la explicación vive en un único mosaico
#  fuera del stepper (VentanaAyuda._descripcion_paso), para que esto se
#  lea como un componente, no como 5 tarjetas sueltas.
# ─────────────────────────────────────────────────────────────
_ANCHO_STEPPER_HORIZONTAL = 620
_DIAMETRO_CIRCULO = 40


class _Stepper(QWidget):
    paso_seleccionado = Signal(int)

    def __init__(self, pasos, parent=None):
        super().__init__(parent)
        self._pasos = pasos
        self._indice_activo = 0
        self._circulos = []
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._horizontal = None
        self._reconstruir(True)

    def fijar_ancho(self, ancho):
        """Igual que `_FlujoEtapas.fijar_ancho`: decide la orientación con
        el ancho real que informa VentanaAyuda, no con `self.width()`
        (poco fiable dentro de un QScrollArea con `widgetResizable`), y
        fuerza ese ancho como máximo para que ningún QLabel interno con
        wordWrap pueda pedir más (ver nota en `_FlujoEtapas.fijar_ancho`)."""
        self.setMaximumWidth(ancho)
        self._reconstruir(ancho >= _ANCHO_STEPPER_HORIZONTAL)

    def _reconstruir(self, horizontal):
        if horizontal == self._horizontal:
            return
        self._horizontal = horizontal
        while self._layout.count():
            item = self._layout.takeAt(0)
            w = item.widget()
            if w:
                w.setParent(None)

        fila = QWidget()
        lay = QHBoxLayout(fila) if horizontal else QVBoxLayout(fila)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        self._circulos = []
        for i, (numero, titulo, _descripcion) in enumerate(self._pasos):
            paso_widget, circulo, titulo_lbl = self._paso(numero, titulo, i == self._indice_activo)
            self._circulos.append((circulo, titulo_lbl))
            # Clic en cualquier parte del paso (closure captura `i` por valor por defecto)
            paso_widget.mousePressEvent = (lambda ev, idx=i: self._seleccionar(idx))
            paso_widget.setCursor(Qt.PointingHandCursor)
            lay.addWidget(paso_widget, 1 if horizontal else 0)
            if i < len(self._pasos) - 1:
                conector = QFrame()
                if horizontal:
                    conector.setFixedHeight(2)
                    conector.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                else:
                    conector.setFixedWidth(2)
                    conector.setFixedHeight(16)
                conector.setStyleSheet("QFrame { background-color: rgba(255,255,255,0.18); border: none; }")
                if horizontal:
                    lay.addWidget(conector, 0, Qt.AlignVCenter)
                else:
                    cont_conector = QWidget()
                    lay_conector = QHBoxLayout(cont_conector)
                    lay_conector.setContentsMargins(19, 0, 0, 0)
                    lay_conector.addWidget(conector)
                    lay.addWidget(cont_conector)
        self._layout.addWidget(fila)

    def _paso(self, numero, titulo, activo):
        cont = QWidget()
        lay = QVBoxLayout(cont) if self._horizontal else QHBoxLayout(cont)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(8)
        if not self._horizontal:
            lay.setAlignment(Qt.AlignVCenter)

        circulo = QLabel(numero)
        circulo.setFixedSize(QSize(_DIAMETRO_CIRCULO, _DIAMETRO_CIRCULO))
        circulo.setAlignment(Qt.AlignCenter)
        self._estilizar_circulo(circulo, activo)
        lay.addWidget(circulo, 0, Qt.AlignHCenter if self._horizontal else Qt.AlignVCenter)

        titulo_lbl = QLabel(titulo)
        titulo_lbl.setWordWrap(True)
        titulo_lbl.setAlignment(Qt.AlignCenter if self._horizontal else Qt.AlignLeft | Qt.AlignVCenter)
        titulo_lbl.setStyleSheet(estiloTexto(
            tipografia.AUXILIAR, "white" if activo else paleta.TEXTO_SECUNDARIO, negrita=activo))
        lay.addWidget(titulo_lbl, 1 if not self._horizontal else 0)

        return cont, circulo, titulo_lbl

    @staticmethod
    def _estilizar_circulo(circulo, activo):
        if activo:
            circulo.setStyleSheet(
                f"QLabel {{ background-color: rgba(126,200,247,0.22); "
                f"border: 2px solid {paleta.ACENTO}; border-radius: {_DIAMETRO_CIRCULO // 2}px; "
                f"color: {paleta.ACENTO}; font-weight: 700; font-size: {tipografia.CUERPO}pt; }}"
            )
        else:
            circulo.setStyleSheet(
                "QLabel { background-color: rgba(255,255,255,0.06); "
                "border: 1px solid rgba(255,255,255,0.25); "
                f"border-radius: {_DIAMETRO_CIRCULO // 2}px; "
                f"color: {paleta.TEXTO_SECUNDARIO}; font-weight: 600; font-size: {tipografia.CUERPO}pt; }}"
            )

    def _seleccionar(self, indice):
        if indice == self._indice_activo:
            return
        self._indice_activo = indice
        for i, (circulo, titulo_lbl) in enumerate(self._circulos):
            activo = i == indice
            self._estilizar_circulo(circulo, activo)
            titulo_lbl.setStyleSheet(estiloTexto(
                tipografia.AUXILIAR, "white" if activo else paleta.TEXTO_SECUNDARIO, negrita=activo))
        self.paso_seleccionado.emit(indice)
