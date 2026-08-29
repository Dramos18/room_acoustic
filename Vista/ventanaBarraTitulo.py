from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Vista.archivos_pyGenerados.barraTitulo import Ui_formBarraTitulo

class VentanaConBarra(QWidget):
    def __init__(self, contenido):
        """
        Clase base para cualquier ventana con la barra de título ya incluida.

        :param contenido: QWidget que representa el contenido principal de la ventana.
        """
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Layout general (barra arriba, contenido abajo)
        layout_general = QVBoxLayout(self)
        layout_general.setContentsMargins(0, 0, 0, 0)
        layout_general.setSpacing(0)

        # Crear la barra de título
        self.barra = QWidget()
        self.uiBarra = Ui_formBarraTitulo()
        self.uiBarra.setupUi(self.barra)

        # Ruta del logo
        pixmap = QPixmap("../Recursos/iconos/logoBN.png")

        # Escalar el logo a un tamaño razonable (por ejemplo, 100x100)
        pixmap = pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Asignar el logo escalado al QLabel
        self.uiBarra.logoBarraTitulo.setPixmap(pixmap)

        self.uiBarra.buttonClose.setIcon(QIcon("../Recursos/iconos/cruz-pequena.png"))
        self.uiBarra.buttonClose.setIconSize(QSize(24, 24))
        self.uiBarra.buttonClose.setText("")  # Opcional

        self.uiBarra.buttonMinim.setIcon(QIcon("../Recursos/iconos/menos-pequeno.png"))
        self.uiBarra.buttonMinim.setIconSize(QSize(24, 24))
        self.uiBarra.buttonMinim.setText("")  # Opcional

        self.uiBarra.buttonMaxim.setIcon(QIcon("../Recursos/iconos/restaurar-ventana.png"))
        self.uiBarra.buttonMaxim.setIconSize(QSize(24, 24))
        self.uiBarra.buttonMaxim.setText("")  # Opcional


        # Agregar la barra y el contenido al layout
        layout_general.addWidget(self.barra)
        layout_general.addWidget(contenido)

 # Eventos para los botones
        self.uiBarra.buttonClose.clicked.connect(self.close)
        self.uiBarra.buttonMinim.clicked.connect(self.showMinimized)
        self.uiBarra.buttonMaxim.clicked.connect(self.toggle_max_restore)



        # Para controlar el estado maximizado o restaurado
        self.maximizado = False

    def toggle_max_restore(self):
        if self.maximizado:
            self.showNormal()
            self.maximizado = False
            # Si quieres cambiar el ícono al de maximizar, hazlo aquí
        else:
            self.showMaximized()
            self.maximizado = True
            # Cambia el ícono al de restaurar si quieres

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.barra.underMouse():
            self.offset = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset') and event.buttons() == Qt.LeftButton and self.barra.underMouse():
            self.move(event.globalPos() - self.offset)



