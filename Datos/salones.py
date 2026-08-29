def obtener_salones(salonTipo1, salonTipo2, salonTipo4, salonTipo5, salonTipo6, salonTipo7,
                    salonTipo8, salonTipo9, salonTipo10, salonTipo11, salonTipo12, salonTipo13,
                    salonTipo14, salonTipo15, salonTipo16, salonTipo17, salonTipo18, salonTipo20,
                    salonTipo21, salonTipo22, salonTipo23):
    salones=[salonTipo1, salonTipo2, salonTipo4, salonTipo5, salonTipo6, salonTipo7,
             salonTipo8, salonTipo9, salonTipo10, salonTipo11, salonTipo12, salonTipo13,
             salonTipo14, salonTipo15, salonTipo16, salonTipo17, salonTipo18, salonTipo20,
             salonTipo21, salonTipo22, salonTipo23]
    return salones

DiccionarioRecibido={
    'Tipo': 'Salón tipo 1', 'aulas': '101-104',
    'dimensiones': {'largo': 9.94, 'ancho': 5.87, 'altura': 3.67},
    'materiales': {'Frontal': {'material': 'Revoque rugoso',
                               'objetos_adheridos': [{
                                   'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                                   'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
                   'Trasera': {'material': 'Revoque rugoso',
                               'objetos_adheridos': [{
                                   'nombre': 'Ventana', 'material': 'Vidrio', 'area': 10.29}]},
                   'Izquierda': {'material': 'Revoque rugoso'},
                   'Derecha': {'material': 'Revoque rugoso', 'objetos_adheridos': [{
                       'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso',
                       'area': 2.737}]}, 'Piso': {'material': 'Hormigón rasado o monolítico'},
                   'Techo': {'material': 'Hormigón rústico'}}, 'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 42.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.24}}

DiccionarioEnviado= {'sabine_rt': {125: 28.22, 250: 27.6, 500: 27.01, 1000: 18.27, 2000: 13.95, 4000: 13.95},
                     'eyring_rt': {125: 28.15, 250: 27.53, 500: 26.94, 1000: 18.19, 2000: 13.88, 4000: 13.88},
                     #'grafica': <_io.BytesIO object at 0x000001E281532B80>
                     }
salon= {'Tipo':'Salón tipo 1', 'aulas': '101-104',
          'dimensiones': {'largo': 9.94, 'ancho': 5.87, 'altura': 3.67},
          'materiales': {
              'Frontal': {'material': 'Revoque rugoso',
                          'objetos_adheridos': [{
                              'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                              'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}],
                          'area': 13.5984},
              'Trasera': {'material': 'Revoque rugoso',
                          'objetos_adheridos': [{
                              'nombre': 'Ventana', 'material': 'Vidrio', 'area': 10.29}],
                          'area': 11.2529},
              'Izquierda': {'material': 'Revoque rugoso',
                            'area': 36.4798},
              'Derecha': {'material': 'Revoque rugoso',
                          'objetos_adheridos': [{
                              'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}],
                          'area': 33.742799999999995},
              'Piso': {'material': 'Hormigón rasado o monolítico',
                       'area': 58.3478},
              'Techo': {'material': 'Hormigón rústico',
                        'area': 58.3478}},
          'objetos_adicionales': [{
              'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 42.0}, {
              'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
          'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.24}},
detalle= [{
    'zona': 'Derecha', 'material': 'Parquet de madera sobre contrapiso',
             'frecuencia': 125,
             'area_aplicada': 2.737,
             'coeficiente': 0.02,
             'absorcion': 0.054740000000000004}, {
    'zona': 'Derecha', 'material': 'Parquet de madera sobre contrapiso', 'frecuencia': 250, 'area_aplicada': 2.737, 'coeficiente': 0.03, 'absorcion': 0.08211}, {
    'zona': 'Derecha', 'material': 'Parquet de madera sobre contrapiso', 'frecuencia': 500, 'area_aplicada': 2.737, 'coeficiente': 0.04, 'absorcion': 0.10948000000000001}, {
    'zona': 'Derecha', 'material': 'Parquet de madera sobre contrapiso', 'frecuencia': 1000, 'area_aplicada': 2.737, 'coeficiente': 0.05, 'absorcion': 0.13685}, {
    'zona': 'Derecha', 'material': 'Parquet de madera sobre contrapiso', 'frecuencia': 2000, 'area_aplicada': 2.737, 'coeficiente': 0.05, 'absorcion': 0.13685}, {
    'zona': 'Derecha', 'material': 'Parquet de madera sobre contrapiso', 'frecuencia': 4000, 'area_aplicada': 2.737, 'coeficiente': 0.05, 'absorcion': 0.13685}, {
    'zona': 'Piso', 'material': 'Hormigón rasado o monolítico', 'frecuencia': 125, 'area_aplicada': 58.3478, 'coeficiente': 0.02, 'absorcion': 1.166956}, {
    'zona': 'Piso', 'material': 'Hormigón rasado o monolítico', 'frecuencia': 250, 'area_aplicada': 58.3478, 'coeficiente': 0.02, 'absorcion': 1.166956}, {
    'zona': 'Piso', 'material': 'Hormigón rasado o monolítico', 'frecuencia': 500, 'area_aplicada': 58.3478, 'coeficiente': 0.02, 'absorcion': 1.166956}, {
    'zona': 'Piso', 'material': 'Hormigón rasado o monolítico', 'frecuencia': 1000, 'area_aplicada': 58.3478, 'coeficiente': 0.03, 'absorcion': 1.7504339999999998}, {
    'zona': 'Piso', 'material': 'Hormigón rasado o monolítico', 'frecuencia': 2000, 'area_aplicada': 58.3478, 'coeficiente': 0.04, 'absorcion': 2.333912}, {
    'zona': 'Piso', 'material': 'Hormigón rasado o monolítico', 'frecuencia': 4000, 'area_aplicada': 58.3478, 'coeficiente': 0.04, 'absorcion': 2.333912}]
reporte_inteligibilidad= {
    'Constante del Recinto (R)': 73.5,
    'Distancia Crítica (Dc)': 0.82,
    '%ALCONS': 204.48, 'Evaluación':
        '🔴 Crítico: Acústica extremadamente deficiente. Requiere atención urgente.',
    'Detalles': {
        'Distancia al oyente': 1.5,
        'Tiempo de Reverberación': 13.95,
        'Volumen de la sala': 214.136426,
        'Factor de Directividad': 2,
        'Superficie Total': 232.74099999999999,
        'Coeficiente Medio de Absorción': 0.24}}
absorsion= {
    125: 1.2216960000000001,
    250: 1.249066,
    500: 1.2764360000000001,
    1000: 1.8872839999999997,
    2000: 2.470762, 4000: 2.470762}
salon2=  {
    'Tipo': 'Salón tipo 1',
    'aulas': '101-104',
    'dimensiones': {'largo': 9.94, 'ancho': 5.87, 'altura': 3.67},
    'materiales': {'Frontal': {'material': 'Revoque rugoso',
                               'objetos_adheridos': [{
                                   'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                                   'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}],
                               'area': 13.5984},
                   'Trasera': {'material': 'Revoque rugoso',
                                'objetos_adheridos': [{
                                    'nombre': 'Ventana', 'material': 'Vidrio', 'area': 10.29}],
                               'area': 11.2529},
                   'Izquierda': {'material': 'Revoque rugoso', 'area': 36.4798},
                   'Derecha': {'material': 'Revoque rugoso',
                               'objetos_adheridos': [{
                                   'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}],
                               'area': 33.742799999999995},
                   'Piso': {'material': 'Hormigón rasado o monolítico', 'area': 58.3478},
                   'Techo': {'material': 'Hormigón rústico', 'area': 58.3478}},
    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 42.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.24}}





salon = {
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

salon101 = {
    'aulas': '201H - 204H',
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


salonEjemplo =  {
    'aulas': '101H - 104H',
    'dimensiones': {'largo': 12.0, 'ancho': 14.0, 'altura': 3.0},
    'materiales': {
        'Frontal': {'material': 'Ventana de doble vidrio',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Cortina veneciana de metal', 'area': 12.0}, {
                        'nombre': 'Ventana', 'material': 'Cortina veneciana de metal', 'area': 12.0}]},
        'Trasera': {'material': 'Ventana de vidrio',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Butaca de madera', 'area': 12.0}]},
        'Izquierda': {'material': 'Ventana de vidrio'},
        'Derecha': {'material': 'Ventana de vidrio común',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Ventana de vidrio', 'area': 3.0}]},
        'Piso': {'material': 'Área de audiencia ocupada'},
        'Techo': {'material': 'Público en asientos de tapizados en cuero',
                  'objetos_adheridos': [{
                      'nombre': 'paneles', 'material': 'Cortina veneciana de metal', 'area': 3.0}]}},
    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 40.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 2.0}],
    'inteligibilidad': {'distancia': 12.0, 'coeficiente_medio': 10.0}
}

salonTipo1 = {
    'Tipo': 'Salón tipo 1',
    'aulas': '101-104',
    'dimensiones': {'largo': 9.94, 'ancho': 5.87, 'altura': 3.67},
    'materiales': {
        'Frontal': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 10.29}]},
        'Izquierda': {'material': 'Revoque rugoso'},
        'Derecha': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón rústico'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 42.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.24}
}

salonTipo2 = {
    'Tipo': 'Salón tipo 2',
    'aulas': '105-106',
    # aulas 105-106
    'dimensiones': {'largo': 9.57, 'ancho': 5.88, 'altura': 2.52},
    'materiales': {
        'Frontal': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 13.0524}]},
        'Izquierda': {'material': 'Revoque rugoso'},
        'Derecha': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón rústico'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 30.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.24}
}

salonTipo3 = {
    'Tipo': 'Salón tipo 3',
    'aulas': '201-206',
    # aulas 201-206
    'dimensiones': {'largo': 9.97, 'ancho': 5.85, 'altura': 3.52},
    'materiales': {
        'Frontal': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 2.7216}]},
        'Trasera': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 10.18}]},
        'Izquierda': {'material': 'Revoque rugoso'},
        'Derecha': {'material': 'Revoque rugoso',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón rústico'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 45.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.24}
}

salonTipo4 = {
    'Tipo': 'Salón tipo 4',
    'aulas': '209-210',
    # aulas 209-210 "tiene A/A"
    'dimensiones': {'largo': 13.11, 'ancho': 5.68, 'altura': 2.7},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 8.89}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 45.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo5 = {
    'Tipo': 'Salón tipo 5',
    'aulas': '211-214',
    # aulas 211-214
    'dimensiones': {'largo': 6.99, 'ancho': 4.81, 'altura': 2.69},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 4.62}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 30.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo6 = {
    'Tipo': 'Salón tipo 6',
    'aulas': '215-216 y 315-316',
    # aulas 215-216 315-316
    'dimensiones': {'largo': 7.25, 'ancho': 4.77, 'altura': 2.67},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 7.73}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo7 = {
    'Tipo': 'Salón tipo 7',
    'aulas': '217-218 y 317-319',
    # aulas 217-218 317-319
    'dimensiones': {'largo': 7.89, 'ancho': 5.68, 'altura': 2.68},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 9.03}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo8 = {
    'Tipo': 'Salón tipo 8',
    'aulas': '219 y 314',
    # aulas 219 y 314
    'dimensiones': {'largo': 7.89, 'ancho': 5.68, 'altura': 3.65},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 8.86}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón Normal'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.22}
}

salonTipo9 = {
    'Tipo': 'Salón tipo 9',
    'aulas': '301-306',
    # aulas 301-306
    'dimensiones': {'largo': 9.97, 'ancho': 5.85, 'altura': 3.52},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 3.0226}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 9.45}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón Normal'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.22}
}

