import math



def calcular_constante_recinto(superficie_total, coef_medio_absor):
    """
        Calcula la constante del recinto acústico.

        Args:
            superficie_total (float): Superficie total del recinto en metros cuadrados.
            coef_medio_absor (float): Coeficiente medio de absorción del recinto (0 <= coef_medio_absor < 1).

        Returns:
            float: Constante del recinto.
        """
    if coef_medio_absor == 1:
        raise ValueError("El coeficiente medio de absorción debe ser diferente de 1.")
    return (superficie_total * coef_medio_absor) / (1 - coef_medio_absor)


def calcular_distancia_critica(factor_directividad, constante_recinto):
    """
        Calcula la distancia crítica utilizando el factor de directividad y la constante del recinto.

        Args:
            factor_directividad (float): Factor de directividad del sistema.
            constante_recinto (float): Constante del recinto.

        Returns:
            float: Distancia crítica del sistema.
        """
    if constante_recinto <= 0 or factor_directividad <= 0:
        raise ValueError("La constante del recinto y el factor de directividad deben ser mayores que 0.")
    return 0.14 * (math.sqrt(factor_directividad * constante_recinto))


def calcular_dc(volumen, tr_2000Hz):
    """
        Calcula la distancia crítica basada en el volumen de la sala y el tiempo de reverberación.

        Args:
            volumen (float): Volumen de la sala en metros cúbicos.
            tr_2000Hz (float): Tiempo de reverberación en segundos (para banda de 2000Hz).

        Returns:
            float: Distancia crítica calculada.
        """
    if volumen <= 0 or tr_2000Hz <= 0:
        raise ValueError("El volumen de la sala y el tiempo de reverberación deben ser mayores que 0.")
    return 0.21 * (math.sqrt(volumen / tr_2000Hz))


def calcular_alcons(distancia, tr_2000Hz, volumen_sala, factor_directividad, distancia_critica):
    """
        Calcula el porcentaje de pérdida de inteligibilidad de palabra (%Alcons).

        Args:
            distancia (float): Distancia al oyente en metros.
            tr_2000Hz (float): Tiempo de reverberación (en segundos, banda 2000Hz).
            volumen_sala (float): Volumen total del recinto en metros cúbicos.
            factor_directividad (float): Factor de directividad del sistema.
            distancia_critica (float): Distancia crítica calculada.

        Returns:
            float: %Alcons (pérdida de inteligibilidad).
        """
    if distancia <= 0 or tr_2000Hz <= 0 or volumen_sala <= 0 or factor_directividad <= 0:
        raise ValueError("Todos los parámetros deben ser mayores que 0.")

    if distancia <= 3.16 * distancia_critica:
        print("Distancia menor a 3.16 veces la distancia crítica.")
        alcons = (200 * math.pow(distancia, 2) * math.pow(tr_2000Hz, 2)) / (volumen_sala * factor_directividad)
    else:
        print("Distancia mayor a 3.16 veces la distancia crítica.")
        alcons = 9 * tr_2000Hz

    return alcons


def evaluar_alcons(alcons):
    """
    Evalúa el porcentaje de ALcons y retorna un mensaje acorde al nivel de inteligibilidad.

    Args:
        alcons (float): Porcentaje de ALcons calculado.

    Returns:
        str: Mensaje indicando la calidad de inteligibilidad según el valor de ALcons.
    """
    if alcons < 0:
        return "Error: El valor de ALcons no puede ser negativo. Verifique los datos ingresados."

    if 0 <= alcons <= 1.4:
        print("🌟 Excelente: Las condiciones acústicas son ideales. "
                "La inteligibilidad de las palabras es máxima y no se esperan problemas.")
    elif 1.5 <= alcons <= 5:
        print("😊 Buena: El rendimiento acústico es adecuado. "
                "La inteligibilidad de la palabra es muy buena con ligeras pérdidas.")
    elif 5.1 <= alcons <= 11.4:
        return ("😐 Regular: La sala presenta deficiencias acústicas notables. "
                "La inteligibilidad de las palabras puede ser afectada en áreas específicas.")
    elif 11.5 <= alcons <= 24.4:
        return ("😟 Pobre: Las condiciones no son ideales. "
                "Es probable que los oyentes tengan dificultades para entender palabras con claridad.")
    elif 24.5 <= alcons <= 47:
        return ("🛑 Mala: La inteligibilidad de las palabras es insuficiente. "
                "Se necesitan mejoras significativas en el diseño acústico del espacio.")
    else:
        return ("🔴 Crítico: El valor de ALcons está fuera de rango aceptable. "
                "La acústica es extremadamente deficiente y requiere atención inmediata.")


def main():
    # Parámetros del problema
    distancia = 1.5  # Distancia en metros
    tr_2000Hz = 1.89  # Tiempo de reverberación en segundos
    volumen_sala = 214.14  # Volumen en m³
    factor_directividad = 2  # Factor de directividad
    superficie_total = 293.04  # Superficie del recinto en m²
    coef_medio_absor = 0.24  # Coeficiente medio de absorción

    try:
        # Cálculos
        constante_recinto = calcular_constante_recinto(superficie_total, coef_medio_absor)
        print(f"Constante del recinto (R): {constante_recinto:.2f}")

        distancia_critica = calcular_distancia_critica(factor_directividad, constante_recinto)
        print(f"Distancia crítica (Dc1): {distancia_critica:.2f} m")

        dc_alt = calcular_dc(volumen_sala, tr_2000Hz)
        print(f"Distancia crítica alternativa (Dc2): {dc_alt:.2f} m")

        alcons = calcular_alcons(distancia, tr_2000Hz, volumen_sala, factor_directividad, distancia_critica)
        print(f"%Alcons: {alcons:.2f}%")

        evaluacion = evaluar_alcons(alcons)

    except ValueError as e:
        print(f"Error en el cálculo: {e}")


if __name__ == "__main__":
    main()
