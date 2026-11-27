# Especificación funcional y técnica de módulos

**Proyecto:** Room Acoustic  
**Base de inspección:** rama `master`, commit `89417063de9e3053a4cc05739bc7eeda3fc8900e`  
**Fecha de elaboración:** 2026-11-27  
**Estado:** especificación inicial basada en inspección estática del código y documentación del repositorio. No sustituye pruebas de ejecución ni validación académica.

> **Criterio de lectura:** se distingue entre comportamiento observado en código, información descrita por la documentación y aspectos pendientes de confirmar. Una función presente en el repositorio no se considera automáticamente validada en todos sus casos de uso.

## 1. Visión general

Room Acoustic es una aplicación de escritorio desarrollada en Python y PySide6 para apoyar la evaluación de condiciones acústicas de aulas. La aplicación reúne tres módulos funcionales:

1. **M1 — Tiempo de Reverberación:** registra geometría, superficies, materiales y objetos; calcula RT60 mediante Sabine y Eyring; presenta resultados y permite generar un reporte PDF.
2. **M2 — Inteligibilidad del Habla:** calcula el porcentaje de pérdida de articulación de consonantes (%ALCons) mediante la implementación del modelo de Peutz y presenta su interpretación.
3. **M3 — Base de Datos:** permite seleccionar aulas caracterizadas del Bloque H y someter sus datos al flujo de análisis de reverberación.

La aplicación también incluye Inicio, navegación, una pantalla de Ayuda y componentes compartidos para resultados y reportes.

## 2. Mapa de módulos

| Módulo | Entrada principal | Procesamiento | Salida principal | Implementación identificada |
|---|---|---|---|---|
| M1 — Tiempo de Reverberación | Dimensiones, materiales, superficies, objetos adheridos y adicionales | Áreas, absorción por banda, RT60 Sabine/Eyring y evaluación | Resultados, gráfico y PDF | `Vista/ventTiempoReverberacion.py`, `Controlador/controlTR.py`, `Modelo/calculoRT2.py` |
| M2 — Inteligibilidad | Distancia, TR a 2000 Hz, volumen, directividad, superficie y absorción media | Constante del recinto, distancia crítica, %ALCons y clasificación | Resultado de inteligibilidad y PDF | `Vista/ventInteligibilidad.py`, `Vista/ventResultadosInteligibilidad.py`, `Modelo/alcons2.py` |
| M3 — Base de Datos | Aula seleccionada del catálogo del Bloque H | Reutiliza el procesamiento de reverberación | Pantalla de resultados RT y reporte | `Vista/ventInfoBD.py`, `Datos/salones.py`, `Controlador/controlTR.py` |
| Ayuda | Selección de tema | Presentación de guías y flujos explicativos | Contenido de ayuda | `Vista/ventAyuda.py` |

Los tres módulos analíticos no son tres motores matemáticos independientes: M3 reutiliza el procesamiento de M1. La Ayuda describe los flujos, pero no sustituye la especificación técnica ni las validaciones de cada módulo.

## 3. M1 — Tiempo de Reverberación

### 3.1 Propósito

Estimar el tiempo de reverberación del recinto por bandas de frecuencia y comparar los resultados obtenidos mediante los métodos de Sabine y Eyring.

### 3.2 Entradas

El formulario de `VentanaTiempoReverberacion` permite construir los datos del recinto. La estructura de datos procesada incluye:

- **Dimensiones:** largo, ancho y altura.
- **Superficies:** frontal, trasera, izquierda, derecha, piso y techo.
- **Material base:** material asociado a cada superficie.
- **Objetos adheridos:** elementos asignados a una superficie, con nombre, material y área.
- **Objetos adicionales:** elementos sueltos con material y cantidad.
- **Opción de inteligibilidad:** el formulario contempla una opción para incorporar el análisis de inteligibilidad al flujo de resultados.

Los nombres de las claves del diccionario son parte del contrato interno de datos. No deben cambiarse sin rastrear todas sus referencias.

### 3.3 Procesamiento geométrico

En `Modelo/calculoRT2.py`, `calcular_areas_basicas(largo, ancho, altura)` calcula las áreas geométricas de un recinto rectangular:

| Superficie | Área |
|---|---:|
| Frontal | ancho × altura |
| Trasera | ancho × altura |
| Izquierda | largo × altura |
| Derecha | largo × altura |
| Piso | largo × ancho |
| Techo | largo × ancho |

La función `agregar_areas_materiales(datos)` toma esas áreas, suma el área de los objetos adheridos de cada superficie, valida que dicha suma no exceda el área geométrica y guarda en `materiales[zona]["area"]` el área restante.

