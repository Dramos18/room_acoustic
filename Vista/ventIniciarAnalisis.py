from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget

from Vista.ventTiempoReverberacion import VentanaTiempoReverberacion
from Vista.ventInteligibilidad import VentanaInteligibiliad
from Vista.ventTransicion import VentanaTransicion
from Vista.ventInfoBD import VentanaInfoBaseDatos
from Vista.archivos_pyGenerados.iniciarAnalisis import  Ui_ventanaIniciarAnalisis # importa tu clase generada


class VentanaIniciarAnalisis(QWidget):
    """
    Esta clase representa la pantalla de 'Iniciar Análisis', usada dentro de la ventana principal.
    No usa barra de título personalizada, ya que eso lo maneja VentanaPrincipal.
    """

    def __init__(self, stacked_widget, parent=None):
        super().__init__(parent)
        self.ui = Ui_ventanaIniciarAnalisis()
        self.ui.setupUi(self)

        self.stacked_widget = stacked_widget  # Referencia al stackedWidget de la ventana principal

        # Iconos
        self.ui.botonIniciarTR.setIcon(QIcon("../Recursos/iconos/angulo-derecho.png"))
        self.ui.botonIniciarIH.setIcon(QIcon("../Recursos/iconos/angulo-derecho.png"))
        self.ui.botonIniciarBD.setIcon(QIcon("../Recursos/iconos/angulo-derecho.png"))
        self.ui.botonRegresar.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))
        self.ui.labelIcon3.setPixmap(QPixmap("../Recursos/iconos/logoBN.png"))
        self.ui.label_2.setPixmap(QPixmap("../Recursos/iconos/ondas-de-audio.png"))
        self.ui.label_4.setPixmap(QPixmap("../Recursos/iconos/terapia-musical.png"))


        # Eventos
        self.setup_events()

    def setup_events(self):
        self.ui.botonIniciarTR.clicked.connect(self.abrir_ventana_tiempoReverberacion)
        self.ui.botonIniciarIH.clicked.connect(self.abrir_ventana_inteligibilidad)
        self.ui.botonIniciarBD.clicked.connect(self.abrir_ventana_basedatos)
        self.ui.botonRegresar.clicked.connect(self.regresar_a_ventana_principal)

    def abrir_ventana_tiempoReverberacion(self):
        # Mostrar la transición (bloquea la ejecución hasta cerrarse)
        transicion = VentanaTransicion("../Recursos/gifs/gifmicro.gif", duracion_ms=2000, parent=self)


        self.indice_anterior = self.stacked_widget.currentIndex()
        ventana_tr = VentanaTiempoReverberacion(stacked_widget= self.stacked_widget, indice_anterior= self.indice_anterior)

        self.stacked_widget.addWidget(ventana_tr)
        transicion.exec()
        self.stacked_widget.setCurrentWidget(ventana_tr)

    def abrir_ventana_inteligibilidad(self):
        self.indice_anterior = self.stacked_widget.currentIndex()
        ventana_ih = VentanaInteligibiliad(stacked_widget=self.stacked_widget, indice_anterior=self.indice_anterior )
        self.stacked_widget.addWidget(ventana_ih)
        self.stacked_widget.setCurrentWidget(ventana_ih)

    def abrir_ventana_basedatos(self):
        self.indice_anterior = self.stacked_widget.currentIndex()
        ventana_bd = VentanaInfoBaseDatos(stacked_widget= self.stacked_widget, indice_anterior=self.indice_anterior)
        self.stacked_widget.addWidget(ventana_bd)
        self.stacked_widget.setCurrentWidget(ventana_bd)

    def regresar_a_ventana_principal(self):
        self.stacked_widget.setCurrentIndex(0)