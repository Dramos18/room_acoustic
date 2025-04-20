import re

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCompleter, QMessageBox, QLineEdit, QComboBox, QLabel, QCheckBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from Controlador.Controlador import obtener_lista_materiales
from Vista.graficas.estilo import estiloFrameRT, estiloObjeto
from Vista.objetoSuperficie import Ui_formObjetoSuperficie
import os

class ManejadorObjetosSuperficie:
    def __init__(self, layout_padre: QVBoxLayout, area_maxima: float,  checkbox: QCheckBox, label_error: QLabel):
        self.label_error = label_error
        self.layout_padre = layout_padre
        self.area_maxima = area_maxima
        self.limite = 4
        self.lista_widgets = []
        self.loader = QUiLoader()
        self.materiales = obtener_lista_materiales()
        self.checkbox = checkbox


        self.agregar_nuevo_objeto()  # uno por defecto



    def cargar_widget_objeto(self):
        ui_file = QFile("Vista/objetoSuperficie.ui")
        ui_file.open(QFile.ReadOnly)
        widget = self.loader.load(ui_file)

        widget.setStyleSheet(estiloObjeto)
        ui_file.close()


        return widget

    def agregar_nuevo_objeto(self):
        if len(self.lista_widgets) >= self.limite:
            return

        widget = self.cargar_widget_objeto()

        #llenar combo box
        self.llenar_combobox_materiales(widget)

        # Conectar botones
        btn_agregar = widget.findChild(QWidget, "botonAgregar")
        btn_eliminar = widget.findChild(QWidget, "botonEliminar")

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
            btn_eliminar = widget.findChild(QWidget, "botonEliminar")
            btn_eliminar.setEnabled(len(self.lista_widgets) > 1)

    def llenar_combobox_materiales(self, widget):
        combo = widget.findChild(QWidget, "cbObjFrontal")  # Usa el nombre exacto que le diste en Qt Designer
        combo.setEditable(True)

        completer = QCompleter(self.materiales)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        combo.setCompleter(completer)

        if combo:
            combo.clear()
            combo.addItems(self.materiales)



    def obtener_datos(self):
        datos = []
        for widget in self.lista_widgets:
            nombre = widget.findChild(QWidget, "lineObjFrontal").text()
            material = widget.findChild(QWidget, "cbObjFrontal").currentText()
            area = widget.findChild(QWidget, "lineObjAreaFrontal").text()
            datos.append({
                "nombre": nombre,
                "material": material,
                "area": float(area) if area else 0
            })
        return datos

    def validar_y_obtener_datos(self):
        if not self.checkbox.isChecked():
            return None
        datos = []
        hay_errores = False
        suma_areas_objetos = 0

        for i, widget in enumerate(self.lista_widgets):
            nombre = widget.findChild(QLineEdit, "lineObjFrontal")
            material = widget.findChild(QComboBox, "cbObjFrontal")
            area = widget.findChild(QLineEdit, "lineObjAreaFrontal")

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
                # Validar área
                try:
                    area_valor = float(area.text())
                    if area_valor <= 0:
                        raise ValueError
                    area.setStyleSheet("")
                    suma_areas_objetos += area_valor  # Sumar el área validada al total
                except ValueError:
                    area.setStyleSheet("border: 1px solid red;")
                    errores.append("Área inválida. Debe ser un número positivo.")

            # Mostrar errores en el QLabel correspondiente
            if errores:
                hay_errores = True
                if self.label_error:
                    self.label_error.setText("⚠️ " + "\n".join(errores))
            else:
                if self.label_error:
                    self.label_error.setText("")  # Limpiar si no hay errores
                datos.append({
                    "nombre": nombre.text(),
                    "material": material.currentText(),
                    "area": area_valor
                })

        if hay_errores:
            return None  # No pasar al cálculo si hay errores
        else:
            return {
                "objetos_adheridos": datos
            }


