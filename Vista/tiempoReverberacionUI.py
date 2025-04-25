# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiempoReverberacionUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_FormTR(object):
    def setupUi(self, FormTR):
        if not FormTR.objectName():
            FormTR.setObjectName(u"FormTR")
        FormTR.resize(1036, 619)
        FormTR.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.495, y2:1, stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255))\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(FormTR)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(FormTR)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 40))
        self.scrollArea.setStyleSheet(u"    QScrollBar:vertical {\n"
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
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
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
"        border"
                        "-radius: 4px;\n"
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1026, 627))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: transparent\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frTop1 = QFrame(self.frame)
        self.frTop1.setObjectName(u"frTop1")
        self.frTop1.setMinimumSize(QSize(45, 60))
        self.frTop1.setMaximumSize(QSize(16777215, 60))
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
        icon.addFile(u"graficas/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.botonAtras)

        self.horizontalSpacer = QSpacerItem(267, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frTop1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(267, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frTop1)

        self.frMedium2 = QFrame(self.frame)
        self.frMedium2.setObjectName(u"frMedium2")
        self.frMedium2.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid white; /* Borde blanco */\n"
"    border-radius: 10px;  /* Bordes redondeados */\n"
"    margin-top: 10px; /* Espacio para el t\u00edtulo */\n"
"    background-color: rgba(255, 255, 255, 20); /* Color de fondo trasl\u00facido */\n"
"    font: bold 12px \"Arial\"; /* Texto en negrita */\n"
"    color: white; /* Color del texto */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; /* Para que el t\u00edtulo no se sobreponga */\n"
"    subcontrol-position: top center; /* Centrar el t\u00edtulo arriba */\n"
"    padding: 5px; /* Espaciado del t\u00edtulo */\n"
"    font-size: 14px; /* Tama\u00f1o del t\u00edtulo */\n"
"    color: white; /* Color del t\u00edtulo */\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: white;  /* Letras en blanco */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid white; /* Borde blanco semitransparente */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    background-color: rg"
                        "ba(255, 255, 255, 0.2); /* Blanco transl\u00facido */\n"
"    color: white; /* Texto blanco */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    selection-background-color: rgba(255, 255, 255, 0.3); /* Selecci\u00f3n en blanco transl\u00facido */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid cyan;  /* Cuando se selecciona, cambia el borde a cyan */\n"
"    box-shadow: 0px 0px 10px cyan; /* Brillo alrededor */\n"
"    background-color: rgba(255, 255, 255, 0.5); /* Un poco m\u00e1s blanco al seleccionarlo */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background: rgba(255, 255, 255, 0.2); /* Fondo transl\u00facido */\n"
"    border: 1px solid white; /* Borde blanco */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    color: white; /* Texto blanco */\n"
"    padding: 3px; /* Espaciado interno */\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        background-color: white;\n"
"        color: black;\n"
"        selection-background-color: lightgray;\n"
"    }\n"
"\n"
""
                        "    QComboBox QScrollBar:vertical {\n"
"        border: none;\n"
"        background: #f0f0f0;\n"
"        width: 10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"    QComboBox QScrollBar::handle:vertical {\n"
"        background: #bfbfbf;\n"
"        min-height: 20px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QComboBox QScrollBar::handle:vertical:hover {\n"
"        background: #a6a6a6;\n"
"    }\n"
"\n"
"    QComboBox QScrollBar::add-line:vertical,\n"
"    QComboBox QScrollBar::sub-line:vertical {\n"
"        height: 0px;\n"
"    }\n"
"\n"
"    QComboBox QScrollBar::add-page:vertical,\n"
"    QComboBox QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"/* Checkbox */\n"
"QCheckBox {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 4px;\n"
"    background: rgba(255, 255, 255, 0.2); /* Fondo sutil */\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"\n"
"/* Hover para dar efe"
                        "cto visual */\n"
"QCheckBox::indicator:hover {\n"
"    background: rgba(255, 255, 255, 0.4);\n"
"}\n"
"/* Aqu\u00ed NO se usa 'image', as\u00ed Qt usa el chulito predeterminado */\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(255, 255, 255, 0.8);\n"
"	image: url(Vista/graficas/iconos/controlar.png);\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Botones \"+\" y \"-\" */\n"
"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.frMedium2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frMedium2)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_5 = QFrame(self.frMedium2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.boxDimensiones = QGroupBox(self.frame_5)
        self.boxDimensiones.setObjectName(u"boxDimensiones")
        self.boxDimensiones.setAutoFillBackground(False)
        self.boxDimensiones.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.boxDimensiones)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 9, 20, 9)
        self.frame_2 = QFrame(self.boxDimensiones)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineLargo = QLineEdit(self.frame_2)
        self.lineLargo.setObjectName(u"lineLargo")
        self.lineLargo.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.lineLargo)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.boxDimensiones)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineAncho = QLineEdit(self.frame_3)
        self.lineAncho.setObjectName(u"lineAncho")

        self.horizontalLayout_4.addWidget(self.lineAncho)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.boxDimensiones)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineAlto = QLineEdit(self.frame_4)
        self.lineAlto.setObjectName(u"lineAlto")

        self.horizontalLayout_5.addWidget(self.lineAlto)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.labelErrorDimensiones = QLabel(self.boxDimensiones)
        self.labelErrorDimensiones.setObjectName(u"labelErrorDimensiones")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelErrorDimensiones.sizePolicy().hasHeightForWidth())
        self.labelErrorDimensiones.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.labelErrorDimensiones)


        self.verticalLayout_7.addWidget(self.boxDimensiones)

        self.groupBox_3 = QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setStyleSheet(u"QCheckBox {\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.checkObjAdicional = QCheckBox(self.groupBox_3)
        self.checkObjAdicional.setObjectName(u"checkObjAdicional")
        self.checkObjAdicional.setLayoutDirection(Qt.RightToLeft)
        self.checkObjAdicional.setAutoFillBackground(False)

        self.verticalLayout_20.addWidget(self.checkObjAdicional)

        self.contObjAdicional = QFrame(self.groupBox_3)
        self.contObjAdicional.setObjectName(u"contObjAdicional")
        self.contObjAdicional.setEnabled(False)
        self.contObjAdicional.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2F80ED;\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Fondo transl\u00facido */\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    padding: 6px 10px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #2F80ED;  /* Azul el\u00e9ctrico al seleccionar */\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"/* Flechas de incremento y decremento */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/*QSpinBox::up-arrow {\n"
"    image: url(:/iconos/flecha_arriba.png);Cambia por tu icono o c"
                        "omenta si no tienes \n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/iconos/flecha_abajo.png);  Cambia por tu icono o comenta si no tienes \n"
"}\n"
"*/\n"
"/* Hover */\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"\n"
"QLabel:disabled,\n"
"QLineEdit:disabled,\n"
"QComboBox:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled,\n"
"QCheckBox:disabled {\n"
"    color: rgba(255, 255, 255, 0.4);  /* Letras opacas en los widgets internos */\n"
"}\n"
"")
        self.contObjAdicional.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_19 = QVBoxLayout(self.contObjAdicional)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.objAdic = QFrame(self.contObjAdicional)
        self.objAdic.setObjectName(u"objAdic")
        self.objAdic.setEnabled(False)
        self.objAdic.setFrameShape(QFrame.StyledPanel)
        self.objAdic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.objAdic)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_19.addWidget(self.objAdic)


        self.verticalLayout_20.addWidget(self.contObjAdicional)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.gbInteligibilad = QGroupBox(self.frame_5)
        self.gbInteligibilad.setObjectName(u"gbInteligibilad")
        self.gbInteligibilad.setEnabled(False)
        self.gbInteligibilad.setStyleSheet(u"\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background: rgba(255, 255, 255, 0.15);\n"
"    border: 1px solid white;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox:disabled {\n"
"    background-color: rgba(100, 100, 100, 0.3); /* Fondo gris transl\u00facido cuando est\u00e1 desactivado */\n"
"    color: gray;  /* Color del texto tambi\u00e9n puede cambiar */\n"
"    border: 1px gray;\n"
"}\n"
"\n"
"QGroupBox QLabel:disabled,\n"
"QGroupBox QLineEdit:disabled,\n"
"QGroupBox QComboBox:disabled,\n"
"QGroupBox QSpinBox:disabled,\n"
"QGroupBox QDoubleSpinBox:disabled,\n"
"QGroupBox QCheckBox:disabled {\n"
"    color: rgba(255, 255, 255, 0.4);  /* Letras opacas en los widgets internos */\n"
"}\n"
"QGroupBox::title:disabled {\n"
"    color: rgba(255, 255, 255, 0.3);  /* T\u00edtulo m\u00e1s opaco */\n"
"}\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.gbInteligibilad)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_8 = QFrame(self.gbInteligibilad)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_15)

        self.distanciaRyE = QDoubleSpinBox(self.frame_8)
        self.distanciaRyE.setObjectName(u"distanciaRyE")
        self.distanciaRyE.setMinimumSize(QSize(90, 0))
        self.distanciaRyE.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_22.addWidget(self.distanciaRyE)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_12.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.gbInteligibilad)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_14)

        self.coeficienteMedio = QDoubleSpinBox(self.frame_11)
        self.coeficienteMedio.setObjectName(u"coeficienteMedio")
        self.coeficienteMedio.setMinimumSize(QSize(90, 0))
        self.coeficienteMedio.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_23.addWidget(self.coeficienteMedio)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.label_16 = QLabel(self.gbInteligibilad)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_12.addWidget(self.label_16)


        self.verticalLayout_7.addWidget(self.gbInteligibilad)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.boxSuperficies = QGroupBox(self.frMedium2)
        self.boxSuperficies.setObjectName(u"boxSuperficies")
        sizePolicy.setHeightForWidth(self.boxSuperficies.sizePolicy().hasHeightForWidth())
        self.boxSuperficies.setSizePolicy(sizePolicy)
        self.boxSuperficies.setAutoFillBackground(False)
        self.boxSuperficies.setStyleSheet(u"    QLineEdit {\n"
"        font-size: 11px;         /* Tama\u00f1o del texto */\n"
"        font-weight: normal;     /* Opcional: puedes usar 'bold' */\n"
"        color: white;            /* Color del texto */\n"
"        background: rgba(255, 255, 255, 0.2); /* Fondo trasl\u00facido */\n"
"        border: 1px solid white;\n"
"        border-radius: 8px;\n"
"        padding: 4px 8px;\n"
"    }\n"
"    \n"
"    QLineEdit:focus {\n"
"        border: 1px solid #00AEEF; /* Borde azul al enfocar */\n"
"        background: rgba(255, 255, 255, 0.3);\n"
"    }")
        self.gridLayout = QGridLayout(self.boxSuperficies)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frParedFrontal = QFrame(self.boxSuperficies)
        self.frParedFrontal.setObjectName(u"frParedFrontal")
        self.frParedFrontal.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frParedFrontal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pdFrontal = QFrame(self.frParedFrontal)
        self.pdFrontal.setObjectName(u"pdFrontal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pdFrontal.sizePolicy().hasHeightForWidth())
        self.pdFrontal.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setKerning(True)
        self.pdFrontal.setFont(font)
        self.pdFrontal.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.pdFrontal)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.label_8 = QLabel(self.pdFrontal)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.cbPdFrontal = QComboBox(self.pdFrontal)
        self.cbPdFrontal.setObjectName(u"cbPdFrontal")
        self.cbPdFrontal.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_6.addWidget(self.cbPdFrontal)

        self.checkPdFrontal = QCheckBox(self.pdFrontal)
        self.checkPdFrontal.setObjectName(u"checkPdFrontal")
        self.checkPdFrontal.setMaximumSize(QSize(25, 25))
        self.checkPdFrontal.setCursor(QCursor(Qt.ArrowCursor))
        self.checkPdFrontal.setFocusPolicy(Qt.StrongFocus)
        self.checkPdFrontal.setContextMenuPolicy(Qt.PreventContextMenu)
        self.checkPdFrontal.setStyleSheet(u"")
        self.checkPdFrontal.setIconSize(QSize(16, 16))
        self.checkPdFrontal.setCheckable(True)
        self.checkPdFrontal.setChecked(False)
        self.checkPdFrontal.setAutoRepeat(False)
        self.checkPdFrontal.setAutoExclusive(False)
        self.checkPdFrontal.setTristate(False)

        self.horizontalLayout_6.addWidget(self.checkPdFrontal)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.pdFrontal)

        self.contObjFrontal = QFrame(self.frParedFrontal)
        self.contObjFrontal.setObjectName(u"contObjFrontal")
        sizePolicy.setHeightForWidth(self.contObjFrontal.sizePolicy().hasHeightForWidth())
        self.contObjFrontal.setSizePolicy(sizePolicy)
        self.contObjFrontal.setFrameShape(QFrame.NoFrame)
        self.contObjFrontal.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.contObjFrontal)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.objetoPdFrontal = QFrame(self.contObjFrontal)
        self.objetoPdFrontal.setObjectName(u"objetoPdFrontal")
        self.objetoPdFrontal.setEnabled(True)
        self.objetoPdFrontal.setStyleSheet(u"")
        self.objetoPdFrontal.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.objetoPdFrontal)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.objetoPdFrontal)


        self.verticalLayout_4.addWidget(self.contObjFrontal)


        self.gridLayout.addWidget(self.frParedFrontal, 0, 0, 1, 1)

        self.frParedTrasera = QFrame(self.boxSuperficies)
        self.frParedTrasera.setObjectName(u"frParedTrasera")
        self.frParedTrasera.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.frParedTrasera)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pdTrasera = QFrame(self.frParedTrasera)
        self.pdTrasera.setObjectName(u"pdTrasera")
        sizePolicy1.setHeightForWidth(self.pdTrasera.sizePolicy().hasHeightForWidth())
        self.pdTrasera.setSizePolicy(sizePolicy1)
        self.pdTrasera.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.pdTrasera)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_9 = QLabel(self.pdTrasera)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_9)

        self.cbParedTrasera = QComboBox(self.pdTrasera)
        self.cbParedTrasera.setObjectName(u"cbParedTrasera")
        self.cbParedTrasera.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_11.addWidget(self.cbParedTrasera)

        self.checkPdTrasera = QCheckBox(self.pdTrasera)
        self.checkPdTrasera.setObjectName(u"checkPdTrasera")
        self.checkPdTrasera.setMaximumSize(QSize(25, 25))
        self.checkPdTrasera.setCheckable(True)
        self.checkPdTrasera.setChecked(False)
        self.checkPdTrasera.setAutoRepeat(False)
        self.checkPdTrasera.setAutoExclusive(False)

        self.horizontalLayout_11.addWidget(self.checkPdTrasera)


        self.verticalLayout_9.addWidget(self.pdTrasera)

        self.contObjTrasera = QFrame(self.frParedTrasera)
        self.contObjTrasera.setObjectName(u"contObjTrasera")
        sizePolicy.setHeightForWidth(self.contObjTrasera.sizePolicy().hasHeightForWidth())
        self.contObjTrasera.setSizePolicy(sizePolicy)
        self.contObjTrasera.setFrameShape(QFrame.NoFrame)
        self.contObjTrasera.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.contObjTrasera)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.objetoPdTrasera = QFrame(self.contObjTrasera)
        self.objetoPdTrasera.setObjectName(u"objetoPdTrasera")
        self.objetoPdTrasera.setStyleSheet(u"")
        self.objetoPdTrasera.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_16 = QHBoxLayout(self.objetoPdTrasera)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(30, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.objetoPdTrasera)


        self.verticalLayout_9.addWidget(self.contObjTrasera)


        self.gridLayout.addWidget(self.frParedTrasera, 0, 1, 1, 1)

        self.frParedIzquierda = QFrame(self.boxSuperficies)
        self.frParedIzquierda.setObjectName(u"frParedIzquierda")
        self.frParedIzquierda.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_14 = QVBoxLayout(self.frParedIzquierda)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pdIzquierda = QFrame(self.frParedIzquierda)
        self.pdIzquierda.setObjectName(u"pdIzquierda")
        sizePolicy1.setHeightForWidth(self.pdIzquierda.sizePolicy().hasHeightForWidth())
        self.pdIzquierda.setSizePolicy(sizePolicy1)
        self.pdIzquierda.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.pdIzquierda)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_10 = QLabel(self.pdIzquierda)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.cbpdIzq = QComboBox(self.pdIzquierda)
        self.cbpdIzq.setObjectName(u"cbpdIzq")
        self.cbpdIzq.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_7.addWidget(self.cbpdIzq)

        self.checkPdIzq = QCheckBox(self.pdIzquierda)
        self.checkPdIzq.setObjectName(u"checkPdIzq")
        self.checkPdIzq.setMaximumSize(QSize(25, 25))
        self.checkPdIzq.setCheckable(True)
        self.checkPdIzq.setChecked(False)
        self.checkPdIzq.setAutoRepeat(False)
        self.checkPdIzq.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.checkPdIzq)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_14.addWidget(self.pdIzquierda)

        self.contObjIzq = QFrame(self.frParedIzquierda)
        self.contObjIzq.setObjectName(u"contObjIzq")
        self.contObjIzq.setFrameShape(QFrame.StyledPanel)
        self.contObjIzq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.contObjIzq)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.objetoPdIzq = QFrame(self.contObjIzq)
        self.objetoPdIzq.setObjectName(u"objetoPdIzq")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.objetoPdIzq.sizePolicy().hasHeightForWidth())
        self.objetoPdIzq.setSizePolicy(sizePolicy2)
        self.objetoPdIzq.setStyleSheet(u"")
        self.objetoPdIzq.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.objetoPdIzq)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(30, 0, 0, -1)

        self.verticalLayout_5.addWidget(self.objetoPdIzq)


        self.verticalLayout_14.addWidget(self.contObjIzq)


        self.gridLayout.addWidget(self.frParedIzquierda, 1, 0, 1, 1)

        self.frParedDerecha = QFrame(self.boxSuperficies)
        self.frParedDerecha.setObjectName(u"frParedDerecha")
        self.frParedDerecha.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.frParedDerecha)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pdDerecha_2 = QFrame(self.frParedDerecha)
        self.pdDerecha_2.setObjectName(u"pdDerecha_2")
        sizePolicy1.setHeightForWidth(self.pdDerecha_2.sizePolicy().hasHeightForWidth())
        self.pdDerecha_2.setSizePolicy(sizePolicy1)
        self.pdDerecha_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.pdDerecha_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.label_11 = QLabel(self.pdDerecha_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(100, 16777215))
        self.label_11.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.cbPdDerecha = QComboBox(self.pdDerecha_2)
        self.cbPdDerecha.setObjectName(u"cbPdDerecha")
        self.cbPdDerecha.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_8.addWidget(self.cbPdDerecha)

        self.checkPdDer = QCheckBox(self.pdDerecha_2)
        self.checkPdDer.setObjectName(u"checkPdDer")
        self.checkPdDer.setMaximumSize(QSize(25, 25))
        self.checkPdDer.setCheckable(True)
        self.checkPdDer.setChecked(False)
        self.checkPdDer.setAutoRepeat(False)
        self.checkPdDer.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.checkPdDer)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_8.addWidget(self.pdDerecha_2)

        self.contObjDer = QFrame(self.frParedDerecha)
        self.contObjDer.setObjectName(u"contObjDer")
        sizePolicy2.setHeightForWidth(self.contObjDer.sizePolicy().hasHeightForWidth())
        self.contObjDer.setSizePolicy(sizePolicy2)
        self.contObjDer.setFrameShape(QFrame.StyledPanel)
        self.contObjDer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.contObjDer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.objetoPdDer = QFrame(self.contObjDer)
        self.objetoPdDer.setObjectName(u"objetoPdDer")
        sizePolicy2.setHeightForWidth(self.objetoPdDer.sizePolicy().hasHeightForWidth())
        self.objetoPdDer.setSizePolicy(sizePolicy2)
        self.objetoPdDer.setStyleSheet(u"")
        self.objetoPdDer.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_17 = QHBoxLayout(self.objetoPdDer)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(30, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.objetoPdDer)


        self.verticalLayout_8.addWidget(self.contObjDer)


        self.gridLayout.addWidget(self.frParedDerecha, 1, 1, 1, 1)

        self.frPiso = QFrame(self.boxSuperficies)
        self.frPiso.setObjectName(u"frPiso")
        self.frPiso.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.frPiso)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.piso = QFrame(self.frPiso)
        self.piso.setObjectName(u"piso")
        sizePolicy1.setHeightForWidth(self.piso.sizePolicy().hasHeightForWidth())
        self.piso.setSizePolicy(sizePolicy1)
        self.piso.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.piso)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.label_12 = QLabel(self.piso)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.label_12)

        self.cbPiso = QComboBox(self.piso)
        self.cbPiso.setObjectName(u"cbPiso")
        self.cbPiso.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_9.addWidget(self.cbPiso)

        self.checkPiso = QCheckBox(self.piso)
        self.checkPiso.setObjectName(u"checkPiso")
        self.checkPiso.setMaximumSize(QSize(25, 25))
        self.checkPiso.setCheckable(True)
        self.checkPiso.setChecked(False)
        self.checkPiso.setAutoRepeat(False)
        self.checkPiso.setAutoExclusive(False)

        self.horizontalLayout_9.addWidget(self.checkPiso)


        self.verticalLayout_10.addWidget(self.piso)

        self.contObjPiso = QFrame(self.frPiso)
        self.contObjPiso.setObjectName(u"contObjPiso")
        self.contObjPiso.setFrameShape(QFrame.StyledPanel)
        self.contObjPiso.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.contObjPiso)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.objetoPiso = QFrame(self.contObjPiso)
        self.objetoPiso.setObjectName(u"objetoPiso")
        sizePolicy2.setHeightForWidth(self.objetoPiso.sizePolicy().hasHeightForWidth())
        self.objetoPiso.setSizePolicy(sizePolicy2)
        self.objetoPiso.setStyleSheet(u"")
        self.objetoPiso.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.objetoPiso)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, 0, 0, 0)

        self.verticalLayout_17.addWidget(self.objetoPiso)


        self.verticalLayout_10.addWidget(self.contObjPiso)


        self.gridLayout.addWidget(self.frPiso, 2, 0, 1, 1)

        self.frTecho = QFrame(self.boxSuperficies)
        self.frTecho.setObjectName(u"frTecho")
        self.frTecho.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frTecho)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.techo = QFrame(self.frTecho)
        self.techo.setObjectName(u"techo")
        sizePolicy1.setHeightForWidth(self.techo.sizePolicy().hasHeightForWidth())
        self.techo.setSizePolicy(sizePolicy1)
        self.techo.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.techo)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.label_13 = QLabel(self.techo)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.label_13)

        self.cbTecho = QComboBox(self.techo)
        self.cbTecho.setObjectName(u"cbTecho")
        self.cbTecho.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_10.addWidget(self.cbTecho)

        self.checkTecho = QCheckBox(self.techo)
        self.checkTecho.setObjectName(u"checkTecho")
        self.checkTecho.setMaximumSize(QSize(25, 25))
        self.checkTecho.setCheckable(True)
        self.checkTecho.setChecked(False)
        self.checkTecho.setAutoRepeat(False)
        self.checkTecho.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.checkTecho)


        self.verticalLayout_11.addWidget(self.techo)

        self.contObjTecho = QFrame(self.frTecho)
        self.contObjTecho.setObjectName(u"contObjTecho")
        sizePolicy2.setHeightForWidth(self.contObjTecho.sizePolicy().hasHeightForWidth())
        self.contObjTecho.setSizePolicy(sizePolicy2)
        self.contObjTecho.setFrameShape(QFrame.StyledPanel)
        self.contObjTecho.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.contObjTecho)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.objetoTecho = QFrame(self.contObjTecho)
        self.objetoTecho.setObjectName(u"objetoTecho")
        self.objetoTecho.setStyleSheet(u"")
        self.objetoTecho.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_18 = QHBoxLayout(self.objetoTecho)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(30, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.objetoTecho)


        self.verticalLayout_11.addWidget(self.contObjTecho)


        self.gridLayout.addWidget(self.frTecho, 2, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 1)

        self.horizontalLayout_2.addWidget(self.boxSuperficies)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.frMedium2)

        self.frBottom3 = QFrame(self.frame)
        self.frBottom3.setObjectName(u"frBottom3")
        self.frBottom3.setMinimumSize(QSize(0, 60))
        self.frBottom3.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border: 2px solid white;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"	font-size: 18px;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.4);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background: transparent;\n"
