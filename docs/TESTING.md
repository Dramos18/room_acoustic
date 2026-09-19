# Testing Strategy

## Situación actual

El snapshot no contiene una suite automatizada.

Esto debe corregirse progresivamente antes de grandes refactorizaciones.

## Nivel 1 — Smoke test

Verificar: - la aplicación inicia; - la ventana principal abre; - la
navegación funciona; - no hay errores de importación; - recursos
gráficos se cargan.

## Nivel 2 — Pruebas unitarias acústicas

Prioridad: - áreas; - absorción; - Sabine; - Eyring; - distancia
crítica; - %ALCons; - clasificación.

## Nivel 3 — Casos de referencia

Crear casos conocidos del proyecto académico.

Cada caso debe registrar: - entradas; - resultado esperado; -
tolerancia; - fuente.

## Nivel 4 — Integración

Verificar: - UI → cálculo; - cálculo → resultados; - resultados → PDF; -
datos Excel → cálculo; - diccionarios de salones → análisis.

## Nivel 5 — Regresión

Cada bug importante debe convertirse en una prueba para evitar que
vuelva a aparecer.

## Regla

Un refactor de una función de cálculo sin prueba equivalente debe
considerarse incompleto.

## Verificación manual reproducible de UI (2026-09-18)

Mientras no exista `tests/`, cada bloque de UI se verifica así (las capturas
usan la plataforma `offscreen`, sin abrir ventanas):

1. **Imports**: importar todos los módulos de `Vista`, `Controlador`,
   `Modelo`, `Datos` y `Recursos.estilos` sin errores.
2. **Arranque real**: `cd Vista && PYTHONPATH=.. ../.venv/bin/python main.py`
   (`timeout 6`; código 124 = sigue vivo en el loop de eventos, sin
   excepciones).
3. **Flujo real del Módulo 1** (sin forzar el backend de matplotlib para
   detectar bloqueos): abrir `VentanaTiempoReverberacion` dentro de un
   `QStackedWidget`, escribir dimensiones, `botonIniciarAnalisis.click()`,
   comprobar que aparece `VentanaGraficaRT`; con y sin
   `checkInteligibilidadOpcion`; navegar con `botonAtras`/`botonGoHome`;
   guardar con `QFileDialog.getSaveFileName` simulado (comprobar cabecera
   `%PDF-`) y cancelar (no crea archivo).
4. **Resultados numéricos**: la tabla y los Tr MID coinciden con
   `calcular_resultados`; comparar `sabine_rt`, `eyring_rt`, reporte de
   %ALCONS y `detalle` de los 23 salones contra el commit anterior
   (`git show HEAD:Modelo/calculoRT2.py` cargado como módulo aparte,
   `MPLBACKEND=Agg`).
5. **Capturas** con `widget.grab().save(...)` a 1920×1080, 1366×768,
   800×600 y 500×400 (y `scrollAreaWidgetContents.grab()` para ver el
   contenido completo). Casos: no óptima con y sin inteligibilidad y óptima
   (Salón tipo 5 o 12). Tras reconstruir tarjetas, procesar los borrados
   diferidos (`sendPostedEvents(None, QEvent.DeferredDelete)`) para evitar
   fantasmas que no existen en la aplicación real.
6. **Advertencias de Qt**: instalar `qInstallMessageHandler` con
   `traceback.format_stack()` y recorrer el flujo; el resultado esperado es
   ninguna advertencia (sin redirigir ni silenciar la terminal).
7. **Regresión visual del formulario**: comparar píxel a píxel la captura del
   formulario antes y después (`PIL.ImageChops.difference`).

8. **Reportes PDF** (`docs/REPORTS.md`; `MPLBACKEND=Agg`, `QT_QPA_PLATFORM=offscreen`,
   `QFileDialog.getSaveFileName` y `QMessageBox.exec` simulados): generar (a) RT sin
   IH (3 páginas), (b) RT con IH (4), (c) solo IH (1), (d) salón de la BD con
   `Tipo`/`aulas`, (e) contenido largo (materiales largos, 4 objetos adheridos
   por superficie, 25 objetos adicionales, `Tipo` largo) y (f) los 23 salones.
   Con un `Canvas` instrumentado comprobar: páginas esperadas, todo el contenido
   dentro de los márgenes laterales y sobre el pie, sin solapes de texto ni en
   el encabezado, y sin `...` en contenido. Comprobar que los números del PDF
   (tabla RT, Tr MID, %ALCONS, clasificación) coinciden con `calcular_resultados`
   y que `_nivel_alcons` coincide con `AlconsCalculator.evaluar_alcons` en un
   barrido (límites 1.4, 5, 11.4, 24.4 y 47 incluidos). Rasterizar con
   `QtPdf` (`QPdfDocument.render`) y revisar; en esta máquina requiere
   `libgssapi_krb5.so.2` (ver `docs/DEPENDENCIES.md`), usada solo vía
   `LD_LIBRARY_PATH` para el análisis.

Limitaciones: mover/redimensionar la ventana y el diálogo de guardado real
solo pueden validarse de forma interactiva en el equipo del usuario.

