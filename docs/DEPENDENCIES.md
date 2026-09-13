# Dependencies

## Dependencias confirmadas (auditoría completa de imports, 2026-09-12)

El código importa directamente:

- PySide6
- pandas
- matplotlib
- reportlab

`pandas.read_excel` requiere `openpyxl` como motor para leer los `.xlsx`
del proyecto (`Datos/coeficientes.xlsx`, `Datos/coefs_absorcion.xlsx`).
No se importa explícitamente pero es una dependencia de ejecución real
de `Modelo/excel.py`.

No se encontró ninguna otra dependencia de terceros en el código de la
aplicación (fuera de `prueba.py`, ver Legacy).

## Entorno probado (Linux/SteamOS)

Instalación limpia verificada en `.venv` con Python 3.13.15:

- PySide6 6.11.2
- pandas 3.0.5
- openpyxl 3.1.5
- matplotlib 3.11.2
- reportlab 5.0.1

Ver `requirements.txt` en la raíz del repositorio para instalación
reproducible (`pip install -r requirements.txt`).

Compatibilidad con Windows: POR VALIDAR (no se ha repetido esta
instalación limpia en una máquina Windows en esta sesión).

## Legacy

`prueba.py` importa PyQt5 y `Recursos.MainWindow` (inexistente en el
repositorio). No forma parte de la aplicación principal (que usa
PySide6). No se agregó PyQt5 a `requirements.txt`.

## Objetivo

Llegar a una instalación reproducible para: - Windows; - entorno de
desarrollo del equipo; - Linux/SteamOS.

La compatibilidad con Windows debe seguir verificándose; la
compatibilidad con Linux/SteamOS quedó verificada en esta sesión.
