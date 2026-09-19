# Reportes PDF

Guía para trabajar en `Datos/utils/reportePDF.py`. Los reportes se generan con
ReportLab (canvas, fuentes estándar Helvetica) y se invocan desde
`Vista/ventGraficaRT.py` (RT) y `Vista/ventInteligibilidad.py` (%ALCONS). El
sistema visual quedó estandarizado el 2026-09-19 (UX-07); no cambia ninguna
fórmula ni resultado, solo presentación.

## Tipos de reporte

| Método (firma sin cambios) | Contenido | Páginas |
|---|---|---|
| `ReportePDF.reporte_tiempo_reverberacion(self, resultados)` | RT60 (Sabine/Eyring) y, si `resultados["reporte_inteligibilidad"]` no es `None`, %ALCONS | 3 (sin IH) o 4 (con IH) |
| `ReportePDF.reporte_inteligibiliad(self, reporte)` (sic) | Solo %ALCONS | 1 |

El número de páginas es el de siempre para casos normales. Solo crece si el
contenido no cabe (p. ej. muchas filas de objetos): entonces se abre una página
de continuación (ver "Paginación"). Cualquier reporte nuevo (p. ej. Base de
Datos) debe reutilizar los mismos ayudantes.

## Estructura de páginas (reporte RT)

1. **Ficha del Salón**: identificación (solo si existe), dimensiones,
   materiales de las superficies, objetos adicionales.
2. **Resultados de RT60**: gráfica Sabine vs Eyring (250 pt de alto) y tabla
   numérica.
3. **Análisis Acústico**: Tr MID, semáforo, cómo interpretar, conclusión.
4. **Evaluación de la Inteligibilidad** (opcional): `_bloque_alcons`.

El reporte independiente de Inteligibilidad es la misma página 4 con el mismo
encabezado y `_bloque_alcons`.

## Patrón visual

- Paleta institucional derivada de `Recursos/estilos/paleta.py` (`AZUL_UA`,
  `NARANJA_UA` vía `_rgb`). Los demás colores son propios del PDF (más oscuros,
  pensados para impresión) y se dejan en el módulo.
- Geometría (constantes al inicio del módulo): carta 612×792 pt, `MARGEN` =
  72, **`ANCHO_UTIL` = 468 pt** (todo el contenido usa este ancho), inicio de
  contenido `Y_INICIO`, límite inferior `Y_MIN` = 56 (sobre el pie).
- Tipografía: Helvetica. Encabezado 13 pt, título de página `T_H1` 16 pt,
  título de sección `T_SECCION` 12 pt, cuerpo `T_CUERPO` 10 pt, tablas
  `T_TABLA` 8 pt, notas `T_AUX` 8 pt.
- Jerarquía: título de página (azul con filete naranja) > título de sección
  (marca naranja + filete gris) > cuerpo. Todas las páginas comienzan con el
  título de página (`_titulo_pagina`).
- Tarjetas (`_mini_card`/`_fila_cards`): ancho útil repartido en partes
  iguales; valores largos se reducen y pasan a dos líneas.

## Encabezado y pie

`_header(c, width, height, titulo_pagina, fecha_hora, logo_path=None,
subtitulo=None)` es el **único encabezado** de todos los reportes y páginas:

```
[logo blanco]  Título de la página                    (negrita, 13 pt)
               Room Acoustic · Salón tipo N · Aulas X   Generado: dd/mm/aaaa hh:mm
```

Título y (subtítulo + fecha) van en líneas distintas, así que nunca chocan con
el logo ni entre sí; el título baja hasta 10 pt o se recorta con `...` si es
extremadamente largo. Logo: `Recursos/iconos/logoBN.png`. El subtítulo incluye
`Tipo` y `aulas` solo si existen en el diccionario del salón; si no, muestra
"Room Acoustic · Universidad del Atlántico".

`_footer`: filete naranja, "Software de Evaluación Acústica — Universidad del
Atlántico | Página N de M". `M` se calcula con una pasada previa
(`_contar_paginas`).

## Marca de agua

`_marca_agua` **ya no se usa** en ningún reporte (atravesaba tablas y tarjetas).
La función y `Recursos/iconos/isotipoUA.png` se conservan como recurso; la
identidad institucional la da el logo del encabezado.

