# Room Acoustic — Índice de documentación

Este directorio contiene la memoria técnica del software, el registro de decisiones y cambios, la evidencia de verificación y los documentos de coordinación con el trabajo académico.

**Última reorganización:** 2026-11-27  
**Rama de trabajo:** `docs/knowledge-base-2026-11`

## 1. Cómo leer la documentación

No todos los documentos tienen el mismo propósito ni autoridad. Ante una contradicción, aplicar este orden:

1. **Implementación:** código que existe en la rama revisada del repositorio.
2. **Modelo matemático aprobado:** `ACOUSTIC_MODEL.md`, junto con las decisiones y referencias que lo sustentan.
3. **Criterios y decisiones de desarrollo:** `DECISIONS.md`.
4. **Estado y evidencia de ingeniería:** `CURRENT_STATE.md`, `CHANGELOG.md`, `TESTING.md`, auditorías y documentos especializados.
5. **Base académica:** documento Word vigente de trabajo de grado. Describe el planteamiento académico y debe actualizarse cuando exista evidencia validada de cambios del software.
6. **Conversaciones con asistentes:** contexto auxiliar; nunca sustituyen las fuentes anteriores.

Cuando una afirmación no esté demostrada, usar **POR VALIDAR**, **PENDIENTE DE EVIDENCIA** o **HALLAZGO DE AUDITORÍA**. No presentar una propuesta o requisito como funcionalidad implementada.

## 2. Mapa documental

### A. Identidad, contexto y estado del proyecto

| Documento | Propósito |
|---|---|
| [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) | Identidad, propósito, alcance y contexto general |
| [CURRENT_STATE.md](CURRENT_STATE.md) | Estado vigente y registro cronológico de evolución; leer primero la actualización superior |
| [HANDOFF.md](HANDOFF.md) | Instrucciones para retomar trabajo en una nueva sesión |
| [INDEX.md](INDEX.md) | Este mapa de documentación |

### B. Arquitectura, datos e integración

| Documento | Propósito |
|---|---|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Estructura MVC+S y responsabilidades de carpetas |
| [INTEGRATION.md](INTEGRATION.md) | Impacto entre cambios del software y memoria académica |
| [NAMING_AND_TRACEABILITY.md](NAMING_AND_TRACEABILITY.md) | Conservación y trazabilidad de identificadores |
| [DEPENDENCIES.md](DEPENDENCIES.md) | Dependencias y entorno Linux/SteamOS |
| [ACOUSTIC_DATA_CATALOG.md](ACOUSTIC_DATA_CATALOG.md) | Inventario de los 23 perfiles del Bloque H, esquema, materiales y trazabilidad pendiente |
| [RESOURCES.md](RESOURCES.md) | Inventario de iconos, GIF y estilos |
| [ACCOUNTING_MODEL.md](ACCOUNTING_MODEL.md) | Documento existente; alcance y pertinencia por confirmar |

### C. Dominio acústico y requisitos

| Documento | Propósito |
|---|---|
| [ACOUSTIC_MODEL.md](ACOUSTIC_MODEL.md) | Formulación y parámetros acústicos implementados |
| [ALCONS_CLASSIFICATION_REVIEW.md](ALCONS_CLASSIFICATION_REVIEW.md) | Análisis de fuentes y criterio operativo D-019 |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Requisitos funcionales, no funcionales y criterios |
| [MODULES_SPECIFICATION.md](MODULES_SPECIFICATION.md) | Especificación funcional y técnica de M1, M2 y M3: entradas, procesamiento, salidas, archivos y validaciones |
| [REPORTS.md](REPORTS.md) | Diseño y comportamiento de reportes PDF |

### D. Interfaz y experiencia de usuario

| Documento | Propósito |
|---|---|
| [UI_INVENTORY.md](UI_INVENTORY.md) | Inventario de pantallas, archivos UI y patrones visuales |

### E. Calidad, auditoría y deuda técnica

| Documento | Propósito |
|---|---|
| [TESTING.md](TESTING.md) | Procedimientos de pruebas manuales y regresión |
| [SOFTWARE_VALIDATION.md](SOFTWARE_VALIDATION.md) | Separación de verificación, validación matemática, experimental y usabilidad; matriz de evidencia y cierre |
| [CODEBASE_AUDIT.md](CODEBASE_AUDIT.md) | Hallazgos de auditoría estática; revisar vigencia antes de actuar |
| [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md) | Flujo de trabajo desde preparación hasta documentación |

### F. Historial y gobierno del proyecto

| Documento | Propósito |
|---|---|
| [CHANGELOG.md](CHANGELOG.md) | Registro cronológico de cambios relevantes |
| [DECISIONS.md](DECISIONS.md) | Decisiones técnicas y metodológicas con su estado |
| [DEVELOPMENT_HISTORY.md](DEVELOPMENT_HISTORY.md) | Hitos consolidados y evolución funcional del software |
| [AI_ROLES.md](AI_ROLES.md) | Responsabilidades de usuario, Claude y apoyo documental |

### G. Continuidad y uso de asistentes

| Documento | Propósito |
|---|---|
| [CLAUDE_FIRST_SESSION.md](CLAUDE_FIRST_SESSION.md) | Instrucción para una primera auditoría con Claude Code |
| [CLAUDE_TASK_TEMPLATE.md](CLAUDE_TASK_TEMPLATE.md) | Plantilla para definir tareas de implementación |

### H. Relación con el documento académico

| Documento | Propósito |
|---|---|
| [ACADEMIC_ALIGNMENT.md](ACADEMIC_ALIGNMENT.md) | Matriz de alineación entre el Word académico y el software actual; registra discrepancias que deben resolverse antes de actualizar la tesis |

## 3. Convenciones de mantenimiento

- Actualizar `CHANGELOG.md` cuando se complete un cambio técnico relevante.
- Actualizar `DECISIONS.md` cuando el equipo adopte o cambie una decisión.
- Actualizar `CURRENT_STATE.md` cuando cambie el estado funcional o técnico.
- Actualizar `HANDOFF.md` cuando cambien las prioridades o el siguiente paso recomendado.
- Actualizar `TESTING.md` cuando se incorporen pruebas o cambien los procedimientos de verificación.
- Actualizar `ACADEMIC_ALIGNMENT.md` cuando una implementación modifique requisitos, metodología, resultados, capturas o afirmaciones de la tesis.
- No duplicar contenido extenso: mantener un documento especializado como fuente y enlazarlo desde los demás.

## 4. Estado de la reorganización

Esta primera versión organiza el inventario y añade documentos de trazabilidad. No implica que todos los documentos existentes hayan sido revisados línea por línea ni que su contenido esté completamente actualizado.

La reconciliación documental es incremental. `CURRENT_STATE.md` y `HANDOFF.md` tienen una actualización vigente al inicio y conservan debajo el registro histórico. `CODEBASE_AUDIT.md` y las secciones antiguas de `CHANGELOG.md` aún requieren revisión de vigencia; no deben interpretarse automáticamente como estado actual.
