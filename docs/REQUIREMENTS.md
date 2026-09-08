# REQUIREMENTS

## Requisitos funcionales iniciales

| ID | Funcionalidad | Descripción | Estado |
|---|---|---|---|
| RF1 | Seleccionar módulo | TR, Inteligibilidad o Base de Datos | POR VALIDAR |
| RF2 | Dimensiones | Registrar largo, ancho y alto | POR VALIDAR |
| RF3 | Materiales | Asociar materiales/coefs. a superficies | POR VALIDAR |
| RF4 | Objetos adheridos | Incorporar elementos que modifican absorción | POR VALIDAR |
| RF5 | Objetos adicionales | Incorporar elementos independientes | POR VALIDAR |
| RF6 | Inteligibilidad desde TR | Ejecutar %ALCons asociado a RT | POR VALIDAR |
| RF7 | Inteligibilidad independiente | Calcular %ALCons con parámetros propios | POR VALIDAR |
| RF8 | Base de datos | Seleccionar aula del Bloque H | POR VALIDAR |
| RF9 | PDF | Generar reporte con resultados y gráficos | POR VALIDAR |

## Cálculos
RT60 mediante Sabine y Eyring. El documento académico describe bandas de 125 Hz a 4000 Hz.

%ALCons mediante el modelo de Peutz incorporado al proyecto.

## Validaciones documentadas
- dimensiones > 1 m;
- área de objetos ≤ área de superficie;
- coeficientes de absorción en [0,1];
- campos obligatorios no vacíos;
- RT60 > 0;
- referencia de 2000 Hz;
- distancia de referencia 1,5 m;
- Q = 2.

## Criterios documentados
RT: error <10 % en al menos tres aulas de referencia.

Inteligibilidad: error ≤5 % frente a referencias del Bloque H.

Estos son criterios documentados, no resultados demostrados.

## No funcionales iniciales
- RNF01 Usabilidad.
- RNF02 Validación.
- RNF03 Consistencia entre resultados/gráficos/PDF.
- RNF04 Mantenibilidad.
- RNF05 Portabilidad.
- RNF06 Rendimiento.
- RNF07 Trazabilidad en GitHub.

Los umbrales cuantitativos de rendimiento están pendientes.
