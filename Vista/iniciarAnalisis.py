# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iniciarAnalisis.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ventanaIniciarAnalisis(object):
    def setupUi(self, ventanaIniciarAnalisis):
        if not ventanaIniciarAnalisis.objectName():
            ventanaIniciarAnalisis.setObjectName(u"ventanaIniciarAnalisis")
        ventanaIniciarAnalisis.resize(763, 441)
        ventanaIniciarAnalisis.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.495, y2:1, stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255))\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(ventanaIniciarAnalisis)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameVentana = QFrame(ventanaIniciarAnalisis)
        self.frameVentana.setObjectName(u"frameVentana")
        self.frameVentana.setStyleSheet(u"QFrame{\n"
"	background-color: transparent\n"
"}")
        self.frameVentana.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frameVentana)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frameVentana)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frameCards = QFrame(self.frameVentana)
        self.frameCards.setObjectName(u"frameCards")
        self.frameCards.setAutoFillBackground(False)
        self.frameCards.setStyleSheet(u"")
        self.frameCards.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameCards)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)
        self.frContainer1 = QFrame(self.frameCards)
        self.frContainer1.setObjectName(u"frContainer1")
        self.frContainer1.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"    padding: 15px;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    transform: scale(1.05);\n"
"}\n"
"\n"
"QLabel {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    font-size: 24px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: gray;\n"
"}")
        self.frContainer1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frContainer1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frContainer1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame {\n"
"    background: none;\n"
"    border: none;\n"
"	padding: 0px\n"
"}")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_11)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.vboxLayout = QVBoxLayout(self.frame_23)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_23)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 5em; /* Escala con el sistema */\n"
"}")
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)

        self.vboxLayout.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_12)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setAutoFillBackground(False)
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.frame_24)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_24)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u"graficas/iconos/ondas-de-audio.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_24)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {\n"
"    border-top: 0.6px solid  rgba(255, 255, 255, 0.8);  /* Cambia el color y grosor seg\u00fan tu preferencia */\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-bottom: none;\n"
"	border-radius: 0;\n"
"}")
        self.frame_13.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.frame_13)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_8)

        self.frameBoton = QFrame(self.frame_11)
        self.frameBoton.setObjectName(u"frameBoton")
        self.frameBoton.setLayoutDirection(Qt.LeftToRight)
        self.frameBoton.setAutoFillBackground(False)
        self.frameBoton.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frameBoton)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.botonIniciarTR = QPushButton(self.frameBoton)
        self.botonIniciarTR.setObjectName(u"botonIniciarTR")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.botonIniciarTR.sizePolicy().hasHeightForWidth())
        self.botonIniciarTR.setSizePolicy(sizePolicy2)
        self.botonIniciarTR.setMaximumSize(QSize(50, 50))
        self.botonIniciarTR.setLayoutDirection(Qt.LeftToRight)
        self.botonIniciarTR.setAutoFillBackground(False)
        self.botonIniciarTR.setStyleSheet(u"QPushButton {\n"
"    background-color: #000000ff;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(255, 255, 255, 0.4);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"	border-radius: 20px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"graficas/iconos/angulo-derecho.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonIniciarTR.setIcon(icon)
        self.botonIniciarTR.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.botonIniciarTR)

        self.horizontalSpacer = QSpacerItem(126, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.frameBoton)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 3)
        self.verticalLayout_3.setStretch(3, 2)

        self.horizontalLayout_3.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.frContainer1)

        self.frContainer2 = QFrame(self.frameCards)
        self.frContainer2.setObjectName(u"frContainer2")
        self.frContainer2.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"    padding: 15px;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    transform: scale(1.05);\n"
