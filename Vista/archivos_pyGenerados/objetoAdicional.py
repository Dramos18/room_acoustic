# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'objetoAdicional.ui'
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
    QSpinBox, QVBoxLayout, QWidget)

class Ui_formObjetoAdicional(object):
    def setupUi(self, formObjetoAdicional):
        if not formObjetoAdicional.objectName():
            formObjetoAdicional.setObjectName(u"formObjetoAdicional")
        formObjetoAdicional.resize(320, 56)
        formObjetoAdicional.setStyleSheet(u"QWidget#formObjetoAdicional { background: transparent; }\n"
"QFrame { background-color: transparent; border: none; }\n"
"\n"
"/* Card del objeto adicional \u2014 acento naranja para diferenciarlo de superficies */\n"
"QFrame#frameObjAdicCard {\n"
"    background-color: rgba(255,255,255,0.07);\n"
"    border: 1px solid rgba(255,255,255,0.16);\n"
"    border-left: 2px solid rgba(251,146,60,0.65);\n"
"    border-radius: 8px;\n"
"}\n"
"QFrame#frameObjAdicCard:hover {\n"
"    background-color: rgba(255,255,255,0.11);\n"
"    border-left: 2px solid rgba(251,146,60,0.90);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 10px;\n"
"    color: white;\n"
"    background: rgba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.28);\n"
"    border-radius: 6px;\n"
"    padding: 3px 7px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgba(251,146,60,0.80);\n"
"    background: rgba(251,146,60,0.12);\n"
"}\n"
"QLineEdit::placeholder { color: rgba(255,255,255,0.35); }\n"
"\n"
"QComboBox {\n"
"    background: rg"
                        "ba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.28);\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-size: 10px;\n"
"    padding: 3px 6px;\n"
"}\n"
"QComboBox:focus { border: 1px solid rgba(251,146,60,0.80); }\n"
"QComboBox::drop-down { border: none; width: 18px; }\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #001a4d;\n"
"    color: white;\n"
"    selection-background-color: rgba(251,146,60,0.30);\n"
"    border: 1px solid rgba(255,255,255,0.20);\n"
"}\n"
"QComboBox QScrollBar:vertical { border: none; background: #f0f0f0; width: 8px; }\n"
"QComboBox QScrollBar::handle:vertical { background: #bfbfbf; min-height: 16px; border-radius: 3px; }\n"
"\n"
"QSpinBox {\n"
"    background: rgba(255,255,255,0.12);\n"
"    border: 1px solid rgba(255,255,255,0.28);\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-size: 10px;\n"
"    padding: 3px 6px;\n"
"}\n"
"QSpinBox:focus { border: 1px solid rgba(251,146,60,0.80); }\n"
"QSpinBox::up-button, QSpinBox::down-butt"
                        "on {\n"
"    width: 14px;\n"
"    background: rgba(255,255,255,0.10);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: transparent;\n"
"    border: 1px solid rgba(255,255,255,0.22);\n"
"    border-radius: 5px;\n"
"    min-width: 22px; max-width: 22px;\n"
"    min-height: 22px; max-height: 22px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255,255,255,0.16);\n"
"    border: 1px solid rgba(255,255,255,0.50);\n"
"}\n"
"QPushButton:pressed { background: rgba(255,255,255,0.32); }\n"
"\n"
"/* Label de error inline */\n"
"QLabel#labelErrorObjAdicional {\n"
"    color: rgba(248,113,113,0.90);\n"
"    font-size: 9px;\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding-left: 4px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(formObjetoAdicional)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 2, 0, 2)
        self.frameObjAdicCard = QFrame(formObjetoAdicional)
        self.frameObjAdicCard.setObjectName(u"frameObjAdicCard")
        self.frameObjAdicCard.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frameObjAdicCard)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 8, 5)
        self.lineObjAdicional = QLineEdit(self.frameObjAdicCard)
        self.lineObjAdicional.setObjectName(u"lineObjAdicional")
        self.lineObjAdicional.setMinimumSize(QSize(80, 26))
        self.lineObjAdicional.setMaximumSize(QSize(100, 26))
        self.lineObjAdicional.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineObjAdicional)

        self.cbObjAdicional = QComboBox(self.frameObjAdicCard)
        self.cbObjAdicional.setObjectName(u"cbObjAdicional")
        self.cbObjAdicional.setMinimumSize(QSize(120, 26))
        self.cbObjAdicional.setMaximumSize(QSize(170, 26))

        self.horizontalLayout.addWidget(self.cbObjAdicional)

        self.spinBoxCantidad = QSpinBox(self.frameObjAdicCard)
        self.spinBoxCantidad.setObjectName(u"spinBoxCantidad")
        self.spinBoxCantidad.setMinimumSize(QSize(52, 26))
        self.spinBoxCantidad.setMaximumSize(QSize(60, 26))
        self.spinBoxCantidad.setMinimum(1)
        self.spinBoxCantidad.setMaximum(200)

        self.horizontalLayout.addWidget(self.spinBoxCantidad)

        self.botonAgregar_2 = QPushButton(self.frameObjAdicCard)
        self.botonAgregar_2.setObjectName(u"botonAgregar_2")
        icon = QIcon()
        icon.addFile(u"graficas/iconos/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAgregar_2.setIcon(icon)
        self.botonAgregar_2.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.botonAgregar_2)

        self.botonEliminar_2 = QPushButton(self.frameObjAdicCard)
        self.botonEliminar_2.setObjectName(u"botonEliminar_2")
        icon1 = QIcon()
        icon1.addFile(u"graficas/iconos/quitar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonEliminar_2.setIcon(icon1)
        self.botonEliminar_2.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.botonEliminar_2)


        self.verticalLayout.addWidget(self.frameObjAdicCard)

        self.labelErrorObjAdicional = QLabel(formObjetoAdicional)
        self.labelErrorObjAdicional.setObjectName(u"labelErrorObjAdicional")
        self.labelErrorObjAdicional.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelErrorObjAdicional)


        self.retranslateUi(formObjetoAdicional)

        QMetaObject.connectSlotsByName(formObjetoAdicional)
    # setupUi

    def retranslateUi(self, formObjetoAdicional):
        formObjetoAdicional.setWindowTitle(QCoreApplication.translate("formObjetoAdicional", u"Form", None))
        self.lineObjAdicional.setPlaceholderText(QCoreApplication.translate("formObjetoAdicional", u"Ej: Sillas", None))
#if QT_CONFIG(tooltip)
        self.lineObjAdicional.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Nombre del objeto dentro del aula (ej: Sillas, Escritorios, Armario)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbObjAdicional.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Material del objeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBoxCantidad.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Cantidad de este tipo de objeto en el aula", None))
#endif // QT_CONFIG(tooltip)
        self.botonAgregar_2.setText("")
#if QT_CONFIG(tooltip)
        self.botonAgregar_2.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Agregar otro objeto adicional", None))
#endif // QT_CONFIG(tooltip)
        self.botonEliminar_2.setText("")
#if QT_CONFIG(tooltip)
        self.botonEliminar_2.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Eliminar este objeto adicional", None))
#endif // QT_CONFIG(tooltip)
        self.labelErrorObjAdicional.setText("")
    # retranslateUi

