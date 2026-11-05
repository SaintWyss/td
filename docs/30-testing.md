# Plan de pruebas y evidencia

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

## Niveles

Unitarias puras: cantidades, fees, temporalidad, señales, dimensionamiento, estados y métricas. Property-based: suma de journal, exposición nunca superior a cap, permutaciones de duplicados, orden de revisiones y round-trip de esquemas. Integración: PostgreSQL real temporal, outbox/leases, archivos atómicos, HTTP simulado por proveedor y permisos. Contrato: fixtures válidos/invalidos, schema drift, tipos de unidades y clients OpenAPI. E2E: UI→API→job→paper→ledger y roles. Chaos: corte en cada frontera, reloj desviado, espacio lleno, status incierto, pérdida de red y restauración.

Tests de estrategias no exigen rentabilidad en fixtures inventados. Verifican señales, abstenciones, costos y falsación; evidencia financiera proviene de datasets apropiados. Los tests golden tienen resultados manuales independientes. Toda simulación conserva su modelo de fill y limitaciones.

## Gates de código

CI de Python: Ruff, mypy estricto del dominio/puertos, pytest unit/integration y import rules. Web: TypeScript, lint, pruebas de componentes y Playwright en flujos mutantes. Escaneo de secretos/dependencias y SBOM. Cobertura objetivo ≥90% de ramas en riesgo, contabilidad y estados, acompañada de pruebas de propiedades y mutation testing selectivo; un porcentaje no reemplaza casos adversariales.

## Comandos contractuales para el futuro repo

El bootstrap T-001 incorpora `make verify-spec`, `make lint`, `make typecheck`, `make test-unit`; las tareas posteriores agregan `make test-integration`, `make test-contract`, `make test-e2e`, `make test-chaos`. Cada tarea de producto deberá tener pruebas con nombres significativos y evidencia vinculada a su ID. Los tests actuales verifican herramientas documentales; no cubren lógica de negocio.

`tools/validate_spec.py` usa dependencias fijadas en `pyproject.toml` y `uv.lock`. Valida JSON Schemas, ejemplos positivos/negativos, OpenAPI, extremos de transiciones, referencias locales, trazabilidad y DAG de tareas. También detecta tablas derivadas desactualizadas. `make verify-spec` escribe `audit/latest.json`; la captura del bootstrap está en `audit/validation.json`. No valida manifiestos de release, semántica financiera, render de diagramas, RPC, dinero real, alpha ni RAM efectiva.

## Evidencia exigida

Cada tarea entrega commit base/final, diff, archivos, comandos exactos, salida/exit code, versiones, duración, fixtures y limitaciones. No se aceptan capturas como única prueba de backend ni «tests deberían pasar». Si un comando falla, estado FAILED/BLOCKED, causa y alcance. Si el test de red no puede ejecutarse, marcarlo pendiente; el fixture local no se presenta como prueba de cuenta.

Matriz de amenazas y fallos críticos: prompt injection, SSRF, XSS de fuente, IDOR/roles, doble reserva, replay, timeout de envío, reorg, fee desconocida, inventario negativo, pérdida total token, consumo simultáneo de budget y restauración obsoleta. Cada uno tiene caso en el backlog y en semantic-rules.

## Evidencia G-DESIGN

`tools/validate_design.py` comprueba el motivo exacto de los negativos (omisión única),
24 casos de frontera con keyword/path, bindings de intención, guards/reachability y rutas.
Las 12 pruebas actuales incluyen mutaciones adversariales del validador. No ejecutan riesgo,
ledger ni estrategias. Los ejemplos positivos son fixtures de forma; GD-17 conserva el trabajo
pendiente de escenarios financieros enlazados. `tools/render_diagrams.py` genera SVG con un
renderer y Chromium suministrados; revisión visual separada en audit/g-design/visual-review.json.
Comandos, versiones y códigos reales: audit/g-design/validation.json y logs asociados.
