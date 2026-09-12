# Prompt Template — Tareas futuras

Usa esta estructura para pedir cambios importantes a Claude:

## Objetivo

Quiero \[describir comportamiento deseado\].

## Problema actual

Actualmente \[describir comportamiento\].

## Restricciones

- conservar identificadores existentes;
- no modificar fórmulas sin validación;
- no eliminar archivos sin confirmar;
- no refactorizar partes no relacionadas;
- mantener compatibilidad con la arquitectura actual salvo
  justificación.

## Criterios de aceptación

- \[criterio 1\]
- \[criterio 2\]
- \[criterio 3\]

## Forma de trabajo

Antes de editar: 1. inspecciona archivos relacionados; 2. identifica
dependencias; 3. explica brevemente el plan.

Después: 1. implementa; 2. ejecuta pruebas; 3. muestra diff; 4. resume
archivos modificados; 5. actualiza documentación; 6. indica
riesgos/pedientes.

## Regla de trazabilidad

Si un identificador existente debe cambiar: - busca todas las
referencias; - actualízalas; - comprueba que no queden referencias
antiguas; - documenta el cambio.
