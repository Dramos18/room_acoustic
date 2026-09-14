"""
Escala tipográfica de referencia para room_acoustic.

La auditoría de UI/UX encontró más de 15 tamaños de fuente distintos en
uso simultáneo, sin un patrón de jerarquía reconocible (título/
subtítulo/cuerpo/auxiliar), y con unidades mezcladas (`px` en Tiempo de
Reverberación, `pt` en el resto).

Este módulo no migra toda la aplicación de una sola vez — sería un
rediseño, no una mejora incremental. Define los tamaños con nombre para
que las pantallas que se toquen de ahora en adelante los reutilicen en
vez de inventar un número nuevo, y para los dos ajustes puntuales que sí
se aplican en esta fase (ver `docs/CHANGELOG.md`): el texto introductorio
de Inicio y las etiquetas de sección de Base de Datos, ambos
demasiado pequeños para su función.

Expresados en puntos (`pt`), que es la unidad ya dominante en los `.ui`
de las pantallas afectadas.
"""

TITULO = 20      # título de sección dentro de una pantalla
SUBTITULO = 13   # subtítulo / texto destacado
CUERPO = 11      # texto de orientación al usuario, valores importantes
AUXILIAR = 9     # etiquetas secundarias, metadatos, contadores
