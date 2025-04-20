# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vistaGraficaRT.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)

class Ui_formGraficoRT(object):
    def setupUi(self, formGraficoRT):
        if not formGraficoRT.objectName():
            formGraficoRT.setObjectName(u"formGraficoRT")
        formGraficoRT.resize(795, 560)
        formGraficoRT.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.495, y2:1, stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255))\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: none;\n"
"    background: transparent; /* Opcional */\n"
"}\n"
"\n"
"\n"
"   QScrollBar:vertical {\n"
"        background: transparent;\n"
"        width: 8px;\n"
"        margin: 2px 0 2px 0;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: rgba(100, 100, 100, 120);  /* color gris suave */\n"
"        min-height: 25px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical:hover {\n"
"        background-color: rgba(80, 80, 80, 160);  /* m\u00e1s oscuro al pasar el mouse */\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        height: 0px;\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vert"
                        "ical {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:horizontal {\n"
"        background: transparent;\n"
"        height: 8px;\n"
"        margin: 0 2px 0 2px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal {\n"
"        background-color: rgba(100, 100, 100, 120);\n"
"        min-width: 25px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal:hover {\n"
"        background-color: rgba(80, 80, 80, 160);\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"        width: 0px;\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"        background: none;\n"
"    }")
        self.verticalLayout = QVBoxLayout(formGraficoRT)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(formGraficoRT)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -80, 787, 652))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameTop = QFrame(self.scrollAreaWidgetContents)
        self.frameTop.setObjectName(u"frameTop")
        self.frameTop.setMinimumSize(QSize(0, 60))
        self.frameTop.setFrameShape(QFrame.StyledPanel)
        self.frameTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.botonAtras = QPushButton(self.frameTop)
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
        icon.addFile(u"graficas/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.botonAtras)

        self.horizontalSpacer = QSpacerItem(258, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frameTop)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(257, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frameTop)

        self.frameMedium = QFrame(self.scrollAreaWidgetContents)
        self.frameMedium.setObjectName(u"frameMedium")
        self.frameMedium.setFrameShape(QFrame.StyledPanel)
        self.frameMedium.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameMedium)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameGrafica = QFrame(self.frameMedium)
        self.frameGrafica.setObjectName(u"frameGrafica")
        self.frameGrafica.setFrameShape(QFrame.StyledPanel)
        self.frameGrafica.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameGrafica)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.grafica = QLabel(self.frameGrafica)
        self.grafica.setObjectName(u"grafica")

        self.verticalLayout_8.addWidget(self.grafica)


        self.horizontalLayout.addWidget(self.frameGrafica)

        self.frame_2 = QFrame(self.frameMedium)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setStyleSheet(u"QStackedWidget {\n"
"    background-color: trasparent; /* Totalmente transparente */\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QFrame {\n"
"    background-color: transparent; /* Totalmente transparente */\n"
"}\n"
"QStackedWidget {\n"
"    background-color: transparent; /* Totalmente transparente */\n"
"}\n"
"")
        self.pageRT = QWidget()
        self.pageRT.setObjectName(u"pageRT")
        self.pageRT.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.pageRT)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.infoRT = QFrame(self.pageRT)
        self.infoRT.setObjectName(u"infoRT")
        self.infoRT.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 180);\n"
"    border-radius: 12px;\n"
"    border: 10px solid white;\n"
"    padding: 10px;\n"
"    box-shadow: 5px 4px 12px rgba(0, 0, 0, 0.1); /* Sombra suave */\n"
"}\n"
"")
        self.infoRT.setFrameShape(QFrame.StyledPanel)
        self.infoRT.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.infoRT)

        self.stackedWidget.addWidget(self.pageRT)
        self.pageCombinada_2 = QWidget()
        self.pageCombinada_2.setObjectName(u"pageCombinada_2")
        self.verticalLayout_5 = QVBoxLayout(self.pageCombinada_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tollboxCombinada = QToolBox(self.pageCombinada_2)
        self.tollboxCombinada.setObjectName(u"tollboxCombinada")
        self.tollboxCombinada.setMinimumSize(QSize(0, 450))
        self.tollboxCombinada.setStyleSheet(u"QToolBox {\n"
"    background: #fefefe; /* Fondo tipo tarjeta */\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 12px;\n"
"    padding: 5px;\n"
"    font: 12pt \"Segoe UI\";\n"
"    color: #333;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background: #f0f0f5;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 1px 15px;\n"
"    margin: 1px 2px;\n"
"    font-weight: 500;\n"
"    color: #333;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    background: #e0e0e8;\n"
"    font-weight: bold;\n"
"    color: #111;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    background: #eaeaf0;\n"
"}\n"
"")
        self.pageRT_2 = QWidget()
        self.pageRT_2.setObjectName(u"pageRT_2")
        self.pageRT_2.setGeometry(QRect(0, 0, 308, 368))
        self.verticalLayout_6 = QVBoxLayout(self.pageRT_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.pageRT_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 308, 368))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contenidoTR = QFrame(self.scrollAreaWidgetContents_2)
        self.contenidoTR.setObjectName(u"contenidoTR")
        self.contenidoTR.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco con transparencia */\n"
"    padding: 10px;\n"
"}\n"
"")
        self.contenidoTR.setFrameShape(QFrame.StyledPanel)
        self.contenidoTR.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.contenidoTR)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.contenidoTR)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco con transparencia */\n"
