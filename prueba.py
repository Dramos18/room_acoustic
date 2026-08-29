import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#from Vista.interfaz import Ui_MainWindow  # Asegúrate de que el nombre de la clase sea correcto
from Controlador.Controlador import obtener_lista_materiales
from Recursos.MainWindow import Ui_MainWindow
from Vista.archivos_pyGenerados.iniciarAnalisis import Ui_ventanaIniciarAnalisis


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)  # Configura la UI dentro de la ventana



        def abrir_ventana_analisis():
            self.iniciarAnalisis = Ui_ventanaIniciarAnalisis()
            self.iniciarAnalisis.show()

        materiales = obtener_lista_materiales()
        self.comboBox.addItems(materiales)
        # Conectar el botón al evento (sin paréntesis)
        self.botonEnviar.clicked.connect(self.miFuncion)




    def miFuncion(self):
        print("¡El botón fue presionado!")
        texto = self.campoTexto.text()  # Obtener texto del QLineEdit
        self.eqiqueta.setText(texto)


          # Agregar materiales al ComboBox




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

