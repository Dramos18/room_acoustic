import re

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCompleter, QSpinBox, QLineEdit, QComboBox, QLabel, QCheckBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from Controlador.Controlador import obtener_lista_materiales
from Vista.graficas.estilo import estiloObjeto
from Vista.objetoAdicional import Ui_formObjetoAdicional  # Asumiendo que tienes este ui

class ManejadorObjetoAdicional:
    def __init__(self, layout_padre: QVBoxLayout, checkbox: QCheckBox):
        self.layout_padre = layout_padre
        self.limite = 5
        self.lista_widgets = []
        self.loader = QUiLoader()
        self.materiales = obtener_lista_materiales()
        self.checkbox = checkbox

        self.agregar_nuevo_objeto()  # uno por defecto


    def cargar_widget_objeto(self):
        ui_file = QFile("Vista/objetoAdicional.ui")
        ui_file.open(QFile.ReadOnly)
        widget = self.loader.load(ui_file)
        ui_file.close()

        widget.setStyleSheet(estiloObjeto)
        return widget

    def agregar_nuevo_objeto(self):
        if len(self.lista_widgets) >= self.limite:
            return

        widget = self.cargar_widget_objeto()

        self.llenar_combobox_materiales(widget)

        btn_agregar = widget.findChild(QWidget, "botonAgregar_2")
        btn_eliminar = widget.findChild(QWidget, "botonEliminar_2")

        btn_agregar.clicked.connect(self.agregar_nuevo_objeto)
        btn_eliminar.clicked.connect(lambda: self.eliminar_objeto(widget))

        btn_agregar.setIcon(QIcon("Vista/graficas/iconos/agregar.png"))
        btn_eliminar.setIcon(QIcon("Vista/graficas/iconos/quitar.png"))

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
            btn_eliminar = widget.findChild(QWidget, "botonEliminar_2")
            btn_eliminar.setEnabled(len(self.lista_widgets) > 1)

    def llenar_combobox_materiales(self, widget):
        combo = widget.findChild(QWidget, "cbObjAdicional")  # nombre exacto en el ui
        if combo:
            combo.setEditable(True)
            completer = QCompleter(self.materiales)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            combo.setCompleter(completer)
            combo.clear()
            combo.addItems(self.materiales)

    def obtener_datos(self):
        datos = []
        for widget in self.lista_widgets:
            nombre = widget.findChild(QWidget, "lineObjAdicional").text()
            material = widget.findChild(QWidget, "cbObjAdicional").currentText()
            cantidad = widget.findChild(QSpinBox, "spinBoxCantidad").value()
            datos.append({
                "nombre": nombre,
                "material": material,
                "cantidad": int(cantidad) if cantidad else 0
            })
        return datos

    def validar_y_obtener_datos(self):
        if not self.checkbox.isChecked():
            return None
        datos = []
        hay_errores = False

        for i, widget in enumerate(self.lista_widgets):
            nombre = widget.findChild(QLineEdit, "lineObjAdicional")
            material = widget.findChild(QComboBox, "cbObjAdicional")
            cantidad = widget.findChild(QSpinBox, "spinBoxCantidad")
            label_error = widget.findChild(QLabel, "labelErrorObjAdicional")

            errores = []

            # Validar nombre
            if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ\s]{2,30}", nombre.text()):
                nombre.setStyleSheet("border: 1px solid red;")
                errores.append("Nombre inválido. Solo letras (2-30 caracteres).")
            else:
                nombre.setStyleSheet("")

            # Validar material
            if material.currentText() not in self.materiales:
                material.setStyleSheet("border: 1px solid red;")
                errores.append("Seleccione un material válido.")
            else:
                material.setStyleSheet("")

            # Validar área
            try:
                cant_objeto = float(cantidad.text())
                if cant_objeto <= 0:
                    raise ValueError
                cantidad.setStyleSheet("")
            except ValueError:
                cantidad.setStyleSheet("border: 1px solid red;")
                errores.append("Ingrese una cantidad")

            # Mostrar errores en el QLabel correspondiente
            if errores:
                hay_errores = True
                if label_error:
                    label_error.setText("⚠️ " + "\n".join(errores))
            else:
                if label_error:
                    label_error.setText("")  # Limpiar si no hay errores
                datos.append({
                    "nombre": nombre.text(),
                    "material": material.currentText(),
                    "cantidad": cant_objeto
                })

        if hay_errores:
            return None  # No pasar al cálculo si hay errores
        else:
            return {
                "objetos_adicionales": datos
            }
