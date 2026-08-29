# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inteligibilidadHabla.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(836, 566)
        Form.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.495, y2:1, stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255))\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: transparent\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.frTop1 = QFrame(self.frame)
        self.frTop1.setObjectName(u"frTop1")
        self.frTop1.setMinimumSize(QSize(45, 80))
        self.frTop1.setMaximumSize(QSize(16777215, 80))
        self.frTop1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frTop1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botonAtras = QPushButton(self.frTop1)
        self.botonAtras.setObjectName(u"botonAtras")
        self.botonAtras.setMinimumSize(QSize(45, 45))
        self.botonAtras.setMaximumSize(QSize(45, 45))
        self.botonAtras.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u"estilos/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.botonAtras)

        self.horizontalSpacer = QSpacerItem(124, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frTop1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(190, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frTop1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"    background-color: transparent; /* Transparente con leve fondo */\n"
"    border: none;\n"
"    border-radius: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    background-color: transparent; /* Asegura que no herede fondo raro */\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background: rgba(255, 255, 255, 0.15);\n"
"    border: 1px solid white;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 20, 30, 20)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.distanciaRyE = QDoubleSpinBox(self.frame_8)
        self.distanciaRyE.setObjectName(u"distanciaRyE")
        self.distanciaRyE.setMinimumSize(QSize(90, 0))
        self.distanciaRyE.setMaximumSize(QSize(90, 16777215))
        self.distanciaRyE.setSingleStep(1.500000000000000)

        self.horizontalLayout_3.addWidget(self.distanciaRyE)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.recintoTR = QDoubleSpinBox(self.frame_12)
        self.recintoTR.setObjectName(u"recintoTR")
        self.recintoTR.setMinimumSize(QSize(90, 0))
        self.recintoTR.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.recintoTR)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.volumenSala = QDoubleSpinBox(self.frame_9)
        self.volumenSala.setObjectName(u"volumenSala")
        self.volumenSala.setMinimumSize(QSize(90, 0))
        self.volumenSala.setMaximumSize(QSize(90, 16777215))
        self.volumenSala.setMaximum(1000.000000000000000)
        self.volumenSala.setSingleStep(10.000000000000000)

        self.horizontalLayout_5.addWidget(self.volumenSala)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.coeficienteMedio = QDoubleSpinBox(self.frame_11)
        self.coeficienteMedio.setObjectName(u"coeficienteMedio")
        self.coeficienteMedio.setMinimumSize(QSize(90, 0))
        self.coeficienteMedio.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_6.addWidget(self.coeficienteMedio)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.superficieTotal = QDoubleSpinBox(self.frame_10)
        self.superficieTotal.setObjectName(u"superficieTotal")
        self.superficieTotal.setMinimumSize(QSize(90, 0))
        self.superficieTotal.setMaximumSize(QSize(90, 16777215))
        self.superficieTotal.setMaximum(1000.000000000000000)
        self.superficieTotal.setSingleStep(10.000000000000000)

        self.horizontalLayout_7.addWidget(self.superficieTotal)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)

        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"	font-size: 18px;\n"
"    border-radius: 15px;\n"
"\n"
"    padding: 10px 24px;\n"
"    letter-spacing: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.4);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(454, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.botonGoHome = QPushButton(self.frame_3)
        self.botonGoHome.setObjectName(u"botonGoHome")
        self.botonGoHome.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.botonGoHome)

        self.botonIniciarAnalisis = QPushButton(self.frame_3)
        self.botonIniciarAnalisis.setObjectName(u"botonIniciarAnalisis")
        self.botonIniciarAnalisis.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_8.addWidget(self.botonIniciarAnalisis)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.botonAtras.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700; color:#ffffff;\">Inteligibilidad Del Habla</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u00bfCu\u00e1l es la distancia entre el emisor y el receptor?", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ingresa el tiempo de reverberaci\u00f3n del recinto (TR):", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u00bfCu\u00e1nto mide el volumen total de la sala?", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ingresa el coeficiente medio de absorcion del aula", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Ingresa la superficie total del recinto:", None))
        self.botonGoHome.setText(QCoreApplication.translate("Form", u"Ir al Inicio", None))
        self.botonIniciarAnalisis.setText(QCoreApplication.translate("Form", u"Iniciar An\u00e1lisis", None))
    # retranslateUi

