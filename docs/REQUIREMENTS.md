# Requirements

## Funcionales

### RF-01 — Evaluación de tiempo de reverberación

El sistema debe permitir ingresar/obtener: - dimensiones; -
superficies; - materiales; - objetos adheridos; - objetos adicionales.

Debe calcular RT60 por bandas.

### RF-02 — Métodos acústicos

Debe soportar: - Sabine; - Eyring.

### RF-03 — Bandas

Bandas actuales: - 125 Hz; - 250 Hz; - 500 Hz; - 1000 Hz; - 2000 Hz; -
4000 Hz.

### RF-04 — Inteligibilidad

Debe permitir calcular %ALCons mediante el modelo de Peutz.

### RF-05 — Parámetros de Peutz

La implementación actual contempla, entre otros: - distancia; - TR a
2000 Hz; - volumen; - factor de directividad; - distancia crítica; -
superficie total; - coeficiente medio de absorción.

### RF-06 — Base de datos Bloque H

Debe contener los 23 tipos de salón definidos por el proyecto.

### RF-07 — Reportes

Debe permitir generar resultados en PDF.

### RF-08 — Visualización

Debe permitir visualizar resultados acústicos de forma comprensible y
mediante gráficos donde corresponda.

## Validación de entrada

El Word vigente establece, entre otros criterios: - dimensiones mayores
que 1 m; - áreas de objetos no mayores que la superficie disponible; -
coeficientes de absorción entre 0 y 1; - campos obligatorios; - RT60 \>
0; - referencia de 2000 Hz para inteligibilidad; - distancia de
referencia 1.5 m; - Q = 2.

Los criterios exactos deben permanecer alineados con la versión vigente
del Word.

## No funcionales

- Usabilidad.
- Legibilidad.
- Estabilidad.
- Mantenibilidad.
- Trazabilidad.
- Compatibilidad con el entorno Python/PySide6 definido por el proyecto.
- Resultados reproducibles.
- Reportes consistentes.

## Criterios académicos de validación

Según el Word vigente: - error de RT \< 10 % para al menos tres aulas de
referencia; - error de inteligibilidad ≤ 5 % frente a referencias.

Estos criterios no deben relajarse sin una decisión académica explícita.

## Requisitos de interfaz (UI/UX)

Añadidos el 2026-09-18 a partir de la auditoría de UX y del cierre visual del
Módulo 1. Son decisiones del equipo de desarrollo, **no** provienen del Word
vigente: `POR VALIDAR` con el compañero de documentación antes de citarlos
en la tesis. Cada uno indica cómo se verifica (ver `docs/TESTING.md`).

| ID | Requisito | Verificación |
|---|---|---|
| RNF-UI-01 | La pantalla de resultados de RT muestra primero el resultado principal: un único bloque "Tiempo de Reverberación" (veredicto, Tr MID Sabine y Eyring, tabla por banda, conclusión); la inteligibilidad es un bloque independiente debajo | Captura de resultados con y sin inteligibilidad |
| RNF-UI-02 | El veredicto óptima / no óptima se comunica con color + icono (✓ / ✗) + texto, nunca solo con color; el criterio (Tr MID ≤ 0.8 s en Sabine y Eyring) se muestra en pantalla | Captura de un salón óptimo (tipos 5 y 12) y uno no óptimo |
| RNF-UI-03 | Cuando la inteligibilidad no se calculó, se indica claramente sin competir visualmente con el resultado de RT; cuando sí, se muestra `%ALCONS` y su evaluación | Ídem RNF-UI-01 |
| RNF-UI-04 | La pantalla es utilizable de 500×400 a 1920×1080 sin recortes ni scroll horizontal: gráfico y panel lado a lado desde 1100 px de ancho y apilados por debajo; pie compacto por debajo de 560 px | Capturas en 1920×1080, 1366×768, 800×600 y 500×400 |
| RNF-UI-05 | El gráfico crece con la ventana conservando su relación de aspecto y se centra verticalmente; la tabla no crece más allá de sus filas | Capturas; `pixmap` sin deformación |
| RNF-UI-06 | Una acción de guardar/generar no bloquea ni abre ventanas extra: no se llama a `plt.show()` en el flujo de la aplicación | Flujo real con el backend por defecto de matplotlib |
| RNF-UI-07 | Los cálculos acústicos no cambian por ajustes de interfaz | Comparación de los 23 salones contra el commit anterior |
| RNF-UI-08 | Sin emojis como recurso visual; iconografía mínima, coherente y funcional (`docs/RESOURCES.md`) | Búsqueda de emojis en la vista |
| RNF-UI-09 | Sin advertencias de Qt en terminal durante el flujo del Módulo 1 (p. ej. `Unknown property ...`) | Manejador de mensajes de Qt con traza |
| RNF-UI-10 | Estilos, colores y tamaños de texto reutilizables se definen una sola vez en `Recursos/estilos/` (`estilo.py`, `paleta.py`, `tipografia.py`); no se duplican por pantalla | Revisión de código |
| RNF-UI-11 | Componentes consistentes entre módulos: botón "Atrás" 42×42 con icono 22×22, botón principal 224×34 con estados hover/pressed/disabled, flechas de ComboBox/SpinBox, checkbox con ✓ | Inspección de capturas y de `docs/UI_INVENTORY.md` |

Pendiente de definir como requisitos cuando se aprueben: mover y
redimensionar la ventana (ver `docs/HANDOFF.md`) y feedback al guardar el PDF
(propuesta en `docs/CHANGELOG.md`, 2026-09-18).

## Requisitos de ejecución (entorno)

Ver `docs/DEPENDENCIES.md` para versiones y `requirements.txt` para
instalación reproducible. Resumen: Python 3.13, PySide6, pandas, openpyxl,
matplotlib, reportlab. Los ajustes de UI de 2026-09-13/18 **no añadieron
ninguna dependencia**.

## Cambios futuros

Cualquier requisito nuevo debe registrarse antes o durante su
implementación y, cuando corresponda, relacionarse con una prueba.