salonTipo10 = {
    'Tipo': 'Salón tipo 10',
    'aulas': '309',
    # aulas 309
    'dimensiones': {'largo': 13.12, 'ancho': 5.88, 'altura': 2.84},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 8.90}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo11 = {
    'Tipo': 'Salón tipo 11',
    'aulas': '310',
    # aulas 310
    'dimensiones': {'largo': 11.59, 'ancho': 5.62, 'altura': 2.63},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 8.65}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 36.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo12 = {
    'Tipo': 'Salón tipo 12',
    'aulas': '311-313',
    # aulas 311-313
    'dimensiones': {'largo': 6.97, 'ancho': 4.86, 'altura': 2.63},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 4.70}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 36.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo13 = {
    'Tipo': 'Salón tipo 13',
    'aulas': '401 y 404',
    # aulas 401 y 404
    'dimensiones': {'largo': 6.91, 'ancho': 5.06, 'altura': 3.64},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 5.21}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 37.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo14 = {
    'Tipo': 'Salón tipo 14',
    'aulas': '402 y 403',
    # aulas 402 y 403
    'dimensiones': {'largo': 8.85, 'ancho': 4.74, 'altura': 3.68},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 1.668}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 14.80}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón Normal'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 37.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.22}
}

salonTipo15 = {
    'Tipo': 'Salón tipo 15',
    'aulas': '405 y 408',
    # aulas 405 y 408
    'dimensiones': {'largo': 7.25, 'ancho': 5.02, 'altura': 3.52},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},  # NO APLICA,
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 8.90}]},  # NO APLICA,
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón Normal'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 20.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.2}
}

