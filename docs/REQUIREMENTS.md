# Requirements

## Funcionales

### RF-01 — Evaluación de tiempo de reverberación

El sistema debe permitir ingresar/obtener: - dimensiones; -
superficies; - materiales; - objetos adheridos; - objetos adicionales.

Debe calcular RT60 por bandas.

### RF-02 — Métodos acústicos

Debe soportar: - Sabine; - Eyring.

### RF-03 — Bandas

Bandas actuales: - 125 Hz; - 250 Hz; - 500 Hz; - 1000 Hz; - 2000 Hz; -
4000 Hz.

### RF-04 — Inteligibilidad

Debe permitir calcular %ALCons mediante el modelo de Peutz.

### RF-05 — Parámetros de Peutz

La implementación actual contempla, entre otros: - distancia; - TR a
2000 Hz; - volumen; - factor de directividad; - distancia crítica; -
superficie total; - coeficiente medio de absorción.

### RF-06 — Base de datos Bloque H

Debe contener los 23 tipos de salón definidos por el proyecto.

### RF-07 — Reportes

Debe permitir generar resultados en PDF.

### RF-08 — Visualización

Debe permitir visualizar resultados acústicos de forma comprensible y
mediante gráficos donde corresponda.

## Validación de entrada

El Word vigente establece, entre otros criterios: - dimensiones mayores
que 1 m; - áreas de objetos no mayores que la superficie disponible; -
coeficientes de absorción entre 0 y 1; - campos obligatorios; - RT60 \>
0; - referencia de 2000 Hz para inteligibilidad; - distancia de
referencia 1.5 m; - Q = 2.

Los criterios exactos deben permanecer alineados con la versión vigente
del Word.

## No funcionales

- Usabilidad.
- Legibilidad.
- Estabilidad.
- Mantenibilidad.
- Trazabilidad.
- Compatibilidad con el entorno Python/PySide6 definido por el proyecto.
- Resultados reproducibles.
- Reportes consistentes.

## Criterios académicos de validación

Según el Word vigente: - error de RT \< 10 % para al menos tres aulas de
referencia; - error de inteligibilidad ≤ 5 % frente a referencias.

Estos criterios no deben relajarse sin una decisión académica explícita.

## Cambios futuros

Cualquier requisito nuevo debe registrarse antes o durante su
implementación y, cuando corresponda, relacionarse con una prueba.
