# Resources — Iconos y recursos gráficos

Inventario de los recursos gráficos de `room_acoustic` (iconos, GIF y
recursos de estilo definidos en código), verificado contra el código real
el 2026-09-18, más una lista de iconos que podrían necesitarse en el
futuro.

Documentos relacionados: `docs/UI_INVENTORY.md` (pantallas y patrón visual),
`docs/DECISIONS.md` (D-013, regla de iconos) y `docs/CHANGELOG.md`.

## 1. Reglas

1. **No usar iconos arbitrarios.** Antes de reutilizar uno hay que
   preguntarse si realmente representa esa acción o entidad. Si no existe
   un recurso adecuado, no se pone otro para llenar el espacio: se anota
   aquí lo que convendría crear.
2. **Iconografía mínima, coherente y funcional.** Solo iconos de módulo,
   estado (✓ / ✗), navegación y flechas. Sin decoración.
3. **Sin emojis** como recurso visual. Un estado nunca se comunica solo con
   color: color + icono + texto.
4. **Reutilizar antes de crear.** Buscar primero en este documento,
   `Recursos/iconos/` y `Recursos/estilos/`. No duplicar iconos (ya hay
   derivados por rotación: `angulo-abajo`, `angulo-arriba`).
5. Los iconos nuevos los proporciona el equipo (o se aprueban antes de
   crearlos); no se dibujan "a ojo" para salir del paso.
6. No eliminar recursos sin uso aparente sin aprobación explícita:
   pueden estar reservados para otra pantalla (ver sección 6).

## 2. Cómo agregar un icono nuevo

1. Colocar el archivo en `Recursos/iconos/` con el nombre sugerido en la
   sección 7 (o uno equivalente: minúsculas, guiones, sin tildes).
2. Formato: **PNG RGBA con fondo transparente**, trazo **blanco** (`#FFFFFF`)
   de una sola tinta, estilo de línea minimalista como `angulo-*.png`,
   `controlar.png` y `cruz.png` (trazo ~5 px sobre 64 px, extremos
   redondeados, sin sombras ni degradados). Tamaño recomendado 64×64 (o
   256×256, se reduce a 18–30 px al usarse). Fondo oscuro de la aplicación:
   por eso van en blanco.
3. Actualizar la tabla de la sección 8 (registro) o avisar; al integrarlo se
   referencia por código con la ruta relativa `../Recursos/iconos/<archivo>`
   (la aplicación se ejecuta con directorio de trabajo `Vista/`).
4. Registrar la integración en `docs/CHANGELOG.md`.

## 3. Iconos existentes (`Recursos/iconos/`)

Resolución: casi todos 64×64; `agregar`/`quitar` 500×500; `logoBN`/`isotipoUA`
1000×1000; `backIcon` 256×256. "Uso" cuenta solo código activo (no `.ui`
huérfanos ni código muerto).

