# Renders verificados

12 SVG con fuentes incrustadas. Fuente canónica: docs/diagrams/*.mmd.
Mermaid CLI 12.2.0 y Chromium 153.0.8010.0 (@sparticuz/chromium 153.0.0).
El lock del renderer está en ../renderer/. No es una dependencia del producto.

Reproducción: instalar ese lock con `npm ci --ignore-scripts` en un directorio temporal,
proveer un Chromium local compatible y ejecutar desde la raíz:

```sh
uv run --frozen python tools/render_diagrams.py --mmdc /ruta/node_modules/.bin/mmdc --chromium /ruta/chromium --output audit/g-design/diagrams-final
```

No se descargan navegadores desde el script. En esta sesión se extrajo el binario Brotli
incluido en el paquete de Chromium a /tmp, verificando su tamaño completo (209022176 bytes).
El SHA256 del binario es 53a15d6c3a3d27dfb54c4ba60278b1683136f70cf1e67e989da7dfbd3d451ef0.
El modo --no-sandbox se usó sólo para renderizar fuentes locales inspeccionadas en un entorno
aislado de QA; no es configuración de despliegue de TD. No abrir contenido remoto con ese modo.

render.json conserva comandos y hashes de esta ejecución; visual-review.json, un nivel arriba,
conserva las 12 revisiones. Abrir el SVG con zoom para el ER vertical. Fuentes incrustadas evitan
recortes de labels por sustitución tipográfica. Las capturas son auxiliares; el SVG es entregable.
Los directorios de intentos fallidos conservan sus exit codes y logs; no son evidencia de éxito.
