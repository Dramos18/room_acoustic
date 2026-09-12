# Prompt — Primera sesión con Claude Code

Copia este prompt en Claude Code después de abrir el repositorio.

------------------------------------------------------------------------

Quiero que trabajemos sobre este repositorio como un proyecto real de
ingeniería de software y de grado.

Antes de modificar cualquier archivo:

1.  verifica la raíz del repositorio;
2.  ejecuta `git status`;
3.  verifica la rama actual y el remoto;
4.  lee `CLAUDE.md`;
5.  lee `AI_RULES.md`;
6.  lee:
    - `docs/PROJECT_CONTEXT.md`
    - `docs/CURRENT_STATE.md`
    - `docs/AI_ROLES.md`
    - `docs/ARCHITECTURE.md`
    - `docs/REQUIREMENTS.md`
    - `docs/ACOUSTIC_MODEL.md`
    - `docs/UI_INVENTORY.md`
    - `docs/DECISIONS.md`
    - `docs/INTEGRATION.md`
    - `docs/HANDOFF.md`
    - `docs/CODEBASE_AUDIT.md`
    - `docs/NAMING_AND_TRACEABILITY.md`
    - `docs/TESTING.md`

Después haz una auditoría del código real.

Quiero que identifiques: - punto de entrada; - flujo principal de la
aplicación; - módulos activos; - módulos duplicados/legacy; -
dependencias; - rutas de recursos; - puntos de acoplamiento; - funciones
de cálculo; - flujo de datos Excel → modelo → UI; - flujo de datos
diccionarios → modelo → UI; - flujo de resultados → PDF; - ausencia de
pruebas; - riesgos técnicos.

REGLA CRÍTICA: No cambies nombres de variables, funciones, clases,
atributos o claves existentes salvo que exista una razón clara. Si
propones un renombramiento, primero muestra el impacto y asegúrate de
actualizar TODAS las referencias.

No hagas todavía una gran refactorización.

Tu primera entrega debe ser un informe técnico de auditoría con: 1.
arquitectura real; 2. mapa de dependencias; 3. problemas encontrados; 4.
riesgos; 5. prioridades P0/P1/P2/P3; 6. estrategia de pruebas; 7.
propuesta de roadmap.

Después quiero que esperes mi decisión sobre qué punto implementar
primero.

No inventes comportamiento que no hayas verificado leyendo el código.
