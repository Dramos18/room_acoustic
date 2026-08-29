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
        Form.resize(1035, 620)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0.488, y1:0, x2:0.495, y2:1,\n"
"        stop:0.306818 rgba(0, 0, 93, 255),\n"
"        stop:0.710227 rgba(0, 0, 45, 255)\n"
"    );\n"
"}\n"
"QFrame {\n"
"    background-color: transparent;\n"
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
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frTop1 = QFrame(self.frame)
        self.frTop1.setObjectName(u"frTop1")
        self.frTop1.setMinimumSize(QSize(45, 100))
        self.frTop1.setMaximumSize(QSize(16777215, 80))
        self.frTop1.setStyleSheet(u"")
        self.frTop1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frTop1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, 20, -1)
        self.botonAtras = QPushButton(self.frTop1)
        self.botonAtras.setObjectName(u"botonAtras")
        self.botonAtras.setMinimumSize(QSize(45, 45))
        self.botonAtras.setMaximumSize(QSize(45, 45))
        self.botonAtras.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgba(255,255,255,0.35);\n"
"    border-radius: 22px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255,255,255,0.2);\n"
"    border: 1px solid white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255,0.4);\n"
"}")
        icon = QIcon()
        icon.addFile(u"estilos/iconos/angulo-izquierdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.botonAtras)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frameTitulo = QFrame(self.frTop1)
        self.frameTitulo.setObjectName(u"frameTitulo")
        self.frameTitulo.setFrameShape(QFrame.NoFrame)
        self.vloTitulo = QVBoxLayout(self.frameTitulo)
        self.vloTitulo.setSpacing(2)
        self.vloTitulo.setObjectName(u"vloTitulo")
        self.vloTitulo.setContentsMargins(0, 6, 0, 6)
        self.label = QLabel(self.frameTitulo)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setWordWrap(False)

        self.vloTitulo.addWidget(self.label)

        self.labelSubtitulo = QLabel(self.frameTitulo)
        self.labelSubtitulo.setObjectName(u"labelSubtitulo")
        self.labelSubtitulo.setMinimumSize(QSize(0, 20))

        self.vloTitulo.addWidget(self.labelSubtitulo)


        self.horizontalLayout.addWidget(self.frameTitulo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frTop1)

        self.frame_medio = QFrame(self.frame)
        self.frame_medio.setObjectName(u"frame_medio")
        self.frame_medio.setStyleSheet(u"")
        self.frame_medio.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_medio)
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(18, 14, 18, 14)
        self.frame_GuiaValores = QFrame(self.frame_medio)
        self.frame_GuiaValores.setObjectName(u"frame_GuiaValores")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_GuiaValores.sizePolicy().hasHeightForWidth())
        self.frame_GuiaValores.setSizePolicy(sizePolicy)
        self.frame_GuiaValores.setStyleSheet(u"QFrame {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel#labelGuiaTitulo {\n"
"    color: #7ec8f7;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel {\n"
"    color: rgba(255,255,255,0.80);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.frame_GuiaValores.setFrameShape(QFrame.NoFrame)
        self.vloGuia = QVBoxLayout(self.frame_GuiaValores)
        self.vloGuia.setSpacing(8)
        self.vloGuia.setObjectName(u"vloGuia")
        self.vloGuia.setContentsMargins(16, 18, 16, 18)
        self.labelGuiaTitulo = QLabel(self.frame_GuiaValores)
        self.labelGuiaTitulo.setObjectName(u"labelGuiaTitulo")

        self.vloGuia.addWidget(self.labelGuiaTitulo)

        self.lineaSepGuia = QFrame(self.frame_GuiaValores)
        self.lineaSepGuia.setObjectName(u"lineaSepGuia")
        self.lineaSepGuia.setStyleSheet(u"QFrame { background-color: rgba(126,200,247,0.4); max-height: 1px; border: none; }")
        self.lineaSepGuia.setFrameShape(QFrame.NoFrame)

        self.vloGuia.addWidget(self.lineaSepGuia)

        self.labelG1 = QLabel(self.frame_GuiaValores)
        self.labelG1.setObjectName(u"labelG1")
        self.labelG1.setTextFormat(Qt.AutoText)
        self.labelG1.setWordWrap(True)

        self.vloGuia.addWidget(self.labelG1)

        self.div1 = QFrame(self.frame_GuiaValores)
        self.div1.setObjectName(u"div1")
        self.div1.setStyleSheet(u"QFrame { background-color: rgba(255,255,255,0.12); max-height: 1px; border: none; }")
        self.div1.setFrameShape(QFrame.NoFrame)

        self.vloGuia.addWidget(self.div1)

        self.labelG2 = QLabel(self.frame_GuiaValores)
        self.labelG2.setObjectName(u"labelG2")
        self.labelG2.setWordWrap(True)

        self.vloGuia.addWidget(self.labelG2)

        self.div2 = QFrame(self.frame_GuiaValores)
        self.div2.setObjectName(u"div2")
        self.div2.setStyleSheet(u"QFrame { background-color: rgba(255,255,255,0.12); max-height: 1px; border: none; }")
        self.div2.setFrameShape(QFrame.NoFrame)

        self.vloGuia.addWidget(self.div2)

        self.labelG3 = QLabel(self.frame_GuiaValores)
        self.labelG3.setObjectName(u"labelG3")
        self.labelG3.setWordWrap(True)

        self.vloGuia.addWidget(self.labelG3)

        self.div3 = QFrame(self.frame_GuiaValores)
        self.div3.setObjectName(u"div3")
        self.div3.setStyleSheet(u"QFrame { background-color: rgba(255,255,255,0.12); max-height: 1px; border: none; }")
        self.div3.setFrameShape(QFrame.NoFrame)

        self.vloGuia.addWidget(self.div3)

        self.labelG4 = QLabel(self.frame_GuiaValores)
        self.labelG4.setObjectName(u"labelG4")
        self.labelG4.setWordWrap(True)

        self.vloGuia.addWidget(self.labelG4)

        self.div4 = QFrame(self.frame_GuiaValores)
        self.div4.setObjectName(u"div4")
        self.div4.setStyleSheet(u"QFrame { background-color: rgba(255,255,255,0.12); max-height: 1px; border: none; }")
        self.div4.setFrameShape(QFrame.NoFrame)

        self.vloGuia.addWidget(self.div4)

        self.labelG5 = QLabel(self.frame_GuiaValores)
        self.labelG5.setObjectName(u"labelG5")
        self.labelG5.setWordWrap(True)

        self.vloGuia.addWidget(self.labelG5)


        self.horizontalLayout_2.addWidget(self.frame_GuiaValores)

        self.frame_form = QFrame(self.frame_medio)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setEnabled(True)
        self.frame_form.setMaximumSize(QSize(16777215, 600))
        self.frame_form.setStyleSheet(u"\n"
"QFrame#frame_form {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QDoubleSpinBox { background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.40); border-radius: 8px; padding: 5px 8px; color: white; font-size: 11pt; font-weight: bold; min-width: 100px; max-width: 110px; } \n"
"\n"
"QDoubleSpinBox:focus { border: 1px solid #7ec8f7; background: rgba(126,200,247,0.18); } ")
        self.frame_form.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_form)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 18, 20, 18)
        self.frameEncabezado = QFrame(self.frame_form)
        self.frameEncabezado.setObjectName(u"frameEncabezado")
        self.frameEncabezado.setFrameShape(QFrame.NoFrame)
        self.vloEnc = QVBoxLayout(self.frameEncabezado)
        self.vloEnc.setSpacing(2)
        self.vloEnc.setObjectName(u"vloEnc")
        self.vloEnc.setContentsMargins(0, 0, 0, 8)
        self.labelFormTitulo = QLabel(self.frameEncabezado)
        self.labelFormTitulo.setObjectName(u"labelFormTitulo")

        self.vloEnc.addWidget(self.labelFormTitulo)

        self.labelFormDesc = QLabel(self.frameEncabezado)
        self.labelFormDesc.setObjectName(u"labelFormDesc")

        self.vloEnc.addWidget(self.labelFormDesc)

        self.lineaEncSep = QFrame(self.frameEncabezado)
        self.lineaEncSep.setObjectName(u"lineaEncSep")
        self.lineaEncSep.setStyleSheet(u"QFrame { background-color: rgba(126,200,247,0.45); max-height: 1px; border: none; }")
        self.lineaEncSep.setFrameShape(QFrame.NoFrame)

        self.vloEnc.addWidget(self.lineaEncSep)


        self.verticalLayout_3.addWidget(self.frameEncabezado)

        self.frameFilaX_2 = QFrame(self.frame_form)
        self.frameFilaX_2.setObjectName(u"frameFilaX_2")
        self.frameFilaX_2.setStyleSheet(u"QFrame#frameFilaX_2 {\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#frameFilaX_2:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"}\n"
