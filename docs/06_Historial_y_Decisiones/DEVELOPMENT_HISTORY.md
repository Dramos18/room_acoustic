# Historial de desarrollo — Room Acoustic

## Propósito

Este documento consolida los hitos funcionales y técnicos que pueden rastrearse en el repositorio y sus registros de cambios. No reemplaza el historial detallado de `CHANGELOG.md` ni pretende reconstruir actividades que no dejaron evidencia.

**Corte documental:** 2026-11-27  
**Último commit remoto consultado:** `89417063de9e3053a4cc05739bc7eeda3fc8900e` — actualización de HANDOFF y UI_INVENTORY para Ayuda V1 (2026-10-12).

## 1. Evolución funcional

### 1.1 Núcleo de evaluación acústica

El software se organiza alrededor de tres módulos funcionales:

1. **Tiempo de Reverberación (RT60):** ingreso o recuperación de dimensiones, materiales y elementos del recinto; cálculo por bandas mediante Sabine y Eyring; presentación de tablas y gráficos.
2. **Inteligibilidad del Habla:** estimación de %ALCons mediante el modelo de Peutz, utilizando parámetros del recinto y distancia emisor–receptor.
3. **Base de Datos del Bloque H:** consulta de 23 tipos de salón caracterizados, con sus dimensiones, materiales y elementos registrados, para lanzar su análisis acústico.

El flujo de resultados permite generar reportes PDF. La implementación utiliza una fuente de datos híbrida: diccionarios Python para aulas y libros Excel para coeficientes de absorción.

### 1.2 Consolidación de M1, M2 y M3

Los registros de `HANDOFF.md`, `UI_INVENTORY.md` y `CHANGELOG.md` describen el cierre visual de los módulos siguiendo M1 como patrón de referencia:

- **M1 — Tiempo de Reverberación:** formulario, validaciones, resultados gráficos y tabulares, semáforo acústico y generación de reporte.
- **M2 — Inteligibilidad:** formulario propio, validación inline, pantalla de resultados dedicada y presentación de la escala cualitativa D-019.
- **M3 — Base de Datos:** selección de aulas, resumen de características, validación inline, navegación de retorno y reutilización de la pantalla de resultados RT.

La expresión “cierre visual” se refiere a los bloques de trabajo registrados; no equivale a afirmar que toda la aplicación esté libre de deuda técnica o que la validación académica final esté terminada.

## 2. Hitos técnicos documentados

| Fecha registrada | Hito | Evidencia en el repositorio |
|---|---|---|
| 2026-09-12 | Entorno Linux/SteamOS y dependencias fijadas | `DEPENDENCIES.md`, `requirements.txt` |
| 2026-09-13/18 | Mejoras de interfaz, estructura visual y recursos | `CHANGELOG.md`, `UI_INVENTORY.md`, `RESOURCES.md` |
| 2026-09-19 | Estandarización visual de reportes PDF (UX-07) | `REPORTS.md`, `CHANGELOG.md`, D-018 |
| 2026-10-11 | Cierre visual de M2 — Inteligibilidad | `CHANGELOG.md`, `HANDOFF.md`, `UI_INVENTORY.md` |
| 2026-10-11 | Implementación de D-019 en clasificación %ALCons | `DECISIONS.md`, `ALCONS_CLASSIFICATION_REVIEW.md` |
| 2026-10-11 | Cierre visual de M3 — Base de Datos | `HANDOFF.md`, `UI_INVENTORY.md` |
| 2026-10-11 | D-016: mover, redimensionar y maximizar ventana en Wayland | `DECISIONS.md`, `CHANGELOG.md` |
| 2026-10-11 | D-017: feedback al guardar PDF de RT en M1/M3 | `DECISIONS.md`, `CHANGELOG.md` |
| 2026-10-11 | Ayuda V1 interactiva desde la pantalla de inicio | `HANDOFF.md`, `UI_INVENTORY.md`, commit `eeefc61` |
| 2026-10-12 | Documentación de Ayuda V1 en HANDOFF e inventario UI | commit `8941706` |

