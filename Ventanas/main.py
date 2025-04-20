import sys
from PySide6.QtCore import Slot, QSize, Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QWidget
from Vista.iniciarAnalisis import  Ui_ventanaIniciarAnalisis # importa tu clase generada
from Ventanas.ventanaBarraTitulo import VentanaConBarra
from Vista.ventanaPrincipal import Ui_formVentanaPrincipal
from Ventanas.ventIniciarAnalisis import VentanaIniciarAnalisis


class VentanaPrincipal(VentanaConBarra):
    """
       Esta es la ventana principal.
       """

    def __init__(self):
        contenido = QWidget()
        self.ui = Ui_formVentanaPrincipal()
        self.ui.setupUi(contenido)

        # Llamar a la superclase con la barra
        super().__init__(contenido)

        self.resize(800, 600)

        self.setup_events()

        self.ui.labelMainTittle.setAlignment(Qt.AlignCenter)

        # Cargar el GIF con QMovie
        self.movie = QMovie("Vista/graficas/iconos/gifmicro.gif")  # Cambia esta ruta
        self.ui.label.setMovie(self.movie)
        self.ui.label.setAlignment(Qt.AlignCenter)
        self.movie.setScaledSize(QSize(400, 400))
        self.ui.label.resize(self.movie.scaledSize())


        # Iniciar animación
        self.movie.start()

    def setup_events(self):

        # Conectar el botón "Iniciar Análisis"
        self.ui.botonIniciar.clicked.connect(self.abrir_iniciar_analisis)

        # Los otros botones (Opcional: los puedes conectar a otros métodos)
        #self.ui.btnOpciones.clicked.connect(self.mostrar_opciones)
        #self.ui.btnAyuda.clicked.connect(self.mostrar_ayuda)

    @Slot()
    def abrir_iniciar_analisis(self):
        """
        Abre la ventana de formulario para 'Iniciar Análisis'.
        """
        self.ventana_iniciar = VentanaIniciarAnalisis(ventana_anterior=self)
        self.ventana_iniciar.show()
        self.hide()


    @Slot()
    def mostrar_opciones(self):
        """
        Acción para el botón Opciones (puedes implementarlo después).
        """
        print("El botón Opciones fue presionado.")

    @Slot()
    def mostrar_ayuda(self):
        """
        Acción para el botón Ayuda (puedes implementarlo después).
        """
        print("El botón Ayuda fue presionado.")








if __name__ == "__main__":
    print("Inicializando aplicación...")  # Depuración inicial
    app = QApplication(sys.argv)

    try:
        ventana = VentanaPrincipal()
        print("Ventana creada correctamente.")
        ventana.show()
    except Exception as e:
        print(f"Error al mostrar la ventana: {e}")  # Muestra el error si ocurre

    sys.exit(app.exec())