**Importante:** el cálculo de absorción posterior también suma la absorción de los objetos adheridos. Por ello, el área restante de la superficie y el área de los objetos se contabilizan por separado, evitando tratar el área ocupada como si desapareciera acústicamente.

### 3.4 Absorción acústica

La función principal observada es `calcular_absorcion(salon, coeficientes, frecuencias=None)`.

Para cada frecuencia, inicializa una absorción total y acumula contribuciones de:

1. Material base de cada superficie: área aplicada × coeficiente de absorción.
2. Objetos adheridos: área del objeto × coeficiente del material del objeto.
3. Objetos adicionales: cantidad × coeficiente del material.

La función devuelve:
- `absorcion_total`: diccionario de absorción total por frecuencia.
- `detalles`: lista de registros con zona, tipo de elemento, material, frecuencia, área/cantidad, coeficiente y absorción calculada.

Las bandas predeterminadas observadas son **125, 250, 500, 1000, 2000 y 4000 Hz**. Los coeficientes se obtienen desde los datos tabulares cargados por el controlador.

### 3.5 Cálculo de RT60

**Sabine**

La implementación observada en `calcular_rt60_sabine` utiliza:

```
RT60 = 0.161 × V / A
```

donde V es el volumen del recinto y A es la absorción total para la frecuencia evaluada.

Si la absorción es cero o no positiva, el método devuelve el texto `"Infinito"` para esa frecuencia.

**Eyring**

La implementación observada en `calcular_rt60_eyring` utiliza:

```
α_prom = A / S
RT60 = -0.161 × V / (S × ln(1 - α_prom))
```

donde S corresponde al área total de las superficies y α_prom al coeficiente medio de absorción de la banda.

Si A no es positivo o el argumento del logaritmo no pertenece al dominio utilizado por el código, devuelve `"Infinito"`.

> Las expresiones y constantes aquí transcritas describen el código inspeccionado. La aprobación académica de fórmulas, unidades, hipótesis y redondeos debe mantenerse vinculada a `ACOUSTIC_MODEL.md` y al documento de grado vigente.

### 3.6 Resultados e interfaz

La clase `VentanaGraficaRT` presenta la salida del análisis. La documentación de interfaz describe como elementos del resultado:

- comparación gráfica Sabine/Eyring;
- tabla de resultados por banda;
- tiempo de reverberación medio (`Tr MID`);
- veredicto de condición óptima/no óptima;
- bloque independiente de inteligibilidad cuando el análisis se incluye.

El gráfico se construye con Matplotlib y se integra en la interfaz. La vista de resultados también ofrece la generación del reporte PDF.

### 3.7 Reporte PDF

La clase `ReportePDF` en `Datos/utils/reportePDF.py` contiene el método `reporte_tiempo_reverberacion(self, resultados)`. Según `REPORTS.md`, el reporte estándar organiza la ficha del salón, resultados RT60 y análisis acústico; incluye la evaluación de inteligibilidad cuando se encuentra disponible en los resultados.

La documentación registra feedback de éxito/error al guardar el PDF (D-017). El detalle visual y de paginación se mantiene en `REPORTS.md`.

### 3.8 Archivos principales y responsabilidades

| Archivo | Responsabilidad |
|---|---|
| `Vista/ventTiempoReverberacion.py` | Formulario, configuración de materiales, interacción y construcción de datos |
| `Vista/manejadorObjetos.py` | Gestión de objetos adheridos a superficies |
| `Vista/manejadorObjetoAdicional.py` | Gestión de objetos adicionales |
| `Controlador/controlTR.py` | Función `procesar_datos`, que delega el diccionario a `calcular_resultados` |
| `Controlador/Controlador.py` | Obtención de lista de materiales y coeficientes |
| `Modelo/calculoRT2.py` | Geometría, absorción, cálculos RT y ensamblaje de resultados |
| `Vista/ventGraficaRT.py` | Presentación de resultados, gráfico y acciones de salida |
| `Datos/utils/reportePDF.py` | Construcción de reportes PDF |

### 3.9 Validaciones y pruebas conocidas

La documentación del proyecto registra validaciones de dimensiones, áreas de objetos adheridos, coeficientes y campos obligatorios. El detalle normativo debe contrastarse con el Word vigente y con los validadores actuales del formulario.

Pruebas manuales documentadas en `TESTING.md` incluyen flujo M1 con y sin inteligibilidad, navegación, guardado/cancelación de PDF, comparación de resultados numéricos y casos de salones de la base de datos.

**Pendiente:** convertir las verificaciones manuales en pruebas automatizadas reproducibles y mantener casos de referencia con entradas, resultados esperados, tolerancias y fuente.

