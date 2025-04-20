from Controlador.Controlador import obtener_lista_materiales, obtener_coeficientes_materiales
import math
import matplotlib.pyplot as plt
from Modelo.alcons2 import AlconsCalculator

# Obtener los coeficientes de absorción acústica desde el controlador
coeficientes = obtener_coeficientes_materiales()


# =============================
# Función: calcular_areas_basicas
# =============================
def calcular_areas_basicas(largo, ancho, altura):
    """
    Calcula áreas de las seis superficies de un salón rectangular:
    paredes (frontal, trasera, izquierda, derecha), piso y techo.

    :param largo: Longitud del salón (en metros).
    :param ancho: Anchura del salón (en metros).
    :param altura: Altura del salón (en metros).
    :return: Diccionario con las áreas de las superficies.
    """
    # Área base de cada superficie
    area_pared_frontal = ancho * altura
    area_pared_lateral = largo * altura
    area_piso = largo * ancho
    area_techo = area_piso  # El techo tiene el mismo área que el piso

    # Crear un diccionario con las áreas calculadas para cada superficie
    superficies = {
        "Frontal": area_pared_frontal,
        "Trasera": area_pared_frontal,  # Igual a la pared frontal
        "Izquierda": area_pared_lateral,
        "Derecha": area_pared_lateral,  # Igual a la pared izquierda
        "Piso": area_piso,
        "Techo": area_techo,
    }
    return superficies


# =============================
# Función: agregar_areas_materiales
# =============================
def agregar_areas_materiales(datos):
    """
    Calcula las áreas reales de las superficies del salón y las agrega al diccionario 'materiales'.
    Resta el área de los objetos adheridos (como ventanas y puertas) si se especifican,
    y valida que estas áreas no excedan el área total de su superficie correspondiente.

    :param datos: Diccionario de información del salón, con claves:
        - 'dimensiones': contiene largo, ancho y altura del salón.
        - 'materiales': contiene los materiales de las superficies.
    :return: Diccionario 'datos' actualizado con las áreas ajustadas.
    """
    # Extraer dimensiones del salón
    dimensiones = datos.get("dimensiones", {})
    largo = dimensiones.get("largo", 0)  # Longitud
    ancho = dimensiones.get("ancho", 0)  # Anchura
    altura = dimensiones.get("altura", 0)  # Altura

    # Calcular áreas básicas a partir de las dimensiones dadas
    superficies_basicas = calcular_areas_basicas(largo, ancho, altura)

    # Obtener el diccionario de materiales en 'datos'
    materiales = datos.get("materiales", {})

    # Iterar sobre cada superficie/zona especificada en el diccionario de materiales
    for zona, propiedades in materiales.items():
        # Obtener el área base de la superficie
        area_superficie = superficies_basicas.get(zona, 0)

        # Calcular el área de los objetos adheridos (es decir, ventanas, puertas, etc.)
        objetos_adheridos = propiedades.get("objetos_adheridos", [])
        area_adheridos = sum(objeto.get("area", 0) for objeto in objetos_adheridos)

        # Validar que el área adherida no exceda el área total de la superficie
        if area_adheridos > area_superficie:
            raise ValueError(
                f"El área adherida total en '{zona}' ({area_adheridos:.2f} m²) excede el área disponible "
                f"de la superficie ({area_superficie:.2f} m²)."
            )

        # Restar el área adherida del área total para obtener el área final
        area_final = area_superficie - area_adheridos

        # Asegurarse de que el área final no sea negativa (por posibles problemas con los cálculos o datos)
        area_final = max(area_final, 0)

        # Actualizar el diccionario de materiales con el área calculada
        materiales[zona]["area"] = area_final

    # Retornar el diccionario de datos actualizado
    return datos


