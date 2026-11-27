# Auditoría estática del código — estado y trazabilidad

**Corte de actualización:** 2026-11-27  
**Rama inspeccionada:** `docs/knowledge-base-2026-11`  
**Naturaleza:** revisión estática de código y documentación. No equivale a pruebas de ejecución ni autoriza por sí sola cambios de comportamiento.

## 1. Alcance y criterio de lectura

Este archivo se originó como auditoría del snapshot inicial `room_acoustic-master.zip`. Sus hallazgos se conservaron para trazabilidad, pero algunos fueron corregidos posteriormente. Esta versión distingue:
- **Corregido:** existe evidencia documental posterior de la corrección.
- **Vigente observado:** el patrón sigue presente en el código inspeccionado.
- **Pendiente de verificación:** requiere análisis de ejecución, dependencias o impacto antes de concluir.
- **Histórico:** describe el estado de un snapshot anterior y no debe tratarse como defecto actual.

La fuente de verdad para el comportamiento es el código de la rama evaluada; el historial y las pruebas documentadas permiten conocer cuándo y cómo se verificaron los cambios.

## 2. Arquitectura y rutas principales

La aplicación principal está organizada en `Controlador/`, `Datos/`, `Modelo/`, `Recursos/` y `Vista/`. El punto de entrada documentado es `Vista/main.py`. El entorno y dependencias se describen en `DEPENDENCIES.md`; la arquitectura lógica, en `ARCHITECTURE.md`.

## 3. Hallazgos y estado al corte

### AUD-01 — Implementaciones alternativas/legacy de modelos

**Observación:** existen `Modelo/alcons2.py` y `Modelo/%alcons.py`, así como `Modelo/calculoRT2.py` y `Modelo/calculoRT.py`.

**Estado:** pendiente de auditoría de dependencias completa. La interfaz principal de inteligibilidad importa `Modelo.alcons2`; el flujo principal de reverberación usa `Modelo/calculoRT2`. La revisión anterior de `ALCONS_CLASSIFICATION_REVIEW.md` no identificó imports de `Modelo/%alcons.py` en el repositorio, pero esto no basta para eliminarlo sin revisar usos indirectos, scripts y consumidores externos.

**Acción:** mapear imports y llamadas, comparar comportamiento y registrar decisión antes de retirar o fusionar módulos. No eliminar archivos legacy como parte de una limpieza incidental.

### AUD-02 — Archivo `prueba.py`

**Observación:** importa PyQt5 y referencia `Recursos.MainWindow`, mientras que la aplicación principal usa PySide6 y el snapshot revisado no contiene ese módulo.

**Estado:** probable archivo legacy/de prueba; no forma parte del flujo principal documentado.

**Acción:** confirmar si alguien lo utiliza antes de archivarlo o retirarlo. PyQt5 no debe añadirse a las dependencias principales por este archivo sin una decisión expresa.

### AUD-03 — Validación del área de objetos adheridos

**Observación histórica:** la auditoría inicial encontró una construcción `ValueError(...)` sin `raise` en `Modelo/calculoRT2.py::agregar_areas_materiales`.

**Estado:** **CORREGIDO**. El código inspeccionado contiene `raise ValueError(...)`. `CHANGELOG.md` registra la corrección del 2026-09-13 y la comprobación de un caso inválido, además de una comparación de regresión del caso de referencia.

**Acción:** conservar una prueba automatizada para el caso límite cuando se implemente la suite; no volver a registrar este punto como bug abierto.

### AUD-04 — Función alternativa de absorción

**Observación:** `calcular_absorcion_total` contiene lógica que requiere compararse con `calcular_absorcion`, función usada en el flujo descrito del motor principal. La auditoría inicial observó cálculos intermedios y sumas que podrían no tener el mismo tratamiento de áreas/cantidades.

**Estado:** **PENDIENTE DE ANÁLISIS FUNCIONAL**. No hay base suficiente en esta revisión para declararla defectuosa ni para eliminarla.

**Acción:** localizar todos sus consumidores, construir casos comparativos y documentar si es una ruta activa, alternativa o legacy.

### AUD-05 — Mensajes de diagnóstico

