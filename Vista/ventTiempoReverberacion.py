from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QComboBox, QCompleter

from Controlador.controlTR import procesar_datos
from Vista.archivos_pyGenerados.tiempoReverberacionUI import Ui_FormTR
from Vista.ventGraficaRT import VentanaGraficaRT
from Controlador.Controlador import obtener_lista_materiales
from Recursos.estilos.estilo import estiloFrameRT
from manejadorObjetos import ManejadorObjetosSuperficie
from manejadorObjetoAdicional import ManejadorObjetoAdicional
from Modelo.calculoRT2 import calcular_areas_basicas

# ── Estilos de validación ────────────────────────────────────
_ERROR_INPUT  = "border: 1px solid rgba(248,113,113,0.90); background: rgba(248,113,113,0.10);"
_OK_INPUT     = ""

# Altura máxima para el panel de objetos dinámicos.
# Se usa un valor holgado; la animación no ocupa más espacio del necesario
# porque el frame tiene sizePolicy Minimum.
_ALTURA_ANIM  = 400


class VentanaTiempoReverberacion(QWidget):
    """
    Ventana principal del módulo de Tiempo de Reverberación.
    Permite ingresar dimensiones, materiales y objetos de las 6
    superficies del aula para calcular el RT60 (Sabine y Eyring).
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormTR()
        self.ui.setupUi(self)
        self.indice_anterior = indice_anterior
        self.stacked_widget  = stacked_widget

        # Materiales
        self.materiales = obtener_lista_materiales()
        self.configurar_combobox_en_frame(self.ui.frMedium2, self.materiales)

        # Iconos
        self.ui.botonAtras.setIcon(QIcon("../Recursos/iconos/angulo-izquierdo.png"))
        ruta_check = "../Recursos/iconos/controlar.png"


        self.ui.checkObjAdicional.setStyleSheet(f"""
            QCheckBox {{
                background: transparent;
                color: rgba(255, 255, 255, 0.85);
                font-size: 11px;
            }}

            QCheckBox::indicator {{
                width: 17px;
                height: 17px;
                border-radius: 4px;
                background: rgba(255, 255, 255, 0.15);
                border: 1px solid rgba(255, 255, 255, 0.45);
            }}

            QCheckBox::indicator:hover {{
                background: rgba(255, 255, 255, 0.30);
            }}

            QCheckBox::indicator:checked {{
                background: rgba(126, 200, 247, 0.55);
                border: 1px solid #7ec8f7;
                image: url({ruta_check}); /* Python inserta la ruta aquí */
            }}
        """)
    #    self.ui.check.setStyleSheet(f"""
    #                QCheckBox {{
    #                    background: transparent;
    #                    color: rgba(255, 255, 255, 0.85);
    #                    font-size: 11px;
    #                }}
#
    #                QCheckBox::indicator {{
    #                    width: 17px;
    #                    height: 17px;
    #                    border-radius: 4px;
    #                    background: rgba(255, 255, 255, 0.15);
    #                    border: 1px solid rgba(255, 255, 255, 0.45);
    #                }}
#
    #                QCheckBox::indicator:hover {{
    #                    background: rgba(255, 255, 255, 0.30);
    #                }}
