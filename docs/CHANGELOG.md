# Changelog

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
