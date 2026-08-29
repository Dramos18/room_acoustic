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
        ventanaIniciarAnalisis.resize(880, 580)
        ventanaIniciarAnalisis.setStyleSheet(u"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0.488, y1:0, x2:0.495, y2:1,\n"
"        stop:0.306818 rgba(0,0,93,255),\n"
"        stop:0.710227 rgba(0,0,45,255)\n"
"    );\n"
"}\n"
"QFrame { background-color: transparent; border: none; }\n"
"")
        self.verticalLayout = QVBoxLayout(ventanaIniciarAnalisis)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameVentana = QFrame(ventanaIniciarAnalisis)
        self.frameVentana.setObjectName(u"frameVentana")
        self.frameVentana.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frameVentana)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frameVentana)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 64))
        self.frame_2.setMaximumSize(QSize(16777215, 64))
        self.frame_2.setStyleSheet(u"QFrame#frame_2 {\n"
"    background-color: rgba(0,0,0,0.22);\n"
"    border-bottom: 1px solid rgba(255,255,255,0.12);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_14.setSpacing(14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(14, 0, 20, 0)
        self.botonRegresar = QPushButton(self.frame_2)
        self.botonRegresar.setObjectName(u"botonRegresar")
        self.botonRegresar.setMinimumSize(QSize(42, 42))
        self.botonRegresar.setMaximumSize(QSize(42, 42))
        self.botonRegresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonRegresar.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(255,255,255,0.35);\n"
"    border-radius: 21px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255,255,255,0.18);\n"
"    border: 1px solid white;\n"
"}\n"
"QPushButton:pressed { background-color: rgba(255,255,255,0.38); }")
        icon = QIcon()
        icon.addFile(u"graficas/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonRegresar.setIcon(icon)
        self.botonRegresar.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.botonRegresar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.frameTituloTop = QFrame(self.frame_2)
        self.frameTituloTop.setObjectName(u"frameTituloTop")
        self.frameTituloTop.setFrameShape(QFrame.NoFrame)
        self.vloTituloTop = QVBoxLayout(self.frameTituloTop)
        self.vloTituloTop.setSpacing(2)
        self.vloTituloTop.setObjectName(u"vloTituloTop")
        self.vloTituloTop.setContentsMargins(0, 8, 0, 8)
        self.labelTituloTop = QLabel(self.frameTituloTop)
        self.labelTituloTop.setObjectName(u"labelTituloTop")
        self.labelTituloTop.setAlignment(Qt.AlignCenter)

        self.vloTituloTop.addWidget(self.labelTituloTop)

        self.labelSubtituloTop = QLabel(self.frameTituloTop)
        self.labelSubtituloTop.setObjectName(u"labelSubtituloTop")
        self.labelSubtituloTop.setAlignment(Qt.AlignCenter)

        self.vloTituloTop.addWidget(self.labelSubtituloTop)


        self.horizontalLayout_14.addWidget(self.frameTituloTop)

        self.horizontalSpacerTopR = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacerTopR)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frameCards = QFrame(self.frameVentana)
        self.frameCards.setObjectName(u"frameCards")
        self.frameCards.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameCards)
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(28, 100, 28, 100)
        self.frContainer1 = QFrame(self.frameCards)
        self.frContainer1.setObjectName(u"frContainer1")
        self.frContainer1.setStyleSheet(u"/* Card externa */\n"
"QFrame#frContainer1 {\n"
"    background-color: rgba(255,255,255,0.09);\n"
"    border: 1.5px solid rgba(126,200,247,0.55);\n"
"    border-radius: 16px;\n"
"}\n"
"QFrame#frContainer1:hover {\n"
"    background-color: rgba(126,200,247,0.13);\n"
"    border: 1.5px solid rgba(126,200,247,0.90);\n"
"}\n"
"/* Subelementos internos */\n"
"QFrame#frContainer1 QFrame { background: transparent; border: none; }\n"
"QFrame#frContainer1 QLabel { background: transparent; border: none; }\n"
"/* L\u00ednea separadora */\n"
"QFrame#linea1 {\n"
"    background-color: rgba(126,200,247,0.35);\n"
"    max-height: 1px;\n"
"    border: none;\n"
"}\n"
"/* Badge de n\u00famero */\n"
"QLabel#labelBadge1 {\n"
"    background-color: rgba(126,200,247,0.20);\n"
"    border: 1px solid rgba(126,200,247,0.55);\n"
"    border-radius: 12px;\n"
"    color: #7ec8f7;\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"    padding: 1px 8px;\n"
"}\n"
"/* Bot\u00f3n de acci\u00f3n */\n"
"QPushButton#botonIniciarTR {\n"
"   "
                        " background-color: rgba(126,200,247,0.18);\n"
"    border: 1.5px solid rgba(126,200,247,0.70);\n"
"    border-radius: 10px;\n"
"    color: #7ec8f7;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    padding: 8px 16px;\n"
"    min-width: 140px;\n"
"    max-width: 200px;\n"
"    max-height: 38px;\n"
"}\n"
"QPushButton#botonIniciarTR:hover {\n"
"    background-color: rgba(126,200,247,0.35);\n"
"    color: white;\n"
"    border-color: white;\n"
"}\n"
"QPushButton#botonIniciarTR:pressed {\n"
"    background-color: rgba(126,200,247,0.55);\n"
"    color: white;\n"
"}\n"
"")
        self.frContainer1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frContainer1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frContainer1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_11)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.vloHeader1 = QVBoxLayout(self.frame_12)
        self.vloHeader1.setSpacing(6)
        self.vloHeader1.setObjectName(u"vloHeader1")
        self.vloHeader1.setContentsMargins(0, 0, 0, 0)
        self.frameBadgeIcon1 = QFrame(self.frame_12)
        self.frameBadgeIcon1.setObjectName(u"frameBadgeIcon1")
        self.frameBadgeIcon1.setFrameShape(QFrame.NoFrame)
        self.hloBadgeIcon1 = QHBoxLayout(self.frameBadgeIcon1)
        self.hloBadgeIcon1.setSpacing(8)
        self.hloBadgeIcon1.setObjectName(u"hloBadgeIcon1")
        self.hloBadgeIcon1.setContentsMargins(0, 0, 0, 0)
        self.labelBadge1 = QLabel(self.frameBadgeIcon1)
        self.labelBadge1.setObjectName(u"labelBadge1")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.labelBadge1.setFont(font)

        self.hloBadgeIcon1.addWidget(self.labelBadge1)

        self.spacerBadge1 = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hloBadgeIcon1.addItem(self.spacerBadge1)

        self.label_2 = QLabel(self.frameBadgeIcon1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(48, 48))
        self.label_2.setPixmap(QPixmap(u"graficas/iconos/ondas-de-audio.png"))
        self.label_2.setScaledContents(True)

        self.hloBadgeIcon1.addWidget(self.label_2)


        self.vloHeader1.addWidget(self.frameBadgeIcon1)

        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.vloHeader1.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.linea1 = QFrame(self.frame_11)
        self.linea1.setObjectName(u"linea1")
        self.linea1.setStyleSheet(u"QFrame { background-color: rgba(126,200,247,0.30); max-height:1px; border:none; }")
        self.linea1.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.linea1)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_8)

        self.frameBoton = QFrame(self.frame_11)
        self.frameBoton.setObjectName(u"frameBoton")
        self.frameBoton.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frameBoton)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.botonIniciarTR = QPushButton(self.frameBoton)
        self.botonIniciarTR.setObjectName(u"botonIniciarTR")
        self.botonIniciarTR.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonIniciarTR.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u"graficas/iconos/angulo-derecho.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonIniciarTR.setIcon(icon1)
        self.botonIniciarTR.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.botonIniciarTR)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frameBoton)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 4)
        self.verticalLayout_3.setStretch(3, 2)

        self.horizontalLayout_3.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.frContainer1)

        self.frContainer2 = QFrame(self.frameCards)
        self.frContainer2.setObjectName(u"frContainer2")
        self.frContainer2.setStyleSheet(u"QFrame#frContainer2 {\n"
"    background-color: rgba(255,255,255,0.09);\n"
"    border: 1.5px solid rgba(52,211,153,0.55);\n"
"    border-radius: 16px;\n"
"}\n"
"QFrame#frContainer2:hover {\n"
"    background-color: rgba(52,211,153,0.11);\n"
"    border: 1.5px solid rgba(52,211,153,0.90);\n"
"}\n"
"QFrame#frContainer2 QFrame { background: transparent; border: none; }\n"
"QFrame#frContainer2 QLabel { background: transparent; border: none; }\n"
"QFrame#linea2 {\n"
"    background-color: rgba(52,211,153,0.30);\n"
"    max-height: 1px; border: none;\n"
"}\n"
"QLabel#labelBadge2 {\n"
"    background-color: rgba(52,211,153,0.18);\n"
"    border: 1px solid rgba(52,211,153,0.55);\n"
"    border-radius: 12px;\n"
"    color: #34d399;\n"
"    font-size: 9pt; font-weight: bold;\n"
"    padding: 1px 8px;\n"
"}\n"
"QPushButton#botonIniciarIH {\n"
"    background-color: rgba(52,211,153,0.16);\n"
"    border: 1.5px solid rgba(52,211,153,0.65);\n"
"    border-radius: 10px;\n"
"    color: #34d399;\n"
"    font-size: 11pt; font-"
                        "weight: bold;\n"
"    padding: 8px 16px;\n"
"    min-width: 140px; max-width: 200px; max-height: 38px;\n"
"}\n"
"QPushButton#botonIniciarIH:hover {\n"
"    background-color: rgba(52,211,153,0.32);\n"
"    color: white; border-color: white;\n"
"}\n"
"QPushButton#botonIniciarIH:pressed {\n"
"    background-color: rgba(52,211,153,0.52); color: white;\n"
"}\n"
"")
        self.frContainer2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frContainer2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frContainer2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_15)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.vloHeader2 = QVBoxLayout(self.frame_16)
        self.vloHeader2.setSpacing(6)
        self.vloHeader2.setObjectName(u"vloHeader2")
        self.vloHeader2.setContentsMargins(0, 0, 0, 0)
        self.frameBadgeIcon2 = QFrame(self.frame_16)
        self.frameBadgeIcon2.setObjectName(u"frameBadgeIcon2")
        self.frameBadgeIcon2.setFrameShape(QFrame.NoFrame)
        self.hloBadgeIcon2 = QHBoxLayout(self.frameBadgeIcon2)
        self.hloBadgeIcon2.setSpacing(8)
        self.hloBadgeIcon2.setObjectName(u"hloBadgeIcon2")
        self.hloBadgeIcon2.setContentsMargins(0, 0, 0, 0)
        self.labelBadge2 = QLabel(self.frameBadgeIcon2)
        self.labelBadge2.setObjectName(u"labelBadge2")

        self.hloBadgeIcon2.addWidget(self.labelBadge2)

        self.spacerBadge2 = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hloBadgeIcon2.addItem(self.spacerBadge2)

        self.label_4 = QLabel(self.frameBadgeIcon2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(48, 48))
        self.label_4.setMaximumSize(QSize(48, 48))
        self.label_4.setPixmap(QPixmap(u"graficas/iconos/terapia-musical.png"))
        self.label_4.setScaledContents(True)

        self.hloBadgeIcon2.addWidget(self.label_4)


        self.vloHeader2.addWidget(self.frameBadgeIcon2)

        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.vloHeader2.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.linea2 = QFrame(self.frame_15)
        self.linea2.setObjectName(u"linea2")
        self.linea2.setStyleSheet(u"QFrame { background-color: rgba(52,211,153,0.28); max-height:1px; border:none; }")
        self.linea2.setFrameShape(QFrame.HLine)

        self.verticalLayout_4.addWidget(self.linea2)

        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.frameBoton_2 = QFrame(self.frame_15)
        self.frameBoton_2.setObjectName(u"frameBoton_2")
        self.frameBoton_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frameBoton_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.botonIniciarIH = QPushButton(self.frameBoton_2)
        self.botonIniciarIH.setObjectName(u"botonIniciarIH")
        self.botonIniciarIH.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonIniciarIH.setLayoutDirection(Qt.RightToLeft)
        self.botonIniciarIH.setIcon(icon1)
        self.botonIniciarIH.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.botonIniciarIH)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frameBoton_2)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 4)
        self.verticalLayout_4.setStretch(3, 2)

        self.horizontalLayout_6.addWidget(self.frame_15)


        self.horizontalLayout.addWidget(self.frContainer2)

        self.frContainer3 = QFrame(self.frameCards)
        self.frContainer3.setObjectName(u"frContainer3")
        self.frContainer3.setStyleSheet(u"QFrame#frContainer3 {\n"
"    background-color: rgba(255,255,255,0.09);\n"
"    border: 1.5px solid rgba(251,146,60,0.55);\n"
"    border-radius: 16px;\n"
"}\n"
"QFrame#frContainer3:hover {\n"
"    background-color: rgba(251,146,60,0.11);\n"
"    border: 1.5px solid rgba(251,146,60,0.90);\n"
"}\n"
"QFrame#frContainer3 QFrame { background: transparent; border: none; }\n"
"QFrame#frContainer3 QLabel { background: transparent; border: none; }\n"
"QFrame#linea3 {\n"
"    background-color: rgba(251,146,60,0.28);\n"
"    max-height: 1px; border: none;\n"
"}\n"
"QLabel#labelBadge3 {\n"
"    background-color: rgba(251,146,60,0.18);\n"
"    border: 1px solid rgba(251,146,60,0.55);\n"
"    border-radius: 12px;\n"
"    color: #fb923c;\n"
"    font-size: 9pt; font-weight: bold;\n"
"    padding: 1px 8px;\n"
"}\n"
"QPushButton#botonIniciarBD {\n"
"    background-color: rgba(251,146,60,0.16);\n"
"    border: 1.5px solid rgba(251,146,60,0.65);\n"
"    border-radius: 10px;\n"
"    color: #fb923c;\n"
"    font-size: 11pt; font-"
                        "weight: bold;\n"
"    padding: 8px 16px;\n"
"    min-width: 140px; max-width: 200px; max-height: 38px;\n"
"}\n"
"QPushButton#botonIniciarBD:hover {\n"
"    background-color: rgba(251,146,60,0.32);\n"
"    color: white; border-color: white;\n"
"}\n"
"QPushButton#botonIniciarBD:pressed {\n"
"    background-color: rgba(251,146,60,0.52); color: white;\n"
"}\n"
"")
        self.frContainer3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frContainer3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.subFrame3 = QFrame(self.frContainer3)
        self.subFrame3.setObjectName(u"subFrame3")
        self.subFrame3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.subFrame3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.containerTittle3 = QFrame(self.subFrame3)
        self.containerTittle3.setObjectName(u"containerTittle3")
        self.containerTittle3.setFrameShape(QFrame.NoFrame)
        self.vloHeader3 = QVBoxLayout(self.containerTittle3)
        self.vloHeader3.setSpacing(6)
        self.vloHeader3.setObjectName(u"vloHeader3")
        self.vloHeader3.setContentsMargins(0, 0, 0, 0)
        self.frameBadgeIcon3 = QFrame(self.containerTittle3)
        self.frameBadgeIcon3.setObjectName(u"frameBadgeIcon3")
        self.frameBadgeIcon3.setFrameShape(QFrame.NoFrame)
        self.hloBadgeIcon3 = QHBoxLayout(self.frameBadgeIcon3)
        self.hloBadgeIcon3.setSpacing(8)
        self.hloBadgeIcon3.setObjectName(u"hloBadgeIcon3")
        self.hloBadgeIcon3.setContentsMargins(0, 0, 0, 0)
        self.labelBadge3 = QLabel(self.frameBadgeIcon3)
        self.labelBadge3.setObjectName(u"labelBadge3")

        self.hloBadgeIcon3.addWidget(self.labelBadge3)

        self.spacerBadge3 = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hloBadgeIcon3.addItem(self.spacerBadge3)

        self.labelIcon3 = QLabel(self.frameBadgeIcon3)
        self.labelIcon3.setObjectName(u"labelIcon3")
        self.labelIcon3.setMinimumSize(QSize(48, 48))
        self.labelIcon3.setMaximumSize(QSize(48, 48))
        self.labelIcon3.setPixmap(QPixmap(u"graficas/iconos/logoBN.png"))
        self.labelIcon3.setScaledContents(True)

        self.hloBadgeIcon3.addWidget(self.labelIcon3)


        self.vloHeader3.addWidget(self.frameBadgeIcon3)

        self.labelTitle3 = QLabel(self.containerTittle3)
        self.labelTitle3.setObjectName(u"labelTitle3")
        self.labelTitle3.setWordWrap(True)

        self.vloHeader3.addWidget(self.labelTitle3)


        self.verticalLayout_5.addWidget(self.containerTittle3)

        self.linea3 = QFrame(self.subFrame3)
        self.linea3.setObjectName(u"linea3")
        self.linea3.setStyleSheet(u"QFrame { background-color: rgba(251,146,60,0.28); max-height:1px; border:none; }")
        self.linea3.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.linea3)

        self.lbDescripcion3 = QLabel(self.subFrame3)
        self.lbDescripcion3.setObjectName(u"lbDescripcion3")
        self.lbDescripcion3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbDescripcion3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.lbDescripcion3)

        self.frameBoton_3 = QFrame(self.subFrame3)
        self.frameBoton_3.setObjectName(u"frameBoton_3")
        self.frameBoton_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.frameBoton_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.botonIniciarBD = QPushButton(self.frameBoton_3)
        self.botonIniciarBD.setObjectName(u"botonIniciarBD")
        self.botonIniciarBD.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonIniciarBD.setLayoutDirection(Qt.RightToLeft)
        self.botonIniciarBD.setIcon(icon1)
        self.botonIniciarBD.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.botonIniciarBD)

        self.horizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer3)


        self.verticalLayout_5.addWidget(self.frameBoton_3)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 4)
        self.verticalLayout_5.setStretch(3, 2)

        self.horizontalLayout_9.addWidget(self.subFrame3)


        self.horizontalLayout.addWidget(self.frContainer3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frameCards)

        self.frame_4 = QFrame(self.frameVentana)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 36))
        self.frame_4.setMaximumSize(QSize(16777215, 36))
        self.frame_4.setStyleSheet(u"QFrame#frame_4 {\n"
"    background-color: rgba(0,0,0,0.18);\n"
"    border-top: 1px solid rgba(255,255,255,0.09);\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.frameBotonRegresar = QFrame(self.frame_4)
        self.frameBotonRegresar.setObjectName(u"frameBotonRegresar")
        self.frameBotonRegresar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frameBotonRegresar)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frameBotonRegresar)

        self.labelFooterInfo = QLabel(self.frame_4)
        self.labelFooterInfo.setObjectName(u"labelFooterInfo")
        self.labelFooterInfo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelFooterInfo)

        self.frameBotonBD = QFrame(self.frame_4)
        self.frameBotonBD.setObjectName(u"frameBotonBD")
        self.frameBotonBD.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.frameBotonBD)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.horizontalLayout_2.addWidget(self.frameBotonBD)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frameVentana)


        self.retranslateUi(ventanaIniciarAnalisis)

        QMetaObject.connectSlotsByName(ventanaIniciarAnalisis)
    # setupUi

    def retranslateUi(self, ventanaIniciarAnalisis):
        ventanaIniciarAnalisis.setWindowTitle(QCoreApplication.translate("ventanaIniciarAnalisis", u"Form", None))
