# UI Inventory

## Navegación observada

La aplicación utiliza ventanas/widgets PySide6 y un `QStackedWidget` en
la ventana principal.

## Ventana principal

`Vista/main.py`

Funciones observadas: - ventana principal; - GIF/logo; - navegación
hacia análisis; - botón de inicio; - estructura de páginas.

El botón de Ayuda ya está conectado (`botonAyuda` → `VentanaAyuda`,
2026-10-11) — ver sección "Ayuda" más abajo.

## Inicio de análisis

`Vista/ventIniciarAnalisis.py`

Actúa como punto de navegación hacia los análisis.

## Tiempo de Reverberación

`Vista/ventTiempoReverberacion.py`

Integra: - captura de datos; - superficies; - objetos; - cálculo; -
navegación; - estilos; - resultados.

## Gráficas / resultados de RT

`Vista/ventGraficaRT.py` (clase `VentanaGraficaRT`; diseño en
`vistaGraficaRT.ui`, `Ui_formGraficoRT`). También la usa el flujo de Base de
Datos.

Estructura (2026-09-18): barra superior (Atrás + "Resultados del análisis" y
subtítulo) · contenido: gráfico | panel · barra inferior ("Ir al Inicio"
secundario, "Guardar Reporte PDF" principal). El panel tiene dos bloques:
"Tiempo de Reverberación" (veredicto, Tr MID Sabine/Eyring, tabla por banda
con las bandas 500/1000/2000 Hz resaltadas, conclusión) e "Inteligibilidad
del Habla" (independiente). Gráfico y panel se apilan por debajo de 1100 px.
El acordeón heredado (`tollboxCombinada`/`stackedWidget`) sigue en el `.ui`,
oculto. Flujo: formulario → `procesar_datos` → `calcular_resultados` →
`VentanaGraficaRT` → `ReportePDF.reporte_tiempo_reverberacion`.

## Inteligibilidad

`Vista/ventInteligibilidad.py` (formulario) + `Vista/ventResultadosInteligibilidad.py`
(resultados, clase `VentanaResultadosInteligibilidad`; bloque M2-UX,
2026-10-11).

Formulario: validación inline (no bloqueante, igual que RT), cálculo
mediante `AlconsCalculator`, navegación a la pantalla de resultados. Sigue
el mismo patrón visual que el Módulo 1 (`estiloBarraSuperior`,
`estiloBotonAtras`, `estiloBarraInferior`; flechas de los 5
`QDoubleSpinBox` corregidas con el mismo QSS que `tiempoReverberacionUI.ui`).

Resultados: pantalla propia (ya no `QMessageBox`), construida en Python sin
`.ui` nuevo (mismo criterio que `VentanaGraficaRT`): %ALCons y categoría en
grande con el color del nivel, escala de 6 segmentos (misma fuente que el
PDF, `Datos/utils/reportePDF.py::NIVELES_ALCONS`), parámetros utilizados,
resultado acústico (Dc, R), botones "Ir al Inicio"/"Guardar Reporte PDF".
Flujo: formulario → `enviar_calculos_inteligibilidad` →
`AlconsCalculator.generar_reporte` → `mostrar_pantalla_resultados` →
`VentanaResultadosInteligibilidad` → `ReportePDF.reporte_inteligibiliad`.

## Base de datos

