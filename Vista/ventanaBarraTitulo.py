from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Vista.archivos_pyGenerados.barraTitulo import Ui_formBarraTitulo

# Ancho (px) de la franja junto a cada borde de la ventana donde un clic
# inicia el redimensionado en vez del contenido normal — ver diagnóstico
# D-016 en docs/DECISIONS.md.
_MARGEN_REDIMENSION = 6

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

    def toggle_max_restore(self):
        # Antes se rastreaba el estado maximizado en self.maximizado,
        # inicializado en False en el constructor — pero main.py llama a
        # showMaximized() *después* de construir la ventana, así que el
        # flag nunca reflejaba el estado real: el primer clic en
        # "restaurar" no hacía nada visible (creía que no estaba
        # maximizada y volvía a maximizar). Se usa self.isMaximized()
        # directamente, una sola fuente de verdad (diagnóstico D-016 en
        # docs/DECISIONS.md).
        if self.isMaximized():
            self.showNormal()
            # Si quieres cambiar el ícono al de maximizar, hazlo aquí
        else:
            self.showMaximized()
            # Cambia el ícono al de restaurar si quieres

    def _borde_bajo_cursor(self, pos):
        """
        Qt.Edge (o combinación, para las esquinas) si `pos` —coordenadas
        locales de la ventana— cae dentro de `_MARGEN_REDIMENSION` de algún
        borde; None si está en el interior.
        """
        m = _MARGEN_REDIMENSION
        izquierda = pos.x() <= m
        derecha = pos.x() >= self.width() - m
        arriba = pos.y() <= m
        abajo = pos.y() >= self.height() - m
        if not (izquierda or derecha or arriba or abajo):
            return None
        edges = Qt.Edge(0)
        if izquierda:
            edges |= Qt.Edge.LeftEdge
        if derecha:
            edges |= Qt.Edge.RightEdge
        if arriba:
            edges |= Qt.Edge.TopEdge
        if abajo:
            edges |= Qt.Edge.BottomEdge
        return edges

    def mousePressEvent(self, event):
        # Mover y redimensionar vía el compositor (startSystemMove/
        # startSystemResize), no con move() manual: en Wayland un cliente
        # no puede fijar la posición de su propia ventana — ver
        # diagnóstico D-016 en docs/DECISIONS.md. Una ventana maximizada
        # no se mueve ni se redimensiona (igual que la mayoría de apps).
        if event.button() != Qt.LeftButton or self.isMaximized():
            return
        ventana = self.windowHandle()
        if ventana is None:
            return
        pos = event.position().toPoint()
        borde = self._borde_bajo_cursor(pos)
        if borde is not None:
            ventana.startSystemResize(borde)
        elif self.barra.geometry().contains(pos):
            # Geometría directa en vez de underMouse(): depende solo de la
            # posición real del clic, no del hover-tracking de Qt.
            ventana.startSystemMove()



