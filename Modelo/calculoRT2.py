import io

from Controlador.Controlador import obtener_lista_materiales, obtener_coeficientes_materiales
import math
import matplotlib.pyplot as plt
from Modelo.alcons2 import AlconsCalculator

coeficientes = obtener_coeficientes_materiales()




def calcular_areas_basicas(largo, ancho, altura):
    """
    Calcula áreas de paredes, piso y techo de un salón rectangular.
    """

    # Área base de cada superficie
    area_pared_frontal = ancho * altura
    area_pared_lateral = largo * altura
    area_piso = largo * ancho
    area_techo = area_piso

    # · Áreas por material (se pueden ajustar posteriormente para ventanas y puertas)
    superficies = {
        "Frontal": area_pared_frontal,
        "Trasera": area_pared_frontal,
        "Izquierda": area_pared_lateral,
        "Derecha": area_pared_lateral,
        "Piso": area_piso,
        "Techo": area_techo


    }
    return superficies

def agregar_areas_materiales(datos):
    """
    Calcula las áreas de las superficies (paredes, techo, piso) y las agrega al diccionario 'materiales',
    restando el área de los objetos adheridos si los hay.
    También valida que las áreas de los objetos adheridos no excedan el área total de la superficie.
    """
    dimensiones = datos.get("dimensiones", {})
    largo = dimensiones.get("largo", 0)
    ancho = dimensiones.get("ancho", 0)
    altura = dimensiones.get("altura", 0)

    # 2. Calcular las áreas básicas de las superficies
    superficies_basicas = calcular_areas_basicas(largo, ancho, altura)

    # Obtener la referencia al diccionario de materiales
    materiales = datos.get("materiales", {})

    # 3. Iterar sobre cada zona y calcular el área restante
    for zona, propiedades in materiales.items():
        # Área base de la superficie
        area_superficie = superficies_basicas.get(zona, 0)

        # Verificar si existen objetos adheridos
        objetos_adheridos = propiedades.get("objetos_adheridos", [])
        area_adheridos = sum(objeto.get("area", 0) for objeto in objetos_adheridos)

        # Validar si el área adherida supera el área total de la superficie
        if area_adheridos > area_superficie:
             ValueError(f"El área total de los objetos adheridos en '{zona}' ({area_adheridos:.2f}) "
                             f"excede el área de la superficie ({area_superficie:.2f}).")

        # Calcular el área restante después de restar los objetos adheridos
        area_final = area_superficie - area_adheridos

        # Asegurar que el área final no sea negativa
        area_final = max(area_final, 0)

        # Añadir el área final al diccionario de materiales
        materiales[zona]["area"] = area_final

    # Devolver el diccionario actualizado (opcional si quieres modificar `datos` directamente)
    return datos

