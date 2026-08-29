import math


class AlconsCalculator:
    @staticmethod
    def calcular_constante_recinto(superficie_total, coef_medio_absor):
        """
        Calcula la constante del recinto acústico.
        """
        if coef_medio_absor == 1:
            raise ValueError("El coeficiente medio de absorción debe ser diferente de 1.")
        return   (superficie_total * coef_medio_absor) / (1 - coef_medio_absor)

    @staticmethod
    def calcular_distancia_critica(factor_directividad, constante_recinto):
        """
        Calcula la distancia crítica utilizando el factor de directividad y la constante del recinto.
        """
        if constante_recinto <= 0 or factor_directividad <= 0:
            raise ValueError("La constante del recinto y el factor de directividad deben ser mayores que 0.")
        return 0.14 * (math.sqrt(factor_directividad * constante_recinto))

    @staticmethod
    def calcular_dc(volumen, tr_2000Hz):
        """
        Calcula la distancia crítica basada en el volumen de la sala y el tiempo de reverberación.
        """
        if volumen <= 0 or tr_2000Hz <= 0:
            raise ValueError("El volumen de la sala y el tiempo de reverberación deben ser mayores que 0.")
        return 0.21 * (math.sqrt(volumen / tr_2000Hz))

    @staticmethod
    def calcular_alcons(distancia, tr_2000Hz, volumen_sala, factor_directividad, distancia_critica):
        """
        Calcula el porcentaje de pérdida de inteligibilidad de palabra (%Alcons).
        """
        if any(param <= 0 for param in [distancia, tr_2000Hz, volumen_sala, factor_directividad]):
            raise ValueError("Todos los parámetros deben ser mayores que 0.")

        if distancia <= 3.16 * distancia_critica:
            alcons = (200 * math.pow(distancia, 2) * math.pow(tr_2000Hz, 2)) / (volumen_sala * factor_directividad)
        else:
            alcons = 9 * tr_2000Hz

        return round(alcons, 2)

    @staticmethod
    def evaluar_alcons(alcons):
        """
        Evalúa el %ALCONS y proporciona una calificación de inteligibilidad.
        """
        if alcons < 0:
            return "Error: El valor de ALcons no puede ser negativo. Verifique los datos ingresados."

        if 0 <= alcons <= 1.4:
            return " Excelente: Condiciones acústicas ideales. Máxima inteligibilidad."
        elif alcons <= 5:
            return " Buena: Rendimiento acústico adecuado con ligeras pérdidas."
        elif alcons <= 11.4:
            return " Regular: Deficiencias acústicas notables. La inteligibilidad puede verse afectada."
        elif alcons <= 24.4:
            return " Pobre: Dificultades para interpretar palabras con claridad."
        elif alcons <= 47:
            return " Mala: Inteligibilidad insuficiente. Necesita mejoras significativas."
        else:
            return " Crítico: Acústica extremadamente deficiente. Requiere atención urgente."

    @staticmethod
    def generar_reporte(distancia, tr_2000Hz, volumen_sala, factor_directividad, superficie_total, coef_medio_absor):
        """
        Genera un reporte completo basado en los cálculos realizados.
        """
        try:
            # Cálculos básicos
            constante_recinto = AlconsCalculator.calcular_constante_recinto(superficie_total, coef_medio_absor)
            #distancia_critica = AlconsCalculator.calcular_distancia_critica(factor_directividad, constante_recinto)
            distancia_critica = AlconsCalculator.calcular_dc(volumen_sala, tr_2000Hz)
            alcons = AlconsCalculator.calcular_alcons(
                distancia, tr_2000Hz, volumen_sala, factor_directividad, distancia_critica
            )
            evaluacion = AlconsCalculator.evaluar_alcons(alcons)

            # Estructura el reporte como un diccionario
            reporte = {
                "Constante del Recinto (R)": round(constante_recinto, 2),
                "Distancia Crítica (Dc)": round(distancia_critica, 2),
                "%ALCONS": alcons,
                "Evaluación": evaluacion,
                "Detalles": {
                    "Distancia al oyente": distancia,
                    "Tiempo de Reverberación": tr_2000Hz,
                    "Volumen de la sala": volumen_sala,
                    "Factor de Directividad": factor_directividad,
                    "Superficie Total": superficie_total,
                    "Coeficiente Medio de Absorción": coef_medio_absor,
                }
            }
            return reporte

        except ValueError as e:
            return {"Error": str(e)}



