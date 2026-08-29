# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoBD.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 580)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0.488, y1:0, x2:0.495, y2:1,\n"
"        stop:0.306818 rgba(0,0,93,255),\n"
"        stop:0.710227 rgba(0,0,45,255)\n"
"    );\n"
"}\n"
"QFrame { border: none; background-color: transparent; }\n"
"QScrollBar:vertical { background: transparent; width: 8px; margin: 2px 0 2px 0; }\n"
"QScrollBar::handle:vertical { background-color: rgba(255,255,255,0.25); min-height: 25px; border-radius: 4px; }\n"
"QScrollBar::handle:vertical:hover { background-color: rgba(255,255,255,0.45); }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; background: none; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet(u"QScrollArea { border: none; background: transparent; }")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 900, 580))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameTop = QFrame(self.frame)
        self.frameTop.setObjectName(u"frameTop")
        self.frameTop.setMinimumSize(QSize(0, 72))
        self.frameTop.setMaximumSize(QSize(16777215, 72))
        self.frameTop.setFrameShape(QFrame.NoFrame)
        self.frameTop.setStyleSheet(u"QFrame#frameTop { background-color: rgba(0,0,0,0.25); border-bottom: 1px solid rgba(255,255,255,0.14); }")
        self.horizontalLayout_4 = QHBoxLayout(self.frameTop)
        self.horizontalLayout_4.setSpacing(14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 0, 20, 0)
        self.botonAtras = QPushButton(self.frameTop)
        self.botonAtras.setObjectName(u"botonAtras")
        self.botonAtras.setMinimumSize(QSize(42, 42))
        self.botonAtras.setMaximumSize(QSize(42, 42))
        self.botonAtras.setStyleSheet(u"QPushButton { background-color: transparent; border: 1px solid rgba(255,255,255,0.35); border-radius: 21px; } QPushButton:hover { background-color: rgba(255,255,255,0.18); border: 1px solid white; } QPushButton:pressed { background-color: rgba(255,255,255,0.38); }")
        icon = QIcon()
        icon.addFile(u"graficas/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.botonAtras)

        self.spacerTopL = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.spacerTopL)

        self.frameTitulo = QFrame(self.frameTop)
        self.frameTitulo.setObjectName(u"frameTitulo")
        self.frameTitulo.setFrameShape(QFrame.NoFrame)
        self.vloTitulo = QVBoxLayout(self.frameTitulo)
        self.vloTitulo.setSpacing(2)
        self.vloTitulo.setObjectName(u"vloTitulo")
        self.vloTitulo.setContentsMargins(0, 8, 0, 8)
        self.labelTituloPrincipal = QLabel(self.frameTitulo)
        self.labelTituloPrincipal.setObjectName(u"labelTituloPrincipal")
        self.labelTituloPrincipal.setAlignment(Qt.AlignCenter)

        self.vloTitulo.addWidget(self.labelTituloPrincipal)

        self.labelSubtitulo = QLabel(self.frameTitulo)
        self.labelSubtitulo.setObjectName(u"labelSubtitulo")
        self.labelSubtitulo.setAlignment(Qt.AlignCenter)

        self.vloTitulo.addWidget(self.labelSubtitulo)


        self.horizontalLayout_4.addWidget(self.frameTitulo)

        self.spacerTopR = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.spacerTopR)


        self.verticalLayout_3.addWidget(self.frameTop)

        self.frameMedium = QFrame(self.frame)
        self.frameMedium.setObjectName(u"frameMedium")
        self.frameMedium.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameMedium)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 16, 20, 16)
        self.frame_2 = QFrame(self.frameMedium)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setMaximumSize(QSize(16777215, 64))
        self.frame_3.setStyleSheet(u"QFrame#frame_3 { background-color: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.22); border-radius: 12px; } QLabel { color: rgba(255,255,255,0.70); font-size: 10pt; font-weight: bold; background: transparent; border: none; } QComboBox { background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.45); border-radius: 8px; color: white; font-size: 11pt; font-weight: bold; padding: 5px 10px; min-height: 32px; } QComboBox:hover { border: 1px solid #7ec8f7; background: rgba(126,200,247,0.15); } QComboBox::drop-down { border: none; width: 24px; } QComboBox QAbstractItemView { background-color: #001a4d; color: white; selection-background-color: rgba(126,200,247,0.30); border: 1px solid rgba(255,255,255,0.25); border-radius: 6px; } QComboBox QScrollBar:vertical { border: none; background: #f0f0f0; width: 10px; } QComboBox QScrollBar::handle:vertical { background: #bfbfbf; min-height: 20px; border-radius: 4px; }")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 8, 16, 8)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignVCenter|Qt.AlignLeft)

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"QFrame#cardDim { background-color: rgba(255,255,255,0.09); border: 1px solid rgba(255,255,255,0.22); border-radius: 10px; } QLabel#labelDimEtiq { color: rgba(255,255,255,0.55); font-size: 8pt; background: transparent; border: none; } QLabel#labelDimVal { color: white; font-size: 14pt; font-weight: bold; background: transparent; border: none; }")
        self.gridLayout = QHBoxLayout(self.frame_4)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cardAula = QFrame(self.frame_4)
        self.cardAula.setObjectName(u"cardAula")
        self.cardAula.setFrameShape(QFrame.NoFrame)
        self.vloCA = QVBoxLayout(self.cardAula)
        self.vloCA.setSpacing(2)
        self.vloCA.setObjectName(u"vloCA")
        self.vloCA.setContentsMargins(10, 6, 10, 6)
        self.labelEtiqAula = QLabel(self.cardAula)
        self.labelEtiqAula.setObjectName(u"labelEtiqAula")
        self.labelEtiqAula.setAlignment(Qt.AlignCenter)

        self.vloCA.addWidget(self.labelEtiqAula)

        self.labelNumeroAula = QLabel(self.cardAula)
        self.labelNumeroAula.setObjectName(u"labelNumeroAula")
        self.labelNumeroAula.setAlignment(Qt.AlignCenter)

        self.vloCA.addWidget(self.labelNumeroAula)


        self.gridLayout.addWidget(self.cardAula)

        self.cardLargo = QFrame(self.frame_4)
        self.cardLargo.setObjectName(u"cardLargo")
        self.cardLargo.setFrameShape(QFrame.NoFrame)
        self.vloCL = QVBoxLayout(self.cardLargo)
        self.vloCL.setSpacing(2)
        self.vloCL.setObjectName(u"vloCL")
        self.vloCL.setContentsMargins(10, 6, 10, 6)
        self.labelEtiqLargo = QLabel(self.cardLargo)
        self.labelEtiqLargo.setObjectName(u"labelEtiqLargo")
        self.labelEtiqLargo.setAlignment(Qt.AlignCenter)

        self.vloCL.addWidget(self.labelEtiqLargo)

        self.labelLargo = QLabel(self.cardLargo)
        self.labelLargo.setObjectName(u"labelLargo")
        self.labelLargo.setAlignment(Qt.AlignCenter)

        self.vloCL.addWidget(self.labelLargo)


        self.gridLayout.addWidget(self.cardLargo)

        self.cardAncho = QFrame(self.frame_4)
        self.cardAncho.setObjectName(u"cardAncho")
        self.cardAncho.setFrameShape(QFrame.NoFrame)
        self.vloCAncho = QVBoxLayout(self.cardAncho)
        self.vloCAncho.setSpacing(2)
        self.vloCAncho.setObjectName(u"vloCAncho")
        self.vloCAncho.setContentsMargins(10, 6, 10, 6)
        self.labelEtiqAncho = QLabel(self.cardAncho)
        self.labelEtiqAncho.setObjectName(u"labelEtiqAncho")
        self.labelEtiqAncho.setAlignment(Qt.AlignCenter)

        self.vloCAncho.addWidget(self.labelEtiqAncho)

        self.labelAncho = QLabel(self.cardAncho)
        self.labelAncho.setObjectName(u"labelAncho")
        self.labelAncho.setAlignment(Qt.AlignCenter)

        self.vloCAncho.addWidget(self.labelAncho)


        self.gridLayout.addWidget(self.cardAncho)

        self.cardAlto = QFrame(self.frame_4)
        self.cardAlto.setObjectName(u"cardAlto")
        self.cardAlto.setFrameShape(QFrame.NoFrame)
        self.vloCAlto = QVBoxLayout(self.cardAlto)
        self.vloCAlto.setSpacing(2)
        self.vloCAlto.setObjectName(u"vloCAlto")
        self.vloCAlto.setContentsMargins(10, 6, 10, 6)
        self.labelEtiqAlto = QLabel(self.cardAlto)
        self.labelEtiqAlto.setObjectName(u"labelEtiqAlto")
        self.labelEtiqAlto.setAlignment(Qt.AlignCenter)

        self.vloCAlto.addWidget(self.labelEtiqAlto)

        self.labelAlto = QLabel(self.cardAlto)
        self.labelAlto.setObjectName(u"labelAlto")
        self.labelAlto.setAlignment(Qt.AlignCenter)

        self.vloCAlto.addWidget(self.labelAlto)


        self.gridLayout.addWidget(self.cardAlto)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frameTreeHeader = QFrame(self.frame_2)
        self.frameTreeHeader.setObjectName(u"frameTreeHeader")
        self.frameTreeHeader.setFrameShape(QFrame.NoFrame)
        self.frameTreeHeader.setMaximumSize(QSize(16777215, 28))
        self.hloTreeHeader = QHBoxLayout(self.frameTreeHeader)
        self.hloTreeHeader.setSpacing(8)
        self.hloTreeHeader.setObjectName(u"hloTreeHeader")
        self.hloTreeHeader.setContentsMargins(2, 0, 2, 0)
        self.accentBar = QFrame(self.frameTreeHeader)
        self.accentBar.setObjectName(u"accentBar")
        self.accentBar.setFrameShape(QFrame.NoFrame)
        self.accentBar.setMinimumSize(QSize(4, 18))
        self.accentBar.setMaximumSize(QSize(4, 18))
        self.accentBar.setStyleSheet(u"QFrame { background-color: rgba(222,112,25,0.9); border-radius: 2px; }")

        self.hloTreeHeader.addWidget(self.accentBar)

        self.labelTreeTitulo = QLabel(self.frameTreeHeader)
        self.labelTreeTitulo.setObjectName(u"labelTreeTitulo")

        self.hloTreeHeader.addWidget(self.labelTreeTitulo)

        self.labelTreeDesc = QLabel(self.frameTreeHeader)
        self.labelTreeDesc.setObjectName(u"labelTreeDesc")

        self.hloTreeHeader.addWidget(self.labelTreeDesc)

        self.spacerTreeH = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hloTreeHeader.addItem(self.spacerTreeH)


        self.verticalLayout_4.addWidget(self.frameTreeHeader)

        self.scrollMateriales = QScrollArea(self.frame_2)
        self.scrollMateriales.setObjectName(u"scrollMateriales")
        self.scrollMateriales.setWidgetResizable(True)
        self.scrollMateriales.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollMateriales.setStyleSheet(u"QScrollArea#scrollMateriales {\n"
"    background-color: rgba(255,255,255,0.04);\n"
"    border: 1px solid rgba(255,255,255,0.13);\n"
"    border-radius: 12px;\n"
"}\n"
"QScrollArea#scrollMateriales > QWidget > QWidget { background: transparent; }\n"
"QScrollArea#scrollMateriales QScrollBar:vertical {\n"
"    background: transparent; width: 6px; margin: 4px 0 4px 0;\n"
"}\n"
"QScrollArea#scrollMateriales QScrollBar::handle:vertical {\n"
"    background-color: rgba(255,255,255,0.22); min-height: 20px; border-radius: 3px;\n"
"}\n"
"QScrollArea#scrollMateriales QScrollBar::handle:vertical:hover { background-color: rgba(255,255,255,0.40); }\n"
"QScrollArea#scrollMateriales QScrollBar::add-line:vertical,\n"
"QScrollArea#scrollMateriales QScrollBar::sub-line:vertical { height: 0px; background: none; }\n"
"QScrollArea#scrollMateriales QScrollBar::add-page:vertical,\n"
"QScrollArea#scrollMateriales QScrollBar::sub-page:vertical { background: none; }\n"
"")
        self.contenedorCards = QWidget()
        self.contenedorCards.setObjectName(u"contenedorCards")
        self.contenedorCards.setStyleSheet(u"QWidget#contenedorCards { background: transparent; }")
        self.scrollMateriales.setWidget(self.contenedorCards)

        self.verticalLayout_4.addWidget(self.scrollMateriales)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frameMedium)

        self.frameBottom = QFrame(self.frame)
        self.frameBottom.setObjectName(u"frameBottom")
        self.frameBottom.setMinimumSize(QSize(0, 64))
        self.frameBottom.setMaximumSize(QSize(16777215, 64))
        self.frameBottom.setFrameShape(QFrame.NoFrame)
        self.frameBottom.setStyleSheet(u"QFrame#frameBottom { background-color: rgba(0,0,0,0.22); border-top: 1px solid rgba(255,255,255,0.12); } QPushButton { background-color: rgba(255,255,255,0.12); border: 1.5px solid rgba(255,255,255,0.45); color: white; font-weight: bold; font-size: 12px; border-radius: 12px; padding: 8px 22px; letter-spacing: 0.5px; } QPushButton:hover { background-color: rgba(255,255,255,0.25); border: 1.5px solid white; } QPushButton:pressed { background-color: rgba(255,255,255,0.45); color: #00005d; } QPushButton#botonIniciarAnalisis { background-color: rgba(126,200,247,0.20); border: 1.5px solid #7ec8f7; color: #7ec8f7; min-width: 180px; } QPushButton#botonIniciarAnalisis:hover { background-color: rgba(126,200,247,0.38); color: white; border-color: white; } QPushButton#botonIniciarAnalisis:disabled { background-color: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.18); color: rgba(255,255,255,0.30); }")
        self.horizontalLayout_5 = QHBoxLayout(self.frameBottom)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.botonIniciarAnalisis = QPushButton(self.frameBottom)
        self.botonIniciarAnalisis.setObjectName(u"botonIniciarAnalisis")
        self.botonIniciarAnalisis.setMinimumSize(QSize(180, 0))
        self.botonIniciarAnalisis.setMaximumSize(QSize(220, 16777215))

        self.horizontalLayout_5.addWidget(self.botonIniciarAnalisis)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addWidget(self.frameBottom)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 8)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.botonAtras.setText("")
