import re

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QCompleter, QSpinBox,
    QLineEdit, QComboBox, QLabel, QCheckBox
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

from Controlador.Controlador import obtener_lista_materiales
from Recursos.estilos.estilo import estiloObjeto

# ── Estilos de validación ────────────────────────────────────
_ESTILO_ERROR = "border: 1px solid rgba(248,113,113,0.90); background: rgba(248,113,113,0.10);"
_ESTILO_OK    = ""


class ManejadorObjetoAdicional:
    """
    Gestiona la lista dinámica de objetos adicionales dentro del aula.
    Cada objeto tiene: nombre, material y cantidad.
    """

    def __init__(self, layout_padre: QVBoxLayout, checkbox: QCheckBox):
        self.layout_padre  = layout_padre
        self.limite        = 5
        self.lista_widgets = []
        self.loader        = QUiLoader()
        self.materiales    = obtener_lista_materiales()
        self.checkbox      = checkbox

        self.agregar_nuevo_objeto()   # uno por defecto

    # ── Carga del widget desde .ui ──────────────────────────────

    def cargar_widget_objeto(self):
        ui_file = QFile("../Vista/archivos_qtDesigner/objetoAdicional.ui")
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

        btn_agregar  = widget.findChild(QWidget, "botonAgregar_2")
        btn_eliminar = widget.findChild(QWidget, "botonEliminar_2")

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
            btn = widget.findChild(QWidget, "botonEliminar_2")
            btn.setEnabled(len(self.lista_widgets) > 1)

    # ── ComboBox ────────────────────────────────────────────────

    def llenar_combobox_materiales(self, widget):
        combo = widget.findChild(QWidget, "cbObjAdicional")
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
            nombre   = widget.findChild(QWidget, "lineObjAdicional").text()
            material = widget.findChild(QWidget, "cbObjAdicional").currentText()
            cantidad = widget.findChild(QSpinBox, "spinBoxCantidad").value()   # FIX: .value() no .text()
            datos.append({
                "nombre":   nombre,
                "material": material,
                "cantidad": int(cantidad),
            })
        return datos

    # ── Validación completa ─────────────────────────────────────

    def validar_y_obtener_datos(self):
        """
        Valida todos los objetos adicionales.
        Retorna None si el checkbox está desmarcado o si hay errores de validación.
        Retorna {'objetos_adicionales': [...]} si todo es válido.
        """
        if not self.checkbox.isChecked():
            return None

        datos      = []
        hay_errores = False

        for widget in self.lista_widgets:
            nombre        = widget.findChild(QLineEdit,  "lineObjAdicional")
            material      = widget.findChild(QComboBox,  "cbObjAdicional")
            cantidad      = widget.findChild(QSpinBox,   "spinBoxCantidad")
            label_error   = widget.findChild(QLabel,     "labelErrorObjAdicional")

            errores_fila = []

            # ── Validar nombre ──
            if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ\s]{2,30}", nombre.text().strip()):
                nombre.setStyleSheet(_ESTILO_ERROR)
                errores_fila.append("Nombre inválido (2-30 letras).")
            else:
                nombre.setStyleSheet(_ESTILO_OK)

            # ── Validar material ──
            if material.currentText() not in self.materiales:
                material.setStyleSheet(_ESTILO_ERROR)
                errores_fila.append("Seleccione un material válido.")
            else:
                material.setStyleSheet(_ESTILO_OK)

            # ── Validar cantidad — FIX: usar .value() en QSpinBox ──
            cant_valor = cantidad.value()   # QSpinBox.value() devuelve int, nunca falla
            if cant_valor <= 0:
                cantidad.setStyleSheet(_ESTILO_ERROR)
                errores_fila.append("La cantidad debe ser mayor a 0.")
            else:
                cantidad.setStyleSheet(_ESTILO_OK)

            # ── Mostrar / limpiar error inline ──
            if label_error:
                label_error.setText("⚠ " + " · ".join(errores_fila) if errores_fila else "")

            if errores_fila:
                hay_errores = True
            else:
                datos.append({
                    "nombre":   nombre.text().strip(),
                    "material": material.currentText(),
                    "cantidad": cant_valor,
                })

        if hay_errores:
            return None

        return {"objetos_adicionales": datos}