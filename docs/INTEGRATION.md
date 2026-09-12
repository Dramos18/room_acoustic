# Integration — Software ↔ Thesis

## Regla principal

Una modificación del software puede producir impacto académico, pero no
todo cambio técnico requiere modificar la tesis.

## Tipos de cambio

### A — Interno

Ejemplo: - renombrar una variable local; - limpiar `print()`; - mejorar
estructura interna sin cambiar resultados.

Impacto académico: normalmente ninguno.

### B — Funcional

Ejemplo: - nuevo botón; - nuevo flujo; - nuevo reporte; - nuevo módulo.

Impacto: puede requerir actualizar descripción, capturas y metodología.

### C — Matemático

Ejemplo: - cambiar fórmula; - cambiar parámetro; - cambiar
clasificación; - cambiar frecuencia o referencia.

Impacto académico: obligatorio revisar Word, resultados y validación.

### D — Datos

Ejemplo: - cambiar 23 aulas; - cambiar coeficientes; - cambiar
estructura de almacenamiento.

Impacto: revisar resultados y tablas.

## Protocolo

1.  Claude identifica el tipo de cambio.
2.  Se actualiza código.
3.  Se ejecutan pruebas.
4.  Se identifica impacto académico.
5.  Se registra en este documento o `CHANGELOG`.
6.  El equipo actualiza Word si corresponde.
7.  Las capturas se reemplazan solo después de validar la UI.

## Regla de resultados

Nunca actualizar la tesis con resultados generados por una versión no
validada del software.
