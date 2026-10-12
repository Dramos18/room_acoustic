# Handoff

## Estado actual

El proyecto está funcionalmente avanzado pero todavía en evolución.

La prioridad actual es preparar una base sólida para que Claude pueda
intervenir en el código de manera segura, trazable y verificable.

## Próxima sesión de Claude

Claude debe comenzar por:

1.  verificar `git status`;
2.  verificar rama y remoto;
3.  leer `CLAUDE.md`;
4.  leer `AI_RULES.md`;
5.  leer `docs/PROJECT_CONTEXT.md`;
6.  leer `docs/CURRENT_STATE.md`;
7.  leer `docs/ARCHITECTURE.md`;
8.  leer `docs/ACOUSTIC_MODEL.md`;
9.  hacer un mapa de dependencias;
10. identificar puntos de entrada;
11. identificar código duplicado;
12. proponer una estrategia de pruebas;
13. NO hacer una gran refactorización todavía.

## Primera meta técnica

Construir una línea base reproducible: - instalación; - ejecución; -
prueba de humo; - casos acústicos de referencia; - generación de PDF; -
navegación principal.

## Regla de continuidad

Antes de continuar trabajo iniciado por otra sesión, Claude debe revisar
el estado real del repositorio y no confiar únicamente en el resumen de
una conversación anterior.

## Próximos pasos (actualizado 2026-09-18)

**Reportes PDF (UX-07, 2026-09-19):** estandarizados en
`Datos/utils/reportePDF.py`; ver `docs/REPORTS.md` antes de tocarlos.
Pendiente de revisión visual del equipo (sin commit al cierre de esta
sesión).

Orden acordado: primero cerrar cada módulo, tomando el Módulo 1 como
referencia visual.

1. **Módulo 2 — Inteligibilidad**: ✅ cerrado visualmente (bloque M2-UX,
   2026-10-11). Formulario con barra superior/inferior y botón "Atrás"
   alineados al patrón de `docs/UI_INVENTORY.md`, flechas de los 5
   `QDoubleSpinBox` corregidas, validación inline (no bloqueante), y
   pantalla de resultados propia (`Vista/ventResultadosInteligibilidad.py`,
   ya no `QMessageBox`) con la escala de %ALCons de 6 niveles (D-019)
   visible junto al resultado. Detalle completo en `docs/CHANGELOG.md`.
   Pendiente, señalado pero no resuelto en este bloque: verificar en
   pantalla real la responsividad de las 3 columnas del formulario
   (`frame_GuiaValores`/`frame_form`/`frame_escala`) en ventanas angostas;
   dos iconos opcionales recomendados (`distanciaPeople.png`, `info.png`,
   ver `docs/RESOURCES.md`) sin implementar, exigirían tocar
   `frame_GuiaValores`.
2. **Módulo 3 — Base de Datos**: ✅ cerrado visualmente (auditoría +
   bloque M3-UX, 2026-10-11). Validación inline junto al ComboBox (ya no
   `QMessageBox.Critical`) y botón "Ir al Inicio" añadido al pie (no
   existía; construido en Python sin tocar `infoBD.ui`), ambos al mismo
   patrón de M1/M2. Resultados: sigue reutilizando `VentanaGraficaRT` (la
   de Módulo 1), decisión correcta, no una carencia. Detalle completo en
   `docs/UI_INVENTORY.md`.
   Pendiente real: icono temático propio (hoy `logoBN.png`); considerar
   `base-de-datos.png` (`RESOURCES.md`) cuando el equipo lo aporte. De
   menor prioridad, sin resolver a propósito (bajo riesgo de cambiar algo
   visualmente sin necesidad): migrar `frameTop`/`frameBottom` a los
   helpers de `estilo.py`.
3. **Ventana**: ✅ implementada (D-016, 2026-10-11). Mover y redimensionar vía
   `startSystemMove()`/`startSystemResize()` (en vez de `move()`, que no
   funciona en Wayland), maximizar/restaurar corregido (usa
   `isMaximized()` directamente), y cursor de redimensión al pasar por el
   borde antes de hacer clic. Todo en `Vista/ventanaBarraTitulo.py`
   (commits `e1adca8`, `13efea8`). Detalle completo en `docs/CHANGELOG.md`
   y `docs/DECISIONS.md`.
4. **Feedback al guardar el PDF**: ✅ implementada (D-017, 2026-10-11).
   `ReportePDF.reporte_tiempo_reverberacion` (M1 y M3) ya muestra el mismo
   `QMessageBox` de éxito/error que ya tenía `reporte_inteligibiliad` (M2).
   Detalle en `docs/CHANGELOG.md` y `docs/DECISIONS.md`.
5. **Iconos**: el equipo agrega los recursos que vea necesarios en
   `Recursos/iconos/` y los registra en `docs/RESOURCES.md` (sección 8).
6. Pendientes P3 del Módulo 1 en `docs/CHANGELOG.md` (eje logarítmico del
   gráfico, iconos de inicio/guardar, etc.).
7. **Ayuda**: ✅ implementada V1 (2026-10-11). `botonAyuda` del Inicio
   (antes sin conectar) ahora abre `Vista/ventAyuda.py` (`VentanaAyuda`),
   guía interactiva construida en Python puro, sin `.ui` nuevo: menú de
   6 secciones, stepper para "Cómo empezar", componente de flujo
   Entrada→Procesamiento→Resultado reutilizado en Tiempo de
   Reverberación/Inteligibilidad/Base de Datos/Resultados y PDF, escala
   de %ALCons tomada de `NIVELES_ALCONS` (D-019, sin duplicar umbrales).
   Responsive real (3→2→1 columnas, stepper/flujos de horizontal a
   vertical) verificado en 1920×1080, 1366×768, 800×600 y 500×800. No se
   tocó M1, M2, M3, el modelo, D-019, el PDF ni D-016. Detalle completo
   en `docs/UI_INVENTORY.md`.
   Pendiente real, señalado a propósito para una fase posterior:
   refinamiento visual (consistencia de fondo/superficie, transparencias
   y bordes entre componentes) y ampliación de contenido — no bloqueante.

Reglas vigentes para continuar: no tocar fórmulas ni datos; reutilizar antes
de crear (estilos, iconos, constantes); sin emojis; ajustes por código sin
regenerar `.ui` (D-011); verificar tras cada bloque (`docs/TESTING.md`); no
hacer commit sin revisión visual del usuario.

