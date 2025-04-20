salones = {
    "Salón Tipo 1": {
        "numero_salon": "101 - 104",
        "dimensiones": {"largo": 9.94, "ancho": 5.87, "altura": 3.67},
        "materiales": {
            "Techo": [("Hormigón rústico", None)],
            "Piso": [("Hormigón alisado o monolítico", None)],
            "Pared Frontal": [("Revoque rugoso", None), ("Ventana de vidrio común", 6.2475), ("Puerta", 1.5)],
            "Pared Trasera": [("Revoque rugoso", None), ("Ventana de vidrio común", 10.29)],
            "Pared Izquierda": [("Revoque rugoso", None)],
            "Pared Derecha": [("Revoque rugoso", None)]
        },
        "objetos_adicionales": [{"nombre": "sillas", "area_efectiva": 45, "material": "Butaca tapizada con plástico"}]
    },
    "Salón Tipo 2": {
            "numero_salon": "105 - 106",
            "dimensiones": {"largo": 9.57, "ancho": 5.88, "altura": 2.52},
            "materiales": {
                "Techo": [("Hormigón rústico", None)],
                "Piso": [("Hormigón alisado o monolítico", None)],
                "Pared Frontal": [("Revoque rugoso", None), ("Puerta", 1.5)],
                "Pared Trasera": [("Revoque rugoso", None), ("Ventana de vidrio común", 42.18)],
                "Pared Izquierda": [("Revoque rugoso", None)],
                "Pared Derecha": [("Revoque rugoso", None)]
            },
            "objetos_adicionales": [{"nombre": "sillas", "area_efectiva": 45, "material": "Butaca tapizada con plástico"}]
        },


}

ejemplo={
    'dimensiones': {'largo': 12.0, 'ancho': 121.0, 'altura': 22.0},
    'materiales': {
        'Frontal': {'material': 'Cortina veneciana de metal',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio de espejo', 'area': 10.0}, {
                        'nombre': 'Puerta', 'material': 'Puerta', 'area': 1.5}]},
        'Trasera': {'material': 'Cortina veneciana de metal',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio pesado', 'area': 12.0}]},
        'Izquierda': {'material': 'Cortina veneciana de metal'},
        'Derecha': {'material': 'Cortina veneciana de metal'},
        'Piso': {'material': 'Cortina veneciana de metal'},
        'Techo': {'material': 'Butaca semi-tapizada'}},
    'objetos_adicionales': [{
        'nombre': 'Sillas', 'material': 'Cortina veneciana de metal', 'cantidad': 10.0}],
    'inteligibilidad': None}
ejemploConArea = {
    'dimensiones': {'largo': 12.0, 'ancho': 121.0, 'altura': 22.0},
    'materiales': {
        'Frontal': {'material': 'Cortina veneciana de metal',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio de espejo', 'area': 10.0}, {
                        'nombre': 'Puerta', 'material': 'Puerta', 'area': 1.5}], 'area': 2650.5},
        'Trasera': {'material': 'Cortina veneciana de metal',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio pesado', 'area': 12.0}],
                    'area': 2650.0},
        'Izquierda': {'material': 'Cortina veneciana de metal',
                      'area': 264.0},
        'Derecha': {'material': 'Cortina veneciana de metal',
                    'area': 264.0},
        'Piso': {'material': 'Cortina veneciana de metal',
                 'area': 1452.0},
        'Techo': {'material': 'Butaca semi-tapizada',
                  'area': 1452.0}},
    'objetos_adicionales': [{
        'nombre': 'Sillas', 'material': 'Cortina veneciana de metal', 'cantidad': 10.0}],
    'inteligibilidad': None}
