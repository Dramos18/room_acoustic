
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QCompleter, QSizePolicy

from Controlador.controlTR import procesar_datos
from Vista.tiempoReverberacionUI import  Ui_FormTR # importa tu clase generada
from Vista.objetoSuperficie import Ui_formObjetoSuperficie
from Ventanas.ventanaBarraTitulo import VentanaConBarra
from Ventanas.ventGraficaRT import VentanaGraficaRT
from Controlador.Controlador import obtener_lista_materiales
from Vista.graficas.estilo import estiloFrameRT, estiloObjeto
from manejadorObjetos import ManejadorObjetosSuperficie
from manejadorObjetoAdicional import ManejadorObjetoAdicional
from Modelo.calculoRT2 import calcular_areas_basicas
from Modelo.Datos.utils.reportePDF import ReportePDF

class VentanaTiempoReverberacion(QWidget):
    """
    Esta clase representa la ventana de "Tiempo de Reverberacion".
    Es una subclase de QWidget que carga el diseño de iniciarAnalisis.
    """

    def __init__(self, stacked_widget, indice_anterior, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormTR()
        self.ui.setupUi(self)
        self.indice_anterior = indice_anterior
        self.stacked_widget = stacked_widget


        #self.cargar_materiales_en_combobox()
        self.materiales = obtener_lista_materiales()
        self.configurar_combobox_en_frame(self.ui.frMedium2, self.materiales)

        self.ui.frMedium2.setStyleSheet(estiloFrameRT)
        self.ui.frBottom3.setStyleSheet(estiloFrameRT)

        self.ui.botonAtras.setIcon(QIcon("Vista/graficas/iconos/angulo-izquierdo.png"))



        self.ui.checkInteligibilidadOpcion.stateChanged.connect(self.toggle_grupo_detalles)
        self.ui.checkObjAdicional.stateChanged.connect(self.toggle_grupo_objetos_adicionales)

        self.ui.frParedFrontal.layout().setAlignment(Qt.AlignCenter)
        self.ui.frParedTrasera.layout().setAlignment(Qt.AlignCenter)
        self.ui.frParedIzquierda.layout().setAlignment(Qt.AlignCenter)
        self.ui.frParedDerecha.layout().setAlignment(Qt.AlignCenter)
        self.ui.frPiso.layout().setAlignment(Qt.AlignCenter)
        self.ui.frTecho.layout().setAlignment(Qt.AlignCenter)
        self.ui.contObjAdicional.layout().setAlignment(Qt.AlignCenter)

        self.setup_events() #inicia los eventos de cada boton en la ventana

        #INFO diccionarios

        self.superficies = {
            "Frontal": self.ui.cbPdFrontal,
            "Trasera": self.ui.cbParedTrasera,
            "Izquierda": self.ui.cbpdIzq,
            "Derecha": self.ui.cbPdDerecha,
            "Piso": self.ui.cbPiso,
            "Techo": self.ui.cbTecho
        }



        self.manejadores = {}
        #Agrega objetos por superficies
        self.manejadores["Frontal"]   = ManejadorObjetosSuperficie(self.ui.contObjFrontal.layout(), area_maxima=25, checkbox=self.ui.checkPdFrontal, label_error=self.ui.labelError)
        self.manejadores["Trasera"]   = ManejadorObjetosSuperficie(self.ui.contObjTrasera.layout(), area_maxima=25, checkbox=self.ui.checkPdTrasera, label_error=self.ui.labelError)
        self.manejadores["Izquierda"] = ManejadorObjetosSuperficie(self.ui.contObjIzq.layout(),     area_maxima=25, checkbox=self.ui.checkPdIzq, label_error=self.ui.labelError)
        self.manejadores["Derecha"]   = ManejadorObjetosSuperficie(self.ui.contObjDer.layout(),     area_maxima=25, checkbox=self.ui.checkPdDer, label_error=self.ui.labelError)
        self.manejadores["Piso"]        = ManejadorObjetosSuperficie(self.ui.contObjPiso.layout(),    area_maxima=25, checkbox=self.ui.checkPiso, label_error=self.ui.labelError)
        self.manejadores["Techo"]       = ManejadorObjetosSuperficie(self.ui.contObjTecho.layout(),   area_maxima=25, checkbox=self.ui.checkTecho, label_error=self.ui.labelError)

        self.manejadores["ObjAdicional"] = ManejadorObjetoAdicional(self.ui.contObjAdicional.layout(), checkbox=self.ui.checkObjAdicional)


        #self.ui.botonIniciarAnalisis.clicked.connect(lambda: self.abrir_ventana_grafica())
        #self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)

        self.check_frame_map = {
            self.ui.checkPdFrontal: self.ui.contObjFrontal,
            self.ui.checkPdTrasera: self.ui.contObjTrasera,
            self.ui.checkPdIzq:     self.ui.contObjIzq,
            self.ui.checkPdDer:     self.ui.contObjDer,
            self.ui.checkPiso:      self.ui.contObjPiso,
            self.ui.checkTecho:     self.ui.contObjTecho,
        }
        for frame in self.check_frame_map.values():
            frame.hide()

            # Conectamos todos los checkboxes a un mismo metodo
        for checkbox in self.check_frame_map:
            checkbox.stateChanged.connect(self.actualizar_frames)

    def setup_events(self):
        self.ui.botonIniciarAnalisis.clicked.connect(lambda: self.abrir_ventana_grafica())
        self.ui.botonAtras.clicked.connect(self.regresar_a_ventana_anterior)



    def actualizar_frames(self):
        for checkbox, frame in self.check_frame_map.items():
            if checkbox.isChecked():
                self.animar_mostrar_frame(frame)
            else:
                self.animar_ocultar_frame(frame)

    def animar_mostrar_frame(self, frame):
        frame.setMaximumHeight(0)  # Preparar para expansión
        frame.show()
        animacion = QPropertyAnimation(frame, b"maximumHeight")
        animacion.setDuration(300)
        animacion.setStartValue(0)
        animacion.setEndValue(150)  # Altura deseada, ajústala si tu frame es más grande
        animacion.setEasingCurve(QEasingCurve.OutCubic)
        animacion.start()
        frame.animacion = animacion  # Evita que se destruya la animación

    def animar_ocultar_frame(self, frame):
        animacion = QPropertyAnimation(frame, b"maximumHeight")
        animacion.setDuration(300)
        animacion.setStartValue(frame.height())
        animacion.setEndValue(0)
        animacion.setEasingCurve(QEasingCurve.InCubic)
        animacion.finished.connect(frame.hide)
        animacion.start()
        frame.animacion = animacion  # Mantener la referencia

    def configurar_combobox_en_frame(self, frame, lista_opciones):
        for combo in frame.findChildren(QComboBox):
            combo.setEditable(True)

            completer = QCompleter(lista_opciones)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            combo.setCompleter(completer)

            if combo.count() == 0:
                combo.addItems(lista_opciones)

    def toggle_grupo_detalles(self, estado):
        if estado == 2:  # 2 = Checked, 0 = Unchecked
            self.ui.gbInteligibilad.setEnabled(True)
        else:
            self.ui.gbInteligibilad.setEnabled(False)

    def toggle_grupo_objetos_adicionales(self, estado):
        if estado == 2:  # 2 = Checked, 0 = Unchecked
            self.ui.contObjAdicional.setEnabled(True)
        else:
            self.ui.contObjAdicional.setEnabled(False)

    def mostrar_ocultar_frame(self, estado):
        self.ui.objetoPdFrontal.setVisible(estado == 2)

    #boton atras
    def regresar_a_ventana_anterior(self):
        """
        Cambia a la ventana anterior usando el QStackedWidget.
        """
        if hasattr(self, 'stacked_widget') and self.stacked_widget:
            self.stacked_widget.setCurrentIndex(self.indice_anterior)

    #boton iniciar analisis
    def validar_materiales_superficies(self):
        datos_superficies = {}
        errores = []

        for nombre, combobox in self.superficies.items():
            material = combobox.currentText()
            if material not in self.materiales:
                combobox.setStyleSheet("border: 1px solid red;")
                errores.append(f"⚠️ Material inválido en la superficie {nombre}.")
            else:
                combobox.setStyleSheet("")
                datos_superficies[nombre] = {"material": material}

        if errores:
            if self.ui.labelError:
                self.ui.labelError.setText("\n".join(errores))
            return None  # Devuelve `None` si hay errores
        else:
            if self.ui.labelError:
                self.ui.labelError.setText("")  # Limpia los errores si todo está bien
            return datos_superficies
    def validar_dimensiones(self):
        dimensiones = {}
        errores = []

        # Obtener valores de las entradas
        largo = self.ui.lineLargo.text().strip()
        ancho = self.ui.lineAncho.text().strip()
        altura = self.ui.lineAlto.text().strip()

        # Validar campo vacío
        if not largo:
            self.ui.lineLargo.setStyleSheet("border: 1px solid red;")
            errores.append("⚠️ Ingrese el largo de la superficie.")
        else:
            self.ui.lineLargo.setStyleSheet("")

        if not ancho:
            self.ui.lineAncho.setStyleSheet("border: 1px solid red;")
            errores.append("⚠️ Ingrese el ancho de la superficie.")
        else:
            self.ui.lineAncho.setStyleSheet("")

        if not altura:
            self.ui.lineAlto.setStyleSheet("border: 1px solid red;")
            errores.append("⚠️ Ingrese la altura de la superficie.")
        else:
            self.ui.lineAlto.setStyleSheet("")

        # Si no hay errores de entrada vacía, intentamos convertir los valores
        if not errores:
            try:
                largo = float(largo)
                if largo <= 1:
                    errores.append("⚠️ El largo debe ser un número mayor a 1.")
                    self.ui.lineLargo.setStyleSheet("border: 1px solid red;")

                ancho = float(ancho)
                if ancho <= 1:
                    errores.append("⚠️ El ancho debe ser un número mayor a 1.")
                    self.ui.lineAncho.setStyleSheet("border: 1px solid red;")

                altura = float(altura)
                if altura <= 1:
                    errores.append("⚠️ La altura debe ser un número mayor a 1.")
                    self.ui.lineAlto.setStyleSheet("border: 1px solid red;")
            except ValueError:
                errores.append("⚠️ Todas las dimensiones deben ser números válidos.")
                self.ui.lineLargo.setStyleSheet("border: 1px solid red;")
                self.ui.lineAncho.setStyleSheet("border: 1px solid red;")
                self.ui.lineAlto.setStyleSheet("border: 1px solid red;")

        # Si se encuentran errores, mostrarlos y terminar
        if errores:
            if self.ui.labelErrorDimensiones:
                self.ui.labelErrorDimensiones.setText("\n".join(errores))
            return None

        # Si no hay errores, limpiar los estilos y construir el diccionario
        if self.ui.labelErrorDimensiones:
            self.ui.labelErrorDimensiones.setText("")  # Limpia errores si están bien

        # Crear el diccionario de dimensiones
        dimensiones = {
            "largo": largo,
            "ancho": ancho,
            "altura": altura
        }

        return dimensiones
    def validar_areas_por_zona(self, areas_bases):
        """
        Valida que la suma de las áreas adheridas en cada superficie no sobrepase
        el límite permitido (según el área base de cada superficie).
        El error permanece visible hasta que se borre manualmente.
        """
        errores = []  # Lista para almacenar los errores detectados

        for nombre_superficie, manejador in self.manejadores.items():
            # Obtener los objetos adheridos validados por el manejador
            resultado_objetos = manejador.validar_y_obtener_datos()

            if resultado_objetos:
                # Verificar que la clave 'objetos_adheridos' exista en el resultado
                if "objetos_adheridos" in resultado_objetos:
                    # Calcular la suma de las áreas adheridas en esta superficie
                    suma_areas_adheridas = sum(obj["area"] for obj in resultado_objetos["objetos_adheridos"])

                    # Validar que no exceda el área máxima de la superficie
                    area_maxima_superficie = areas_bases.get(nombre_superficie, 0)
                    if suma_areas_adheridas > area_maxima_superficie:
                        errores.append(
                            f"⚠️ La suma de áreas adheridas en la superficie '{nombre_superficie}' " +
                            f"({suma_areas_adheridas:.2f} m²) excede el límite permitido " +
                            f"({area_maxima_superficie:.2f} m²)."
                        )

            elif manejador.checkbox.isChecked():
                # Si el checkbox está activo pero no hay datos válidos, marca error
                errores.append(
                    f"⚠️ Error: No se pudieron validar los objetos adheridos en la superficie '{nombre_superficie}'."
                )

        # Mostrar errores en el labelError
        if errores:
            if self.ui.labelError:
                self.ui.labelError.setVisible(True)  # Asegúrate de que sea visible
                self.ui.labelError.setText("\n".join(errores))  # Muestra todos los errores acumulados
                self.ui.labelError.repaint()  # Fuerza la actualización inmediata
            return True

        # Si no hay errores, oculta el labelError
        return False
    def validar_todas_superficies2(self):
        # Estructura del diccionario final
        caracteristicas = {
            "dimensiones": None,
            "materiales": {},
            "objetos_adicionales": None,
            "inteligibilidad": None
        }
        errores = False

        # Paso 1: Validar dimensiones
        dimensiones = self.validar_dimensiones()
        if dimensiones:
            # Agregar las dimensiones validadas al diccionario final
            caracteristicas["dimensiones"] = dimensiones
            largo = dimensiones.get("largo", 0)
            ancho = dimensiones.get("ancho", 0)
            altura = dimensiones.get("altura", 0)
            areas_bases = calcular_areas_basicas(largo, ancho, altura)
            if self.validar_areas_por_zona(areas_bases):
                errores = True

        else:
            errores = True
            print("Error: Las dimensiones no son válidas.")

        if not errores:
            # Paso 2: Validar materiales con `validar_superficies`
            datos_superficies = self.validar_materiales_superficies()
            if datos_superficies is None:
                errores = True  # Hubo errores en los materiales
                print("Error: No se pudieron validar los materiales de las superficies.")
            else:
                # Inicializa la sección de materiales con las superficies validadas
                caracteristicas["materiales"] = datos_superficies

            # Paso 3: Agregar objetos adheridos por superficie
            for nombre_superficie, manejador in self.manejadores.items():
                # Verifica si el manejador corresponde a una superficie existente en `materiales`
                if nombre_superficie in caracteristicas["materiales"]:
                    resultado_objetos = manejador.validar_y_obtener_datos()
                    if resultado_objetos:
                        # Si hay objetos adheridos, los añadimos a la superficie
                        caracteristicas["materiales"][nombre_superficie]["objetos_adheridos"] = resultado_objetos[
                            "objetos_adheridos"]
                    elif manejador.checkbox.isChecked():
                        # Si el checkbox está activo pero no hay datos válidos, marca error
                        errores = True
                        print(
                            f"Error: Los objetos adheridos de la superficie {nombre_superficie} no se pudieron validar correctamente.")

            # Paso 4: Validar objetos adicionales
            if "ObjAdicional" in self.manejadores:
                manejador_adicional = self.manejadores["ObjAdicional"]
                resultado_adicional = manejador_adicional.validar_y_obtener_datos()
                if resultado_adicional:
                    # Si hay objetos adicionales, los añadimos a `objetos_adicionales`
                    caracteristicas["objetos_adicionales"] = resultado_adicional["objetos_adicionales"]
                elif self.ui.checkObjAdicional.isChecked():
                    # Si hay un checkbox activo pero faltan los objetos adicionales, marca error
                    errores = True
                    print("Error: Los objetos adicionales no se pudieron validar correctamente.")



            #Paso 5: validar inteligibilidad
            inteligibilidad = self.validar_inteligibilidad()
            if inteligibilidad is None and self.ui.checkInteligibilidadOpcion.isChecked():
                # Si hay errores en inteligibilidad, no avanzamos
                errores = True
            else:
                caracteristicas["inteligibilidad"] = inteligibilidad



        # Paso 6: Manejar errores y retornar datos
        if errores:
            print("Error: Se detectaron problemas en la validación.")
            return None

        # Retorno de datos exitosos
        print("Validación exitosa. Datos recopilados:")
        return caracteristicas
    def validar_inteligibilidad(self):
        """
        Valida los valores para "inteligibilidad del habla" si el checkbox está activado.
        Los campos de distancia y coeficiente medio son QDoubleSpinBox.
        """
        # Verificar si la opción de inteligibilidad está activada
        if not self.ui.checkInteligibilidadOpcion.isChecked():
            return None

        inteligibilidad = {}
        errores = []

        # Obtener valores directamente desde QDoubleSpinBox
        distancia = self.ui.distanciaRyE.value()
        coeficiente_medio = self.ui.coeficienteMedio.value()

        # Validar valores mayores que 0
        if distancia <= 0:
            errores.append("⚠️ Ingresa un número válido para la distancia (mayor a 0).")
            self.ui.distanciaRyE.setStyleSheet("border: 1px solid red;")
        else:
            self.ui.distanciaRyE.setStyleSheet("")

        if coeficiente_medio <= 0:
            errores.append("⚠️ Ingresa un número válido para el coeficiente medio (mayor a 0).")
            self.ui.coeficienteMedio.setStyleSheet("border: 1px solid red;")
        else:
            self.ui.coeficienteMedio.setStyleSheet("")

        # Mostrar errores si los hay
        if errores:
            if self.ui.label_16:  # Asegurarnos de que el label existe
                self.ui.label_16.setText("\n".join(errores))
            return None

        # Si no hay errores, limpiar el label de errores y construir el diccionario
        if self.ui.label_16:
            self.ui.label_16.setText("")  # Limpia el texto de errores

        inteligibilidad = {
            "distancia": distancia,
            "coeficiente_medio": coeficiente_medio
        }

        return inteligibilidad
    def validar_todas_superficies(self):
        datos_finales = {}
        errores = False

        # Paso 1: Validar materiales con `validar_superficies`
        datos_superficies = self.validar_materiales_superficies()
        if datos_superficies is None:
            errores = True  # Hubo errores en los materiales
        else:
            # Si pasa la validación de materiales, inicializa datos_finales con datos_superficies
            datos_finales = datos_superficies

        # Paso 2: Agregar objetos adheridos por superficie
        for nombre_superficie, manejador in self.manejadores.items():
            # Verifica si el manejador corresponde a una superficie y existe en `datos_superficies`
            if nombre_superficie in datos_finales:
                resultado_objetos = manejador.validar_y_obtener_datos()
                if resultado_objetos:
                    # Si existen objetos adheridos, los agregamos a la superficie
                    datos_finales[nombre_superficie]["objetos_adheridos"] = resultado_objetos["objetos_adheridos"]
                elif manejador.checkbox.isChecked():
                    # Si el checkbox está activo pero hay errores, marcamos errores
                    errores = True

        # Paso 3: Validar objetos adicionales
        if "ObjAdicional" in self.manejadores:
            manejador_adicional = self.manejadores["ObjAdicional"]
            resultado_adicional = manejador_adicional.validar_y_obtener_datos()
            if resultado_adicional:
                # Agregar objetos adicionales como una clave separada
                datos_finales["objetos_adicionales"] = resultado_adicional["objetos_adicionales"]
            elif self.ui.checkObjAdicional.isChecked():
                # Si el checkbox está activo pero hay errores, marcamos errores
                errores = True

        # Paso 4: Validar dimensiones
        dimensiones = self.validar_dimensiones()
        if dimensiones:
            datos_finales["dimensiones"] = dimensiones
        else:
            errores = True

        # Si hubo errores en cualquier paso, retorna None
        if errores:
            return None

        # Retorna todos los datos validados
        print(datos_finales)
        return datos_finales

    def abrir_ventana_grafica(self):
        self.indice_anterior = self.stacked_widget.currentIndex()
        resultado = self.enviar_obtener_datos_controlador()
        ventana_grafica = VentanaGraficaRT(stacked_widget= self.stacked_widget, indice_anterior=self.indice_anterior,resultados=resultado)
        ventana_grafica.indice_anterior = self.stacked_widget.currentIndex()

        self.stacked_widget.addWidget(ventana_grafica)
        self.stacked_widget.setCurrentWidget(ventana_grafica)

    def enviar_obtener_datos_controlador(self):
        """
        Enviar diccionario generado al Controlador para procesamiento.
        """
        datos = self.validar_todas_superficies2()
        if datos is None:
            # Muestra error en la interfaz si los datos son inválidos
            print("Error en la validación de superficies.")
        else:
            # Envía los datos al controlador
            print("llendo a procesar datos")
            resultados = procesar_datos(datos)
            return resultados







