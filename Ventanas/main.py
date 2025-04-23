import sys
from PySide6.QtCore import Slot, QSize, Qt
from PySide6.QtGui import QMovie, QIcon
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

        # Cargar y añadir la página de "Iniciar análisis" al stackedWidget
        self.iniciar_analisis_widget = QWidget()
        self.ui_iniciar = Ui_ventanaIniciarAnalisis()
        self.ui_iniciar.setupUi(self.iniciar_analisis_widget)
        self.ui.stackedWidget.addWidget(self.iniciar_analisis_widget)

        self.iniciar_analisis_widget = VentanaIniciarAnalisis(stacked_widget=self.ui.stackedWidget)
        self.ui.stackedWidget.addWidget(self.iniciar_analisis_widget)

        self.setup_events()
        self.setup_iniciar_analisis_events()

    def setup_events(self):
        self.ui.botonIniciar.clicked.connect(self.mostrar_iniciar_analisis)

    def setup_iniciar_analisis_events(self):
        # Aquí conectamos los botones de iniciar análisis
        self.ui_iniciar.botonRegresar.clicked.connect(self.volver_a_inicio)

    @Slot()
    def mostrar_iniciar_analisis(self):
        self.ui.stackedWidget.setCurrentWidget(self.iniciar_analisis_widget)

    @Slot()
    def volver_a_inicio(self):
        self.ui.stackedWidget.setCurrentIndex(0)








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

