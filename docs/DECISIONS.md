# Decisions

## D-001 — Un solo repositorio

Se mantiene el repositorio actual como fuente de verdad del software.

**Estado:** Aprobada.

## D-002 — GitHub como fuente de coordinación

El equipo usará GitHub para sincronizar código y documentación técnica.

**Estado:** Aprobada.

## D-003 — Word como documento académico principal

El Word más reciente es la fuente académica vigente.

**Estado:** Aprobada.

## D-004 — Preservar nombres de identificadores

Los nombres existentes se conservarán por defecto para mantener
trazabilidad entre archivos.

Un renombramiento solo se realizará si aporta una mejora clara y se
actualizan todas las referencias.

**Estado:** Aprobada.

## D-005 — Excel + diccionarios

Se mantiene inicialmente la solución híbrida: - Excel para
coeficientes; - diccionarios Python para aulas.

Una migración requiere análisis previo.

**Estado:** Aprobada.

## D-006 — PySide6

La aplicación actual utiliza PySide6/Qt6.

No se regresará a PyQt5.

**Estado:** Aprobada.

## D-007 — Peutz/%ALCons

El modelo actual de inteligibilidad se conserva mientras no exista una
decisión académica para cambiarlo.

**Estado:** Aprobada.

## D-008 — Refactorización progresiva

No se hará un “big bang refactor”. Primero se caracterizará el
comportamiento mediante pruebas y luego se refactorizará por módulos.

**Estado:** Aprobada.

## D-009 — Rama principal

El equipo históricamente trabaja con `master` y ha configurado `main` en
GitHub. El estado efectivo del default branch debe verificarse antes de
establecer políticas automáticas.

**Estado:** Pendiente de verificación.

## D-010 — Claude Code como agente de implementación

Para editar archivos localmente y ver los cambios inmediatamente en el
proyecto, se recomienda Claude Code local/desktop conectado al
repositorio local. El uso web de Claude Code es complementario y trabaja
con ramas/sesiones en la nube.

**Estado:** Aprobada como estrategia de trabajo.

## D-011 — Ajustes de interfaz por código, no regenerando los `.ui`

Los ajustes visuales de 2026-09-13/18 se aplican en los controladores de
`Vista/` (`setStyleSheet`, tamaños, `sizePolicy`, alineación) y no editando
`.ui` ni regenerando los `.py`: `pyside6-uic` 6.11.2 (este entorno) frente a
6.5.2 (con el que se generaron) añade ruido de versión, y los `.py` ya
difieren de sus `.ui` en líneas previas. Excepción: la eliminación de una
declaración `box-shadow` inválida en `vistaGraficaRT.ui`/`.py` (una línea
por archivo, a mano y en sincronía).

**Estado:** Aprobada. `POR VALIDAR` si se prefiere absorber el ruido y
regenerar en una máquina con Qt Designer funcional.

## D-012 — Estilos, colores y tamaños de texto centralizados

`Recursos/estilos/estilo.py` (componentes QSS), `paleta.py` y `tipografia.py`
son la fuente única. Antes de crear un estilo, color o tamaño se busca ahí.

**Estado:** Aprobada.

## D-013 — Regla de iconos

Un icono se reutiliza solo si realmente representa la acción o entidad. Si no
existe uno adecuado no se pone otro para llenar el espacio: se documenta en
`docs/RESOURCES.md` y el equipo proporciona el recurso. Preferencia por
iconografía mínima, coherente y funcional.

**Estado:** Aprobada.

## D-014 — Sin emojis en la interfaz

No se usan emojis como parte de la identidad visual; se usan iconos de
`Recursos/iconos/` o solo texto. Los prefijos `⚠` de texto del formulario RT
se mantienen por ahora (el formulario es la referencia).

**Estado:** Aprobada.

## D-015 — Estructura de la pantalla de resultados de RT

Un único bloque "Tiempo de Reverberación" (veredicto, Tr MID, tabla,
conclusión) y un bloque independiente de "Inteligibilidad del Habla". El
gráfico se centra verticalmente respecto al contenido. Matiz conocido: si el
panel es más alto que la ventana (p. ej. 1366×768) el gráfico queda
desplazado hacia abajo en la primera pantalla; alternativa documentada en
`CHANGELOG.md`.

**Estado:** Aprobada (el matiz queda a criterio del equipo).

## D-016 — Mover y redimensionar la ventana: bloque separado

`VentanaConBarra` (frameless) mueve con `move()`, que no funciona en Wayland,
y no tiene redimensionado. Se implementará como bloque propio con
`startSystemMove()`/`startSystemResize()`; diagnóstico en `CHANGELOG.md`
(2026-09-18). Incluye corregir el estado inicial de `maximizado`.

**Estado:** Pendiente de implementación.

## D-017 — Feedback al guardar el reporte PDF

`ReportePDF.reporte_tiempo_reverberacion` no informa éxito ni error (el de
inteligibilidad sí). Propuesta en `CHANGELOG.md` (2026-09-18); requiere
aprobar el cambio de firma de esa función.

**Estado:** Propuesta pendiente de aprobación.