"QLabel#labelNumero_2 {\n"
"    color: #7ec8f7;\n"
"    font-size: 15pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"}\n"
"QLabel#labelCampoNombre_2 {\n"
"    color: white;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelCampoDesc_2 {\n"
"    color: rgba(255,255,255,0.60);\n"
"    font-size: 8pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelUnidad_2 {\n"
"    color: rgba(255,255,255,0.55);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}")
        self.frameFilaX_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frameFilaX_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 6, 10, 6)
        self.labelNumero_2 = QLabel(self.frameFilaX_2)
        self.labelNumero_2.setObjectName(u"labelNumero_2")
        self.labelNumero_2.setMinimumSize(QSize(28, 0))
        self.labelNumero_2.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_3.addWidget(self.labelNumero_2)

        self.frameTxtD = QFrame(self.frameFilaX_2)
        self.frameTxtD.setObjectName(u"frameTxtD")
        self.frameTxtD.setFrameShape(QFrame.NoFrame)
        self.vloTxtD = QVBoxLayout(self.frameTxtD)
        self.vloTxtD.setSpacing(1)
        self.vloTxtD.setObjectName(u"vloTxtD")
        self.vloTxtD.setContentsMargins(0, 0, 0, 0)
        self.labelCampoNombre_2 = QLabel(self.frameTxtD)
        self.labelCampoNombre_2.setObjectName(u"labelCampoNombre_2")

        self.vloTxtD.addWidget(self.labelCampoNombre_2)

        self.labelCampoDesc_2 = QLabel(self.frameTxtD)
        self.labelCampoDesc_2.setObjectName(u"labelCampoDesc_2")

        self.vloTxtD.addWidget(self.labelCampoDesc_2)


        self.horizontalLayout_3.addWidget(self.frameTxtD)

        self.sp1 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.sp1)

        self.labelUnidad_2 = QLabel(self.frameFilaX_2)
        self.labelUnidad_2.setObjectName(u"labelUnidad_2")

        self.horizontalLayout_3.addWidget(self.labelUnidad_2)

        self.distanciaRyE = QDoubleSpinBox(self.frameFilaX_2)
        self.distanciaRyE.setObjectName(u"distanciaRyE")
        self.distanciaRyE.setMinimumSize(QSize(118, 0))
        self.distanciaRyE.setMaximumSize(QSize(128, 16777215))
        self.distanciaRyE.setDecimals(2)
        self.distanciaRyE.setMinimum(0.000000000000000)
        self.distanciaRyE.setMaximum(30.000000000000000)
        self.distanciaRyE.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.distanciaRyE)


        self.verticalLayout_3.addWidget(self.frameFilaX_2)

        self.frameFilaX_3 = QFrame(self.frame_form)
        self.frameFilaX_3.setObjectName(u"frameFilaX_3")
        self.frameFilaX_3.setStyleSheet(u"QFrame#frameFilaX_3 {\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#frameFilaX_3:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"}\n"
