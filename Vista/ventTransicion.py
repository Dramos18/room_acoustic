from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PySide6.QtGui import QMovie, QColor, QPainter
from PySide6.QtCore import Qt, QTimer, QSize

class VentanaTransicion(QDialog):
    def __init__(self, gif_path, duracion_ms=3000, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setModal(True)

        if parent:
            # Obtener la geometría global (posición + tamaño en pantalla)
            global_pos = parent.mapToGlobal(parent.rect().topLeft())
            self.setGeometry(global_pos.x(), global_pos.y(), parent.width(), parent.height())
        else:
            self.resize(400, 300)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setStyleSheet("background-color: transparent; border: none;")

        layout.addWidget(self.label)

        self.movie = QMovie(gif_path)
        self.movie.setScaledSize(QSize(120, 120))  # Tamaño del gif
        self.label.setMovie(self.movie)
        self.movie.start()

        QTimer.singleShot(duracion_ms, self.accept)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 180))  # Fondo oscuro translúcido


