# Development Workflow

## Flujo recomendado

### 1. Preparar

``` bash
git status
git branch --show-current
git remote -v
git log -5 --oneline
```

### 2. Entender

Leer documentación y abrir los archivos involucrados.

### 3. Planificar

Para cambios medianos/grandes: - objetivo; - archivos; - riesgos; -
pruebas; - impacto académico.

### 4. Implementar

Hacer cambios pequeños y coherentes.

### 5. Verificar

``` bash
git diff
```

Ejecutar pruebas y smoke test correspondiente.

### 6. Documentar

Actualizar: - CHANGELOG; - CURRENT_STATE; - INTEGRATION; - DECISIONS; -
otros documentos afectados.

### 7. Commit

Ejemplos:

``` text
feat: improve acoustic analysis validation
fix: validate attached object area
refactor: isolate RT calculation service
test: add Peutz reference cases
docs: update acoustic model traceability
ui: improve intelligibility results view
```

### 8. Push

El usuario decide cuándo sincronizar cambios con GitHub.

## Trabajo con Claude Code

Para edición local inmediata: 1. abrir el repositorio local; 2. iniciar
Claude Code desde la raíz; 3. permitirle leer el repositorio; 4. pedir
cambios; 5. revisar `/diff`; 6. ejecutar la aplicación/pruebas; 7.
decidir commit/push.

Claude Code puede operar en terminal, IDE y desktop, y entiende el
estado de Git del directorio de trabajo.

## Web vs local

Claude Code web trabaja sobre una copia en la nube y ramas aisladas. Es
útil para tareas delegables y PRs.

Para tu objetivo de editar el proyecto y ver cambios inmediatamente en
PyCharm/desktop, el modo local es el flujo principal.
