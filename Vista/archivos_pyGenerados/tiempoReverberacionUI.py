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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FormTR(object):
    def setupUi(self, FormTR):
        if not FormTR.objectName():
            FormTR.setObjectName(u"FormTR")
        FormTR.resize(1036, 619)
        FormTR.setStyleSheet(u"/* \u2500\u2500 Fondo general \u2500\u2500 */\n"
"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0.488, y1:0, x2:0.495, y2:1,\n"
"        stop:0.306818 rgba(0,0,93,255),\n"
"        stop:0.710227 rgba(0,0,45,255)\n"
"    );\n"
"}\n"
"QFrame { background-color: transparent; border: none; }\n"
"\n"
"/* \u2500\u2500 Scrollbars globales \u2500\u2500 */\n"
"QScrollBar:vertical {\n"
"    background: transparent; width: 7px; margin: 2px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgba(255,255,255,0.22); min-height: 24px; border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:vertical:hover { background-color: rgba(255,255,255,0.42); }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; background: none; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }\n"
"\n"
"/* \u2500\u2500 QGroupBox global (t\u00edtulos de secci\u00f3n) \u2500\u2500 */\n"
"QGroupBox {\n"
"    border: 1px solid rgba(255,255,255,0.22"
                        ");\n"
"    border-radius: 10px;\n"
"    margin-top: 14px;\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    color: rgba(255,255,255,0.80);\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 6px;\n"
"    color: rgba(255,255,255,0.85);\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"/* \u2500\u2500 Labels globales \u2500\u2500 */\n"
"QLabel {\n"
"    color: rgba(255,255,255,0.88);\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u2500\u2500 Inputs globales \u2500\u2500 */\n"
"QLineEdit {\n"
"    border: 1px solid rgba(255,255,255,0.35);\n"
"    border-radius: 8px;\n"
"    background-color: rgba(255,255,255,0.12);\n"
"    color: white;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 5px 8px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7ec8f7;\n"
"    background-colo"
                        "r: rgba(126,200,247,0.15);\n"
"}\n"
"QLineEdit::placeholder { color: rgba(255,255,255,0.35); }\n"
"\n"
"/* \u2500\u2500 ComboBox global \u2500\u2500 */\n"
"QComboBox {\n"
"    background: rgba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.35);\n"
"    border-radius: 7px;\n"
"    color: white;\n"
"    font-size: 11px;\n"
"    padding: 4px 6px;\n"
"}\n"
"QComboBox:focus { border: 1px solid #7ec8f7; }\n"
"QComboBox::drop-down { border: none; width: 20px; }\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #001a4d;\n"
"    color: white;\n"
"    selection-background-color: rgba(126,200,247,0.28);\n"
"    border: 1px solid rgba(255,255,255,0.22);\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox QScrollBar:vertical { border: none; background: #f0f0f0; width: 8px; }\n"
"QComboBox QScrollBar::handle:vertical { background: #bfbfbf; min-height: 16px; border-radius: 3px; }\n"
"QComboBox QScrollBar::add-line:vertical, QComboBox QScrollBar::sub-line:vertical { height: 0; }\n"
"\n"
"/* \u2500\u2500"
                        " CheckBox global \u2500\u2500 */\n"
"\n"
"QCheckBox {\n"
"    background: transparent;\n"
"    color: rgba(255,255,255,0.85);\n"
"    font-size: 11px;\n"
"   \n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:hover { background: rgba(255,255,255,0.30); }\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(126,200,247,0.55);\n"
"    border: 1px solid #7ec8f7;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 17px; height: 17px;\n"
"    border-radius: 4px;\n"
"    background: rgba(255,255,255,0.15);\n"
"    border: 1px solid rgba(255,255,255,0.45);\n"
"}\n"
"\n"
"/* \u2500\u2500 DoubleSpinBox / SpinBox \u2500\u2500 */\n"
"QDoubleSpinBox, QSpinBox {\n"
"    background: rgba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.35);\n"
"    border-radius: 6px;\n"
"    padding: 4px 6px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"}\n"
"QDoubleSpinBox:focus, QSpinBox:focus { border: 1px solid #7ec8f7; }\n"
"\n"
"\n"
"\n"
"/* \u2500\u2500 Widgets deshabilitados \u2500\u2500 */"
                        "\n"
