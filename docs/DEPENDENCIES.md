# Dependencies

## Dependencias observadas

El código importa directamente:

- PySide6
- pandas
- matplotlib
- reportlab

Pandas requiere un motor apropiado para leer los Excel del proyecto;
`openpyxl` debe verificarse según el entorno instalado.

## Legacy

`prueba.py` importa PyQt5.

No asumir que PyQt5 forma parte de la aplicación final. Primero
determinar si `prueba.py` se conserva.

## No crear requirements a ciegas

La lista definitiva debe generarse después de: 1. revisar todos los
imports; 2. identificar código realmente ejecutado; 3. identificar el
motor Excel; 4. probar instalación limpia; 5. registrar versiones
compatibles.

## Objetivo

Llegar a una instalación reproducible para: - Windows; - entorno de
desarrollo del equipo; - futuro entorno Linux/SteamOS si se decide
migrar.

La compatibilidad multiplataforma debe verificarse, no asumirse.
