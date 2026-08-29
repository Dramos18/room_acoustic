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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_formObjetoSuperficie(object):
    def setupUi(self, formObjetoSuperficie):
        if not formObjetoSuperficie.objectName():
            formObjetoSuperficie.setObjectName(u"formObjetoSuperficie")
        formObjetoSuperficie.resize(440, 46)
        formObjetoSuperficie.setStyleSheet(u"/* Contenedor del widget */\n"
"QWidget#formObjetoSuperficie {\n"
"    background: transparent;\n"
"}\n"
"QFrame { background-color: transparent; border: none; }\n"
"\n"
"/* Card del objeto */\n"
"QFrame#frameObjSupCard {\n"
"    background-color: rgba(255,255,255,0.07);\n"
"    border: 1px solid rgba(255,255,255,0.18);\n"
"    border-left: 2px solid rgba(126,200,247,0.60);\n"
"    border-radius: 8px;\n"
"}\n"
"QFrame#frameObjSupCard:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"    border-left: 2px solid rgba(126,200,247,0.90);\n"
"}\n"
"\n"
"/* Inputs */\n"
"QLineEdit {\n"
"    font-size: 10px;\n"
"    font-weight: normal;\n"
"    color: white;\n"
"    background: rgba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.30);\n"
"    border-radius: 6px;\n"
"    padding: 3px 7px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7ec8f7;\n"
"    background: rgba(126,200,247,0.15);\n"
"}\n"
"QLineEdit::placeholder { color: rgba(255,255,255,0.35); }\n"
"\n"
"QComboBox {\n"
"    ba"
                        "ckground: rgba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.30);\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-size: 10px;\n"
"    padding: 3px 6px;\n"
"}\n"
"QComboBox:focus { border: 1px solid #7ec8f7; }\n"
"QComboBox::drop-down { border: none; width: 18px; }\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #001a4d;\n"
"    color: white;\n"
"    selection-background-color: rgba(126,200,247,0.30);\n"
"    border: 1px solid rgba(255,255,255,0.20);\n"
"}\n"
"QComboBox QScrollBar:vertical { border: none; background: #f0f0f0; width: 8px; }\n"
"QComboBox QScrollBar::handle:vertical { background: #bfbfbf; min-height: 16px; border-radius: 3px; }\n"
"\n"
"/* Botones +/\u2212 */\n"
"QPushButton {\n"
"    background: transparent;\n"
"    border: 1px solid rgba(255,255,255,0.25);\n"
"    border-radius: 5px;\n"
"    min-width: 22px; max-width: 22px;\n"
"    min-height: 22px; max-height: 22px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255,255,255,0.18);\n"
"    b"
                        "order: 1px solid rgba(255,255,255,0.55);\n"
"}\n"
"QPushButton:pressed { background: rgba(255,255,255,0.35); }\n"
"\n"
"/* Label de unidad */\n"
"QLabel#labelUnidadArea {\n"
"    color: rgba(255,255,255,0.50);\n"
"    font-size: 9px;\n"
"    min-width: 18px; max-width: 18px;\n"
"    border: none; background: transparent;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(formObjetoSuperficie)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 2, 0, 2)
        self.frameObjSupCard = QFrame(formObjetoSuperficie)
        self.frameObjSupCard.setObjectName(u"frameObjSupCard")
        self.frameObjSupCard.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frameObjSupCard)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 4, 8, 4)
        self.lineObjFrontal = QLineEdit(self.frameObjSupCard)
        self.lineObjFrontal.setObjectName(u"lineObjFrontal")
        self.lineObjFrontal.setMinimumSize(QSize(90, 28))
        self.lineObjFrontal.setMaximumSize(QSize(110, 28))
        self.lineObjFrontal.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.lineObjFrontal)

        self.cbObjFrontal = QComboBox(self.frameObjSupCard)
        self.cbObjFrontal.setObjectName(u"cbObjFrontal")
        self.cbObjFrontal.setMinimumSize(QSize(150, 28))
        self.cbObjFrontal.setMaximumSize(QSize(220, 28))

        self.horizontalLayout_12.addWidget(self.cbObjFrontal)

        self.lineObjAreaFrontal = QLineEdit(self.frameObjSupCard)
        self.lineObjAreaFrontal.setObjectName(u"lineObjAreaFrontal")
        self.lineObjAreaFrontal.setMinimumSize(QSize(68, 28))
        self.lineObjAreaFrontal.setMaximumSize(QSize(68, 28))

        self.horizontalLayout_12.addWidget(self.lineObjAreaFrontal)

        self.botonAgregar = QPushButton(self.frameObjSupCard)
        self.botonAgregar.setObjectName(u"botonAgregar")
        icon = QIcon()
        icon.addFile(u"graficas/iconos/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAgregar.setIcon(icon)
        self.botonAgregar.setIconSize(QSize(18, 18))

        self.horizontalLayout_12.addWidget(self.botonAgregar)

        self.botonEliminar = QPushButton(self.frameObjSupCard)
        self.botonEliminar.setObjectName(u"botonEliminar")
        icon1 = QIcon()
        icon1.addFile(u"graficas/iconos/quitar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonEliminar.setIcon(icon1)
        self.botonEliminar.setIconSize(QSize(18, 18))

        self.horizontalLayout_12.addWidget(self.botonEliminar)


        self.verticalLayout.addWidget(self.frameObjSupCard)


        self.retranslateUi(formObjetoSuperficie)

        QMetaObject.connectSlotsByName(formObjetoSuperficie)
    # setupUi

    def retranslateUi(self, formObjetoSuperficie):
        formObjetoSuperficie.setWindowTitle(QCoreApplication.translate("formObjetoSuperficie", u"Form", None))
        self.lineObjFrontal.setPlaceholderText(QCoreApplication.translate("formObjetoSuperficie", u"Nombre objeto", None))
#if QT_CONFIG(tooltip)
        self.lineObjFrontal.setToolTip(QCoreApplication.translate("formObjetoSuperficie", u"Nombre del objeto adherido a esta superficie (ej: Puerta, Ventana, Tablero)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbObjFrontal.setToolTip(QCoreApplication.translate("formObjetoSuperficie", u"Material del objeto adherido", None))
#endif // QT_CONFIG(tooltip)
        self.lineObjAreaFrontal.setPlaceholderText(QCoreApplication.translate("formObjetoSuperficie", u"Area m\u00b2", None))
#if QT_CONFIG(tooltip)
        self.lineObjAreaFrontal.setToolTip(QCoreApplication.translate("formObjetoSuperficie", u"Area ocupada por este objeto en la superficie (en metros cuadrados)", None))
#endif // QT_CONFIG(tooltip)
        self.botonAgregar.setText("")
#if QT_CONFIG(tooltip)
        self.botonAgregar.setToolTip(QCoreApplication.translate("formObjetoSuperficie", u"Agregar otro objeto a esta superficie", None))
#endif // QT_CONFIG(tooltip)
        self.botonEliminar.setText("")
#if QT_CONFIG(tooltip)
        self.botonEliminar.setToolTip(QCoreApplication.translate("formObjetoSuperficie", u"Eliminar este objeto", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

