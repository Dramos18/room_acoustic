# ACOUSTIC MODEL

> Documento crítico. No modificar ecuaciones o supuestos sin validación.

## Variables
`V` volumen [m³]; `S` superficie [m²]; `α` coeficiente de absorción; `A` absorción equivalente [m² sabin]; `RT60` [s]; `r` distancia [m]; `Q` directividad; `Dc` distancia crítica; `R` constante de sala; `%ALCons`.

## Sabine
Forma estándar:

```text
RT60 = 0.161 V / A
A = Σ(αᵢ Sᵢ)
```

Debe verificarse la constante y la implementación vigente.

## Eyring
Forma estándar:

```text
RT60 = 0.161 V / [-S ln(1 - ᾱ)]
```

Debe verificarse contra el código y la referencia académica definitiva.

## Bandas documentadas
125, 250, 500, 1000, 2000 y 4000 Hz.

## %ALCons
El proyecto utiliza el modelo de Peutz. El documento académico identifica RT, volumen, distancia, directividad, distancia crítica, constante de sala, superficie y absorción media.

**Pendiente crítica:** auditar y registrar aquí la ecuación exacta usada por el código y los umbrales definitivos de clasificación.

## Parámetros de referencia documentados
- frecuencia: 2000 Hz;
- distancia: 1,5 m;
- Q = 2;
- RT60 > 0.

## Validación
Cada caso debe registrar aula, volumen, superficies, materiales, coeficientes, valores esperados/obtenidos, error, fuente y estado.

## Regla
Toda discrepancia entre Word, código, referencias y resultados se registra; no se corrige silenciosamente.