# =============================
# Función: calcular_absorcion_total
# =============================
def calcular_absorcion_total(material, coeficientes, frecuencias=None):
    """
    Calcula el coeficiente de absorción total (A) para cada frecuencia, considerando:

    - Las áreas de superficies y los materiales utilizados.
    - Los objetos adheridos en las superficies.
    - Los objetos adicionales en el salón.

    :param material: Diccionario con información del salón, incluyendo 'materiales', 'objetos_adheridos'.
    :param coeficientes: Diccionario de coeficientes de absorción por material y frecuencia.
    :param frecuencias: Lista de frecuencias (opcional, si no se proporciona se usan por defecto).
    :return:
        - absorcion_total: Diccionario con la absorción total por frecuencia.
        - detalles: Lista con información detallada del cálculo para cada zona/material.
    """
    # Usar frecuencias estándar si no se han especificado
    if frecuencias is None:
        frecuencias = [125, 250, 500, 1000, 2000, 4000]

    # Inicializar la absorción total por frecuencia en cero
    absorcion_total = {f: 0 for f in frecuencias}
    detalles = []  # Lista para almacenar detalles del cálculo

    # Obtener el diccionario de materiales desde los datos
    materiales = material.get("materiales", {})

    # Iterar sobre cada superficie/zona
    for zona, propiedades in materiales.items():
        # Obtener área final de la superficie (ajustada con objetos adheridos)
        area_superficie = propiedades.get("area", 0)
        material_base = propiedades.get("material")  # Material de esta superficie

        # Si el material base tiene coeficientes, calcular su contribución
        if material_base in coeficientes:
            for f in frecuencias:
                coef = coeficientes[material_base].get(f, 0)
                absorcion_total[f] += area_superficie * coef
                detalles.append({
                    "zona": zona,
                    "material": material_base,
                    "frecuencia": f,
                    "area_aplicada": area_superficie,
                    "coeficiente": coef,
                    "absorcion": area_superficie * coef,
                })

        # Calcular la absorción de objetos adheridos en esta superficie
        objetos_adheridos = propiedades.get("objetos_adheridos", [])
        for objeto in objetos_adheridos:
            material_adherido = objeto.get("material")  # Material del objeto adherido
            area_adherida = objeto.get("area", 0)  # Área del objeto
            if material_adherido in coeficientes:
                for f in frecuencias:
                    coef = coeficientes[material_adherido].get(f, 0)
                    absorcion_total[f] += area_adherida * coef
                    detalles.append({
                        "zona": zona,
                        "material": material_adherido,
                        "frecuencia": f,
                        "area_aplicada": area_adherida,
                        "coeficiente": coef,
                        "absorcion": area_adherida * coef,
                    })

    # Calcular absorción de objetos adicionales en el salón
    objetos_adicionales = materiales.get("objetos_adicionales", [])
    for objeto in objetos_adicionales:
        material = objeto.get("material")  # Material del objeto adicional
        cantidad = objeto.get("cantidad", 1)  # Número de objetos
        area_efectiva = objeto.get("area_efectiva", 0) * cantidad  # Área total

        if material in coeficientes:
            for f in frecuencias:
                coef = coeficientes[material].get(f, 0)
                absorcion_total[f] += area_efectiva * coef
                detalles.append({
                    "zona": "Objeto Adicional",
                    "material": material,
                    "frecuencia": f,
                    "area_aplicada": area_efectiva,
                    "coeficiente": coef,
                    "absorcion": area_efectiva * coef,
                })

    return absorcion_total, detalles


# =============================
# Funciones de cálculo de RT60
# =============================

# RT60 (Sabine)
def calcular_rt60_sabine(volumen, absorcion_total, decimales=2):
    """
    Calcula el RT60 usando la fórmula de Sabine.
    """
    rt60 = {}
    for frecuencia, absorcion in absorcion_total.items():
        if absorcion > 0:
            rt60[frecuencia] = round(0.161 * volumen / absorcion, decimales)
        else:
            rt60[frecuencia] = "Infinito"  # Reverberación infinita si no hay absorción
    return rt60


# RT60 (Eyring)
def calcular_rt60_eyring(volumen, area_total, absorcion_total, decimales=2):
    """
    Calcula el RT60 usando la fórmula de Eyring.
    """
    rt60 = {}
    for frecuencia, absorcion in absorcion_total.items():
        if absorcion > 0:
            alpha_prom = absorcion / area_total
            if 1 - alpha_prom > 0:
                rt60[frecuencia] = round(-0.161 * volumen / (area_total * math.log(1 - alpha_prom)), decimales)
            else:
                rt60[frecuencia] = "Infinito"
        else:
            rt60[frecuencia] = "Infinito"
    return rt60

