#import QBuffer
from PySide6.QtCore import QBuffer, QSize, QEvent
from PySide6.QtGui import QPixmap, Qt, QIcon, QColor, QBrush
from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QSizePolicy, QFrame, QVBoxLayout, QHBoxLayout,
    QBoxLayout, QLabel, QHeaderView, QAbstractItemView,
)
from Datos.utils.reportePDF import ReportePDF
from Vista.archivos_pyGenerados.vistaGraficaRT import Ui_formGraficoRT
from Recursos.estilos import paleta, tipografia
from Recursos.estilos.estilo import (
    estiloBotonAtras, estiloBarraSuperior, estiloBarraInferior,
    estiloTarjeta, estiloTexto,
)

# Por debajo de este ancho de ventana el gráfico y el panel de resultados se
# apilan (gráfico arriba, panel abajo) en vez de ir lado a lado.
_ANCHO_APILAR = 1100
# Por debajo de este ancho el pie de página usa botones compactos.
_ANCHO_PIE_COMPACTO = 560

# Bandas cuyo promedio da el Tr MID (se resaltan también en la tabla).
_BANDAS_TR_MID = (500, 1000, 2000)

_ALTO_FILA_TABLA = 30

_ICONO_OPTIMO = "../Recursos/iconos/controlar.png"
_ICONO_NO_OPTIMO = "../Recursos/iconos/cruz.png"
# Mismos iconos que identifican a cada módulo en "Iniciar análisis".
_ICONO_TIEMPO_REVERBERACION = "../Recursos/iconos/ondas-de-audio.png"
_ICONO_INTELIGIBILIDAD = "../Recursos/iconos/terapia-musical.png"


def _rgba(color_hex, alfa):
    c = QColor(color_hex)
    return f"rgba({c.red()},{c.green()},{c.blue()},{alfa})"


