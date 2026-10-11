# Revisión metodológica — Clasificación cualitativa del %ALCons

**Estado: CRITERIO OPERATIVO APROBADO E IMPLEMENTADO (2026-10-11, D-019).**
El equipo aprobó la clasificación de la sección 8 como **criterio operativo
vigente del software** (registrado en `docs/DECISIONS.md`, D-019) y se
implementó el mismo día en `Modelo/alcons2.py::evaluar_alcons`,
`Datos/utils/reportePDF.py::NIVELES_ALCONS` y el panel estático del
formulario de Inteligibilidad (corregido por código en
`Vista/ventInteligibilidad.py`, sin tocar el `.ui`). Modelo, PDF e interfaz
muestran ya la misma clasificación (ver sección 14). Esta implementación es
sobre la **clasificación**, no sobre la fórmula de cálculo del %ALCons
(sección 3), que no cambió — verificado contra los 23 salones del Bloque H.
Esto **no** implica que la redacción académica definitiva de la tesis esté
cerrada; esa revisión se hará en un bloque posterior e independiente.

Preparado a partir de: (a) el código actual del repositorio, (b) el artículo
académico localizado como fuente bibliográfica directa (ver sección 12), y
(c) el criterio operativo de 6 categorías que el equipo aprobó (D-019). No
se tuvo acceso en este entorno al Word de la tesis
(`proyectoGradoSoftware.docx`); no se afirma haberlo leído. El artículo usado
como fuente principal se encontró en `~/Downloads/` de esta misma máquina,
**no fue adjuntado a esta conversación** — se identifica así explícitamente
para que el equipo confirme que es el material que quería usar como
referencia (ver sección 12 para los detalles que lo hacen, con alta
probabilidad, relevante y no una coincidencia).

---

## 1. Qué es el %ALCons y qué representa

El %ALCons ("porcentaje de pérdida de articulación de consonantes",
*Articulation Loss of Consonants*) es un indicador objetivo de inteligibilidad
del habla en un recinto cerrado. Estima qué fracción de las consonantes
pronunciadas por un hablante **no llega de forma comprensible** al oyente,
debido a la combinación de reverberación y distancia entre emisor y receptor.
Las consonantes son las que distinguen palabras parecidas entre sí (p. ej.
"pero"/"perro"); perderlas reduce la inteligibilidad del mensaje aunque el
volumen sonoro sea suficiente. Fue formulado por Victor M. A. Peutz en 1971
(citado en la fuente académica, sección 12, ref. [19] del artículo).

## 2. Diferencia entre cálculo numérico y clasificación cualitativa

Son dos pasos distintos y **este documento solo revisa el segundo**:

1. **Cálculo numérico** (`Modelo/alcons2.py::calcular_alcons`): produce un
   valor continuo en porcentaje, a partir de la fórmula de Peutz (sección 3).
   **No se toca en esta revisión.**
2. **Clasificación cualitativa** (`Modelo/alcons2.py::evaluar_alcons`): toma
   ese número y lo traduce a una categoría con nombre (Excelente, Buena...) y
   una frase explicativa para el usuario. Es un mapeo de rangos sobre un
   número ya calculado; cambiarlo **no altera el %ALCons de ningún salón**,
   solo la etiqueta con la que se presenta.

La distinción importa porque todo lo que sigue es sobre el punto 2. El punto
1 (la fórmula) no está en discusión.

## 3. Fórmulas y supuestos de Peutz utilizados por el proyecto

Tal como están implementadas en `Modelo/alcons2.py` (sin cambios) y
documentadas en `docs/ACOUSTIC_MODEL.md` §4:

```
R   = (S_TOT · ᾱ) / (1 − ᾱ)              Constante del recinto
Dc  = 0.21 · √(V / TR_2000Hz)            Distancia crítica (fórmula en uso)
Dc' = 0.14 · √(Q · R)                    Distancia crítica alternativa (definida en código, NO usada hoy)

si r ≤ 3.16 · Dc:  %ALCons = (200 · r² · TR²) / (V · Q)
si r >  3.16 · Dc:  %ALCons = 9 · TR
```

