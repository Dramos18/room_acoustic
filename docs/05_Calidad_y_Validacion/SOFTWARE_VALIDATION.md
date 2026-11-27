# Validación y verificación del software

**Proyecto:** Room Acoustic  
**Base:** código y documentación inspeccionados en la rama docs/knowledge-base-2026-11, 2026-11-27  
**Estado:** matriz de evidencia y protocolo. No declara ejecutadas pruebas que solo están descritas como procedimiento.

## 1. Propósito y distinciones

La evaluación separa cuatro dimensiones:

- **Verificación del software:** comprobar que la implementación satisface especificaciones técnicas.
- **Validación del modelo:** comprobar que la formulación y sus parámetros representan adecuadamente el fenómeno para el uso previsto.
- **Validación experimental:** contrastar resultados con mediciones reales o referencias experimentales independientes.
- **Evaluación de usabilidad:** comprobar que usuarios representativos pueden completar tareas previstas de forma eficaz y comprensible.

Una comparación de regresión entre versiones demuestra estabilidad, no exactitud física. Una prueba de interfaz no valida el modelo acústico.

## 2. Alcance

| Componente | Aspectos por verificar |
|---|---|
| M1 — Tiempo de Reverberación | Geometría, áreas, absorción por banda, Sabine, Eyring, resultados y PDF |
| M2 — Inteligibilidad | Parámetros, distancia crítica activa, condición por tramos, %ALCons y D-019 |
| M3 — Base de Datos | Integridad de 23 perfiles, selección, procesamiento compartido, identificación y PDF |
| Interfaz | Navegación, validaciones, responsividad y estados de error |
| Datos y salidas | Carga de Excel y generación de PDF |
| Instalación | Reproducibilidad Linux/SteamOS y compatibilidad Windows |

## 3. Evidencia documentada y límites

| ID | Evidencia registrada | Alcance que respalda | No demuestra |
|---|---|---|---|
| EV-01 | CHANGELOG registra smoke test de imports y arranque (2026-09-13) | Imports y arranque en el entorno de esa sesión | Ausencia de defectos en todos los flujos/plataformas |
| EV-02 | CHANGELOG registra comparación de un caso de referencia antes/después de corregir validación de áreas | No regresión del caso comparado | Exactitud absoluta |
| EV-03 | CHANGELOG y D-019 registran comparación numérica de 23 salones al cambiar la clasificación | Conservación de resultados numéricos en ese cambio | Validez física de datos y ecuaciones |
| EV-04 | DEPENDENCIES registra instalación limpia en Linux/SteamOS | Reproducibilidad documentada en ese entorno | Compatibilidad Windows |
| EV-05 | HANDOFF registra verificación de Ayuda V1 en cuatro tamaños | Responsividad en tamaños documentados | Usabilidad con participantes |
| EV-06 | TESTING describe procedimientos manuales de UI, PDF, regresión y salones | Protocolo reproducible documentado | Ejecución reciente de cada caso |
| EV-07 | REPORTS especifica estructura, paginación y controles PDF | Diseño y procedimiento de comprobación | Aprobación visual final de todos los PDF |
| EV-08 | ACADEMIC_ALIGNMENT identifica objetivos de error y comparación experimental del Word | Requisitos académicos a comprobar | Cumplimiento de los umbrales |

**Limitación de esta actualización:** se inspeccionaron código y documentación remotos. No se ejecutó la aplicación ni se corrieron pruebas en una máquina de desarrollo; tampoco se inspeccionaron registros primarios de mediciones acústicas.

## 4. Protocolo de verificación del software

La ejecución debe fijarse a un commit y un entorno identificables. Registrar SHA, rama, sistema operativo, versión de Python, dependencias, versión/hash de los Excel, fecha, responsable, resultado y evidencia.

### 4.1 Pruebas unitarias

Crear casos deterministas para:
1. áreas de paredes, piso, techo y volumen;
2. área remanente tras descontar objetos adheridos;
3. rechazo cuando el área adherida excede el área geométrica;
4. absorción de material base, objetos adheridos y adicionales;
5. Sabine por banda;
6. Eyring y dominio del logaritmo;
7. constante del recinto y distancia crítica;
8. selección de rama de %ALCons;
9. clasificación D-019, incluidos límites y valores inmediatamente inferiores/superiores;
10. entradas nulas, negativas, no numéricas y resultados no finitos.

Cada caso debe registrar entrada, salida esperada, tolerancia, fuente matemática y resultado observado. Probar explícitamente el resultado textual "Infinito", que puede devolver el motor RT cuando la absorción o el dominio no permiten un valor finito.

### 4.2 Pruebas de integración

- M1: formulario → diccionario → controlador → cálculo → gráfico/resultados → PDF.
- M2: formulario → cálculo → resultados → PDF.
- M3: selección de perfil → cálculo compartido → identificación → PDF.
- Datos: Excel → catálogo de materiales → coeficientes → absorción.

