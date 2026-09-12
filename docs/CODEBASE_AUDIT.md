# Codebase Audit — Baseline

## Alcance

Auditoría estática del snapshot `room_acoustic-master.zip` entregado
para configurar el trabajo con Claude.

No constituye una auditoría exhaustiva de comportamiento en ejecución.

## Estructura

``` text
Controlador/
Datos/
Modelo/
Recursos/
Vista/
prueba.py
```

## Hallazgos

### 1. Implementaciones duplicadas

Existen: - `Modelo/%alcons.py` - `Modelo/alcons2.py`

La ventana `Vista/ventInteligibilidad.py` importa `Modelo.alcons2`.

Existen: - `Modelo/calculoRT.py` - `Modelo/calculoRT2.py`

El controlador de RT y la ventana de RT usan `calculoRT2`.

**Recomendación:** no eliminar todavía. Primero comparar comportamiento
y referencias.

### 2. Archivo de prueba legacy

`prueba.py` importa PyQt5 y `Recursos.MainWindow`.

La aplicación principal usa PySide6 y el snapshot no contiene
`Recursos/MainWindow.py`.

**Estado:** probable archivo legacy/de prueba. No eliminar sin
confirmar.

### 3. Validación defectuosa potencial

En `Modelo/calculoRT2.py`, dentro de `agregar_areas_materiales`,
aparece:

``` python
if area_adheridos > area_superficie:
    ValueError(...)
```

La excepción se construye pero no se lanza con `raise`.

**Estado:** bug potencial confirmado por inspección estática. Debe
corregirse mediante una tarea específica y prueba asociada.

### 4. Posible cálculo no utilizado

En `calcular_absorcion_total` se calcula `area_efectiva`, pero la suma
observada utiliza `cantidad * coef`.

**Estado:** requiere análisis funcional antes de modificar.

### 5. Diagnóstico en producción

Hay múltiples `print()` en módulos de cálculo/control.

**Estado:** deuda técnica. Sustituir gradualmente por logging o eliminar
cuando ya no sean necesarios.

### 6. Dependencias

Importaciones observadas incluyen: - PySide6; - pandas; - matplotlib; -
reportlab; - PyQt5 en archivo legacy.

La dependencia real debe formalizarse después de decidir qué código
legacy se conserva.

### 7. Pruebas

No se encontró carpeta `tests/`.

**Estado:** prioridad alta antes de refactorizaciones importantes.

### 8. Rutas

Hay rutas relativas hacia recursos, por ejemplo iconos/GIF.

**Estado:** revisar para que la aplicación no dependa del directorio
actual desde el cual se ejecuta.

## Prioridad sugerida

P0 — reproducibilidad y ejecución  
P1 — pruebas de caracterización  
P1 — rutas de recursos  
P1 — validaciones defectuosas  
P2 — duplicación de modelos  
P2 — limpieza de diagnósticos  
P3 — refactorización arquitectónica mayor