`Vista/ventInfoBD.py` (activo; `Vista/ventInfoBD2.py` es huérfano, sin
ningún `import` en el repositorio — ver sección "Pantallas/archivos
huérfanos" más abajo).

Cerrado visualmente al patrón de M1/M2 (auditoría + bloque M3-UX,
2026-10-11). Estructura: ComboBox de selección de aula ("Tipo de aula —
Bloque H"), 4 mini-cards de dimensiones (Aulas/Largo/Ancho/Alto), y una
lista de cards dentro de un `QScrollArea` interno (`scrollMateriales`,
scroll solo vertical) con una card por superficie (Frontal/Trasera/
Izquierda/Derecha/Piso/Techo, con sus objetos adheridos si los hay) y una
card de objetos adicionales — construidas dinámicamente en Python
(`_card_superficie`, `_card_objetos_adicionales`, `_fila_objeto` en
`ventInfoBD.py`), no desde el `.ui`.

No tiene pantalla de resultados propia: reutiliza directamente
`VentanaGraficaRT` (la misma de Módulo 1) — al elegir una aula y pulsar
"Iniciar Análisis", el salón pasa por el mismo `Controlador/controlTR.py::
procesar_datos`/`Modelo/calculoRT2.py` que usa RT, y se muestran los mismos
resultados (RT60, Tr MID, %ALCons si el salón trae `inteligibilidad`) y el
mismo PDF, con `Tipo`/`aulas` identificando el salón en el subtítulo.

Validación: si no se selecciona ninguna aula, un mensaje inline junto al
ComboBox ("⚠ Seleccione un tipo de aula de la base de datos") lo indica —
no bloqueante, desaparece en cuanto se elige una opción válida (mismo
patrón que `labelErrorInteligibilidad` del Módulo 2).

Navegación: "Atrás" (vuelve a "Iniciar análisis") e "Ir al Inicio" (vuelve
al índice 0) en el pie, junto a "Iniciar Análisis" — el botón "Ir al
Inicio" no existía antes del bloque M3-UX; se construyó en Python sobre el
pie ya generado por el `.ui` (sin editarlo), mismo criterio que D-011 y que
el pie de `VentanaResultadosInteligibilidad`.

Pendiente real: el icono de la tarjeta de este módulo en "Iniciar análisis"
sigue siendo `logoBN.png` (genérico/institucional), no uno temático como
`ondas-de-audio.png` (M1) o `terapia-musical.png` (M2) — ver
`docs/RESOURCES.md` (`base-de-datos.png`, recomendado, aún sin aportar por
el equipo). También quedan, de menor prioridad, sin resolver: `frameTop`/
`frameBottom` con QSS propio en vez de los helpers de `estilo.py` (difieren
en detalles — opacidades, padding — que impiden migrarlos sin cambiar algo
visualmente), y un `QScrollArea` externo que envuelve todo el formulario
(cabecera incluida) además del interno de las cards — hoy inofensivo (no
se activa en ningún tamaño probado), ver auditoría de cierre del Módulo 3.

## Ayuda

`Vista/ventAyuda.py` (clase `VentanaAyuda`; sin `.ui` nuevo, construida en
Python puro — mismo criterio que `VentanaGraficaRT`/
`VentanaResultadosInteligibilidad`). V1 implementada 2026-10-11; instanciada
una sola vez desde `Vista/main.py` y agregada al `stackedWidget` igual que
`VentanaIniciarAnalisis` (se reutiliza, no se reconstruye en cada clic: su
contenido no depende de ningún cálculo).

Estructura: cabecera (`estiloBarraSuperior`, botón "Atrás" solo visible
dentro de un tema, migas de pan "Ayuda › <sección>") · contenido: un
`QStackedWidget` interno propio con 7 páginas (menú + 6 secciones) · pie
(`estiloBarraInferior`, botón único "Volver al Inicio" — a diferencia de
M1/M2/M3, Ayuda solo se entra desde el Inicio, así que "Atrás" y "Volver al
Inicio" no serían la misma acción redundante si se duplicaran).

Menú principal: grid de 6 tarjetas clicables (`_TarjetaTema`, acento lateral
de color, hover/pressed reales), responsivo de verdad (3→2→1 columnas según
el ancho de contenido disponible, no una grilla fija que solo se encoge).
Íconos de módulo solo en Tiempo de Reverberación/Inteligibilidad
(`ondas-de-audio.png`/`terapia-musical.png`, los mismos que ya identifican
esos módulos en el resto de la app) — deliberadamente sin ícono en Base de
Datos: `logoBN.png` se ve ilegible a tamaño de ícono pequeño, mismo motivo
ya señalado para la tarjeta de M3 en "Iniciar análisis" (ver
`docs/RESOURCES.md`).

Secciones: "Cómo empezar" (stepper de 5 pasos, horizontal en pantallas
anchas/vertical en angostas, con un panel de descripción único que cambia
al seleccionar un paso — no 5 tarjetas sueltas); "Tiempo de Reverberación",
"Inteligibilidad", "Base de Datos" y "Resultados y PDF" comparten un mismo
componente de flujo Entrada → Procesamiento → Resultado (`_FlujoEtapas`),
para que las 4 páginas de módulo tengan una composición consistente en vez
de bloques de texto distintos cada una; "Acerca del proyecto" (información
institucional mínima, solo lo que el repositorio respalda — sin autores,
versión ni año inventados). La escala de %ALCons de la sección
Inteligibilidad se construye directamente desde
`Datos/utils/reportePDF.py::NIVELES_ALCONS` (misma fuente que D-019 y el
PDF), sin duplicar los umbrales numéricos aquí.

No se tocó M1, M2, M3, el modelo acústico, D-019, el PDF ni D-016
(`Vista/ventanaBarraTitulo.py`) para implementar Ayuda.

Pendiente, señalado a propósito para una fase posterior (no bloqueante):
revisar la consistencia visual de fondo/superficie, transparencias y
bordes entre los componentes de Ayuda y el resto de la app — algunos
elementos se sienten más integrados al lenguaje visual real que otros; y
ampliar el contenido de cada sección.

## UI generada

`Vista/archivos_pyGenerados/`

Contiene clases `Ui_*` generadas a partir de `.ui`.

## Diseños fuente

`Vista/archivos_qtDesigner/`

Contiene: - ventana principal; - barra de título; - inicio; -
información BD; - inteligibilidad; - objetos; - RT; - gráficas; -
utilidades.

## Patrón visual de referencia (Módulo 1 — Tiempo de Reverberación)

El formulario RT y su pantalla de resultados son la referencia para los
módulos 2 (Inteligibilidad) y 3 (Base de Datos). No se busca que todas las
pantallas sean idénticas, sino que compartan estos elementos:

| Elemento | Definición (centralizada) |
|---|---|
| Fondo | Degradado azul oscuro del `.ui`; tarjetas translúcidas |
| Barra superior | `estilo.estiloBarraSuperior(nombre)`; título 18 pt en negrita + subtítulo 9 pt (`tipografia.TITULO_PANTALLA`, `AUXILIAR`) |
| Botón "Atrás" | `estilo.estiloBotonAtras`; 42×42, icono `angulo-izquierdo.png` 22×22 |
| Barra inferior | `estilo.estiloBarraInferior(nombre, primario)`; secundario con contorno tenue, principal con acento `#7ec8f7`, 224×34 |
| Tarjeta | `estilo.estiloTarjeta(nombre)`; texto con `estilo.estiloTexto(pt, color, negrita)` |
| Colores | `paleta.py` (acento, texto principal/secundario, estado óptimo/no óptimo) |
| Tamaños de texto | `tipografia.py` (`VALOR` 24, `CUERPO` 11, `AUXILIAR` 9) |
| Flechas de ComboBox/SpinBox | `angulo-abajo.png` / `angulo-arriba.png` |
| Checkbox marcado | `controlar.png` |
| Estado de resultado | color + icono (✓ `controlar.png`, ✗ `cruz.png`) + texto, nunca solo color |
| Iconos de módulo | `ondas-de-audio.png` (RT), `terapia-musical.png` (Inteligibilidad) |
| Sin emojis | Se usan iconos de `Recursos/iconos/` o solo texto |
| Responsivo | Ancho < 1100 px: columnas apiladas; < 560 px: pie compacto |
| Ajustes por código | Los `.ui` no se modifican (ver `CHANGELOG.md`, 2026-09-14) |

Regla de iconos: antes de usar un icono existente preguntarse si
realmente representa esa acción o entidad; si no, no se pone otro solo para
llenar el espacio (se documenta el recurso que convendría crear). Preferir
iconografía mínima: iconos de módulo, estado (✓/✗), navegación y flechas.

Reglas para nuevas pantallas: reutilizar antes de crear (buscar en
`Recursos/estilos/` y `Recursos/iconos/`); barras superior/inferior a
stretch 0 y contenido a stretch 1; un `QLabel` con pixmap necesita un
ancho mínimo explícito para poder encogerse.

Recursos gráficos (iconos, GIF, constantes de estilo) y lista de iconos por
crear: `docs/RESOURCES.md`.

## Inventario .ui → .py generado → controlador (auditoría UI/UX 2026-09-13)

Verificado por inspección directa del XML de cada `.ui` y por búsqueda de
referencias en todo el código Python (no por el nombre del archivo).

### Pantallas activas (en uso por algún flujo real de la app)

| `.ui` | `.py` generado | Controlador que lo usa | Notas |
|---|---|---|---|
| `barraTitulo.ui` | `archivos_pyGenerados/barraTitulo.py` | `Vista/ventanaBarraTitulo.py` | Barra de título custom (frameless) |
| `ventanaPrincipal.ui` | `archivos_pyGenerados/ventanaPrincipal.py` | `Vista/main.py` | Ventana principal |
| `iniciarAnalisis.ui` | `archivos_pyGenerados/iniciarAnalisis.py` | `Vista/main.py`, `Vista/ventIniciarAnalisis.py` | Menú de navegación a los 3 análisis |
| `tiempoReverberacionUI.ui` | `archivos_pyGenerados/tiempoReverberacionUI.py` | `Vista/ventTiempoReverberacion.py` | Formulario de Tiempo de Reverberación |
| `inteligibilidadHabla.ui` | `archivos_pyGenerados/inteligibilidadHabla.py` | `Vista/ventInteligibilidad.py` | Formulario de Inteligibilidad |
| `infoBD.ui` | `archivos_pyGenerados/infoBD.py` | `Vista/ventInfoBD.py` | Base de Datos — versión de **cards**, la que realmente se navega desde "Iniciar análisis" |
| `vistaGraficaRT.ui` | `archivos_pyGenerados/vistaGraficaRT.py` | `Vista/ventGraficaRT.py` | Pantalla de resultados (gráfico + tabla + %ALCons) |
| `objetoSuperficie.ui` | `archivos_pyGenerados/objetoSuperficie.py` (generado pero **no se usa**) | `Vista/manejadorObjetos.py` | Se carga el `.ui` **directamente en tiempo de ejecución** vía `QUiLoader` (no usa la clase `Ui_*` generada) |
| `objetoAdicional.ui` | `archivos_pyGenerados/objetoAdicional.py` (generado pero **no se usa**) | `Vista/manejadorObjetoAdicional.py` | Igual que arriba: `QUiLoader` en tiempo de ejecución |

### Pantallas/archivos huérfanos (sin `.py` generado y/o sin ningún import en el código)

| `.ui` | `.py` generado | ¿Referenciado en algún controlador? | Estado |
|---|---|---|---|
| `infoBD2.ui` | — (no existe) | No | Huérfano. El controlador `Vista/ventInfoBD2.py` sí existe pero usa `archivos_pyGenerados/infoBD.py` (el mismo `Ui_Form` que la versión activa), **no** `infoBD2.ui`; además referencia `self.ui.treeWidget`, atributo que ya no existe en el `Ui_Form` actual (solo tiene `contenedorCards`). `ventInfoBD2.py` no está importado por ningún flujo activo. |
| `iniciarAnalisis2.ui` | — (no existe) | No | Huérfano |
| `objetoAdicional2.ui` | — (no existe) | No | Huérfano |
| `objetoSuperficie2.ui` | — (no existe) | No | Huérfano |
| `tiempoReverberacionUI2.ui` | — (no existe) | No | Huérfano |
| `ventanaPrincipal2.ui` | — (no existe) | No | Huérfano |
| `userUtilidades.ui` | — (no existe) | No | Huérfano, sin flujo asociado conocido |
| `inteligibilidadHabla2.ui` | `archivos_pyGenerados/inteligibilidadHabla2.py` (sí generado) | No | Generado pero ningún controlador lo importa; código muerto |
| `MainWindow.ui` | — (no existe) | Solo referenciado por `prueba.py` (legacy PyQt5, fuera de la app) | Fuera de alcance de la app PySide6 |

Ninguno de estos archivos se modificó, eliminó ni completó en esta
fase. Antes de tocarlos en el futuro, se requiere una decisión de
producto explícita: completar el rediseño "2", archivarlos, o
eliminarlos (ver `docs/DECISIONS.md`).

## Regla para capturas de tesis

Las capturas del Word representan una versión concreta del software. Si
cambia la UI, deben actualizarse las capturas afectadas después de
validar la nueva interfaz.

No usar una captura como evidencia de una funcionalidad que ya no
coincide con el software.
