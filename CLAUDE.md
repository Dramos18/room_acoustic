# CLAUDE.md — Instrucciones permanentes para Claude Code

## 1. Identidad del proyecto

Este repositorio es el proyecto de grado de Ingeniería Industrial de la
Universidad del Atlántico para el desarrollo de un software de
evaluación acústica de aulas.

El repositorio actual es `Run Acoustic` y su rama principal histórica
indicada por el equipo es `master`. Antes de asumir el nombre de la rama
por defecto, verificar siempre con `git branch --show-current`,
`git remote -v` y, si aplica, la configuración de GitHub.

La fuente académica principal y vigente es el documento Word más
reciente del proyecto. El PDF histórico sobre el Bloque H es material de
referencia, no la fuente de verdad actual.

## 2. Objetivo de Claude

Claude actúa como agente de ingeniería del proyecto: debe investigar el
código existente, proponer mejoras, implementar cambios cuando el
usuario lo solicite, ejecutar verificaciones, explicar los cambios y
mantener la documentación sincronizada.

No debe limitarse a sugerir código si el usuario pidió explícitamente
implementarlo.

## 3. Regla crítica de trazabilidad de variables y nombres

Los nombres de variables, funciones, clases, atributos, claves de
diccionario, widgets y otros identificadores existentes son parte del
contrato de trazabilidad del proyecto.

Reglas:

1.  No renombrar identificadores existentes solo por estilo.
2.  Antes de renombrar un identificador, buscar todas sus referencias en
    el repositorio.
3.  Si el renombramiento aporta una mejora real de legibilidad,
    usabilidad, mantenibilidad o consistencia, proponerlo primero cuando
    pueda afectar muchos archivos.
4.  Si se aprueba un renombramiento, actualizar todas las referencias en
    una sola operación coherente.
5.  Nunca dejar referencias parcialmente migradas.
6.  Registrar los renombramientos importantes en `docs/CHANGELOG.md` y,
    si afectan arquitectura o integración, en `docs/DECISIONS.md` o
    `docs/INTEGRATION.md`.
7.  Preferir conservar nombres existentes aunque no sean perfectos si el
    cambio no aporta una mejora suficientemente clara.
8.  Las claves de datos y nombres usados para comunicar módulos deben
    tratarse con especial cuidado porque pueden ser dependencias
    implícitas.

## 4. Antes de modificar código

Siempre:

- inspeccionar `git status`;
- identificar la rama actual;
- leer `AI_RULES.md`, `docs/PROJECT_CONTEXT.md`,
  `docs/CURRENT_STATE.md`, `docs/CHANGELOG.md` y `docs/HANDOFF.md`;
- para cálculos acústicos, leer también `docs/ACOUSTIC_MODEL.md`;
- para cambios de arquitectura, leer `docs/ARCHITECTURE.md`;
- para requisitos/UI, leer `docs/REQUIREMENTS.md` y
  `docs/UI_INVENTORY.md`;
- abrir los archivos reales involucrados antes de hacer afirmaciones
  sobre su contenido.

Nunca especular sobre código que no se haya inspeccionado.

## 5. Flujo obligatorio de trabajo

Para cambios no triviales:

ANALIZAR → PROPONER → IMPLEMENTAR → VERIFICAR → DOCUMENTAR → MOSTRAR
DIFF.

Si el cambio es potencialmente riesgoso para el modelo acústico, primero
separar: - cambio matemático; - cambio de implementación; - cambio de
interfaz.

Un cambio en uno no debe implicar automáticamente cambios en los otros.

## 6. Variables y modelo acústico

El software trabaja actualmente con:

- Tiempo de reverberación;
- modelos de Sabine y Eyring;
- frecuencias de 125, 250, 500, 1000, 2000 y 4000 Hz;
- inteligibilidad mediante %ALCons;
- modelo de Peutz;
- Q = 2 para voz humana en dirección frontal;
- datos de aulas del Bloque H;
- Excel para coeficientes acústicos;
- diccionarios Python para los 23 tipos de salón.

No modificar el modelo matemático solo para “mejorar” el código. Toda
modificación matemática debe estar respaldada por la fuente académica y
registrada como cambio que requiere validación.

## 7. UI y archivos generados

No editar manualmente archivos generados por Qt si el cambio corresponde
realmente al diseño `.ui`.

Cuando corresponda: 1. modificar el `.ui` en Qt Designer; 2. regenerar
el `.py`; 3. revisar las referencias del código; 4. probar la ventana.

No eliminar archivos `.ui` o `.py` generados sin verificar sus
dependencias.

## 8. Datos

No sustituir Excel o los diccionarios por otra tecnología únicamente por
preferencia técnica.

Una migración a JSON, SQLite, otra base de datos o una estructura
distinta solo procede si: - existe una ventaja técnica clara; - se
analiza el impacto; - se preserva la trazabilidad; - se validan los
resultados; - se documenta la decisión.

## 9. Pruebas

Antes de declarar un cambio terminado:

- ejecutar las pruebas disponibles;
- si no existen pruebas automatizadas para el área modificada, crear
  pruebas razonables o una verificación reproducible;
- ejecutar al menos una prueba de humo de la aplicación cuando el cambio
  afecte UI/integración;
- comprobar que los resultados acústicos no cambien accidentalmente.

No eliminar ni debilitar pruebas para hacer que el proyecto pase.

## 10. Git

No ejecutar: - `git push --force`; - `git reset --hard`; - borrado de
ramas; - eliminación masiva de archivos; - cambios destructivos en
datos;

sin confirmación explícita del usuario.

Para trabajo normal, usar commits pequeños y descriptivos.

## 11. Documentación

Después de cambios significativos actualizar los documentos afectados.

La documentación debe describir el estado real del repositorio, no un
estado ideal.

Si algo no está verificado, marcarlo como `POR VALIDAR`.

## 12. Principio de mínima sorpresa

No realizar refactorizaciones grandes, migraciones tecnológicas o nuevas
abstracciones solo porque sean posibles.

Primero mejorar: - corrección; - estabilidad; - trazabilidad; -
usabilidad; - mantenibilidad; - pruebas; - documentación.

Después optimizar arquitectura si existe una justificación concreta.

## 13. Contexto de la tesis

El Word vigente describe el desarrollo como una herramienta para evaluar
condiciones acústicas de aulas, con módulos de Tiempo de Reverberación,
Inteligibilidad del Habla y Base de Datos del Bloque H.

El Word es la fuente académica. Los `.md` son documentación técnica y de
coordinación para el desarrollo.
