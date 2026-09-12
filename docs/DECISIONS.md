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
