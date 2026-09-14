# Changelog

## 2026-09-13 — Correcciones puntuales (mejoras #1-#3 del ranking de auditoría)

### Corregido

- `Datos/salones.py`: `obtener_salones()` no recibía `salonTipo3` ni
  `salonTipo19` (ya definidos en el archivo, con sus datos intactos).
  La lista `salones` pasaba de 21 a 23 elementos. Verificado:
  `len(salones) == 23` y tipos 1-23 sin huecos. No se modificaron los
  datos internos de ningún salón.
- `Modelo/calculoRT2.py` (`agregar_areas_materiales`): se agregó el
  `raise` faltante antes del `ValueError` que validaba que el área de
  objetos adheridos no supere el área de la superficie. Verificado:
  (a) un caso inválido ahora lanza `ValueError` correctamente; (b) el
  caso válido de referencia (`DiccionarioRecibido`) produce
  `sabine_rt`, `eyring_rt` y `reporte_inteligibilidad` idénticos byte
  a byte a los obtenidos con el código anterior al cambio (comparado
  contra el commit previo). Ninguna fórmula fue modificada.
- `Controlador/Controlador.py` (`obtener_coeficientes_materiales`): se
  agregó una verificación de `None` para `materiales_dos` (mismo
  patrón ya usado en `obtener_lista_materiales`), evitando un
  `AttributeError` no controlado si la carga del Excel de coeficientes
  falla. Verificado: el camino feliz (Excel cargado) produce
  exactamente los mismos resultados que antes; el camino de fallo
  simulado (`materiales_dos = None`) ahora degrada a `{}` en vez de
  lanzar una excepción sin manejar. No se cambiaron coeficientes ni la
  fuente de datos (Excel).

### Verificación

- Smoke test de imports de todos los módulos de `Vista`, `Controlador`,
  `Modelo`, `Datos`: sin errores.
- Arranque de `Vista/main.py`: sin excepciones, ventana creada
  correctamente.

## 2026-09-12 — Entorno reproducible en Linux/SteamOS

### Confirmado

- Punto de entrada real: `Vista/main.py`. Ejecución equivalente a la
  configuración de PyCharm (`WORKING_DIRECTORY=Vista`,
  `ADD_CONTENT_ROOTS=true`): `cd Vista && PYTHONPATH=.. python main.py`.
- Dependencias directas confirmadas por auditoría de imports: PySide6,
  pandas, openpyxl (motor de `pandas.read_excel` para `.xlsx`),
  matplotlib, reportlab.
- Entorno probado: Python 3.13.15, PySide6 6.11.2, pandas 3.0.5,
  openpyxl 3.1.5, matplotlib 3.11.2, reportlab 5.0.1.
- Se creó `requirements.txt` en la raíz con estas versiones fijadas.

### Corregido

- `Modelo/excel.py`: las rutas a `Datos/coeficientes.xlsx` y
  `Datos/coefs_absorcion.xlsx` usaban separadores `\\` (Windows)
  incrustados en la cadena, lo que impedía localizarlos en Linux. Se
  cambió a segmentos separados en `os.path.join` (sin alterar nombres
  de variables ni lógica). Verificado: ambos Excel cargan correctamente
  en Linux tras el cambio.

### Pendiente / observado (no modificado en esta tarea)

- `Vista/ventInfoBD.py:392` y `Vista/ventInfoBD2.py:155` referencian
  `"Recursos/estilos/iconos/ondas.gif"`, ruta inexistente (el archivo
  real es `Recursos/gifs/ondas.gif`). Bug preexistente independiente
  del sistema operativo; no bloquea el arranque de la aplicación.
  POR VALIDAR con el equipo antes de corregirlo.
- `prueba.py` sigue como archivo legacy (PyQt5, `Recursos.MainWindow`
  inexistente); no se tocó.

## 2026-09-12 — Baseline para Claude Code

### Confirmado

- Repositorio actual: Room Acoustic.
- Bloque H: 23 tipos de salón.
- Datos de salones: diccionarios Python.
- Coeficientes: Excel.
- Inteligibilidad: Peutz/%ALCons.
- Word vigente identificado como `proyectoGradoSoftware.docx`.

### Auditoría inicial del snapshot

- Aplicación principal basada en PySide6.
- `Modelo/alcons2.py` es usado por la ventana de inteligibilidad.
- `Modelo/calculoRT2.py` es usado por el controlador de RT.
- Existen implementaciones alternativas/legacy.
- No hay suite de pruebas automatizadas.
- No existe `requirements.txt` ni `pyproject.toml`.

### Pendiente

- Verificar default branch real de GitHub.
- Crear pruebas de caracterización.
- Resolver/registrar duplicación de modelos.
- Auditar rutas de recursos.
- Formalizar dependencias.
- Revisar y actualizar capturas de la tesis cuando cambie la UI.
