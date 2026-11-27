# Catálogo de datos acústicos — Bloque H

**Proyecto:** Room Acoustic  
**Fuente primaria en el software:** Datos/salones.py  
**Revisión:** rama docs/knowledge-base-2026-11, 2026-11-27  
**Estado:** inventario de configuración implementada. No certifica el levantamiento físico ni constituye validación experimental.

## 1. Propósito y alcance

Describe los 23 perfiles operativos que alimentan M3, su estructura y su recorrido hacia el motor de reverberación. No duplica las ecuaciones ni la especificación de módulos. El inventario se limita a salonTipo1–salonTipo23 y a la lista salones construida por obtener_salones(...); los diccionarios de ejemplo y variables auxiliares del mismo archivo no forman parte de esa lista.

## 2. Esquema de datos

| Campo | Contenido | Aplicación |
|---|---|---|
| Tipo | Identificador textual del perfil | Identificación |
| aulas | Código o rango de aulas | Identificación |
| dimensiones | largo, ancho, altura | Geometría |
| materiales | Material base por superficie | Absorción |
| objetos_adheridos | Nombre, material y área, asociados a una superficie | Área remanente y absorción propia |
| objetos_adicionales | Nombre, material y cantidad | Absorción por cantidad |
| inteligibilidad | Distancia y coeficiente medio de absorción | Parámetros iniciales del análisis opcional |

Las seis superficies geométricas reconocidas son Frontal, Trasera, Izquierda, Derecha, Piso y Techo.

**Unidades:** las magnitudes son compatibles con metros y metros cuadrados según las operaciones del modelo y el formato de los reportes, pero el diccionario no declara unidades ni metadatos de medición. Confirmar la unidad contra la fuente primaria antes de afirmarla como dato metrológico en la tesis.

## 3. Inventario de los 23 perfiles

Dimensiones en orden largo × ancho × altura. La cantidad de sillas se transcribe del campo cantidad; no equivale a aforo certificado.

| Tipo | Aulas | Dimensiones | Sillas | Coef. medio |
|---:|---|---:|---:|---:|
| 1 | 101–104 | 9,94 × 5,87 × 3,67 | 42 | 0,24 |
| 2 | 105–106 | 9,57 × 5,88 × 2,52 | 30 | 0,24 |
| 3 | 201–206 | 9,97 × 5,85 × 3,52 | 45 | 0,24 |
| 4 | 209–210 | 13,11 × 5,68 × 2,70 | 45 | 0,25 |
| 5 | 211–214 | 6,99 × 4,81 × 2,69 | 30 | 0,25 |
| 6 | 215–216 y 315–316 | 7,25 × 4,77 × 2,67 | 25 | 0,25 |
| 7 | 217–218 y 317–319 | 7,89 × 5,68 × 2,68 | 25 | 0,25 |
| 8 | 219 y 314 | 7,89 × 5,68 × 3,65 | 25 | 0,22 |
| 9 | 301–306 | 9,97 × 5,85 × 3,52 | 25 | 0,22 |
| 10 | 309 | 13,12 × 5,88 × 2,84 | 25 | 0,25 |
| 11 | 310 | 11,59 × 5,62 × 2,63 | 36 | 0,25 |
| 12 | 311–313 | 6,97 × 4,86 × 2,63 | 36 | 0,25 |
| 13 | 401 y 404 | 6,91 × 5,06 × 3,64 | 37 | 0,25 |
| 14 | 402 y 403 | 8,85 × 4,74 × 3,68 | 37 | 0,22 |
| 15 | 405 y 408 | 7,25 × 5,02 × 3,52 | 20 | 0,20 |
| 16 | 406–407 | 8,79 × 4,71 × 3,65 | 20 | 0,22 |
| 17 | 411 | 13,11 × 5,16 × 2,67 | 20 | 0,25 |
| 18 | 501* | 7,01 × 5,03 × 2,84 | 20 | 0,25 |
| 19 | 502–504 | 8,82 × 4,68 × 2,84 | 25 | 0,25 |
| 20 | 505–507 | 5,48 × 9,96 × 2,80 | 30 | 0,25 |
| 21 | 513–514 | 8,06 × 5,86 × 2,67 | 25 | 0,25 |
| 22 | 515 | 8,06 × 5,88 × 2,68 | 24 | 0,25 |
| 23 | 517–520 | 4,89 × 7,03 × 2,66 | 15 | 0,25 |