"QLabel#labelNumero_3 {\n"
"    color: #7ec8f7;\n"
"    font-size: 15pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"}\n"
"QLabel#labelCampoNombre_3 {\n"
"    color: white;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelCampoDesc_3 {\n"
"    color: rgba(255,255,255,0.60);\n"
"    font-size: 8pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelUnidad_3 {\n"
"    color: rgba(255,255,255,0.55);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}")
        self.frameFilaX_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frameFilaX_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 6, 10, 6)
        self.labelNumero_3 = QLabel(self.frameFilaX_3)
        self.labelNumero_3.setObjectName(u"labelNumero_3")
        self.labelNumero_3.setMinimumSize(QSize(28, 0))
        self.labelNumero_3.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_4.addWidget(self.labelNumero_3)

        self.frameTxtTR = QFrame(self.frameFilaX_3)
        self.frameTxtTR.setObjectName(u"frameTxtTR")
        self.frameTxtTR.setFrameShape(QFrame.NoFrame)
        self.vloTxtTR = QVBoxLayout(self.frameTxtTR)
        self.vloTxtTR.setSpacing(1)
        self.vloTxtTR.setObjectName(u"vloTxtTR")
        self.vloTxtTR.setContentsMargins(0, 0, 0, 0)
        self.labelCampoNombre_3 = QLabel(self.frameTxtTR)
        self.labelCampoNombre_3.setObjectName(u"labelCampoNombre_3")

        self.vloTxtTR.addWidget(self.labelCampoNombre_3)

        self.labelCampoDesc_3 = QLabel(self.frameTxtTR)
        self.labelCampoDesc_3.setObjectName(u"labelCampoDesc_3")

        self.vloTxtTR.addWidget(self.labelCampoDesc_3)


        self.horizontalLayout_4.addWidget(self.frameTxtTR)

        self.sp2 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.sp2)

        self.labelUnidad_3 = QLabel(self.frameFilaX_3)
        self.labelUnidad_3.setObjectName(u"labelUnidad_3")

        self.horizontalLayout_4.addWidget(self.labelUnidad_3)

        self.recintoTR = QDoubleSpinBox(self.frameFilaX_3)
        self.recintoTR.setObjectName(u"recintoTR")
        self.recintoTR.setMinimumSize(QSize(118, 0))
        self.recintoTR.setMaximumSize(QSize(128, 16777215))
        self.recintoTR.setDecimals(2)
        self.recintoTR.setMinimum(0.000000000000000)
        self.recintoTR.setMaximum(10.000000000000000)
        self.recintoTR.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.recintoTR)


        self.verticalLayout_3.addWidget(self.frameFilaX_3)

        self.frameFilaX = QFrame(self.frame_form)
        self.frameFilaX.setObjectName(u"frameFilaX")
        self.frameFilaX.setStyleSheet(u"QFrame#frameFilaX {\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#frameFilaX_2:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"}\n"
