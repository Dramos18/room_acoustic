# Changelog

## 2026-09-12 — Baseline para Claude Code

### Confirmado

- Repositorio actual: Run Acoustic.
- Bloque H: 23 tipos de salón.
- Datos de salones: diccionarios Python.
- Coeficientes: Excel.
- Inteligibilidad: Peutz/%ALCons.
- Word vigente identificado como `proyectoGradoSoftware.docx`.

### Auditoría inicial del snapshot

- Aplicación principal basada en PySide6.
- `Modelo/alcons2.py` es usado por la ventana de inteligibilidad.
- `Modelo/calculoRT2.py` es usado por el controlador de RT.
- Existen implementaciones alternativas/legacy.
- No hay suite de pruebas automatizadas.
- No existe `requirements.txt` ni `pyproject.toml`.

### Pendiente

- Verificar default branch real de GitHub.
- Crear pruebas de caracterización.
- Resolver/registrar duplicación de modelos.
- Auditar rutas de recursos.
- Formalizar dependencias.
- Revisar y actualizar capturas de la tesis cuando cambie la UI.
