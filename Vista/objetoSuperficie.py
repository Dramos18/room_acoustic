# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'objetoSuperficie.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_formObjetoSuperficie(object):
    def setupUi(self, formObjetoSuperficie):
        if not formObjetoSuperficie.objectName():
            formObjetoSuperficie.setObjectName(u"formObjetoSuperficie")
        formObjetoSuperficie.resize(420, 64)
        formObjetoSuperficie.setStyleSheet(u"QFrame{\n"
"	background-color: transparent\n"
"}\n"
"QLineEdit {\n"
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
"    }\n"
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
"        selection-"
                        "background-color: lightgray;\n"
"    }\n"
"QComboBox QScrollBar:vertical {\n"
"        border: none;\n"
"        background: #f0f0f0;\n"
"        width: 10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
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
"    }")
        self.verticalLayout = QVBoxLayout(formObjetoSuperficie)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 4)
        self.objetoPdFrontal = QFrame(formObjetoSuperficie)
        self.objetoPdFrontal.setObjectName(u"objetoPdFrontal")
        self.objetoPdFrontal.setEnabled(True)
        self.objetoPdFrontal.setStyleSheet(u"QFrame{\n"
"	background-color: transparent\n"
"}")
        self.objetoPdFrontal.setFrameShape(QFrame.StyledPanel)
        self.objetoPdFrontal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.objetoPdFrontal)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 4, 4, 4)
        self.lineObjFrontal = QLineEdit(self.objetoPdFrontal)
        self.lineObjFrontal.setObjectName(u"lineObjFrontal")
        self.lineObjFrontal.setMinimumSize(QSize(90, 30))
        self.lineObjFrontal.setMaximumSize(QSize(100, 30))
        self.lineObjFrontal.setClearButtonEnabled(False)

        self.horizontalLayout_12.addWidget(self.lineObjFrontal)

        self.cbObjFrontal = QComboBox(self.objetoPdFrontal)
        self.cbObjFrontal.setObjectName(u"cbObjFrontal")
        self.cbObjFrontal.setMinimumSize(QSize(150, 30))
        self.cbObjFrontal.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_12.addWidget(self.cbObjFrontal)

        self.lineObjAreaFrontal = QLineEdit(self.objetoPdFrontal)
        self.lineObjAreaFrontal.setObjectName(u"lineObjAreaFrontal")
        self.lineObjAreaFrontal.setMinimumSize(QSize(70, 30))
        self.lineObjAreaFrontal.setMaximumSize(QSize(70, 30))
        self.lineObjAreaFrontal.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_12.addWidget(self.lineObjAreaFrontal)

        self.botonAgregar = QPushButton(self.objetoPdFrontal)
        self.botonAgregar.setObjectName(u"botonAgregar")
        self.botonAgregar.setMinimumSize(QSize(25, 25))
        self.botonAgregar.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/graficas/iconos/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAgregar.setIcon(icon)
        self.botonAgregar.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.botonAgregar)

        self.botonEliminar = QPushButton(self.objetoPdFrontal)
        self.botonEliminar.setObjectName(u"botonEliminar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonEliminar.sizePolicy().hasHeightForWidth())
        self.botonEliminar.setSizePolicy(sizePolicy)
        self.botonEliminar.setMinimumSize(QSize(25, 25))
        self.botonEliminar.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setKerning(True)
        self.botonEliminar.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../../../../.designer/backup/graficas/iconos/quitar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonEliminar.setIcon(icon1)
        self.botonEliminar.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.botonEliminar)


        self.verticalLayout.addWidget(self.objetoPdFrontal)

        self.labelErrorObj = QLabel(formObjetoSuperficie)
        self.labelErrorObj.setObjectName(u"labelErrorObj")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelErrorObj.sizePolicy().hasHeightForWidth())
        self.labelErrorObj.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.labelErrorObj)

        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(formObjetoSuperficie)

        QMetaObject.connectSlotsByName(formObjetoSuperficie)
    # setupUi

    def retranslateUi(self, formObjetoSuperficie):
        formObjetoSuperficie.setWindowTitle(QCoreApplication.translate("formObjetoSuperficie", u"Form", None))
        self.lineObjFrontal.setText("")
        self.lineObjFrontal.setPlaceholderText(QCoreApplication.translate("formObjetoSuperficie", u"Nombre Objeto", None))
        self.lineObjAreaFrontal.setPlaceholderText(QCoreApplication.translate("formObjetoSuperficie", u"\u00c1rea (m2)", None))
        self.botonAgregar.setText("")
        self.botonEliminar.setText("")
        self.labelErrorObj.setText("")
    # retranslateUi