"QLabel#labelNumero {\n"
"    color: #7ec8f7;\n"
"    font-size: 15pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"}\n"
"QLabel#labelCampoNombre {\n"
"    color: white;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelCampoDesc {\n"
"    color: rgba(255,255,255,0.60);\n"
"    font-size: 8pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelUnidad {\n"
"    color: rgba(255,255,255,0.55);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}")
        self.frameFilaX.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frameFilaX)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 6, 10, 6)
        self.labelNumero = QLabel(self.frameFilaX)
        self.labelNumero.setObjectName(u"labelNumero")
        self.labelNumero.setMinimumSize(QSize(28, 0))
        self.labelNumero.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_5.addWidget(self.labelNumero)

        self.frameTxtV = QFrame(self.frameFilaX)
        self.frameTxtV.setObjectName(u"frameTxtV")
        self.frameTxtV.setFrameShape(QFrame.NoFrame)
        self.vloTxtV = QVBoxLayout(self.frameTxtV)
        self.vloTxtV.setSpacing(1)
        self.vloTxtV.setObjectName(u"vloTxtV")
        self.vloTxtV.setContentsMargins(0, 0, 0, 0)
        self.labelCampoNombre = QLabel(self.frameTxtV)
        self.labelCampoNombre.setObjectName(u"labelCampoNombre")

        self.vloTxtV.addWidget(self.labelCampoNombre)

        self.labelCampoDesc = QLabel(self.frameTxtV)
        self.labelCampoDesc.setObjectName(u"labelCampoDesc")

        self.vloTxtV.addWidget(self.labelCampoDesc)


        self.horizontalLayout_5.addWidget(self.frameTxtV)

        self.sp3 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_5.addItem(self.sp3)

        self.labelUnidad = QLabel(self.frameFilaX)
        self.labelUnidad.setObjectName(u"labelUnidad")

        self.horizontalLayout_5.addWidget(self.labelUnidad)

        self.volumenSala = QDoubleSpinBox(self.frameFilaX)
        self.volumenSala.setObjectName(u"volumenSala")
        self.volumenSala.setMinimumSize(QSize(118, 0))
        self.volumenSala.setMaximumSize(QSize(128, 16777215))
        self.volumenSala.setDecimals(2)
        self.volumenSala.setMinimum(0.000000000000000)
        self.volumenSala.setMaximum(2000.000000000000000)
        self.volumenSala.setSingleStep(10.000000000000000)

        self.horizontalLayout_5.addWidget(self.volumenSala)


        self.verticalLayout_3.addWidget(self.frameFilaX)

        self.frameFilaX_4 = QFrame(self.frame_form)
        self.frameFilaX_4.setObjectName(u"frameFilaX_4")
        self.frameFilaX_4.setStyleSheet(u"QFrame#frameFilaX_4 {\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#frameFilaX_4:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"}\n"
