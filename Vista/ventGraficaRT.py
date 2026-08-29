#import QBuffer
from PySide6.QtCore import QBuffer
from PySide6.QtGui import QPixmap, Qt, QIcon
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from Datos.utils.reportePDF import ReportePDF
from Vista.archivos_pyGenerados.vistaGraficaRT import Ui_formGraficoRT

class VentanaGraficaRT(QWidget):
    """
    Esta clase representa la ventana de "Tiempo de Reverberacion".
    Es una subclase de QWidget que carga el diseño de iniciarAnalisis.
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None, resultados=None):
        super().__init__(parent)
        self.ui = Ui_formGraficoRT()
        self.ui.setupUi(self)

        self.indice_anterior = indice_anterior
        self.resultados = resultados
        self.stacked_widget = stacked_widget

        self.ui.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))

        self.ui.verticalLayout_11.setAlignment(Qt.AlignCenter)
        self.ui.verticalLayout_11.setContentsMargins(10, 10, 10, 10)

        # Suponiendo que tienes un QToolBox llamado "toolBox"
        self.ui.tollboxCombinada.setItemText(0, "🔊 Tiempo de Reverberación")
        self.ui.tollboxCombinada.setItemText(1, "🗣️ Inteligibilidad de la Palabra")

        # Configurar tabla
        self.ui.tableRT.setShowGrid(True)
        self.ui.tableRT.setStyleSheet(
            """
            QTableWidget::item {
                border: 1px solid black;
            }
            QHeaderView::section {
                background-color: lightgray;
                font-weight: bold;
                border: 1px solid black;
            }
            """
        )

        sabine = self.resultados.get("sabine_rt")
        eyring = self.resultados.get("eyring_rt")
        grafica = self.resultados.get("grafica")
        salon = self.resultados.get("salon")
        detalles_rt = self.resultados.get("detalles")
        alcons = self.resultados.get("reporte_inteligibilidad")




        self.setup_events()
        self.mostrar_grafica(grafica)
        self.llenar_tabla_resultados()
        self.mostrar_alcons()
        self.mostrar_info()

    def setup_events(self):
        self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)
        self.ui.botonGoHome.clicked.connect(self.ir_ventana_home)
        self.ui.botonGuardarPDF.clicked.connect(self.importar_pdf)



    def regresar_a_ventana_anterior(self):
        """
        Cambia a la ventana anterior usando el QStackedWidget.
        """
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)

    def ir_ventana_home(self):
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(0)
    def importar_pdf(self):
        self.crear_pdf(self.resultados)

    def crear_pdf(self, resultado):
        ReportePDF.reporte_tiempo_reverberacion(self, resultado)


    def mostrar_grafica(self, grafica):
        # Convertir el grafico de BytesIO a QPixmap (compatible con PyQt5)
        buffer_qt = QBuffer()
        buffer_qt.setData(grafica.read())
        grafica.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer_qt.data())

        # Definir tamaño deseado (puedes cambiar el alto o el ancho según prefieras)
        alto_deseado = 450
        ancho_escala = int(pixmap.width() * (alto_deseado / pixmap.height()))

        # Escalar manteniendo proporción
        pixmap_escalado = pixmap.scaled(
            ancho_escala, alto_deseado, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        self.ui.grafica.setPixmap(pixmap_escalado)
        self.ui.grafica.setAlignment(Qt.AlignCenter)
        self.ui.grafica.setScaledContents(False)

    def llenar_tabla_resultados(self):
        """
        Llena la tabla de resultados con las frecuencias y los valores de Sabine y Eyring,
        centrando el contenido y asegurando que no haya scroll.
        """
        # Datos de Sabine y Eyring
        sabine = self.resultados.get("sabine_rt", {})
        eyring = self.resultados.get("eyring_rt", {})
        frecuencias = sorted(sabine.keys())  # Ordenar las frecuencias de menor a mayor

        # Configurar tabla
        self.ui.tableRT.setRowCount(len(frecuencias))
        self.ui.tableRT.setColumnCount(3)
        self.ui.tableRT.setHorizontalHeaderLabels(["Frecuencia (Hz)", "Sabine RT (s)", "Eyring RT (s)"])

        for row, frecuencia in enumerate(frecuencias):
            # Celda de Frecuencia
            item_frecuencia = QTableWidgetItem(str(frecuencia))
            item_frecuencia.setTextAlignment(Qt.AlignCenter)  # Centrar texto
            self.ui.tableRT.setItem(row, 0, item_frecuencia)

            # Celda Sabine RT
            item_sabine = QTableWidgetItem(f"{sabine[frecuencia]:.2f}")
            item_sabine.setTextAlignment(Qt.AlignCenter)  # Centrar texto
            self.ui.tableRT.setItem(row, 1, item_sabine)

            # Celda Eyring RT
            item_eyring = QTableWidgetItem(f"{eyring.get(frecuencia, 0):.2f}")
            item_eyring.setTextAlignment(Qt.AlignCenter)  # Centrar texto
            self.ui.tableRT.setItem(row, 2, item_eyring)

        # Ajustar tamaño de las columnas y las filas al contenido
        self.ui.tableRT.resizeColumnsToContents()
        self.ui.tableRT.resizeRowsToContents()



        # Calcular altura exacta para que quepa todo sin scroll
        total_height = (
                self.ui.tableRT.horizontalHeader().height() +
                sum([self.ui.tableRT.rowHeight(i) for i in range(self.ui.tableRT.rowCount())]) +
                2  # Margen extra
        )
        self.ui.tableRT.setMinimumHeight(total_height+40)
        self.ui.tableRT.setMaximumHeight(total_height+40)

        # Calcular ancho total para que se vea completa
        total_width = (
                sum([self.ui.tableRT.columnWidth(c) for c in range(self.ui.tableRT.columnCount())]) +
                self.ui.tableRT.verticalHeader().width() +
                2  # Margen extra
        )
        self.ui.tableRT.setMinimumWidth(total_width+40)
        self.ui.tableRT.setMaximumWidth(total_width+40)

        # Desactivar las barras de scroll
        self.ui.tableRT.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tableRT.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.tableRT.horizontalHeader().setFixedHeight(40)
        self.ui.tableRT.verticalHeader().setVisible(False)

        self.ui.tableRT.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.ui.verticalLayout_11.setAlignment(self.ui.tableRT, Qt.AlignCenter)

        # Mostrar encabezado de columnas
        #self.ui.tableRT.horizontalHeader().setVisible(True)

    def mostrar_info(self):
        sabine = self.resultados.get("sabine_rt")
        eyring = self.resultados.get("eyring_rt")

        # Extraer solo las frecuencias clave para Tr MID
        frecuencias_mid = [500, 1000, 2000]

        # Asegurarte de que existan en los resultados
        sabine_mid = [sabine[f] for f in frecuencias_mid if f in sabine]
        eyring_mid = [eyring[f] for f in frecuencias_mid if f in eyring]

        # Calcular los promedios Tr MID
        trmid_sabine = sum(sabine_mid) / len(sabine_mid) if sabine_mid else 0
        trmid_eyring = sum(eyring_mid) / len(eyring_mid) if eyring_mid else 0

        # Mostrar en un QLabel
        self.ui.labelResumeSabine.setText(f"Tr MID Sabine: {trmid_sabine:.2f} s\nTr MID Eyring: {trmid_eyring:.2f} s")

        # Evaluar si es óptimo
        es_optimo = trmid_sabine <= 0.8 and trmid_eyring <= 0.8

        if es_optimo:
            self.ui.labelIndicador.setText("Condición acústica: ÓPTIMA")
            self.ui.indicador.setStyleSheet("background-color: #4CAF50; border-radius: 5px;")  # Verde
        else:
            self.ui.labelIndicador.setText("Condición acústica: NO ÓPTIMA")
            self.ui.indicador.setStyleSheet("background-color: #F44336; border-radius: 5px;")  # Rojo

        tooltip_text = (
            "El tiempo de reverberación medio (Tr MID) se calcula promediando los valores de 500 Hz, 1000 Hz y 2000 Hz, "
            "ya que estas frecuencias contienen la mayor energía de la voz humana. Según los estándares acústicos, "
            "el Tr MID en aulas debe ser menor o igual a 0.8 segundos para garantizar una buena inteligibilidad del habla."
        )

        self.ui.frameIndicador.setToolTip(tooltip_text)
        self.ui.labelResumeSabine.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                padding: 8px;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
        """)

        # Estilo para el QLabel del resultado óptimo/no óptimo
        self.ui.labelIndicador.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: black;
                padding: 8px;
                border-radius: 6px;
            }
        """)

        #conclusion
        self.ui.labelConclusion.setWordWrap(True)  # Para que se ajuste al tamaño del QLabel
        self.ui.labelConclusion.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                padding: 8px;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
        """)

        # Mostrar conclusión según el resultado
        if es_optimo:
            self.ui.labelConclusion.setText(
                "<b>La condición acústica de este salón es óptima</b>, ya que el Tiempo de Reverberación medio (Tr MID) "
                "se encuentra dentro del rango recomendado (≤ 0.8 s) para aulas de clase según el estándar "
                "<b>BUILDING BULLETIN 93 (BB93)</b>. "
                "Esto garantiza una adecuada inteligibilidad del habla y confort auditivo durante las actividades académicas."
            )
        else:
            self.ui.labelConclusion.setText(
                "<b>La condición acústica de este salón no es óptima</b>, debido a que el Tiempo de Reverberación medio (Tr MID) "
                "supera el límite máximo permitido de 0.8 segundos, establecido por el estándar "
                "<b>BUILDING BULLETIN 93 (BB93)</b> para espacios educativos. "
                "Esto puede afectar la claridad del habla y disminuir la calidad del entorno de aprendizaje."
            )
    def mostrar_alcons(self):

        reporte = self.resultados.get("reporte_inteligibilidad")

        self.ui.labelAlcons.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente
        self.ui.labelAlcons.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333;
            }
        """)
        self.ui.labelEvaluacion.setTextFormat(Qt.RichText)
        self.ui.labelAlcons.setTextFormat(Qt.RichText)
        self.ui.labelEvaluacion.setWordWrap(True)
        self.ui.labelAlcons.setWordWrap(True)

        if reporte==None:

            self.ui.labelEvaluacion.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    color: #555;
                    padding: 10px;
                    background-color: #fff3cd;
                    border: 1px solid #ffeeba;
                    border-radius: 8px;
                }
            """)
            self.ui.labelAlcons.setText("⚠️ <b>Inteligibilidad no aplicada</b><br><br>")
            self.ui.labelEvaluacion.setText(
                "No se seleccionó la opción de calcular la inteligibilidad para esta aula de clases. "
                "Si lo desea, puede <b>regresar</b> e ingresar los datos faltantes para realizar el análisis correspondiente."
            )
        else:
            alcons = reporte["%ALCONS"]
            evaluacion = reporte["Evaluación"]

            self.ui.labelEvaluacion.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    color: #2e2e2e;
                    padding: 12px;
                    background-color: #e8f5e9;
                    border: 1px solid #c8e6c9;
                    border-radius: 8px;
                }
            """)

            self.ui.labelAlcons.setText(f"🔊 <b>%ALCONS:</b> {alcons}%<br>")
            self.ui.labelEvaluacion.setText(
                f"🗣️ <b>Inteligibilidad de la palabra</b><br><br>"
                f"📊 <b>Evaluación:</b> {evaluacion}<br><br>"
                "Este análisis se basa en la constante del recinto, el volumen del aula y el tiempo de reverberación. "
                "Una menor pérdida de consonantes (%ALCONS bajo) indica mejor claridad del habla en el salón."
            )

















