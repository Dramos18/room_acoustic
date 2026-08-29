
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from Datos.utils.reportePDF import ReportePDF
from Modelo.alcons2 import AlconsCalculator
from Vista.archivos_pyGenerados.inteligibilidadHabla import Ui_Form
from Recursos.estilos.estilo import estiloWarning

class VentanaInteligibiliad(QWidget):
    """
    Esta clase representa la ventana de "Tiempo de Reverberacion".
    Es una subclase de QWidget que carga el diseño de iniciarAnalisis.
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.indice_anterior = indice_anterior
        self.stacked_widget = stacked_widget

        self.ui.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))

        self.setup_events()



    def setup_events(self):
        self.ui.botonIniciarAnalisis.clicked.connect(lambda: self.enviar_calculos_inteligibilidad())
        self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)
        self.ui.botonGoHome.clicked.connect(self.ir_ventana_home)
    # boton atras
    def regresar_a_ventana_anterior(self):
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)
    def ir_ventana_home(self):
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(0)

    def validar_parametros_inteligibilidad(self):
        """
        Valida cada uno de los parámetros de inteligibilidad.
        Cualquier campo inválido se marca con fondo rojo.
        """
        errores = False  # Identifica si hay errores

        # Validar distancia
        distancia = self.ui.distanciaRyE.value()
        if distancia <= 0:
            self.ui.distanciaRyE.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 0.1);")
            errores = True
        else:
            self.ui.distanciaRyE.setStyleSheet("")  # Restaura el estilo

        # Validar tiempo de reverberación
        tiempo_reverberacion = self.ui.recintoTR.value()
        if tiempo_reverberacion <= 0:
            self.ui.recintoTR.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 0.1);")
            errores = True
        else:
            self.ui.recintoTR.setStyleSheet("")

        # Validar volumen
        volumen_sala = self.ui.volumenSala.value()
        if volumen_sala <= 0:
            self.ui.volumenSala.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 0.1);")
            errores = True
        else:
            self.ui.volumenSala.setStyleSheet("")

        # Validar coeficiente de absorción
        coeficiente_absorcion = self.ui.coeficienteMedio.value()
        if coeficiente_absorcion <= 0:
            self.ui.coeficienteMedio.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 0.1);")
            errores = True
        else:
            self.ui.coeficienteMedio.setStyleSheet("")

        # Validar superficie total
        superficie_total = self.ui.superficieTotal.value()
        if superficie_total <= 0:
            self.ui.superficieTotal.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 0.1);")
            errores = True
        else:
            self.ui.superficieTotal.setStyleSheet("")

        # Verificar si hay errores
        if errores:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)  # Icono de advertencia
            msg.setWindowTitle("Error de Validación")
            msg.setText("Algunos parámetros son inválidos (0 o negativos). Por favor, corrígelos.")

            msg.setStyleSheet(estiloWarning)

            msg.exec()

            return None

        # Retornar los valores válidos como un diccionario
        reporte = {
            "distancia": distancia,
            "tiempo_reverberacion": tiempo_reverberacion,
            "volumen_sala": volumen_sala,
            "coeficiente_absorcion": coeficiente_absorcion,
            "superficie_total": superficie_total,
        }
        return reporte

    def enviar_calculos_inteligibilidad(self):
        """
        Valida los parámetros y muestra un resumen con opción de generar PDF.
        """
        datos = self.validar_parametros_inteligibilidad()
        if datos:
            print("Validación exitosa. Datos obtenidos:", datos)

            try:
                # Generar el reporte desde los cálculos
                reporte = AlconsCalculator.generar_reporte(
                    distancia=datos["distancia"],
                    tr_2000Hz=datos["tiempo_reverberacion"],
                    volumen_sala=datos["volumen_sala"],
                    factor_directividad=2,  # Puedes asignar dinámicamente
                    superficie_total=datos["superficie_total"],
                    coef_medio_absor=datos["coeficiente_absorcion"],
                )

                # Mostrar el resumen clave en un QMessageBox
                self.mostrar_resumen_reporte(reporte)

            except Exception as e:
                QMessageBox.critical(self, "Error durante el cálculo", f"Se produjo un error:\n{str(e)}")

    def mostrar_resumen_reporte(self, reporte):
        """
        Muestra el resumen del reporte con opción para generar un PDF.
        """
        if "Error" in reporte:
            QMessageBox.warning(self, "Error en los cálculos", reporte["Error"])
            return

        # Crear el texto del resumen
        resumen = (
            f"<h3> Resultados del análisis %ALCONS </h3>"
            f"<p><b>Constante del Recinto (R):</b> {reporte['Constante del Recinto (R)']} </p>"
            f"<p><b>Distancia Crítica (Dc):</b> {reporte['Distancia Crítica (Dc)']} m</p>"
            f"<p><b>%ALCONS:</b> {reporte['%ALCONS']}%</p>"
            f"<p><b>Evaluación:</b> {reporte['Evaluación']}</p>"
        )

        # Crear el mensaje
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(estiloWarning)
        msg.setWindowTitle("Resumen del Análisis")
        msg.setText(resumen)
        msg.setStandardButtons(QMessageBox.Save | QMessageBox.Close)
        msg.button(QMessageBox.Save).setText("Generar Reporte PDF")

        # Manejo de botones
        respuesta = msg.exec()
        if respuesta == QMessageBox.Save:
            # Generar el PDF al guardar
            self.generar_reporte_pdf_alcons(reporte)

    def generar_reporte_pdf(self, reporte):
        """
        Genera un reporte detallado en PDF utilizando la librería ReportLab.
        """
        # Abrir un cuadro de diálogo para elegir dónde guardar el archivo
        nombre_archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Reporte PDF", os.getenv('HOME', './'), "Archivos PDF (*.pdf)"
        )
        if not nombre_archivo:  # Si el usuario cancela, no hacemos nada
            return

        try:
            # Crear el PDF
            c = canvas.Canvas(nombre_archivo, pagesize=letter)
            c.setFont("Helvetica-Bold", 16)



            # Título
            c.drawString(100, 800, "📊 Reporte de Inteligibilidad (%ALCONS)")

            # Espaciado inicial
            y = 760

            # Resultados principales
            c.setFont("Helvetica", 12)
            c.drawString(50, y, "Resultados Principales:")
            y -= 20  # Espaciado

            c.setFont("Helvetica", 11)
            c.drawString(50, y, f"Constante del Recinto (R): {reporte['Constante del Recinto (R)']}")
            y -= 20
            c.drawString(50, y, f"Distancia Crítica (Dc): {reporte['Distancia Crítica (Dc)']} m")
            y -= 20
            c.drawString(50, y, f"%ALCONS: {reporte['%ALCONS']}%")
            y -= 20
            c.drawString(50, y, f"Evaluación: {reporte['Evaluación']}")

            agregar_marca_agua(c, letter, letter, "../Recursos/iconos/isotipoUA.png")

            # Espaciado antes de los detalles técnicos
            y -= 40
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, "Detalles Técnicos:")
            y -= 20

            # Agregar los detalles técnicos en forma de lista
            c.setFont("Helvetica", 11)
            for clave, valor in reporte["Detalles"].items():
                if y < 50:  # Salto de nueva página si se llena
                    c.showPage()
                    c.setFont("Helvetica", 11)
                    y = 800
                c.drawString(60, y, f"- {clave}: {valor}")
                y -= 20

            # Finalizar y guardar el PDF
            c.showPage()
            c.save()

            msgOk = QMessageBox(self)
            msgOk.setIcon(QMessageBox.Information)
            msgOk.setWindowTitle("Reporte Generado")
            msgOk.setText(f"El reporte PDF se ha guardado correctamente en:\n{nombre_archivo}")
            msgOk.setStyleSheet(estiloWarning)
            msgOk.exec()

        except Exception as e:
            msgError = QMessageBox(self)
            msgError.setIcon(QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText(f"Hubo un error al generar el PDF:\n{str(e)}")
            msgError.setStyleSheet(estiloWarning)
            msgError.exec()

    def generar_reporte_pdf_alcons(self, reporte):

        ReportePDF.reporte_inteligibiliad(self, reporte)

def agregar_marca_agua(c, width, height, logo_path):
    logo = ImageReader(logo_path)
    logo_width = 300
    logo_height = 300
    x = (width - logo_width) / 2
    y = (height - logo_height) / 2

    c.saveState()
    c.setFillAlpha(0.1)
    c.drawImage(logo, x, y, width=logo_width, height=logo_height, mask='auto')
    c.restoreState()

