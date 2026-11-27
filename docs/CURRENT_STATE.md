# Current State

## Actualización vigente — 2026-11-27

**Base de revisión:** rama `docs/knowledge-base-2026-11`. Esta sección prevalece sobre las descripciones antiguas que aparecen más abajo; esas secciones se conservan como historial y no deben leerse como fotografía actual.

### Estado funcional documentado

- M1 (Tiempo de Reverberación), M2 (Inteligibilidad), M3 (Base de Datos) y Ayuda V1 están implementados en el repositorio y cuentan con documentación de sus flujos.
- M3 reutiliza el motor de cálculo de reverberación de M1; no es un motor acústico independiente.
- D-016 (mover/redimensionar ventana), D-017 (feedback al guardar PDF) y D-019 (clasificación operativa %ALCons) figuran como implementados en CHANGELOG/DECISIONS.
- El catálogo de datos contiene 23 perfiles en Datos/salones.py. Su procedencia geométrica, física y bibliográfica aún requiere trazabilidad; ver ACOUSTIC_DATA_CATALOG.md.
- La especificación de módulos, el catálogo de datos, la matriz de verificación/validación y la alineación académica están documentados en MODULES_SPECIFICATION.md, ACOUSTIC_DATA_CATALOG.md, SOFTWARE_VALIDATION.md y ACADEMIC_ALIGNMENT.md. La auditoría estática fue reconciliada en CODEBASE_AUDIT.md.

### Calidad y validación

- TESTING.md describe procedimientos manuales y de regresión; no equivale a una suite automatizada.
- No se ha establecido en esta revisión una ejecución reciente de toda la matriz de pruebas. SOFTWARE_VALIDATION.md separa evidencia histórica, pruebas pendientes, validación matemática y validación experimental.
- Linux/SteamOS tiene un entorno de instalación documentado en DEPENDENCIES.md. Compatibilidad Windows continúa POR VALIDAR.
- La validación experimental contra mediciones independientes no está demostrada por los registros inspeccionados.
- El equipo confirmó 3,16 × Dc como umbral de transición del modelo de Peutz para la versión del software (D-020). El Word debe actualizarse para no describir 3,5 × Dc. La Dc activa es 0,21 · sqrt(V / TR_2000Hz); la expresión 0,14 · sqrt(Q · R) está definida, pero no se utiliza en el flujo activo. La verificación bibliográfica primaria de Dc/R y la validación experimental siguen pendientes.

### Hallazgos de datos pendientes

- salonTipo18 usa la clave aula en singular, mientras los demás perfiles utilizan aulas. Revisar consumidores antes de corregir.
- Existen tres libros Excel relacionados con coeficientes; el flujo principal inspeccionado carga coefs_absorcion.xlsx. La procedencia bibliográfica de los coeficientes y la función de los otros libros deben documentarse.
- No se ejecutó la aplicación ni se corrieron pruebas durante la actualización documental del 2026-11-27.

### Prioridades técnicas y académicas

1. Fijar un commit de evaluación y una línea base reproducible.
2. Resolver con respaldo bibliográfico y académico las discrepancias de Peutz.
3. Recuperar fuentes primarias de geometría, materiales, mobiliario y coeficientes.
4. Convertir los casos centrales del motor acústico en pruebas automatizadas.
5. Ejecutar pruebas de integración M1/M2/M3 y reportes, conservando evidencias.
6. Realizar validación experimental con mediciones independientes según el protocolo aprobado.
7. Actualizar el manuscrito de grado solo después de resolver las discrepancias y consolidar evidencias.

---

> El contenido histórico que sigue documenta auditorías y decisiones de fechas anteriores. No eliminarlo sin migrar primero la información que siga siendo pertinente y fechar explícitamente cualquier cambio de estado.

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

## Actualización 2026-09-19 — Reportes PDF (UX-07)

- Reportes RT (3/4 páginas) e Inteligibilidad (1 página) estandarizados:
  encabezado único con logo blanco, sin marca de agua, ortografía corregida,
  escala de %ALCONS de 6 niveles igual a la del modelo, tablas con ajuste de
  texto y paginación. Ver `docs/REPORTS.md`.
- Sin cambios en modelo, datos ni firmas. Feedback al guardar (D-017) sigue
  pendiente. Revisión visual de los PDF por el equipo: POR VALIDAR.

## Actualización 2026-10-11 — D-019 y Módulo 2 (Inteligibilidad)

- **D-019**: clasificación operativa de %ALCons de 6 categorías
  (1,4/4,8/11,4/24,2/46,5) implementada en `Modelo/alcons2.py`,
  `Datos/utils/reportePDF.py` y la interfaz. Ver `docs/DECISIONS.md` y
  `docs/ALCONS_CLASSIFICATION_REVIEW.md`.
- **Módulo 2 (Inteligibilidad)**: cerrado visualmente (bloque M2-UX, mismo
  nivel que el Módulo 1). Pantalla de resultados propia
  (`Vista/ventResultadosInteligibilidad.py`), ya no `QMessageBox`; flechas
  de SpinBox corregidas; validación inline; helpers de estilo centralizados.
  Ver `docs/CHANGELOG.md`.
- Módulo 3 (Base de Datos) sigue pendiente de alinear según
  `docs/HANDOFF.md`. D-016 (mover, redimensionar, maximizar/restaurar la
  ventana) y D-017 (feedback al guardar el PDF de RT) ya fueron
  implementados (2026-10-11); ver `docs/DECISIONS.md`.
- Resultados numéricos: sin cambios (23 salones idénticos; Sabine/Eyring y
  %ALCons numérico verificados contra el commit anterior a D-019).
