from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QFileDialog, QMessageBox
import os

from Vista.graficas.estilo import estiloWarning


class ReportePDF:
    @staticmethod
    def reporte_inteligibiliad(self, reporte):
        """
        Genera un reporte detallado en PDF utilizando la librería ReportLab.
        """
        nombre_archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Reporte PDF", os.getenv('HOME', './'), "Archivos PDF (*.pdf)"
        )
        if not nombre_archivo:  # Si el usuario cancela, no hacemos nada
            return

        try:
            # Crear el PDF
            c = canvas.Canvas(nombre_archivo)
            c.setFont("Helvetica-Bold", 16)

            # Título
            c.drawString(100, 800, "📊 Reporte de Inteligibilidad (%ALCONS)")

            # Espaciado inicial
            y = 760

            # Resultados principales
            c.setFont("Helvetica", 12)
            c.drawString(50, y, "Resultados Principales:")
            y -= 20

            c.setFont("Helvetica", 11)
            c.drawString(50, y, f"Constante del Recinto (R): {reporte['Constante del Recinto (R)']}")
            y -= 20
            c.drawString(50, y, f"Distancia Crítica (Dc): {reporte['Distancia Crítica (Dc)']} m")
            y -= 20
            c.drawString(50, y, f"%ALCONS: {reporte['%ALCONS']}%")
            y -= 20
            c.drawString(50, y, f"Evaluación: {reporte['Evaluación']}")

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