Incluir caminos válidos y errores: fallo de carga Excel, material ausente, datos incompletos y cancelación del guardado.

### 4.3 Interfaz y reportes

Mantener el procedimiento detallado de TESTING.md. Por caso registrar precondiciones, pasos, esperado, observado, captura/PDF/log y estado: aprobado, fallido, bloqueado o no ejecutado. No marcar aprobado por el solo hecho de que el procedimiento esté escrito. Los PDF requieren revisión numérica y visual (paginación, márgenes, solapes, legibilidad e integridad).

## 5. Validación del modelo acústico

Contrastar de forma explícita: ecuaciones del documento académico, código implementado, fuentes bibliográficas originales, unidades, hipótesis y resultados independientes de referencia.

### 5.1 Reverberación

Construir casos conocidos para Sabine y Eyring con geometría y absorción por frecuencia. Justificar método y rango de aplicación. Comparar por banda, no solo con un promedio global.

### 5.2 Inteligibilidad

Resolver antes de cerrar M2 las discrepancias de ACADEMIC_ALIGNMENT.md:
- el Word indica umbral de régimen cercano de 3,5 × Dc, mientras el código documentado usa 3,16 × Dc;
- la expresión de distancia crítica efectivamente utilizada frente a la alternativa implementada;
- parámetros de directividad, TR de referencia y unidades;
- fundamento de D-019 frente a la fuente bibliográfica.

No modificar código para hacer coincidir documentos sin decisión académica explícita y análisis de impacto.

## 6. Validación experimental

La validación experimental exige mediciones independientes. No se satisface con pruebas de interfaz, regresiones entre commits ni resultados generados por el propio software.

Para cada aula/caso registrar:

| Grupo | Información necesaria |
|---|---|
| Identificación | Aula, fecha, responsable y condiciones del recinto |
| Geometría | Dimensiones, método/instrumento y resolución |
| Materiales/ocupación | Superficies, mobiliario, ocupación y estado de puertas/ventanas |
| Instrumentación | Equipo, micrófono, fuente, calibración y configuración |
| Procedimiento | Norma/protocolo, posiciones de fuente/receptor, repeticiones y condiciones pertinentes |
| Referencia | RT medido por banda y, si aplica, métrica de inteligibilidad |
| Software | Commit, entradas, coeficientes y resultados exportados |
| Análisis | Diferencia absoluta, error relativo, tolerancia, incertidumbre y explicación |

Los objetivos del Word (error RT menor al 10 % en al menos tres aulas e inteligibilidad con error ≤ 5 % frente a referencias) son **criterios por verificar**, no resultados alcanzados, hasta aportar mediciones y cálculos comparativos reproducibles.

## 7. Evaluación de usabilidad

La responsividad visual no equivale a evaluación de usabilidad. Si se desea sustentar facilidad de uso, ejecutar tareas con participantes representativos: registrar/seleccionar aula, analizar RT, interpretar resultado, ejecutar inteligibilidad, seleccionar aula de base de datos y exportar PDF.

Registrar éxito, tiempo, errores, solicitudes de ayuda y observaciones. Definir participantes, consentimiento, protocolo y criterio de aceptación antes de ejecutar. Si no se realiza, limitar la tesis a describir decisiones de diseño y verificaciones de interfaz.

## 8. Matriz de cierre

| Prioridad | Actividad | Evidencia requerida | Estado |
|---|---|---|---|
| P0 | Fijar commit y entorno evaluado | Registro de versión/entorno | Pendiente |
| P0 | Actualizar el Word a 3,16 × Dc y verificar fuente primaria de Dc/R | Manuscrito coherente y referencia primaria consultada | Parcial: umbral confirmado; manuscrito y fuente primaria pendientes |
| P0 | Obtener fuentes primarias de geometría, materiales y coeficientes | Catálogo con procedencia | Pendiente |
| P1 | Crear pruebas unitarias de geometría, absorción, RT y %ALCons | Suite y resultados | Pendiente |
| P1 | Ejecutar integración M1/M2/M3 y PDF | Matriz con evidencias | Pendiente de nueva ejecución |
| P1 | Contrastar aulas con mediciones independientes | Informe de error/incertidumbre | Pendiente de evidencia experimental |
| P2 | Validar instalación Windows | Registro reproducible | Pendiente |
| P2 | Evaluar usabilidad si se afirmará en la tesis | Protocolo e informe | Pendiente |

## 9. Criterio de declaración

No declarar globalmente "software validado" mientras existan dimensiones sin evidencia. El informe final debe separar pruebas de software, revisión del modelo, validación experimental, plataformas probadas y limitaciones. Toda conclusión debe rastrearse a un caso, registro, fuente o resultado cuantitativo.

## 10. Documentos relacionados

- ACOUSTIC_DATA_CATALOG.md
- TESTING.md
- ACOUSTIC_MODEL.md
- ACADEMIC_ALIGNMENT.md
- MODULES_SPECIFICATION.md
