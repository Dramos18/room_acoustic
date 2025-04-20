import sys
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QStyle

from Ventanas.ventTiempoReverberacion import VentanaTiempoReverberacion
from Ventanas.ventInteligibilidad import VentanaInteligibiliad
from Vista.iniciarAnalisis import  Ui_ventanaIniciarAnalisis # importa tu clase generada
from Ventanas.ventanaBarraTitulo import VentanaConBarra

class VentanaIniciarAnalisis(VentanaConBarra):
    """
    Esta clase representa la ventana de "Iniciar Análisis".
    Es una subclase de QWidget que carga el diseño de iniciarAnalisis.
    """

    def __init__(self, ventana_anterior=None):
        contenido = QWidget()
        self.ui = Ui_ventanaIniciarAnalisis()
        self.ui.setupUi(contenido)
        # Llamar al constructor de la clase base y pasarle el contenido
        super().__init__(contenido)
        self.ventana_anterior = ventana_anterior
        self.resize(800, 600)

        self.setup_events()

        self.ui.botonIniciarTR.setIcon(QIcon("Vista/graficas/iconos/angulo-derecho.png"))
        self.ui.botonIniciarIH.setIcon(QIcon("Vista/graficas/iconos/angulo-derecho.png"))
        self.ui.botonIniciarIH.setIcon(QIcon("Vista/graficas/iconos/angulo-derecho.png"))

        self.ui.botonRegresar.setIcon(QIcon("Vista/graficas/iconos/angulo-izquierdo.png"))
        self.ui.botonRegresar.clicked.connect(self.regresar_a_ventana_anterior)

    def setup_events(self):
        # Conectar el botón "Iniciar Análisis"
        (self.ui.botonIniciarTR.clicked.connect(self.abrir_ventana_tiempoReverberacion))
        (self.ui.botonIniciarIH.clicked.connect(self.abrir_ventana_inteligibilidad))
        (self.ui.botonIniciarBD.clicked.connect(self.abrir_ventana_basedatos))

    def abrir_ventana_tiempoReverberacion(self):
        self.ventana_tiempoReverberacion = VentanaTiempoReverberacion(ventana_anterior=self)
        self.ventana_tiempoReverberacion.show()
        self.hide()
    def abrir_ventana_inteligibilidad(self):
        self.ventana_inteligibilidad = VentanaInteligibiliad(ventana_anterior=self)
        self.ventana_inteligibilidad.show()
        self.hide()
    def abrir_ventana_basedatos(self):
        self.ventana_tiempoReverberacion = VentanaTiempoReverberacion(ventana_anterior=self)
        self.ventana_tiempoReverberacion.show()
        self.hide()

        # boton atras
    def regresar_a_ventana_anterior(self):
        """
        Oculta la ventana actual y regresa a la ventana anterior.
        """
        if hasattr(self, 'ventana_anterior') and self.ventana_anterior:
            self.hide()  # Oculta la ventana actual
            self.ventana_anterior.show()  # Muestra la ventana anterior
        else:
            print("Error: No se encontró una ventana anterior a la cual regresar.")