"    padding: 10px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableRT = QTableWidget(self.frame)
        self.tableRT.setObjectName(u"tableRT")

        self.verticalLayout_11.addWidget(self.tableRT)


        self.verticalLayout_10.addWidget(self.frame)

        self.frame_3 = QFrame(self.contenidoTR)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelResumeSabine = QLabel(self.frame_3)
        self.labelResumeSabine.setObjectName(u"labelResumeSabine")

        self.verticalLayout_12.addWidget(self.labelResumeSabine)

        self.frameIndicador = QFrame(self.frame_3)
        self.frameIndicador.setObjectName(u"frameIndicador")
        self.frameIndicador.setStyleSheet(u"")
        self.frameIndicador.setFrameShape(QFrame.StyledPanel)
        self.frameIndicador.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameIndicador)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelIndicador = QLabel(self.frameIndicador)
        self.labelIndicador.setObjectName(u"labelIndicador")

        self.horizontalLayout_4.addWidget(self.labelIndicador)

        self.indicador = QFrame(self.frameIndicador)
        self.indicador.setObjectName(u"indicador")
        self.indicador.setFrameShape(QFrame.StyledPanel)
        self.indicador.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.indicador)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_12.addWidget(self.frameIndicador)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.contenidoTR)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelConclusion = QLabel(self.frame_4)
        self.labelConclusion.setObjectName(u"labelConclusion")

        self.verticalLayout_13.addWidget(self.labelConclusion)


        self.verticalLayout_10.addWidget(self.frame_4)


        self.verticalLayout_7.addWidget(self.contenidoTR)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.tollboxCombinada.addItem(self.pageRT_2, u"Page 1")
        self.pageAlcons = QWidget()
        self.pageAlcons.setObjectName(u"pageAlcons")
        self.pageAlcons.setGeometry(QRect(0, 0, 308, 368))
        font = QFont()
        font.setKerning(True)
        self.pageAlcons.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.pageAlcons)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.infoAlcons = QFrame(self.pageAlcons)
        self.infoAlcons.setObjectName(u"infoAlcons")
        self.infoAlcons.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco con transparencia */\n"
"    padding: 10px;\n"
"}\n"
"")
        self.infoAlcons.setFrameShape(QFrame.StyledPanel)
        self.infoAlcons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.infoAlcons)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.infoAlcons)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.labelAlcons = QLabel(self.frame_5)
        self.labelAlcons.setObjectName(u"labelAlcons")

        self.verticalLayout_15.addWidget(self.labelAlcons)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.labelEvaluacion = QLabel(self.frame_5)
        self.labelEvaluacion.setObjectName(u"labelEvaluacion")

        self.verticalLayout_15.addWidget(self.labelEvaluacion)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 2)
        self.verticalLayout_15.setStretch(2, 1)
        self.verticalLayout_15.setStretch(3, 5)
        self.verticalLayout_15.setStretch(4, 1)

        self.verticalLayout_14.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.infoAlcons)

        self.tollboxCombinada.addItem(self.pageAlcons, u"Page 2")

        self.verticalLayout_5.addWidget(self.tollboxCombinada)

        self.stackedWidget.addWidget(self.pageCombinada_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frameMedium)

        self.frameBottom = QFrame(self.scrollAreaWidgetContents)
        self.frameBottom.setObjectName(u"frameBottom")
        self.frameBottom.setMinimumSize(QSize(0, 60))
        self.frameBottom.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"	font-size: 13px;\n"
"    border-radius: 13px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.4);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"}")
        self.frameBottom.setFrameShape(QFrame.StyledPanel)
        self.frameBottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameBottom)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(512, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.botonGoHome = QPushButton(self.frameBottom)
        self.botonGoHome.setObjectName(u"botonGoHome")

        self.horizontalLayout_3.addWidget(self.botonGoHome)

        self.botonGuardarPDF = QPushButton(self.frameBottom)
        self.botonGuardarPDF.setObjectName(u"botonGuardarPDF")

        self.horizontalLayout_3.addWidget(self.botonGuardarPDF)


        self.verticalLayout_2.addWidget(self.frameBottom)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
        self.verticalLayout_2.setStretch(2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(formGraficoRT)

        self.stackedWidget.setCurrentIndex(1)
        self.tollboxCombinada.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(formGraficoRT)
    # setupUi

    def retranslateUi(self, formGraficoRT):
        formGraficoRT.setWindowTitle(QCoreApplication.translate("formGraficoRT", u"Form", None))
        self.botonAtras.setText("")
        self.label.setText(QCoreApplication.translate("formGraficoRT", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\">Reporte Final</span></p></body></html>", None))
        self.grafica.setText("")
        self.labelResumeSabine.setText("")
        self.labelIndicador.setText("")
        self.labelConclusion.setText("")
        self.tollboxCombinada.setItemText(self.tollboxCombinada.indexOf(self.pageRT_2), QCoreApplication.translate("formGraficoRT", u"Page 1", None))
        self.labelAlcons.setText("")
        self.labelEvaluacion.setText("")
        self.tollboxCombinada.setItemText(self.tollboxCombinada.indexOf(self.pageAlcons), QCoreApplication.translate("formGraficoRT", u"Page 2", None))
        self.botonGoHome.setText(QCoreApplication.translate("formGraficoRT", u"Ir al Inicio", None))
        self.botonGuardarPDF.setText(QCoreApplication.translate("formGraficoRT", u"Guardar Reporte PDF", None))
    # retranslateUi