Donde `r` = distancia emisor–oyente (m), `TR` = tiempo de reverberación a
2000 Hz (s), `V` = volumen de la sala (m³), `Q` = factor de directividad
(fijo en 2, voz humana frontal), `S_TOT` = superficie total del recinto (m²),
`ᾱ` = coeficiente medio de absorción.

El artículo académico de la sección 12 (p. 3–4) presenta la misma fórmula por
tramos y los mismos supuestos (Q=2 para voz frontal, TR a 2000 Hz, r en
metros), citando a Peutz (1971) a través de García Lope (ref. [19] del
artículo). Las imágenes de las fórmulas de `Dc` y `R` en ese PDF no se
extrajeron como texto legible (son ecuaciones incrustadas como gráfico); el
texto circundante sí confirma que usa las mismas variables (`Q`, `R`,
`S_TOT`, `ᾱ`) que `Modelo/alcons2.py`. **No se verificó carácter por carácter
esa ecuación en el artículo**, se señala como limitación (sección 11).

**Nota de trazabilidad (no es parte del cálculo, pero es relevante):**
`Modelo/alcons2.py::calcular_distancia_critica` implementa `Dc'` pero no se
usa; `generar_reporte` usa `calcular_dc` (`Dc`). `docs/ACOUSTIC_MODEL.md`
documenta ambas sin indicar cuál es la vigente — ya señalado en la auditoría
general del 2026-10-06. No se resuelve en este documento (es un tema de la
fórmula/implementación, no de la clasificación).

## 4. Tabla de cinco categorías encontrada en las fuentes

