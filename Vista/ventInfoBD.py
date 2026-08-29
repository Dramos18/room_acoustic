from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame, QSizePolicy, QMessageBox, QSpacerItem
)

from Controlador.controlTR import procesar_datos
from Vista.ventGraficaRT import VentanaGraficaRT
from Vista.ventTransicion import VentanaTransicion
from Vista.archivos_pyGenerados.infoBD import Ui_Form
from Recursos.estilos.estilo import estiloWarning
from Datos.salones import salones


# ─────────────────────────────────────────────────────────────
#  PALETA DE COLORES — consistente con el resto del proyecto
# ─────────────────────────────────────────────────────────────
_COLORES_SUPERFICIE = {
    "frontal":    ("rgba(126,200,247,0.18)", "rgba(126,200,247,0.55)"),   # azul claro
    "trasera":    ("rgba(167,139,250,0.18)", "rgba(167,139,250,0.55)"),   # violeta
    "izquierda":  ("rgba(52,211,153,0.18)",  "rgba(52,211,153,0.55)"),    # verde menta
    "derecha":    ("rgba(251,191,36,0.15)",  "rgba(251,191,36,0.55)"),    # amarillo
    "piso":       ("rgba(251,146,60,0.15)",  "rgba(251,146,60,0.55)"),    # naranja
    "techo":      ("rgba(248,113,113,0.15)", "rgba(248,113,113,0.55)"),   # rojo suave
}
_COLOR_ADICIONALES = ("rgba(255,255,255,0.09)", "rgba(255,255,255,0.40)")

_ICONOS_SUPERFICIE = {
    "frontal":   "▣",
    "trasera":   "▣",
    "izquierda": "◧",
    "derecha":   "◨",
    "piso":      "▬",
    "techo":     "▲",
}


# ─────────────────────────────────────────────────────────────
#  CONSTRUCTORES DE WIDGETS (helpers privados)
# ─────────────────────────────────────────────────────────────

def _label(texto: str, size_pt: int = 9, bold: bool = False,
           color: str = "rgba(255,255,255,0.85)", wrap: bool = False) -> QLabel:
    """Crea un QLabel con estilo inline."""
    lbl = QLabel(texto)
    peso = "bold" if bold else "normal"
    lbl.setStyleSheet(
        f"color: {color}; font-size: {size_pt}pt; font-weight: {peso};"
        " background: transparent; border: none;"
    )
    lbl.setWordWrap(wrap)
    return lbl


def _separador_h(opacidad: float = 0.15) -> QFrame:
    """Línea horizontal divisoria."""
    linea = QFrame()
    linea.setFrameShape(QFrame.HLine)
    c = int(opacidad * 255)
    linea.setStyleSheet(
        f"background-color: rgba(255,255,255,{opacidad:.2f}); "
        "max-height: 1px; border: none;"
    )
    linea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return linea


def _fila_objeto(nombre: str, material: str, valor: str,
                 es_par: bool = True) -> QFrame:
    """
    Fila compacta para un objeto adherido u objeto adicional.
    Formato: [nombre]  ·  [material]  ·  [valor]
    """
    fondo = "rgba(255,255,255,0.06)" if es_par else "rgba(255,255,255,0.03)"
    fila = QFrame()
    fila.setStyleSheet(
        f"QFrame {{ background-color: {fondo}; border-radius: 6px; border: none; }}"
    )
    layout = QHBoxLayout(fila)
    layout.setContentsMargins(10, 4, 10, 4)
    layout.setSpacing(8)

    lbl_nombre = _label(f"  {nombre}", size_pt=9, color="rgba(255,255,255,0.80)")
    lbl_nombre.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    lbl_sep1 = _label("·", size_pt=9, color="rgba(255,255,255,0.30)")
    lbl_sep1.setFixedWidth(10)
    lbl_sep1.setAlignment(Qt.AlignCenter)

    lbl_mat = _label(material, size_pt=9, color="rgba(255,255,255,0.60)", wrap=True)
    lbl_mat.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    lbl_sep2 = _label("·", size_pt=9, color="rgba(255,255,255,0.30)")
    lbl_sep2.setFixedWidth(10)
    lbl_sep2.setAlignment(Qt.AlignCenter)

    lbl_val = _label(valor, size_pt=9, bold=True, color="rgba(255,255,255,0.75)")
    lbl_val.setFixedWidth(70)
    lbl_val.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

    layout.addWidget(lbl_nombre)
    layout.addWidget(lbl_sep1)
    layout.addWidget(lbl_mat)
    layout.addWidget(lbl_sep2)
    layout.addWidget(lbl_val)
    return fila