#
    #                QCheckBox::indicator:checked {{
    #                    background: rgba(126, 200, 247, 0.55);
    #                    border: 1px solid #7ec8f7;
    #                    image: url({ruta_check}); /* Python inserta la ruta aquí */
    #                }}
    #            """)

        # Checkboxes de sección
        self.ui.checkInteligibilidadOpcion.stateChanged.connect(self.toggle_grupo_detalles)
        self.ui.checkObjAdicional.stateChanged.connect(self.toggle_grupo_objetos_adicionales)

        # Alineación de contenedores
        for nombre in ("frParedFrontal", "frParedTrasera", "frParedIzquierda",
                       "frParedDerecha", "frPiso", "frTecho", "contObjAdicional"):
            frame = getattr(self.ui, nombre)
            if frame.layout():
                frame.layout().setAlignment(Qt.AlignTop)

        self.setup_events()

        # ── Mapa superficie → comboBox ──────────────────────────
        self.superficies = {
            "Frontal":    self.ui.cbPdFrontal,
            "Trasera":    self.ui.cbParedTrasera,
            "Izquierda":  self.ui.cbpdIzq,
            "Derecha":    self.ui.cbPdDerecha,
            "Piso":       self.ui.cbPiso,
            "Techo":      self.ui.cbTecho,
        }

        # ── Manejadores de objetos dinámicos ────────────────────
        self.manejadores = {}
        self.manejadores["Frontal"]      = ManejadorObjetosSuperficie(
            self.ui.contObjFrontal.layout(), area_maxima=25,
            checkbox=self.ui.checkPdFrontal,  label_error=self.ui.labelError)
        self.manejadores["Trasera"]      = ManejadorObjetosSuperficie(
            self.ui.contObjTrasera.layout(), area_maxima=25,
            checkbox=self.ui.checkPdTrasera,  label_error=self.ui.labelError)
        self.manejadores["Izquierda"]    = ManejadorObjetosSuperficie(
            self.ui.contObjIzq.layout(),     area_maxima=25,
            checkbox=self.ui.checkPdIzq,      label_error=self.ui.labelError)
        self.manejadores["Derecha"]      = ManejadorObjetosSuperficie(
            self.ui.contObjDer.layout(),     area_maxima=25,
            checkbox=self.ui.checkPdDer,      label_error=self.ui.labelError)
        self.manejadores["Piso"]         = ManejadorObjetosSuperficie(
            self.ui.contObjPiso.layout(),    area_maxima=25,
            checkbox=self.ui.checkPiso,       label_error=self.ui.labelError)
        self.manejadores["Techo"]        = ManejadorObjetosSuperficie(
            self.ui.contObjTecho.layout(),   area_maxima=25,
            checkbox=self.ui.checkTecho,      label_error=self.ui.labelError)
        self.manejadores["ObjAdicional"] = ManejadorObjetoAdicional(
            self.ui.contObjAdicional.layout(), checkbox=self.ui.checkObjAdicional)

        # ── Mapa checkbox → frame de objetos ────────────────────
        self.check_frame_map = {
            self.ui.checkPdFrontal: self.ui.contObjFrontal,
            self.ui.checkPdTrasera: self.ui.contObjTrasera,
            self.ui.checkPdIzq:     self.ui.contObjIzq,
            self.ui.checkPdDer:     self.ui.contObjDer,
            self.ui.checkPiso:      self.ui.contObjPiso,
            self.ui.checkTecho:     self.ui.contObjTecho,
        }

        # Ocultar todos los contenedores de objetos al inicio
        for frame in self.check_frame_map.values():
            frame.hide()

        # Conectar checkboxes de superficie
        for checkbox in self.check_frame_map:
            checkbox.stateChanged.connect(self.actualizar_frames)

    # ── Eventos ─────────────────────────────────────────────────

    def setup_events(self):
        self.ui.botonIniciarAnalisis.clicked.connect(self.abrir_ventana_grafica)
        self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)

    # ── Animaciones de expansión/colapso ────────────────────────

    def actualizar_frames(self):
        for checkbox, frame in self.check_frame_map.items():
            if checkbox.isChecked():
                self.animar_mostrar_frame(frame)
            else:
                self.animar_ocultar_frame(frame)

    def animar_mostrar_frame(self, frame):
        """
        Expande el frame con animación suave.
        Usa sizeHint().height() como objetivo para adaptarse al contenido real,
        con un mínimo de _ALTURA_ANIM como techo holgado.
        """
        frame.setMaximumHeight(0)
        frame.show()

        # Calcular altura real del contenido
        hint = frame.sizeHint().height()
        target = max(hint, 80) if hint > 0 else _ALTURA_ANIM

        animacion = QPropertyAnimation(frame, b"maximumHeight")
        animacion.setDuration(280)
        animacion.setStartValue(0)
        animacion.setEndValue(target)
        animacion.setEasingCurve(QEasingCurve.OutCubic)
        animacion.finished.connect(lambda: frame.setMaximumHeight(16777215))
        animacion.start()
        frame._animacion = animacion  # evitar que el GC destruya la animación

    def animar_ocultar_frame(self, frame):
        """Colapsa el frame con animación suave."""
        animacion = QPropertyAnimation(frame, b"maximumHeight")
        animacion.setDuration(240)
        animacion.setStartValue(frame.height())
        animacion.setEndValue(0)
        animacion.setEasingCurve(QEasingCurve.InCubic)
        animacion.finished.connect(frame.hide)
        animacion.start()
        frame._animacion = animacion

    # ── ComboBox ─────────────────────────────────────────────────

    def configurar_combobox_en_frame(self, frame, lista_opciones):
        for combo in frame.findChildren(QComboBox):
            combo.setEditable(True)
            completer = QCompleter(lista_opciones)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            combo.setCompleter(completer)
            if combo.count() == 0:
                combo.addItems(lista_opciones)

    # ── Toggles de sección ───────────────────────────────────────

    def toggle_grupo_detalles(self, estado):
        """Habilita/deshabilita el GroupBox de inteligibilidad."""
        self.ui.gbInteligibilad.setEnabled(estado == 2)

    def toggle_grupo_objetos_adicionales(self, estado):
        """
        Habilita/deshabilita el contenedor de objetos adicionales
        con una animación suave de expansión.
        """
        habilitado = (estado == 2)
        self.ui.contObjAdicional.setEnabled(habilitado)

        if habilitado:
            self.animar_mostrar_frame(self.ui.contObjAdicional)
        else:
            self.animar_ocultar_frame(self.ui.contObjAdicional)

    def mostrar_ocultar_frame(self, estado):
        self.ui.objetoPdFrontal.setVisible(estado == 2)

    # ── Navegación ───────────────────────────────────────────────

    def regresar_a_ventana_anterior(self):
        if hasattr(self, "stacked_widget") and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)

    # ── Validaciones ─────────────────────────────────────────────

    def validar_materiales_superficies(self):
        datos_superficies = {}
        errores = []

        for nombre, combobox in self.superficies.items():
            material = combobox.currentText()
            if material not in self.materiales:
                combobox.setStyleSheet(_ERROR_INPUT)
                errores.append(f"Material inválido en la superficie {nombre}.")
            else:
                combobox.setStyleSheet(_OK_INPUT)
                datos_superficies[nombre] = {"material": material}

        if errores:
            if self.ui.labelError:
                self.ui.labelError.setText("⚠ " + " · ".join(errores))
            return None

        if self.ui.labelError:
            self.ui.labelError.setText("")
        return datos_superficies

    def validar_dimensiones(self):
        dimensiones = {}
        errores = []

        largo  = self.ui.lineLargo.text().strip()
        ancho  = self.ui.lineAncho.text().strip()
        altura = self.ui.lineAlto.text().strip()

        # Vacíos
        for valor, widget, etiqueta in [
            (largo,  self.ui.lineLargo, "largo"),
            (ancho,  self.ui.lineAncho, "ancho"),
            (altura, self.ui.lineAlto,  "alto"),
        ]:
            if not valor:
                widget.setStyleSheet(_ERROR_INPUT)
                errores.append(f"Ingrese el {etiqueta}.")
            else:
                widget.setStyleSheet(_OK_INPUT)

        if not errores:
            try:
                largo_f  = float(largo.replace(",", "."))
                ancho_f  = float(ancho.replace(",", "."))
                altura_f = float(altura.replace(",", "."))

                if largo_f <= 1:
                    errores.append("El largo debe ser > 1 m.")
                    self.ui.lineLargo.setStyleSheet(_ERROR_INPUT)
                if ancho_f <= 1:
                    errores.append("El ancho debe ser > 1 m.")
                    self.ui.lineAncho.setStyleSheet(_ERROR_INPUT)
                if altura_f <= 1:
                    errores.append("La altura debe ser > 1 m.")
                    self.ui.lineAlto.setStyleSheet(_ERROR_INPUT)

            except ValueError:
                errores.append("Las dimensiones deben ser números válidos.")
                for w in (self.ui.lineLargo, self.ui.lineAncho, self.ui.lineAlto):
                    w.setStyleSheet(_ERROR_INPUT)

        if errores:
            if self.ui.labelErrorDimensiones:
                self.ui.labelErrorDimensiones.setText("⚠ " + " · ".join(errores))
            return None

        if self.ui.labelErrorDimensiones:
            self.ui.labelErrorDimensiones.setText("")
        return {"largo": largo_f, "ancho": ancho_f, "altura": altura_f}

    def validar_areas_por_zona(self, areas_bases):
        errores = []
        for nombre_superficie, manejador in self.manejadores.items():
            resultado = manejador.validar_y_obtener_datos()
            if resultado and "objetos_adheridos" in resultado:
                suma = sum(obj["area"] for obj in resultado["objetos_adheridos"])
                maximo = areas_bases.get(nombre_superficie, 0)
                if suma > maximo:
                    errores.append(
                        f"Superficie {nombre_superficie}: suma de areas "
                        f"({suma:.2f} m²) excede el limite ({maximo:.2f} m²)."
                    )
            elif manejador.checkbox.isChecked() and resultado is None:
                errores.append(f"Objetos invalidos en superficie {nombre_superficie}.")

        if errores:
            if self.ui.labelError:
                self.ui.labelError.setVisible(True)
                self.ui.labelError.setText("⚠ " + " · ".join(errores))
            return True
        return False

    def validar_inteligibilidad(self):
        if not self.ui.checkInteligibilidadOpcion.isChecked():
            return None

        errores = []
        distancia        = self.ui.distanciaRyE.value()
        coeficiente_medio = self.ui.coeficienteMedio.value()

        if distancia <= 0:
            errores.append("Distancia debe ser mayor a 0.")
            self.ui.distanciaRyE.setStyleSheet(_ERROR_INPUT)
        else:
            self.ui.distanciaRyE.setStyleSheet(_OK_INPUT)

        if coeficiente_medio <= 0:
            errores.append("Coeficiente medio debe ser mayor a 0.")
            self.ui.coeficienteMedio.setStyleSheet(_ERROR_INPUT)
        else:
            self.ui.coeficienteMedio.setStyleSheet(_OK_INPUT)

        if errores:
            if self.ui.label_16:
                self.ui.label_16.setText("⚠ " + " · ".join(errores))
            return None

        if self.ui.label_16:
            self.ui.label_16.setText("")
        return {"distancia": distancia, "coeficiente_medio": coeficiente_medio}

    def validar_todas_superficies(self):
        datos_finales = {}
        errores = False

        datos_superficies = self.validar_materiales_superficies()
        if datos_superficies is None:
            errores = True
        else:
            datos_finales = datos_superficies

        for nombre_superficie, manejador in self.manejadores.items():
            if nombre_superficie in datos_finales:
                resultado = manejador.validar_y_obtener_datos()
                if resultado:
                    datos_finales[nombre_superficie]["objetos_adheridos"] = \
                        resultado["objetos_adheridos"]
                elif manejador.checkbox.isChecked():
                    errores = True

        if "ObjAdicional" in self.manejadores:
            manejador_adicional = self.manejadores["ObjAdicional"]
            resultado_adicional = manejador_adicional.validar_y_obtener_datos()
            if resultado_adicional:
                datos_finales["objetos_adicionales"] = \
                    resultado_adicional["objetos_adicionales"]
            elif self.ui.checkObjAdicional.isChecked():
                errores = True

        dimensiones = self.validar_dimensiones()
        if dimensiones:
            datos_finales["dimensiones"] = dimensiones
        else:
            errores = True

        if errores:
            return None
        return datos_finales

    def validar_todas_superficies2(self):
        caracteristicas = {
            "dimensiones":        None,
            "materiales":         {},
            "objetos_adicionales": None,
            "inteligibilidad":    None,
        }
        errores = False

        # Paso 1: Dimensiones
        dimensiones = self.validar_dimensiones()
        if dimensiones:
            caracteristicas["dimensiones"] = dimensiones
            largo  = dimensiones.get("largo",  0)
            ancho  = dimensiones.get("ancho",  0)
            altura = dimensiones.get("altura", 0)
            areas_bases = calcular_areas_basicas(largo, ancho, altura)
            if self.validar_areas_por_zona(areas_bases):
                errores = True
        else:
            errores = True
            print("Error: dimensiones inválidas.")

        if not errores:
            # Paso 2: Materiales
            datos_superficies = self.validar_materiales_superficies()
            if datos_superficies is None:
                errores = True
                print("Error: materiales inválidos.")
            else:
                caracteristicas["materiales"] = datos_superficies

            # Paso 3: Objetos adheridos
            for nombre, manejador in self.manejadores.items():
                if nombre in caracteristicas["materiales"]:
                    resultado = manejador.validar_y_obtener_datos()
                    if resultado:
                        caracteristicas["materiales"][nombre]["objetos_adheridos"] = \
                            resultado["objetos_adheridos"]
                    elif manejador.checkbox.isChecked():
                        errores = True
                        print(f"Error: objetos adheridos de {nombre} inválidos.")

            # Paso 4: Objetos adicionales
            if "ObjAdicional" in self.manejadores:
                manejador_adicional = self.manejadores["ObjAdicional"]
                resultado_adicional = manejador_adicional.validar_y_obtener_datos()
                if resultado_adicional:
                    caracteristicas["objetos_adicionales"] = \
                        resultado_adicional["objetos_adicionales"]
                elif self.ui.checkObjAdicional.isChecked():
                    errores = True
                    print("Error: objetos adicionales inválidos.")

            # Paso 5: Inteligibilidad
            inteligibilidad = self.validar_inteligibilidad()
            if inteligibilidad is None and self.ui.checkInteligibilidadOpcion.isChecked():
                errores = True
            else:
                caracteristicas["inteligibilidad"] = inteligibilidad

        if errores:
            print("Error: validación con problemas.")
            return None

        print("Validación exitosa:", caracteristicas)
        return caracteristicas

    # ── Flujo hacia la ventana de resultados ─────────────────────

    def abrir_ventana_grafica(self):
        self.indice = self.stacked_widget.currentIndex()
        resultado = self.enviar_obtener_datos_controlador()
        if resultado is None:
            return   # los errores ya se mostraron en los labels
        ventana_grafica = VentanaGraficaRT(
            stacked_widget=self.stacked_widget,
            indice_anterior=self.indice,
            resultados=resultado,
        )
        ventana_grafica.indice_anterior = self.stacked_widget.currentIndex()
        self.stacked_widget.addWidget(ventana_grafica)
        self.stacked_widget.setCurrentWidget(ventana_grafica)

    def enviar_obtener_datos_controlador(self):
        datos = self.validar_todas_superficies2()
        if datos is None:
            print("Error en la validación de superficies.")
            return None
        print("Procesando datos...")
        return procesar_datos(datos)