from Recursos.estilos import paleta

estiloFrameRT = """
QGroupBox {
    border: 2px solid white;
    border-radius: 10px;
    margin-top: 10px;
    background-color: rgba(255, 255, 255, 20);
    font: bold 12px "Arial";
    color: white;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 5px;
    font-size: 14px;
    color: white;
}

QLabel {
    color: white;
    font-size: 14px;
    font-weight: bold;
}

QLineEdit {
    border: 2px solid white;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
    font-size: 14px;
    font-weight: bold;
    padding: 6px;
    selection-background-color: rgba(255, 255, 255, 0.3);
}

QLineEdit:focus {
    border: 2px solid cyan;
    background-color: rgba(255, 255, 255, 0.5);
}

QComboBox {
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid white;
    border-radius: 5px;
    color: white;
    padding: 3px;
}

QComboBox QAbstractItemView {
    background-color: white;
    color: black;
    selection-background-color: lightgray;
}

QComboBox QScrollBar:vertical {
    border: none;
    background: #f0f0f0;
    width: 10px;
    margin: 0px 0px 0px 0px;
}

QComboBox QScrollBar::handle:vertical {
    background: #bfbfbf;
    min-height: 20px;
    border-radius: 4px;
}

QComboBox QScrollBar::handle:vertical:hover {
    background: #a6a6a6;
}

QComboBox QScrollBar::add-line:vertical,
QComboBox QScrollBar::sub-line:vertical {
    height: 0px;
}

QComboBox QScrollBar::add-page:vertical,
QComboBox QScrollBar::sub-page:vertical {
    background: none;
}

/* Checkbox */
QCheckBox {
    background: transparent;
    color: white;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid white;
}

QCheckBox::indicator:hover {
    background: rgba(255, 255, 255, 0.4);
}

QCheckBox::indicator:checked {
    image: url(Vista/estilos/iconos/controlar.png);
    border: 2px solid white;
}

/* Botones "+" y "-" */
QPushButton {
    background: transparent;
    border: none;
}

QPushButton:hover {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 5px;
}
"""

estiloObjeto = """
QWidget {
    background-color: transparent;
}

QLineEdit {
    font-size: 11px;
    font-weight: normal;
    color: white;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid white;
    border-radius: 8px;
    padding: 4px 8px;
}
QLineEdit:focus {
    border: 1px solid #00AEEF;
    background: rgba(255, 255, 255, 0.25);
}

/* COMBOBOX */
QComboBox {
    background: rgba(255, 255, 255, 0.3);
    border: 1px solid white;
    border-radius: 5px;
    color: white;
    padding: 4px;
}
QComboBox:focus {
    border: 1px solid #00AEEF;
    background: rgba(255, 255, 255, 0.4);
}
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox::down-arrow {
    image: url(../Recursos/iconos/angulo-abajo.png);
    width: 10px;
    height: 10px;
}

/* Lista desplegable */
QComboBox QAbstractItemView {
    background-color: #001a4d;
    color: white;
    selection-background-color: rgba(126,200,247,0.30);
    selection-color: white;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 5px;
}

/* Scroll */
QComboBox QScrollBar:vertical {
    background: transparent;
    width: 8px;
}
QComboBox QScrollBar::handle:vertical {
    background: #aaa;
    border-radius: 4px;
}
QComboBox QScrollBar::handle:vertical:hover {
    background: #888;
}
QComboBox QScrollBar::add-line:vertical,
QComboBox QScrollBar::sub-line:vertical {
    height: 0px;
}
QComboBox QScrollBar::add-page:vertical,
QComboBox QScrollBar::sub-page:vertical {
    background: none;
}

/* Botones "+" y "-" */
QPushButton {
    background: transparent;
    border: none;
}
QPushButton:hover {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 5px;
}
"""

estiloWarning = """
QMessageBox {
    background-color: #f5f7fa;
    font-family: 'Segoe UI', 'Arial';
    font-size: 14px;
    color: #2c3e50;
    border-radius: 12px;
    padding: 10px;
}

QLabel {
    color: #2c3e50;
    font-size: 14px;
}

QPushButton {
    background-color: #e0e4ec;
    color: #2c3e50;
    border: none;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 13px;
    min-width: 70px;
}

QPushButton:hover {
    background-color: #d4d9e1;
}

QPushButton:pressed {
    background-color: #c8cdd6;
}
"""


