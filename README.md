# TD — investigación cuantitativa e inteligencia Solana

Repositorio privado con el blueprint de diseño y una base de desarrollo reproducible.
**G-DESIGN: NOT_READY. Bootstrap T-001 completado; producto pendiente.** La revisión
de contratos es `1.1.0-draft`; los documentos sin cambios conservan su fecha histórica. No es una release. El primer objetivo es investigación y simulación (**MVP-PAPER**).

No hay motor de trading, API, dashboard, conectores, modelos entrenados ni ejecución
de órdenes implementados. No se requiere ninguna credencial para los checks locales.

## Empezar

Requisitos: Python 3.12, uv 0.13.5, Node 24, pnpm 11.25.0 y GNU Make.

```bash
git clone https://github.com/SaintWyss/td.git
cd td
make setup
make check
```

`make setup` instala las versiones fijadas en `uv.lock` y `web/pnpm-lock.yaml`.
No inicia servicios. `make check` ejecuta validación documental, Ruff, mypy,
TypeScript y las pruebas del validador. La CI ejecuta los mismos comandos sin
secretos ni permisos de escritura en el repositorio.

## Qué contiene

| Ruta | Contenido actual |
|---|---|
| `backend/src/td/` | Paquete Python y fronteras domain/application/ports/adapters/entrypoints |
| `web/` | Workspace TypeScript estricto; UI pendiente |
| `docs/` | 40 documentos principales, 18 ADR (16 originales + 2 de auditoría), 20 estrategias y 144 tareas propuestas |
| `docs/contracts/` | 106 definiciones de dominio (102 originales + 4 requests), OpenAPI, eventos, políticas y ejemplos |
| `tools/` | Validación estructural y regeneración de tablas derivadas |
| `tests/unit/` | Pruebas adversariales del validador documental |
| `config/`, `infra/` | Alcance previsto de configuración e infraestructura |
| `audit/` | Resultados de checks y sus límites |

## Lecturas principales

- [Estado actual y pendientes](docs/status/current.md).
- [Índice del blueprint](docs/00-index.md), [arquitectura](docs/06-architecture-overview.md) y [roadmap](docs/32-implementation-roadmap.md).
- [Backlog](docs/33-implementation-backlog.md) y [guía para contribuir](CONTRIBUTING.md).
- [Reglas de trabajo](AGENTS.md) y [plan de pruebas](docs/30-testing.md).
- [Informe G-DESIGN](audit/G-DESIGN-FINAL-REPORT.md), [hallazgos](audit/g-design/findings.json) y [delegabilidad de las 144 tareas](audit/g-design/delegability.md).
- [Resultado estructural del bootstrap](audit/validation.json), preservado como evidencia histórica.

La validación comprueba esquemas y ejemplos, referencias, DAG, trazabilidad,
transiciones declaradas y sincronización de tablas. **No demuestra** invariantes
financieras entre campos, seguridad operativa, disponibilidad de APIs, permisos
de datos, consumo real de recursos ni rentabilidad. Los 12 diagramas Mermaid
conservan sus fuentes; los renders y su revisión están en `audit/g-design/diagrams-final/`
y `audit/g-design/visual-review.json`. Renderizar no valida la semántica financiera.

Los originales recibidos están en `docs/evidence/`; se preservan como antecedentes,
no como instrucciones de ejecución ni fuentes verificadas de forma automática.
El historial Git registra los cambios: no se presenta este bootstrap como un
paquete de release con manifiesto de integridad independiente.