salonTipo16 = {
    'Tipo': 'Salón tipo 16',
    'aulas': '406-407',
    # aulas 406-407
    'dimensiones': {'largo': 8.79, 'ancho': 4.71, 'altura': 3.65},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 14.80}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Hormigón Normal'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 20.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.22}
}

salonTipo17 = {
    'Tipo': 'Salón tipo 17',
    'aulas': '411',
    # aulas 411
    'dimensiones': {'largo': 13.11, 'ancho': 5.16, 'altura': 2.67},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 7.95}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Escritorios de madera y metal', 'cantidad': 20.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo18 = {
    'Tipo': 'Salón tipo 18',
    'aula': '501',
    # aulas 501
    'dimensiones': {'largo': 7.01, 'ancho': 5.03, 'altura': 2.84},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 5.41}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 20.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo19 = {
    'Tipo': 'Salón tipo 19',
    'aulas': '502-504',
    # aulas 502-504
    'dimensiones': {'largo': 8.82, 'ancho': 4.68, 'altura': 2.84},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 7.25}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo20 = {
    'Tipo': 'Salón tipo 20',
    'aulas': '505-507',
    # aulas 505-507
    'dimensiones': {'largo': 5.48, 'ancho': 9.96, 'altura': 2.8},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 15.44}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 30.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo21 = {
    'Tipo': 'Salón tipo 21',
    'aulas': '513-514',
    # aulas 513-514
    'dimensiones': {'largo': 8.06, 'ancho': 5.86, 'altura': 2.67},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 9.08}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 25.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}


