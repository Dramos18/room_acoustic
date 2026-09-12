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

## Regla para capturas de tesis

Las capturas del Word representan una versión concreta del software. Si
cambia la UI, deben actualizarse las capturas afectadas después de
validar la nueva interfaz.

No usar una captura como evidencia de una funcionalidad que ya no
coincide con el software.
