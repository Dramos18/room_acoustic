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
        formObjetoAdicional.resize(288, 61)
        self.verticalLayout = QVBoxLayout(formObjetoAdicional)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameObj = QFrame(formObjetoAdicional)
        self.frameObj.setObjectName(u"frameObj")
        self.frameObj.setFrameShape(QFrame.StyledPanel)
        self.frameObj.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameObj)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.lineObjAdicional = QLineEdit(self.frameObj)
        self.lineObjAdicional.setObjectName(u"lineObjAdicional")
        self.lineObjAdicional.setMinimumSize(QSize(70, 0))
        self.lineObjAdicional.setMaximumSize(QSize(90, 30))
        self.lineObjAdicional.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineObjAdicional)

        self.cbObjAdicional = QComboBox(self.frameObj)
        self.cbObjAdicional.setObjectName(u"cbObjAdicional")
        self.cbObjAdicional.setMinimumSize(QSize(80, 0))
        self.cbObjAdicional.setMaximumSize(QSize(150, 30))
        self.cbObjAdicional.setEditable(False)

        self.horizontalLayout.addWidget(self.cbObjAdicional)

        self.spinBoxCantidad = QSpinBox(self.frameObj)
        self.spinBoxCantidad.setObjectName(u"spinBoxCantidad")
        self.spinBoxCantidad.setMinimumSize(QSize(50, 0))
        self.spinBoxCantidad.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.spinBoxCantidad)

        self.botonAgregar_2 = QPushButton(self.frameObj)
        self.botonAgregar_2.setObjectName(u"botonAgregar_2")
        self.botonAgregar_2.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u"graficas/iconos/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonAgregar_2.setIcon(icon)
        self.botonAgregar_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.botonAgregar_2)

        self.botonEliminar_2 = QPushButton(self.frameObj)
        self.botonEliminar_2.setObjectName(u"botonEliminar_2")
        self.botonEliminar_2.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setKerning(True)
        self.botonEliminar_2.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"graficas/iconos/quitar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonEliminar_2.setIcon(icon1)
        self.botonEliminar_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.botonEliminar_2)


        self.verticalLayout.addWidget(self.frameObj)

        self.labelErrorObjAdicional = QLabel(formObjetoAdicional)
        self.labelErrorObjAdicional.setObjectName(u"labelErrorObjAdicional")

        self.verticalLayout.addWidget(self.labelErrorObjAdicional)

        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(formObjetoAdicional)

        QMetaObject.connectSlotsByName(formObjetoAdicional)
    # setupUi

    def retranslateUi(self, formObjetoAdicional):
        formObjetoAdicional.setWindowTitle(QCoreApplication.translate("formObjetoAdicional", u"Form", None))
#if QT_CONFIG(tooltip)
        self.lineObjAdicional.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Nombre del Objeto", None))
#endif // QT_CONFIG(tooltip)
        self.lineObjAdicional.setText("")
        self.lineObjAdicional.setPlaceholderText(QCoreApplication.translate("formObjetoAdicional", u"Ej: Sillas", None))
#if QT_CONFIG(tooltip)
        self.cbObjAdicional.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Material del Objeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBoxCantidad.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Cantidad", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.botonAgregar_2.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Agregar Objeto", None))
#endif // QT_CONFIG(tooltip)
        self.botonAgregar_2.setText("")
#if QT_CONFIG(tooltip)
        self.botonEliminar_2.setToolTip(QCoreApplication.translate("formObjetoAdicional", u"Quitar Objeto", None))
#endif // QT_CONFIG(tooltip)
        self.botonEliminar_2.setText("")
        self.labelErrorObjAdicional.setText("")
    # retranslateUi

