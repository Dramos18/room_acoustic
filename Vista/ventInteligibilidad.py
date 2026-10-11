
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QFileDialog, QFrame, QVBoxLayout, QLabel,
    QBoxLayout, QScrollArea, QSizePolicy,
)
import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from Datos.utils.reportePDF import ReportePDF
from Modelo.alcons2 import AlconsCalculator
from Vista.archivos_pyGenerados.inteligibilidadHabla import Ui_Form
from Vista.ventResultadosInteligibilidad import VentanaResultadosInteligibilidad
from Recursos.estilos import paleta, tipografia
from Recursos.estilos.estilo import (
    estiloWarning, estiloBotonAtras, estiloBarraSuperior, estiloBarraInferior,
    estiloTexto,
)

# Por debajo de este ancho de ventana, las 3 columnas del formulario (Guía
# de valores / Parámetros / Escala) pasan a disposición vertical. Mismo
# umbral que ya usa VentanaGraficaRT (_ANCHO_APILAR), para un único punto
# de corte coherente en toda la app — ver auditoría de layout del Módulo 2.
_ANCHO_APILAR = 1100

# Alto máximo común de las 3 tarjetas cuando están en disposición
# horizontal (una sola fuente de verdad, no 3 números sueltos). Por encima
# de las sizeHint naturales medidas (hasta ~472 px en la escala de 6
# niveles), con margen; evita que los paneles laterales crezcan sin límite
# en ventanas muy altas.
_ALTURA_COMUN_TARJETAS = 500

# Padding interno unificado de las 3 tarjetas (antes 16/18/16/18 en guía y
# escala, 20/18/20/18 en el formulario: mismo vertical, distinto horizontal).
_PADDING_TARJETA = 18