"QLabel:disabled, QLineEdit:disabled, QComboBox:disabled,\n"
"QSpinBox:disabled, QDoubleSpinBox:disabled, QCheckBox:disabled {\n"
"    color: rgba(255,255,255,0.35);\n"
"}\n"
"QGroupBox:disabled {\n"
"    background-color: rgba(80,80,80,0.18);\n"
"    border-color: rgba(255,255,255,0.12);\n"
"}\n"
"QGroupBox::title:disabled { color: rgba(255,255,255,0.28); }\n"
"")
        self.verticalLayout_6 = QVBoxLayout(FormTR)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(FormTR)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea { border: none; background: transparent; }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1036, 619))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frTop1 = QFrame(self.frame)
        self.frTop1.setObjectName(u"frTop1")
        self.frTop1.setMinimumSize(QSize(45, 80))
        self.frTop1.setMaximumSize(QSize(16777215, 100))
        self.frTop1.setStyleSheet(u"QFrame#frTop1 {\n"
"    background-color: rgba(0,0,0,0.25);\n"
"    border-bottom: 1px solid rgba(255,255,255,0.13);\n"
"}")
        self.frTop1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frTop1)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, 20, -1)
        self.botonAtras = QPushButton(self.frTop1)
        self.botonAtras.setObjectName(u"botonAtras")
        self.botonAtras.setMinimumSize(QSize(42, 42))
        self.botonAtras.setMaximumSize(QSize(42, 42))
        self.botonAtras.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(255,255,255,0.35);\n"