## Ayudantes compartidos

`_Doc` (cursor vertical `y`, paginación, encabezado/pie automáticos),
`_titulo_pagina`, `_seccion` / `_seccion_titulo`, `_parrafos` (ajuste con
`simpleSplit`), `_fila_cards` / `_mini_card`, `_tabla`, `_caja_conclusion`,
`_semaforo`, `_barra_nivel`, `_bloque_alcons`, `_tabla_rt`, y utilidades de
texto `_lineas`, `_recortar`, `_num`, `_cantidad`.

## Tablas

- `_tabla(doc, columnas, filas, ...)`: ancho = `ANCHO_UTIL`, columnas
  proporcionales `(título, proporción, alineación)`, encabezado azul, filas
  alternas, relleno de 4 pt. Números a la derecha, texto a la izquierda.
- **Sin truncar por número de caracteres**: el texto se mide con `stringWidth`
  y se divide con `simpleSplit` en las líneas necesarias (la fila crece).
  `...` solo aparece si un texto necesita más de 24 líneas.
- Tabla larga: si la fila no cabe se abre una página de continuación
  ("… (continuación)" en el encabezado) y se repite la fila de títulos. Nada
  invade el pie ni sale del área imprimible.
- `_tabla_rt`: las filas de 500, 1000 y 2000 Hz (referencia del Tr MID) llevan
  un tinte azul en toda la fila y texto en negrita.

## %ALCONS: escala de 6 niveles

`NIVELES_ALCONS` reproduce exactamente `AlconsCalculator.evaluar_alcons`
(`docs/ACOUSTIC_MODEL.md` §5; límites superiores inclusivos): Excelente ≤ 1.4,
Buena ≤ 5, Regular ≤ 11.4, Pobre ≤ 24.4, Mala ≤ 47, Crítico > 47.
`_nivel_alcons(valor)` da el nivel; `_barra_nivel` dibuja seis segmentos con
nombre y rango, el activo a color completo y un marcador con el valor.
**Si el modelo cambia sus límites, hay que actualizar `NIVELES_ALCONS`**; la
prueba de barrido (`docs/TESTING.md`, punto 8) lo detecta. La clasificación
textual mostrada es la que devuelve el modelo, sin reescribirla.

## Unidades y decimales

m, m², m³, s, Hz, % con espacio antes de la unidad. Dimensiones, áreas, Tr,
%ALCONS, Dc y R con 2 decimales; factor de directividad con 1 y coeficiente
medio de absorción con 3 (`_FORMATO_PARAMETROS`). Cantidades de objetos sin
decimales cuando son enteros. Solo se formatea al imprimir: los valores del
modelo no se alteran.

## Identificación del aula

Los salones de la Base de Datos traen `Tipo` (p. ej. "Salón tipo 1") y `aulas`
("101-104"). Si existen se muestran en la tarjeta "Identificación del Salón" de
la página 1 y en el subtítulo del encabezado; si no existen (flujo de
formulario) no se muestra nada ni se inventan datos. No se modificó ninguna
estructura de datos.

## Ortografía

Los textos propios del reporte llevan tildes y signos (Evaluación, Página,
Atlántico, Clasificación, Parámetros, ¿Qué…?, Crítico…) con Helvetica estándar
(Latin-1). Helvetica no tiene `≤`, por eso el texto dice "menor o igual a".
Los textos que vienen del modelo se imprimen tal cual (solo se quita el prefijo
`■` heredado si aparece).

## Decisiones visuales (UX-07)

- Logo blanco (`logoBN.png`) en la banda azul; sin marca de agua.
- Semáforo con ✓/✗ dibujados con trazos de ReportLab (sin emojis ni imágenes)
  y texto ÓPTIMA / NO ÓPTIMA: no depende solo del color.
- Caja de conclusión con altura calculada a partir del texto (relleno
  uniforme arriba y abajo).
- El guardado no cambió: mismo diálogo, mismos mensajes. El feedback del
  reporte RT sigue pendiente (D-017).

## Cómo probar

Ver `docs/TESTING.md` (procedimiento de PDF): generar los casos, comprobar
páginas, márgenes, solapes, números y escala, y rasterizar para revisión visual.