class VentanaGraficaRT(QWidget):
    """
    Esta clase representa la ventana de "Tiempo de Reverberacion".
    Es una subclase de QWidget que carga el diseño de iniciarAnalisis.
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None, resultados=None):
        super().__init__(parent)
        self.ui = Ui_formGraficoRT()
        self.ui.setupUi(self)
        self._pixmap_grafica_original = None
        self._apilado = None
        self._pie_compacto = None

        self.indice_anterior = indice_anterior
        self.resultados = resultados
        self.stacked_widget = stacked_widget

        self._configurar_cabecera()
        self._configurar_barra_inferior()
        self._configurar_distribucion()
        self._construir_panel_resultados()

        # El tamaño real de self.ui.grafica solo queda definitivo después
        # de que el layout (anidado dentro del QScrollArea) termina de
        # recalcularse; escuchamos el resizeEvent del propio QLabel en
        # vez del de la ventana para reescalar siempre con el tamaño final.
        self.ui.grafica.installEventFilter(self)

        # El acordeón heredado (tollboxCombinada) ya no se muestra; se
        # mantienen sus títulos sin emojis por coherencia.
        self.ui.tollboxCombinada.setItemText(0, "Tiempo de Reverberación")
        self.ui.tollboxCombinada.setItemText(1, "Inteligibilidad de la Palabra")

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
        self._ajustar_disposicion()

    # ── Construcción visual ─────────────────────────────────────────────

    def _configurar_cabecera(self):
        """Barra superior con el mismo lenguaje que la del formulario de RT."""
        ui = self.ui
        ui.frameTop.setStyleSheet(estiloBarraSuperior("frameTop"))
        ui.frameTop.setMinimumHeight(72)
        ui.horizontalLayout_2.setContentsMargins(12, 8, 12, 8)

        ui.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))
        ui.botonAtras.setMinimumSize(QSize(42, 42))
        ui.botonAtras.setMaximumSize(QSize(42, 42))
        ui.botonAtras.setIconSize(QSize(22, 22))
        ui.botonAtras.setStyleSheet(estiloBotonAtras)
        ui.botonAtras.setToolTip("Volver al formulario")

        subtitulo = "Tiempo de Reverberación · Sabine y Eyring"
        aulas = (self.resultados or {}).get("salon", {}).get("aulas")
        if aulas:
            subtitulo += f" · Aula {aulas}"
        ui.label.setStyleSheet("QLabel { background: transparent; border: none; }")
        ui.label.setText(
            '<html><body><p align="center">'
            f'<span style="font-size:{tipografia.TITULO_PANTALLA}pt; font-weight:700; color:#ffffff;">'
            'Resultados del análisis</span><br>'
            f'<span style="font-size:{tipografia.AUXILIAR}pt; color:{paleta.TEXTO_SECUNDARIO};">'
            f'{subtitulo}</span></p></body></html>'
        )

    def _configurar_barra_inferior(self):
        """
        Barra inferior como la del formulario: "Ir al Inicio" es la acción
        secundaria y "Guardar Reporte PDF" la principal (acento azul).
        """
        ui = self.ui
        ui.frameBottom.setStyleSheet(estiloBarraInferior("frameBottom", "botonGuardarPDF"))
        ui.horizontalLayout_3.setContentsMargins(16, 8, 16, 8)
        ui.horizontalLayout_3.setSpacing(12)
        # El espaciador venía con un ancho preferido de 512 px que, en
        # ventanas angostas, comprimía los botones antes que a sí mismo.
        ui.horizontalSpacer_3.changeSize(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        ui.horizontalLayout_3.invalidate()
        ui.botonGoHome.setToolTip("Volver a la pantalla principal")
        ui.botonGuardarPDF.setToolTip("Guardar el reporte completo en un archivo PDF")

    def _configurar_distribucion(self):
        """
        Distribución responsiva: la barra superior e inferior mantienen su
        alto natural (stretch 0) y todo el espacio sobrante es para el
        contenido. Gráfico | panel de resultados (3:2), apilados si la
        ventana es angosta (ver _ajustar_disposicion).
        """
        ui = self.ui
        ui.verticalLayout_2.setStretch(0, 0)
        ui.verticalLayout_2.setStretch(1, 1)
        ui.verticalLayout_2.setStretch(2, 0)

        ui.frameMedium.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ui.horizontalLayout.setContentsMargins(16, 16, 16, 16)
        ui.horizontalLayout.setSpacing(16)

        ui.frameGrafica.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Centrado vertical: si el panel de resultados crece, el gráfico se
        # mantiene equilibrado respecto al contenido en vez de quedar pegado
        # arriba. La altura del gráfico sigue a su ancho (ver
        # _ajustar_alto_grafica), así que el layout solo reparte el espacio libre.
        ui.horizontalLayout.setAlignment(ui.frameGrafica, Qt.AlignVCenter)
        ui.frameGrafica.setStyleSheet(estiloTarjeta("frameGrafica"))
        ui.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        ui.verticalLayout_8.setSpacing(0)
        ui.grafica.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Ancho mínimo explícito: sin él, un QLabel con pixmap no puede
        # encogerse por debajo del tamaño de la imagen ya cargada.
        ui.grafica.setMinimumWidth(200)
        ui.grafica.setStyleSheet("QLabel { background: white; border: none; }")

        ui.frame_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ui.frame_2.setMinimumSize(QSize(320, 0))
        ui.frame_2.setStyleSheet("")
        ui.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        ui.verticalLayout_3.setSpacing(0)

    @staticmethod
    def _tarjeta(nombre, layout_cls=QVBoxLayout, margenes=(16, 12, 16, 14), espaciado=8, **estilo):
        frame = QFrame()
        frame.setObjectName(nombre)
        frame.setStyleSheet(estiloTarjeta(nombre, **estilo))
        layout = layout_cls(frame)
        layout.setContentsMargins(*margenes)
        layout.setSpacing(espaciado)
        return frame, layout

    @staticmethod
    def _etiqueta(texto, tamano_pt, color=paleta.TEXTO_PRINCIPAL, negrita=False):
        lbl = QLabel(texto)
        lbl.setStyleSheet(estiloTexto(tamano_pt, color, negrita))
        lbl.setWordWrap(True)
        return lbl

    @staticmethod
    def _separador():
        """Línea divisoria fina entre las partes de un mismo bloque."""
        linea = QFrame()
        linea.setFixedHeight(1)
        linea.setStyleSheet("QFrame { background-color: rgba(255,255,255,0.10); border: none; }")
        return linea

    def _cabecera_seccion(self, icono, titulo):
        """Encabezado de sección: icono del módulo + nombre. Devuelve (layout, icono, título)."""
        fila = QHBoxLayout()
        fila.setSpacing(8)
        lbl_icono = QLabel()
        lbl_icono.setStyleSheet("QLabel { background: transparent; border: none; }")
        lbl_icono.setPixmap(QIcon(icono).pixmap(QSize(20, 20)))
        lbl_titulo = self._etiqueta(titulo, tipografia.SUBTITULO, "white", negrita=True)
        lbl_titulo.setWordWrap(False)
        fila.addWidget(lbl_icono)
        fila.addWidget(lbl_titulo, 1)
        return fila, lbl_icono, lbl_titulo

    def _construir_panel_resultados(self):
        """
        Reemplaza el acordeón "Tiempo de Reverberación / Inteligibilidad"
        (que abría en la pestaña de Inteligibilidad y dejaba oculto el
        resultado principal) por dos bloques:

          1) Tiempo de Reverberación: UN solo bloque que agrupa veredicto,
             Tr MID (Sabine y Eyring), tabla por banda y conclusión, para que
             se lea como un único resultado.
          2) Inteligibilidad del Habla: bloque independiente debajo.

        Se reutilizan los widgets ya existentes (tableRT, labelIndicador,
        indicador, labelResumeSabine, labelConclusion, labelAlcons,
        labelEvaluacion); solo cambia su contenedor.
        """
        ui = self.ui
        ui.stackedWidget.hide()

        panel = QWidget()
        panel.setObjectName("panelResultados")
        panel.setStyleSheet("QWidget#panelResultados { background: transparent; }")
        col = QVBoxLayout(panel)
        col.setContentsMargins(0, 0, 0, 0)
        col.setSpacing(16)
        self._panel_resultados = panel
        ui.verticalLayout_3.addWidget(panel)

        # ── 1) Tiempo de Reverberación (bloque principal) ────────────────
        tarjeta_tr, lay_tr = self._tarjeta("tarjetaTR", margenes=(16, 14, 16, 16), espaciado=12)
        cabecera_tr, _, _ = self._cabecera_seccion(_ICONO_TIEMPO_REVERBERACION, "Tiempo de Reverberación")
        lay_tr.addLayout(cabecera_tr)

        # Veredicto de la condición acústica (banda tintada según el estado)
        self._tarjeta_estado, fila = self._tarjeta(
            "tarjetaEstado", QHBoxLayout, margenes=(14, 12, 14, 12), espaciado=14)
        ui.indicador.setFixedSize(QSize(46, 46))
        icono_lay = QHBoxLayout(ui.indicador)
        icono_lay.setContentsMargins(0, 0, 0, 0)
        self._icono_estado = QLabel()
        self._icono_estado.setAlignment(Qt.AlignCenter)
        self._icono_estado.setStyleSheet("QLabel { background: transparent; border: none; }")
        icono_lay.addWidget(self._icono_estado)
        fila.addWidget(ui.indicador)
        texto = QVBoxLayout()
        texto.setSpacing(0)
        texto.addWidget(self._etiqueta("Condición acústica", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        texto.addWidget(ui.labelIndicador)
        texto.addWidget(self._etiqueta("Criterio: Tr MID ≤ 0.8 s en Sabine y Eyring (BB93)",
                                       tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        fila.addLayout(texto, 1)
        lay_tr.addWidget(self._tarjeta_estado)

        # Tr MID (Sabine y Eyring)
        ui.labelResumeSabine.setStyleSheet(estiloTexto(tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        ui.labelResumeSabine.setWordWrap(True)
        lay_tr.addWidget(ui.labelResumeSabine)
        tiles = QHBoxLayout()
        tiles.setSpacing(12)
        self.labelTrMidSabine = self._tile_trmid(tiles, "tileSabine", "Sabine", paleta.SERIE_SABINE)
        self.labelTrMidEyring = self._tile_trmid(tiles, "tileEyring", "Eyring", paleta.SERIE_EYRING)
        lay_tr.addLayout(tiles)

        # Tabla por banda de frecuencia
        lay_tr.addWidget(self._separador())
        lay_tr.addWidget(self._etiqueta("Tiempo de reverberación por banda",
                                        tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        lay_tr.addWidget(ui.tableRT)

        # Conclusión
        lay_tr.addWidget(self._separador())
        lay_tr.addWidget(self._etiqueta("Conclusión", tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        lay_tr.addWidget(ui.labelConclusion)
        col.addWidget(tarjeta_tr)

        # ── 2) Inteligibilidad del Habla (bloque independiente) ──────────
        self._tarjeta_ih, lay_ih = self._tarjeta("tarjetaIH", margenes=(16, 14, 16, 16), espaciado=10)
        cab_ih, self._icono_ih, self._titulo_ih = self._cabecera_seccion(
            _ICONO_INTELIGIBILIDAD, "Inteligibilidad del Habla")
        lay_ih.addLayout(cab_ih)
        lay_ih.addWidget(ui.labelAlcons)
        lay_ih.addWidget(ui.labelEvaluacion)
        col.addWidget(self._tarjeta_ih)

        col.addStretch(1)

    def _tile_trmid(self, layout, nombre, titulo, color_serie):
        """Mosaico con un Tr MID; el borde izquierdo repite el color de su curva en el gráfico."""
        tile = QFrame()
        tile.setObjectName(nombre)
        tile.setStyleSheet(
            f"QFrame#{nombre} {{ background-color: rgba(255,255,255,0.05); border: none; "
            f"border-left: 3px solid {color_serie}; border-radius: 4px; }}"
        )
        lay = QVBoxLayout(tile)
        lay.setContentsMargins(12, 8, 12, 8)
        lay.setSpacing(0)
        lay.addWidget(self._etiqueta(titulo, tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
        valor = self._etiqueta("", tipografia.VALOR, "white", negrita=True)
        valor.setWordWrap(False)
        lay.addWidget(valor)
        layout.addWidget(tile, 1)
        return valor

    # ── Disposición según el ancho ──────────────────────────────────────

    def _ajustar_disposicion(self):
        """
        Ventana ancha: gráfico | panel. Ventana angosta: gráfico arriba y
        panel debajo (antes el gráfico quedaba en miniatura ilegible y el
        panel cortado). En ventanas muy angostas el pie usa botones
        compactos para que no desborden.
        """
        ui = self.ui
        apilar = self.width() < _ANCHO_APILAR
        if apilar != self._apilado:
            self._apilado = apilar
            ui.horizontalLayout.setDirection(
                QBoxLayout.TopToBottom if apilar else QBoxLayout.LeftToRight)
            ui.horizontalLayout.setStretchFactor(ui.frameGrafica, 0 if apilar else 5)
            ui.horizontalLayout.setStretchFactor(ui.frame_2, 0 if apilar else 3)

        compacto = self.width() < _ANCHO_PIE_COMPACTO
        if compacto != self._pie_compacto:
            self._pie_compacto = compacto
            ui.frameBottom.setStyleSheet(
                estiloBarraInferior("frameBottom", "botonGuardarPDF", compacto=compacto))

        self._ajustar_alto_grafica()

    def _ajustar_alto_grafica(self):
        """
        La altura del gráfico sigue a su ancho (misma relación de aspecto que
        la imagen): así no queda una losa blanca alrededor cuando el panel de
        resultados es más alto que el gráfico.
        """
        pix = self._pixmap_grafica_original
        if pix is None or pix.width() <= 0:
            return
        alto = max(int(self.ui.grafica.width() * pix.height() / pix.width()), 150)
        if self.ui.grafica.height() != alto or self.ui.grafica.maximumHeight() != alto:
            self.ui.grafica.setFixedHeight(alto)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._ajustar_disposicion()

    # ── Eventos ─────────────────────────────────────────────────

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

        self.ui.grafica.setAlignment(Qt.AlignCenter)
        self.ui.grafica.setScaledContents(False)

        # Guardamos el pixmap original (sin escalar) para poder
        # reescalarlo cada vez que cambie el tamaño real disponible,
        # en vez de fijarlo a una altura constante.
        self._pixmap_grafica_original = pixmap
        self._ajustar_alto_grafica()
        self._actualizar_pixmap_grafica()

    def _actualizar_pixmap_grafica(self):
        """
        Reescala la gráfica ya generada al tamaño real disponible del
        QLabel, conservando su relación de aspecto (sin deformarla).
        Se llama al mostrar la gráfica y cada vez que el QLabel cambia
        de tamaño (ver eventFilter).
        """
        if self._pixmap_grafica_original is None:
            return

        tamano_disponible = self.ui.grafica.size()
        if tamano_disponible.width() <= 0 or tamano_disponible.height() <= 0:
            return

        pixmap_escalado = self._pixmap_grafica_original.scaled(
            tamano_disponible, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.ui.grafica.setPixmap(pixmap_escalado)

    def eventFilter(self, obj, event):
        if obj is self.ui.grafica and event.type() == QEvent.Resize:
            self._ajustar_alto_grafica()
            self._actualizar_pixmap_grafica()
        return super().eventFilter(obj, event)

    def llenar_tabla_resultados(self):
        """
        Llena la tabla de resultados con las frecuencias y los valores de Sabine y Eyring,
        centrando el contenido y asegurando que no haya scroll. Las bandas que
        alimentan el Tr MID (500, 1000 y 2000 Hz) se resaltan.
        """
        # Datos de Sabine y Eyring
        sabine = self.resultados.get("sabine_rt", {})
        eyring = self.resultados.get("eyring_rt", {})
        frecuencias = sorted(sabine.keys())  # Ordenar las frecuencias de menor a mayor

        tabla = self.ui.tableRT
        color = QColor(paleta.ACENTO)
        color.setAlpha(34)
        resaltado = QBrush(color)

        # Configurar tabla
        tabla.setRowCount(len(frecuencias))
        tabla.setColumnCount(3)
        tabla.setHorizontalHeaderLabels(["Frecuencia (Hz)", "Sabine RT (s)", "Eyring RT (s)"])

        for row, frecuencia in enumerate(frecuencias):
            # Celda de Frecuencia
            item_frecuencia = QTableWidgetItem(str(frecuencia))
            item_frecuencia.setTextAlignment(Qt.AlignCenter)  # Centrar texto
            tabla.setItem(row, 0, item_frecuencia)

            # Celda Sabine RT
            item_sabine = QTableWidgetItem(f"{sabine[frecuencia]:.2f}")
            item_sabine.setTextAlignment(Qt.AlignCenter)  # Centrar texto
            tabla.setItem(row, 1, item_sabine)

            # Celda Eyring RT
            item_eyring = QTableWidgetItem(f"{eyring.get(frecuencia, 0):.2f}")
            item_eyring.setTextAlignment(Qt.AlignCenter)  # Centrar texto
            tabla.setItem(row, 2, item_eyring)

            if frecuencia in _BANDAS_TR_MID:
                for col in range(3):
                    tabla.item(row, col).setBackground(resaltado)

        # Solo lectura, sin selección ni foco: es una tabla de resultados.
        tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tabla.setSelectionMode(QAbstractItemView.NoSelection)
        tabla.setFocusPolicy(Qt.NoFocus)
        tabla.setShowGrid(True)
        tabla.setFrameShape(QFrame.NoFrame)
        tabla.setStyleSheet(
            f"""
            QTableWidget {{
                background: transparent; border: none; color: white;
                font-size: {tipografia.CUERPO}pt;
                gridline-color: rgba(255,255,255,0.10);
            }}
            QHeaderView {{ background: transparent; }}
            QHeaderView::section {{
                background-color: rgba(255,255,255,0.10); color: white;
                font-weight: bold; font-size: {tipografia.AUXILIAR + 1}pt;
                border: none; padding: 4px;
            }}
            """
        )

        # Columnas repartidas en el ancho de la tarjeta; alto exacto para que
        # quepa todo sin scroll (la tabla no crece más allá de sus filas).
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabla.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        tabla.horizontalHeader().setFixedHeight(_ALTO_FILA_TABLA + 4)
        tabla.verticalHeader().setVisible(False)
        tabla.verticalHeader().setDefaultSectionSize(_ALTO_FILA_TABLA)
        for row in range(tabla.rowCount()):
            tabla.setRowHeight(row, _ALTO_FILA_TABLA)

        tabla.setFixedHeight(_ALTO_FILA_TABLA + 4 + _ALTO_FILA_TABLA * tabla.rowCount() + 2)
        tabla.setMinimumWidth(260)
        tabla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Desactivar las barras de scroll
        tabla.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        tabla.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def mostrar_info(self):
        sabine = self.resultados.get("sabine_rt")
        eyring = self.resultados.get("eyring_rt")

        # Extraer solo las frecuencias clave para Tr MID
        frecuencias_mid = list(_BANDAS_TR_MID)

        # Asegurarte de que existan en los resultados
        sabine_mid = [sabine[f] for f in frecuencias_mid if f in sabine]
        eyring_mid = [eyring[f] for f in frecuencias_mid if f in eyring]

        # Calcular los promedios Tr MID
        trmid_sabine = sum(sabine_mid) / len(sabine_mid) if sabine_mid else 0
        trmid_eyring = sum(eyring_mid) / len(eyring_mid) if eyring_mid else 0

        # Mostrar Tr MID (dos mosaicos con la cifra destacada)
        self.ui.labelResumeSabine.setText(
            "Tr MID · promedio de 500, 1000 y 2000 Hz (bandas resaltadas en la tabla)")
        self.labelTrMidSabine.setText(f"{trmid_sabine:.2f} s")
        self.labelTrMidEyring.setText(f"{trmid_eyring:.2f} s")

        # Evaluar si es óptimo
        es_optimo = trmid_sabine <= 0.8 and trmid_eyring <= 0.8

        # El estado se comunica con color + icono (✓ / ✗) + texto, para no
        # depender solo del color.
        color = paleta.ESTADO_OPTIMO if es_optimo else paleta.ESTADO_NO_OPTIMO
        self._tarjeta_estado.setStyleSheet(
            estiloTarjeta("tarjetaEstado", fondo=_rgba(color, 0.10), borde=_rgba(color, 0.45)))
        self.ui.indicador.setStyleSheet(
            f"QFrame#indicador {{ background-color: {_rgba(color, 0.22)}; "
            f"border: 2px solid {color}; border-radius: 23px; }}")
        self._icono_estado.setPixmap(
            QIcon(_ICONO_OPTIMO if es_optimo else _ICONO_NO_OPTIMO).pixmap(QSize(22, 22)))
        self.ui.labelIndicador.setText("ÓPTIMA" if es_optimo else "NO ÓPTIMA")
        self.ui.labelIndicador.setStyleSheet(estiloTexto(tipografia.VALOR, color, negrita=True))

        tooltip_text = (
            "El tiempo de reverberación medio (Tr MID) se calcula promediando los valores de 500 Hz, 1000 Hz y 2000 Hz, "
            "ya que estas frecuencias contienen la mayor energía de la voz humana. Según los estándares acústicos, "
            "el Tr MID en aulas debe ser menor o igual a 0.8 segundos para garantizar una buena inteligibilidad del habla."
        )

        self._tarjeta_estado.setToolTip(tooltip_text)
        self.ui.frameIndicador.setToolTip(tooltip_text)

        #conclusion
        self.ui.labelConclusion.setWordWrap(True)  # Para que se ajuste al tamaño del QLabel
        self.ui.labelConclusion.setStyleSheet(estiloTexto(tipografia.CUERPO))

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

        self.ui.labelAlcons.setTextFormat(Qt.RichText)
        self.ui.labelEvaluacion.setTextFormat(Qt.RichText)
        self.ui.labelEvaluacion.setWordWrap(True)
        self.ui.labelAlcons.setWordWrap(True)

        if reporte==None:
            # No aplicada: nota discreta al final del panel, sin cifra
            # grande ni borde de acento, para no competir con el RT.
            self._tarjeta_ih.setStyleSheet(
                estiloTarjeta("tarjetaIH", fondo="transparent", borde="rgba(255,255,255,0.12)"))
            self._icono_ih.setEnabled(False)
            self._titulo_ih.setStyleSheet(estiloTexto(tipografia.SUBTITULO, paleta.TEXTO_SECUNDARIO, negrita=True))
            self.ui.labelAlcons.hide()
            self.ui.labelEvaluacion.setStyleSheet(estiloTexto(tipografia.AUXILIAR, paleta.TEXTO_SECUNDARIO))
            self.ui.labelEvaluacion.setText(
                "No calculada: la opción no se activó en el formulario. "
                "Puede volver atrás y activarla para incluir el %ALCONS en el reporte."
            )
        else:
            alcons = reporte["%ALCONS"]
            evaluacion = reporte["Evaluación"].strip()
            categoria, sep, detalle = evaluacion.partition(":")

            self._tarjeta_ih.setStyleSheet(estiloTarjeta("tarjetaIH"))
            self._icono_ih.setEnabled(True)
            self._titulo_ih.setStyleSheet(estiloTexto(tipografia.SUBTITULO, "white", negrita=True))
            self.ui.labelAlcons.show()
            self.ui.labelAlcons.setStyleSheet(estiloTexto(tipografia.VALOR, "white", negrita=True))
            self.ui.labelAlcons.setText(
                f"{alcons} <span style=\"font-size:{tipografia.CUERPO}pt;\">%ALCONS</span>")
            self.ui.labelEvaluacion.setStyleSheet(estiloTexto(tipografia.CUERPO))
            self.ui.labelEvaluacion.setText(
                f"<b>{categoria}</b>{sep}{detalle}<br><br>"
                f"<span style=\"color:{paleta.TEXTO_SECUNDARIO};\">"
                "Este análisis se basa en la constante del recinto, el volumen del aula y el tiempo de reverberación. "
                "Una menor pérdida de consonantes (%ALCONS bajo) indica mejor claridad del habla en el salón."
                "</span>"
            )
