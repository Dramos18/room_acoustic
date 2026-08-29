import pandas as pd
import os

RUTA_COEFICIENTES = os.path.join(os.path.dirname(__file__), '..\\Datos\\coeficientes.xlsx')
RUTA_COEFICIENTES_COMUN = os.path.join(os.path.dirname(__file__), '..\\Datos\\coefs_absorcion.xlsx')

def cargar_coeficientes():
    """Carga la tabla de coeficientes de absorción desde Excel."""
    try:
        df = pd.read_excel(RUTA_COEFICIENTES)
        print("Coeficientes cargados correctamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los coeficientes: {e}")
        return None

def cargar_coeficientes_dos():
    """Carga la tabla de coeficientes de absorción desde Excel."""
    try:
        df = pd.read_excel(RUTA_COEFICIENTES_COMUN)
        print("Coeficientes cargados correctamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los coeficientes: {e}")
        return None