## 4. M2 — Inteligibilidad del Habla

### 4.1 Propósito

Estimar la pérdida de articulación de consonantes (%ALCons) como indicador de inteligibilidad de la palabra en el recinto, a partir de parámetros acústicos y geométricos.

### 4.2 Entradas identificadas

La interfaz `VentanaInteligibiliad` y el modelo `AlconsCalculator` trabajan con:

- distancia emisor–oyente (`distancia`);
- tiempo de reverberación a 2000 Hz (`tr_2000Hz`);
- volumen del recinto (`volumen_sala`);
- factor de directividad (`factor_directividad`);
- superficie total (`superficie_total`);
- coeficiente medio de absorción (`coef_medio_absor`).

La documentación del proyecto identifica Q = 2 como valor de referencia para voz humana frontal y 1.5 m como distancia de referencia del proyecto. La configuración exacta y posibilidad de edición deben verificarse en la interfaz y en el documento académico antes de describirlas como constantes invariables.

### 4.3 Procesamiento implementado

La clase `AlconsCalculator` de `Modelo/alcons2.py` contiene los métodos siguientes:

**Constante del recinto**

```
R = (S × α_prom) / (1 - α_prom)
```

La función `calcular_constante_recinto(superficie_total, coef_medio_absor)` rechaza el caso de coeficiente medio igual a 1.

**Distancia crítica utilizada por el reporte**

```
Dc = 0.21 × √(V / TR_2000Hz)
```

Se calcula mediante `calcular_dc(volumen, tr_2000Hz)`, que exige volumen y TR positivos.

**Otra expresión disponible**

```
Dc_alternativa = 0.14 × √(Q × R)
```

Está implementada en `calcular_distancia_critica(factor_directividad, constante_recinto)`. En el método `generar_reporte` la llamada a esta alternativa está comentada y se utiliza `calcular_dc`. Por tanto, no deben presentarse ambas como simultáneamente utilizadas.

**Cálculo de %ALCons**

```
Si r ≤ 3.16 × Dc:
    %ALCons = (200 × r² × TR²) / (V × Q)
Si r > 3.16 × Dc:
    %ALCons = 9 × TR
```

La función `calcular_alcons` devuelve el valor redondeado a dos decimales y valida que distancia, TR, volumen y factor de directividad sean positivos. El umbral de transición de 3.16 × Dc fue confirmado como criterio de implementación en D-020 (2026-11-27); el código ya aplicaba ese valor.

### 4.4 Clasificación cualitativa D-019

La función `evaluar_alcons` implementa la clasificación operativa de seis niveles aprobada en D-019:

| Intervalo | Categoría |
|---|---|
| 0 ≤ x ≤ 1.4 | Excelente |
| 1.4 < x ≤ 4.8 | Buena |
| 4.8 < x ≤ 11.4 | Regular |
| 11.4 < x ≤ 24.2 | Pobre |
| 24.2 < x ≤ 46.5 | Mala |
| x > 46.5 | Crítico |

La escala continua de seis niveles es una decisión operativa del proyecto basada en los límites superiores de la tabla bibliográfica analizada. No debe atribuirse literalmente a la fuente como si esta publicara seis categorías continuas. La justificación y comparación están en `ALCONS_CLASSIFICATION_REVIEW.md`; la decisión está en `DECISIONS.md`.

### 4.5 Presentación y reporte

La interfaz se implementa en `Vista/ventInteligibilidad.py`, con una pantalla de resultados propia en `Vista/ventResultadosInteligibilidad.py`. La clasificación visual del formulario se genera a partir de la constante compartida `NIVELES_ALCONS` del módulo de reportes, evitando duplicar umbrales.

El reporte independiente se genera mediante `ReportePDF.reporte_inteligibiliad(self, reporte)` (se conserva la grafía histórica del método). La documentación de reportes indica que el formato independiente estándar ocupa una página.

### 4.6 Archivos principales

| Archivo | Responsabilidad |
|---|---|
| `Vista/ventInteligibilidad.py` | Formulario, validación de entradas y coordinación del análisis |
| `Vista/ventResultadosInteligibilidad.py` | Presentación de resultados de M2 |
| `Modelo/alcons2.py` | Constante del recinto, distancias críticas, cálculo y evaluación |
| `Datos/utils/reportePDF.py` | Escala común y reporte PDF de inteligibilidad |

### 4.7 Validaciones y pruebas conocidas

El modelo valida parámetros positivos y rechaza coeficiente medio de absorción igual a 1 al calcular R. La función `generar_reporte` captura `ValueError` y devuelve un diccionario con clave `"Error"`.

