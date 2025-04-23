import sys
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QStyle

from Ventanas.ventTiempoReverberacion import VentanaTiempoReverberacion
from Ventanas.ventInteligibilidad import VentanaInteligibiliad
from Vista.iniciarAnalisis import  Ui_ventanaIniciarAnalisis # importa tu clase generada
from Ventanas.ventanaBarraTitulo import VentanaConBarra

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
        self.ui.botonIniciarTR.setIcon(QIcon("Vista/graficas/iconos/angulo-derecho.png"))
        self.ui.botonIniciarIH.setIcon(QIcon("Vista/graficas/iconos/angulo-derecho.png"))
        self.ui.botonIniciarBD.setIcon(QIcon("Vista/graficas/iconos/angulo-derecho.png"))
        self.ui.botonRegresar.setIcon(QIcon("Vista/graficas/iconos/angulo-izquierdo.png"))

        # Eventos
        self.setup_events()

    def setup_events(self):
        self.ui.botonIniciarTR.clicked.connect(self.abrir_ventana_tiempoReverberacion)
        self.ui.botonIniciarIH.clicked.connect(self.abrir_ventana_inteligibilidad)
        #self.ui.botonIniciarBD.clicked.connect(self.abrir_ventana_basedatos)
        self.ui.botonRegresar.clicked.connect(self.regresar_a_ventana_principal)

    def abrir_ventana_tiempoReverberacion(self):
        self.indice_anterior = self.stacked_widget.currentIndex()
        ventana_tr = VentanaTiempoReverberacion(stacked_widget= self.stacked_widget, indice_anterior= self.indice_anterior)
        self.stacked_widget.addWidget(ventana_tr)
        self.stacked_widget.setCurrentWidget(ventana_tr)

    def abrir_ventana_inteligibilidad(self):
        ventana_ih = VentanaInteligibiliad(self.stacked_widget)
        self.stacked_widget.addWidget(ventana_ih)
        self.stacked_widget.setCurrentWidget(ventana_ih)

    #def abrir_ventana_basedatos(self):
    #    from Ventanas.ventanaBaseDatos import VentanaBaseDatos  # si la tienes
    #    ventana_bd = VentanaBaseDatos(self.stacked_widget)
    #    self.stacked_widget.addWidget(ventana_bd)
    #    self.stacked_widget.setCurrentWidget(ventana_bd)

    def regresar_a_ventana_principal(self):
        self.stacked_widget.setCurrentIndex(0)