# Changelog

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
