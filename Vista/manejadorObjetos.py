import re

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QCompleter, QLineEdit,
    QComboBox, QLabel, QCheckBox
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

from Controlador.Controlador import obtener_lista_materiales
from Recursos.estilos.estilo import estiloObjeto

# ── Estilos de validación ────────────────────────────────────
_ESTILO_ERROR  = "border: 1px solid rgba(248,113,113,0.90); background: rgba(248,113,113,0.10);"
_ESTILO_OK     = ""


class ManejadorObjetosSuperficie:
    """
    Gestiona la lista dinámica de objetos adheridos a una superficie.
    Cada objeto tiene: nombre, material y área.
    """

    def __init__(self, layout_padre: QVBoxLayout, area_maxima: float,
                 checkbox: QCheckBox, label_error: QLabel):
        self.label_error  = label_error
        self.layout_padre = layout_padre
        self.area_maxima  = area_maxima
        self.limite       = 4
        self.lista_widgets = []
        self.loader        = QUiLoader()
        self.materiales    = obtener_lista_materiales()
        self.checkbox      = checkbox

        self.agregar_nuevo_objeto()   # primer objeto por defecto

    # ── Carga del widget desde .ui ──────────────────────────────

    def cargar_widget_objeto(self):
        ui_file = QFile("../Vista/archivos_qtDesigner/objetoSuperficie.ui")
        ui_file.open(QFile.ReadOnly)
        widget = self.loader.load(ui_file)
        ui_file.close()
        widget.setStyleSheet(estiloObjeto)
        return widget

    # ── CRUD de objetos ─────────────────────────────────────────

    def agregar_nuevo_objeto(self):
        if len(self.lista_widgets) >= self.limite:
            return

        widget = self.cargar_widget_objeto()
        self.llenar_combobox_materiales(widget)

        btn_agregar  = widget.findChild(QWidget, "botonAgregar")
        btn_eliminar = widget.findChild(QWidget, "botonEliminar")

        btn_agregar.clicked.connect(self.agregar_nuevo_objeto)
        btn_eliminar.clicked.connect(lambda: self.eliminar_objeto(widget))

        btn_agregar.setIcon(QIcon("../Recursos/iconos/agregar.png"))
        btn_eliminar.setIcon(QIcon("../Recursos/iconos/quitar.png"))

        self.lista_widgets.append(widget)
        self.layout_padre.addWidget(widget)
        self.validar_botones()

    def eliminar_objeto(self, widget):
        if len(self.lista_widgets) <= 1:
            return
        widget.setParent(None)
        self.lista_widgets.remove(widget)
        self.validar_botones()

    def validar_botones(self):
        for widget in self.lista_widgets:
            btn = widget.findChild(QWidget, "botonEliminar")
            btn.setEnabled(len(self.lista_widgets) > 1)

    # ── ComboBox ────────────────────────────────────────────────

    def llenar_combobox_materiales(self, widget):
        combo = widget.findChild(QWidget, "cbObjFrontal")
        if combo is None:
            return
        combo.setEditable(True)
        completer = QCompleter(self.materiales)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        combo.setCompleter(completer)
        combo.clear()
        combo.addItems(self.materiales)

    # ── Lectura de datos (sin validación) ───────────────────────

    def obtener_datos(self):
        datos = []
        for widget in self.lista_widgets:
            nombre = widget.findChild(QWidget, "lineObjFrontal").text()
            material = widget.findChild(QWidget, "cbObjFrontal").currentText()
            area_raw = widget.findChild(QWidget, "lineObjAreaFrontal").text()
            datos.append({
                "nombre":   nombre,
                "material": material,
                "area":     float(area_raw) if area_raw else 0,
            })
        return datos

    # ── Validación completa ─────────────────────────────────────

    def validar_y_obtener_datos(self):
        """
        Valida todos los objetos de la superficie.
        Retorna None si hay errores, o el dict con 'objetos_adheridos' si todo es válido.
        Si el checkbox no está activo, retorna None sin error (el llamador lo ignora).
        """
        if not self.checkbox.isChecked():
            return None

        datos = []
        hay_errores = False
        suma_areas  = 0.0

        for widget in self.lista_widgets:
            nombre   = widget.findChild(QLineEdit, "lineObjFrontal")
            material = widget.findChild(QComboBox, "cbObjFrontal")
            area     = widget.findChild(QLineEdit, "lineObjAreaFrontal")

            errores_fila = []

            # ── Validar nombre ──
            if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ\s]{2,30}", nombre.text().strip()):
                nombre.setStyleSheet(_ESTILO_ERROR)
                errores_fila.append("Nombre inválido (solo letras, 2-30 caracteres).")
            else:
                nombre.setStyleSheet(_ESTILO_OK)

            # ── Validar material ──
            if material.currentText() not in self.materiales:
                material.setStyleSheet(_ESTILO_ERROR)
                errores_fila.append("Seleccione un material válido.")
            else:
                material.setStyleSheet(_ESTILO_OK)

            # ── Validar área — SIEMPRE se valida, independiente del material ──
            area_valor = None
            try:
                area_valor = float(area.text().replace(",", "."))
                if area_valor <= 0:
                    raise ValueError("El área debe ser mayor a 0.")
                if self.area_maxima and area_valor > self.area_maxima:
                    raise ValueError(f"El área no puede superar {self.area_maxima} m².")
                area.setStyleSheet(_ESTILO_OK)
                suma_areas += area_valor
            except ValueError as e:
                area.setStyleSheet(_ESTILO_ERROR)
                errores_fila.append(f"Área inválida: {e}")

            if errores_fila:
                hay_errores = True
                if self.label_error:
                    self.label_error.setText("⚠ " + " · ".join(errores_fila))
            else:
                if area_valor is not None:
                    datos.append({
                        "nombre":   nombre.text().strip(),
                        "material": material.currentText(),
                        "area":     area_valor,
                    })

        if hay_errores:
            return None

        # Limpiar error si todo OK
        if self.label_error:
            self.label_error.setText("")
        return {"objetos_adheridos": datos}