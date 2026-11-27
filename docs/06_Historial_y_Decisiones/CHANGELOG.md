# Changelog

## 2026-10-11 — D-017 implementada: feedback al guardar el PDF de RT

`Datos/utils/reportePDF.py::ReportePDF.reporte_tiempo_reverberacion` (usada
por M1 y M3, vía `VentanaGraficaRT`) no informaba éxito ni error al guardar
el PDF, a diferencia de `reporte_inteligibiliad` (M2), que sí lo hacía. Se
cierra la brecha señalada en D-017 (`docs/DECISIONS.md`).

- El cuerpo del método se envolvió en `try/except Exception`, con el mismo
  patrón que ya usaba `reporte_inteligibiliad`: `QMessageBox.Information`
  ("Reporte Generado", con la ruta del archivo) si el guardado tiene éxito,
  `QMessageBox.Critical` ("Error", con el mensaje de la excepción) si falla.
  No se cambió la firma del método (la propuesta original de D-017
  consideraba necesario cambiarla; no lo fue).
- No se tocó la lógica de dibujo del PDF (`_dibujar_reporte_rt`, `_Doc`,
  encabezado, pie, paginación) ni ningún otro método de `ReportePDF`. No se
  modificó M1, M2 ni M3 (solo el guardado del PDF compartido por M1/M3).
- Cancelar el diálogo de guardado sigue sin mostrar ningún mensaje ni crear
  archivo (comportamiento ya existente, verificado sin cambios).
- **Pruebas**: script con `QFileDialog.getSaveFileName` y `QMessageBox.exec`
  simulados (mismo criterio que `docs/TESTING.md` §8), contra un resultado
  real de `calcular_resultados` (Salón tipo 1): (a) guardado exitoso →
  PDF con cabecera `%PDF-` y `QMessageBox.Information` con la ruta correcta;
  (b) ruta en directorio inexistente → no crea archivo, `QMessageBox.Critical`
  con el mensaje de la excepción; (c) cancelar → sin archivo, sin mensaje.
  Los tres casos pasaron.

## 2026-10-11 — Módulo 2 (Inteligibilidad): pantalla de resultados propia y cierre visual (bloque M2-UX)

Auditoría UX/UI previa sin cambios de código; este bloque implementa lo
aprobado de esa auditoría. No se tocó `Modelo/alcons2.py`,
`Datos/utils/reportePDF.py`, ni ningún `.ui`/`.py` generado (mismo criterio
D-011). D-019 (clasificación de %ALCons) no se modificó.

- **Nueva pantalla de resultados** (`Vista/ventResultadosInteligibilidad.py`,
  clase `VentanaResultadosInteligibilidad`): reemplaza el `QMessageBox` que
  mostraba antes `mostrar_resumen_reporte`. Construida en Python puro, sin
  `.ui` nuevo (mismo criterio que `VentanaGraficaRT`): valor de %ALCons y
  categoría en grande con el color del nivel, escala de 6 segmentos (colores
  y umbrales tomados directamente de `Datos/utils/reportePDF.py::NIVELES_ALCONS`
  y `_nivel_alcons`, para que esta pantalla y el PDF no puedan desincronizarse),
  parámetros utilizados y resultado acústico (Dc, R). Reutiliza
  `estiloBarraSuperior`/`estiloBotonAtras`/`estiloBarraInferior`/
  `estiloTarjeta`/`estiloTexto` de `Recursos/estilos/estilo.py`, sin estilos
  paralelos. El PDF se genera llamando a `ReportePDF.reporte_inteligibiliad`
  directamente, sin duplicar lógica.
- **`Vista/ventInteligibilidad.py`**:
  - Flechas de los 5 `QDoubleSpinBox` (`distanciaRyE`, `recintoTR`,
    `volumenSala`, `coeficienteMedio`, `superficieTotal`): no tenían QSS de
    `::up-button/::down-button/::up-arrow/::down-arrow`, así que Qt usaba el
    control nativo, invisible sobre el fondo oscuro. Se aplica el mismo
    bloque QSS (y los mismos iconos `angulo-arriba.png`/`angulo-abajo.png`)
    que ya corrige esto en `Vista/ventTiempoReverberacion.py`.
  - Validación: el `QMessageBox.Warning` bloqueante se reemplaza por un
    texto inline (`labelErrorInteligibilidad`, nuevo `QLabel`, no viene del
    `.ui`) con el mismo prefijo `⚠` y el mismo criterio no bloqueante que el
    formulario de RT; el mensaje ahora nombra cada campo inválido en vez de
    un texto genérico. De paso se corrige el tope superior del coeficiente
    de absorción (antes solo exigía `> 0`; ahora `0 < α ≤ 1`, coherente con
    `docs/REQUIREMENTS.md`) — una corrección que la auditoría anterior daba
    por hecha pero no estaba implementada.
  - Cabecera y pie: reemplazados los estilos inline por los helpers
    centralizados (`estiloBarraSuperior`, `estiloBotonAtras`,
    `estiloBarraInferior`), igual que el resto de la app.
  - `botonGoHome` ya no lleva icono de chevron (inconsistente con Módulo 1 y
    Base de Datos, que lo dejan solo texto).
  - `enviar_calculos_inteligibilidad` navega ahora a
    `VentanaResultadosInteligibilidad` (mismo patrón que
    `abrir_ventana_tiempoReverberacion`/`iniciar_analisis`: `addWidget` +
    `setCurrentWidget`, `indice_anterior` guardado antes de navegar).
  - `mostrar_resumen_reporte`, `generar_reporte_pdf` y `agregar_marca_agua`
    quedan sin uso (superados por la pantalla nueva); se conservan
    documentadas, sin eliminar, mismo criterio que `_marca_agua` (UX-07).