"    border-radius: 21px;\n"
"}\n"
"QPushButton:hover { background-color: rgba(255,255,255,0.18); border: 1px solid white; }\n"
"QPushButton:pressed { background-color: rgba(255,255,255,0.38); }")
        icon = QIcon()
        icon.addFile(u"graficas/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.botonAtras)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frameTituloTop = QFrame(self.frTop1)
        self.frameTituloTop.setObjectName(u"frameTituloTop")
        self.frameTituloTop.setFrameShape(QFrame.NoFrame)
        self.vloTituloTop = QVBoxLayout(self.frameTituloTop)
        self.vloTituloTop.setSpacing(2)
        self.vloTituloTop.setObjectName(u"vloTituloTop")
        self.vloTituloTop.setContentsMargins(0, 8, 0, 8)
        self.label = QLabel(self.frameTituloTop)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.vloTituloTop.addWidget(self.label)

        self.labelSubtituloTop = QLabel(self.frameTituloTop)
        self.labelSubtituloTop.setObjectName(u"labelSubtituloTop")
        self.labelSubtituloTop.setAlignment(Qt.AlignCenter)

        self.vloTituloTop.addWidget(self.labelSubtituloTop)


        self.horizontalLayout.addWidget(self.frameTituloTop)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frTop1)

        self.frMedium2 = QFrame(self.frame)
        self.frMedium2.setObjectName(u"frMedium2")
        self.frMedium2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frMedium2)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.frame_5 = QFrame(self.frMedium2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.boxDimensiones = QGroupBox(self.frame_5)
        self.boxDimensiones.setObjectName(u"boxDimensiones")
        self.boxDimensiones.setMaximumSize(QSize(16777215, 16777210))
        self.boxDimensiones.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.boxDimensiones)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(14, 16, 14, 10)
        self.frame_2 = QFrame(self.boxDimensiones)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(46, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineLargo = QLineEdit(self.frame_2)
        self.lineLargo.setObjectName(u"lineLargo")

        self.horizontalLayout_3.addWidget(self.lineLargo)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(16, 0))
        self.label_3.setStyleSheet(u"color: rgba(255,255,255,0.50); font-size:10px; font-weight:normal;")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.boxDimensiones)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(46, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineAncho = QLineEdit(self.frame_3)
        self.lineAncho.setObjectName(u"lineAncho")

        self.horizontalLayout_4.addWidget(self.lineAncho)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(16, 0))
        self.label_5.setStyleSheet(u"color: rgba(255,255,255,0.50); font-size:10px; font-weight:normal;")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.boxDimensiones)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(46, 0))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineAlto = QLineEdit(self.frame_4)
        self.lineAlto.setObjectName(u"lineAlto")

        self.horizontalLayout_5.addWidget(self.lineAlto)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(16, 0))
        self.label_7.setStyleSheet(u"color: rgba(255,255,255,0.50); font-size:10px; font-weight:normal;")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.labelErrorDimensiones = QLabel(self.boxDimensiones)
        self.labelErrorDimensiones.setObjectName(u"labelErrorDimensiones")
        self.labelErrorDimensiones.setStyleSheet(u"color: rgba(248,113,113,0.90); font-size:10px; font-weight:normal;")
        self.labelErrorDimensiones.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.labelErrorDimensiones)


        self.verticalLayout_7.addWidget(self.boxDimensiones)

        self.sepDimObjAdic = QFrame(self.frame_5)
        self.sepDimObjAdic.setObjectName(u"sepDimObjAdic")
        self.sepDimObjAdic.setStyleSheet(u"QFrame { background-color: rgba(255,255,255,0.10); max-height: 1px; border: none; }")
        self.sepDimObjAdic.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.sepDimObjAdic)

        self.groupBox_3 = QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setSpacing(8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 14, 10, 10)
        self.checkObjAdicional = QCheckBox(self.groupBox_3)
        self.checkObjAdicional.setObjectName(u"checkObjAdicional")

        self.verticalLayout_20.addWidget(self.checkObjAdicional)

        self.contObjAdicional = QFrame(self.groupBox_3)
        self.contObjAdicional.setObjectName(u"contObjAdicional")
        self.contObjAdicional.setEnabled(False)
        self.contObjAdicional.setStyleSheet(u"QFrame#contObjAdicional {\n"
"    background-color: rgba(251,146,60,0.06);\n"
"    border: 1px solid rgba(251,146,60,0.22);\n"
"    border-radius: 8px;\n"
"}\n"
"QFrame#contObjAdicional:disabled { border-color: rgba(255,255,255,0.10); background: transparent; }\n"
"")
        self.contObjAdicional.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_19 = QVBoxLayout(self.contObjAdicional)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(6, 6, 6, 6)
        self.objAdic = QFrame(self.contObjAdicional)
        self.objAdic.setObjectName(u"objAdic")
        self.objAdic.setEnabled(False)
        self.objAdic.setFrameShape(QFrame.NoFrame)
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
        self.verticalLayout_12 = QVBoxLayout(self.gbInteligibilad)
        self.verticalLayout_12.setSpacing(8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(12, 14, 12, 10)
        self.frame_8 = QFrame(self.gbInteligibilad)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_22.setSpacing(8)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_15)

        self.distanciaRyE = QDoubleSpinBox(self.frame_8)
        self.distanciaRyE.setObjectName(u"distanciaRyE")
        self.distanciaRyE.setMinimumSize(QSize(80, 0))
        self.distanciaRyE.setMaximumSize(QSize(90, 16777215))
        self.distanciaRyE.setDecimals(2)
        self.distanciaRyE.setMaximum(30.000000000000000)
        self.distanciaRyE.setSingleStep(0.500000000000000)

        self.horizontalLayout_22.addWidget(self.distanciaRyE)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_12.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.gbInteligibilad)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_23.setSpacing(8)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_14)

        self.coeficienteMedio = QDoubleSpinBox(self.frame_11)
        self.coeficienteMedio.setObjectName(u"coeficienteMedio")
        self.coeficienteMedio.setMinimumSize(QSize(80, 0))
        self.coeficienteMedio.setMaximumSize(QSize(90, 16777215))
        self.coeficienteMedio.setDecimals(3)
        self.coeficienteMedio.setMaximum(1.000000000000000)
        self.coeficienteMedio.setSingleStep(0.010000000000000)

        self.horizontalLayout_23.addWidget(self.coeficienteMedio)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.label_16 = QLabel(self.gbInteligibilad)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgba(248,113,113,0.90); font-size:10px; font-weight:normal;")
        self.label_16.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_16)


        self.verticalLayout_7.addWidget(self.gbInteligibilad)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.boxSuperficies = QGroupBox(self.frMedium2)
        self.boxSuperficies.setObjectName(u"boxSuperficies")
        self.boxSuperficies.setStyleSheet(u"QGroupBox#boxSuperficies {\n"
"    border: 1px solid rgba(255,255,255,0.20);\n"
"    border-radius: 12px;\n"
"    background-color: rgba(255,255,255,0.04);\n"
"    margin-top: 14px;\n"
"}\n"
"QGroupBox#boxSuperficies::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 14px;\n"
"    padding: 0 6px;\n"
"    color: rgba(255,255,255,0.80);\n"
"    font-size: 11px;\n"
"}\n"
"/* Card de cada superficie */\n"
"QFrame[class=\"cardSuperficie\"] {\n"
"    border-radius: 9px;\n"
"    background-color: rgba(255,255,255,0.07);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.boxSuperficies)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 18, 10, 10)
        self.frParedFrontal = QFrame(self.boxSuperficies)
        self.frParedFrontal.setObjectName(u"frParedFrontal")
        self.frParedFrontal.setStyleSheet(u"QFrame#frParedFrontal {\n"
"    background-color: rgba(126,200,247,0.07);\n"
"    border: 1px solid rgba(126,200,247,0.30);\n"
"    border-left: 2px solid rgba(126,200,247,0.75);\n"
"    border-radius: 8px;\n"
"}")
        self.frParedFrontal.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frParedFrontal)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 6, 8, 6)
        self.pdFrontal = QFrame(self.frParedFrontal)
        self.pdFrontal.setObjectName(u"pdFrontal")
        self.pdFrontal.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.pdFrontal)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.pdFrontal)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(66, 0))
        self.label_8.setMaximumSize(QSize(80, 16777215))
        self.label_8.setStyleSheet(u"color: rgba(126,200,247,0.90); font-size:11px;")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.cbPdFrontal = QComboBox(self.pdFrontal)
        self.cbPdFrontal.setObjectName(u"cbPdFrontal")
        self.cbPdFrontal.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_6.addWidget(self.cbPdFrontal)

        self.checkPdFrontal = QCheckBox(self.pdFrontal)
        self.checkPdFrontal.setObjectName(u"checkPdFrontal")
        self.checkPdFrontal.setMaximumSize(QSize(22, 22))
        self.checkPdFrontal.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.checkPdFrontal)


        self.verticalLayout_4.addWidget(self.pdFrontal)

        self.contObjFrontal = QFrame(self.frParedFrontal)
        self.contObjFrontal.setObjectName(u"contObjFrontal")
        self.contObjFrontal.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.contObjFrontal)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.objetoPdFrontal = QFrame(self.contObjFrontal)
        self.objetoPdFrontal.setObjectName(u"objetoPdFrontal")
        self.objetoPdFrontal.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.objetoPdFrontal)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.objetoPdFrontal)


        self.verticalLayout_4.addWidget(self.contObjFrontal)


        self.gridLayout.addWidget(self.frParedFrontal, 0, 0, 1, 1)

        self.frParedTrasera = QFrame(self.boxSuperficies)
        self.frParedTrasera.setObjectName(u"frParedTrasera")
        self.frParedTrasera.setStyleSheet(u"QFrame#frParedTrasera {\n"
"    background-color: rgba(167,139,250,0.07);\n"
"    border: 1px solid rgba(167,139,250,0.28);\n"
"    border-left: 2px solid rgba(167,139,250,0.70);\n"
"    border-radius: 8px;\n"
"}")
        self.frParedTrasera.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.frParedTrasera)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(8, 6, 8, 6)
        self.pdTrasera = QFrame(self.frParedTrasera)
        self.pdTrasera.setObjectName(u"pdTrasera")
        self.pdTrasera.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.pdTrasera)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.pdTrasera)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(66, 0))
        self.label_9.setMaximumSize(QSize(80, 16777215))
        self.label_9.setStyleSheet(u"color: rgba(167,139,250,0.90); font-size:11px;")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.cbParedTrasera = QComboBox(self.pdTrasera)
        self.cbParedTrasera.setObjectName(u"cbParedTrasera")
        self.cbParedTrasera.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_11.addWidget(self.cbParedTrasera)

        self.checkPdTrasera = QCheckBox(self.pdTrasera)
        self.checkPdTrasera.setObjectName(u"checkPdTrasera")
        self.checkPdTrasera.setMaximumSize(QSize(22, 22))
        self.checkPdTrasera.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.checkPdTrasera)


        self.verticalLayout_9.addWidget(self.pdTrasera)

        self.contObjTrasera = QFrame(self.frParedTrasera)
        self.contObjTrasera.setObjectName(u"contObjTrasera")
        self.contObjTrasera.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.contObjTrasera)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.objetoPdTrasera = QFrame(self.contObjTrasera)
        self.objetoPdTrasera.setObjectName(u"objetoPdTrasera")
        self.objetoPdTrasera.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_16 = QHBoxLayout(self.objetoPdTrasera)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.objetoPdTrasera)


        self.verticalLayout_9.addWidget(self.contObjTrasera)


        self.gridLayout.addWidget(self.frParedTrasera, 0, 1, 1, 1)

        self.frParedIzquierda = QFrame(self.boxSuperficies)
        self.frParedIzquierda.setObjectName(u"frParedIzquierda")
        self.frParedIzquierda.setStyleSheet(u"QFrame#frParedIzquierda {\n"
"    background-color: rgba(52,211,153,0.07);\n"
"    border: 1px solid rgba(52,211,153,0.28);\n"
"    border-left: 2px solid rgba(52,211,153,0.70);\n"
"    border-radius: 8px;\n"
"}")
        self.frParedIzquierda.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_14 = QVBoxLayout(self.frParedIzquierda)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(8, 6, 8, 6)
        self.pdIzquierda = QFrame(self.frParedIzquierda)
        self.pdIzquierda.setObjectName(u"pdIzquierda")
        self.pdIzquierda.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.pdIzquierda)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.pdIzquierda)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(66, 0))
        self.label_10.setMaximumSize(QSize(80, 16777215))
        self.label_10.setStyleSheet(u"color: rgba(52,211,153,0.90); font-size:11px;")
        self.label_10.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.cbpdIzq = QComboBox(self.pdIzquierda)
        self.cbpdIzq.setObjectName(u"cbpdIzq")
        self.cbpdIzq.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_7.addWidget(self.cbpdIzq)

        self.checkPdIzq = QCheckBox(self.pdIzquierda)
        self.checkPdIzq.setObjectName(u"checkPdIzq")
        self.checkPdIzq.setMaximumSize(QSize(22, 22))
        self.checkPdIzq.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.checkPdIzq)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_14.addWidget(self.pdIzquierda)

        self.contObjIzq = QFrame(self.frParedIzquierda)
        self.contObjIzq.setObjectName(u"contObjIzq")
        self.contObjIzq.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.contObjIzq)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.objetoPdIzq = QFrame(self.contObjIzq)
        self.objetoPdIzq.setObjectName(u"objetoPdIzq")
        self.objetoPdIzq.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.objetoPdIzq)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.objetoPdIzq)


        self.verticalLayout_14.addWidget(self.contObjIzq)


        self.gridLayout.addWidget(self.frParedIzquierda, 1, 0, 1, 1)

        self.frParedDerecha = QFrame(self.boxSuperficies)
        self.frParedDerecha.setObjectName(u"frParedDerecha")
        self.frParedDerecha.setStyleSheet(u"QFrame#frParedDerecha {\n"
"    background-color: rgba(251,191,36,0.07);\n"
"    border: 1px solid rgba(251,191,36,0.28);\n"
"    border-left: 2px solid rgba(251,191,36,0.70);\n"
"    border-radius: 8px;\n"
"}")
        self.frParedDerecha.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.frParedDerecha)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 6, 8, 6)
        self.pdDerecha_2 = QFrame(self.frParedDerecha)
        self.pdDerecha_2.setObjectName(u"pdDerecha_2")
        self.pdDerecha_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.pdDerecha_2)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.pdDerecha_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(66, 0))
        self.label_11.setMaximumSize(QSize(80, 16777215))
        self.label_11.setStyleSheet(u"color: rgba(251,191,36,0.90); font-size:11px;")
        self.label_11.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.cbPdDerecha = QComboBox(self.pdDerecha_2)
        self.cbPdDerecha.setObjectName(u"cbPdDerecha")
        self.cbPdDerecha.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_8.addWidget(self.cbPdDerecha)

        self.checkPdDer = QCheckBox(self.pdDerecha_2)
        self.checkPdDer.setObjectName(u"checkPdDer")
        self.checkPdDer.setMaximumSize(QSize(22, 22))
        self.checkPdDer.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.checkPdDer)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_8.addWidget(self.pdDerecha_2)

        self.contObjDer = QFrame(self.frParedDerecha)
        self.contObjDer.setObjectName(u"contObjDer")
        self.contObjDer.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_16 = QVBoxLayout(self.contObjDer)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.objetoPdDer = QFrame(self.contObjDer)
        self.objetoPdDer.setObjectName(u"objetoPdDer")
        self.objetoPdDer.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_17 = QHBoxLayout(self.objetoPdDer)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.objetoPdDer)


        self.verticalLayout_8.addWidget(self.contObjDer)


        self.gridLayout.addWidget(self.frParedDerecha, 1, 1, 1, 1)

        self.frPiso = QFrame(self.boxSuperficies)
        self.frPiso.setObjectName(u"frPiso")
        self.frPiso.setStyleSheet(u"QFrame#frPiso {\n"
"    background-color: rgba(251,146,60,0.07);\n"
"    border: 1px solid rgba(251,146,60,0.28);\n"
"    border-left: 2px solid rgba(251,146,60,0.70);\n"
"    border-radius: 8px;\n"
"}")
        self.frPiso.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.frPiso)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(8, 6, 8, 6)
        self.piso = QFrame(self.frPiso)
        self.piso.setObjectName(u"piso")
        self.piso.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.piso)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.piso)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(66, 0))
        self.label_12.setMaximumSize(QSize(80, 16777215))
        self.label_12.setStyleSheet(u"color: rgba(251,146,60,0.90); font-size:11px;")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.cbPiso = QComboBox(self.piso)
        self.cbPiso.setObjectName(u"cbPiso")
        self.cbPiso.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_9.addWidget(self.cbPiso)

        self.checkPiso = QCheckBox(self.piso)
        self.checkPiso.setObjectName(u"checkPiso")
        self.checkPiso.setMaximumSize(QSize(22, 22))
        self.checkPiso.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.checkPiso)


        self.verticalLayout_10.addWidget(self.piso)

        self.contObjPiso = QFrame(self.frPiso)
        self.contObjPiso.setObjectName(u"contObjPiso")
        self.contObjPiso.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.contObjPiso)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.objetoPiso = QFrame(self.contObjPiso)
        self.objetoPiso.setObjectName(u"objetoPiso")
        self.objetoPiso.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.objetoPiso)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_17.addWidget(self.objetoPiso)


        self.verticalLayout_10.addWidget(self.contObjPiso)


        self.gridLayout.addWidget(self.frPiso, 2, 0, 1, 1)

        self.frTecho = QFrame(self.boxSuperficies)
        self.frTecho.setObjectName(u"frTecho")
        self.frTecho.setStyleSheet(u"QFrame#frTecho {\n"
"    background-color: rgba(248,113,113,0.07);\n"
"    border: 1px solid rgba(248,113,113,0.28);\n"
"    border-left: 2px solid rgba(248,113,113,0.70);\n"
"    border-radius: 8px;\n"
"}")
        self.frTecho.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frTecho)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(8, 6, 8, 6)
        self.techo = QFrame(self.frTecho)
        self.techo.setObjectName(u"techo")
        self.techo.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.techo)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.techo)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(66, 0))
        self.label_13.setMaximumSize(QSize(80, 16777215))
        self.label_13.setStyleSheet(u"color: rgba(248,113,113,0.90); font-size:11px;")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.cbTecho = QComboBox(self.techo)
        self.cbTecho.setObjectName(u"cbTecho")
        self.cbTecho.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_10.addWidget(self.cbTecho)

        self.checkTecho = QCheckBox(self.techo)
        self.checkTecho.setObjectName(u"checkTecho")
        self.checkTecho.setMaximumSize(QSize(22, 22))
        self.checkTecho.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.checkTecho)


        self.verticalLayout_11.addWidget(self.techo)

        self.contObjTecho = QFrame(self.frTecho)
        self.contObjTecho.setObjectName(u"contObjTecho")
        self.contObjTecho.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_18 = QVBoxLayout(self.contObjTecho)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.objetoTecho = QFrame(self.contObjTecho)
        self.objetoTecho.setObjectName(u"objetoTecho")
        self.objetoTecho.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_18 = QHBoxLayout(self.objetoTecho)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.objetoTecho)


        self.verticalLayout_11.addWidget(self.contObjTecho)


        self.gridLayout.addWidget(self.frTecho, 2, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.boxSuperficies)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.frMedium2)

        self.frBottom3 = QFrame(self.frame)
        self.frBottom3.setObjectName(u"frBottom3")
        self.frBottom3.setMinimumSize(QSize(0, 58))
        self.frBottom3.setMaximumSize(QSize(16777215, 58))
        self.frBottom3.setStyleSheet(u"QFrame#frBottom3 {\n"
"    background-color: rgba(0,0,0,0.22);\n"
"    border-top: 1px solid rgba(255,255,255,0.12);\n"
"}\n"
"QPushButton#botonIniciarAnalisis {\n"
"    background-color: rgba(126,200,247,0.18);\n"
"    border: 1.5px solid #7ec8f7;\n"
"    color: #7ec8f7;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    border-radius: 12px;\n"
"    padding: 8px 20px;\n"
"    min-width: 180px;\n"
"    max-width: 210px;\n"
"}\n"
"QPushButton#botonIniciarAnalisis:hover {\n"
"    background-color: rgba(126,200,247,0.35);\n"
"    color: white;\n"
"    border-color: white;\n"
"}\n"
"QPushButton#botonIniciarAnalisis:pressed {\n"
"    background-color: rgba(126,200,247,0.55);\n"
"    color: white;\n"
"}\n"
"QCheckBox#checkInteligibilidadOpcion {\n"
"    color: rgba(255,255,255,0.80);\n"
"    font-size: 11px;\n"
"    spacing: 6px;\n"
"}\n"
"")
        self.frBottom3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_19 = QHBoxLayout(self.frBottom3)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(16, -1, 16, -1)
        self.checkInteligibilidadOpcion = QCheckBox(self.frBottom3)
        self.checkInteligibilidadOpcion.setObjectName(u"checkInteligibilidadOpcion")

        self.horizontalLayout_19.addWidget(self.checkInteligibilidadOpcion)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)

        self.labelError = QLabel(self.frBottom3)
        self.labelError.setObjectName(u"labelError")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy)
        self.labelError.setStyleSheet(u"color: rgba(248,113,113,0.90); font-size:11px; font-weight:bold;")
        self.labelError.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.labelError)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.botonIniciarAnalisis = QPushButton(self.frBottom3)
        self.botonIniciarAnalisis.setObjectName(u"botonIniciarAnalisis")

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
#if QT_CONFIG(tooltip)
        self.botonAtras.setToolTip(QCoreApplication.translate("FormTR", u"Regresar a la pantalla anterior", None))
