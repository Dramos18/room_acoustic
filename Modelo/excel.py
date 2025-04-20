import pandas as pd
import os

RUTA_COEFICIENTES = os.path.join(os.path.dirname(__file__), 'Datos\\coeficientes.xlsx')

def cargar_coeficientes():
    """Carga la tabla de coeficientes de absorción desde Excel."""
    try:
        df = pd.read_excel(RUTA_COEFICIENTES)
        print("Coeficientes cargados correctamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los coeficientes: {e}")
        return None
