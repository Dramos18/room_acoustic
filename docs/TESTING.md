# Testing Strategy

## Situación actual

El snapshot no contiene una suite automatizada.

Esto debe corregirse progresivamente antes de grandes refactorizaciones.

## Nivel 1 — Smoke test

Verificar: - la aplicación inicia; - la ventana principal abre; - la
navegación funciona; - no hay errores de importación; - recursos
gráficos se cargan.

## Nivel 2 — Pruebas unitarias acústicas

Prioridad: - áreas; - absorción; - Sabine; - Eyring; - distancia
crítica; - %ALCons; - clasificación.

## Nivel 3 — Casos de referencia

Crear casos conocidos del proyecto académico.

Cada caso debe registrar: - entradas; - resultado esperado; -
tolerancia; - fuente.

## Nivel 4 — Integración

Verificar: - UI → cálculo; - cálculo → resultados; - resultados → PDF; -
datos Excel → cálculo; - diccionarios de salones → análisis.

## Nivel 5 — Regresión

Cada bug importante debe convertirse en una prueba para evitar que
vuelva a aparecer.

## Regla

Un refactor de una función de cálculo sin prueba equivalente debe
considerarse incompleto.