| Archivo | Representa | Uso actual | Estado |
|---|---|---|---|
| `angulo-izquierdo.png` | Chevron `<` | Botón "Atrás" en todas las pantallas; `botonRegresar` de "Iniciar análisis" | En uso |
| `angulo-derecho.png` | Chevron `>` (es `angulo-izquierdo` girado 180°) | Botones de módulo en "Iniciar análisis" | En uso |
| `angulo-abajo.png` | Chevron `v` (derivado de `angulo-derecho` por rotación) | Flecha de ComboBox (TR, Base de Datos, `estiloObjeto`); flecha "abajo" de SpinBox | En uso (creado 2026-09-14) |
| `angulo-arriba.png` | Chevron `^` (derivado por rotación) | Flecha "arriba" de los `QDoubleSpinBox` de inteligibilidad (TR) | En uso (creado 2026-09-14) |
| `controlar.png` | Check ✓ | Checkbox marcado (TR); estado "ÓPTIMA" en resultados | En uso |
| `cruz.png` | Aspa ✗ grande | Estado "NO ÓPTIMA" en resultados | En uso |
| `cruz-pequena.png` | Aspa pequeña | Botón cerrar de la barra de título | En uso |
| `menos-pequeno.png` | Signo menos | Botón minimizar de la barra de título | En uso |
| `restaurar-ventana.png` | Restaurar/maximizar | Botón maximizar de la barra de título (siempre este, ver sección 7) | En uso |
| `agregar.png` | Signo más | Botón "+" de filas de objetos (adheridos y adicionales) | En uso |
| `quitar.png` | Signo menos | Botón "−" de filas de objetos | En uso |
| `ondas-de-audio.png` | Forma de onda | Tarjeta del Módulo 1 en "Iniciar análisis"; encabezado "Tiempo de Reverberación" en resultados | En uso |
| `terapia-musical.png` | Oído + altavoz | Tarjeta del Módulo 2 en "Iniciar análisis"; encabezado "Inteligibilidad del Habla" en resultados | En uso |
| `logoBN.png` | Logo Universidad del Atlántico (blanco y negro) | Barra de título; tarjeta del Módulo 3 en "Iniciar análisis" | En uso |
| `isotipoUA.png` | Isotipo UA en color | Marca de agua y encabezado de los reportes PDF | En uso |
| `backIcon.png` | Chevron `<` (más grueso, 256 px) | — | Sin uso; parecido a `angulo-izquierdo`, no idéntico |
| `flecha-correcta.png` | Chevron `>` | — | Sin uso; parecido a `angulo-derecho`, no idéntico |
| `frecuencia-de-sonido.png` | Barras de frecuencia | — | Sin uso |
| `mezcla-de-audio.png` | Mezclador con deslizadores | — | Sin uso |
| `microfono.png` | Micrófono | — | Sin uso |
| `sonido.png` | Consola / panel de sonido | — | Sin uso |
| `voz.png` | Cabeza con sonido (voz) | — | Sin uso; candidato natural para inteligibilidad del habla |

## 4. GIF (`Recursos/gifs/`)

| Archivo | Tamaño / frames / peso | Uso actual | Nota |
|---|---|---|---|
| `logoMainGIF.gif` | 1080×1080, 287 fr., 2.9 MB | Logo animado de Inicio (`main.py`) | En uso |
| `gifmicro.gif` | 1100×1100, 179 fr., **13.9 MB** | Transición al abrir el formulario de Tiempo de Reverberación | En uso; muy pesado para mostrarse 120×120 px durante 2 s |
| `ondas.gif` | 500×500, 149 fr., 0.9 MB | Transición al analizar desde Base de Datos | En uso (ruta corregida 2026-09-13) |
| `cerrar-sesion.gif` | 640×640, 44 fr., 141 KB | — | Sin uso |
| `maximizar.gif` | 640×640, 45 fr., 140 KB | — | Sin uso |
| `minimizar.gif` | 640×640, 45 fr., 139 KB | — | Sin uso |

## 5. Recursos definidos en código (`Recursos/estilos/`)

| Módulo | Contenido |
|---|---|
| `paleta.py` | Colores: `ACENTO` `#7ec8f7`, `AZUL_UA` `#00458C`, `NARANJA_UA` `#DE7019`, niveles de blanco (`BLANCO_10/25/45/80`), `TEXTO_PRINCIPAL/SECUNDARIO`, `ESTADO_OPTIMO` `#34d399` / `ESTADO_NO_OPTIMO` `#f87171`, `SERIE_SABINE` / `SERIE_EYRING` (colores de las curvas), paleta categórica de superficies y de objetos adicionales |
| `tipografia.py` | Tamaños con nombre (pt): `TITULO_PANTALLA` 18, `TITULO` 20, `VALOR` 24, `SUBTITULO` 13, `CUERPO` 11, `AUXILIAR` 9 |
| `estilo.py` | Hojas QSS heredadas (`estiloObjeto`, `estiloWarning`, `estiloFrameRT` —no se aplica—, `estiloTree` —sin uso—) y componentes compartidos: `estiloBotonAtras`, `estiloBarraSuperior(nombre)`, `estiloBarraInferior(nombre, primario, compacto)`, `estiloTarjeta(nombre, fondo, borde)`, `estiloTexto(pt, color, negrita)` |

Los `.ui` activos y huérfanos están en `docs/UI_INVENTORY.md`.

## 6. Observaciones

- **Posibles duplicados funcionales** (sin uso, no se eliminan sin
  aprobación): `backIcon.png` respecto de `angulo-izquierdo.png` y
  `flecha-correcta.png` respecto de `angulo-derecho.png`.