"	color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"\n"
"    border: 1px solid white;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 4px;\n"
"    background: rgba(255, 255, 255, 0.2); /* Fondo sutil */\n"
"}\n"
"\n"
"/* Hover para dar efecto visual */\n"
"QCheckBox::indicator:hover {\n"
"    background: rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"/* Aqu\u00ed NO se usa 'image', as\u00ed Qt usa el chulito predeterminado */\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(255, 255, 255, 0.8);\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"\n"
"")
        self.frBottom3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_19 = QHBoxLayout(self.frBottom3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.checkInteligibilidadOpcion = QCheckBox(self.frBottom3)
        self.checkInteligibilidadOpcion.setObjectName(u"checkInteligibilidadOpcion")

        self.horizontalLayout_19.addWidget(self.checkInteligibilidadOpcion)

        self.horizontalSpacer_3 = QSpacerItem(285, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)

        self.labelError = QLabel(self.frBottom3)
        self.labelError.setObjectName(u"labelError")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy3)
        self.labelError.setMinimumSize(QSize(400, 0))
        self.labelError.setStyleSheet(u"QLabel {\n"
"    color: white;  /* Letras en blanco */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.labelError.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.labelError)

        self.horizontalSpacer_4 = QSpacerItem(284, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.botonIniciarAnalisis = QPushButton(self.frBottom3)
        self.botonIniciarAnalisis.setObjectName(u"botonIniciarAnalisis")
        self.botonIniciarAnalisis.setMinimumSize(QSize(200, 0))
        self.botonIniciarAnalisis.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_19.addWidget(self.botonIniciarAnalisis)


        self.verticalLayout_3.addWidget(self.frBottom3)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.scrollArea, self.botonAtras)
        QWidget.setTabOrder(self.botonAtras, self.lineLargo)
        QWidget.setTabOrder(self.lineLargo, self.lineAncho)
        QWidget.setTabOrder(self.lineAncho, self.lineAlto)
        QWidget.setTabOrder(self.lineAlto, self.cbPdFrontal)
        QWidget.setTabOrder(self.cbPdFrontal, self.checkPdFrontal)
        QWidget.setTabOrder(self.checkPdFrontal, self.cbParedTrasera)
        QWidget.setTabOrder(self.cbParedTrasera, self.checkPdTrasera)
        QWidget.setTabOrder(self.checkPdTrasera, self.cbpdIzq)
        QWidget.setTabOrder(self.cbpdIzq, self.checkPdIzq)
        QWidget.setTabOrder(self.checkPdIzq, self.cbPdDerecha)
        QWidget.setTabOrder(self.cbPdDerecha, self.checkPdDer)
        QWidget.setTabOrder(self.checkPdDer, self.cbPiso)
        QWidget.setTabOrder(self.cbPiso, self.checkPiso)
        QWidget.setTabOrder(self.checkPiso, self.cbTecho)
        QWidget.setTabOrder(self.cbTecho, self.checkTecho)

        self.retranslateUi(FormTR)

        QMetaObject.connectSlotsByName(FormTR)
    # setupUi

    def retranslateUi(self, FormTR):
        FormTR.setWindowTitle(QCoreApplication.translate("FormTR", u"Form", None))
        self.botonAtras.setText("")
        self.label.setText(QCoreApplication.translate("FormTR", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">Tiempo De Reverberaci\u00f3n</span></p></body></html>", None))
        self.boxDimensiones.setTitle(QCoreApplication.translate("FormTR", u"Dimensiones", None))
        self.label_2.setText(QCoreApplication.translate("FormTR", u"Largo", None))
        self.label_3.setText(QCoreApplication.translate("FormTR", u"m", None))
        self.label_4.setText(QCoreApplication.translate("FormTR", u"Ancho", None))
        self.label_5.setText(QCoreApplication.translate("FormTR", u"m", None))
        self.label_6.setText(QCoreApplication.translate("FormTR", u"Alto", None))
        self.label_7.setText(QCoreApplication.translate("FormTR", u"m", None))
        self.labelErrorDimensiones.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("FormTR", u"Objetos Adicionales", None))
        self.checkObjAdicional.setText(QCoreApplication.translate("FormTR", u"Hay objetos dentro del aula de clases", None))
        self.gbInteligibilad.setTitle(QCoreApplication.translate("FormTR", u"Inteligibilidad del Habla", None))
        self.label_15.setText(QCoreApplication.translate("FormTR", u"\u00bfCu\u00e1l es la distancia entre el emisor y el receptor?", None))
        self.label_14.setText(QCoreApplication.translate("FormTR", u"Ingresa el coeficiente medio de absorcion del aula", None))
        self.label_16.setText("")
        self.boxSuperficies.setTitle(QCoreApplication.translate("FormTR", u"Superficies", None))
        self.label_8.setText(QCoreApplication.translate("FormTR", u"Pared Frontal", None))