#endif // QT_CONFIG(tooltip)
        self.botonAtras.setText("")
        self.label.setText(QCoreApplication.translate("FormTR", u"<html><body><p><span style=\"font-size:18pt; font-weight:700; color:#ffffff;\">Tiempo de Reverberacion</span></p></body></html>", None))
        self.labelSubtituloTop.setText(QCoreApplication.translate("FormTR", u"<html><body><p><span style=\"font-size:9pt; color:rgba(255,255,255,0.55);\">Ingresa dimensiones, materiales y objetos para calcular el RT60 (Sabine y Eyring)</span></p></body></html>", None))
        self.boxDimensiones.setTitle(QCoreApplication.translate("FormTR", u"Dimensiones del aula", None))
        self.label_2.setText(QCoreApplication.translate("FormTR", u"Largo", None))
#if QT_CONFIG(tooltip)
        self.lineLargo.setToolTip(QCoreApplication.translate("FormTR", u"Largo del salon en metros", None))
#endif // QT_CONFIG(tooltip)
        self.lineLargo.setPlaceholderText(QCoreApplication.translate("FormTR", u"ej: 9.5", None))
        self.label_3.setText(QCoreApplication.translate("FormTR", u"m", None))
        self.label_4.setText(QCoreApplication.translate("FormTR", u"Ancho", None))