El artículo académico (sección 12), en su Tabla 1 ("Correspondencia %ALCons y
escala subjetiva", p. 4), cita la siguiente tabla **tal cual aparece
impresa**, atribuida a su referencia [20] (C. Carrión Carranza y C. M.
Carrión, *Valores y Principios para Evaluar la Educación*, Paidos Mexicana,
2001):

| %ALCons | Valoración |
|---|---|
| 0 % – 1,4 % | Excelente |
| 1,6 % – 4,8 % | Buena |
| 5,3 % – 11,4 % | Regular |
| 12 % – 24,2 % | Pobre |
| 27 % – 46,5 % | Mala |

Son **cinco** categorías, no seis: no existe una sexta fila para valores por
encima de 46,5 %.

## 5. Intervalos que la fuente no define explícitamente

La tabla de la sección 4, tomada literalmente, **no es continua**: hay
huecos entre categorías consecutivas que la fuente no asigna a ninguna
valoración:

| Hueco | Rango sin clasificar |
|---|---|
| Entre Excelente y Buena | 1,4 % < x < 1,6 % |
| Entre Buena y Regular | 4,8 % < x < 5,3 % |
| Entre Regular y Pobre | 11,4 % < x < 12 % |
| Entre Pobre y Mala | 24,2 % < x < 27 % |
| Por encima de Mala | x > 46,5 % (sin categoría) |

Un valor calculado que caiga exactamente en uno de estos huecos (por ejemplo
4,9 %, o 25 %) no tiene, según la tabla publicada, una categoría literal
asignada. Cualquier software que use esta tabla **tiene que decidir** cómo
cerrar esos huecos; la fuente no lo hace por el equipo.

## 6. Diferencias de nomenclatura entre fuentes

| Fuente | Categorías | Nombres |
|---|---|---|
| Artículo académico, Tabla 1 (ref. [20]) | 5 | Excelente, Buena, Regular, Pobre, Mala |
| `Modelo/alcons2.py::evaluar_alcons` (código actual) | 6 | Excelente, Buena, Regular, Pobre, Mala, **Crítico** |
| `Datos/utils/reportePDF.py::NIVELES_ALCONS` (PDF, UX-07) | 6 | Idénticos al código (Excelente…Crítico) |
| `docs/ACOUSTIC_MODEL.md` §5 | 6 | Idénticos al código |
| Panel estático "Escala %ALCons" del formulario, **antes** de este bloque (`inteligibilidadHabla.ui`, `frame_escala`) | 5 | Excelente, Buena, Regular, Pobre, **Mala** (última fila, sin "Crítico") |
| Criterio operativo adoptado e implementado (D-019) — modelo, PDF e interfaz | 6 | Excelente, Buena, Regular, Pobre, Mala, Crítico |

Los **nombres** de categoría son consistentes entre todas las fuentes
(ninguna usa un nombre distinto para el mismo nivel); la diferencia real
estaba en los **umbrales numéricos** y en si existía o no una sexta
categoría. Desde la implementación de D-019 (2026-10-11), el código, el PDF
y el panel del formulario ya usan la misma escala de 6 categorías — ver
sección 14 (Tarea 3) para el detalle cruzado actualizado.

## 7. El problema de los resultados superiores a 46,5 %

Ninguna de las cinco categorías de la fuente académica cubre valores por
encima de 46,5 %. Esto no es un caso hipotético: el propio repositorio tiene
un valor de prueba de `%ALCONS: 204.48` en `Datos/salones.py` (variable
`DiccionarioRecibido`, un diccionario de ejemplo sin uso en la app real, pero
que muestra que el cálculo puede producir valores muy por encima de 46,5 %
ante parámetros extremos — p. ej. un TR muy alto). Sin una categoría
"Crítico" (o equivalente), el software tendría que: (a) dejar esos valores
sin clasificar, (b) reutilizar incorrectamente la etiqueta "Mala" para
condiciones mucho peores entre sí, o (c) fallar. El código actual y la
criterio operativo adoptado (D-019) resuelven esto añadiendo una sexta
categoría; la tabla de la fuente académica, tal como está publicada, no lo
resuelve.

## 8. Criterio operativo de clasificación adoptado por el proyecto (6 categorías)

**CRITERIO OPERATIVO APROBADO E IMPLEMENTADO (D-019, `docs/DECISIONS.md`):**

```
0 % ≤ x ≤ 1,4 %      → Excelente
1,4 % < x ≤ 4,8 %    → Buena
4,8 % < x ≤ 11,4 %   → Regular
11,4 % < x ≤ 24,2 %  → Pobre
24,2 % < x ≤ 46,5 %  → Mala
x > 46,5 %           → Crítico
```

**Esto no es la tabla de la fuente bibliográfica (sección 4) transcrita tal
cual** — la fuente no define una escala continua de 6 categorías; define 5,
con huecos entre ellas (sección 5) y sin ninguna por encima de 46,5 %
(sección 7). Lo que sí toma de la fuente, literalmente, son los **5 límites
superiores** de cada categoría (1,4 / 4,8 / 11,4 / 24,2 / 46,5). A partir de
ahí, el proyecto decide, como criterio operativo propio:

1. Cerrar los huecos de la sección 5 asignando cada valor intermedio no
   especificado por la fuente a la categoría **inmediatamente siguiente**
   (el límite superior de una categoría es, con `>` estricto, el arranque de
   la siguiente) — en vez de usar los límites inferiores, ligeramente
   distintos, que también publica la tabla (1,6 / 5,3 / 12 / 27).
2. Garantizar que **todo** valor de %ALCons no negativo tenga una categoría,
   sin dejar huecos sin clasificar.
3. Añadir **"Crítico"** para x > 46,5 %. Esta categoría es una **extensión
   operativa propia del proyecto**, no una categoría que la fuente
   bibliográfica defina ni nombre — se incorpora para resolver el problema
   de la sección 7 (valores por encima del límite superior que sí publica la
   fuente, como el caso real de `Datos/salones.py::DiccionarioRecibido`,
   %ALCONS = 204.48).

## 9. Qué valores proceden de la bibliografía y cuáles son decisiones del equipo

| Elemento | Origen |
|---|---|
| Los 5 nombres de categoría (Excelente…Mala) | Bibliografía (artículo, Tabla 1, ref. [20]) |
| Los 5 límites superiores (1,4 / 4,8 / 11,4 / 24,2 / 46,5) | Bibliografía (literal de la Tabla 1) |
| Los 5 límites inferiores "alternativos" que publica la tabla (1,6 / 5,3 / 12 / 27) | Bibliografía, pero **no se usan** en el criterio operativo adoptado (ver más abajo) |
| Cerrar los huecos usando el límite superior de cada categoría como frontera (en vez del límite inferior ligeramente distinto de la siguiente) | **Decisión metodológica del equipo** — la fuente no indica cuál de los dos números (p. ej. 4,8 o 5,3) debe ser la frontera real; ambos aparecen impresos y son incompatibles entre sí para una partición continua |
| Añadir la categoría "Crítico" para x > 46,5 % | **Decisión metodológica del equipo** — no existe en la fuente académica consultada |
| El nombre "Crítico" en sí (y no otro, p. ej. "Muy mala") | Ya estaba en el código heredado (`Modelo/alcons2.py`) antes de esta revisión; se reutiliza en el criterio operativo adoptado por continuidad, no proviene de la fuente académica de la sección 12 |
| Los umbrales que estuvieron activos en el código **antes de D-019** (1,4 / **5** / 11,4 / **24,4** / **47**, reemplazados el 2026-10-11) | **Sin origen documentado en el repositorio** (ver sección 11) — no coincidían exactamente con ninguno de los dos juegos de números que publica la fuente académica (ni los superiores 4,8/24,2/46,5 ni los inferiores 5,3/27) |

## 10. Ejemplos de clasificación en los límites e intervalos intermedios

Comparando la clasificación que daban los umbrales **anteriores a D-019**
(`alcons2.py`, 1,4/5/11,4/24,4/47, reemplazados el 2026-10-11) contra el
**criterio operativo vigente** (D-019; umbrales 1,4/4,8/11,4/24,2/46,5). Las
filas en negrita son casos donde ambas escalas **difieren** — es decir,
casos donde esta implementación cambió el resultado mostrado al usuario:

| %ALCons | Clasificación con los umbrales anteriores (histórico) | Clasificación con el criterio operativo vigente (D-019) |
|---|---|---|
| 1,4 (límite) | Excelente | Excelente |
| **4,9** | Buena (≤ 5) | **Regular** (> 4,8) |
| 5,0 (límite anterior) | Buena | Regular |
| 11,4 (límite, coincide en ambas) | Regular | Regular |
| **24,3** | Pobre (≤ 24,4) | **Mala** (> 24,2) |
| **46,8** | Mala (≤ 47) | **Crítico** (> 46,5) |
| 47,2 | Crítico | Crítico |

Caso real tomado del artículo académico (sección 12): los 23 tipos de salón
que reporta (Tabla 3 del artículo) tienen %ALCons entre 12,69 % y 24,12 %.
Con **ambas** escalas, los 23 valores caen en "Pobre" sin excepción — en ese
conjunto de datos publicado, la diferencia de umbrales no cambiaba ningún
resultado. Lo mismo se verificó en esta implementación contra los 23 salones
de `Datos/salones.py` (sección 15): ninguno cruza un umbral que haya
cambiado, así que su clasificación textual no varió — pero la tabla anterior
muestra que sí hay divergencia real cerca de 4,8–5,0 %, 24,2–24,4 % y
46,5–47 %, y cualquier salón futuro con un %ALCons en esos rangos sí se
clasificará distinto que antes de D-019.

## 11. Limitaciones y aspectos que todavía deben verificarse

1. **No se tuvo acceso al Word de la tesis** en este entorno; esta revisión
   se apoya en el artículo académico de la sección 12 como fuente
   bibliográfica disponible, no en el documento de grado. Falta confirmar
   que ambos documentos usan la misma tabla de clasificación.
2. **La referencia [20] del artículo** (Carrión Carranza y Carrión, *Valores
   y Principios para Evaluar la Educación*, Paidos Mexicana, 2001) es un
   libro sobre evaluación educativa, no un texto de acústica técnica; no se
   tuvo acceso a ese libro para verificar la tabla en su fuente original. Es
   posible que sea una cita de segunda o tercera mano de la tabla original de
   Peutz/IEC — no se puede confirmar ni descartar con lo disponible.
3. **El origen de los umbrales actualmente activos en el código** (5 / 24,4
   / 47, en vez de 4,8 / 24,2 / 46,5 o 5,3 / 27 / sin límite) no está
   documentado en ningún commit ni documento del repositorio: estaban ya
   presentes en el snapshot inicial entregado para este proyecto (antes de
   cualquier sesión de Claude Code). No se pudo determinar si provienen de
   una fuente distinta, de un redondeo deliberado, o de un error de
   transcripción.
4. Las fórmulas de `Dc` y `R` del artículo académico están incrustadas como
   imagen en el PDF; no se pudieron extraer como texto para comparar
   carácter por carácter con `Modelo/alcons2.py` (sí se comparó el texto
   circundante y las variables nombradas, que coinciden).
5. No se verificó si el "Word vigente" del proyecto (fuente académica
   principal según `CLAUDE.md` §1) reproduce la tabla de 5 categorías del
   artículo, una distinta, o directamente el criterio operativo adoptado de 6
   categorías — es
   la pregunta central que el equipo está resolviendo con la fuente
   bibliográfica.
6. Esta revisión no evalúa si 46,5 % (o 47 %) es, en términos acústicos, el
   punto de corte correcto entre "Mala" y una categoría peor — solo compara
   qué dicen las fuentes disponibles y qué decide hoy el código. La
   idoneidad acústica del punto de corte es una decisión del equipo
   académico, no algo que este documento resuelva.

## 12. Referencias bibliográficas

**Fuente principal de esta revisión** (localizada en
`~/Downloads/Dialnet-EvaluacionDeLasCondicionesAcusticasDeLasAulasDeCla-10417103.pdf`
de esta máquina; no fue adjuntada a la conversación, se identifica aquí para
que el equipo la confirme):

> Duran Uron, A. E., Jimeno Martínez, M. G., Rodríguez Barraza, D. S.,
> Meléndez Serrano, A. I., & Arteta Peña, Y. C. (2025). *Evaluación de las
> condiciones acústicas de las aulas de clase de un centro de educación
> superior de la Costa Caribe Colombiana*. Investigación e Innovación en
> Ingenierías, 13(1), 82–96. https://doi.org/10.17081/invinno.13.1.8065

Razones para considerarla altamente relevante (no una coincidencia): autoría
afiliada a la Universidad del Atlántico (correo de correspondencia
`armando.duran@mail.uniatlantico.edu.co`, mismo dominio que el usuario de
este proyecto); usa exactamente los **23 tipos de salón** del Bloque H, con
los **mismos rangos de número de aula** que `Datos/salones.py` (p. ej. "Tipo
1 → aulas 101-104", idéntico al código); usa las mismas fórmulas de Sabine,
Eyring, BB93 (Tr MID, límite 0,8 s) y Peutz (%ALCons) que implementa este
software.

**Referencias citadas dentro de ese artículo, relevantes para este
análisis:**

- [19] García Lope, P. P. *Acondicionamiento acústico del aula 105, Capítulo
  2: Diseño acústico de salas*. Universidad de Sevilla.
  http://bibing.us.es/proyectos/abreproy/4393/fichero/Capitulo+2%2FCapitulo+2.pdf
  — fuente de la fórmula de Peutz citada por el artículo.
- [20] Carrión Carranza, C., & Carrión, C. M. (2001). *Valores y Principios
  para Evaluar la Educación* (edición ilustrada, vol. 162, 180 págs.).
  México: Paidós Mexicana. — fuente de la Tabla 1 (5 categorías, sección 4
  de este documento). No se tuvo acceso al texto completo; no se verificó
  en la fuente original.
- [18] Department for Education (DFE). (2015). *Building Bulletin 93 (BB93):
  Acoustic design of schools*. Europa. (Norma que fija Tr MID ≤ 0,8 s para
  aulas, ya usada por `Modelo/calculoRT2.py`/`docs/ACOUSTIC_MODEL.md` sin
  cambios en esta revisión.)

**Documentos internos del repositorio consultados** (sin modificar):
`Modelo/alcons2.py`, `Datos/utils/reportePDF.py`, `Datos/salones.py`,
`docs/ACOUSTIC_MODEL.md`, `docs/REPORTS.md`, `docs/REQUIREMENTS.md`,
`Vista/archivos_pyGenerados/inteligibilidadHabla.py` (panel estático de
escala).

---

## 13. Documento base para futuras investigaciones (no usado para justificar esta decisión)

El equipo indicó que existe, en el entorno local del equipo, un documento de
referencia adicional:

> Rodríguez Barraza, D. S., & Jimeno Martínez, M. G. (2020). *Evaluación de
> las condiciones acústicas de las aulas de clase del Bloque H de la
> Universidad del Atlántico*. Universidad del Atlántico.

**No se tuvo acceso a este documento en este entorno** y no se usó para
preparar ninguna sección de este análisis ni para justificar el criterio
operativo de la sección 8 — esa justificación se apoya exclusivamente en la
fuente bibliográfica de la sección 12 (Duran Uron et al., 2025), que sí se
pudo leer. Nótese que ambos trabajos comparten dos de las mismas autoras
(Rodríguez Barraza y Jimeno Martínez) y el mismo Bloque H de 23 tipos de
salón, por lo que es razonable asumir que están relacionados (posiblemente
el trabajo de grado del que deriva el artículo de 2025), pero esto no se
verificó.

Se registra aquí, tal como pidió el equipo, como **fuente de referencia del
proyecto para futuras investigaciones, verificaciones metodológicas y
decisiones relacionadas con el modelo acústico** (RT60, Sabine/Eyring,
%ALCons, Peutz, geometría y materiales de las aulas, metodología de
evaluación). Cuando una decisión futura dependa de su contenido, deberá
consultarse directamente y distinguirse explícitamente qué proviene de él y
qué es una decisión propia del proyecto — siguiendo el mismo criterio de
trazabilidad aplicado en este documento para la fuente de 2025. No debe
usarse para completar ni inventar información que no se haya verificado en
él directamente.

---

## 14. Tarea 3 — Revisión cruzada (contradicciones internas)

**Actualizada 2026-10-11, después de implementar D-019.**

| Par comparado | ¿Coinciden? | Detalle |
|---|---|---|
| `Modelo/alcons2.py::evaluar_alcons` ↔ `Datos/utils/reportePDF.py::NIVELES_ALCONS` | **Sí** | Mismos 6 niveles, mismos umbrales (1,4/4,8/11,4/24,2/46,5; criterio operativo D-019). `docs/REPORTS.md` documenta esto como contrato deliberado (UX-07/D-019). |
| `Modelo/alcons2.py` ↔ `Vista/ventInteligibilidad.py` (panel "Escala %ALCons") | **Sí** | El panel se corrigió por código (sin tocar el `.ui`) para mostrar las mismas 6 categorías y los mismos umbrales que el modelo, incluyendo un bloque nuevo para "Crítico" que antes no existía. |
| `Modelo/alcons2.py` ↔ `docs/ACOUSTIC_MODEL.md` §5 | **Sí** | El documento transcribe exactamente los umbrales del código actual (D-019). |
| `Datos/utils/reportePDF.py` ↔ `docs/REPORTS.md` | **Sí** | `REPORTS.md` describe `NIVELES_ALCONS` tal como está en el código. |
| `docs/REQUIREMENTS.md` (RF-07) ↔ el resto | **Sí, por referencia** | No fija números propios; dice "escala de %ALCONS de 6 niveles idéntica a la del modelo", y una nota explícita confirma que ya está implementada (D-019). |
| Criterio operativo adoptado (D-019) ↔ fuente bibliográfica (sección 4) | **Parcial, documentado como tal** | Comparte los 5 límites superiores; difiere en cómo cierra los huecos y añade "Crítico". Ninguna sección de este documento afirma que la fuente presente literalmente la escala de 6 categorías (ver §8, §9) — esto se mantiene igual después de implementar: la distinción fuente/decisión operativa es independiente de que el código ya la use. |

**Antes de esta implementación** existían dos contradicciones, ambas
resueltas en este bloque: (a) el panel estático del formulario usaba 5
categorías con umbrales 0–2/2–5/5–10/10–15/>15 %, ajenos a todo lo demás
(señalada en la inspección del Bloque 2, punto F.1); (b) el código activo
usaba los umbrales antiguos (1,4/5/11,4/24,4/47) mientras D-019 ya estaba
aprobada como criterio operativo pero no implementada. Ninguna de las dos
sigue vigente.

No quedó ninguna referencia **viva** (en ejecución real de la aplicación) a
la escala antigua. `Modelo/%alcons.py` (archivo legacy, confirmado sin
ningún `import` en el repositorio) conserva su propia clasificación interna
con los umbrales antiguos; no se tocó, por estar fuera del alcance de este
bloque (no es código vivo) y porque el equipo pidió explícitamente no hacer
limpieza general de legacy en este bloque.

## 15. Verificación de la implementación (2026-10-11)

Pruebas ejecutadas tras implementar D-019 (detalle completo en la respuesta
de la sesión; resumen aquí para trazabilidad):

- **Límites exactos** (0, 1,4, 1,4001, 4,8, 4,8001, 11,4, 11,4001, 24,2,
  24,2001, 46,5, 46,5001, y los valores representativos 1,5/5,0/25,0/50,0):
  los 15 casos clasifican igual en `Modelo/alcons2.py::evaluar_alcons` y en
  `Datos/utils/reportePDF.py::_nivel_alcons`, y coinciden con la categoría
  esperada en los 15 casos.
- **Cobertura sin huecos ni solapes**: barrido de 0 a 200 % en pasos de
  0,001 (200 000 valores) — ningún valor no negativo quedó sin clasificar.
- **23 salones de `Datos/salones.py`**: `sabine_rt`, `eyring_rt`, el
  `%ALCONS` numérico y la `Distancia Crítica (Dc)` son idénticos a los que
  calculaba el código antes de esta implementación (comparado contra
  `git show HEAD:Modelo/calculoRT2.py`); ninguno cruza un umbral que haya
  cambiado, así que tampoco cambió el texto de clasificación de ninguno —
  resultado esperado, no un error (ver sección 10).
- **PDF**: `ReportePDF.reporte_tiempo_reverberacion` sigue generando el
  archivo correctamente con la nueva escala.
- **Arranque e imports**: la aplicación completa (`Vista/main.py`) y todos
  los módulos importan y arrancan sin excepciones.

No se modificó ninguna fórmula acústica, el cálculo numérico del %ALCons, la
distancia crítica, RT60 (Sabine/Eyring) ni el diseño visual del PDF.
