from Modelo.calculoRT2 import calcular_resultados
#from Modelo.calculoRT import calcular_resultados


def procesar_datos(diccionario):
    """
    Procesa el diccionario recibido desde la interfaz gráfica.
    """
    print("Diccionario recibido en el controlador:", diccionario)

    # Ahora puedes pasarlo al modelo o hacer cálculos con él
    reporte = calcular_resultados(diccionario)
    return reporte