"QLabel#labelNumero_4 {\n"
"    color: #7ec8f7;\n"
"    font-size: 15pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"}\n"
"QLabel#labelCampoNombre_4 {\n"
"    color: white;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelCampoDesc_4 {\n"
"    color: rgba(255,255,255,0.60);\n"
"    font-size: 8pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelUnidad_4 {\n"
"    color: rgba(255,255,255,0.55);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}")
        self.frameFilaX_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frameFilaX_4)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 6, 10, 6)
        self.labelNumero_4 = QLabel(self.frameFilaX_4)
        self.labelNumero_4.setObjectName(u"labelNumero_4")
        self.labelNumero_4.setMinimumSize(QSize(28, 0))
        self.labelNumero_4.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_6.addWidget(self.labelNumero_4)

        self.frameTxtC = QFrame(self.frameFilaX_4)
        self.frameTxtC.setObjectName(u"frameTxtC")
        self.frameTxtC.setFrameShape(QFrame.NoFrame)
        self.vloTxtC = QVBoxLayout(self.frameTxtC)
        self.vloTxtC.setSpacing(1)
        self.vloTxtC.setObjectName(u"vloTxtC")
        self.vloTxtC.setContentsMargins(0, 0, 0, 0)
        self.labelCampoNombre_4 = QLabel(self.frameTxtC)
        self.labelCampoNombre_4.setObjectName(u"labelCampoNombre_4")

        self.vloTxtC.addWidget(self.labelCampoNombre_4)

        self.labelCampoDesc_4 = QLabel(self.frameTxtC)
        self.labelCampoDesc_4.setObjectName(u"labelCampoDesc_4")

        self.vloTxtC.addWidget(self.labelCampoDesc_4)


        self.horizontalLayout_6.addWidget(self.frameTxtC)

        self.sp4 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_6.addItem(self.sp4)

        self.labelUnidad_4 = QLabel(self.frameFilaX_4)
        self.labelUnidad_4.setObjectName(u"labelUnidad_4")

        self.horizontalLayout_6.addWidget(self.labelUnidad_4)

        self.coeficienteMedio = QDoubleSpinBox(self.frameFilaX_4)
        self.coeficienteMedio.setObjectName(u"coeficienteMedio")
        self.coeficienteMedio.setMinimumSize(QSize(118, 0))
        self.coeficienteMedio.setMaximumSize(QSize(128, 16777215))
        self.coeficienteMedio.setDecimals(3)
        self.coeficienteMedio.setMinimum(0.000000000000000)
        self.coeficienteMedio.setMaximum(1.000000000000000)
        self.coeficienteMedio.setSingleStep(0.010000000000000)

        self.horizontalLayout_6.addWidget(self.coeficienteMedio)


        self.verticalLayout_3.addWidget(self.frameFilaX_4)

        self.frameFilaX_5 = QFrame(self.frame_form)
        self.frameFilaX_5.setObjectName(u"frameFilaX_5")
        self.frameFilaX_5.setStyleSheet(u"QFrame#frameFilaX_5 {\n"
"    background-color: rgba(255,255,255,0.06);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#frameFilaX_5:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"}\n"
"QLabel#labelNumero_5 {\n"
"    color: #7ec8f7;\n"
"    font-size: 15pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    max-width: 28px;\n"
"}\n"
"QLabel#labelCampoNombre_5 {\n"
"    color: white;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelCampoDesc_5 {\n"
"    color: rgba(255,255,255,0.60);\n"
"    font-size: 8pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelUnidad_5 {\n"
"    color: rgba(255,255,255,0.55);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}")
        self.frameFilaX_5.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frameFilaX_5)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 6, 10, 6)
        self.labelNumero_5 = QLabel(self.frameFilaX_5)
        self.labelNumero_5.setObjectName(u"labelNumero_5")
        self.labelNumero_5.setMinimumSize(QSize(28, 0))
        self.labelNumero_5.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_7.addWidget(self.labelNumero_5)

        self.frameTxtS = QFrame(self.frameFilaX_5)
        self.frameTxtS.setObjectName(u"frameTxtS")
        self.frameTxtS.setFrameShape(QFrame.NoFrame)
        self.vloTxtS = QVBoxLayout(self.frameTxtS)
        self.vloTxtS.setSpacing(1)
        self.vloTxtS.setObjectName(u"vloTxtS")
        self.vloTxtS.setContentsMargins(0, 0, 0, 0)
        self.labelCampoNombre_5 = QLabel(self.frameTxtS)
        self.labelCampoNombre_5.setObjectName(u"labelCampoNombre_5")

        self.vloTxtS.addWidget(self.labelCampoNombre_5)

        self.labelCampoDesc_5 = QLabel(self.frameTxtS)
        self.labelCampoDesc_5.setObjectName(u"labelCampoDesc_5")

        self.vloTxtS.addWidget(self.labelCampoDesc_5)


        self.horizontalLayout_7.addWidget(self.frameTxtS)

        self.sp5 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_7.addItem(self.sp5)

        self.labelUnidad_5 = QLabel(self.frameFilaX_5)
        self.labelUnidad_5.setObjectName(u"labelUnidad_5")

        self.horizontalLayout_7.addWidget(self.labelUnidad_5)

        self.superficieTotal = QDoubleSpinBox(self.frameFilaX_5)
        self.superficieTotal.setObjectName(u"superficieTotal")
        self.superficieTotal.setMinimumSize(QSize(118, 0))
        self.superficieTotal.setMaximumSize(QSize(128, 16777215))
        self.superficieTotal.setDecimals(2)
        self.superficieTotal.setMinimum(0.000000000000000)
        self.superficieTotal.setMaximum(2000.000000000000000)
        self.superficieTotal.setSingleStep(10.000000000000000)

        self.horizontalLayout_7.addWidget(self.superficieTotal)


        self.verticalLayout_3.addWidget(self.frameFilaX_5)


        self.horizontalLayout_2.addWidget(self.frame_form)

        self.frame_escala = QFrame(self.frame_medio)
        self.frame_escala.setObjectName(u"frame_escala")
        sizePolicy.setHeightForWidth(self.frame_escala.sizePolicy().hasHeightForWidth())
        self.frame_escala.setSizePolicy(sizePolicy)
        self.frame_escala.setStyleSheet(u"\n"
"QFrame#frame_escala  {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* Transparente con leve fondo */\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel#labelEscalaTitulo {\n"
"    color: #7ec8f7;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel {\n"
"    color: rgba(255,255,255,0.85);\n"
"    font-size: 9pt;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelNivelExcelente { color: #22c55e; font-weight: bold; }\n"
"QLabel#labelNivelBuena     { color: #86efac; font-weight: bold; }\n"
"QLabel#labelNivelRegular   { color: #fde047; font-weight: bold; }\n"
"QLabel#labelNivelPobre     { color: #fb923c; font-weight: bold; }\n"
"QLabel#labelNivelMala      { color: #f87171; font-weight: bold; }\n"
"")
        self.frame_escala.setFrameShape(QFrame.NoFrame)
        self.vloEscala = QVBoxLayout(self.frame_escala)
        self.vloEscala.setSpacing(8)
        self.vloEscala.setObjectName(u"vloEscala")
        self.vloEscala.setContentsMargins(16, 18, 16, 18)
        self.labelEscalaTitulo = QLabel(self.frame_escala)
        self.labelEscalaTitulo.setObjectName(u"labelEscalaTitulo")

        self.vloEscala.addWidget(self.labelEscalaTitulo)

        self.lineaSepEscala = QFrame(self.frame_escala)
        self.lineaSepEscala.setObjectName(u"lineaSepEscala")
        self.lineaSepEscala.setStyleSheet(u"QFrame { background-color: rgba(126,200,247,0.4); max-height: 1px; border: none; }")
        self.lineaSepEscala.setFrameShape(QFrame.NoFrame)

        self.vloEscala.addWidget(self.lineaSepEscala)

        self.labelEscalaIntro = QLabel(self.frame_escala)
        self.labelEscalaIntro.setObjectName(u"labelEscalaIntro")
        self.labelEscalaIntro.setWordWrap(True)

        self.vloEscala.addWidget(self.labelEscalaIntro)

        self.fNiv1 = QFrame(self.frame_escala)
        self.fNiv1.setObjectName(u"fNiv1")
        self.fNiv1.setStyleSheet(u"QFrame { background-color: rgba(34,197,94,0.14); border-radius: 8px; border: 1px solid rgba(34,197,94,0.35); }")
        self.fNiv1.setFrameShape(QFrame.NoFrame)
        self.vN1 = QVBoxLayout(self.fNiv1)
        self.vN1.setSpacing(1)
        self.vN1.setObjectName(u"vN1")
        self.vN1.setContentsMargins(8, 5, 8, 5)
        self.labelNivelExcelente = QLabel(self.fNiv1)
        self.labelNivelExcelente.setObjectName(u"labelNivelExcelente")

        self.vN1.addWidget(self.labelNivelExcelente)

        self.labelDescExcelente = QLabel(self.fNiv1)
        self.labelDescExcelente.setObjectName(u"labelDescExcelente")
        self.labelDescExcelente.setWordWrap(True)

        self.vN1.addWidget(self.labelDescExcelente)


        self.vloEscala.addWidget(self.fNiv1)

        self.fNiv2 = QFrame(self.frame_escala)
        self.fNiv2.setObjectName(u"fNiv2")
        self.fNiv2.setStyleSheet(u"QFrame { background-color: rgba(134,239,172,0.10); border-radius: 8px; border: 1px solid rgba(134,239,172,0.30); }")
        self.fNiv2.setFrameShape(QFrame.NoFrame)
        self.vN2 = QVBoxLayout(self.fNiv2)
        self.vN2.setSpacing(1)
        self.vN2.setObjectName(u"vN2")
        self.vN2.setContentsMargins(8, 5, 8, 5)
        self.labelNivelBuena = QLabel(self.fNiv2)
        self.labelNivelBuena.setObjectName(u"labelNivelBuena")

        self.vN2.addWidget(self.labelNivelBuena)

        self.labelDescBuena = QLabel(self.fNiv2)
        self.labelDescBuena.setObjectName(u"labelDescBuena")
        self.labelDescBuena.setWordWrap(True)

        self.vN2.addWidget(self.labelDescBuena)


        self.vloEscala.addWidget(self.fNiv2)

        self.fNiv3 = QFrame(self.frame_escala)
        self.fNiv3.setObjectName(u"fNiv3")
        self.fNiv3.setStyleSheet(u"QFrame { background-color: rgba(253,224,71,0.10); border-radius: 8px; border: 1px solid rgba(253,224,71,0.28); }")
        self.fNiv3.setFrameShape(QFrame.NoFrame)
        self.vN3 = QVBoxLayout(self.fNiv3)
        self.vN3.setSpacing(1)
        self.vN3.setObjectName(u"vN3")
        self.vN3.setContentsMargins(8, 5, 8, 5)
        self.labelNivelRegular = QLabel(self.fNiv3)
        self.labelNivelRegular.setObjectName(u"labelNivelRegular")

        self.vN3.addWidget(self.labelNivelRegular)

        self.labelDescRegular = QLabel(self.fNiv3)
        self.labelDescRegular.setObjectName(u"labelDescRegular")
        self.labelDescRegular.setWordWrap(True)

        self.vN3.addWidget(self.labelDescRegular)


        self.vloEscala.addWidget(self.fNiv3)

        self.fNiv4 = QFrame(self.frame_escala)
        self.fNiv4.setObjectName(u"fNiv4")
        self.fNiv4.setStyleSheet(u"QFrame { background-color: rgba(251,146,60,0.10); border-radius: 8px; border: 1px solid rgba(251,146,60,0.28); }")
        self.fNiv4.setFrameShape(QFrame.NoFrame)
        self.vN4 = QVBoxLayout(self.fNiv4)
        self.vN4.setSpacing(1)
        self.vN4.setObjectName(u"vN4")
        self.vN4.setContentsMargins(8, 5, 8, 5)
        self.labelNivelPobre = QLabel(self.fNiv4)
        self.labelNivelPobre.setObjectName(u"labelNivelPobre")

        self.vN4.addWidget(self.labelNivelPobre)

        self.labelDescPobre = QLabel(self.fNiv4)
        self.labelDescPobre.setObjectName(u"labelDescPobre")
        self.labelDescPobre.setWordWrap(True)

        self.vN4.addWidget(self.labelDescPobre)


        self.vloEscala.addWidget(self.fNiv4)

        self.fNiv5 = QFrame(self.frame_escala)
        self.fNiv5.setObjectName(u"fNiv5")
        self.fNiv5.setStyleSheet(u"QFrame { background-color: rgba(248,113,113,0.12); border-radius: 8px; border: 1px solid rgba(248,113,113,0.30); }")
        self.fNiv5.setFrameShape(QFrame.NoFrame)
        self.vN5 = QVBoxLayout(self.fNiv5)
        self.vN5.setSpacing(1)
        self.vN5.setObjectName(u"vN5")
        self.vN5.setContentsMargins(8, 5, 8, 5)
        self.labelNivelMala = QLabel(self.fNiv5)
        self.labelNivelMala.setObjectName(u"labelNivelMala")

        self.vN5.addWidget(self.labelNivelMala)

        self.labelDescMala = QLabel(self.fNiv5)
        self.labelDescMala.setObjectName(u"labelDescMala")
        self.labelDescMala.setWordWrap(True)

        self.vN5.addWidget(self.labelDescMala)


        self.vloEscala.addWidget(self.fNiv5)


        self.horizontalLayout_2.addWidget(self.frame_escala)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout_2.addWidget(self.frame_medio)

        self.frame_bottom = QFrame(self.frame)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(0, 64))
        self.frame_bottom.setStyleSheet(u"QFrame#frame_3 {\n"
"    background-color: rgba(0,0,0,0.20);\n"
"    border-top: 1px solid rgba(255,255,255,0.12);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgba(255,255,255,0.12);\n"
"    border: 1.5px solid rgba(255,255,255,0.45);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    border-radius: 12px;\n"
"    padding: 8px 22px;\n"
"    letter-spacing: 0.5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255,255,255,0.25);\n"
"    border: 1.5px solid white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255,255,255,0.45);\n"
"    color: #00005d;\n"
"}\n"
"QPushButton#botonIniciarAnalisis {\n"
"    background-color: rgba(126,200,247,0.22);\n"
"    border: 1.5px solid #7ec8f7;\n"
"    color: #7ec8f7;\n"
"}\n"
"QPushButton#botonIniciarAnalisis:hover {\n"
"    background-color: rgba(126,200,247,0.40);\n"
"    color: white;\n"
"    border-color: white;\n"
"}\n"
"")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.botonGoHome = QPushButton(self.frame_bottom)
        self.botonGoHome.setObjectName(u"botonGoHome")
        self.botonGoHome.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.botonGoHome)

        self.botonIniciarAnalisis = QPushButton(self.frame_bottom)
        self.botonIniciarAnalisis.setObjectName(u"botonIniciarAnalisis")
        self.botonIniciarAnalisis.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_8.addWidget(self.botonIniciarAnalisis)

        self.horizontalLayout_8.setStretch(0, 4)

        self.verticalLayout_2.addWidget(self.frame_bottom)

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
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">Inteligibilidad del Habla</span></p></body></html>", None))
        self.labelSubtitulo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:rgba(255,255,255,0.647059);\">Calculo del porcentaje de perdida de articulacion de consonantes (%ALCons)</span></p></body></html>", None))
        self.labelGuiaTitulo.setText(QCoreApplication.translate("Form", u"Guia de valores", None))
        self.labelG1.setText(QCoreApplication.translate("Form", u"<b>Distancia (r)</b><br/>Tipico en aulas: 1.5 \u2013 8 m<br/>Se usa la posicion del oyente mas lejano.", None))
        self.labelG2.setText(QCoreApplication.translate("Form", u"<b>Tiempo de Reverberacion (TR)</b><br/>Optimo para aulas: 0.4 \u2013 0.8 s<br/>Usar el valor a 2000 Hz.", None))
        self.labelG3.setText(QCoreApplication.translate("Form", u"<b>Volumen (V)</b><br/>Aulas tipicas: 100 \u2013 400 m3<br/>Largo x Ancho x Altura.", None))
        self.labelG4.setText(QCoreApplication.translate("Form", u"<b>Coeficiente de absorcion (a)</b><br/>Rango valido: 0.01 \u2013 1.00<br/>Promedio ponderado de todas las superficies.", None))
        self.labelG5.setText(QCoreApplication.translate("Form", u"<b>Superficie total (St)</b><br/>Tipico: 150 \u2013 500 m2<br/>Suma de todas las caras del recinto.", None))
        self.labelFormTitulo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:13pt; font-weight:700; color:#ffffff;\">Parametros de entrada</span></p></body></html>", None))
        self.labelFormDesc.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:rgba(255,255,255,0.54902);\">Completa los 5 campos para calcular el %ALCons</span></p></body></html>", None))
        self.labelNumero_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.labelCampoNombre_2.setText(QCoreApplication.translate("Form", u"Distancia emisor \u2013 receptor", None))
        self.labelCampoDesc_2.setText(QCoreApplication.translate("Form", u"Distancia entre el docente y el oyente mas lejano", None))
        self.labelUnidad_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">m</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.distanciaRyE.setToolTip(QCoreApplication.translate("Form", u"Distancia tipica en aulas: 1.5 \u2013 8 m", None))
