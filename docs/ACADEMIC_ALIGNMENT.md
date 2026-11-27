# Alineación entre el documento académico y Room Acoustic

## 1. Propósito y fuentes revisadas

Este documento registra la relación entre el Word académico suministrado como `proyectoGradoSoftware.docx` y la documentación/código del repositorio `Dramos18/room_acoustic`.

Fuentes consideradas:

- Documento Word de trabajo de grado, 57 páginas.
- `CLAUDE.md` y `AI_RULES.md`.
- `docs/PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `ACOUSTIC_MODEL.md`, `REQUIREMENTS.md`, `DEPENDENCIES.md`, `REPORTS.md`, `UI_INVENTORY.md`, `DECISIONS.md`, `CHANGELOG.md`, `HANDOFF.md`, `TESTING.md` y `ALCONS_CLASSIFICATION_REVIEW.md`.

**Corte de revisión:** 2026-11-27.  
**Importante:** esta es una revisión de trazabilidad documental, no una aprobación académica del contenido ni una validación independiente de las ecuaciones.

## 2. Base académica identificada en el Word

El Word presenta el proyecto bajo el título:

> Software para evaluar la acústica en aulas: tiempo de reverberación e inteligibilidad de la palabra.

Identifica como contexto institucional a la Universidad del Atlántico, Facultad de Ingeniería, Programa de Ingeniería Industrial, y como escenario de aplicación las aulas del Bloque H.

### 2.1 Problema y alcance

El documento plantea la necesidad de una herramienta computacional accesible para evaluar parámetros acústicos de aulas, especialmente tiempo de reverberación e inteligibilidad de la palabra. Delimita el alcance a recintos cerrados de uso educativo y describe el ingreso manual de información, sin integración automática de sensores.

La base de datos de 23 tipos de aulas del Bloque H aparece como alcance específico, con posibilidad de introducir manualmente datos de otros recintos.

### 2.2 Objetivo general y objetivos específicos transcritos como base

**Objetivo general del Word:**

“Desarrollar un software especializado para evaluar la acústica en aulas de clase, mediante el análisis del tiempo de reverberación y la inteligibilidad del habla, con el fin de proporcionar datos precisos que permitan optimizar las condiciones acústicas en entornos educativos.”

**Objetivos específicos del Word:**

1. Desarrollar algoritmos de cálculo acústico para determinar el tiempo de reverberación y la inteligibilidad de la palabra.
2. Diseñar una interfaz de usuario intuitiva, amigable y accesible que permita ingresar datos de las aulas y visualizar los resultados de las evaluaciones acústicas de manera clara y comprensible.
3. Validar el software mediante mediciones reales y generar un informe técnico sobre su usabilidad y precisión.
4. Permitir la personalización del análisis acústico, ajustando parámetros, modelos de cálculo y formatos de salida.

Estos objetivos se conservan como formulación del documento académico. El estado de cumplimiento de cada uno debe demostrarse con evidencia específica; no se presume por la mera existencia de una función.

### 2.3 Metodología descrita

El Word caracteriza el trabajo como investigación aplicada y tecnológica, con enfoque cuantitativo. Describe un desarrollo iterativo que se alinea con principios ágiles, organizado en cinco fases:

1. Análisis.
2. Diseño.
3. Implementación.
4. Prueba.
5. Implementación final.

También menciona el método I.D.E.A.L. como guía conceptual y una arquitectura MVC ampliada con capas de datos y recursos, denominada MVC+S en el capítulo de resultados.

## 3. Correspondencia entre el Word y el software documentado

| Tema | Word académico | Estado técnico documentado | Acción antes de actualizar la tesis |
|---|---|---|---|
| Tiempo de reverberación | Sabine y Eyring | M1 implementa ambos modelos por bandas | Actualizar descripción, pantallas y evidencia desde la versión actual |
| Inteligibilidad | %ALCons mediante Peutz | M2 propio y opción integrada al flujo RT; resultado dedicado | Actualizar el flujo y la pantalla de resultados |
| Base Bloque H | 23 tipos de salones | 23 tipos en diccionarios Python | Confirmar etiquetas, integridad y datos vigentes |
| Coeficientes de materiales | Tablas en hojas Excel | Excel + `openpyxl`/pandas según documentación | Identificar archivo(s), hojas, columnas, bandas y origen de datos |
| Reportes | Exportación PDF | Reportes RT e inteligibilidad con sistema visual estandarizado | Sustituir capturas y documentar estructura actual |
| Interfaz | Pantallas de bienvenida, módulos y formularios | M1/M2/M3 refinados; Ayuda V1 incorporada | Actualizar capturas, nombres de pantallas y navegación |
| Clasificación %ALCons | El Word presenta la valoración de forma general y una tabla previa | D-019 implementa seis categorías operativas | Explicar diferencia entre fuente bibliográfica y decisión del proyecto |
| Arquitectura | MVC / MVC+S | Repositorio separado en Modelo, Vista, Controlador, Datos y Recursos | Actualizar diagrama con estructura y dependencias reales |
| Validación | Propone comparación con mediciones reales | Hay pruebas de software y comparaciones de regresión documentadas | Separar validación matemática, pruebas de software y validación experimental |
| Plataforma | PyCharm, Python, PySide6/Qt Designer | Entorno fijado y probado en Linux/SteamOS | Actualizar versión de Python/dependencias y registrar compatibilidad Windows como pendiente |

## 4. Discrepancias y asuntos que necesitan resolución

### 4.1 Portada y fechas del documento

En las primeras páginas aparece una portada con año 2025 y otra página de presentación del trabajo de grado con año 2020. Debe confirmarse cuál es la fecha correcta de la versión y eliminarse la inconsistencia antes de producir una versión académica final.

### 4.2 Ecuación/umbral por tramos del modelo de Peutz

El Word, en la explicación de inteligibilidad (páginas 23–24), describe que el régimen cercano se aplica cuando la distancia del oyente es menor a 3,5 veces la distancia crítica. La documentación técnica actual del repositorio registra el umbral implementado como 3,16 × Dc.

Este punto requiere revisar la fuente bibliográfica y la ecuación exacta adoptada. No cambiar código ni Word hasta confirmar el criterio matemático aprobado. Registrar el resultado en `ACOUSTIC_MODEL.md` y, si corresponde, en `DECISIONS.md`.

### 4.3 Fórmula de distancia crítica

El Word expone la definición de distancia crítica y la constante de sala, pero la extracción disponible no permite verificar de manera inequívoca toda la ecuación impresa. La documentación técnica del repositorio identifica una expresión usada y otra alternativa definida pero no usada. Debe mantenerse explícita la diferencia entre fórmula activa y alternativa, sin presentar ambas como equivalentes.

### 4.4 Módulo de Inteligibilidad

El Word describe un formulario independiente y un cuadro de texto informativo. El estado actual documentado incluye un formulario con campos específicos, validación inline, pantalla de resultados propia y clasificación de seis niveles. La tesis necesita describir el comportamiento que existe actualmente y actualizar sus capturas.

### 4.5 Ayuda

El Word describe Ayuda como un espacio para manual de usuario, créditos, archivos de referencia y datos de contacto. La implementación Ayuda V1 documentada en octubre de 2026 es una guía interactiva de seis secciones. Revisar el contenido real y actualizar la descripción; no asumir que la V1 incluye todas las funciones enumeradas en el Word antiguo.

### 4.6 Validación académica vs. pruebas de software

El Word establece criterios de aceptación como error menor al 10 % para RT en al menos tres aulas y error ≤ 5 % para inteligibilidad frente a referencias. La documentación del repositorio también registra pruebas de regresión, comparación de resultados entre commits, pruebas de interfaz y generación PDF.

Estas actividades no son intercambiables:

- **Prueba unitaria:** verifica una función o fórmula con entradas controladas.
- **Prueba de integración:** verifica el flujo entre componentes.
- **Regresión:** verifica que cambios no alteren resultados previos.
- **Validación experimental:** contrasta el modelo/software contra mediciones reales o referencias experimentales identificadas.

No afirmar que el objetivo de validación mediante mediciones reales está cumplido hasta reunir registros de mediciones, condiciones de ensayo, instrumentos, incertidumbre, valores de referencia, resultados del software y análisis de error.

### 4.7 Estado del manuscrito

El archivo suministrado tiene 57 páginas y el contenido extraído llega al diseño de la estructura de datos y la bibliografía. No se observan capítulos desarrollados de conclusiones ni recomendaciones en el material revisado. La tabla de contenido también termina en el capítulo metodológico, aunque el cuerpo alcanza el capítulo 8.

El manuscrito contiene además referencias de campo sin resolver (“Error: Reference source not found”), números de figuras/tablas incompletos y entradas bibliográficas que requieren normalización y revisión de pertinencia. Estos son asuntos editoriales y de estructura, no defectos del software.

## 5. Evidencias necesarias para cerrar la relación software–tesis

| Evidencia | Uso académico | Estado |
|---|---|---|
| Código/commit de la versión evaluada | Identificar versión del producto evaluado | Pendiente de fijar versión de evaluación |
| Casos de cálculo de referencia | Sustentar exactitud de Sabine/Eyring/Peutz | Pendiente de consolidación |
| Datos medidos de aulas | Validación experimental | No aportados en este paquete |
| Matriz de error | Cuantificar diferencias por aula y frecuencia | Pendiente |
| Capturas actuales de M1/M2/M3/Ayuda | Describir interfaz implementada | Requiere capturas de versión actual |
| Ejemplos PDF actuales | Evidenciar salidas del sistema | Requiere revisión visual final |
| Inventario de aulas y fuentes | Sustentar la base de datos de 23 tipos | Requiere confirmar fuente primaria y trazabilidad |
| Matriz requisito–implementación–prueba | Demostrar cumplimiento de objetivos | Por construir |
| Prueba de instalación reproducible | Sustentar transferencia/ejecución | Linux/SteamOS documentado; Windows POR VALIDAR |

## 6. Matriz de cumplimiento de objetivos: estado preliminar

| Objetivo específico | Evidencia disponible | Estado preliminar |
|---|---|---|
| Algoritmos RT e inteligibilidad | M1, M2, documentación de modelos y decisiones | Implementado en el software; validación académica final por consolidar |
| Interfaz intuitiva y visualización | UI_INVENTORY, CHANGELOG, HANDOFF y módulos refinados | Implementación documentada; evaluación formal de usabilidad por consolidar |
| Validación mediante mediciones reales | El Word la plantea; TESTING registra pruebas de software y regresión | PENDIENTE DE EVIDENCIA EXPERIMENTAL |
| Personalización de análisis, modelos y salidas | Formularios, selección de materiales, objetos, Sabine/Eyring, parámetros de inteligibilidad y PDF | Requiere mapear cada aspecto a requisitos y pruebas actuales |

Este estado es deliberadamente conservador: diferencia funcionamiento documentado de cumplimiento académico demostrado.

## 7. Regla para futuras actualizaciones del Word

Antes de insertar texto nuevo en el manuscrito:

1. identificar el capítulo y afirmación que se quiere actualizar;
2. citar la fuente técnica o evidencia del repositorio;
3. confirmar si se trata de una decisión, una implementación o un resultado probado;
4. comprobar si el cambio altera objetivos, metodología, resultados o conclusiones;
5. revisar con el equipo académico;
6. actualizar figuras, tablas, referencias cruzadas y bibliografía asociadas.

Este documento es una matriz de trabajo. No reemplaza ni modifica el Word académico.
