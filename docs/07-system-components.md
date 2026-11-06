# Componentes, puertos y propiedad de datos

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Cada fila define responsabilidad única. El path es destino previsto del código futuro, relativo a `backend/src/td/` salvo `web`. El inventario machine-readable está en `components.json`; los payloads en `contracts/domain.schema.json`.

| Componente | Responsabilidad | Contratos | Inicio |
|---|---|---|---|
| C-CORE | Configuración, cantidades, identidad, permisos y auditoría | Settings,Money,AuditRecord | V0 |
| C-DATA | Conectores, ingesta, disponibilidad, calidad y cobertura | Observation,SourceGrant,ConnectorStatus | V1 |
| C-SOLANA | Pools, mints, holders, extensiones y riesgo observable | Asset,Pool,TokenAssessment | V2 |
| C-LAB | Datasets, splits, replay, métricas y validación | DatasetManifest,Experiment,EvaluationReport | V3 |
| C-ML | Features, entrenamiento, predicción y artefactos | FeatureSnapshot,Prediction,ModelArtifact | V4 |
| C-STRATEGY | Reglas intercambiables y capacidades | StrategyConfig,Signal | V5 |
| C-DECISION | Selección determinista y abstención | Decision,Signal | V5 |
| C-RISK | Sizing, reservas, exposición, modos y control_epoch | RiskAssessment,Reservation,ControlCommand | V5 |
| C-EXEC | Paper y futura preparación/conciliación de ejecución | ExecutionIntent,Order,Attempt,ExecutionReport | V6 |
| C-LEDGER | Fills, asientos por activo, posiciones y NAV | Fill,JournalEntry,PortfolioView | V3 |
| C-AI | Gateway LLM, fallback, schemas, coste y prompts | ExtractionRequest,ExtractionResult,CostRecord | V7 |
| C-RESEARCH | Fuentes, claims, hipótesis y jobs autorizados | ResearchClaim,Hypothesis,SourceGrant | V7 |
| C-TRADERS | Historial de wallets, inventario y scores PIT | TraderProfile,Observation | V8 |
| C-LEARN | Outcomes, drift, promoción y assignments | Outcome,Promotion,ModelArtifact | V10 |
| C-API | HTTP, sesiones, dashboard y exportaciones | Problem,Job,Page,Session | V0 |
| C-OPS | Backups, releases, alertas, incidentes y budget | Alert,ReleaseManifest,CostRecord | V0 |

## Interfaces y permisos

Puertos de lectura: `MarketDataPort`, `ChainReader`, `QuotePort`, `ArtifactStore`, `EvidenceReader`. Puertos de aplicación: `JobQueue`, `UnitOfWork`, `Clock`, `IdGenerator`, `AuditSink`, `BudgetLedger`. Puertos críticos: `RiskAuthorizer`, `ExecutionPort`, `SignerPort`, `LedgerWriter`. Los métodos y payloads exactos están en `contracts/ports.json`; cada componente depende de abstracciones hacia dentro.

La API orquesta comandos humanos, no escribe fills ni reservas directamente. Risk es dueño de reservas y modo de cartera; Ledger de journal; Exec de órdenes/intentos; Data de raw/canonical/cursors; Lab de manifests/experimentos; Learn de asignaciones. Una transacción cruzada se implementa en caso de uso con UnitOfWork y permisos mínimos, no SQL desde una estrategia.

Los consumidores usan vistas de lectura o contratos; no importan tablas del vecino. Para un módulo nuevo, contrato y propietario se definen antes de tarea. Los errores de proveedores se convierten a códigos internos tipados. El composition root es el único lugar autorizado a conocer implementaciones concretas.

## Falla y recuperación

Data caído degrada calidad y provoca abstención; AI caído sólo suspende research; Trainer caído deja champion intacto; DB caída impide nuevos efectos; Risk caído impide ejecuciones; Exec incierto conserva reservas; API caída no debería perder reconciliación. Ningún módulo de análisis puede «ayudar» escribiendo directamente en el estado de otro para saltar un error.

## Contratos financieros R2

[Operaciones, instrumentos y unidades](contracts/financial-operations.md) y ADR-019 especifican
LedgerPostRequest, LedgerPostResult, ReconciliationRequest y catálogo Instrument. Son normativos
para depósitos/rent/fees/reservas/reversos y liquidación; LedgerWriter ya no recibe Fill aislado.
Los metadatos de Instrument y los escenarios son requisitos de implementación, no servicios activos.