#if QT_CONFIG(tooltip)
        self.botonRegresar.setToolTip(QCoreApplication.translate("ventanaIniciarAnalisis", u"Regresar a la pantalla de inicio", None))
#endif // QT_CONFIG(tooltip)
        self.botonRegresar.setText("")
        self.labelTituloTop.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:16pt; font-weight:700; color:#ffffff;\">Selecciona un modulo de analisis</span></p></body></html>", None))
        self.labelSubtituloTop.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:9pt; color:rgba(255,255,255,0.55);\">Tiempo de Reverberacion \u00b7 Inteligibilidad del Habla \u00b7 Base de Datos Bloque H</span></p></body></html>", None))
        self.labelBadge1.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"01", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:16pt; font-weight:700; color:#ffffff;\">Tiempo de Reverberacion</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:10pt; color:rgba(255,255,255,0.80);\">Calcula el <b>RT60</b>: el tiempo que tarda el sonido en disminuir 60 dB dentro del aula.</span></p><p><span style=\"font-size:9pt; color:rgba(255,255,255,0.55);\">Ingresa dimensiones y materiales. Opcionalmente incluye el analisis de inteligibilidad del habla.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.botonIniciarTR.setToolTip(QCoreApplication.translate("ventanaIniciarAnalisis", u"Abrir el modulo de Tiempo de Reverberacion", None))
