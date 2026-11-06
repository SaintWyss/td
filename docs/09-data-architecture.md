# Arquitectura de datos y persistencia

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Tres capas

Raw: payload original permitido, hash SHA-256, fuente, recepción, tamaño, permisos y cursor. Canonical: observaciones tipadas, estado de cadena y revisiones. Research: Parquet particionado por `chain/date/kind`, manifiesto con hashes, cardinalidad, cobertura y features. Los datos personales/textos con retención limitada no se hacen inmutables indefinidamente: raw cifrado se elimina según grant, manteniendo tombstone y hash cuando sea legítimo.

`event_time` es hora declarada por fuente; `received_at` es primera recepción propia; `available_at` es cuándo el dato validado estuvo disponible a la estrategia. `recorded_at` mide persistencia. `slot` ordena cadena sin inventar precisión temporal. El tiempo de decisión usa UTC. Para una revisión, `supersedes_id` apunta al anterior; el replay elige la versión disponible en t. Eventos tardíos corrigen estadísticas futuras, no decisiones pasadas.

## Tablas y claves

| Grupo | Tablas / clave e índice principal |
|---|---|
| Fuentes | source_grants(id, revision), connector_cursors(source, partition), coverage_intervals(source,start,end,status) |
| Cadena | assets(chain,mint), pools(chain,address), observations(id), UNIQUE(source,dedup_key,revision) |
| Evidencia | artifacts(hash), evidence(id,artifact_hash,offset), dataset_manifests(id,hash) |
| Investigación | research_claims(id), hypotheses(id), experiments(id), experiment_trials(experiment_id,trial_id) |
| Modelos | model_artifacts(id), prediction_records(id), promotions(id), champion_assignments(strategy,revision) |
| Trading | decisions(id), risk_assessments(id), reservations(id), portfolios(id,revision), orders(id), attempts(id), fills(id) |
| Ledger | journal_entries(id,external_effect_key UNIQUE), journal_lines(entry_id,line_no), position_projections(portfolio,asset) |
| Operación | jobs(id,idempotency_key UNIQUE), outbox(event_id), consumer_receipts(consumer,event_id UNIQUE), audit_log(seq,hash) |

SQL usa `numeric(78,0)` para cantidades atómicas y `numeric(38,18)` para valores monetarios derivados; overflow rechaza y alerta. Direcciones se validan por chain, con comparación sensible a mayúsculas cuando corresponda. Índices temporales por `(asset_id, available_at)` y particiones mensuales de observaciones; no hacer particiones por cada mint.

## Transacciones y almacenamiento

Publicar un archivo: escribir temporal, fsync, hash, renombrar atómicamente, registrar manifiesto READY y outbox. Un archivo huérfano no es dataset; limpieza usa retención y referencia. Backup captura manifiesto y archivos incluidos con checkpoint de DB. Un dataset no depende de un glob que pueda cambiar mientras corre el experimento.

La ausencia de trades no implica precio constante ni liquidez disponible. OHLCV vacío se marca; no hay forward-fill de volumen. El universo conserva mints muertos, pools drenados, rutas ausentes y intervalos sin observación. Retención inicial: raw on-chain 30 días caliente, canonical/Parquet 180 días caliente y archivo hasta 365 días según capacidad; manifiestos, decisiones y ledger se conservan durante la vida del experimento. Límites son política local y se revisan contra contrato de cada fuente.

Cold storage al HDD del escritorio; portátil sólo fixtures y resultados resumidos. Al 80% de cuota detener nuevos backfills; al 90% detener colectores secundarios; nunca borrar archivos referenciados por holdouts o incidentes sin decisión explícita.

## Contratos financieros R2

[Operaciones, instrumentos y unidades](contracts/financial-operations.md) y ADR-019 especifican
LedgerPostRequest, LedgerPostResult, ReconciliationRequest y catálogo Instrument. Son normativos
para depósitos/rent/fees/reservas/reversos y liquidación; LedgerWriter ya no recibe Fill aislado.
Los metadatos de Instrument y los escenarios son requisitos de implementación, no servicios activos.

## Puertos e historiales R2

[Contratos auxiliares](contracts/auxiliary-ports.md) y `contracts/ports.json` fijan métodos, contexto, errores, deadline, cancelación y recuperación. Las consultas históricas tienen schemas por tipo, corte de disponibilidad, snapshot estable y cobertura explícita. No interpretar páginas vacías como cobertura garantizada.