- **Siete iconos y tres GIF sin uso** (lista en las secciones 3 y 4);
  `maximizar.gif`/`minimizar.gif`/`cerrar-sesion.gif` parecen pensados para
  la barra de título. Decidir con el bloque de redimensión de ventana.
- **Peso**: `gifmicro.gif` (13.9 MB) se carga al abrir el formulario de RT.
  Candidato a optimizar (menos fotogramas / menor resolución) sin cambiar su
  aspecto a 120×120 px.
- **Resolución mezclada** (64, 256, 500 y 1000 px): funciona porque Qt
  escala, pero conviene unificar los nuevos en 64 o 256 px.
- **Símbolos de texto usados como icono** (no son emojis, pero conviene
  decidir si se reemplazan): `▶` en "Iniciar Análisis" y `?` en "Ayuda"
  (Inicio); `⚠` como prefijo de 6 mensajes de validación (formulario RT y
  manejadores de objetos); `▣ ◧ ◨ ▬ ▲ ◈` como marcas de las tarjetas de
  Base de Datos.
- **Módulo 3**: su tarjeta en "Iniciar análisis" usa `logoBN.png`
  (logo institucional), a diferencia de los módulos 1 y 2, que tienen un
  icono temático.
- El botón maximizar de la barra de título muestra siempre
  `restaurar-ventana.png`; ver `maximizar.png` en la sección 7.

## 7. Iconos que podrían necesitarse (lista viva)

"Necesidad": **Recomendado** = mejora coherencia y conviene cuando se toque
esa pantalla; **Opcional** = solo si se quiere; **Requerido** = hace falta
para completar un bloque de trabajo. Ninguno se crea sin aprobación.

| Nombre sugerido | Dónde se usaría | Hoy | Necesidad | Prioridad |
|---|---|---|---|---|
| `advertencia.png` | Sustituir el prefijo de texto `⚠` de los mensajes de validación (formulario RT y objetos) y avisos | Carácter de texto | Recomendado (coherencia "sin emojis") | Media |
| `base-de-datos.png` | Tarjeta del Módulo 3 en "Iniciar análisis" y encabezado de la pantalla de Base de Datos | `logoBN.png` | Recomendado al hacer el Módulo 3 | Media |
| `maximizar.png` (□) | Botón maximizar de la barra de título, alternando con `restaurar-ventana.png` | Siempre `restaurar-ventana.png` | Requerido cuando se implemente el bloque de ventana (mover/redimensionar/maximizar) | Media (futuro) |
| `inicio.png` (casa) | Botón "Ir al Inicio" (resultados, Inteligibilidad, Base de Datos) | Solo texto | Opcional | Baja |
| `guardar.png` (o `pdf.png`) | Botón "Guardar Reporte PDF" | Solo texto | Opcional (el texto ya es claro) | Baja |
| `ayuda.png` | Botón "Ayuda" de Inicio, cuando se conecte la sección de ayuda | `?` de texto | Opcional | Baja |
| `iniciar.png` (▶) | Botón "Iniciar Análisis" de Inicio | `▶` de texto | Opcional | Baja |
| `informacion.png` | Ayuda contextual junto a criterios (p. ej. Tr MID ≤ 0.8 s) o nota "no calculada" | Tooltip / texto | Opcional | Baja |
| `exito.png` / `error.png` | Mensajes al guardar el reporte (propuesta pendiente en `CHANGELOG.md`) | No hay mensaje | Opcional, ligado a esa propuesta | Baja |
| `aula.png` | Encabezado de sección en Base de Datos | Texto | Opcional | Baja |
| `superficie-*.png` (6) | Marcas de las tarjetas de superficie de Base de Datos | Glifos `▣ ◧ ◨ ▬ ▲` | Opcional | Baja |
| `objetos.png` | Encabezado "Objetos adicionales" | Glifo `◈` | Opcional | Baja |

Iconos existentes sin uso que podrían cubrir alguno de estos casos si el
equipo lo considera adecuado (a decidir, no a asumir): `voz.png`
(inteligibilidad del habla), `microfono.png`, `sonido.png`.

## 8. Registro de iconos aportados

Completar a medida que se agreguen; el asistente los tomará de aquí.

| Fecha | Archivo | Reemplaza / cubre | Integrado en | Estado |
|---|---|---|---|---|
| — | — | — | — | — |
