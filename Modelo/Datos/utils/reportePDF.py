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
        if not nombre_archivo:
            return

        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter
        margin = inch

        salon = resultados.get("salon", {})
        dimensiones = salon.get("dimensiones", {})
        largo = dimensiones.get("largo", "N/A")
        ancho = dimensiones.get("ancho", "N/A")
        altura = dimensiones.get("altura", "N/A")
        alcons = resultados.get("reporte_inteligibilidad")
        materiales = salon.get("materiales", {})

        def obtener_materiales_y_objetos(materiales):
            resumen = []
            for superficie, datos in materiales.items():
                material = datos.get("material", "N/A")
                area = datos.get("area", "N/A")
                objetos = datos.get("objetos_adheridos") or []
                resumen.append(f"{superficie}: {area} m² - Material: {material}")
                if objetos:
                    for obj in objetos:
                        resumen.append(f"    - {obj['nombre']} ({obj['material']}), Área: {obj['area']} m²")
            return resumen

        materiales_resumen = obtener_materiales_y_objetos(materiales)
        objetos_adicionales = salon.get("objetos_adicionales") or []
        objetos_resumen = ", ".join(
            [f"{obj['cantidad']} {obj['material']} ({obj['nombre']})" for obj in objetos_adicionales])

        # === PÁGINA 1: RESUMEN DEL SALÓN ===
        c.setFont("Helvetica-Bold", 16)
        c.drawString(margin, height - margin, "Resumen del Salón")

        c.setFont("Helvetica", 12)
        y_pos = height - margin - 40
        c.drawString(margin, y_pos, "Dimensiones del salón:")
        y_pos -= 20
        c.drawString(margin, y_pos, f"Largo: {largo} m")
        y_pos -= 20
        c.drawString(margin, y_pos, f"Ancho: {ancho} m")
        y_pos -= 20
        c.drawString(margin, y_pos, f"Altura: {altura} m")

        y_pos -= 40
        c.drawString(margin, y_pos, "Materiales de las superficies:")
        y_pos -= 20
        for item in materiales_resumen:
            c.drawString(margin, y_pos, item)
            y_pos -= 20

        if objetos_resumen:
            y_pos -= 10
            c.drawString(margin, y_pos, f"Objetos adicionales: {objetos_resumen}")

        c.showPage()

        # === PÁGINA 2: GRÁFICA Y TABLA ===
        grafica = resultados.get("grafica")
        if grafica:
            grafica.seek(0)
            imagen = ImageReader(grafica)
            img_width, img_height = imagen.getSize()
            altura_img = 300
            escala = altura_img / img_height
            ancho_img = img_width * escala
            x = (width - ancho_img) / 2
            y = height - altura_img - margin
            c.drawImage(imagen, x, y, width=ancho_img, height=altura_img)
            tabla_top = y - 40
        else:
            tabla_top = height - margin

        sabine = resultados.get("sabine_rt", {})
        eyring = resultados.get("eyring_rt", {})
        frecuencias = sorted(sabine.keys())

        encabezados = ["Frecuencia (Hz)", "Sabine RT (s)", "Eyring RT (s)"]
        col_width = (width - 2 * margin) / len(encabezados)
        row_height = 20
        tabla_left = margin

        c.setFont("Helvetica-Bold", 14)
        c.drawString(tabla_left, tabla_top + 30, "Resultados Numéricos")

        c.setFont("Helvetica-Bold", 10)
        for i, texto in enumerate(encabezados):
            x = tabla_left + i * col_width
            c.setFillColor(colors.lightblue)
            c.rect(x, tabla_top - row_height, col_width, row_height, fill=True, stroke=True)
            c.setFillColor(colors.black)
            c.drawCentredString(x + col_width / 2, tabla_top - row_height + 5, texto)

        c.setFont("Helvetica", 10)
        for fila, f in enumerate(frecuencias):
            y = tabla_top - (fila + 2) * row_height
            valores = [str(f), f"{sabine[f]:.2f}", f"{eyring.get(f, 0):.2f}"]
            for col, val in enumerate(valores):
                x = tabla_left + col * col_width
                c.setFillColor(colors.whitesmoke if fila % 2 == 0 else colors.lightgrey)
                c.rect(x, y, col_width, row_height, fill=True, stroke=True)
                c.setFillColor(colors.black)
                c.drawCentredString(x + col_width / 2, y + 5, val)

        c.showPage()

        # === PÁGINA 3: INTERPRETACIÓN ===
        sabine_mid = [sabine[f] for f in [500, 1000, 2000] if f in sabine]
        eyring_mid = [eyring[f] for f in [500, 1000, 2000] if f in eyring]
        trmid_sabine = sum(sabine_mid) / len(sabine_mid) if sabine_mid else 0
        trmid_eyring = sum(eyring_mid) / len(eyring_mid) if eyring_mid else 0
        es_optimo = trmid_sabine <= 0.8 and trmid_eyring <= 0.8

        c.setFont("Helvetica-Bold", 16)
        c.drawString(margin, height - margin, "Análisis Acústico: Interpretación de Resultados")

        c.setFont("Helvetica", 12)
        c.drawString(margin, height - margin - 30, f"Tr MID Sabine: {trmid_sabine:.2f} s")
        c.drawString(margin, height - margin - 50, f"Tr MID Eyring: {trmid_eyring:.2f} s")

        estado = "ÓPTIMA" if es_optimo else "NO ÓPTIMA"
        color_estado = colors.green if es_optimo else colors.red
        c.setFillColor(color_estado)
        c.rect(margin, height - margin - 85, 12, 12, fill=True, stroke=False)
        c.setFillColor(colors.black)
        c.drawString(margin + 20, height - margin - 83, f"Condición acústica: {estado}")

        tooltip_text = (
            "El tiempo de reverberación medio (Tr MID) se calcula promediando los valores a 500 Hz,"
            " 1000 Hz y 2000 Hz.\n"
            "En ambientes educativos, un Tr MID ≤ 0.8 s es ideal para asegurar que las palabras se "
            "comprendan con claridad.\n"
            "Este criterio se basa en la normativa BUILDING BULLETIN 93 (BB93)."
        )

        text = c.beginText()
        text.setTextOrigin(margin, height - margin - 130)
        text.setFont("Helvetica-Oblique", 9)  # Fuente en cursiva
        text.setLeading(16)

        for linea in tooltip_text.split('\n'):
            text.textLine(linea.strip())

        c.drawText(text)

        conclusion = (
            "La condición acústica de este salón es óptima, ya que el Tr MID se encuentra dentro\n"
            "del rango recomendado (≤ 0.8 s)\n"
            "para aulas de clase. Esto garantiza una adecuada inteligibilidad del habla y confort\n"
            "auditivo.\n"
            if es_optimo else
            "La condición acústica de este salón no es óptima, debido a que el Tr MID supera el\n"
            "límite máximo permitido de 0.8 segundos.\n"
            "Esto puede afectar la claridad del habla y disminuir la calidad del entorno de aprendizaje."
        )

        # Coordenadas y dimensiones del cuadro
        box_x = margin
        box_y = height - margin - 290  # Más bajo para dejar espacio al título
        box_width = width - 2 * margin
        box_height = 90 if es_optimo else 105  # Ajustar altura según texto

        # Fondo del cuadro
        c.setFillColorRGB(0.95, 0.95, 0.85)  # fondo suave tipo beige
        c.roundRect(box_x, box_y, box_width, box_height, 10, fill=1, stroke=0)

        # Borde del cuadro
        c.setStrokeColorRGB(0.7, 0.5, 0.1)  # marrón claro
        c.setLineWidth(1)
        c.roundRect(box_x, box_y, box_width, box_height, 10, fill=0, stroke=1)

        c.setFillColorRGB(0.1, 0.1, 0.1)

        # Título "Conclusión:"
        c.setFont("Helvetica-Bold", 12)
        c.drawString(box_x + 10, box_y + box_height - 15, "Conclusión:")

        # Texto dentro del cuadro
        text2 = c.beginText()
        text2.setTextOrigin(box_x + 10, box_y + box_height - 35)  # margen interior
        text2.setFont("Helvetica", 11)
        text2.setLeading(14)
        for linea in conclusion.split('\n'):
            text2.textLine(linea.strip())

        c.drawText(text2)

        # Nueva página
        c.showPage()
        print(alcons)

        if alcons is not None:
            print("imprimio")


            # Título
            c.setFont("Helvetica-Bold", 14)
            c.setFillColorRGB(0.1, 0.1, 0.1)
            c.drawString(margin, height - margin - 20, "Resultados de la Inteligibilidad - %ALCONS")


            # Cuerpo del texto
            text3 = c.beginText()
            text3.setTextOrigin(margin, height - margin - 60)
            text3.setFont("Helvetica", 11)
            text3.setLeading(18)

            for clave, valor in alcons.items():
                if clave != "Detalles":
                    text3.textLine(f"{clave}: {valor}")
                else:
                    text3.textLine("Detalles:")
                    for subclave, subvalor in valor.items():
                        text3.textLine(f"   - {subclave}: {round(subvalor, 2)}")

            c.drawText(text3)

            c.showPage()

        c.save()