La documentación registra pruebas de límites D-019, coherencia entre clasificación del modelo y PDF y verificación de que la implementación de clasificación no alteró los valores numéricos de %ALCons de los 23 salones.

**Pendiente:** ampliar pruebas automatizadas del cálculo de Peutz, especialmente transiciones alrededor de `r = 3.16 × Dc`, dominios extremos y tratamiento de errores que llegan a la interfaz.

## 5. M3 — Base de Datos del Bloque H

### 5.1 Propósito

Permitir seleccionar un aula previamente caracterizada del Bloque H y ejecutar su análisis acústico con los datos registrados, evitando volver a introducir manualmente las características del recinto.

### 5.2 Fuente de datos

La fuente identificada en el repositorio es `Datos/salones.py`, que contiene la colección `salones` y estructuras de diccionarios para los **23 tipos de salón**.

La documentación del proyecto describe que la base contiene dimensiones, materiales y objetos asociados a las aulas. Los coeficientes de absorción se obtienen de los archivos Excel utilizados por el sistema.

La estructura exacta de cada ficha debe considerarse contrato de datos. Las claves opcionales, por ejemplo `Tipo` o `aulas`, pueden afectar la presentación y el reporte.

### 5.3 Flujo de operación

1. El usuario abre el módulo Base de Datos desde la navegación de análisis.
2. Selecciona un aula de la colección `salones`.
3. La vista obtiene el diccionario correspondiente.
4. La vista delega el procesamiento en `procesar_datos`, del controlador compartido de RT.
5. El modelo calcula absorción y RT60 con el mismo motor `calculoRT2`.
6. El flujo navega a `VentanaGraficaRT` para mostrar resultados y permitir el reporte.

La reutilización de la pantalla de resultados RT es intencional: M3 utiliza el mismo análisis de reverberación, con datos precargados del aula.

### 5.4 Archivos principales

| Archivo | Responsabilidad |
|---|---|
| `Datos/salones.py` | Catálogo de aulas y sus características |
| `Vista/ventInfoBD.py` | Selección y presentación de la información del aula |
| `Controlador/controlTR.py` | Delegación al motor de cálculo RT |
| `Modelo/calculoRT2.py` | Cálculos de absorción y RT60 |
| `Vista/ventGraficaRT.py` | Presentación compartida de resultados |
| `Datos/utils/reportePDF.py` | Reporte del análisis |

### 5.5 Validación y pruebas conocidas

`TESTING.md` documenta una verificación de los 23 salones comparando resultados de Sabine, Eyring, %ALCons numérico y distancia crítica con una versión anterior del código. También contempla generar PDF para cada salón y comprobar que los datos de identificación se presenten cuando existen.

**Pendiente de auditoría:** comprobar de forma sistemática la integridad del esquema de los 23 diccionarios (claves requeridas, claves opcionales, unidades, materiales existentes en Excel y consistencia entre superficies y objetos). La existencia de 23 entradas no demuestra por sí sola la validez acústica de todos sus datos.

## 6. Componentes compartidos

### 6.1 Controlador de reverberación

`Controlador/controlTR.py` expone `procesar_datos(diccionario)`, que delega el cálculo a `Modelo.calculoRT2.calcular_resultados`. Es utilizado tanto por el formulario M1 como por M3.

### 6.2 Datos de materiales y coeficientes

`Controlador/Controlador.py` proporciona funciones para obtener la lista de materiales y los coeficientes desde los libros Excel. Los archivos de datos y la estructura de columnas deben mantenerse documentados en el catálogo de datos, incluyendo unidades, bandas y procedencia.

### 6.3 Reportes

`Datos/utils/reportePDF.py` centraliza el diseño y la generación de reportes con ReportLab. `REPORTS.md` es la referencia específica para páginas, estructura, encabezados, pies, tablas, paginación y escala de inteligibilidad.

### 6.4 Ayuda

`Vista/ventAyuda.py` implementa la Ayuda V1 en Python/PySide6. La documentación de `UI_INVENTORY.md` registra sus seis secciones, navegación, stepper y componentes de flujo. La Ayuda es contenido orientativo de usuario, no un manual académico exhaustivo.

## 7. Flujo general de datos

