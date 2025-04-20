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
    image: url(Vista/graficas/iconos/controlar.png);
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

/* Lista desplegable */
QComboBox QAbstractItemView {
    background-color: rgba(255, 255, 255);
    background: withe;
    color: rgba(255, 255, 255);
    selection-background-color: #f0f0f0;
    selection-color: black;
    border: 1px solid #ccc;
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
