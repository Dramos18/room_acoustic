# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaPrincipal.ui'
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
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_formVentanaPrincipal(object):
    def setupUi(self, formVentanaPrincipal):
        if not formVentanaPrincipal.objectName():
            formVentanaPrincipal.setObjectName(u"formVentanaPrincipal")
        formVentanaPrincipal.resize(900, 600)
        formVentanaPrincipal.setStyleSheet(u"/* \u2500\u2500 Fondo principal \u2500\u2500 */\n"
"\n"
"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.495, y2:1, stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255))\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u2500\u2500 Frames internos transparentes \u2500\u2500 */\n"
"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u2500\u2500 Separador horizontal \u2500\u2500 */\n"
"QFrame#lineSeparador {\n"
"    background-color: rgba(255, 255, 255, 0.15);\n"
"    border: none;\n"
"    min-height: 0px;\n"
"    max-height: 0px;\n"
"}\n"
"\n"
"/* \u2500\u2500 T\u00edtulo principal \u2500\u2500 */\n"
"QLabel#labelMainTittle {\n"
"    color: #FFFFFF;\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 28pt;\n"
"    font-weight: 700;\n"
"    letter-spacing: 1px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u2500\u2500 Subt\u00edtulo / descripci\u00f3n \u2500\u2500 */\n"
"QLabel#labelSubTitulo {\n"
"    color: rgba(180,"
                        " 210, 255, 0.85);\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 11pt;\n"
"    font-weight: 400;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u2500\u2500 Label GIF \u2500\u2500 */\n"
"QLabel#labelSuperior {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u2500\u2500 Bot\u00f3n primario: Iniciar \u2500\u2500 */\n"
"QPushButton#botonIniciar {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0.0 rgba(30, 80, 200, 255),\n"
"        stop:1.0 rgba(60, 140, 255, 255)\n"
"    );\n"
"    color: #FFFFFF;\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 15pt;\n"
"    font-weight: 700;\n"
"    border: none;\n"
"    border-radius: 18px;\n"
"    padding: 14px 30px;\n"
"    letter-spacing: 1px;\n"
"}\n"
"QPushButton#botonIniciar:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0.0 rgba(50, 110, 230, 255),\n"
"        stop:1.0 rgba(90"
                        ", 170, 255, 255)\n"
"    );\n"
"}\n"
"QPushButton#botonIniciar:pressed {\n"
"    background-color: rgba(30, 60, 160, 255);\n"
"}\n"
"\n"
"/* \u2500\u2500 Bot\u00f3n secundario: Ayuda \u2500\u2500 */\n"
"QPushButton#botonAyuda {\n"
"    background-color: transparent;\n"
"    color: rgba(180, 210, 255, 0.90);\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 12pt;\n"
"    font-weight: 500;\n"
"    border: 1px solid rgba(150, 190, 255, 0.45);\n"
"    border-radius: 18px;\n"
"    padding: 10px 30px;\n"
"    letter-spacing: 0.5px;\n"
"}\n"
"QPushButton#botonAyuda:hover {\n"
"    background-color: rgba(100, 160, 255, 0.12);\n"
"    border: 1px solid rgba(180, 210, 255, 0.70);\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton#botonAyuda:pressed {\n"
"    background-color: rgba(100, 160, 255, 0.25);\n"
"}\n"
"\n"
"/* \u2500\u2500 Footer labels \u2500\u2500 */\n"
"QLabel#labelUniversidad {\n"
"    color: rgba(180, 210, 255, 0.60);\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    "
                        "font-size: 8pt;\n"
"    background: transparent;\n"
"}\n"
"QLabel#labelVersion {\n"
"    color: rgba(180, 210, 255, 0.40);\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 8pt;\n"
"    background: transparent;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(formVentanaPrincipal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(formVentanaPrincipal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QFrame { background-color: transparent; border: none; }")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.stackedWidgetPage1.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(self.stackedWidgetPage1)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setMinimumSize(QSize(0, 120))
        self.frameHeader.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_header = QVBoxLayout(self.frameHeader)
        self.verticalLayout_header.setSpacing(6)
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.verticalLayout_header.setContentsMargins(40, 28, 40, 14)
        self.labelMainTittle = QLabel(self.frameHeader)
        self.labelMainTittle.setObjectName(u"labelMainTittle")

        self.verticalLayout_header.addWidget(self.labelMainTittle)

        self.labelSubTitulo = QLabel(self.frameHeader)
        self.labelSubTitulo.setObjectName(u"labelSubTitulo")

        self.verticalLayout_header.addWidget(self.labelSubTitulo)


        self.verticalLayout_2.addWidget(self.frameHeader)

        self.lineSeparadorTop = QFrame(self.stackedWidgetPage1)
        self.lineSeparadorTop.setObjectName(u"lineSeparadorTop")
        self.lineSeparadorTop.setMinimumSize(QSize(0, 1))
        self.lineSeparadorTop.setMaximumSize(QSize(16777215, 1))
        self.lineSeparadorTop.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.12); border: none;")
        self.lineSeparadorTop.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.lineSeparadorTop)

        self.frameMainMiddle = QFrame(self.stackedWidgetPage1)
        self.frameMainMiddle.setObjectName(u"frameMainMiddle")
        self.frameMainMiddle.setFrameShape(QFrame.StyledPanel)
        self.frameMainMiddle.setLineWidth(0)
        self.horizontalLayout_middle = QHBoxLayout(self.frameMainMiddle)
        self.horizontalLayout_middle.setSpacing(0)
        self.horizontalLayout_middle.setObjectName(u"horizontalLayout_middle")
        self.horizontalLayout_middle.setContentsMargins(0, 0, 0, 0)
        self.frameGif = QFrame(self.frameMainMiddle)
        self.frameGif.setObjectName(u"frameGif")
        self.frameGif.setFrameShape(QFrame.NoFrame)
        self.frameGif.setLineWidth(0)
        self.verticalLayout_gif = QVBoxLayout(self.frameGif)
        self.verticalLayout_gif.setObjectName(u"verticalLayout_gif")
        self.verticalLayout_gif.setContentsMargins(30, 20, 10, 20)
        self.labelSuperior = QLabel(self.frameGif)
        self.labelSuperior.setObjectName(u"labelSuperior")
        self.labelSuperior.setMinimumSize(QSize(0, 280))
        self.labelSuperior.setAlignment(Qt.AlignCenter)

        self.verticalLayout_gif.addWidget(self.labelSuperior)


        self.horizontalLayout_middle.addWidget(self.frameGif)

        self.frameBotones = QFrame(self.frameMainMiddle)
        self.frameBotones.setObjectName(u"frameBotones")
        self.frameBotones.setLayoutDirection(Qt.LeftToRight)
        self.frameBotones.setFrameShape(QFrame.NoFrame)
        self.frameBotones.setLineWidth(0)
        self.verticalLayout_botones = QVBoxLayout(self.frameBotones)
        self.verticalLayout_botones.setSpacing(16)
        self.verticalLayout_botones.setObjectName(u"verticalLayout_botones")
        self.verticalLayout_botones.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_botones.setContentsMargins(200, -1, 200, 40)
        self.verticalSpacerTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_botones.addItem(self.verticalSpacerTop)

        self.labelAcciones = QLabel(self.frameBotones)
        self.labelAcciones.setObjectName(u"labelAcciones")
        self.labelAcciones.setAlignment(Qt.AlignCenter)

        self.verticalLayout_botones.addWidget(self.labelAcciones)

        self.botonIniciar = QPushButton(self.frameBotones)
        self.botonIniciar.setObjectName(u"botonIniciar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonIniciar.sizePolicy().hasHeightForWidth())
        self.botonIniciar.setSizePolicy(sizePolicy)
        self.botonIniciar.setMinimumSize(QSize(220, 56))
        self.botonIniciar.setMaximumSize(QSize(320, 56))
        self.botonIniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonIniciar.setAutoDefault(False)

        self.verticalLayout_botones.addWidget(self.botonIniciar)

        self.botonAyuda = QPushButton(self.frameBotones)
        self.botonAyuda.setObjectName(u"botonAyuda")
        self.botonAyuda.setMinimumSize(QSize(220, 46))
        self.botonAyuda.setMaximumSize(QSize(320, 46))
        self.botonAyuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonAyuda.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_botones.addWidget(self.botonAyuda)

        self.verticalSpacerBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_botones.addItem(self.verticalSpacerBottom)


        self.horizontalLayout_middle.addWidget(self.frameBotones)


        self.verticalLayout_2.addWidget(self.frameMainMiddle)

        self.lineSeparadorBottom = QFrame(self.stackedWidgetPage1)
        self.lineSeparadorBottom.setObjectName(u"lineSeparadorBottom")
        self.lineSeparadorBottom.setMinimumSize(QSize(0, 1))
        self.lineSeparadorBottom.setMaximumSize(QSize(16777215, 1))
        self.lineSeparadorBottom.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.12); border: none;")
        self.lineSeparadorBottom.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.lineSeparadorBottom)

        self.frameFooter = QFrame(self.stackedWidgetPage1)
        self.frameFooter.setObjectName(u"frameFooter")
        self.frameFooter.setMinimumSize(QSize(0, 36))
        self.frameFooter.setMaximumSize(QSize(16777215, 36))
        self.frameFooter.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_footer = QHBoxLayout(self.frameFooter)
        self.horizontalLayout_footer.setObjectName(u"horizontalLayout_footer")
        self.horizontalLayout_footer.setContentsMargins(20, 0, 20, 8)
        self.labelUniversidad = QLabel(self.frameFooter)
        self.labelUniversidad.setObjectName(u"labelUniversidad")

        self.horizontalLayout_footer.addWidget(self.labelUniversidad)

        self.horizontalSpacerFooter = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_footer.addItem(self.horizontalSpacerFooter)

        self.labelVersion = QLabel(self.frameFooter)
        self.labelVersion.setObjectName(u"labelVersion")

        self.horizontalLayout_footer.addWidget(self.labelVersion)


        self.verticalLayout_2.addWidget(self.frameFooter)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(formVentanaPrincipal)

        QMetaObject.connectSlotsByName(formVentanaPrincipal)
    # setupUi

    def retranslateUi(self, formVentanaPrincipal):
        formVentanaPrincipal.setWindowTitle(QCoreApplication.translate("formVentanaPrincipal", u"Form", None))
        self.labelMainTittle.setText(QCoreApplication.translate("formVentanaPrincipal", u"<html><head/><body><p align=\"center\">An\u00e1lisis Ac\u00fastico en Aulas de Clases</p></body></html>", None))
        self.labelSubTitulo.setText(QCoreApplication.translate("formVentanaPrincipal", u"<html><head/><body><p align=\"center\">Evaluaci\u00f3n de par\u00e1metros ac\u00fasticos \u00b7 Tiempo de Reverberaci\u00f3n \u00b7 Inteligibilidad del Habla</p></body></html>", None))
        self.labelSuperior.setText("")
        self.labelAcciones.setText(QCoreApplication.translate("formVentanaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\"color:rgba(180,210,255,0.70); font-size:9pt;\">Selecciona una opci\u00f3n para comenzar</span></p></body></html>", None))
        self.botonIniciar.setText(QCoreApplication.translate("formVentanaPrincipal", u"\u25b6  Iniciar An\u00e1lisis", None))
        self.botonAyuda.setText(QCoreApplication.translate("formVentanaPrincipal", u"?  Ayuda", None))
        self.labelUniversidad.setText(QCoreApplication.translate("formVentanaPrincipal", u"Universidad del Atl\u00e1ntico \u00b7 Bloque H", None))
        self.labelVersion.setText(QCoreApplication.translate("formVentanaPrincipal", u"v1.0", None))
    # retranslateUi