#if QT_CONFIG(tooltip)
        self.lineAncho.setToolTip(QCoreApplication.translate("FormTR", u"Ancho del salon en metros", None))
#endif // QT_CONFIG(tooltip)
        self.lineAncho.setPlaceholderText(QCoreApplication.translate("FormTR", u"ej: 6.0", None))
        self.label_5.setText(QCoreApplication.translate("FormTR", u"m", None))
        self.label_6.setText(QCoreApplication.translate("FormTR", u"Alto", None))
#if QT_CONFIG(tooltip)
        self.lineAlto.setToolTip(QCoreApplication.translate("FormTR", u"Altura del salon en metros", None))
#endif // QT_CONFIG(tooltip)
        self.lineAlto.setPlaceholderText(QCoreApplication.translate("FormTR", u"ej: 3.5", None))
        self.label_7.setText(QCoreApplication.translate("FormTR", u"m", None))
        self.labelErrorDimensiones.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("FormTR", u"Objetos adicionales en el aula", None))
#if QT_CONFIG(tooltip)
        self.checkObjAdicional.setToolTip(QCoreApplication.translate("FormTR", u"Activa para agregar sillas, escritorios u otros objetos que afectan la absorcion", None))
#endif // QT_CONFIG(tooltip)
        self.checkObjAdicional.setText(QCoreApplication.translate("FormTR", u"Hay objetos dentro del aula de clases", None))
        self.gbInteligibilad.setTitle(QCoreApplication.translate("FormTR", u"Inteligibilidad del Habla (%ALCons)", None))
        self.label_15.setText(QCoreApplication.translate("FormTR", u"Distancia emisor \u2013 receptor", None))