#endif // QT_CONFIG(tooltip)
        self.botonIniciarTR.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"Iniciar analisis", None))
        self.labelBadge2.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"02", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:16pt; font-weight:700; color:#ffffff;\">Inteligibilidad del Habla</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:10pt; color:rgba(255,255,255,0.80);\">Analiza que tan comprensible es la voz dentro del salon mediante el indice <b>%ALCONS</b>.</span></p><p><span style=\"font-size:9pt; color:rgba(255,255,255,0.55);\">Influenciado por el tiempo de reverberacion y parametros acousticos del recinto.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.botonIniciarIH.setToolTip(QCoreApplication.translate("ventanaIniciarAnalisis", u"Abrir el modulo de Inteligibilidad del Habla", None))
#endif // QT_CONFIG(tooltip)
        self.botonIniciarIH.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"Iniciar analisis", None))
        self.labelBadge3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"03", None))
        self.labelIcon3.setText("")
        self.labelTitle3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:16pt; font-weight:700; color:#ffffff;\">Base de Datos: Bloque H</span></p></body></html>", None))
        self.lbDescripcion3.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:10pt; color:rgba(255,255,255,0.80);\">Explora <b>23 tipos de aulas reales</b> del Bloque H de la Universidad del Atlantico.</span></p><p><span style=\"font-size:9pt; color:rgba(255,255,255,0.55);\">Conoce sus caracteristicas acusticas y realiza analisis sin ingresar datos manualmente.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.botonIniciarBD.setToolTip(QCoreApplication.translate("ventanaIniciarAnalisis", u"Abrir la base de datos de aulas del Bloque H", None))
#endif // QT_CONFIG(tooltip)
        self.botonIniciarBD.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"Explorar aulas", None))
        self.labelFooterInfo.setText(QCoreApplication.translate("ventanaIniciarAnalisis", u"<html><body><p><span style=\"font-size:8pt; color:rgba(255,255,255,0.38);\">Software de Evaluacion Acustica \u2014 Universidad del Atlantico \u00b7 Bloque H \u00b7 Barranquilla, Colombia</span></p></body></html>", None))
    # retranslateUi

