# Project Context

## Identificación

**Proyecto:** Run Acoustic  
**Tipo:** Proyecto de grado — Ingeniería Industrial, Universidad del
Atlántico  
**Propósito:** Software para evaluar condiciones acústicas de aulas
mediante tiempo de reverberación e inteligibilidad de la palabra.

## Estado académico

El documento Word `proyectoGradoSoftware.docx` es la versión académica
vigente sobre la cual continuará el trabajo.

El PDF histórico sobre las condiciones acústicas del Bloque H se
conserva como antecedente y referencia, no como fuente primaria para
describir el estado actual del software.

## Alcance funcional

El documento académico vigente describe tres componentes principales:

1.  Tiempo de Reverberación.
2.  Inteligibilidad del Habla.
3.  Base de Datos de aulas del Bloque H.

La aplicación contempla ingreso de dimensiones, materiales y objetos;
cálculo acústico; visualización de resultados; gráficos; generación de
PDF y consulta de aulas caracterizadas.

## Modelo acústico

El software implementa: - Sabine; - Eyring; - %ALCons; - modelo de Peutz
para pérdida de consonantes; - bandas de 125, 250, 500, 1000, 2000 y
4000 Hz.

La implementación actual de %ALCons se considera, según el equipo,
equivalente a la descrita en el Word vigente.

## Datos

El sistema usa actualmente una solución híbrida: - diccionarios Python
para los 23 tipos de salón del Bloque H; - archivos Excel para
coeficientes de absorción acústica.

## Tecnología

- Python.
- PySide6 / Qt6.
- Qt Designer.
- PyCharm.
- pandas.
- Matplotlib.
- ReportLab.

## Arquitectura declarada

La tesis describe el uso de MVC. El repositorio contiene carpetas
`Modelo`, `Vista`, `Controlador`, `Datos` y `Recursos`.

La arquitectura real debe seguir auditándose antes de realizar una
refactorización mayor.

## Principio de evolución

El objetivo no es simplemente “hacer que funcione”. El objetivo es
evolucionar la aplicación hacia un software: - mantenible; - trazable; -
validado; - documentado; - usable; - estable; - preparado para futuras
extensiones.

## Responsabilidad de IA

Claude debe actuar como apoyo de ingeniería y no como sustituto del
criterio académico. Los cambios que alteren el significado físico o
matemático deben ser revisados por el equipo.
