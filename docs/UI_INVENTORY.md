# UI Inventory

## Navegación observada

La aplicación utiliza ventanas/widgets PySide6 y un `QStackedWidget` en
la ventana principal.

## Ventana principal

`Vista/main.py`

Funciones observadas: - ventana principal; - GIF/logo; - navegación
hacia análisis; - botón de inicio; - estructura de páginas.

El botón de Ayuda aparece pendiente de conexión en el snapshot.

## Inicio de análisis

`Vista/ventIniciarAnalisis.py`

Actúa como punto de navegación hacia los análisis.

## Tiempo de Reverberación

`Vista/ventTiempoReverberacion.py`

Integra: - captura de datos; - superficies; - objetos; - cálculo; -
navegación; - estilos; - resultados.

## Gráficas

`Vista/ventGraficaRT.py`

Integra visualización de resultados RT.

## Inteligibilidad

`Vista/ventInteligibilidad.py`

Integra: - validación; - cálculo mediante `AlconsCalculator`; -
resumen; - generación de PDF.

## Base de datos

`Vista/ventInfoBD.py` `Vista/ventInfoBD2.py`

Relacionadas con consulta/visualización de información de aulas.

## UI generada

`Vista/archivos_pyGenerados/`

Contiene clases `Ui_*` generadas a partir de `.ui`.

## Diseños fuente

`Vista/archivos_qtDesigner/`

Contiene: - ventana principal; - barra de título; - inicio; -
información BD; - inteligibilidad; - objetos; - RT; - gráficas; -
utilidades.

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