```text
M1: Formulario
    └── dimensiones + superficies + materiales + objetos
          └── Controlador.controlTR.procesar_datos
                └── Modelo.calculoRT2.calcular_resultados
                      ├── áreas y absorción por banda
                      ├── RT60 Sabine
                      ├── RT60 Eyring
                      └── resultados y detalles
                            └── VentanaGraficaRT
                                  ├── tabla / gráfico / interpretación
                                  └── ReportePDF

M2: Formulario de inteligibilidad
    └── parámetros acústicos y geométricos
          └── Modelo.alcons2.AlconsCalculator
                ├── constante del recinto
                ├── distancia crítica utilizada
                ├── %ALCons
                └── clasificación D-019
                      ├── VentanaResultadosInteligibilidad
                      └── ReportePDF

M3: Selección de aula
    └── Datos.salones.salones
          └── Controlador.controlTR.procesar_datos
                └── mismo motor de M1
                      └── VentanaGraficaRT / ReportePDF
```

El diagrama representa las dependencias principales observadas; no sustituye un diagrama de secuencia completo ni documenta cada señal/slot de Qt.

## 8. Estado de implementación frente a validación

| Área | Implementación observada/documentada | Validación que aún debe distinguirse |
|---|---|---|
| M1 — Sabine/Eyring | Implementado en el motor RT | Validación académica contra mediciones o casos de referencia |
| M1 — formulario y resultados | Flujo funcional documentado | Pruebas automatizadas de validadores y navegación |
| M2 — Peutz/%ALCons | Implementado en `alcons2.py` | Validación académica independiente de la clasificación |
| M2 — D-019 | Implementada y compartida por modelo/UI/PDF | Aprobación de redacción académica definitiva |
| M3 — 23 aulas | Catálogo y flujo de análisis implementados | Auditoría de integridad y validez de los datos fuente |
| PDF | Generación implementada y documentada | Regresión automatizada de contenido y geometría de páginas |
| Ayuda V1 | Implementada y documentada | Refinamiento visual y ampliación de contenido |
| Pruebas | Procedimientos manuales reproducibles documentados | Suite automatizada y ejecución continua |

## 9. Riesgos y asuntos que no deben ocultarse

1. **Documentación desactualizada:** `CURRENT_STATE.md` contiene secciones históricas que contradicen el estado posterior registrado en `HANDOFF.md`, `CHANGELOG.md` y `UI_INVENTORY.md`. Debe reconciliarse sin borrar el historial.
2. **Pruebas automatizadas:** `TESTING.md` señala que no existe una suite automatizada consolidada en el snapshot documentado.
3. **Implementaciones alternativas/legacy:** existen archivos alternativos de cálculo RT y %ALCons. No deben eliminarse sin análisis de referencias y equivalencia.
4. **Datos de aulas:** debe verificarse la integridad del esquema y de los coeficientes asociados.
5. **Dominios extremos:** los métodos RT pueden devolver el texto `"Infinito"`; las funciones consumidoras deben manejar de forma coherente resultados numéricos y no numéricos.
6. **Validación académica:** la implementación y la clasificación operativa no equivalen por sí solas a validación experimental o aprobación final de la tesis.

Estos puntos son riesgos documentales/técnicos que requieren tareas específicas; esta especificación no autoriza cambios en fórmulas, datos ni arquitectura.

## 10. Documentos relacionados

- `PROJECT_CONTEXT.md` — identidad, alcance y contexto.
- `CURRENT_STATE.md` — estado consolidado que debe mantenerse actualizado.
- `ARCHITECTURE.md` — estructura y responsabilidades técnicas.
- `ACOUSTIC_MODEL.md` — modelo matemático.
- `REQUIREMENTS.md` — requisitos funcionales y no funcionales.
- `ALCONS_CLASSIFICATION_REVIEW.md` — fundamento y límites de D-019.
- `DECISIONS.md` — decisiones de diseño y metodología.
- `UI_INVENTORY.md` — inventario de pantallas y componentes.
- `REPORTS.md` — diseño y comportamiento de reportes PDF.
- `RESOURCES.md` — recursos gráficos y estilos.
- `TESTING.md` — estrategia y verificaciones conocidas.
- `INTEGRATION.md` — impacto del software en el documento académico.
- `DEVELOPMENT_HISTORY.md` — cronología de evolución del proyecto.
- `ACADEMIC_ALIGNMENT.md` — trazabilidad entre documento de grado e implementación.

## 11. Próxima actualización requerida

Esta especificación debe actualizarse cuando cambie una de estas áreas: entradas, estructura de datos, fórmulas, parámetros, validaciones, navegación, presentación de resultados, reportes o pruebas.

Cada actualización debe indicar:
- fecha y commit inspeccionado;
- archivos de código revisados;
- comportamiento modificado;
- pruebas ejecutadas y resultado;
- impacto sobre `ACOUSTIC_MODEL.md`, `REQUIREMENTS.md` y documento académico;
- aspectos que continúan POR VALIDAR.
