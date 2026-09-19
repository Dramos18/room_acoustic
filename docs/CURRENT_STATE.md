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
4.  ~~`Modelo/calculoRT2.py` contiene una construcción `ValueError(...)`
    sin `raise` en la validación del área de objetos adheridos; requiere
    revisión.~~ **Corregido 2026-09-13** (ver `docs/CHANGELOG.md`).
5.  Existen varios `print()` de diagnóstico en lógica de aplicación;
    deben limpiarse gradualmente sin ocultar errores.
6.  Debe verificarse la gestión de rutas de recursos para ejecución
    desde distintos directorios.
7.  Debe incorporarse una estrategia de pruebas antes de refactorizar
    cálculos centrales.

Estas observaciones son hallazgos de auditoría, no instrucciones para
modificar inmediatamente el código.

## Actualización 2026-09-12 — Entorno reproducible

- Ya existe `requirements.txt` en la raíz (PySide6, pandas, openpyxl,
  matplotlib, reportlab, versiones fijadas y probadas en Linux).
- Se corrigió `Modelo/excel.py` (separadores de ruta `\\` → `os.path.join`
  con segmentos) para que la carga de Excel funcione en Linux; ver
  `docs/CHANGELOG.md`.
- Sigue sin existir carpeta `tests/`. Sigue sin existir `pyproject.toml`
  (no se ha decidido adoptarlo).
- El punto 3 de esta sección (`prueba.py` legacy) sigue vigente y sin
  cambios.

## Actualización 2026-09-18 — Interfaz (UI/UX)

- Módulo 1 (Tiempo de Reverberación) cerrado visualmente: formulario
  (referencia de calidad) → resultados → guardar PDF. Estructura de la
  pantalla de resultados y patrón compartido: `docs/UI_INVENTORY.md`.
- Estilos reutilizables en `Recursos/estilos/` (`estilo.py`, `paleta.py`,
  `tipografia.py`); recursos gráficos inventariados en `docs/RESOURCES.md`.
- Corregidos: `plt.show()` que abría una ventana extra y bloqueaba el flujo;
  aviso `Unknown property box-shadow` (origen en `vistaGraficaRT.ui/.py`);
  regresión de stretch que dejaba bandas vacías en resultados y Base de
  Datos; ruta del GIF de transición de Base de Datos.
- Sin emojis en la pantalla de resultados. El prefijo `⚠` de los mensajes de
  validación del formulario RT se mantiene.
- Módulos 2 (Inteligibilidad) y 3 (Base de Datos): pendientes de alinearse
  al patrón del Módulo 1 (botones "Ir al Inicio" aún con chevron, encabezados,
  barras, iconos de módulo).
- Pendientes: mover/redimensionar/maximizar la ventana (D-016), feedback al
  guardar el PDF (D-017), iconos nuevos opcionales (`RESOURCES.md`), P3 de
  `CHANGELOG.md`.
- Resultados numéricos: sin cambios (23 salones idénticos al commit anterior
  a los ajustes de resultados).
- Sigue sin existir carpeta `tests/`; la verificación de UI es un
  procedimiento manual reproducible (`docs/TESTING.md`).