def _card_superficie(nombre_superficie: str, datos: dict) -> QFrame:
    """
    Card para una superficie del salón.
    Muestra: nombre + material base + objetos adheridos (si los hay).
    """
    clave = nombre_superficie.lower()
    bg, acento = _COLORES_SUPERFICIE.get(clave, _COLOR_ADICIONALES)
    icono = _ICONOS_SUPERFICIE.get(clave, "◻")

    card = QFrame()
    card.setObjectName("cardSuperficie")
    card.setStyleSheet(
        f"QFrame#cardSuperficie {{"
        f"  background-color: {bg};"
        f"  border: 1px solid {acento};"
        f"  border-radius: 10px;"
        f"}}"
    )
    card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    layout = QVBoxLayout(card)
    layout.setContentsMargins(12, 10, 12, 10)
    layout.setSpacing(6)

    # ── Cabecera: icono + nombre + material ──
    cabecera = QWidget()
    cabecera.setStyleSheet("background: transparent;")
    hlo = QHBoxLayout(cabecera)
    hlo.setContentsMargins(0, 0, 0, 0)
    hlo.setSpacing(8)

    lbl_icono = _label(icono, size_pt=14, bold=True, color=acento)
    lbl_icono.setFixedWidth(22)
    lbl_icono.setAlignment(Qt.AlignCenter)

    lbl_nombre = _label(nombre_superficie.capitalize(), size_pt=10, bold=True,
                        color="white")

    material_base = datos.get("material", "N/A")
    area_base = datos.get("area", "")
    area_str = f"  ({area_base} m²)" if area_base else ""
    lbl_material = _label(f"{material_base}{area_str}", size_pt=9,
                          color="rgba(255,255,255,0.65)", wrap=True)
    lbl_material.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    hlo.addWidget(lbl_icono)
    hlo.addWidget(lbl_nombre)
    hlo.addWidget(lbl_material, stretch=1)
    layout.addWidget(cabecera)

    # ── Objetos adheridos (si existen) ──
    objetos = datos.get("objetos_adheridos") or []
    if objetos:
        layout.addWidget(_separador_h(0.12))

        encab_obj = QWidget()
        encab_obj.setStyleSheet("background: transparent;")
        hlo_enc = QHBoxLayout(encab_obj)
        hlo_enc.setContentsMargins(2, 0, 2, 0)
        hlo_enc.setSpacing(6)
        hlo_enc.addWidget(
            _label("Objetos adheridos", size_pt=8, color="rgba(255,255,255,0.45)")
        )
        hlo_enc.addWidget(
            _label(f"{len(objetos)}", size_pt=8, bold=True, color=acento)
        )
        hlo_enc.addStretch()
        layout.addWidget(encab_obj)

        for idx, obj in enumerate(objetos):
            nombre_obj = obj.get("nombre", "")
            mat_obj    = obj.get("material", "")
            area_obj   = f"{obj.get('area', '')} m²"
            layout.addWidget(_fila_objeto(nombre_obj, mat_obj, area_obj,
                                          es_par=(idx % 2 == 0)))

    return card


def _card_objetos_adicionales(objetos: list) -> QFrame:
    """Card especial para los objetos adicionales del salón."""
    bg, acento = _COLOR_ADICIONALES

    card = QFrame()
    card.setObjectName("cardAdicionales")
    card.setStyleSheet(
        f"QFrame#cardAdicionales {{"
        f"  background-color: {bg};"
        f"  border: 1px solid {acento};"
        f"  border-radius: 10px;"
        f"}}"
    )
    card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    layout = QVBoxLayout(card)
    layout.setContentsMargins(12, 10, 12, 10)
    layout.setSpacing(6)

    # Cabecera
    cab = QWidget()
    cab.setStyleSheet("background: transparent;")
    hlo = QHBoxLayout(cab)
    hlo.setContentsMargins(0, 0, 0, 0)
    hlo.setSpacing(8)
    hlo.addWidget(_label("◈", size_pt=13, bold=True, color=acento))
    hlo.addWidget(_label("Objetos adicionales", size_pt=10, bold=True, color="white"))
    hlo.addWidget(
        _label(f"{len(objetos)} elemento(s)", size_pt=9,
               color="rgba(255,255,255,0.50)")
    )
    hlo.addStretch()
    layout.addWidget(cab)

    if objetos:
        layout.addWidget(_separador_h(0.12))
        for idx, obj in enumerate(objetos):
            nombre_obj   = obj.get("nombre", "")
            mat_obj      = obj.get("material", "")
            cantidad_obj = f"× {obj.get('cantidad', '')}"
            layout.addWidget(
                _fila_objeto(nombre_obj, mat_obj, cantidad_obj,
                             es_par=(idx % 2 == 0))
            )
    else:
        layout.addWidget(
            _label("No hay objetos adicionales registrados.", size_pt=9,
                   color="rgba(255,255,255,0.40)")
        )

    return card


# ─────────────────────────────────────────────────────────────
#  VENTANA PRINCIPAL
# ─────────────────────────────────────────────────────────────