estiloTree = """
        QTreeWidget {
            background-color: transparent;  /* Azul rey para el fondo del árbol */
            color: white;                      /* Texto en blanco */
            border: none;                      /* Sin bordes */
            font-size: 12pt;                   /* Tamaño de fuente */
        }
        
        QTreeWidget::item {
            border: none;                      /* Sin bordes para los ítems */
            background-color: rgb(0, 31, 61);   /* Fondo azul rey para los ítems */
            padding: 5px;                      /* Espaciado alrededor de los ítems */
        }
        
        QTreeWidget::item:selected {
            background-color: rgb(0, 90, 141);  /* Azul más claro para el ítem seleccionado */
        }
        
        QTreeWidget::item:!selected {
            background-color: rgb(0, 31, 61);   /* Fondo normal de los ítems no seleccionados */
        }
        
        QTreeWidget::header {
            background-color: rgb(0, 31, 61);  /* Azul rey para el encabezado */
            color: white;                      /* Texto del encabezado en blanco */
            font-size: 14pt;                   /* Tamaño de fuente del encabezado */
        }
        
        QTreeWidget::branch {
            background-color: transparent;
        }
        
        QHeaderView::section {
            background-color: rgb(0, 31, 61);  /* Azul rey para las secciones de encabezado */
            color: white;                      /* Texto en blanco */
            padding: 5px;
            border: none;
        }
    
    """


# ─────────────────────────────────────────────────────────────
#  Componentes compartidos entre pantallas
#  Referencia visual: formulario de Tiempo de Reverberación
#  (Vista/archivos_qtDesigner/tiempoReverberacionUI.ui). Mismos valores
#  que ya usa ese formulario; centralizados para que el resto de
#  pantallas (resultados, Inteligibilidad, Base de Datos) los reutilicen
#  en vez de repetirlos.
# ─────────────────────────────────────────────────────────────

# Botón circular "Atrás" (42x42, borde tenue; hover/pressed rellenan).
estiloBotonAtras = """
QPushButton {
    background-color: transparent;
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 21px;
}
QPushButton:hover { background-color: rgba(255,255,255,0.18); border: 1px solid white; }
QPushButton:pressed { background-color: rgba(255,255,255,0.38); }
"""


def estiloBarraSuperior(nombre):
    """Barra superior oscura con línea inferior (frame con objectName `nombre`)."""
    return (
        f"QFrame#{nombre} {{ background-color: rgba(0,0,0,0.25); "
        f"border-bottom: 1px solid rgba(255,255,255,0.13); }}"
    )


def estiloBarraInferior(nombre, primario, compacto=False):
    """
    Barra inferior oscura con línea superior. Los QPushButton hijos son
    secundarios (contorno tenue); el que tenga objectName `primario` es la
    acción principal (acento azul, mismo aspecto y tamaño que el botón
    "Iniciar Análisis" del formulario: 224x34 renderizado). `compacto`
    reduce el ancho de los botones para ventanas muy angostas (< ~560 px),
    donde dos botones de 224 px no caben en una fila.
    """
    relleno, ancho_min, ancho_max = ("8px 12px", 110, 210) if compacto else ("8px 20px", 180, 210)
    return f"""
QFrame#{nombre} {{
    background-color: rgba(0,0,0,0.22);
    border-top: 1px solid rgba(255,255,255,0.12);
}}
QPushButton {{
    background-color: rgba(255,255,255,0.10);
    border: 1.5px solid rgba(255,255,255,0.40);
    color: rgba(255,255,255,0.90);
    font-weight: bold;
    font-size: 12px;
    border-radius: 12px;
    padding: {relleno};
    min-width: {ancho_min}px;
    max-width: {ancho_max}px;
}}
QPushButton:hover {{ background-color: rgba(255,255,255,0.22); border-color: white; color: white; }}
QPushButton:pressed {{ background-color: rgba(255,255,255,0.38); color: white; }}
QPushButton:disabled {{
    background-color: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.18);
    color: rgba(255,255,255,0.30);
}}
QPushButton#{primario} {{
    background-color: rgba(126,200,247,0.18);
    border: 1.5px solid {paleta.ACENTO};
    color: {paleta.ACENTO};
}}
QPushButton#{primario}:hover {{
    background-color: rgba(126,200,247,0.35);
    color: white;
    border-color: white;
}}
QPushButton#{primario}:pressed {{ background-color: rgba(126,200,247,0.55); color: white; }}
QPushButton#{primario}:disabled {{
    background-color: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.18);
    color: rgba(255,255,255,0.30);
}}
"""


def estiloTarjeta(nombre, fondo="rgba(255,255,255,0.06)", borde="rgba(255,255,255,0.22)"):
    """Tarjeta translúcida (mismo tratamiento que los QGroupBox del formulario de RT)."""
    return (
        f"QFrame#{nombre} {{ background-color: {fondo}; border: 1px solid {borde}; "
        f"border-radius: 10px; }}"
    )


def estiloTexto(tamano_pt, color=paleta.TEXTO_PRINCIPAL, negrita=False):
    """QSS para un QLabel de texto sobre fondo oscuro (sin fondo ni borde propios)."""
    peso = "bold" if negrita else "normal"
    return (
        f"QLabel {{ background: transparent; border: none; color: {color}; "
        f"font-size: {tamano_pt}pt; font-weight: {peso}; }}"
    )

