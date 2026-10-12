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

**Estado:** Implementada (2026-10-11) en `Vista/ventanaBarraTitulo.py`
(commits `e1adca8`, `13efea8`): mover, redimensionar y maximizar/restaurar
vía `startSystemMove()`/`startSystemResize()`, estado de maximizado leído
con `isMaximized()` (ya no un flag propio), y cursor de redimensión al
pasar por el borde.

## D-017 — Feedback al guardar el reporte PDF

`ReportePDF.reporte_tiempo_reverberacion` no informa éxito ni error (el de
inteligibilidad sí). Propuesta en `CHANGELOG.md` (2026-09-18); requiere
aprobar el cambio de firma de esa función.

**Estado:** Implementada (2026-10-11) en `Datos/utils/reportePDF.py`. El
cuerpo de `reporte_tiempo_reverberacion` (usada por M1 y M3 vía
`VentanaGraficaRT`) quedó envuelto en `try/except`, con el mismo
`QMessageBox` de éxito/error que ya tenía `reporte_inteligibiliad` (M2). No
hizo falta cambiar la firma del método. Detalle en `docs/CHANGELOG.md`.

## D-018 — Sistema visual único para los reportes PDF

Todos los reportes usan un mismo encabezado (`_header`, logo blanco `logoBN.png`,
título, subtítulo y fecha en líneas separadas), pie, jerarquía de títulos, ancho
útil de 468 pt, tablas sin truncar por caracteres y bloque `_bloque_alcons`
compartido. Se retira la marca de agua del flujo (la función se conserva sin
uso). La escala de %ALCONS del PDF tiene 6 niveles idénticos a
`AlconsCalculator.evaluar_alcons`. Solo presentación: sin cambios en fórmulas,
resultados, estructuras de datos ni firmas. Detalle en `docs/REPORTS.md`.

**Estado:** Implementada; pendiente de revisión visual del equipo.

*Nota (2026-10-11):* los 6 niveles de %ALCons que menciona este párrafo
seguían siendo, en el momento de esta decisión (UX-07), los umbrales
heredados (1,4/5/11,4/24,4/47). Esta decisión queda como el antecedente
histórico del sistema visual del PDF; los umbrales numéricos de la escala
los fija ahora D-019, que la sustituye en ese punto específico sin alterar
nada más de lo descrito aquí.

## D-019 — Criterio operativo de clasificación del %ALCons (6 categorías)

El equipo aprobó como **criterio operativo del proyecto** una clasificación
cualitativa de %ALCons de 6 categorías, documentada en detalle en
`docs/ALCONS_CLASSIFICATION_REVIEW.md`:

```
0 % ≤ x ≤ 1,4 %      → Excelente
1,4 % < x ≤ 4,8 %    → Buena
4,8 % < x ≤ 11,4 %   → Regular
11,4 % < x ≤ 24,2 %  → Pobre
24,2 % < x ≤ 46,5 %  → Mala
x > 46,5 %           → Crítico
```

Es una **decisión metodológica del proyecto**, no una transcripción literal
de la fuente bibliográfica consultada (Duran Uron et al., 2025, citando a su
vez a Carrión Carranza y Carrión, 2001), que publica 5 categorías con
intervalos no contiguos entre sí y sin categoría para valores superiores a
46,5 %. Los 5 límites superiores de cada categoría (1,4 / 4,8 / 11,4 / 24,2 /
46,5) sí coinciden con los que publica esa fuente; el equipo decidió (a)
asignar los valores intermedios que la fuente deja sin especificar a la
categoría inmediatamente siguiente, y (b) añadir "Crítico" como **extensión
operativa propia del proyecto** para x > 46,5 %, sin atribuirla a la fuente.

Esta clasificación **reemplazó** (2026-10-11) los umbrales anteriormente
activos en `Modelo/alcons2.py::evaluar_alcons` y
`Datos/utils/reportePDF.py::NIVELES_ALCONS` (1,4 / 5 / 11,4 / 24,4 / 47),
cuyo origen no estaba documentado en el repositorio (ver
`docs/ALCONS_CLASSIFICATION_REVIEW.md` §11).

**Implementación.** `Modelo/alcons2.py::evaluar_alcons` y
`Datos/utils/reportePDF.py::NIVELES_ALCONS` usan ya los 6 niveles de esta
decisión (mismos nombres, mismos umbrales, misma inclusión del límite
superior). El panel estático "Escala %ALCons" del formulario de
Inteligibilidad (`frame_escala`) se corrigió por código en
`Vista/ventInteligibilidad.py` (sin tocar el `.ui`, mismo criterio que D-011)
para mostrar las mismas 6 categorías, incluyendo un bloque nuevo para
"Crítico" que antes no existía ahí. Solo cambió la clasificación: las
fórmulas de Peutz, el cálculo numérico del %ALCons, la distancia crítica,
RT60 (Sabine/Eyring) y el diseño visual del PDF no se modificaron (verificado
contra los 23 salones del Bloque H).

**Esta decisión es el criterio operativo vigente del software.** No implica
que la redacción académica definitiva de la tesis esté cerrada — la
documentación académica formal se revisará en un bloque posterior,
independiente de este.

**Estado:** Aprobada e **implementada** (código, PDF, interfaz del
formulario de Inteligibilidad). Pendiente: revisión y cierre de la
documentación académica definitiva de la tesis (fuera de este bloque).