class VentanaInfoBaseDatos(QWidget):
    """
    Ventana de Base de Datos del Bloque H.
    Reemplaza el QTreeWidget por cards dinámicas dentro de un QScrollArea.
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.indice_anterior = indice_anterior
        self.stacked_widget  = stacked_widget
        self.salones         = salones

        self.ui.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))


        # Preparar el layout interno del QScrollArea de cards
        self._init_scroll_materiales()

        # Conectar ComboBox
        self.cargar_salones(self.ui.comboBox, self.salones)
        self.ui.comboBox.currentIndexChanged.connect(self._on_combo_changed)

        self.setup_events()

    # ── Inicialización del contenedor de cards ──────────────────

    def _init_scroll_materiales(self):
        """Crea el QVBoxLayout dentro de contenedorCards y lo guarda."""
        self._layout_cards = QVBoxLayout()
        self._layout_cards.setContentsMargins(10, 10, 10, 10)
        self._layout_cards.setSpacing(8)
        self._layout_cards.setAlignment(Qt.AlignTop)
        self.ui.contenedorCards.setLayout(self._layout_cards)

    # ── Eventos ─────────────────────────────────────────────────

    def setup_events(self):
        self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)
        self.ui.botonIniciarAnalisis.clicked.connect(self.iniciar_analisis)

    def _on_combo_changed(self):
        self.mostrar_informacion(
            self.ui.comboBox,
            self.ui.labelNumeroAula,
            self.ui.labelLargo,
            self.ui.labelAlto,
            self.ui.labelAncho,
            self.salones,
        )

    def regresar_a_ventana_anterior(self):
        if hasattr(self, "stacked_widget") and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)

    # ── Carga del ComboBox — sin cambios ────────────────────────

    def cargar_salones(self, combo_box, salones):
        combo_box.clear()
        combo_box.addItem("Seleccionar")
        for salon in salones:
            combo_box.addItem(salon["Tipo"])

    # ── Mostrar información del salón seleccionado ───────────────

    def mostrar_informacion(self, combo_box, label_aula, label_largo,
                            label_alto, label_ancho, salones):
        """
        Actualiza las mini-cards de dimensiones y reconstruye
        las cards de materiales en el QScrollArea.
        """
        selected_index = combo_box.currentIndex()

        # Limpiar cards anteriores
        self._limpiar_cards()

        if selected_index == 0:
            label_aula.setText("—")
            label_largo.setText("—")
            label_alto.setText("—")
            label_ancho.setText("—")
            self._mostrar_placeholder()
            return

        salon = salones[selected_index - 1]

        # ── Dimensiones ──
        label_aula.setText(salon.get("aulas", "—"))
        dim = salon.get("dimensiones", {})
        label_largo.setText(f"{dim.get('largo', '—')} m")
        label_alto.setText(f"{dim.get('altura', '—')} m")
        label_ancho.setText(f"{dim.get('ancho', '—')} m")

        # ── Cards de superficies ──
        materiales = salon.get("materiales", {})
        for nombre_sup, datos_sup in materiales.items():
            card = _card_superficie(nombre_sup, datos_sup)
            self._layout_cards.addWidget(card)

        # ── Card de objetos adicionales ──
        objetos_adicionales = salon.get("objetos_adicionales") or []
        card_adicionales = _card_objetos_adicionales(objetos_adicionales)
        self._layout_cards.addWidget(card_adicionales)

        # Espaciador final para que las cards no se estiren
        self._layout_cards.addSpacerItem(
            QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

    def _limpiar_cards(self):
        """Elimina todas las cards del layout interno."""
        while self._layout_cards.count():
            item = self._layout_cards.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def _mostrar_placeholder(self):
        """Mensaje cuando no hay aula seleccionada."""
        lbl = _label(
            "Selecciona un tipo de aula para ver sus materiales y elementos.",
            size_pt=10,
            color="rgba(255,255,255,0.35)",
        )
        lbl.setAlignment(Qt.AlignCenter)
        self._layout_cards.addWidget(lbl)
        self._layout_cards.addSpacerItem(
            QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

    # ── Controlador — sin cambios ────────────────────────────────

    def enviar_obtener_datos_controlador(self, salon):
        if salon is None:
            print("Error en la validación de superficies.")
        else:
            print("yendo a procesar datos")
            resultados = procesar_datos(salon)
            print("diccionario recibido por el controlador", resultados)
            return resultados

    def iniciar_analisis(self):
        selected_index = self.ui.comboBox.currentIndex()
        if selected_index != 0:
            transicion = VentanaTransicion(
                "Recursos/estilos/iconos/ondas.gif",
                duracion_ms=2000,
                parent=self,
            )
            salon_seleccionado = self.salones[selected_index - 1]
            print(salon_seleccionado)
            self.indice = self.stacked_widget.currentIndex()
            resultado = self.enviar_obtener_datos_controlador(salon_seleccionado)
            ventana_grafica = VentanaGraficaRT(
                stacked_widget=self.stacked_widget,
                indice_anterior=self.indice,
                resultados=resultado,
            )
            ventana_grafica.indice_anterior = self.stacked_widget.currentIndex()
            self.stacked_widget.addWidget(ventana_grafica)
            transicion.exec()
            self.stacked_widget.setCurrentWidget(ventana_grafica)
        else:
            msgError = QMessageBox(self)
            msgError.setIcon(QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Seleccione un tipo de aula de la base de datos")
            msgError.setStyleSheet(estiloWarning)
            msgError.exec()
