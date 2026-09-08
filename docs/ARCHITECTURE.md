# ARCHITECTURE

## Arquitectura conceptual
El proyecto utiliza una adaptación de MVC:

```text
Usuario
  ↓
Vista / UI
  ↓
Controlador
  ├── Modelo acústico
  │     ├── Sabine
  │     ├── Eyring
  │     └── %ALCons
  └── Datos
        ├── Materiales
        └── Aulas Bloque H
  ↓
Resultados → gráficos/tablas → PDF
```

## Organización actual conocida
```text
Controlador/
Datos/
Modelo/
Recursos/
Vista/
```

### Controlador
Coordina interfaz y lógica.

### Datos
Materiales, coeficientes, aulas y utilidades de datos.

### Modelo
Lógica acústica y cálculos.

### Vista
Ventanas y elementos relacionados con Qt Designer.

### Recursos
Iconos, estilos, imágenes y recursos estáticos.

## Módulos acústicos conocidos
La estructura previamente identificada incluye módulos relacionados con:
- `calculoRT.py`
- `calculoRT2.py`
- `alcons2.py`
- `%alcons.py`
- `modelo.py`
- `excel.py`

La duplicación y dependencia exacta deben auditarse antes de refactorizar.

## Arquitectura objetivo
Separar progresivamente:
- dominio acústico;
- presentación;
- datos;
- reportes;
- infraestructura UI.

La meta es reutilizar la lógica acústica en una futura aplicación móvil sin copiarla. No implica desarrollarla ahora.

## Regla
Primero auditar; después definir interfaces; luego refactorizar gradualmente.