def calcular_absorcion_total(material, coeficientes, frecuencias=None):
    """
    Calcula el coeficiente de absorción total (A) para cada frecuencia considerando:
        - Áreas de superficies y sus materiales.
        - Áreas de objetos adheridos en las superficies.
        - Absorción de los objetos adicionales, si están presentes en el diccionario `materiales`.

    :param materiales: Diccionario de superficies con áreas, materiales, objetos adheridos y adicionales.
    :param coeficientes: Diccionario con coeficientes de absorción por material y frecuencia.
    :param frecuencias: Lista de frecuencias de interés (opcional).
    :return:
        - absorcion_total (dict): Diccionario con el valor "A" (absorción total) por frecuencia.
        - detalles (list): Lista con información detallada de cada cálculo (coef. aplicado por material/objeto).
    """
    # Frecuencias estándar si no se especifican
    if frecuencias is None:
        frecuencias = [125, 250, 500, 1000, 2000, 4000]

    # Inicializamos el total de absorción por frecuencia (A)
    absorcion_total = {f: 0 for f in frecuencias}

    # Lista para almacenar los detalles del cálculo (área x coef.)
    detalles = []

    materiales = material.get("materiales", {})

    # ===================
    # Cálculo para Materiales y Superficies
    # ===================
    for zona, propiedades in materiales.items():
        area_superficie = propiedades.get("area", 0)  # Área final de la superficie
        material_base = propiedades.get("material")  # Material base de la superficie

        # Absorción del material base
        if material_base in coeficientes:
            for f in frecuencias:
                coef = coeficientes[material_base].get(f, 0)
                absorcion_total[f] += area_superficie * coef
                # Guardar detalle del cálculo
                detalles.append({
                    "zona": zona,
                    "material": material_base,
                    "frecuencia": f,
                    "area_aplicada": area_superficie,
                    "coeficiente": coef,
                    "absorcion": area_superficie * coef
                })

        # Absorción de objetos adheridos
        objetos_adheridos = propiedades.get("objetos_adheridos", [])
        for objeto in objetos_adheridos:
            material_adherido = objeto.get("material")
            area_adherida = objeto.get("area", 0)
            if material_adherido in coeficientes:
                for f in frecuencias:
                    coef = coeficientes[material_adherido].get(f, 0)
                    absorcion_total[f] += area_adherida * coef
                    # Guardar detalle del cálculo
                    detalles.append({
                        "zona": zona,
                        "material": material_adherido,
                        "frecuencia": f,
                        "area_aplicada": area_adherida,
                        "coeficiente": coef,
                        "absorcion": area_adherida * coef
                    })

    # ===================
    # Cálculo para Objetos Adicionales
    # ===================
    objetos_adicionales = materiales.get("objetos_adicionales", [])  # Buscar objetos adicionales como clave en materiales
    if objetos_adicionales:  # Si hay objetos adicionales presentes
        for objeto in objetos_adicionales:
            material = objeto.get("material")
            cantidad = objeto.get("cantidad", 1)  # Si la cantidad no está definida, se toma como 1 por defecto
            area_efectiva = objeto.get("area_efectiva", 0) * cantidad  # Se calcula el área total del objeto

            if material in coeficientes:  # Verificar si hay coeficientes para este material
                for f in frecuencias:
                    coef = coeficientes[material].get(f, 0)
                    absorcion_total[f] += area_efectiva * coef
                    # Guardar detalle del cálculo
                    detalles.append({
                        "zona": "Objeto Adicional",
                        "material": material,
                        "frecuencia": f,
                        "area_aplicada": area_efectiva,
                        "coeficiente": coef,
                        "absorcion": area_efectiva * coef
                    })

    return absorcion_total, detalles

def calcular_rt60_sabine(volumen, absorcion_total, decimales=2):
    """
    Calcula el tiempo de reverberación (RT60) para cada frecuencia usando la fórmula de Sabine.

    RT60 = (0.161 * Volumen) / Absorción Total

    :param volumen: Volumen del espacio en metros cúbicos (m³).
    :param absorcion_total: Diccionario con la absorción total 'A' (por frecuencia).
                           Formato esperado: {frecuencia1: A1, frecuencia2: A2, ...}
    :param decimales: Número de decimales para redondear el resultado. Default es 2.
    :return: Diccionario con los tiempos de reverberación RT60 por frecuencia.
             Formato: {frecuencia1: RT60_1, frecuencia2: RT60_2, ...}
    """

    # Inicializamos el diccionario de resultados
    rt60 = {}

    # Cálculo de RT60 para cada frecuencia
    for frecuencia, absorcion in absorcion_total.items():
        if absorcion > 0:
            # Fórmula de Sabine
            rt60[frecuencia] = round(0.161 * volumen / absorcion, decimales)
        else:
            # Sin absorción: reverberación infinita (o indefinida)
            rt60[frecuencia] = "Infinito"

    return rt60

