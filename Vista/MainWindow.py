# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 487)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.495, y2:1, stop:0.306818 rgba(0, 0, 93, 255), stop:0.710227 rgba(0, 0, 45, 255))\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frameMain = QFrame(self.centralwidget)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setStyleSheet(u"QFrame{\n"
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
        self.frameMain.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frameMain)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameMainMiddle = QFrame(self.frameMain)
        self.frameMainMiddle.setObjectName(u"frameMainMiddle")
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(26)
        font.setBold(True)
        self.frameMainMiddle.setFont(font)
        self.frameMainMiddle.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frameMainMiddle)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelMainTittle = QLabel(self.frameMainMiddle)
        self.labelMainTittle.setObjectName(u"labelMainTittle")

        self.verticalLayout_4.addWidget(self.labelMainTittle)

        self.frameMainImage = QFrame(self.frameMainMiddle)
        self.frameMainImage.setObjectName(u"frameMainImage")
        self.frameMainImage.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frameMainImage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_4.addWidget(self.frameMainImage)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 4)

        self.verticalLayout_2.addWidget(self.frameMainMiddle)

        self.frameMainBotton = QFrame(self.frameMain)
        self.frameMainBotton.setObjectName(u"frameMainBotton")
        self.frameMainBotton.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameMainBotton)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_1 = QFrame(self.frameMainBotton)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid white;\n"
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
        self.frame_1.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, -1, 0, -1)
        self.bottonAjustes = QPushButton(self.frame_1)
        self.bottonAjustes.setObjectName(u"bottonAjustes")

        self.verticalLayout_6.addWidget(self.bottonAjustes)


        self.horizontalLayout.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.frameMainBotton)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid white;\n"
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
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.botonIniciar = QPushButton(self.frame_2)
        self.botonIniciar.setObjectName(u"botonIniciar")

        self.verticalLayout_5.addWidget(self.botonIniciar)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frameMainBotton)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid white;\n"
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
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 50, -1)
        self.botonAyuda = QPushButton(self.frame_3)
        self.botonAyuda.setObjectName(u"botonAyuda")

        self.verticalLayout_3.addWidget(self.botonAyuda)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout_2.addWidget(self.frameMainBotton)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frameMain)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelMainTittle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#ffffff;\">An\u00e1lisis Ac\u00fastico De Salas</span></p></body></html>", None))
        self.bottonAjustes.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.botonIniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.botonAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