**Observación:** se encuentran instrucciones `print()` en código de carga y procesamiento, por ejemplo en `Modelo/excel.py` y en funciones del modelo.

**Estado:** deuda técnica observada; no bloquea por sí sola la ejecución.

**Acción:** migrar gradualmente a logging con niveles adecuados, preservando información de error. Evitar una limpieza masiva que oculte fallos o cambie el comportamiento.

### AUD-06 — Dependencias y entorno

**Observación histórica:** la auditoría inicial no tenía una especificación formal de dependencias.

**Estado:** **FORMALIZADO**. Existe `requirements.txt`; `DEPENDENCIES.md` documenta PySide6, pandas, openpyxl, matplotlib y reportlab, además de un entorno probado en Linux/SteamOS (Python 3.13.15 y versiones fijadas). PyQt5 queda asociado al archivo legacy `prueba.py`, no a la aplicación principal.

**Pendiente:** instalación limpia y compatibilidad Windows POR VALIDAR.

### AUD-07 — Pruebas automatizadas

**Observación:** `TESTING.md` indica que no existe una suite automatizada consolidada y define procedimientos manuales de smoke test, integración, regresión y PDF.

**Estado:** pendiente de automatización y de ejecución reciente de la matriz completa. Los registros históricos de smoke tests y regresión son evidencia de sesiones concretas, no sustituyen una suite repetible en CI.

**Acción:** crear pruebas unitarias para geometría, áreas, absorción, Sabine, Eyring, Dc, %ALCons y D-019; añadir integración de M1/M2/M3 y generación PDF. Seguir `SOFTWARE_VALIDATION.md`.

### AUD-08 — Rutas de recursos

**Observación histórica:** existen rutas relativas de recursos y se registró una ruta GIF potencialmente incorrecta en pantallas de Base de Datos.

**Estado:** pendiente de comprobación integral en el estado actual. La ejecución desde `Vista/` forma parte del procedimiento documentado en `DEPENDENCIES.md`; no se ha demostrado independencia total del directorio de trabajo.

**Acción:** inventariar rutas, probar arranque desde el directorio previsto y desde otros directorios, y corregir solo con pruebas asociadas.

### AUD-09 — Trazabilidad de datos y coeficientes acústicos

**Observación:** los perfiles de aula se almacenan como diccionarios Python y los coeficientes se cargan desde libros Excel. El flujo principal inspeccionado utiliza `Datos/coefs_absorcion.xlsx`.

**Estado:** inventario y riesgos documentados en `ACOUSTIC_DATA_CATALOG.md`; la procedencia primaria de dimensiones, materiales y coeficientes continúa pendiente.

**Acción:** no cambiar coeficientes ni normalizar nombres de materiales hasta recuperar fuentes y confirmar correspondencias.

## 4. Prioridades resultantes

| Prioridad | Trabajo | Documento rector |
|---|---|---|
| P0 | Resolver trazabilidad de datos y coeficientes | `ACOUSTIC_DATA_CATALOG.md` |
| P0 | Completar revisión bibliográfica primaria de Peutz, Dc y R | `ACOUSTIC_MODEL.md`, `ACADEMIC_ALIGNMENT.md` |
| P1 | Automatizar pruebas de caracterización | `TESTING.md`, `SOFTWARE_VALIDATION.md` |
| P1 | Auditar función alternativa de absorción y módulos legacy | Este documento |
| P1 | Verificar rutas de recursos y carga de datos | `DEPENDENCIES.md`, `TESTING.md` |
| P2 | Migrar diagnósticos a logging | Este documento |
| P2 | Validar instalación en Windows | `DEPENDENCIES.md` |

## 5. Regla de mantenimiento

Al resolver un hallazgo:
1. conservar la descripción histórica;
2. registrar fecha, archivos y commit que contienen el cambio;
3. aportar la prueba ejecutada y su resultado;
4. cambiar el estado a CORREGIDO solo con evidencia;
5. actualizar `CURRENT_STATE.md` e `INDEX.md` si cambia una prioridad.

No convertir recomendaciones antiguas en tareas activas sin volver a inspeccionar el código de la rama sobre la que se trabajará.
