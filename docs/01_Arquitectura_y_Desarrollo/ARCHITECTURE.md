# Architecture

## Arquitectura declarada

El proyecto académico adopta el patrón Modelo-Vista-Controlador (MVC).

## Estructura actual observada

``` text
Controlador/
Datos/
Modelo/
Recursos/
Vista/
```

### Modelo

Contiene cálculos y acceso a datos relacionados con: - RT60; - Sabine; -
Eyring; - %ALCons; - lectura de Excel; - estructuras acústicas.

Archivos relevantes: - `Modelo/calculoRT2.py` - `Modelo/calculoRT.py` -
`Modelo/alcons2.py` - `Modelo/%alcons.py` - `Modelo/excel.py` -
`Modelo/modelo.py`

### Controlador

Archivos principales: - `Controlador/Controlador.py` -
`Controlador/controlTR.py`

El controlador conecta datos, cálculos y vistas.

### Vista

Contiene: - ventanas PySide6; - lógica de interacción; - widgets; -
gráficos; - navegación; - integración con reportes.

### Datos

- `Datos/salones.py`: diccionarios de los salones.
- `Datos/*.xlsx`: coeficientes acústicos.
- `Datos/utils/reportePDF.py`: generación/soporte de reportes.

### Recursos

- iconos;
- GIF;
- estilos;
- recursos de interfaz.

## Qt Designer

La carpeta `Vista/archivos_qtDesigner/` contiene archivos `.ui`.

La carpeta `Vista/archivos_pyGenerados/` contiene Python generado desde
Qt Designer.

Regla: `.ui` → generación → `.py` generado → controlador/lógica de
ventana.

No invertir esta relación.

## Arquitectura objetivo

A mediano plazo se busca separar mejor: - dominio acústico; - acceso a
datos; - servicios de reporte; - presentación; - navegación.

Sin embargo, no se hará una migración arquitectónica masiva mientras el
comportamiento actual no esté cubierto por pruebas mínimas.

## Principio de refactorización

Primero caracterizar comportamiento; después refactorizar.

Una mejora arquitectónica debe conservar: - fórmulas; - nombres públicos
importantes; - contratos de datos; - resultados esperados; -
comportamiento visible salvo que la tarea pida cambiarlo.