def calcular_rt60_eyring(volumen, area_total, absorcion_total, decimales=2):
    """
    Calcula el tiempo de reverberación (RT60) para cada frecuencia usando la fórmula de Eyring.

    RT60 = -0.161 * volumen / (area_total * log(1 - alpha_prom))

    :param volumen: (float) Volumen del espacio en m³.
    :param area_total: (float) Área total de las superficies en m².
    :param absorcion_total: (dict) Total de absorción acústica para cada frecuencia.
                            Formato esperado: {frecuencia1: absorcion1, frecuencia2: absorcion2, ...}
    :param decimales: (int) Número de decimales para los resultados. Default = 2.
    :return: (dict) RT60 calculado por frecuencia usando la fórmula de Eyring.
             Formato: {frecuencia1: RT60_1, frecuencia2: RT60_2, ...}.
    """

    # Inicializamos el diccionario de resultados
    rt60 = {}

    # Cálculo para cada frecuencia
    for frecuencia, absorcion in absorcion_total.items():
        if absorcion > 0:
            # Coef. promedio de absorción para esta frecuencia
            alpha_prom = absorcion / area_total

            # Validar dominio del logaritmo
            if 1 - alpha_prom > 0:
                # Fórmula de Eyring
                rt60[frecuencia] = round(-0.161 * volumen / (area_total * math.log(1 - alpha_prom)), decimales)
            else:
                rt60[frecuencia] = "Infinito"  # Absorción total cercana al 100%
        else:
            rt60[frecuencia] = "Infinito"  # Caso de absorción nula para la frecuencia

    return rt60

