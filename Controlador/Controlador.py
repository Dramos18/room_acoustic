from Modelo.excel import cargar_coeficientes, cargar_coeficientes_dos

dataframe_materiales = cargar_coeficientes()
materiales_dos = cargar_coeficientes_dos()


def obtener_lista_materiales():
    """Devuelve la lista de materiales disponibles a partir del DataFrame proporcionado."""
    if materiales_dos is not None:
        lista_materiales = materiales_dos["Material"].tolist()
        return lista_materiales
    return []

def obtener_coeficientes_materiales():
    df = materiales_dos
    coeficientes = {}
    for _, row in df.iterrows():
        coeficientes[row['Material']] = {  # Frecuencias por material
            125: row['125 Hz'], 250: row['250 Hz'], 500: row['500 Hz'],
            1000: row['1000 Hz'], 2000: row['2000 Hz'], 4000: row['4000 Hz']
        }
    return coeficientes