#endif // QT_CONFIG(tooltip)
        self.labelNumero_3.setText(QCoreApplication.translate("Form", u"2", None))
        self.labelCampoNombre_3.setText(QCoreApplication.translate("Form", u"Tiempo de reverberacion (TR)", None))
        self.labelCampoDesc_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Valor a 2000 Hz</p></body></html>", None))
        self.labelUnidad_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">s</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.recintoTR.setToolTip(QCoreApplication.translate("Form", u"TR a 2000 Hz. Optimo en aulas: 0.4 \u2013 0.8 s", None))
#endif // QT_CONFIG(tooltip)
        self.labelNumero.setText(QCoreApplication.translate("Form", u"3", None))
        self.labelCampoNombre.setText(QCoreApplication.translate("Form", u"Volumen de la sala", None))
        self.labelCampoDesc.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Largo x Ancho x Altura</p></body></html>", None))
        self.labelUnidad.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">m3</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.volumenSala.setToolTip(QCoreApplication.translate("Form", u"Volumen total del recinto en metros cubicos", None))
#endif // QT_CONFIG(tooltip)
        self.labelNumero_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.labelCampoNombre_4.setText(QCoreApplication.translate("Form", u"Coeficiente medio de absorcion", None))
        self.labelCampoDesc_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Promedio ponderado de todas las superficies</p></body></html>", None))
        self.labelUnidad_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">  \u2014</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.coeficienteMedio.setToolTip(QCoreApplication.translate("Form", u"Coeficiente promedio de absorcion entre 0.01 y 1.00", None))
