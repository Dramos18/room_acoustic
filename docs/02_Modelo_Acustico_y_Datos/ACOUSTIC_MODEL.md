# Modelo acústico

## 1. Tiempo de reverberación

El motor de reverberación implementa los métodos de Sabine y Eyring por bandas de frecuencia.

### Sabine

```text
RT60 = 0.161 · V / A
```

Donde V es el volumen del recinto (m³) y A es el área de absorción equivalente total (m² sabin), calculada para cada banda.

### Eyring

```text
RT60 = -0.161 · V / (S · ln(1 - ᾱ))
```

Donde S es el área total de las superficies del recinto (m²) y ᾱ es el coeficiente medio de absorción de la banda. La implementación debe respetar el dominio matemático del logaritmo y los casos límite; no interpretar un resultado no finito como un tiempo numérico válido.

## 2. Bandas de frecuencia

El procesamiento utiliza seis bandas de octava:

- 125 Hz
- 250 Hz
- 500 Hz
- 1000 Hz
- 2000 Hz
- 4000 Hz

## 3. Absorción acústica

La absorción equivalente se construye a partir de las áreas, los coeficientes de absorción tabulados y los elementos presentes en el recinto:

- material base de cada superficie;
- objetos adheridos, cuya área se descuenta de la superficie base y se contabiliza con su propio material;
- objetos adicionales, contabilizados según la cantidad y el coeficiente asociado.

Los perfiles y sus limitaciones de trazabilidad se documentan en `ACOUSTIC_DATA_CATALOG.md`. El flujo de procesamiento y los archivos responsables se describen en `MODULES_SPECIFICATION.md`.

## 4. Inteligibilidad del habla — %ALCons (Peutz)

La implementación activa se encuentra en `Modelo/alcons2.py`, clase `AlconsCalculator`.

### 4.1 Constante del recinto

```text
R = (S_TOT · ᾱ) / (1 - ᾱ)
```

Donde S_TOT es la superficie total del recinto y ᾱ el coeficiente medio de absorción. La implementación rechaza ᾱ = 1.

### 4.2 Distancia crítica activa

```text
Dc = 0.21 · √(V / TR_2000Hz)
```

Esta es la expresión que utiliza actualmente `generar_reporte()` al llamar a `calcular_dc()`. V es el volumen del recinto y TR_2000Hz el tiempo de reverberación a 2000 Hz.

El código también contiene `calcular_distancia_critica(Q, R)`, que calcula:

```text
Dc' = 0.14 · √(Q · R)
```

Esta segunda expresión **no está activa en el flujo de generación del reporte**: la llamada correspondiente permanece comentada. No se deben presentar ambas expresiones como equivalentes ni intercambiarlas sin una decisión metodológica y pruebas de impacto.

### 4.3 Cálculo por tramos

El criterio de transición confirmado para la implementación del proyecto es **3.16 · Dc**:

```text
si r ≤ 3.16 · Dc:
    %ALCons = (200 · r² · TR²) / (V · Q)
si r > 3.16 · Dc:
    %ALCons = 9 · TR
```

Donde:
- r: distancia entre emisor y oyente (m);
- TR: tiempo de reverberación a 2000 Hz (s);
- V: volumen del recinto (m³);
- Q: factor de directividad (2 para voz humana frontal, según los parámetros establecidos por el proyecto);
- Dc: distancia crítica activa definida en §4.2.

El umbral 3.16 es el criterio adoptado para el software y coincide con la implementación existente en `AlconsCalculator.calcular_alcons()`. La decisión se registra en D-020. El documento académico debe utilizar el mismo criterio al describir la versión evaluada.

### 4.4 Clasificación cualitativa

La clasificación operativa de seis niveles se encuentra implementada en el modelo, la interfaz y los reportes:

| Intervalo de %ALCons | Clasificación |
|---|---|
| 0 ≤ x ≤ 1.4 | Excelente |
| 1.4 < x ≤ 4.8 | Buena |
| 4.8 < x ≤ 11.4 | Regular |
| 11.4 < x ≤ 24.2 | Pobre |
| 24.2 < x ≤ 46.5 | Mala |
| x > 46.5 | Crítico |

Es una decisión operativa del proyecto: toma los límites superiores publicados por la fuente secundaria revisada, cierra los intervalos no definidos y añade la categoría Crítico. No debe atribuirse literalmente a la fuente bibliográfica. El análisis de procedencia y limitaciones está en `ALCONS_CLASSIFICATION_REVIEW.md`; la decisión formal, en D-019.

## 5. Parámetros de referencia

El flujo documentado del proyecto establece:
- Q = 2 para voz humana frontal;
- distancia de referencia = 1.5 m en los perfiles que la especifican;
- TR de referencia = 2000 Hz para el cálculo de inteligibilidad.

Los valores particulares de cada perfil se encuentran en `Datos/salones.py` y se inventarían en `ACOUSTIC_DATA_CATALOG.md`.

## 6. Trazabilidad y limitaciones metodológicas

- El umbral 3.16 · Dc se adopta como criterio de implementación y se registra en D-020. La fuente académica secundaria identificada en `ALCONS_CLASSIFICATION_REVIEW.md` describe el mismo criterio por tramos y lo atribuye a Peutz a través de una referencia intermedia.
- La ecuación de Dc activa (0.21 · √(V/TR_2000Hz)) está identificada por inspección directa del código. La ecuación alternativa (0.14 · √(Q·R)) está definida pero no se utiliza en el flujo activo.
- La revisión bibliográfica disponible no permitió verificar carácter por carácter las ecuaciones de Dc y R en la fuente primaria original; las fórmulas aparecen como imágenes en el documento secundario. La procedencia primaria debe completarse antes de afirmar una validación bibliográfica exhaustiva.
- La validez experimental de los resultados requiere mediciones independientes; no se deduce de que la aplicación ejecute las ecuaciones.

## 7. Regla de control de cambios

No modificar una ecuación, constante, banda o parámetro por intuición. Todo cambio debe:
1. identificar y conservar la fuente bibliográfica;
2. comparar explícitamente la formulación actual y la propuesta;
3. analizar el dominio de aplicación y las unidades;
4. calcular el impacto sobre casos de referencia y los 23 perfiles;
5. actualizar código, pruebas, decisiones y documentación académica de forma coordinada;
6. registrar las limitaciones y la evidencia de validación.
