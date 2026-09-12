# AI_RULES.md

## Fuente de verdad

1.  Código actual del repositorio = verdad de implementación.
2.  `docs/ACOUSTIC_MODEL.md` = verdad técnica del modelo matemático
    aprobado.
3.  Word vigente de la tesis = verdad académica.
4.  `docs/` = memoria técnica y coordinación.
5.  Conversaciones con IA = no son fuente de verdad.

## Prioridades de Claude

1.  Preservar funcionalidad existente.
2.  Preservar trazabilidad de identificadores.
3.  Mejorar corrección y robustez.
4.  Mejorar UX/UI cuando sea parte de la tarea.
5.  Reducir duplicación y complejidad cuando exista evidencia.
6.  Documentar cambios.

## Identificadores

Conservar nombres existentes por defecto. Un renombramiento requiere
búsqueda global de referencias y actualización completa.

No cambiar simultáneamente nombres, arquitectura y lógica matemática sin
necesidad.

## Acústica

No alterar Sabine, Eyring o Peutz/%ALCons sin comparación contra la
fuente académica y validación de resultados.

## UI

Los `.ui` y los `.py` generados deben mantenerse sincronizados. No
modificar a mano código generado si la fuente real del cambio es Qt
Designer.

## Datos

Actualmente: - 23 tipos de salones del Bloque H; - diccionarios Python
para datos de salones; - Excel para coeficientes de absorción.

Una migración de almacenamiento debe ser una decisión explícita.

## Cambios

Cada tarea importante debe terminar con: - resumen de cambios; -
archivos afectados; - pruebas realizadas; - riesgos o pendientes; -
documentación actualizada; - estado de Git.

## Seguridad de Git

No force-push, reset destructivo, borrado de ramas ni eliminación masiva
de archivos sin autorización.

## Estilo de desarrollo

Preferir cambios pequeños, reversibles, verificables y trazables.