"}\n"
"\n"
"QLabel {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    font-size: 24px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: gray;\n"
"}")
        self.frContainer2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frContainer2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frContainer2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame {\n"
"    background: none;\n"
"    border: none;\n"
"	padding: 0px\n"
"}")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_15)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_16)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self._2 = QVBoxLayout(self.frame_25)
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_25)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setSizeIncrement(QSize(0, 0))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 5em; /* Escala con el sistema */\n"
"}")
        self.label_3.setWordWrap(True)

        self._2.addWidget(self.label_3)


        self.horizontalLayout_7.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_16)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.frame_26)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_26)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u"graficas/iconos/terapia-musical.png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_7.addWidget(self.frame_26)

        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QFrame {\n"
"    border-top: 0.6px solid  rgba(255, 255, 255, 0.8);  /* Cambia el color y grosor seg\u00fan tu preferencia */\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-bottom: none;\n"
"	border-radius: 0;\n"
"}")
        self.frame_17.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.frame_17)

        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.frameBoton_2 = QFrame(self.frame_15)
        self.frameBoton_2.setObjectName(u"frameBoton_2")
        self.frameBoton_2.setLayoutDirection(Qt.LeftToRight)
        self.frameBoton_2.setAutoFillBackground(False)
        self.frameBoton_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frameBoton_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.botonIniciarIH = QPushButton(self.frameBoton_2)
        self.botonIniciarIH.setObjectName(u"botonIniciarIH")
        self.botonIniciarIH.setMaximumSize(QSize(50, 50))
        self.botonIniciarIH.setLayoutDirection(Qt.LeftToRight)
        self.botonIniciarIH.setAutoFillBackground(False)
        self.botonIniciarIH.setStyleSheet(u"QPushButton {\n"
"    background-color: #000000ff;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(255, 255, 255, 0.4);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"	border-radius: 20px;\n"
"}")
        self.botonIniciarIH.setIcon(icon)
        self.botonIniciarIH.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.botonIniciarIH)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_4.addWidget(self.frameBoton_2)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 5)
        self.verticalLayout_4.setStretch(3, 3)

        self.horizontalLayout_6.addWidget(self.frame_15)


        self.horizontalLayout.addWidget(self.frContainer2)

        self.frContainer3 = QFrame(self.frameCards)
        self.frContainer3.setObjectName(u"frContainer3")
        self.frContainer3.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"    padding: 15px;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    transform: scale(1.05);\n"
"}\n"
"\n"
"QLabel {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    font-size: 24px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: gray;\n"
"}")
        self.frContainer3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frContainer3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.subFrame3 = QFrame(self.frContainer3)
        self.subFrame3.setObjectName(u"subFrame3")
        self.subFrame3.setStyleSheet(u"QFrame {\n"
"    background: none;\n"
"    border: none;\n"
"	padding: 0px\n"
"}")
        self.subFrame3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.subFrame3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.containerTittle3 = QFrame(self.subFrame3)
        self.containerTittle3.setObjectName(u"containerTittle3")
        self.containerTittle3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.containerTittle3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frameTittle3 = QFrame(self.containerTittle3)
        self.frameTittle3.setObjectName(u"frameTittle3")
        self.frameTittle3.setFrameShape(QFrame.NoFrame)
        self._3 = QVBoxLayout(self.frameTittle3)
        self._3.setSpacing(0)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(0, 0, 0, 0)
        self.labelTitle3 = QLabel(self.frameTittle3)
        self.labelTitle3.setObjectName(u"labelTitle3")
        sizePolicy.setHeightForWidth(self.labelTitle3.sizePolicy().hasHeightForWidth())
        self.labelTitle3.setSizePolicy(sizePolicy)
        self.labelTitle3.setSizeIncrement(QSize(0, 0))
        self.labelTitle3.setStyleSheet(u"QLabel {\n"
"    font-size: 5em; /* Escala con el sistema */\n"
"}")
        self.labelTitle3.setWordWrap(True)

        self._3.addWidget(self.labelTitle3)


        self.horizontalLayout_10.addWidget(self.frameTittle3)

        self.frameIcon3 = QFrame(self.containerTittle3)
        self.frameIcon3.setObjectName(u"frameIcon3")
        self.frameIcon3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.frameIcon3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.labelIcon3 = QLabel(self.frameIcon3)
        self.labelIcon3.setObjectName(u"labelIcon3")
        self.labelIcon3.setMinimumSize(QSize(40, 40))
        self.labelIcon3.setMaximumSize(QSize(40, 40))
        self.labelIcon3.setPixmap(QPixmap(u"graficas/iconos/logoBN.png"))
        self.labelIcon3.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.labelIcon3)


        self.horizontalLayout_10.addWidget(self.frameIcon3)

        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 1)

        self.verticalLayout_5.addWidget(self.containerTittle3)

        self.linea3 = QFrame(self.subFrame3)
        self.linea3.setObjectName(u"linea3")
        self.linea3.setStyleSheet(u"QFrame {\n"
"    border-top: 0.6px solid  rgba(255, 255, 255, 0.8);  /* Cambia el color y grosor seg\u00fan tu preferencia */\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-bottom: none;\n"
"	border-radius: 0;\n"
"}")
        self.linea3.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_5.addWidget(self.linea3)

        self.lbDescripcion3 = QLabel(self.subFrame3)
        self.lbDescripcion3.setObjectName(u"lbDescripcion3")
        self.lbDescripcion3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.lbDescripcion3)

        self.frameBoton_3 = QFrame(self.subFrame3)
        self.frameBoton_3.setObjectName(u"frameBoton_3")
        self.frameBoton_3.setLayoutDirection(Qt.LeftToRight)
        self.frameBoton_3.setAutoFillBackground(False)
        self.frameBoton_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.frameBoton_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.botonIniciarBD = QPushButton(self.frameBoton_3)
        self.botonIniciarBD.setObjectName(u"botonIniciarBD")
        self.botonIniciarBD.setMaximumSize(QSize(50, 50))
        self.botonIniciarBD.setLayoutDirection(Qt.LeftToRight)
        self.botonIniciarBD.setAutoFillBackground(False)
        self.botonIniciarBD.setStyleSheet(u"QPushButton {\n"
"    background-color: #000000ff;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(255, 255, 255, 0.4);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"	border-radius: 20px;\n"
"}")
        self.botonIniciarBD.setIcon(icon)
        self.botonIniciarBD.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.botonIniciarBD)

        self.horizontalSpacer3 = QSpacerItem(78, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_11.addItem(self.horizontalSpacer3)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)

        self.verticalLayout_5.addWidget(self.frameBoton_3)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 3)
        self.verticalLayout_5.setStretch(3, 2)

        self.horizontalLayout_9.addWidget(self.subFrame3)


        self.horizontalLayout.addWidget(self.frContainer3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frameCards)

        self.frame_4 = QFrame(self.frameVentana)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frameBotonRegresar = QFrame(self.frame_4)
        self.frameBotonRegresar.setObjectName(u"frameBotonRegresar")
        self.frameBotonRegresar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frameBotonRegresar)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(50, 0, 50, 0)
        self.botonRegresar = QPushButton(self.frameBotonRegresar)
        self.botonRegresar.setObjectName(u"botonRegresar")
        self.botonRegresar.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"	font-size: 18px;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);\n"
