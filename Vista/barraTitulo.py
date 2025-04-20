# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barraTitulo.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_formBarraTitulo(object):
    def setupUi(self, formBarraTitulo):
        if not formBarraTitulo.objectName():
            formBarraTitulo.setObjectName(u"formBarraTitulo")
        formBarraTitulo.resize(962, 50)
        formBarraTitulo.setMinimumSize(QSize(0, 50))
        formBarraTitulo.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(formBarraTitulo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTittleBar = QFrame(formBarraTitulo)
        self.frameTittleBar.setObjectName(u"frameTittleBar")
        self.frameTittleBar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 0, 43)\n"
"}\n"
"QPushButton {\n"
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
        self.frameTittleBar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTittleBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logoBarraTitulo = QLabel(self.frameTittleBar)
        self.logoBarraTitulo.setObjectName(u"logoBarraTitulo")
        self.logoBarraTitulo.setMinimumSize(QSize(32, 32))
        self.logoBarraTitulo.setMaximumSize(QSize(32, 32))
        self.logoBarraTitulo.setPixmap(QPixmap(u"graficas/iconos/logoBN.png"))

        self.horizontalLayout_2.addWidget(self.logoBarraTitulo)

        self.labelTittleBar = QLabel(self.frameTittleBar)
        self.labelTittleBar.setObjectName(u"labelTittleBar")

        self.horizontalLayout_2.addWidget(self.labelTittleBar)

        self.horizontalSpacer = QSpacerItem(543, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonMinim = QPushButton(self.frameTittleBar)
        self.buttonMinim.setObjectName(u"buttonMinim")
        self.buttonMinim.setMinimumSize(QSize(40, 40))
        self.buttonMinim.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u"graficas/iconos/menos-pequeno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonMinim.setIcon(icon)
        self.buttonMinim.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.buttonMinim)

        self.buttonMaxim = QPushButton(self.frameTittleBar)
        self.buttonMaxim.setObjectName(u"buttonMaxim")
        self.buttonMaxim.setMinimumSize(QSize(40, 40))
        self.buttonMaxim.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"graficas/iconos/restaurar-ventana.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonMaxim.setIcon(icon1)
        self.buttonMaxim.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.buttonMaxim)

        self.buttonClose = QPushButton(self.frameTittleBar)
        self.buttonClose.setObjectName(u"buttonClose")
        self.buttonClose.setMinimumSize(QSize(40, 40))
        self.buttonClose.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"graficas/iconos/cruz-pequena.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClose.setIcon(icon2)
        self.buttonClose.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.buttonClose)


        self.horizontalLayout.addWidget(self.frameTittleBar)


        self.retranslateUi(formBarraTitulo)

        QMetaObject.connectSlotsByName(formBarraTitulo)
    # setupUi

    def retranslateUi(self, formBarraTitulo):
        formBarraTitulo.setWindowTitle(QCoreApplication.translate("formBarraTitulo", u"Form", None))
        self.logoBarraTitulo.setText("")
        self.labelTittleBar.setText(QCoreApplication.translate("formBarraTitulo", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Universidad del Atl\u00e1ntico</span></p></body></html>", None))
        self.buttonMinim.setText("")
        self.buttonMaxim.setText("")
        self.buttonClose.setText("")
    # retranslateUi