def graficar_rt602(rt60, rt60_eyring):
    """
    Genera un gráfico comparativo del RT60 por frecuencia calculado con Sabine y Eyring.

    :param rt60: (dict) Resultados de RT60 obtenidos con la fórmula de Sabine.
                 Ejemplo: {125: 1.8, 250: 2.0, 500: 2.3, ...}
    :param rt60_eyring: (dict) Resultados de RT60 obtenidos con la fórmula de Eyring.
                        Ejemplo: {125: 1.7, 250: 1.9, 500: 2.2, ...}
    :return: None. Muestra directamente el gráfico.
    """
    # Extraer frecuencias y valores para Sabine
    frecuencias = list(rt60.keys())
    valores_rt60 = [rt60[f] if isinstance(rt60[f], (int, float)) else None for f in frecuencias]

    # Extraer frecuencias y valores para Eyring
    valores_rt60_eyring = [rt60_eyring[f] if isinstance(rt60_eyring[f], (int, float)) else None for f in frecuencias]

    # Crear el gráfico
    plt.figure(figsize=(10, 6))

    # Gráfico para Sabine
    plt.plot(
        frecuencias, valores_rt60,
        marker="o", linestyle="--", color="#FF6F61",
        label="RT60 (Sabine)", linewidth=2, markersize=8
    )

    # Gráfico para Eyring
    plt.plot(
        frecuencias, valores_rt60_eyring,
        marker="s", linestyle="-.", color="#58B3FF",
        label="RT60 (Eyring)", linewidth=2, markersize=8
    )

    # Estilo del gráfico
    plt.title("Comparación de RT60 por Frecuencia\nSabine vs Eyring", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Frecuencia (Hz)", fontsize=14)
    plt.ylabel("Tiempo de Reverberación (RT60, s)", fontsize=14)
    plt.ylim(0, max(max(valores_rt60, default=0), max(valores_rt60_eyring, default=0)) + 1)

    # Configurar el eje X (frecuencia en Hz) con rotación de etiquetas
    plt.xticks(
        frecuencias,
        [f"{f} Hz" for f in frecuencias],
        fontsize=12,
        rotation=45,  # Rotar etiquetas en el eje X
        ha="right"  # Alinear las etiquetas a la derecha
    )

    plt.grid(axis="both", color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

    # Leyenda
    plt.legend(fontsize=12, loc="upper right", title="Modelos", title_fontsize=13)

    # Anotaciones "Infinito" para casos relevantes
    for i, freq in enumerate(frecuencias):
        if rt60[freq] == "Infinito":
            plt.annotate("∞", (freq, max(valores_rt60) + 0.5), textcoords="offset points",
                         xytext=(-10, 5), color="#FF6F61", fontsize=12, fontweight="bold")
        if rt60_eyring[freq] == "Infinito":
            plt.annotate("∞", (freq, max(valores_rt60_eyring) + 0.5), textcoords="offset points",
                         xytext=(10, 5), color="#58B3FF", fontsize=12, fontweight="bold")

    # Línea base y ajustes finales
    plt.axhline(y=0, color="black", linewidth=0.8, linestyle="--", alpha=0.8)  # Línea base (0)
    plt.tight_layout()  # Ajuste automático de los márgenes
    plt.show()

def graficar_rt60(rt60, rt60_eyring):
    """
    Genera un gráfico comparativo del RT60 por frecuencia calculado con Sabine y Eyring.
    Retorna el gráfico como un objeto BytesIO.

    :param rt60: (dict) Resultados de RT60 obtenidos con la fórmula de Sabine.
                 Ejemplo: {125: 1.8, 250: 2.0, 500: 2.3, ...}
    :param rt60_eyring: (dict) Resultados de RT60 obtenidos con la fórmula de Eyring.
                        Ejemplo: {125: 1.7, 250: 1.9, 500: 2.2, ...}
    :return: BytesIO que contiene el gráfico en formato PNG.
    """
    # Extraer frecuencias y valores para Sabine
    frecuencias = list(rt60.keys())
    valores_rt60 = [rt60[f] if isinstance(rt60[f], (int, float)) else None for f in frecuencias]

    # Extraer frecuencias y valores para Eyring
    valores_rt60_eyring = [rt60_eyring[f] if isinstance(rt60_eyring[f], (int, float)) else None for f in frecuencias]

    # Crear el gráfico
    plt.figure(figsize=(10, 6))

    # Gráfico para Sabine
    plt.plot(
        frecuencias, valores_rt60,
        marker="o", linestyle="--", color="#FF6F61",
        label="RT60 (Sabine)", linewidth=2, markersize=8
    )

    # Gráfico para Eyring
    plt.plot(
        frecuencias, valores_rt60_eyring,
        marker="s", linestyle="-.", color="#58B3FF",
        label="RT60 (Eyring)", linewidth=2, markersize=8
    )

    # Estilo del gráfico
    plt.title("Comparación de RT60 por Frecuencia\nSabine vs Eyring", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Frecuencia (Hz)", fontsize=14)
    plt.ylabel("Tiempo de Reverberación (RT60, s)", fontsize=14)
    plt.ylim(0, max(max(valores_rt60, default=0), max(valores_rt60_eyring, default=0)) + 1)

    # Configurar el eje X (frecuencia en Hz) con rotación de etiquetas
    plt.xticks(
        frecuencias,
        [f"{f} Hz" for f in frecuencias],
        fontsize=12,
        rotation=45,  # Rotar etiquetas en el eje X
        ha="right"  # Alinear las etiquetas a la derecha
    )

    plt.grid(axis="both", color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

    # Leyenda
    plt.legend(fontsize=12, loc="upper right", title="Modelos", title_fontsize=13)

    # Anotaciones "Infinito" para casos relevantes
    for i, freq in enumerate(frecuencias):
        if rt60[freq] == "Infinito":
            plt.annotate("∞", (freq, max(valores_rt60) + 0.5), textcoords="offset points",
                         xytext=(-10, 5), color="#FF6F61", fontsize=12, fontweight="bold")
        if rt60_eyring[freq] == "Infinito":
            plt.annotate("∞", (freq, max(valores_rt60_eyring) + 0.5), textcoords="offset points",
                         xytext=(10, 5), color="#58B3FF", fontsize=12, fontweight="bold")

    # Línea base y ajustes finales
    plt.axhline(y=0, color="black", linewidth=0.8, linestyle="--", alpha=0.8)  # Línea base (0)
    plt.tight_layout()  # Ajuste automático de los márgenes

    # Guardar el gráfico en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")  # Guardar gráfico en formato PNG
    buffer.seek(0)  # Regresar el puntero al inicio del buffer

    plt.show()  # Mostrar el gráfico
    plt.close()  # Cerrar el gráfico para liberar memoria

    return buffer  # Retornar el objeto BytesIO con el gráfico


def calcular_resultados(datos):
    """
    Calcula los resultados acústicos de un salón, incluyendo:
    - Diccionarios Sabine y Eyring.
    - La gráfica de comparación de RT60.
    - Detalles del salón procesado.
    - Reporte de inteligibilidad si está disponible.

    :param datos: Diccionario con los datos de entrada para el cálculo.
    :return: Diccionario con los resultados incluyendo:
        - 'sabine_rt': Diccionario con tiempos RT60 según Sabine.
        - 'eyring_rt': Diccionario con tiempos RT60 según Eyring.
        - 'grafica': True si se generó la gráfica (la gráfica se muestra directamente).
        - 'salon': Diccionario del salón procesado con áreas y materiales.
        - 'reporte_inteligibilidad': Reporte si los datos de inteligibilidad están presentes, None en caso contrario.
    """
    # Obtener parámetros de entrada
    dimensiones = datos.get("dimensiones", {})
    materiales = datos.get("materiales", {})
    objetos_adicionales = datos.get("objetos_adicionales", [])
    inteligibilidad = datos.get("inteligibilidad", {})

    # Calcular dimensiones
    largo = dimensiones.get("largo", 0)
    ancho = dimensiones.get("ancho", 0)
    altura = dimensiones.get("altura", 0)

    # Calcular volumen del salón
    volumen = largo * ancho * altura

    # Calcular áreas básicas de las superficies
    superficies = calcular_areas_basicas(largo, ancho, altura)

    # Calcular área total sumando las superficies
    area_total = sum(superficies.values())

    # Obtener el salón completo con materiales y objetos adheridos
    salon = agregar_areas_materiales(datos)

    # Calcular absorción total y sus detalles
    absorcion, detalles = calcular_absorcion_total(salon, coeficientes)

    # Calcular los tiempos de reverberación con los modelos Sabine y Eyring
    sabine_rt = calcular_rt60_sabine(volumen, absorcion)
    eyring_rt = calcular_rt60_eyring(volumen, area_total, absorcion)

    # Generar la gráfica comparativa de RT60 y guardar en BytesIO
    grafico_buffer = graficar_rt60(sabine_rt, eyring_rt)  # Modificaremos `graficar_rt60`.

    # Inicializar el diccionario de resultados
    resultados = {
        "sabine_rt": sabine_rt,  # Resultados de Sabine
        "eyring_rt": eyring_rt,  # Resultados de Eyring
        "grafica": grafico_buffer,  # Gráfico guardado en BytesIO
        "salon": salon,  # Detalles del salón procesado
        "detalle": detalles,
        "reporte_inteligibilidad": None  # Por defecto, no hay reporte de inteligibilidad
    }

    # Si se proporciona información de inteligibilidad, generar el reporte
    if inteligibilidad:
        reporte = generar_reporte(inteligibilidad, volumen, area_total, sabine_rt)
        resultados["reporte_inteligibilidad"] = reporte

    # Retornar el diccionario de resultados
    return resultados





def generar_reporte(inteligibilidad, volumen, area_total, sabine_rt):


    distancia = inteligibilidad.get("distancia", 0)
    coeficiente_medio = inteligibilidad.get("coeficiente_medio", 0)
    volumen_sala = volumen
    tiempo_reverberacion = sabine_rt[2000]
    factor_directividad = 2
    superficie_total = area_total


    reporte = AlconsCalculator.generar_reporte(
        distancia= distancia,
        tr_2000Hz= tiempo_reverberacion,
        volumen_sala= volumen_sala,
        factor_directividad=2,  # Puedes asignar dinámicamente
        superficie_total= superficie_total,
        coef_medio_absor= coeficiente_medio
    )

    return reporte









''''
result = calcular_resultados(salon)

datos = agregar_areas_materiales(salon)
absorsionTotal, detalles = calcular_absorcion_total(datos, coeficientes)
superficies = calcular_areas_basicas(datos)
frecuencias = [125, 250, 500, 1000, 2000, 4000]

print("absorsion", absorsionTotal)
print("detalles", detalles)

rtsabine= calcular_rt60_sabine(result, absorsionTotal)
rteiting = calcular_rt60_eyring(result, sum(superficies.values()), absorsionTotal)

graficar_comparacion_rt60(frecuencias, rtsabine, rteiting)
graficar_rt60(rtsabine, rteiting)


'''