"}")

        self.horizontalLayout_12.addWidget(self.botonRegresar)


        self.horizontalLayout_2.addWidget(self.frameBotonRegresar)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frameBotonBD = QFrame(self.frame_4)
        self.frameBotonBD.setObjectName(u"frameBotonBD")
        self.frameBotonBD.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.frameBotonBD)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.botonBaseDatosGeneral = QPushButton(self.frameBotonBD)
        self.botonBaseDatosGeneral.setObjectName(u"botonBaseDatosGeneral")
        self.botonBaseDatosGeneral.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"	font-size: 18px;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"graficas/iconos/logoBN.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonBaseDatosGeneral.setIcon(icon1)
        self.botonBaseDatosGeneral.setIconSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.botonBaseDatosGeneral)


        self.horizontalLayout_2.addWidget(self.frameBotonBD)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frameVentana)


        self.retranslateUi(ventanaIniciarAnalisis)

        QMetaObject.connectSlotsByName(ventanaIniciarAnalisis)
    # setupUi

    def retranslateUi(self, ventanaIniciarAnalisis):
        ventanaIniciarAnalisis.setWindowTitle(QCoreApplication.translate("ventanaIniciarAnalisis", u"Form", None))
        self.label.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Tiempo de Reverberaci\u00f3n</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.frame_24.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_2.setText("")
        self.label_8.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Calcula el tiempo que tarda el sonido en disminuir 60 dB en el aula:</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">Ingresa dimensiones y materiales para conocer el tiempo que tarda el sonido en desaparecer.</span></p><p><span style=\" font-size:10pt; font-weight:700; font-style:italic; color:#ffffff;\">Opcional</span><span style=\" font-size:10pt; font-style:italic; color:#ffffff;\">: A\u00f1ade el c\u00e1lculo de </span><span style=\" font-size:10pt; font-weight:700; font-style:italic; color:#ffffff;\">inteligibilidad del habla</span><span style=\" font-size:10pt; font-style:italic; color:#ffffff;\"> desde esta misma secci\u00f3n.</span></p></body></html>", None))
        self.botonIniciarTR.setText("")
        self.label_3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Inteligibilidad del Habla</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_7.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Analiza qu\u00e9 tan comprensible es la voz humana dentro del sal\u00f3n.<br/>Conoce lap\u00e9rdida porcentual de articulaci\u00f3n de las consonantes </span><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">(%ALCONS)</span><span style=\" font-size:14pt; color:#ffffff;\">, \u00fatil para evaluar condiciones \u00f3ptimas de aprendizaje o comunicaci\u00f3n.</span></p><p><span style=\" font-style:italic; color:#ffffff;\">Este valor est\u00e1 influenciado por el tiempo de reverberaci\u00f3n y otros par\u00e1metros ac\u00fasticos.</span></p></body></html>", None))
        self.botonIniciarIH.setText("")
        self.labelTitle3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Base de Datos: Bloque H</span></p></body></html>", None))
        self.labelIcon3.setText("")
        self.lbDescripcion3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Explora 23 aulas reales del bloque H.</span><span style=\" font-size:14pt; color:#ffffff;\"><br/>Visualiza sus caracter\u00edsticas ac\u00fasticas predeterminadas y realiza an\u00e1lisis sin necesidad de ingresar datos manualmente.</span></p></body></html>", None))
        self.botonIniciarBD.setText("")
        self.botonRegresar.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"Regresar", None))
        self.botonBaseDatosGeneral.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"Base de Datos Bloque H", None))
    # retranslateUi

