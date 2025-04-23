from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
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

    @staticmethod
    def reporte_tiempo_reverberacion(self, resultados):
        nombre_archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Reporte PDF", os.getenv('HOME', './'), "Archivos PDF (*.pdf)"
        )
        if not nombre_archivo:  # Si el usuario cancela, no hacemos nada
            return

        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        # === 1. GRAFICA ===
        grafica = self.resultados.get("grafica")
        if grafica:
            grafica.seek(0)
            imagen = ImageReader(grafica)
            img_width, img_height = imagen.getSize()
            alto_deseado_pts = 150
            escala = alto_deseado_pts / img_height
            ancho_escala = img_width * escala
            x = (width - ancho_escala) / 2
            y = height - alto_deseado_pts - inch
            c.drawImage(imagen, x, y, width=ancho_escala, height=alto_deseado_pts)

        #c.showPage()  # Pasar a la siguiente página para la tabla

            tabla_top = y - 40

        # === 2. TABLA SABINE/EYRING ===
        sabine = self.resultados.get("sabine_rt", {})
        eyring = self.resultados.get("eyring_rt", {})
        frecuencias = sorted(sabine.keys())

        # Encabezados
        encabezados = ["Frecuencia (Hz)", "Sabine RT (s)", "Eyring RT (s)"]
        columnas = len(encabezados)
        filas = len(frecuencias) + 1

        # Dimensiones de la tabla
        col_width = (width - 2 * inch) / columnas
        row_height = 20
        tabla_top = height - inch
        tabla_left = inch

        # Título de la tabla
        c.setFont("Helvetica-Bold", 14)
        c.drawString(tabla_left, tabla_top + 30, "Resultados Numéricos")

        # Dibujar encabezado
        c.setFont("Helvetica-Bold", 10)
        for i, texto in enumerate(encabezados):
            x = tabla_left + i * col_width
            c.setFillColor(colors.lightblue)
            c.rect(x, tabla_top - row_height, col_width, row_height, fill=True, stroke=True)
            c.setFillColor(colors.black)
            c.drawCentredString(x + col_width / 2, tabla_top - row_height + 5, texto)

        # Dibujar celdas de datos
        c.setFont("Helvetica", 10)
        for fila, f in enumerate(frecuencias):
            y = tabla_top - (fila + 2) * row_height
            valores = [
                str(f),
                f"{sabine[f]:.2f}",
                f"{eyring.get(f, 0):.2f}"
            ]
            for col, val in enumerate(valores):
                x = tabla_left + col * col_width
                # Alternar colores de fila
                if fila % 2 == 0:
                    c.setFillColor(colors.whitesmoke)
                    c.rect(x, y, col_width, row_height, fill=True, stroke=True)
                else:
                    c.setFillColor(colors.lightgrey)
                    c.rect(x, y, col_width, row_height, fill=True, stroke=True)

                c.setFillColor(colors.black)
                c.drawCentredString(x + col_width / 2, y + 5, val)

        # === SEGUNDA PÁGINA CON INFORMACIÓN Y CONCLUSIÓN ===
        c.showPage()  # Nueva página

        sabine = self.resultados.get("sabine_rt")
        eyring = self.resultados.get("eyring_rt")
        frecuencias_mid = [500, 1000, 2000]

        sabine_mid = [sabine[f] for f in frecuencias_mid if f in sabine]
        eyring_mid = [eyring[f] for f in frecuencias_mid if f in eyring]

        trmid_sabine = sum(sabine_mid) / len(sabine_mid) if sabine_mid else 0
        trmid_eyring = sum(eyring_mid) / len(eyring_mid) if eyring_mid else 0

        es_optimo = trmid_sabine <= 0.8 and trmid_eyring <= 0.8

        # === Estilo y contenido ===
        c.setFont("Helvetica-Bold", 16)
        c.drawString(inch, height - inch, "Análisis Acústico: Interpretación de Resultados")

        c.setFont("Helvetica", 12)
        c.drawString(inch, height - inch - 30, f"Tr MID Sabine: {trmid_sabine:.2f} s")
        c.drawString(inch, height - inch - 50, f"Tr MID Eyring: {trmid_eyring:.2f} s")

        estado = "ÓPTIMA" if es_optimo else "NO ÓPTIMA"
        color_estado = colors.green if es_optimo else colors.red

        # Indicador visual del estado
        c.setFillColor(color_estado)
        c.rect(inch, height - inch - 85, 12, 12, fill=True, stroke=False)
        c.setFillColor(colors.black)
        c.drawString(inch + 20, height - inch - 83, f"Condición acústica: {estado}")

        # Explicación educativa
        tooltip_text = (
            "El tiempo de reverberación medio (Tr MID) se calcula promediando los valores a 500 Hz, 1000 Hz y 2000 Hz, "
            "frecuencias donde se concentra la mayor energía del habla humana. En ambientes educativos, "
            "un Tr MID ≤ 0.8 s es ideal para asegurar que las palabras se comprendan con claridad y no se solapen con los ecos del ambiente. "
            "Este criterio se basa en la normativa internacional BUILDING BULLETIN 93 (BB93)."
        )

        text = c.beginText()
        text.setTextOrigin(inch, height - inch - 130)
        text.setFont("Helvetica", 11)
        text.setLeading(16)
        for linea in tooltip_text.split('. '):
            text.textLine(linea.strip() + ('.' if not linea.strip().endswith('.') else ''))
        c.drawText(text)

        # Conclusión clara y resaltada
        conclusion = (
            "La condición acústica de este salón es óptima, ya que el Tr MID se encuentra dentro del rango recomendado (≤ 0.8 s) "
            "para aulas de clase según el estándar BUILDING BULLETIN 93 (BB93). "
            "Esto garantiza una adecuada inteligibilidad del habla y confort auditivo durante las actividades académicas."
            if es_optimo else
            "La condición acústica de este salón no es óptima, debido a que el Tr MID supera el límite máximo permitido de 0.8 segundos. "
            "Esto puede afectar la claridad del habla y disminuir la calidad del entorno de aprendizaje."
        )

        c.setFont("Helvetica-Bold", 12)
        c.drawString(inch, height - inch - 240, "Conclusión:")

        text2 = c.beginText()
        text2.setTextOrigin(inch, height - inch - 265)
        text2.setFont("Helvetica", 11)
        text2.setLeading(16)
        for linea in conclusion.split('. '):
            text2.textLine(linea.strip() + ('.' if not linea.strip().endswith('.') else ''))
        c.drawText(text2)

        c.showPage()
        c.save()

