# AI RULES — ROOM ACOUSTIC

## 1. Propósito
Reglas rectoras para cualquier asistente de IA que trabaje sobre el proyecto **Software para evaluar la acústica en aulas: tiempo de reverberación e inteligibilidad de la palabra**.

## 2. Fuente de verdad
1. Código del repositorio: implementación realmente existente.
2. Documentación técnica de GitHub: estado, arquitectura, requisitos y decisiones.
3. Documento académico vigente: contexto y contenido académico.
4. Fuentes bibliográficas/normativas: respaldo teórico.
5. Conversaciones con IA: no son fuente permanente.

Ante contradicciones, la IA debe señalarlas y pedir validación.

## 3. No inventar
No inventar resultados, mediciones, referencias, requisitos, funcionalidades, archivos, fórmulas, criterios normativos o decisiones. Usar `POR VALIDAR` cuando algo no esté confirmado.

## 4. Antes de modificar software
Leer `AI_RULES.md`, `docs/PROJECT_CONTEXT.md`, `docs/CURRENT_STATE.md`, `docs/ARCHITECTURE.md`, `docs/REQUIREMENTS.md`, `docs/ACOUSTIC_MODEL.md`, `docs/DECISIONS.md`, `docs/CHANGELOG.md` y `docs/HANDOFF.md`. Leer `docs/INTEGRATION.md` si existe impacto académico.

## 5. Antes de modificar documentación
Leer `AI_RULES.md`, `docs/PROJECT_CONTEXT.md`, `docs/CURRENT_STATE.md`, `docs/INTEGRATION.md`, `docs/HANDOFF.md` y la documentación de `research/` y `thesis/`.

## 6. Modelo acústico protegido
No modificar Sabine, Eyring, %ALCons, variables, unidades, rangos o supuestos sin validación. Todo cambio debe quedar registrado en `DECISIONS.md`, `ACOUSTIC_MODEL.md` y `CHANGELOG.md`, con casos de prueba.

## 7. No refactorizar masivamente sin aprobación
Proceso obligatorio: **analizar → proponer → aprobar → implementar → probar → documentar → commit**.

## 8. Qt Designer
Los `.ui` son fuente de diseño. Los `.py` generados deben tratarse como artefactos derivados y no modificarse manualmente sin justificación.

## 9. Datos
Excel, diccionarios y archivos actualmente utilizados son datos activos hasta demostrar lo contrario. No eliminarlos ni migrarlos sin análisis de dependencias.

## 10. Interfaz
Un cambio de ventana debe actualizar `UI_INVENTORY.md`, `CURRENT_STATE.md` y `CHANGELOG.md`, y las capturas académicas cuando corresponda.

## 11. Coordinación
GitHub es el espacio central de sincronización. La información que deba sobrevivir entre sesiones debe quedar documentada.

## 12. Trazabilidad
Todo cambio significativo debe poder responder: qué cambió, por qué, qué archivos afecta, qué requisito satisface, cómo se verificó y si afecta el documento académico.

## 13. Roles
**Desarrollador:** software, arquitectura, PySide6, Qt Designer, modelo acústico, pruebas y evolución técnica.

**Documentación:** teoría, bibliografía, metodología, resultados, redacción y trazabilidad académica.

Ningún asistente debe asumir automáticamente decisiones del otro.