*En salonTipo18 la clave es aula (singular), mientras los demás perfiles usan aulas. Es una inconsistencia de esquema por revisar en todos los consumidores antes de corregirla.*

## 4. Materiales y objetos

- En los tipos 1–3 predominan paredes de Revoque rugoso; desde el tipo 4 predomina Revoque de cal y arena.
- El piso se registra generalmente como Hormigón rasado o monolítico.
- Los techos varían entre Hormigón rústico, Hormigón Normal y Cielorraso de placas de yeso 13 mm + espacio aire.
- Los objetos adheridos incluyen puertas, ventanas y tableros. Sus áreas se conservan por perfil; no deben sustituirse por valores genéricos.
- Los objetos adicionales son habitualmente sillas y una mesa. Las sillas del tipo 17 usan Escritorios de madera y metal; los demás perfiles emplean principalmente Butaca bien tapizada. Las mesas usan Madera compensada sin cámara.

Las denominaciones se transcriben sin normalización para no alterar la asociación exacta con las etiquetas de coeficientes.

## 5. Flujo de procesamiento

1. Datos/salones.py define los perfiles y construye salones.
2. M3 permite seleccionar un perfil.
3. El diccionario pasa por Controlador/controlTR.py::procesar_datos.
4. Modelo/calculoRT2.py calcula las áreas de las seis superficies.
5. agregar_areas_materiales descuenta de cada superficie las áreas de objetos adheridos y valida que no excedan el área geométrica.
6. calcular_absorcion suma por banda la contribución de la superficie restante, los objetos adheridos y los objetos adicionales.
7. Sabine y Eyring producen los resultados RT, presentados mediante el flujo compartido de M1 y exportables a PDF.

La formulación y las salidas se describen en MODULES_SPECIFICATION.md y ACOUSTIC_MODEL.md.

## 6. Libros de coeficientes

En el repositorio existen Datos/coefs_absorcion.xlsx, Datos/coefs_absorcion_basic.xlsx y Datos/coeficientes.xlsx. Modelo/excel.py define cargar_coeficientes_dos() con ruta a coefs_absorcion.xlsx. Controlador/Controlador.py construye desde ese DataFrame el diccionario de coeficientes por material y por las bandas 125, 250, 500, 1000, 2000 y 4000 Hz. También carga coeficientes.xlsx mediante cargar_coeficientes(), pero el controlador inspeccionado no utiliza ese DataFrame para construir el diccionario que consume el motor principal.

No se transcriben aquí coeficientes ni se les atribuye fuente bibliográfica: la inspección documental no confirmó la procedencia de cada valor ni su correspondencia completa con una referencia primaria. Queda pendiente:
- identificar autor, título, edición/año y página/tabla de cada coeficiente;
- confirmar coincidencia exacta entre nombres de materiales y etiquetas del libro activo;
- documentar unidades y condiciones de ensayo;
- clasificar coefs_absorcion_basic.xlsx como activo, alternativo o histórico.

## 7. Hallazgos de consistencia

| ID | Hallazgo | Riesgo/acción |
|---|---|---|
| DAT-01 | Tipo 18 usa aula en vez de aulas | Revisar consumidores y definir corrección compatible |
| DAT-02 | El archivo contiene ejemplos y estructuras anteriores a los perfiles operativos | Identificar dependencias antes de retirar o reorganizar |
| DAT-03 | Hay tres libros Excel relacionados con coeficientes | Determinar propósito y vigencia de cada uno |
| DAT-04 | Los perfiles no incluyen fuente, fecha de levantamiento, instrumento ni responsable | Recuperar registros primarios para trazabilidad |
| DAT-05 | Los nombres de materiales pueden variar | Auditar correspondencia exacta antes de normalizar |

Son hallazgos de inspección estática, no prueba de fallos en todos los casos.

## 8. Condiciones para validar el catálogo

Se requiere: (1) plano o ficha de levantamiento que respalde dimensiones y asignación de aulas; (2) evidencia de materiales y elementos adheridos; (3) fuente verificable de coeficientes por banda; (4) criterio de ocupación y mobiliario; (5) unidades y precisión de medición; (6) revisión de rangos, duplicados, áreas y claves; y (7) aprobación del responsable del levantamiento y del equipo académico.

Hasta completar estas condiciones, el estado correcto es **catálogo de configuración implementada con procedencia física y bibliográfica pendiente de trazabilidad**.

## 9. Documentos relacionados

- MODULES_SPECIFICATION.md
- ACOUSTIC_MODEL.md
- TESTING.md
- ACADEMIC_ALIGNMENT.md
