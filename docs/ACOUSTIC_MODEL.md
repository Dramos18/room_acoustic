# Acoustic Model

## 1. Tiempo de reverberación

El sistema utiliza las ecuaciones de Sabine y Eyring.

### Sabine

``` text
RT60 = 0.161 * V / A
```

donde: - V = volumen del recinto; - A = absorción total.

### Eyring

La implementación trabaja con el coeficiente medio de absorción por
frecuencia y la relación de Eyring.

La ecuación exacta debe mantenerse alineada con el Word vigente y con la
implementación validada.

## 2. Bandas

- 125 Hz
- 250 Hz
- 500 Hz
- 1000 Hz
- 2000 Hz
- 4000 Hz

## 3. Absorción

La absorción se obtiene a partir de: - área; - material; - coeficiente
de absorción; - objetos adheridos; - objetos adicionales.

## 4. Inteligibilidad — %ALCons

El proyecto utiliza el modelo de Peutz.

La implementación observada en `Modelo/alcons2.py` incluye:

``` text
R = (STOT * alpha_promedio) / (1 - alpha_promedio)
Dc = 0.14 * sqrt(Q * R)

Dc_alternativa = 0.21 * sqrt(V / TR_2000Hz)

si r <= 3.16 * Dc:
    %ALCons = (200 * r² * TR²) / (V * Q)
si r > 3.16 * Dc:
    %ALCons = 9 * TR
```

La fórmula anterior representa la implementación observada en el
snapshot y debe seguir contrastándose contra la formulación exacta del
Word vigente antes de cualquier refactor matemático.

## 5. Evaluación cualitativa

`Modelo/alcons2.py` clasifica actualmente (criterio operativo vigente,
D-019, 2026-10-11): - 0–1.4: Excelente; - hasta 4.8: Buena; - hasta 11.4:
Regular; - hasta 24.2: Pobre; - hasta 46.5: Mala; - superior a 46.5: Crítico.

Es una decisión metodológica/operativa del proyecto, no una transcripción
literal de la fuente bibliográfica consultada (que publica 5 categorías con
intervalos no contiguos y sin categoría por encima de 46.5 %); la
justificación completa, la distinción entre lo que viene de la fuente y lo
que es decisión propia, y las pruebas de los límites están en
`docs/ALCONS_CLASSIFICATION_REVIEW.md` y `docs/DECISIONS.md` (D-019). Esto no
implica que la redacción académica definitiva de la tesis esté cerrada.

La clasificación debe tratarse como parte del contrato funcional hasta
que el equipo académico apruebe un cambio.

## 6. Parámetros de referencia

El proyecto establece: - Q = 2 para voz humana frontal; - distancia de
referencia de 1.5 m; - TR de 2000 Hz para el modelo de inteligibilidad.

## Regla crítica

No modificar una ecuación porque “parezca más correcta”. Toda
modificación debe: 1. identificar la fuente; 2. comparar fórmula actual
vs nueva; 3. comparar resultados; 4. actualizar documentación; 5.
validar contra casos de referencia.