#if QT_CONFIG(tooltip)
        self.checkPdFrontal.setToolTip(QCoreApplication.translate("FormTR", u"Activa si hay objetos en esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdFrontal.setText("")
        self.label_9.setText(QCoreApplication.translate("FormTR", u"Pared Trasera", None))
#if QT_CONFIG(tooltip)
        self.checkPdTrasera.setToolTip(QCoreApplication.translate("FormTR", u"Activa si hay objetos en esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdTrasera.setText("")
        self.label_10.setText(QCoreApplication.translate("FormTR", u"Pared Lateral Izquierda", None))
#if QT_CONFIG(tooltip)
        self.checkPdIzq.setToolTip(QCoreApplication.translate("FormTR", u"Activa si hay objetos en esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdIzq.setText("")
        self.label_11.setText(QCoreApplication.translate("FormTR", u"Pared Lateral Derecha", None))
#if QT_CONFIG(tooltip)
        self.checkPdDer.setToolTip(QCoreApplication.translate("FormTR", u"Activa si hay objetos en esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdDer.setText("")
        self.label_12.setText(QCoreApplication.translate("FormTR", u"Piso", None))
#if QT_CONFIG(tooltip)
        self.checkPiso.setToolTip(QCoreApplication.translate("FormTR", u"Activa si hay objetos en esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.checkPiso.setText("")
        self.label_13.setText(QCoreApplication.translate("FormTR", u"Techo", None))
#if QT_CONFIG(tooltip)
        self.checkTecho.setToolTip(QCoreApplication.translate("FormTR", u"Activa si hay objetos en esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.checkTecho.setText("")
        self.checkInteligibilidadOpcion.setText(QCoreApplication.translate("FormTR", u"Habilitar Inteligibilidad del Habla", None))
        self.labelError.setText("")
        self.botonIniciarAnalisis.setText(QCoreApplication.translate("FormTR", u"Iniciar An\u00e1lisis", None))
    # retranslateUi

