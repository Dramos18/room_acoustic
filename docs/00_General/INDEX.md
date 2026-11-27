# Room Acoustic — Índice de documentación

Esta carpeta contiene la memoria técnica, científica, funcional y de gestión del proyecto. La documentación está organizada por áreas temáticas para facilitar su consulta por el equipo y por herramientas de asistencia como Claude Code.

**Estructura reorganizada:** 2026-11-27  
**Rama:** `docs/knowledge-base-2026-11`

## Cómo leer esta documentación

Ante contradicciones, aplicar este orden de autoridad:

1. **Implementación:** código existente en la rama revisada.
2. **Modelo matemático y decisiones aprobadas:** documentación del modelo acústico y decisiones vigentes.
3. **Estado y evidencia de ingeniería:** estado actual, pruebas, auditorías y validaciones.
4. **Base académica:** documento Word vigente; debe describir el comportamiento efectivamente aprobado y verificado.
5. **Historial y conversaciones:** sirven para trazabilidad, pero no sustituyen código, evidencia ni decisiones aprobadas.

Cuando algo no esté demostrado, identificarlo como **POR VALIDAR**, **PENDIENTE DE EVIDENCIA** o **HALLAZGO DE AUDITORÍA**. No presentar propuestas como funcionalidades implementadas.

## Mapa de carpetas

### 00_General — Identidad y continuidad
- [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md): propósito, alcance y contexto.
- [CURRENT_STATE.md](CURRENT_STATE.md): fotografía vigente del estado del proyecto e historial conservado.
- [HANDOFF.md](HANDOFF.md): guía para retomar el trabajo.

### 01_Arquitectura_y_Desarrollo — Diseño técnico
- [ARCHITECTURE.md](../01_Arquitectura_y_Desarrollo/ARCHITECTURE.md): arquitectura y estructura MVC+S.
- [INTEGRATION.md](../01_Arquitectura_y_Desarrollo/INTEGRATION.md): impacto entre software y memoria académica.
- [NAMING_AND_TRACEABILITY.md](../01_Arquitectura_y_Desarrollo/NAMING_AND_TRACEABILITY.md): identificadores y trazabilidad.
- [DEPENDENCIES.md](../01_Arquitectura_y_Desarrollo/DEPENDENCIES.md): dependencias y entorno.
- [ACCOUNTING_MODEL.md](../01_Arquitectura_y_Desarrollo/ACCOUNTING_MODEL.md): documento heredado; pertinencia por confirmar.

### 02_Modelo_Acustico_y_Datos — Dominio científico y datos
- [ACOUSTIC_MODEL.md](../02_Modelo_Acustico_y_Datos/ACOUSTIC_MODEL.md): formulación, parámetros y comportamiento acústico.
- [ACOUSTIC_DATA_CATALOG.md](../02_Modelo_Acustico_y_Datos/ACOUSTIC_DATA_CATALOG.md): catálogo de 23 perfiles de aulas y trazabilidad de datos.
- [ALCONS_CLASSIFICATION_REVIEW.md](../02_Modelo_Acustico_y_Datos/ALCONS_CLASSIFICATION_REVIEW.md): revisión bibliográfica y criterio operativo de clasificación.

### 03_Modulos_y_Requisitos — Especificación funcional
- [REQUIREMENTS.md](../03_Modulos_y_Requisitos/REQUIREMENTS.md): requisitos del sistema.
- [MODULES_SPECIFICATION.md](../03_Modulos_y_Requisitos/MODULES_SPECIFICATION.md): especificación de M1, M2 y M3.
- [REPORTS.md](../03_Modulos_y_Requisitos/REPORTS.md): generación y comportamiento de reportes PDF.

### 04_Interfaz_y_Recursos — Presentación
- [UI_INVENTORY.md](../04_Interfaz_y_Recursos/UI_INVENTORY.md): pantallas, archivos UI y patrones.
- [RESOURCES.md](../04_Interfaz_y_Recursos/RESOURCES.md): iconos, imágenes, estilos y recursos.

### 05_Calidad_y_Validacion — Verificación y deuda técnica
- [TESTING.md](../05_Calidad_y_Validacion/TESTING.md): procedimientos de prueba.
- [SOFTWARE_VALIDATION.md](../05_Calidad_y_Validacion/SOFTWARE_VALIDATION.md): verificación, validación matemática, experimental y usabilidad.
- [CODEBASE_AUDIT.md](../05_Calidad_y_Validacion/CODEBASE_AUDIT.md): hallazgos de auditoría estática.

### 06_Historial_y_Decisiones — Gobierno del proyecto
- [CHANGELOG.md](../06_Historial_y_Decisiones/CHANGELOG.md): cronología de cambios.
- [DECISIONS.md](../06_Historial_y_Decisiones/DECISIONS.md): decisiones técnicas y metodológicas.
- [DEVELOPMENT_HISTORY.md](../06_Historial_y_Decisiones/DEVELOPMENT_HISTORY.md): hitos y evolución consolidada.

### 07_Trabajo_con_IA — Colaboración con asistentes
- [DEVELOPMENT_WORKFLOW.md](../07_Trabajo_con_IA/DEVELOPMENT_WORKFLOW.md): flujo de trabajo.
- [AI_ROLES.md](../07_Trabajo_con_IA/AI_ROLES.md): responsabilidades y límites de los asistentes.
- [CLAUDE_FIRST_SESSION.md](../07_Trabajo_con_IA/CLAUDE_FIRST_SESSION.md): guía de primera sesión.
- [CLAUDE_TASK_TEMPLATE.md](../07_Trabajo_con_IA/CLAUDE_TASK_TEMPLATE.md): plantilla para definir tareas.

### 08_Alineacion_Academica — Trabajo de grado
- [ACADEMIC_ALIGNMENT.md](../08_Alineacion_Academica/ACADEMIC_ALIGNMENT.md): matriz de alineación entre el manuscrito académico y el software.

## Reglas de mantenimiento

- Registrar cambios técnicos relevantes en `06_Historial_y_Decisiones/CHANGELOG.md`.
- Registrar decisiones aprobadas en `06_Historial_y_Decisiones/DECISIONS.md`.
- Actualizar `00_General/CURRENT_STATE.md` cuando cambie el estado funcional o técnico.
- Actualizar `00_General/HANDOFF.md` al cambiar prioridades o el siguiente paso.
- Actualizar `05_Calidad_y_Validacion/TESTING.md` cuando se incorporen pruebas o cambien procedimientos.
- Actualizar `08_Alineacion_Academica/ACADEMIC_ALIGNMENT.md` cuando una implementación afecte la tesis.
- Mantener una única fuente detallada por tema y enlazarla desde los demás documentos; evitar duplicación.
- Al mover documentos, actualizar enlaces Markdown y referencias de ruta en toda la carpeta.

## Alcance de esta reorganización

Se reorganizaron los documentos existentes por área temática. La reorganización es estructural: no implica que todos los contenidos hayan sido auditados de nuevo ni que las pruebas del software se hayan ejecutado. Los estados de validación y las limitaciones documentadas siguen vigentes.