Las fechas anteriores corresponden a las fechas consignadas en los documentos y mensajes de commit visibles en GitHub. No sustituyen la auditoría de cada diff.

## 3. Decisiones con impacto funcional o metodológico

### D-016 — Gestión de ventana

Se implementó el movimiento y redimensionamiento de la ventana frameless mediante las operaciones de ventana del sistema compatibles con Wayland; el estado maximizado se consulta directamente. Archivos señalados en el registro: `Vista/ventanaBarraTitulo.py`.

### D-017 — Resultado de guardado del PDF

Se incorporó feedback de éxito/error al método `ReportePDF.reporte_tiempo_reverberacion`, utilizado en M1 y M3. El registro indica que no fue necesario cambiar la firma del método y que se probaron guardado exitoso, error de ruta y cancelación.

### D-018 — Sistema visual único para reportes

Se estandarizaron encabezado, pie, jerarquía visual, tablas, paginación y bloques compartidos de reportes. La decisión se limita a presentación y no declara cambios en los cálculos acústicos.

### D-019 — Clasificación operativa de %ALCons

Se adoptó e implementó una clasificación continua de seis categorías:

| Intervalo | Categoría |
|---|---|
| 0 ≤ x ≤ 1,4 | Excelente |
| 1,4 < x ≤ 4,8 | Buena |
| 4,8 < x ≤ 11,4 | Regular |
| 11,4 < x ≤ 24,2 | Pobre |
| 24,2 < x ≤ 46,5 | Mala |
| x > 46,5 | Crítico |

Los cinco límites superiores proceden de la tabla bibliográfica analizada. La asignación de los huecos y la categoría “Crítico” son decisiones operativas propias del proyecto. La revisión y las pruebas descritas están en `ALCONS_CLASSIFICATION_REVIEW.md`. No se debe presentar la escala completa como una transcripción literal de la fuente.

## 4. Evolución de la experiencia de usuario

El inventario de interfaz refleja una evolución desde formularios iniciales hacia un patrón más consistente:

- centralización de colores, tipografía y componentes QSS en `Recursos/estilos/`;
- consistencia de encabezados, botones de retorno, pies y tarjetas;
- validaciones inline en formularios;
- separación de pantallas de resultados;
- reutilización de componentes y de la pantalla RT cuando corresponde;
- ajuste de la ventana a restricciones de Wayland;
- ayuda interactiva con menú temático, stepper y flujos explicativos;
- documentación de recursos gráficos usados y no usados.

Los detalles de widgets, archivos `.ui`, clases y controladores deben consultarse en `UI_INVENTORY.md`, evitando duplicarlos aquí.

## 5. Estado que no debe confundirse

A partir de la evidencia consultada:

- M1, M2 y M3 cuentan con implementación funcional documentada.
- D-016, D-017, D-018 y D-019 aparecen como implementadas en el registro.
- Ayuda V1 aparece como implementada.
- La suite automatizada de regresión sigue siendo una necesidad; `TESTING.md` registra procedimientos reproducibles, pero indica que no existe una suite automatizada en el snapshot descrito.
- La compatibilidad Windows figura como POR VALIDAR en `DEPENDENCIES.md`.
- La distribución/instalador no está documentada como terminada.
- La validación académica frente a mediciones reales debe distinguirse de las pruebas de software y de las comparaciones contra versiones anteriores.
- La Ayuda V1 tiene refinamiento visual y ampliación de contenido señalados como pendientes no bloqueantes.
- Existen hallazgos puntuales y deuda técnica por revisar, sin convertirlos automáticamente en autorización para cambiar código.

## 6. Próxima actualización de este historial

Agregar un hito solo cuando exista evidencia rastreable: commit, registro en CHANGELOG, decisión aprobada, prueba documentada o entregable verificable. Para cada hito futuro, registrar fecha, objetivo, alcance, archivos/componentes afectados, pruebas ejecutadas y pendientes.