# Por debajo de este ancho, el pie usa botones compactos — mismo umbral y
# mecanismo que _ANCHO_PIE_COMPACTO en VentanaGraficaRT.
_ANCHO_PIE_COMPACTO = 560

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

        # Cabecera: mismo lenguaje visual que el resto de la app (helpers
        # centralizados en Recursos/estilos/estilo.py, en vez de los
        # estilos sueltos que traía esta pantalla) — ver auditoría UX/UI
        # del Módulo 2, docs/CHANGELOG.md.
        self.ui.frTop1.setStyleSheet(estiloBarraSuperior("frTop1"))
        # Título y subtítulo no ajustaban línea: al llegar a 500 px (soporte
        # real añadido en esta auditoría de layout) quedaban recortados sin
        # ningún aviso. Se habilita el ajuste de línea (mismo texto).
        self.ui.label.setWordWrap(True)
        self.ui.labelSubtitulo.setWordWrap(True)

        # Botón "Atrás": tamaño estándar en toda la app, 42×42 / icono
        # 22×22; estiloBotonAtras ya incluye el border-radius circular.
        self.ui.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))
        self.ui.botonAtras.setMinimumSize(QSize(42, 42))
        self.ui.botonAtras.setMaximumSize(QSize(42, 42))
        self.ui.botonAtras.setIconSize(QSize(22, 22))
        self.ui.botonAtras.setStyleSheet(estiloBotonAtras)

        # "Ir al Inicio" es texto solo, igual que en Módulo 1 (Resultados
        # de RT) y Base de Datos — antes llevaba el chevron de "Atrás",
        # inconsistente con el resto de la app.

        # Pie: estiloBarraInferior ya resuelve ancho/padding/estados
        # pressed/disabled del botón principal ("Iniciar Análisis") y el
        # aspecto secundario de "Ir al Inicio" (no existe en esta pantalla,
        # pero el selector genérico no afecta si no está presente).
        self.ui.frame_bottom.setStyleSheet(
            estiloBarraInferior("frame_bottom", "botonIniciarAnalisis")
        )
        # El espaciador del pie traía un ancho mínimo de 200px (hereda del
        # .ui), que a 500px de ventana por sí solo ya impedía bajar de ahí;
        # mismo fix que ventGraficaRT.py — el espacio se reparte con
        # Expanding en vez de reservar un mínimo fijo.
        self.ui.horizontalSpacer_3.changeSize(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._pie_compacto = None

        # Flechas de los QDoubleSpinBox: el .ui no define
        # ::up-button/::down-button/::up-arrow/::down-arrow, así que Qt usa
        # el control nativo de la plataforma, invisible sobre este fondo
        # oscuro. Mismo fix ya aplicado en Vista/ventTiempoReverberacion.py,
        # con los mismos iconos (angulo-arriba.png/angulo-abajo.png),
        # aplicado aquí a los 5 campos del formulario.
        ruta_flecha_arriba = "../Recursos/iconos/angulo-arriba.png"
        ruta_flecha_abajo = "../Recursos/iconos/angulo-abajo.png"
        self.setStyleSheet(self.styleSheet() + f"""
            QDoubleSpinBox::up-button, QSpinBox::up-button {{
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 16px;
                border: none;
                background: transparent;
            }}
            QDoubleSpinBox::down-button, QSpinBox::down-button {{
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                width: 16px;
                border: none;
                background: transparent;
            }}
            QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {{
                image: url({ruta_flecha_arriba});
                width: 8px;
                height: 8px;
            }}
            QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {{
                image: url({ruta_flecha_abajo});
                width: 8px;
                height: 8px;
            }}
        """)

        # Mensaje de validación inline (no bloqueante), igual que el
        # formulario de RT (labelError/labelErrorDimensiones): sustituye al
        # QMessageBox.Warning genérico que interrumpía el flujo.
        self.ui.labelErrorInteligibilidad = QLabel("")
        self.ui.labelErrorInteligibilidad.setWordWrap(True)
        self.ui.labelErrorInteligibilidad.setStyleSheet(
            estiloTexto(tipografia.AUXILIAR, paleta.ESTADO_NO_OPTIMO, negrita=True)
        )
        self.ui.verticalLayout_3.addWidget(self.ui.labelErrorInteligibilidad)

        self._apilado = None
        self._configurar_tarjetas_formulario()
        self._actualizar_escala_alcons()
        self.setup_events()

    def _configurar_tarjetas_formulario(self):
        """
        Equilibra las 3 columnas del formulario (Guía de valores /
        Parámetros / Escala): mismo padding interno, soporte real de
        ventanas angostas (500 px) habilitando el ajuste de línea de los
        textos de cada campo y reduciendo los anchos fijos de cada fila, y
        envuelve `frame_medio` en un QScrollArea (solo scroll vertical) para
        que el modo apilado quepa en ventanas bajas. La altura común y el
        apilado en sí los resuelve `_ajustar_disposicion` — ver auditoría de
        layout del Módulo 2 (no se modificó el `.ui`).
        """
        ui = self.ui

        # Padding interno unificado (antes distinto entre el formulario y
        # los otros dos paneles).
        ui.vloGuia.setContentsMargins(_PADDING_TARJETA, _PADDING_TARJETA,
                                       _PADDING_TARJETA, _PADDING_TARJETA)
        ui.verticalLayout_3.setContentsMargins(_PADDING_TARJETA, _PADDING_TARJETA,
                                                _PADDING_TARJETA, _PADDING_TARJETA)
        ui.vloEscala.setContentsMargins(_PADDING_TARJETA, _PADDING_TARJETA,
                                         _PADDING_TARJETA, _PADDING_TARJETA)

        # Soporte real de 500 px de ancho: los nombres/descripciones de cada
        # campo no ajustaban línea, así que su ancho mínimo lo marcaba el
        # texto más largo sin cortar ("Coeficiente medio de absorcion") en
        # una sola línea — el principal responsable de que el formulario no
        # bajara de ~552 px. Se habilita el ajuste de línea (sin tocar
        # ningún texto) y se reducen los anchos fijos de cada fila (número,
        # unidad, spinbox) y sus espaciados.
        for lbl in (ui.labelCampoNombre, ui.labelCampoNombre_2, ui.labelCampoNombre_3,
                    ui.labelCampoNombre_4, ui.labelCampoNombre_5,
                    ui.labelCampoDesc, ui.labelCampoDesc_2, ui.labelCampoDesc_3,
                    ui.labelCampoDesc_4, ui.labelCampoDesc_5):
            lbl.setWordWrap(True)

        ui.frame_form.setStyleSheet(
            ui.frame_form.styleSheet().replace(
                "min-width: 100px; max-width: 110px;",
                "min-width: 74px; max-width: 86px;",
            )
        )
        for fila in (ui.frameFilaX, ui.frameFilaX_2, ui.frameFilaX_3,
                     ui.frameFilaX_4, ui.frameFilaX_5):
            fila.setStyleSheet(
                fila.styleSheet()
                .replace("min-width: 28px;\n    max-width: 28px;",
                         "min-width: 20px;\n    max-width: 20px;")
                .replace("min-width: 30px;\n    max-width: 30px;",
                         "min-width: 22px;\n    max-width: 22px;")
            )
        for lay in (ui.horizontalLayout_3, ui.horizontalLayout_4, ui.horizontalLayout_5,
                    ui.horizontalLayout_6, ui.horizontalLayout_7):
            lay.setSpacing(6)
            lay.setContentsMargins(8, 6, 8, 6)

        # frame_medio envuelto en un QScrollArea: solo scroll vertical
        # (nunca horizontal), necesario para que el modo apilado quepa en
        # ventanas bajas sin recortarse.
        indice = ui.verticalLayout_2.indexOf(ui.frame_medio)
        ui.verticalLayout_2.removeWidget(ui.frame_medio)
        scroll = QScrollArea()
        scroll.setObjectName("scrollFormulario")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # Vertical únicamente: cuando frame_medio (con el tope de alto de
        # _ajustar_disposicion) es más bajo que el viewport, queda centrado
        # en vez de pegado arriba; sin efecto cuando hay scroll (apilado).
        scroll.setAlignment(Qt.AlignVCenter)
        scroll.setWidget(ui.frame_medio)
        ui.verticalLayout_2.insertWidget(indice, scroll, 9)
        self._scroll_formulario = scroll

        self._ajustar_disposicion()

    def _ajustar_disposicion(self):
        """
        Disposición horizontal (3 columnas, stretch 2:3:2, altura común
        `_ALTURA_COMUN_TARJETAS` centrada verticalmente) por encima de
        `_ANCHO_APILAR`; por debajo, disposición vertical con el formulario
        primero (es la acción principal), cada tarjeta a su alto natural.
        Mismo patrón que `VentanaGraficaRT._ajustar_disposicion`.
        """
        apilar = self.width() < _ANCHO_APILAR
        if apilar == self._apilado:
            return
        self._apilado = apilar

        ui = self.ui
        layout = ui.horizontalLayout_2
        tarjetas = (ui.frame_GuiaValores, ui.frame_form, ui.frame_escala)
        for tarjeta in tarjetas:
            layout.removeWidget(tarjeta)

        if apilar:
            layout.setDirection(QBoxLayout.TopToBottom)
            orden = (ui.frame_form, ui.frame_GuiaValores, ui.frame_escala)
            for tarjeta in orden:
                tarjeta.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                layout.addWidget(tarjeta)
            for i in range(3):
                layout.setStretch(i, 0)
            # Sin tope: cada tarjeta a su alto natural, una debajo de otra;
            # el conjunto puede exceder el viewport (scroll vertical).
            ui.frame_medio.setMaximumHeight(16777215)
        else:
            layout.setDirection(QBoxLayout.LeftToRight)
            orden = (ui.frame_GuiaValores, ui.frame_form, ui.frame_escala)
            for tarjeta in orden:
                tarjeta.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                layout.addWidget(tarjeta)
            layout.setStretch(0, 2)
            layout.setStretch(1, 3)
            layout.setStretch(2, 2)
            # Sin alineación explícita por tarjeta: así cada una se estira
            # (Expanding) a la altura interior completa de frame_medio, que
            # es justo _ALTURA_COMUN_TARJETAS gracias al tope de abajo — las
            # 3 quedan exactamente iguales, no solo centradas con distinta
            # altura (ver medición en la respuesta de esta auditoría).
            margen_vertical = layout.contentsMargins().top() + layout.contentsMargins().bottom()
            ui.frame_medio.setMaximumHeight(_ALTURA_COMUN_TARJETAS + margen_vertical)

        compacto = self.width() < _ANCHO_PIE_COMPACTO
        if compacto != self._pie_compacto:
            self._pie_compacto = compacto
            ui.frame_bottom.setStyleSheet(
                estiloBarraInferior("frame_bottom", "botonIniciarAnalisis", compacto=compacto)
            )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._ajustar_disposicion()

    def _actualizar_escala_alcons(self):
        """
        El panel "Escala %ALCons" (`frame_escala`, definido en
        inteligibilidadHabla.ui) traía una escala estática de 5 categorías
        con umbrales propios (0-2/2-5/5-10/10-15/>15 %) que no coincidían
        con `AlconsCalculator.evaluar_alcons`. Se corrige por código, sin
        tocar el .ui (mismo criterio que el resto de ajustes de interfaz,
        ver D-011 en docs/DECISIONS.md), para reflejar la clasificación
        operativa vigente del proyecto (D-019, 6 categorías: Excelente,
        Buena, Regular, Pobre, Mala, Crítico).
        """
        ui = self.ui
        ui.labelNivelExcelente.setText("Excelente  — 0 % a 1.4 %")
        ui.labelNivelBuena.setText("Buena  — >1.4 % a 4.8 %")
        ui.labelNivelRegular.setText("Regular  — >4.8 % a 11.4 %")
        ui.labelNivelPobre.setText("Pobre  — >11.4 % a 24.2 %")
        ui.labelNivelMala.setText("Mala  — >24.2 % a 46.5 %")
        # La descripción de "Mala" pertenecía a la antigua categoría abierta
        # (">15 %", sin límite superior); ahora "Mala" sí tiene límite
        # superior (46.5 %) y el tono más grave pasa a "Crítico" (nueva).
        ui.labelDescMala.setText("Comunicación deficiente. Requiere mejoras significativas.")

        # Cada nivel (fNiv1..fNiv5) traía su propio recuadro con fondo
        # translúcido de color, dentro del fondo translúcido de la propia
        # tarjeta "Escala %ALCons" — dos capas superpuestas, visualmente
        # apiñado. Se reemplaza por una sola franja de color a la izquierda,
        # sin fondo ni borde propios: mismo lenguaje que los mosaicos de Tr
        # MID en Vista/ventGraficaRT.py (_tile_trmid). Los colores son los
        # mismos que ya traía cada recuadro (y los mismos que el texto del
        # nombre de cada nivel, definido en inteligibilidadHabla.ui).
        colores_nivel = {
            ui.fNiv1: "#22c55e", ui.fNiv2: "#86efac", ui.fNiv3: "#fde047",
            ui.fNiv4: "#fb923c", ui.fNiv5: "#f87171",
        }
        for frame, color in colores_nivel.items():
            # Sin border-radius: combinado con border-left, Qt renderiza la
            # franja partida en dos arcos (uno junto al nombre, otro junto a
            # la descripción) en vez de una sola línea continua.
            frame.setStyleSheet(
                f"QFrame {{ background-color: rgba(255,255,255,0.05); border: none; "
                f"border-left: 3px solid {color}; }}"
            )
            frame.layout().setContentsMargins(10, 6, 8, 6)

        # "Crítico" (> 46.5 %) no existía en el panel de 5 categorías; se
        # añade con el mismo estilo de franja (ver arriba), mismo rojo
        # oscuro ya usado para este nivel en el PDF
        # (Datos/utils/reportePDF.py::NIVELES_ALCONS, #8c1212).
        f_nivel_critico = QFrame(ui.frame_escala)
        f_nivel_critico.setObjectName("fNiv6")
        f_nivel_critico.setStyleSheet(
            "QFrame { background-color: rgba(255,255,255,0.05); border: none; "
            "border-left: 3px solid #8c1212; }"
        )
        f_nivel_critico.setFrameShape(QFrame.NoFrame)
        v_nivel_critico = QVBoxLayout(f_nivel_critico)
        v_nivel_critico.setSpacing(1)
        v_nivel_critico.setContentsMargins(10, 6, 8, 6)

        ui.labelNivelCritico = QLabel("Crítico  — >46.5 %", f_nivel_critico)
        ui.labelNivelCritico.setObjectName("labelNivelCritico")
        ui.labelNivelCritico.setStyleSheet(
            "QLabel { color: #8c1212; font-weight: bold; background: transparent; border: none; }"
        )
        v_nivel_critico.addWidget(ui.labelNivelCritico)

        ui.labelDescCritico = QLabel(
            "Comunicación extremadamente deficiente. Requiere atención urgente.",
            f_nivel_critico,
        )
        ui.labelDescCritico.setObjectName("labelDescCritico")
        ui.labelDescCritico.setWordWrap(True)
        v_nivel_critico.addWidget(ui.labelDescCritico)

        ui.vloEscala.addWidget(f_nivel_critico)

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
        Cualquier campo inválido se marca con fondo rojo y se describe en
        `labelErrorInteligibilidad` (texto inline, no bloqueante — ver
        auditoría UX/UI del Módulo 2).
        """
        errores = []  # Mensajes de los campos inválidos

        _estilo_error = "border: 1px solid red; background-color: rgba(255, 0, 0, 0.1);"

        # Validar distancia
        distancia = self.ui.distanciaRyE.value()
        if distancia <= 0:
            self.ui.distanciaRyE.setStyleSheet(_estilo_error)
            errores.append("Distancia debe ser mayor a 0")
        else:
            self.ui.distanciaRyE.setStyleSheet("")  # Restaura el estilo

        # Validar tiempo de reverberación
        tiempo_reverberacion = self.ui.recintoTR.value()
        if tiempo_reverberacion <= 0:
            self.ui.recintoTR.setStyleSheet(_estilo_error)
            errores.append("Tiempo de reverberación debe ser mayor a 0")
        else:
            self.ui.recintoTR.setStyleSheet("")

        # Validar volumen
        volumen_sala = self.ui.volumenSala.value()
        if volumen_sala <= 0:
            self.ui.volumenSala.setStyleSheet(_estilo_error)
            errores.append("Volumen de la sala debe ser mayor a 0")
        else:
            self.ui.volumenSala.setStyleSheet("")

        # Validar coeficiente de absorción (0 < α ≤ 1; antes solo exigía
        # > 0, sin tope superior — corregido en esta auditoría UX/UI).
        coeficiente_absorcion = self.ui.coeficienteMedio.value()
        if coeficiente_absorcion <= 0 or coeficiente_absorcion > 1:
            self.ui.coeficienteMedio.setStyleSheet(_estilo_error)
            errores.append("Coeficiente de absorción debe estar entre 0 y 1")
        else:
            self.ui.coeficienteMedio.setStyleSheet("")

        # Validar superficie total
        superficie_total = self.ui.superficieTotal.value()
        if superficie_total <= 0:
            self.ui.superficieTotal.setStyleSheet(_estilo_error)
            errores.append("Superficie total debe ser mayor a 0")
        else:
            self.ui.superficieTotal.setStyleSheet("")

        # Verificar si hay errores
        if errores:
            self.ui.labelErrorInteligibilidad.setText("⚠ " + " · ".join(errores))
            return None

        self.ui.labelErrorInteligibilidad.setText("")

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
        Valida los parámetros, calcula el %ALCons y navega a la pantalla de
        resultados (VentanaResultadosInteligibilidad).
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

                self.mostrar_pantalla_resultados(reporte)

            except Exception as e:
                QMessageBox.critical(self, "Error durante el cálculo", f"Se produjo un error:\n{str(e)}")

    def mostrar_pantalla_resultados(self, reporte):
        """
        Navega a VentanaResultadosInteligibilidad con el reporte ya
        calculado (mismo patrón que abrir_ventana_tiempoReverberacion en
        ventIniciarAnalisis.py / iniciar_analisis en ventInfoBD.py: se
        agrega al stackedWidget y se vuelve la pantalla actual).
        """
        if "Error" in reporte:
            QMessageBox.warning(self, "Error en los cálculos", reporte["Error"])
            return

        indice_actual = self.stacked_widget.currentIndex()
        ventana_resultados = VentanaResultadosInteligibilidad(
            stacked_widget=self.stacked_widget,
            indice_anterior=indice_actual,
            reporte=reporte,
        )
        self.stacked_widget.addWidget(ventana_resultados)
        self.stacked_widget.setCurrentWidget(ventana_resultados)

    def mostrar_resumen_reporte(self, reporte):
        """
        SIN USO desde la auditoría UX/UI del Módulo 2 (bloque M2-UX):
        reemplazado por mostrar_pantalla_resultados +
        VentanaResultadosInteligibilidad. Se conserva documentada, sin
        eliminar, siguiendo el mismo criterio que _marca_agua en
        Datos/utils/reportePDF.py (UX-07).

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