#if QT_CONFIG(tooltip)
        self.botonAtras.setToolTip(QCoreApplication.translate("Form", u"Regresar a la pantalla anterior", None))
#endif // QT_CONFIG(tooltip)
        self.labelTituloPrincipal.setText(QCoreApplication.translate("Form", u"<html><body><p><span style=\"font-size:20pt; font-weight:700; color:#ffffff;\">Base de Datos \u2014 Bloque H</span></p></body></html>", None))
        self.labelSubtitulo.setText(QCoreApplication.translate("Form", u"<html><body><p><span style=\"font-size:9pt; color:rgba(255,255,255,0.60);\">23 tipos de aula registrados \u2014 Universidad del Atlantico</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tipo de aula \u2014 Bloque H:", None))
#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Form", u"Selecciona un tipo de aula para ver su informacion", None))
#endif // QT_CONFIG(tooltip)
        self.cardAula.setObjectName(QCoreApplication.translate("Form", u"cardDim", None))
        self.labelEtiqAula.setObjectName(QCoreApplication.translate("Form", u"labelDimEtiq", None))
        self.labelEtiqAula.setText(QCoreApplication.translate("Form", u"AULAS", None))
        self.labelNumeroAula.setObjectName(QCoreApplication.translate("Form", u"labelDimVal", None))
        self.labelNumeroAula.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.cardLargo.setObjectName(QCoreApplication.translate("Form", u"cardDim", None))
        self.labelEtiqLargo.setObjectName(QCoreApplication.translate("Form", u"labelDimEtiq", None))
        self.labelEtiqLargo.setText(QCoreApplication.translate("Form", u"LARGO", None))
        self.labelLargo.setObjectName(QCoreApplication.translate("Form", u"labelDimVal", None))
        self.labelLargo.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.cardAncho.setObjectName(QCoreApplication.translate("Form", u"cardDim", None))
        self.labelEtiqAncho.setObjectName(QCoreApplication.translate("Form", u"labelDimEtiq", None))
        self.labelEtiqAncho.setText(QCoreApplication.translate("Form", u"ANCHO", None))
        self.labelAncho.setObjectName(QCoreApplication.translate("Form", u"labelDimVal", None))
        self.labelAncho.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.cardAlto.setObjectName(QCoreApplication.translate("Form", u"cardDim", None))
        self.labelEtiqAlto.setObjectName(QCoreApplication.translate("Form", u"labelDimEtiq", None))
        self.labelEtiqAlto.setText(QCoreApplication.translate("Form", u"ALTO", None))
        self.labelAlto.setObjectName(QCoreApplication.translate("Form", u"labelDimVal", None))
        self.labelAlto.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.labelTreeTitulo.setText(QCoreApplication.translate("Form", u"<html><body><span style=\"font-size:10pt; font-weight:bold; color:white;\">Materiales y elementos del salon</span></body></html>", None))
        self.labelTreeDesc.setText(QCoreApplication.translate("Form", u"<html><body><span style=\"font-size:8pt; color:rgba(255,255,255,0.50);\">6 superficies + objetos adicionales</span></body></html>", None))
        self.botonIniciarAnalisis.setText(QCoreApplication.translate("Form", u"Iniciar Analisis", None))
#if QT_CONFIG(tooltip)
        self.botonIniciarAnalisis.setToolTip(QCoreApplication.translate("Form", u"Calcular RT60 y %ALCons usando los datos del aula seleccionada", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

