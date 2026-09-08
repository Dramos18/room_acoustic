# PROJECT CONTEXT

## Identidad
**Título:** Software para evaluar la acústica en aulas: tiempo de reverberación e inteligibilidad de la palabra.

**Autores:** Daniel Josue Ramos Sandoval y Emanuel Antonio Montilla Villanueva.

**Institución:** Universidad del Atlántico — Facultad de Ingeniería — Ingeniería Industrial.

**Contexto:** aulas de clase, inicialmente tomando como referencia el Bloque H de la Universidad del Atlántico.

## Propósito
Desarrollar una herramienta computacional para evaluar condiciones acústicas de aulas mediante parámetros como RT60 e inteligibilidad de la palabra, utilizando modelos acústicos y datos geométricos/materiales.

## Alcance documentado
- ingreso manual de dimensiones;
- selección de materiales;
- objetos adicionales;
- cálculo RT60;
- Sabine y Eyring;
- %ALCons;
- base interna de aulas del Bloque H;
- gráficos y tablas;
- reportes PDF;
- navegación por módulos;
- ayuda.

El documento académico describe 23 tipos de aulas del Bloque H.

## Fuera del alcance actual
- adquisición automática mediante sensores;
- integración obligatoria con bases externas;
- intervención física automática;
- optimización automática de materiales;
- análisis de auditorios, teatros o espacios abiertos.

## Tecnologías documentadas
Python, PySide6, Qt Designer, PyCharm, Matplotlib, NumPy y ReportLab. La lista definitiva debe verificarse contra el código.

## Arquitectura conceptual
- Modelo: cálculos y lógica acústica.
- Vista: interfaz.
- Controlador: interacción entre vista y lógica.
- Datos: materiales y aulas.
- Recursos: elementos estáticos.

## Objetivos
1. Algoritmos de RT e inteligibilidad.
2. Interfaz intuitiva para entrada y visualización.
3. Validación mediante referencias y mediciones reales.
4. Personalización del análisis y salida.

## Visión futura
La lógica acústica debe poder reutilizarse posteriormente en otros clientes, incluida una posible aplicación móvil. Esto no significa que la app móvil forme parte del alcance actual.
