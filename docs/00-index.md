# Índice del blueprint TD

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

**Revisión documental 1.1.0-draft — 2026-11-04. G-DESIGN: NOT_READY.** Diseño, contratos y roadmap; no contiene la implementación del producto ni autoriza trading real.

Empezar por [resumen ejecutivo](01-executive-summary.md), [alcance](05-scope-and-assumptions.md), [arquitectura](06-architecture-overview.md), [riesgo](20-risk-engine.md) y [validación](23-statistical-validation.md). Para programar, leer [guía de agentes](37-agent-implementation-guide.md) y el [informe G-DESIGN](../audit/G-DESIGN-FINAL-REPORT.md). T-001 ya está terminada; T-002 espera aprobación del gate.

## Documentos obligatorios

- [01 — executive-summary](01-executive-summary.md)
- [02 — product-vision](02-product-vision.md)
- [03 — functional-requirements](03-functional-requirements.md)
- [04 — nonfunctional-requirements](04-nonfunctional-requirements.md)
- [05 — scope-and-assumptions](05-scope-and-assumptions.md)
- [06 — architecture-overview](06-architecture-overview.md)
- [07 — system-components](07-system-components.md)
- [08 — domain-model](08-domain-model.md)
- [09 — data-architecture](09-data-architecture.md)
- [10 — data-source-catalog](10-data-source-catalog.md)
- [11 — api-contracts](11-api-contracts.md)
- [12 — event-contracts](12-event-contracts.md)
- [13 — ai-architecture](13-ai-architecture.md)
- [14 — ml-models](14-ml-models.md)
- [15 — autonomous-research](15-autonomous-research.md)
- [16 — solana-intelligence](16-solana-intelligence.md)
- [17 — trader-intelligence](17-trader-intelligence.md)
- [18 — strategy-engine](18-strategy-engine.md)
- [19 — decision-engine](19-decision-engine.md)
- [20 — risk-engine](20-risk-engine.md)
- [21 — execution-engine](21-execution-engine.md)
- [22 — backtesting](22-backtesting.md)
- [23 — statistical-validation](23-statistical-validation.md)
- [24 — continuous-learning](24-continuous-learning.md)
- [25 — security](25-security.md)
- [26 — dashboard](26-dashboard.md)
- [27 — infrastructure](27-infrastructure.md)
- [28 — deployment](28-deployment.md)
- [29 — observability](29-observability.md)
- [30 — testing](30-testing.md)
- [31 — cost-analysis](31-cost-analysis.md)
- [32 — implementation-roadmap](32-implementation-roadmap.md)
- [33 — implementation-backlog](33-implementation-backlog.md)
- [34 — acceptance-criteria](34-acceptance-criteria.md)
- [35 — traceability-matrix](35-traceability-matrix.md)
- [36 — risk-register](36-risk-register.md)
- [37 — agent-implementation-guide](37-agent-implementation-guide.md)
- [38 — external-dependencies](38-external-dependencies.md)
- [39 — release-and-rollback](39-release-and-rollback.md)

## Especificaciones complementarias

- [Revisión del informe y límites de evidencia](evidence/research-review.md).
- [Fuentes oficiales](evidence/sources.md) y registro estructurado `evidence/sources.json`.
- `adr/`:18 decisiones (16 originales y ADR-017/018 de auditoría) aceptadas de diseño con alternativas y consecuencias.
- `diagrams/`:12 diagramas Mermaid con fuentes editables y renders cuando validados.
- `contracts/`:OpenAPI3.1, JSON Schema2020-12, eventos, puertos, estados, política, reglas semánticas y ejemplos.
- `strategies/`:20 fichas, parámetros y criterios experimentales.
- `tasks/`:144 fichas revisadas; 140 requieren especificación adicional, índice estructurado y formato de evidencia.
- `requirements.json`, `components.json`, `risks.json`, `external-dependencies.json`:inventarios para trazabilidad.
- `../audit/`:resultados reales de validación del paquete, hallazgos y límites.

## Convenciones normativas

Contrato canónico: `contracts/domain.schema.json`; API empaquetada: `contracts/openapi.json`; valores de política: `contracts/policy-defaults.json`; máquina de órdenes: `contracts/order-machine.json`; tarea: ficha T-NNN y `tasks/index.json`. Documento explicativo y ejemplo no pueden cambiar una invariante. Precedencia/conflictos se resuelven según doc37.

Los enlaces de fuentes se identifican S01–S41. `VERIFIED_DOCUMENTATION` sólo significa documentación consultada, nunca cuenta o SLA probado. Parámetros de estrategia y riesgo son decisiones iniciales de laboratorio. Tareas y tests del producto son futuros. El código de `tools/` sólo valida documentación.

## Orden de uso

Consultar el estado actual en `status/current.md`. Preparar el entorno con `make setup`, ejecutar `make check`, verificar dependencias y elegir tareas topológicamente. No desplegar servicios financieros ni contratar APIs como efecto lateral de preparar documentos. Revisar bloqueos antes de cada integración y conservar evidencia incluso si la estrategia fracasa.
