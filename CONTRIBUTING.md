# Desarrollo

Requisitos: Python 3.12, uv 0.13.5, Node 24, pnpm 11.25.0 y GNU Make.
Los locks fijan las dependencias resueltas; no editarlos a mano.

```bash
make setup
make check
```

Leer [el estado actual](docs/status/current.md), la arquitectura y la ficha antes
de elegir una tarea. Usar ramas `feat/…`, `fix/…` o `docs/…` y cambios pequeños.
Una PR explica comportamiento, comprobaciones ejecutadas y límites pendientes.
Actualizar contratos y ejemplos juntos. `make docs-sync` regenera las tres tablas
derivadas; `make verify-spec` detecta divergencias sin corregirlas automáticamente.

Para actualizar dependencias de manera intencional, cambiar pyproject.toml o
web/package.json, regenerar con `uv lock` o `pnpm --dir web install --lockfile-only`
y revisar el diff antes de volver a ejecutar `make setup` y `make check`.

No hay tareas de integración, E2E o despliegue implementadas todavía. No agregar
targets vacíos que devuelvan éxito. Las pruebas de bootstrap y documentación no
demuestran que las estrategias, la seguridad operativa o la contabilidad funcionen.