def graficar_rt60(rt60, rt60_eyring):
    """
    Genera un gráfico comparativo del RT60 (tiempo de reverberación) por frecuencia,
    calculado a partir de los modelos de Sabine y Eyring.

    :param rt60: (dict) Tiempos de reverberación calculados usando la fórmula de Sabine.
                 Ejemplo: {125: 1.8, 250: 2.0, 500: 2.3, ...}
    :param rt60_eyring: (dict) Tiempos de reverberación calculados usando la fórmula de Eyring.
                        Ejemplo: {125: 1.7, 250: 1.9, 500: 2.2, ...}
    :return: None. Muestra directamente el gráfico.
    """
    # ==========================
    # Preparar datos para el gráfico
    # ==========================
    # Extraer las frecuencias comunes de los resultados
    frecuencias = list(rt60.keys())

    # Obtener los valores de RT60 calculados con Sabine, verificando que sean números (ignorar "Infinito")
    valores_rt60 = [rt60[f] if isinstance(rt60[f], (int, float)) else None for f in frecuencias]

    # Obtener los valores de RT60 calculados con Eyring, verificando que sean números (ignorar "Infinito")
    valores_rt60_eyring = [rt60_eyring[f] if isinstance(rt60_eyring[f], (int, float)) else None for f in frecuencias]

    # ==========================
    # Crear el gráfico
    # ==========================
    # Crear una figura personalizada para el gráfico con un tamaño específico
    plt.figure(figsize=(10, 6))

    # Gráfico para Sabine (línea discontinua con círculos)
    plt.plot(
        frecuencias, valores_rt60,
        marker="o", linestyle="--", color="#FF6F61",  # Círculos y color naranja
        label="RT60 (Sabine)", linewidth=2, markersize=8  # Anchura y tamaño de los marcadores
    )

    # Gráfico para Eyring (línea punteada con cuadrados)
    plt.plot(
        frecuencias, valores_rt60_eyring,
        marker="s", linestyle="-.", color="#58B3FF",  # Cuadrados y color azul
        label="RT60 (Eyring)", linewidth=2, markersize=8  # Anchura y tamaño de los marcadores
    )

    # ==========================
    # Estilo y personalización del gráfico
    # ==========================
    # Título
    plt.title("Comparación de RT60 por Frecuencia\nSabine vs Eyring",
              fontsize=18, fontweight="bold", pad=20)

    # Etiquetas de los ejes
    plt.xlabel("Frecuencia (Hz)", fontsize=14)
    plt.ylabel("Tiempo de Reverberación (RT60, s)", fontsize=14)

    # Establecer el límite vertical para que todos los valores se muestren correctamente
    plt.ylim(0, max(max(valores_rt60, default=0), max(valores_rt60_eyring, default=0)) + 1)

    # Configurar las etiquetas del eje X (frecuencias) con rotación para mejor visibilidad
    plt.xticks(
        frecuencias,
        [f"{f} Hz" for f in frecuencias],  # Formato para las etiquetas ("Hz")
        fontsize=12,
        rotation=45,  # Rotar etiquetas ligeramente
        ha="right"  # Alinear las etiquetas a la derecha
    )

    # Agregar una cuadrícula para mejorar la legibilidad
    plt.grid(axis="both", color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

    # Leyenda en la parte superior derecha del gráfico
    plt.legend(fontsize=12, loc="upper right", title="Modelos", title_fontsize=13)

    # ==========================
    # Añadir anotaciones para RT60 "Infinito"
    # ==========================
    for i, freq in enumerate(frecuencias):
        # Si RT60 calculado con Sabine es "Infinito", añadir una anotación ∞
        if rt60[freq] == "Infinito":
            plt.annotate(
                "∞", (freq, max(valores_rt60) + 0.5),  # Coordenadas de la anotación
                textcoords="offset points",
                xytext=(-10, 5),  # Desplazar ligeramente hacia arriba
                color="#FF6F61", fontsize=12, fontweight="bold"
            )
        # Si RT60 calculado con Eyring es "Infinito", añadir una anotación ∞
        if rt60_eyring[freq] == "Infinito":
            plt.annotate(
                "∞", (freq, max(valores_rt60_eyring) + 0.5),  # Coordenadas de la anotación
                textcoords="offset points",
                xytext=(10, 5),  # Desplazar ligeramente hacia arriba
                color="#58B3FF", fontsize=12, fontweight="bold"
            )

    # ==========================
    # Estilo final y visualización
    # ==========================
    # Línea base horizontal en el eje y=0 (para claridad)
    plt.axhline(y=0, color="black", linewidth=0.8, linestyle="--", alpha=0.8)

    # Ajustar automágicamente los márgenes para evitar cortes en el diseño
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()



def calcular_resultados(datos):
    """
    Calcula los resultados acústicos para un salón, incluyendo:
    - Absorción total por frecuencia.
    - Tiempos de reverberación (RT60) usando los modelos de Sabine y Eyring.
    - Generación de gráficos comparativos de RT60.
    - Generación de reporte, si hay datos de inteligibilidad.

    :param datos: Diccionario con información del salón, incluyendo:
        - dimensiones: Diccionario con 'largo', 'ancho', 'altura'.
        - materiales: Diccionario con las superficies y sus propiedades.
        - objetos_adicionales: Lista opcional con objetos adicionales (como muebles).
        - inteligibilidad: Información para calcular inteligibilidad, si es aplicable.
    :return: Reporte generado por la función `generar_reporte`, o None si no se proporciona inteligibilidad.
    """
    # Obtener dimensiones del salón desde el diccionario 'datos'
    dimensiones = datos.get("dimensiones", {})
    largo = dimensiones.get("largo", 0)
    ancho = dimensiones.get("ancho", 0)
    altura = dimensiones.get("altura", 0)

    # Calcular el volumen del salón
    volumen = largo * ancho * altura

    # Calcular áreas básicas de las superficies (sin ajustar por objetos adheridos)
    superficies = calcular_areas_basicas(largo, ancho, altura)

    # Calcular el área total sumando todas las superficies
    area_total = sum(superficies.values())

    # Ajustar las áreas de las superficies con objetos adheridos
    salon = agregar_areas_materiales(datos)

    # Calcular la absorción total y obtener detalles del cálculo
    absorcion, detalles = calcular_absorcion_total(salon, coeficientes)

    # Calcular los tiempos de reverberación usando los modelos de Sabine y Eyring
    sabine_rt = calcular_rt60_sabine(volumen, absorcion)
    eyring_rt = calcular_rt60_eyring(volumen, area_total, absorcion)

    # Graficar los resultados de RT60 (Sabine vs. Eyring)
    graficar_rt60(sabine_rt, eyring_rt)

    # Si se proporciona información sobre inteligibilidad, generar un reporte
    inteligibilidad = datos.get("inteligibilidad", {})
    if inteligibilidad is not None:
        # Llamar a la función para generar el reporte con los datos obtenidos
        reporte = generar_reporte(inteligibilidad, volumen, area_total, sabine_rt)
        return reporte

    # Retornar None si los datos de inteligibilidad no están presentes
    return None


def generar_reporte(inteligibilidad, volumen, area_total, sabine_rt):
    """
    Genera un reporte acústico del salón utilizando los datos de inteligibilidad y los resultados de cálculo.

    Este reporte evalúa factores clave como tiempo de reverberación, volumen,
    coeficiente promedio de absorción, y otros relacionados con la inteligibilidad del espacio.

    :param inteligibilidad: Diccionario con parámetros específicos para el cálculo, incluyendo:
        - 'distancia': Distancia desde el emisor hasta el receptor.
        - 'coeficiente_medio': Coeficiente de absorción promedio de la sala.
    :param volumen: Volumen del salón en metros cúbicos.
    :param area_total: Área total de las superficies del salón en metros cuadrados.
    :param sabine_rt: Diccionario con tiempos de reverberación RT60 calculados con el modelo de Sabine.
                      Se selecciona TR en 2000 Hz (`sabine_rt.get("2000")`) para el cálculo.
    :return: Reporte generado por la clase AlconsCalculator.
    """
    # Extraer parámetros de inteligibilidad desde el diccionario
    distancia = inteligibilidad.get("distancia", 0)  # Distancia al receptor (m)
    coeficiente_medio = inteligibilidad.get("coeficiente_medio", 0)  # Coeficiente medio de absorción
    volumen_sala = volumen  # Volumen del salón
    tiempo_reverberacion = sabine_rt.get("2000", 0)  # RT60 en 2000 Hz
    factor_directividad = 2  # Factor de directividad (valor fijo)
    superficie_total = area_total  # Área total de las superficies

    # Generar reporte llamando al metodo 'generar_reporte' de la clase AlconsCalculator
    reporte = AlconsCalculator.generar_reporte(
        distancia=distancia,  # Distancia desde el emisor hasta el receptor
        tr_2000Hz=tiempo_reverberacion,  # Tiempo de reverberación a 2000 Hz
        volumen_sala=volumen_sala,  # Volumen de la sala
        factor_directividad=factor_directividad,  # Directividad predeterminada (puede ser ajustada si es necesario)
        superficie_total=superficie_total,  # Área total del salón
        coef_medio_absor=coeficiente_medio  # Coeficiente de absorción promedio
    )

    return reporte  # Retornar el reporte generado