#endif // QT_CONFIG(tooltip)
        self.labelNumero_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.labelCampoNombre_5.setText(QCoreApplication.translate("Form", u"Superficie total del recinto", None))
        self.labelCampoDesc_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Suma de todas las caras (paredes, piso, techo)</p></body></html>", None))
        self.labelUnidad_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">m2</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.superficieTotal.setToolTip(QCoreApplication.translate("Form", u"Superficie total del recinto en metros cuadrados", None))
#endif // QT_CONFIG(tooltip)
        self.labelEscalaTitulo.setText(QCoreApplication.translate("Form", u"Escala %ALCons", None))
        self.labelEscalaIntro.setText(QCoreApplication.translate("Form", u"El %ALCons indica que porcion de las consonantes se pierde. Cuanto menor, mejor.", None))
        self.labelNivelExcelente.setText(QCoreApplication.translate("Form", u"Excelente  \u2014 0 % a 2 %", None))
        self.labelDescExcelente.setText(QCoreApplication.translate("Form", u"Comprension casi perfecta del habla.", None))
        self.labelNivelBuena.setText(QCoreApplication.translate("Form", u"Buena  \u2014 2 % a 5 %", None))
        self.labelDescBuena.setText(QCoreApplication.translate("Form", u"Ligeras perdidas, aceptable para aulas.", None))
        self.labelNivelRegular.setText(QCoreApplication.translate("Form", u"Regular  \u2014 5 % a 10 %", None))
        self.labelDescRegular.setText(QCoreApplication.translate("Form", u"Dificultades notorias de comprension.", None))
        self.labelNivelPobre.setText(QCoreApplication.translate("Form", u"Pobre  \u2014 10 % a 15 %", None))
        self.labelDescPobre.setText(QCoreApplication.translate("Form", u"Comunicacion claramente afectada.", None))
        self.labelNivelMala.setText(QCoreApplication.translate("Form", u"Mala  \u2014 mayor a 15 %", None))
        self.labelDescMala.setText(QCoreApplication.translate("Form", u"Comunicacion muy deficiente. Se requieren mejoras urgentes.", None))
#if QT_CONFIG(tooltip)
        self.botonGoHome.setToolTip(QCoreApplication.translate("Form", u"Regresar a la pantalla principal", None))
#endif // QT_CONFIG(tooltip)
        self.botonGoHome.setText(QCoreApplication.translate("Form", u"Ir al Inicio", None))
#if QT_CONFIG(tooltip)
        self.botonIniciarAnalisis.setToolTip(QCoreApplication.translate("Form", u"Calcular %ALCons con los valores ingresados", None))
#endif // QT_CONFIG(tooltip)
        self.botonIniciarAnalisis.setText(QCoreApplication.translate("Form", u"Iniciar Analisis", None))
    # retranslateUi

