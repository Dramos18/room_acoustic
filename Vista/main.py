import sys
from PySide6.QtCore import Slot, QSize, Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QWidget

from Vista.archivos_pyGenerados.iniciarAnalisis import Ui_ventanaIniciarAnalisis
from Vista.ventanaBarraTitulo import VentanaConBarra
from Vista.archivos_pyGenerados.ventanaPrincipal import Ui_formVentanaPrincipal
from Vista.ventIniciarAnalisis import VentanaIniciarAnalisis


class VentanaPrincipal(VentanaConBarra):
    """Ventana principal de la aplicación."""

    def __init__(self):
        contenido = QWidget()
        self.ui = Ui_formVentanaPrincipal()
        self.ui.setupUi(contenido)

        super().__init__(contenido)

        self.resize(900, 600)

        # ── GIF principal ──────────────────────────────────────────────────────
        self.movie = QMovie("../Recursos/gifs/logoMainGIF.gif")
        self.ui.labelSuperior.setMovie(self.movie)
        self.ui.labelSuperior.setAlignment(Qt.AlignCenter)

        # Tamaño del GIF ligeramente mayor para aprovechar el nuevo panel
        self.movie.setScaledSize(QSize(360, 360))

        self.movie.start()

        # ── Páginas del stackedWidget ──────────────────────────────────────────
        # Página de "Iniciar análisis" (UI base generada por uic)
        self.iniciar_analisis_widget_base = QWidget()
        self.ui_iniciar = Ui_ventanaIniciarAnalisis()
        self.ui_iniciar.setupUi(self.iniciar_analisis_widget_base)
        self.ui.stackedWidget.addWidget(self.iniciar_analisis_widget_base)

        # Widget lógico de "Iniciar análisis" (con comportamiento real)
        self.iniciar_analisis_widget = VentanaIniciarAnalisis(
            stacked_widget=self.ui.stackedWidget
        )
        self.ui.stackedWidget.addWidget(self.iniciar_analisis_widget)

        # ── Conexiones ────────────────────────────────────────────────────────
        self.setup_events()
        self.setup_iniciar_analisis_events()

    def setup_events(self):
        self.ui.botonIniciar.clicked.connect(self.mostrar_iniciar_analisis)
        # botonAyuda: conectar aquí cuando la sección de ayuda esté lista
        # self.ui.botonAyuda.clicked.connect(self.mostrar_ayuda)

    def setup_iniciar_analisis_events(self):
        self.ui_iniciar.botonRegresar.clicked.connect(self.volver_a_inicio)

    @Slot()
    def mostrar_iniciar_analisis(self):
        self.ui.stackedWidget.setCurrentWidget(self.iniciar_analisis_widget)

    @Slot()
    def volver_a_inicio(self):
        self.ui.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    print("Inicializando aplicación...")
    app = QApplication(sys.argv)

    try:
        ventana = VentanaPrincipal()
        print("Ventana creada correctamente.")
        ventana.showMaximized()
    except Exception as e:
        print(f"Error al mostrar la ventana: {e}")

    sys.exit(app.exec())