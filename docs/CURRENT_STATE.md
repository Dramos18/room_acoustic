# Current State

## Confirmado por el equipo

- Repositorio actual: `Room Acoustic`.
- La rama principal histórica indicada es `master`.
- El equipo configuró GitHub para trabajar también con `main`; el estado
  efectivo debe verificarse con GitHub/Git.
- Bloque H: 23 tipos de salón.
- Fuente de datos de salones: diccionarios Python.
- Coeficientes acústicos: Excel.
- %ALCons: modelo de Peutz.
- La implementación de %ALCons se considera actualmente equivalente al
  modelo descrito en el Word vigente.
- El Word más reciente es la base académica de continuidad.

## Auditoría del snapshot entregado

El snapshot del repositorio contiene:

- `Controlador/`
- `Datos/`
- `Modelo/`
- `Recursos/`
- `Vista/`
- `prueba.py`
- `.gitignore`
- configuración `.idea/` ignorada por Git.

No contiene todavía: - `README.md`; - `requirements.txt`; -
`pyproject.toml`; - carpeta `tests/`; - documentación técnica `docs/`.

## Implementaciones activas observables

### Inteligibilidad

`Vista/ventInteligibilidad.py` importa
`Modelo.alcons2.AlconsCalculator`.

Por tanto, `Modelo/alcons2.py` es actualmente la implementación
principal de %ALCons utilizada por esa ventana.

`Modelo/%alcons.py` contiene otra implementación del mismo dominio y
debe considerarse duplicada/legacy hasta completar su auditoría.

### Tiempo de reverberación

`Vista/ventTiempoReverberacion.py` y `Controlador/controlTR.py` utilizan
`Modelo/calculoRT2.py`.

`Modelo/calculoRT.py` contiene una implementación alternativa/legacy que
debe auditarse antes de eliminarla.

## Observaciones técnicas pendientes

1.  No existen pruebas automatizadas en el snapshot.
2.  Hay módulos duplicados o alternativos (`alcons2.py` / `%alcons.py`,
    `calculoRT2.py` / `calculoRT.py`).
3.  `prueba.py` usa PyQt5 y referencia `Recursos.MainWindow`, mientras
    la aplicación principal utiliza PySide6; debe tratarse como archivo
    legacy/de prueba hasta validarlo.
4.  `Modelo/calculoRT2.py` contiene una construcción `ValueError(...)`
    sin `raise` en la validación del área de objetos adheridos; requiere
    revisión.
5.  Existen varios `print()` de diagnóstico en lógica de aplicación;
    deben limpiarse gradualmente sin ocultar errores.
6.  Debe verificarse la gestión de rutas de recursos para ejecución
    desde distintos directorios.
7.  Debe incorporarse una estrategia de pruebas antes de refactorizar
    cálculos centrales.

Estas observaciones son hallazgos de auditoría, no instrucciones para
modificar inmediatamente el código.