- **Iconos**: no se incorporó ningún icono nuevo de los 9 agregados por el
  equipo en `Recursos/iconos/` (`advertencia.png`, `distanciaPeople.png`,
  `info.png`, etc.) — se reutilizaron solo los ya existentes
  (`terapia-musical.png`, `angulo-izquierdo.png`, `angulo-arriba.png`,
  `angulo-abajo.png`). La auditoría UX/UI propuso `distanciaPeople.png`
  (junto a "Distancia (r)" en la guía) e `info.png` (junto a "Guía de
  valores") como mejoras opcionales de bajo costo; no se implementaron en
  este bloque porque exigirían reestructurar `frame_GuiaValores` (más
  invasivo que lo demás de este bloque) — quedan documentadas en
  `docs/RESOURCES.md` para un bloque de pulido visual posterior.
- **Pruebas**: validación (todos los campos en 0, coeficiente > 1, caso
  válido); navegación completa a través de la app real
  (`VentanaPrincipal` → Iniciar análisis → Inteligibilidad → Resultados →
  Atrás/Ir al Inicio); los 6 niveles de %ALCons renderizan con su color
  correcto en la nueva pantalla; capturas en 500×800, 1366×768 y 1920×1080;
  sin advertencias de Qt nuevas; PDF generado desde la nueva pantalla; 23
  salones, Sabine/Eyring y %ALCons numérico sin cambios.
- **No incluido a propósito**: responsividad de las 3 columnas del
  formulario (`frame_GuiaValores`/`frame_form`/`frame_escala`) en ventanas
  muy angostas — no se modificó (el `.ui` no se tocó) y no se pudo medir con
  certeza fuera de una pantalla real; queda señalado para revisión.
  Tampoco: rediseño de Módulo 1 o 3, D-016, D-017, limpieza de legacy.

## 2026-10-11 — D-019 implementada: nueva clasificación de %ALCons en modelo, PDF e interfaz

A partir de este bloque, la clasificación de 6 categorías de D-019 es la
**clasificación operativa vigente del software**. Solo cambió la
clasificación cualitativa del %ALCons; no se tocaron fórmulas, el cálculo
numérico, la distancia crítica, RT60 (Sabine/Eyring), el diseño visual del
PDF, la navegación ni ningún otro módulo.

- **`Modelo/alcons2.py::evaluar_alcons`**: umbrales actualizados de
  1,4/5/11,4/24,4/47 a 1,4/4,8/11,4/24,2/46,5 (mismos 6 nombres de
  categoría, misma inclusión del límite superior).
- **`Datos/utils/reportePDF.py::NIVELES_ALCONS`**: mismos umbrales nuevos;
  sin cambios en el diseño visual del reporte.
- **`Vista/ventInteligibilidad.py`**: el panel estático "Escala %ALCons"
  (antes 5 categorías con umbrales 0–2/2–5/5–10/10–15/>15 %, ajenos al
  modelo) se corrige por código — sin tocar `inteligibilidadHabla.ui` ni su
  `.py` generado (mismo criterio que D-011) — para mostrar las 6 categorías
  vigentes, incluyendo un bloque nuevo para "Crítico" que antes no existía
  en esa pantalla.
- **Pruebas**: los 11 límites exactos y 4 valores representativos pedidos
  coinciden con lo esperado en modelo y PDF; barrido de 0–200 % en pasos de
  0,001 sin huecos ni valores sin clasificar; los 23 salones de
  `Datos/salones.py` mantienen `sabine_rt`/`eyring_rt`/%ALCons numérico/Dc
  idénticos a antes de este bloque (ninguno cruza un umbral que cambió, así
  que su clasificación textual tampoco cambió); PDF se sigue generando;
  arranque e imports sin excepciones. Detalle en
  `docs/ALCONS_CLASSIFICATION_REVIEW.md` §15.
- **Documentación**: `docs/DECISIONS.md` (D-019 marcada como implementada;
  D-018 anotada como antecedente de los umbrales que usó antes de D-019),
  `docs/ACOUSTIC_MODEL.md` §5, `docs/REPORTS.md` y `docs/REQUIREMENTS.md`
  actualizados con los nuevos números; `docs/ALCONS_CLASSIFICATION_REVIEW.md`
  actualizada de punta a punta (ya no describe una propuesta pendiente, sino
  la decisión implementada, manteniendo la distinción entre lo que viene de
  la fuente bibliográfica y lo que es decisión operativa del proyecto).
- **No incluido a propósito** (fuera del alcance de este bloque): rediseño
  visual del Módulo 2, Módulo 1, Módulo 3, D-016, D-017, limpieza de
  `Modelo/%alcons.py` (legacy, sin uso, conserva su propia clasificación
  antigua), `print()` de diagnóstico, cualquier otra refactorización.

## 2026-10-11 — Criterio operativo de clasificación del %ALCons (D-019): solo documentación

Ningún archivo de código, `.ui` ni PDF se modificó. Se registró el análisis
metodológico y la decisión en `docs/ALCONS_CLASSIFICATION_REVIEW.md` (nuevo)
y `docs/DECISIONS.md` (D-019): el equipo aprobó un criterio operativo de 6
categorías para el %ALCons (límites 1,4/4,8/11,4/24,2/46,5), distinguiendo
explícitamente qué proviene de la fuente bibliográfica consultada (Duran
Uron et al., 2025) y qué es decisión propia del proyecto (cierre de huecos
entre categorías, categoría "Crítico"). **No implementado todavía**: el
código (`Modelo/alcons2.py`), el PDF (`Datos/utils/reportePDF.py`) y el
panel estático del formulario de Inteligibilidad siguen con sus escalas
actuales, ya documentadas como distintas entre sí. Notas de coherencia
añadidas (sin cambiar lo que describen) en `docs/ACOUSTIC_MODEL.md` §5,
`docs/REPORTS.md` y `docs/REQUIREMENTS.md` (RF-07). Se registró además,
como fuente de referencia para futuras investigaciones (sin usarla para
justificar esta decisión), el documento de Rodríguez Barraza y Jimeno
Martínez (2020) sobre el Bloque H. El Bloque 2 (Inteligibilidad, UI) sigue
en pausa hasta que se apruebe la implementación (ver `docs/HANDOFF.md`).

## 2026-09-19 — UX-07: estandarización visual de los reportes PDF

Solo `Datos/utils/reportePDF.py` (más documentación). Sin cambios en fórmulas,
RT60/Sabine/Eyring/%ALCONS/Peutz, resultados, estructuras de datos, nombres
públicos, firmas, flujo de guardado ni número de páginas de los casos normales
(3, 4 y 1). Sistema descrito en `docs/REPORTS.md`; decisión D-018.

- **Encabezado único** `_header` (logo blanco `logoBN.png` a la izquierda,
  título, subtítulo y fecha en líneas separadas): el logo ya no se superpone a
  la fecha (antes x 504–536 sobre x 427–540). Sirve a RT, Inteligibilidad y
  variantes futuras.
- **Marca de agua retirada** del flujo; `_marca_agua` se conserva documentada
  y sin uso.
- **%ALCONS de 6 niveles** (Excelente/Buena/Regular/Pobre/Mala/Crítico) con
  los límites de `docs/ACOUSTIC_MODEL.md` §5; antes la barra tenía 5 niveles
  hasta 20 %. `_bloque_alcons` compartido por el reporte independiente y la
  página 4 del RT. Se añadió el color del 6.º nivel (Crítico).
- **Ancho útil común (468 pt)** para tablas, tarjetas y filetes (antes
  490/440/468/480/546); tipografía, márgenes y espaciados en constantes.
- **Tablas**: columnas proporcionales, texto ajustado con `simpleSplit` (antes
  truncado a 28/22 caracteres), paginación con encabezado repetido (antes 25
  filas invadían el pie), filas de referencia 500/1000/2000 Hz resaltadas
  completas.
- **Identificación del aula** (`Tipo`, `aulas`) en la ficha y el subtítulo solo
  si existen en los datos.
- **Ortografía**: tildes y signos en los textos propios; unidades (m, m², m³,
  s, %) y decimales uniformes (solo al imprimir).
- **Conclusión**: caja con relleno uniforme y alto calculado (antes el texto
  quedaba a ~4 pt del borde inferior).
- **Semáforo** con ✓/✗ dibujados con trazos de ReportLab (sin emojis).
- `Recursos/estilos/paleta.py`: los colores institucionales del PDF se
  derivan de ahí.
- **Cambios de texto a revisar**: "≤ 0.8 s" pasó a "menor o igual a 0.8 s"
  (Helvetica estándar no tiene `≤`); el %ALCONS "Crítico" ahora tiene su propio
  color. Los parámetros del cálculo se imprimen con unidad.
- Pruebas (`docs/TESTING.md`, punto 8): 23 salones y casos de contenido largo
  sin desbordes ni solapes; números del PDF idénticos al modelo; escala
  idéntica a `evaluar_alcons` en 288 valores; revisión visual rasterizada.
- No incluido a propósito: feedback al guardar (D-017).

## 2026-09-18 — Módulo 1 (Tiempo de Reverberación): pantalla de resultados y flujo de guardado

Cierre visual del recorrido Inicio → Formulario RT → Resultados → Guardar
PDF. El formulario RT no se modificó (verificado píxel a píxel contra una
captura previa) y pasa a ser la referencia visual. Los ajustes se hicieron por
código (criterio de la entrada del 2026-09-14); la única excepción es la
eliminación de una declaración inválida en `vistaGraficaRT.ui` (ver
"Ajustes finales"). No se tocó el modelo acústico: los
resultados de los 23 salones (`sabine_rt`, `eyring_rt`, reporte de
inteligibilidad y detalle) son idénticos a los del commit anterior
(comparados salón por salón).

### Problemas corregidos (P1)

- **Flujo bloqueado** (`Modelo/calculoRT2.py`, `graficar_rt60`): el
  `plt.show()` abría una ventana extra de matplotlib y bloqueaba la
  aplicación hasta cerrarla (backend `qtagg`, medido en pantalla real). Se
  eliminó; el gráfico ya se muestra dentro de la pantalla a partir del
  buffer. Solo presentación: datos y curvas idénticos.
- **Resultado principal oculto** (`Vista/ventGraficaRT.py`): la pantalla
  abría en la pestaña de Inteligibilidad de un acordeón y el resultado de
  RT (tabla, Tr MID, veredicto, conclusión) quedaba colapsado. El acordeón
  se reemplazó por una columna de tarjetas en orden de importancia:
  veredicto → Tr MID → tabla por banda → conclusión → inteligibilidad. Se
  reutilizaron los widgets existentes (`tableRT`, `labelIndicador`,
  `indicador`, `labelResumeSabine`, `labelConclusion`, `labelAlcons`,
  `labelEvaluacion`); el acordeón heredado queda oculto, sin eliminarse.
- **Regresión propia de la fase de responsividad** (`ventGraficaRT.py`,
  `ventInfoBD.py`): `setStretchFactor(frameMedium, 1)` sobre los stretch 1
  y 1 del `.ui` dejó barra superior, contenido y barra inferior en 1:1:1
  (bandas vacías enormes). Ahora barras a 0 y contenido a 1, también en
  Base de Datos.
- **Veredicto ÓPTIMA / NO ÓPTIMA**: antes un cuadro de color diminuto. Ahora
  tarjeta destacada con icono (✓ `controlar.png` / ✗ `cruz.png`), texto
  grande y criterio visible (Tr MID ≤ 0.8 s, BB93); no depende solo del
  color. El criterio matemático no cambió.
- **Ventanas pequeñas**: a menos de 1100 px el gráfico y el panel se
  apilan (antes miniatura ilegible y panel cortado); a menos de 560 px el
  pie usa botones compactos. La altura del gráfico sigue a su ancho
  (misma relación de aspecto) sin losa blanca alrededor.

### Mejoras (P2)

- Tr MID en dos mosaicos con cifra destacada; el borde de cada uno repite
  el color de su curva en el gráfico. La tabla se restiló al tema oscuro
  del formulario, sin edición ni selección, y resalta las bandas 500, 1000
  y 2000 Hz que alimentan el Tr MID; su alto sigue siendo el de sus filas.
- Inteligibilidad: aplicada → tarjeta con `%ALCONS` grande, categoría y
  explicación; no aplicada → nota discreta al final, sin cifra ni acento.
  Icono de módulo reutilizado (`terapia-musical.png`, el de "Iniciar
  análisis").
- Sin emojis en la pantalla (🔊 🗣️ ⚠️ 📊 eliminados).
- Barra superior, botón "Atrás", barra inferior y botón principal tomados
  del formulario RT y centralizados en `Recursos/estilos/estilo.py`
  (`estiloBotonAtras`, `estiloBarraSuperior`, `estiloBarraInferior`,
  `estiloTarjeta`, `estiloTexto`) para reutilizarlos en los módulos 2 y 3.
  "Ir al Inicio" es ahora acción secundaria y "Guardar Reporte PDF" la
  principal (224×34 px, igual que "Iniciar Análisis"). Se quitó el
  chevron que se había puesto en "Ir al Inicio": duplicaba el significado
  de "Atrás".
- Gráfico: la línea roja de 0.8 s aparece rotulada en la leyenda ("Límite
  0.8 s (BB93)") y se guarda a 150 dpi (antes 100) para no verse borroso
  al ampliarse. Título "Reporte Final" → "Resultados del análisis" con
  subtítulo (y aula, si viene de la Base de Datos).
- Constantes nuevas reutilizando valores ya presentes: `paleta.py`
  (`TEXTO_PRINCIPAL/SECUNDARIO`, `ESTADO_OPTIMO/NO_OPTIMO` = verde menta y
  rojo suave de la paleta categórica, `SERIE_SABINE/EYRING` = colores del
  gráfico) y `tipografia.py` (`TITULO_PANTALLA`, `VALOR`).

### Pruebas

Flujo real formulario → cálculo → resultados → Atrás / Ir al Inicio →
Guardar PDF (diálogo simulado; cancelar no crea archivo) con y sin
inteligibilidad y con el backend por defecto de matplotlib (sin
bloqueo); tabla y Tr MID coinciden con el modelo; capturas en 1920×1080,
1366×768, 800×600 y 500×400; imports de todos los módulos; arranque real
de la aplicación.

### Ajustes finales (misma fecha)

- **`Unknown property box-shadow`**: lo emitía `Ui_formGraficoRT.setupUi`
  (`Vista/archivos_pyGenerados/vistaGraficaRT.py`, `infoRT.setStyleSheet`,
  17 veces por apertura de resultados), originado en
  `Vista/archivos_qtDesigner/vistaGraficaRT.ui`. `box-shadow` no existe en
  el QSS de Qt (no genera sombra) y `infoRT` es el panel blanco heredado,
  hoy oculto; la declaración nunca tuvo efecto. Se eliminó esa única línea
  en el `.ui` y, a mano y en sincronía, en su `.py` generado (regenerar con
  `uic` 6.11.2 añade ruido de versión; además el `.py` ya difería del `.ui`
  en otras líneas previas: geometrías, `setCurrentIndex`, tamaño del título).
  Comprobado con un manejador de mensajes de Qt (sin silenciar): 0 avisos,
  también en la plataforma real (Wayland). Queda otra ocurrencia en
  `tiempoReverberacionUI2.ui`, `.ui` huérfano que ninguna pantalla carga.
- **Tiempo de Reverberación como un único bloque** (`ventGraficaRT.py`):
  veredicto, Tr MID (Sabine y Eyring), tabla por banda y conclusión viven
  ahora dentro de una sola tarjeta con encabezado "Tiempo de
  Reverberación", separadas por líneas finas. Mismos valores, tamaños,
  tipografía y colores. Inteligibilidad sigue como bloque independiente
  debajo, con su propio encabezado "Inteligibilidad del Habla" (atenuado
  cuando no se calculó) y `%ALCONS` rotulado junto a la cifra.
- **Gráfico centrado verticalmente** con `Qt.AlignVCenter` en el layout
  (antes `AlignTop`); la altura sigue a su ancho, sin cambios de relación de
  aspecto. Matiz: cuando el panel es más alto que la ventana (p. ej.
  1366×768) se centra respecto a todo el contenido, por lo que en la
  primera pantalla queda desplazado hacia abajo. Alternativa si se prefiere
  que siempre se vea completo: alinear arriba solo mientras exista scroll
  (señal `rangeChanged` de la barra vertical).
- Iconos de encabezado: el de Tiempo de Reverberación reutiliza
  `ondas-de-audio.png` y el de Inteligibilidad `terapia-musical.png`, los
  mismos que identifican cada módulo en "Iniciar análisis".

### Diagnóstico (sin implementar): mover y redimensionar la ventana

- Solo `VentanaPrincipal` (`Vista/main.py`) hereda de `VentanaConBarra`
  (`Vista/ventanaBarraTitulo.py`); el resto de pantallas son páginas de su
  `QStackedWidget`. Cambiar `VentanaConBarra` afecta a **una** ventana, no
  a los módulos.
- **Mover**: existe (`mousePressEvent`/`mouseMoveEvent` con `self.move()`),
  pero `move()` no tiene efecto en Wayland (plataforma real de este equipo:
  el compositor decide la posición). Funciona en Windows/X11. La solución
  portable es `windowHandle().startSystemMove()` (disponible en PySide6).
- **Redimensionar**: no existe código. `Qt.FramelessWindowHint` elimina los
  bordes nativos y nada los reemplaza. No es intencional: no hay
  `setFixedSize`; el mínimo (1087×584) sale de los layouts y no hay máximo.
  Portable: `startSystemResize(bordes)` sobre una franja de borde de la
  ventana (los widgets hijos cubren todo el borde, así que haría falta un
  margen pequeño o seguimiento del ratón).
- Hallazgo aparte: `VentanaConBarra.maximizado` inicia en `False` pero la
  app arranca con `showMaximized()`, así que el primer clic en el botón de
  maximizar no hace nada visible y hace falta un segundo para restaurar
  (debería usarse `isMaximized()`).
- Riesgo/tamaño: bajo-medio, ~40 líneas en un solo archivo, sin tocar los
  módulos; solo puede validarse de forma interactiva (arrastrar/redimensionar
  con ratón) en el equipo del usuario. Recomendación: bloque separado.

### Documentación (misma fecha)

Nuevo `docs/RESOURCES.md` (inventario verificado de iconos/GIF/estilos,
reglas, formato para nuevos iconos y lista viva de iconos que podrían
necesitarse). Actualizados: `REQUIREMENTS.md` (requisitos de interfaz
RNF-UI-01 a 11 y de entorno), `DECISIONS.md` (D-011 a D-017),
`CURRENT_STATE.md`, `HANDOFF.md` (próximos pasos), `TESTING.md`
(procedimiento de verificación de UI), `DEPENDENCIES.md` (entorno Linux;
`requirements.txt` sin cambios), `UI_INVENTORY.md` y `MANIFEST.json`.

### Pendiente (P3, no implementado)

- Eje X del gráfico en escala logarítmica (las etiquetas de 125/250 Hz se
  solapan con eje lineal): cambia la apariencia de la figura de la tesis;
  requiere decisión.
- Iconos dedicados de "inicio" y "guardar": hoy ambos botones son solo
  texto. Solo si se aprueba crear recursos nuevos.
- Por debajo de ~420 px de ancho el encabezado desborda unos píxeles.
- `llenar_tabla_resultados` formatea con `:.2f` y fallaría con un valor
  `"Infinito"` (banda sin absorción); es lógica de datos, no se tocó.
- El prefijo `⚠` de los mensajes de validación del formulario RT y de los
  manejadores de objetos (símbolo de texto, no emoji) se dejó: el
  formulario es la referencia.
- Los botones "Ir al Inicio" de Inteligibilidad y Base de Datos aún llevan
  el chevron de la fase anterior; se alinean al patrón al hacer esos
  módulos.

### Propuesta documentada (no implementada): feedback al guardar el PDF

`ReportePDF.reporte_tiempo_reverberacion` (`Datos/utils/reportePDF.py`) no
muestra ningún mensaje al guardar ni al fallar (no hay `try/except`; el
otro reporte, de inteligibilidad, sí informa éxito y error) y devuelve
`None` tanto si se guardó como si se canceló. Propuesta: que devuelva la
ruta (o `None` si se cancela) y que la vista muestre un `QMessageBox` de
éxito ("Reporte guardado en: …") y de error con el mensaje de la
excepción, igual que el reporte de inteligibilidad. Requiere aprobar el
cambio de firma/lógica de esa función.

## 2026-09-14 — UI/UX: responsividad + auditoría profunda de checkbox/ComboBox/navegación

Dos fases de trabajo sobre `Vista/`, aprobadas por bloques pequeños y
verificadas tras cada uno (ver `docs/UI_INVENTORY.md` para el inventario
de `.ui` activos/huérfanos que sirvió de base). No se tocó ninguna
fórmula, cálculo, dato de las 23 aulas, ni la arquitectura MVC+S. No se
modificó ningún `.ui` directamente: todos los ajustes se aplicaron por
código en el controlador correspondiente (`setStyleSheet`/`setIconSize`/
`sizePolicy`/`setAlignment` tras `setupUi`), porque regenerar los `.ui`
con el `pyside6-uic` de este entorno (6.11.2) frente a la versión con la
que fueron generados originalmente (6.5.2) introduce ~28 líneas de ruido
de versión por archivo no relacionado con el cambio real. Queda
`POR VALIDAR` si en el futuro se prefiere absorber ese ruido y editar
los `.ui` directamente en una máquina con Qt Designer funcional.

### Fase 1 — Responsividad (T-UI-01 a T-UI-08)

- Creado `Recursos/estilos/paleta.py`: centraliza colores que estaban
  repetidos como literales (acento `#7ec8f7`, institucionales
  `AZUL_UA`/`NARANJA_UA`, paleta categórica de superficies de Base de
  Datos). `Vista/ventInfoBD.py` pasa a usar estas constantes;
  verificado que los valores resultantes son idénticos a los
  anteriores.
- `Vista/ventGraficaRT.py`: el gráfico de RT ya no se escala a una
  altura fija de 450px; ahora crece con la ventana conservando su
  relación de aspecto (`QSizePolicy.Expanding` + `eventFilter` sobre el
  `QLabel` + stretch factors). La tabla de resultados conserva su
  tamaño fijo a propósito. Se agregó icono a "Ir al Inicio".
- `Vista/ventInfoBD.py`: el contenedor de cards con scroll reclama el
  espacio vertical disponible (stretch factors); se corrigió la ruta
  rota del GIF de transición (`Recursos/gifs/ondas.gif`); icono
  agregado a "Ir al Inicio".
- `Vista/ventInteligibilidad.py`: icono agregado a "Ir al Inicio".

### Fase 2 — Auditoría profunda de UX (bloques UX-B1 a UX-B5)

- **Checkbox** (`Vista/ventTiempoReverberacion.py`): los 6 checkboxes de
  superficie + "Incluir inteligibilidad" solo cambiaban de tinte al
  marcarse (sin glifo de check), a diferencia de "Objetos adicionales"
  que sí mostraba un ✓. Unificados con el mismo icono
  (`Recursos/iconos/controlar.png`) para los 7.
- **ComboBox — flecha** (nuevo): ningún ComboBox de la app mostraba una
  flecha de despliegue propia (solo la nativa de plataforma). Se creó
  `Recursos/iconos/angulo-abajo.png` (y `angulo-arriba.png` para los
  `QSpinBox`/`QDoubleSpinBox`), derivados rotando el `angulo-derecho.png`
  ya existente — mismo trazo, sin recurso arbitrario. Aplicado en
  `tiempoReverberacionUI` (ComboBox principal + `QDoubleSpinBox` de
  inteligibilidad, a pedido explícito), `infoBD` (ComboBox de aula) y
  `estiloObjeto` (ComboBox de cada fila de objeto).
- **ComboBox — popup ilegible** (`Recursos/estilos/estilo.py`,
  `estiloObjeto`): el desplegable de materiales por objeto tenía CSS
  inválido (`rgba(255,255,255)` sin alfa, typo `background: withe`), que
  Qt no podía interpretar (confirmado por el warning
  `QCssParser::parseColorValue` reproducido en ejecución). Corregido al
  mismo esquema oscuro (`#001a4d` + texto blanco) que ya usa el resto de
  la app.
- **Alineación de Inicio** (`Vista/main.py`): el texto "Selecciona una
  opción para comenzar" y los botones "Iniciar Análisis"/"Ayuda" no
  compartían el mismo eje de centrado (120px de diferencia medidos en
  1920×1080). Corregido alineando los tres al centro de la columna;
  verificado en 1920×1080, 1366×768, 800×600 y 500×400 (diferencia final
  ≤17px en todos los casos).
- **Botón "Atrás"** (`Vista/ventInteligibilidad.py`,
  `Vista/ventGraficaRT.py`): tamaño unificado a 42×42 / icono 22×22 en
  toda la app (antes 45×45 con icono 22×22 o 30×30 según pantalla); se
  corrigió además que Gráfica RT tenía un `border-radius` que lo hacía
  ver menos circular que el resto.
- **Botón "Iniciar Análisis"** (`Vista/ventInfoBD.py`,
  `Vista/ventInteligibilidad.py`, `Vista/ventTiempoReverberacion.py`):
  ancho renderizado unificado a 224×34px exacto en las tres pantallas
  (fijar solo `min-width`/`max-width` no bastaba porque el `padding`
  propio de cada pantalla se sumaba de forma distinta; se fijó `padding`
  junto con el ancho). Se agregó un estado `:pressed` con el acento azul
  propio del botón (antes caía al `:pressed` genérico blanco/oscuro de
  la barra inferior) y `:disabled` donde faltaba.
- **Tipografía**: creado `Recursos/estilos/tipografia.py` (tamaños con
  nombre `TITULO`/`SUBTITULO`/`CUERPO`/`AUXILIAR`, sin aplicación
  masiva). Aplicado solo en dos puntos concretos: el texto introductorio
  de Inicio (9pt → 11pt) y las etiquetas "Objetos adheridos" de Base de
  Datos (8pt → 9pt, para igualarlas con el resto de etiquetas
  secundarias de esa misma pantalla).

### Verificación (ambas fases)

Tras cada bloque: imports completos de todos los módulos sin error,
arranque real de la aplicación maximizada sin excepciones, comprobación
en múltiples tamaños de ventana (1920×1080, 1366×768, 800×600, 500×400
según el caso), y verificación de que `sabine_rt`, `eyring_rt`,
`%ALCONS` y el total de 23 salones no cambiaron respecto a los valores
de referencia de sesiones anteriores.

## 2026-09-13 — Correcciones puntuales (mejoras #1-#3 del ranking de auditoría)

### Corregido

- `Datos/salones.py`: `obtener_salones()` no recibía `salonTipo3` ni
  `salonTipo19` (ya definidos en el archivo, con sus datos intactos).
  La lista `salones` pasaba de 21 a 23 elementos. Verificado:
  `len(salones) == 23` y tipos 1-23 sin huecos. No se modificaron los
  datos internos de ningún salón.
- `Modelo/calculoRT2.py` (`agregar_areas_materiales`): se agregó el
  `raise` faltante antes del `ValueError` que validaba que el área de
  objetos adheridos no supere el área de la superficie. Verificado:
  (a) un caso inválido ahora lanza `ValueError` correctamente; (b) el
  caso válido de referencia (`DiccionarioRecibido`) produce
  `sabine_rt`, `eyring_rt` y `reporte_inteligibilidad` idénticos byte
  a byte a los obtenidos con el código anterior al cambio (comparado
  contra el commit previo). Ninguna fórmula fue modificada.
- `Controlador/Controlador.py` (`obtener_coeficientes_materiales`): se
  agregó una verificación de `None` para `materiales_dos` (mismo
  patrón ya usado en `obtener_lista_materiales`), evitando un
  `AttributeError` no controlado si la carga del Excel de coeficientes
  falla. Verificado: el camino feliz (Excel cargado) produce
  exactamente los mismos resultados que antes; el camino de fallo
  simulado (`materiales_dos = None`) ahora degrada a `{}` en vez de
  lanzar una excepción sin manejar. No se cambiaron coeficientes ni la
  fuente de datos (Excel).

### Verificación

- Smoke test de imports de todos los módulos de `Vista`, `Controlador`,
  `Modelo`, `Datos`: sin errores.
- Arranque de `Vista/main.py`: sin excepciones, ventana creada
  correctamente.

## 2026-09-12 — Entorno reproducible en Linux/SteamOS

### Confirmado

- Punto de entrada real: `Vista/main.py`. Ejecución equivalente a la
  configuración de PyCharm (`WORKING_DIRECTORY=Vista`,
  `ADD_CONTENT_ROOTS=true`): `cd Vista && PYTHONPATH=.. python main.py`.
- Dependencias directas confirmadas por auditoría de imports: PySide6,
  pandas, openpyxl (motor de `pandas.read_excel` para `.xlsx`),
  matplotlib, reportlab.
- Entorno probado: Python 3.13.15, PySide6 6.11.2, pandas 3.0.5,
  openpyxl 3.1.5, matplotlib 3.11.2, reportlab 5.0.1.
- Se creó `requirements.txt` en la raíz con estas versiones fijadas.

### Corregido

- `Modelo/excel.py`: las rutas a `Datos/coeficientes.xlsx` y
  `Datos/coefs_absorcion.xlsx` usaban separadores `\\` (Windows)
  incrustados en la cadena, lo que impedía localizarlos en Linux. Se
  cambió a segmentos separados en `os.path.join` (sin alterar nombres
  de variables ni lógica). Verificado: ambos Excel cargan correctamente
  en Linux tras el cambio.

### Pendiente / observado (no modificado en esta tarea)

- `Vista/ventInfoBD.py:392` y `Vista/ventInfoBD2.py:155` referencian
  `"Recursos/estilos/iconos/ondas.gif"`, ruta inexistente (el archivo
  real es `Recursos/gifs/ondas.gif`). Bug preexistente independiente
  del sistema operativo; no bloquea el arranque de la aplicación.
  POR VALIDAR con el equipo antes de corregirlo.
- `prueba.py` sigue como archivo legacy (PyQt5, `Recursos.MainWindow`
  inexistente); no se tocó.

## 2026-09-12 — Baseline para Claude Code

### Confirmado

- Repositorio actual: Room Acoustic.
- Bloque H: 23 tipos de salón.
- Datos de salones: diccionarios Python.
- Coeficientes: Excel.
- Inteligibilidad: Peutz/%ALCons.
- Word vigente identificado como `proyectoGradoSoftware.docx`.

### Auditoría inicial del snapshot

- Aplicación principal basada en PySide6.
- `Modelo/alcons2.py` es usado por la ventana de inteligibilidad.
- `Modelo/calculoRT2.py` es usado por el controlador de RT.
- Existen implementaciones alternativas/legacy.
- No hay suite de pruebas automatizadas.
- No existe `requirements.txt` ni `pyproject.toml`.

### Pendiente

- Verificar default branch real de GitHub.
- Crear pruebas de caracterización.
- Resolver/registrar duplicación de modelos.
- Auditar rutas de recursos.
- Formalizar dependencias.
- Revisar y actualizar capturas de la tesis cuando cambie la UI.
