# Naming and Traceability

## Objetivo

Garantizar que un identificador usado en un archivo pueda rastrearse de
forma segura en los demás archivos donde se referencia.

## Regla general

**Existente = conservar por defecto.**

La calidad de un nombre no se evalúa aislada: se evalúa por su costo de
migración y su impacto en trazabilidad.

## Antes de renombrar

Claude debe:

1.  buscar el identificador globalmente;
2.  distinguir definición de referencia;
3.  revisar imports;
4.  revisar atributos;
5.  revisar claves de diccionarios;
6.  revisar señales/slots y nombres de widgets si aplica;
7.  revisar documentación;
8.  revisar strings que puedan funcionar como claves de integración;
9.  actualizar todas las referencias;
10. ejecutar pruebas.

## Renombramientos permitidos

### Bajo riesgo

Variables estrictamente locales no expuestas fuera de una función.

### Medio

Funciones internas con pocas referencias.

### Alto

- clases;
- funciones importadas;
- atributos compartidos;
- claves de diccionario;
- nombres de widgets;
- archivos;
- APIs internas;
- nombres usados en reportes;
- nombres usados por la tesis.

Los de alto riesgo requieren explicación y validación.

## Ejemplos actuales que requieren respeto

- `AlconsCalculator`
- `calcular_alcons`
- `calcular_dc`
- `tr_2000Hz`
- `volumen_sala`
- `factor_directividad`
- `distancia_critica`
- `superficie_total`
- `coef_medio_absor`
- `VentanaInteligibiliad`

Un nombre poco ideal no debe cambiarse automáticamente.

## Regla de documentación

Cuando un identificador sea renombrado deliberadamente, documentar:

``` text
Anterior → Nuevo
Motivo
Archivos afectados
Referencias actualizadas
Pruebas ejecutadas
```
