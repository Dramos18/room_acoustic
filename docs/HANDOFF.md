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

Orden acordado: primero cerrar cada módulo, tomando el Módulo 1 como
referencia visual.

1. **Módulo 2 — Inteligibilidad**: formulario → resultados → reporte. Alinear
   barra superior/inferior, botón "Atrás", botón principal, encabezados y
   estados con el patrón de `docs/UI_INVENTORY.md`; quitar el chevron de
   "Ir al Inicio". Hoy sus resultados son un `QMessageBox`.
2. **Módulo 3 — Base de Datos**: formulario/selección → resultados →
   flujo de reporte. Considerar `base-de-datos.png` (`RESOURCES.md`).
3. **Ventana**: mover, redimensionar, maximizar/minimizar (D-016).
4. **Feedback al guardar el PDF** (D-017).
5. **Iconos**: el equipo agrega los recursos que vea necesarios en
   `Recursos/iconos/` y los registra en `docs/RESOURCES.md` (sección 8).
6. Pendientes P3 del Módulo 1 en `docs/CHANGELOG.md` (eje logarítmico del
   gráfico, iconos de inicio/guardar, etc.).

Reglas vigentes para continuar: no tocar fórmulas ni datos; reutilizar antes
de crear (estilos, iconos, constantes); sin emojis; ajustes por código sin
regenerar `.ui` (D-011); verificar tras cada bloque (`docs/TESTING.md`); no
hacer commit sin revisión visual del usuario.