#if QT_CONFIG(tooltip)
        self.distanciaRyE.setToolTip(QCoreApplication.translate("FormTR", u"Distancia entre el docente y el oyente mas lejano (en metros)", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("FormTR", u"Coeficiente medio de absorcion", None))
#if QT_CONFIG(tooltip)
        self.coeficienteMedio.setToolTip(QCoreApplication.translate("FormTR", u"Coeficiente de absorcion promedio de todas las superficies (entre 0.01 y 1.00)", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText("")
        self.boxSuperficies.setTitle(QCoreApplication.translate("FormTR", u"Superficies del aula", None))
        self.label_8.setText(QCoreApplication.translate("FormTR", u"Frontal", None))
#if QT_CONFIG(tooltip)
        self.cbPdFrontal.setToolTip(QCoreApplication.translate("FormTR", u"Material de la pared frontal", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkPdFrontal.setToolTip(QCoreApplication.translate("FormTR", u"Activar para agregar objetos adheridos (ventanas, puertas, tableros...)", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdFrontal.setText("")
        self.label_9.setText(QCoreApplication.translate("FormTR", u"Trasera", None))
#if QT_CONFIG(tooltip)
        self.cbParedTrasera.setToolTip(QCoreApplication.translate("FormTR", u"Material de la pared trasera", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkPdTrasera.setToolTip(QCoreApplication.translate("FormTR", u"Activar para agregar objetos adheridos", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdTrasera.setText("")
        self.label_10.setText(QCoreApplication.translate("FormTR", u"Izquierda", None))
#if QT_CONFIG(tooltip)
        self.cbpdIzq.setToolTip(QCoreApplication.translate("FormTR", u"Material de la pared lateral izquierda", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkPdIzq.setToolTip(QCoreApplication.translate("FormTR", u"Activar para agregar objetos adheridos", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdIzq.setText("")
        self.label_11.setText(QCoreApplication.translate("FormTR", u"Derecha", None))
#if QT_CONFIG(tooltip)
        self.cbPdDerecha.setToolTip(QCoreApplication.translate("FormTR", u"Material de la pared lateral derecha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkPdDer.setToolTip(QCoreApplication.translate("FormTR", u"Activar para agregar objetos adheridos", None))
#endif // QT_CONFIG(tooltip)
        self.checkPdDer.setText("")
        self.label_12.setText(QCoreApplication.translate("FormTR", u"Piso", None))
#if QT_CONFIG(tooltip)
        self.cbPiso.setToolTip(QCoreApplication.translate("FormTR", u"Material del piso", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkPiso.setToolTip(QCoreApplication.translate("FormTR", u"Activar para agregar objetos adheridos al piso", None))
#endif // QT_CONFIG(tooltip)
        self.checkPiso.setText("")
        self.label_13.setText(QCoreApplication.translate("FormTR", u"Techo", None))
#if QT_CONFIG(tooltip)
        self.cbTecho.setToolTip(QCoreApplication.translate("FormTR", u"Material del techo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkTecho.setToolTip(QCoreApplication.translate("FormTR", u"Activar para agregar objetos adheridos al techo", None))
#endif // QT_CONFIG(tooltip)
        self.checkTecho.setText("")
#if QT_CONFIG(tooltip)
        self.checkInteligibilidadOpcion.setToolTip(QCoreApplication.translate("FormTR", u"Activa para calcular tambien el %ALCons junto con el RT60", None))
#endif // QT_CONFIG(tooltip)
        self.checkInteligibilidadOpcion.setText(QCoreApplication.translate("FormTR", u"Incluir Inteligibilidad del Habla", None))
        self.labelError.setText("")
#if QT_CONFIG(tooltip)
        self.botonIniciarAnalisis.setToolTip(QCoreApplication.translate("FormTR", u"Calcular RT60 con los datos ingresados", None))
#endif // QT_CONFIG(tooltip)
        self.botonIniciarAnalisis.setText(QCoreApplication.translate("FormTR", u"Iniciar Analisis", None))
    # retranslateUi

