from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QTreeWidgetItem, QHeaderView, QMessageBox

from Controlador.controlTR import procesar_datos
from Vista.ventGraficaRT import VentanaGraficaRT
from Vista.ventTransicion import VentanaTransicion
from Vista.archivos_pyGenerados.infoBD import Ui_Form
from Recursos.estilos.estilo import estiloWarning
from Datos.salones import salones


class VentanaInfoBaseDatos(QWidget):
    """
    Esta clase representa la ventana de "Información Base de datos".
    Es una subclase de QWidget que carga el diseño de iniciarAnalisis.
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.indice_anterior = indice_anterior
        self.stacked_widget = stacked_widget

        # Crear una lista de salones
        self.salones = salones

        self.ui.botonAtras.setIcon(QIcon("Recursos/estilos/iconos/angulo-izquierdo.png"))

        combo_box = self.ui.comboBox
        label_aula = self.ui.labelNumeroAula
        label_alto = self.ui.labelAlto
        label_ancho = self.ui.labelAncho
        label_largo = self.ui.labelLargo
        tree_widget = self.ui.treeWidget

        self.cargar_salones(combo_box, self.salones)
        combo_box.currentIndexChanged.connect(lambda: self.mostrar_informacion(combo_box, label_aula, label_largo, label_alto, label_ancho, tree_widget, self.salones))

        self.setup_events()

    def setup_events(self):
        self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)
        self.ui.botonIniciarAnalisis.clicked.connect(self.iniciar_analisis)

    def regresar_a_ventana_anterior(self):
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)

    def cargar_salones(self, combo_box, salones):
          # Asegúrate de incluir todos los salones

        # Limpiar el ComboBox antes de agregar elementos
        combo_box.clear()

        combo_box.addItem("Seleccionar")

        # Agregar las claves de los salones (nombre del aula) al ComboBox
        for salon in salones:
            aula_nombre = salon['Tipo']
            combo_box.addItem(aula_nombre)

    def mostrar_informacion(self, combo_box, label_aula, label_largo, label_alto, label_ancho, tree_widget, salones):
        # Obtener el índice seleccionado en el ComboBox
        selected_index = combo_box.currentIndex()

        # Verificar si la selección es diferente de "Seleccionar"
        if selected_index == 0:
            label_aula.setText("No seleccionado")
            label_largo.setText(" ")
            label_alto.setText(" ")
            label_ancho.setText(" ")
            tree_widget.clear()  # Limpiar el TreeWidget
            return

        # Obtener el diccionario del salón seleccionado
        salon_seleccionado = salones[selected_index - 1]  # Restar 1 porque el primer item es "Seleccionar"

        # Mostrar el nombre del aula
        label_aula.setText(salon_seleccionado['aulas'])

        # Mostrar las dimensiones del aula
        dimensiones = salon_seleccionado['dimensiones']
        label_largo.setText(f"{dimensiones['largo']}m")
        label_alto.setText(f"{dimensiones['altura']}m")
        label_ancho.setText(f"{dimensiones['ancho']}m")


        # Limpiar el TreeWidget antes de agregar los nuevos datos
        tree_widget.clear()

        tree_widget.setHeaderLabels(["Nombre", "Material", "Área/Cantidad"])

        # Establecer el ancho predeterminado de las columnas
        tree_widget.setColumnWidth(0, 250)  # Ancho de la columna "Nombre"
        tree_widget.setColumnWidth(1, 350)  # Ancho de la columna "Material"
        tree_widget.setColumnWidth(2, 150)  # Ancho de la columna "Área/Cantidad"

        # Hacer que las columnas sean redimensionables
        header = tree_widget.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  # Redimensionar las columnas al contenido
        header.setStretchLastSection(True)

        # Mostrar las zonas (Frontal, Trasera, etc.)
        for zona, datos in salon_seleccionado['materiales'].items():
            zona_item = QTreeWidgetItem(tree_widget)
            zona_item.setText(0, zona)  # Nombre de la zona (Frontal, Trasera, etc.)
            zona_item.setText(1, datos['material'])  # Nombre del material

            # Si tiene objetos adheridos, mostrarlos
            if 'objetos_adheridos' in datos:
                for objeto in datos['objetos_adheridos']:
                    objeto_item = QTreeWidgetItem(zona_item)
                    objeto_item.setText(0, objeto['nombre'])  # Nombre del objeto
                    objeto_item.setText(1, objeto['material'])  # Material del objeto
                    objeto_item.setText(2, str(objeto['area']))  # Área del objeto

        # Mostrar los objetos adicionales fuera de las zonas
        objetos_adicionales_item = QTreeWidgetItem(tree_widget)
        objetos_adicionales_item.setText(0, "Objetos Adicionales")  # Título para los objetos adicionales
        for obj in salon_seleccionado['objetos_adicionales']:
            objeto_item = QTreeWidgetItem(tree_widget)
            objeto_item.setText(0, obj['nombre'])  # Nombre del objeto adicional
            objeto_item.setText(1, obj['material'])  # Material del objeto adicional
            objeto_item.setText(2, str(obj['cantidad']))  # Cantidad de objetos

        for index in range(tree_widget.topLevelItemCount()):
            item = tree_widget.topLevelItem(index)
            if item.childCount() > 0:  # Si el nodo tiene hijos
                item.setExpanded(False)  # Colapsar el nodo inicialmente para mostrar la flecha
                item.setIcon(0, QIcon())

    def enviar_obtener_datos_controlador(self, salones):
        """
        Enviar diccionario generado al Controlador para procesamiento.
        """
        if salones is None:
            # Muestra error en la interfaz si los datos son inválidos
            print("Error en la validación de superficies.")
        else:
            # Envía los datos al controlador
            print("yendo a procesar datos")
            resultados = procesar_datos(salones)
            print("diccionario recibido por el controlador", resultados)
            return resultados

    def iniciar_analisis(self):
        salones = self.salones
        # Obtener el índice seleccionado en el ComboBox
        selected_index = self.ui.comboBox.currentIndex()

        # Si un salón ha sido seleccionado
        if selected_index != 0:

            transicion = VentanaTransicion("Recursos/estilos/iconos/ondas.gif", duracion_ms=2000, parent=self)
            salon_seleccionado = salones[selected_index - 1]  # Obtener el diccionario del salón seleccionado
            print(salon_seleccionado)
            self.indice = self.stacked_widget.currentIndex()
            resultado = self.enviar_obtener_datos_controlador(salon_seleccionado)
            ventana_grafica = VentanaGraficaRT(stacked_widget=self.stacked_widget, indice_anterior=self.indice,
                                               resultados=resultado)
            ventana_grafica.indice_anterior = self.stacked_widget.currentIndex()

            self.stacked_widget.addWidget(ventana_grafica)
            transicion.exec()
            self.stacked_widget.setCurrentWidget(ventana_grafica)

        else:
            msgError = QMessageBox(self)
            msgError.setIcon(QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Seleccione un un tipo de aula de la base de datos")
            msgError.setStyleSheet(estiloWarning)
            msgError.exec()
            return