salonTipo22 = {
    'Tipo': 'Salón tipo 22',
    'aulas': '515',
    # aulas 515
    'dimensiones': {'largo': 8.06, 'ancho': 5.88, 'altura': 2.68},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 12.15}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 24.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salonTipo23 = {
    'Tipo': 'Salón tipo 23',
    'aulas': '517-520',
    # aulas 517-520
    'dimensiones': {'largo': 4.89, 'ancho': 7.03, 'altura': 2.66},
    'materiales': {
        'Frontal': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Puerta', 'material': 'Vidrio', 'area': 1.697}, {
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 6.2475}]},
        'Trasera': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Ventana', 'material': 'Vidrio', 'area': 10.90}]},
        'Izquierda': {'material': 'Revoque de cal y arena'},
        'Derecha': {'material': 'Revoque de cal y arena',
                    'objetos_adheridos': [{
                        'nombre': 'Tablero', 'material': 'Parquet de madera sobre contrapiso', 'area': 2.737}]},
        'Piso': {'material': 'Hormigón rasado o monolítico'},
        'Techo': {'material': 'Cielorraso de placas de yeso 13 mm + espacio aire'}},

    'objetos_adicionales': [{
        'nombre': 'Silla', 'material': 'Butaca bien tapizada', 'cantidad': 15.0}, {
        'nombre': 'Mesa', 'material': 'Madera compensada sin cámara', 'cantidad': 1.0}],
    'inteligibilidad': {'distancia': 1.5, 'coeficiente_medio': 0.25}
}

salones = obtener_salones(salonTipo1, salonTipo2, salonTipo4, salonTipo5, salonTipo6, salonTipo7,
                    salonTipo8, salonTipo9, salonTipo10, salonTipo11, salonTipo12, salonTipo13,
                    salonTipo14, salonTipo15, salonTipo16, salonTipo17, salonTipo18, salonTipo20,
                    salonTipo21, salonTipo22, salonTipo23)