# Puertos auxiliares e historiales — R2

Fecha 2026-11-06. ADR-021. `ports.json` es el registro canónico de métodos, schemas, owners,
timeouts, retries, cancelación, transacción y pruebas de contrato. Todos los métodos reciben
`(request: input_schema, context: PortContext)` y devuelven output_schema o el error tipado
indicado. No mezclan un éxito parcial con una excepción; coverage parcial existe sólo en readers
que la declaran. Los puertos son interfaces de diseño; no hay implementación ni acceso externo.

## Contexto y errores

PortContext aporta request_id, actor autenticado, correlation_id, deadline UTC, cancel token,
idempotency_key y uow_id. Actor nunca se toma de un formulario sin autenticación. Idempotency key
es obligatoria para mutaciones (excepto begin, que usa UowBegin.id); uow_id es obligatorio para
writes dentro de UoW y null antes de begin. La duración efectiva es min(timeout_ms del puerto,
tiempo restante de deadline). Un worker largo tiene deadline de job, no de la petición HTTP.

PortFailure distingue NOT_FOUND, UNAVAILABLE, PERMISSION_DENIED/REVOKED, invalidación de cursor,
timeout/cancel y UNKNOWN_OUTCOME con effect_state NONE/COMMITTED/UNKNOWN. FinancialError conserva
los motivos financieros. Nunca convertir UNAVAILABLE en NOT_FOUND ni UNKNOWN en rollback probado.
retryable no autoriza repetir efecto; el consumidor primero consulta estado por identidad estable.
Retry de lectura: máximo3 intentos total, backoff250/1000ms sólo si caben en deadline; 429 respeta
retry_after y presupuesto, no multiplica intentos. No retry ante schema drift, permisos o hash roto.
No transacción DB abierta mientras se espera red, LLM, entrenamiento o evidencia externa.

## Clock e identidad

Clock.now devuelve UTC y monotonic_ns junto con epoch_id del proceso. Medir duración con monotónico
sólo dentro del mismo epoch; persistir UTC deadline y reiniciar sin extenderlo. Salto del wall-clock
que impida probar vigencia bloquea autorización. Replay usa reloj inyectado cuya UTC avanza por
available_at y desempate estable; no toca reloj del host ni duerme. No hay fallback silencioso.
Prueba: lectura UTC12:00:00, mono1e9; segunda UTC11:59:59 por ajuste, mono2e9 => duración1s,
alerta por wall regression, no prorrogar una expiración12:00:05. Tras reinicio epoch distinto,
comparar UTC vigente y renovar verificación de datos, nunca restar monotónicos de epochs distintos.

IdGenerator.derive produce namespace + ':' + SHA256 UTF-8 del par canónico JSON
[namespace,causal_key]. Ambos modos usan igual algoritmo; el caller runtime suministra una causal
key nueva (identidad de efecto externo o UUID de petición), replay usa manifest/case/sequence.
Misma causalidad produce mismo ID; ningún contador global oculto. Colisión con payload diferente
es corrupción/IDEMPOTENCY_CONFLICT, no generar otra identidad. No usar IDs como credenciales.
Prueba: repetir ['event','fixture:1']100 veces produce1 ID; cambiar namespace cambia ID.

## Unit of Work

begin(UowBegin) abre SERIALIZABLE, toma locks por entity_id en orden lexicográfico, verifica las
revisiones y devuelve ACTIVE; falla antes de escribir ante revisión vieja. Maximum32 locks,
única conexión/transaction por handle, sin nesting. commit(UowReference) confirma journal,
proyecciones, reservas, órdenes, audit y outbox juntos; commit_token durable pertenece al mismo
commit. status consulta registro de transacción en conexión nueva consistente. rollback sólo
confirma ROLLED_BACK si DB lo acredita; después de COMMITTED retorna COMMITTED, no lo deshace.

El registro UoW se crea duraderamente antes del begin como intención; una transacción activa sin
resultado después de caída se reconcilia con DB/commit_token y lease, nunca se considera abortada
por edad solamente. Se prohíbe usar el registro de intención como prueba de que hubo commit.
Handle UNKNOWN mantiene bloqueadas decisiones dependientes hasta status definitivo. Mismo ID
resuelto devuelve resultado original; otro payload begin con mismo ID => conflicto.

Los repositorios asociados se obtienen por handle local; no se serializa SQL ni un callback
arbitrario en UowBegin. Especificaciones de writes son comandos tipados de cada caso de uso,
especialmente LedgerWriter/RiskAuthorizer/PromotionService. La infraestructura no decide reglas.
Prueba: batch FIN-01 + comando con revisión inválida => ningún journal/saldo/outbox; caída después
de commit antes de respuesta => status COMMITTED con token y repetir request no duplica.

## Jobs

JobQueue.enqueue recibe input_manifest_id y hashes; lee/verifica manifest antes de encolar.
El contenido tiene schema fijado por kind: EXPERIMENT/TRAIN→Experiment, RESEARCH→ResearchRequest,
EXPORT→ExportRequest, RECONCILE→ReconciliationRequest, BACKFILL→MarketReadRequest,
PAPER→PaperRequest. No scripts/rutas/comandos arbitrarios. max_attempts<=3 y deadline inmutable.
Job ID idéntico/hash idéntico devuelve job actual; distinto hash => IDEMPOTENCY_CONFLICT.

claim selecciona primero not_before, luego created_at, luego id; sólo QUEUED elegibles, usa lock
SKIP LOCKED, cambia RUNNING, incrementa attempts/fencing_token y lease<=60s. Null job sólo si
cola leída correctamente sin elegibles. Request de claim repetido conserva el mismo resultado
mientras su lease sigue vigente; tras pérdida devuelve LEASE_LOST, no asigna silenciosamente otro.
Heartbeat renueva30s como máximo desde recepción y nunca supera deadline. Transition exige
worker, revision y fencing exactos. SUCCEED necesita resultado verificado, FAIL error estable;
CANCEL_REQUEST sólo marca bandera por actor autorizado. El worker coopera en checkpoints.

Lease vencida no prueba que worker dejó de ejecutar: CAS invalida fencing, y sólo jobs cuyos
efectos sean deduplicables pueden volver a QUEUED tras recuperación. RECONCILE/PAPER no reenvían
órdenes externas al reintentar; consultan IDs/UNKNOWN. Cancelación durante efecto incierto queda
RUNNING+cancel_requested hasta reconciliar; no liberar presupuesto/reservas por cancelar UI.
Prueba: workerA token7 expira, B token8; A publica resultado con7 => LEASE_LOST sin transición.

## Audit y evidencia

AuditSink.append recibe datos sin hashes de cadena elegidos por caller. Lee último hash bajo lock,
Clock asigna timestamp, calcula SHA256 JSON canónico del record salvo record_hash; genesis previous_hash
es64 ceros. Actor viene del contexto y debe coincidir. Append forma parte del mismo UoW del efecto;
si falla, se deniega la mutación. Logs diagnósticos fuera de DB no sustituyen AuditRecord.
Duplicado record_id + contenido idéntico devuelve original, no agrega eslabón. Redactar secretos
antes de construir record. Auditoría conserva IDs/referencias, no texto protegido ni payload crudo.

EvidenceReader sólo resuelve IDs registrados contra root allowlist, verifica symlink/traversal,
size<=max_bytes (hasta100MiB por request), sha256 y permisos de todas las fuentes derivadas.
local_handle es capacidad local opaca de lectura durante la llamada/job, nunca path arbitrario,
URL ni contenido ejecutable. No deserializar pickle de artefacto no confiable. Revocación/purpose
se comprueba antes y después de materializar, y antes de exponer resultado; cerrar y retirar handle
si revocado. Ausencia NOT_FOUND; truncado/hash incorrecto CORRUPT_EVIDENCE/HASH_MISMATCH.
Prueba: manifest declara abc... pero bytes hash distinto => sin handle, sin uso en modelo/replay.

## Historiales tipados

Cada reader tiene Query/Entry/Page propios; no contenedor heterogéneo ni elección de tabla libre.
Entry conserva id/revision/source/entity/event_time/available_at/retracted y value tipado.

| Reader | Value | Productor / consumidor principales |
|---|---|---|
| TemporalHistoryReader | Bar | T-028 → replay/features/modelos |
| ObservationHistoryReader | Observation | T-014–T-020 → T-021/T-028; payload por artifact/evidence |
| TradeHistoryReader | Trade | T-022 → T-028/T-033 |
| WalletHistoryReader | WalletTransaction | T-067 → T-068/T-069 |
| FeatureHistoryReader | FeatureSnapshot | T-028/T-071 → T-033/T-038/T-070 |
| PredictionHistoryReader | Prediction | T-040 → T-072/T-073 |
| DecisionHistoryReader | Decision | T-049 → T-055/T-081/T-085 |
| EvidenceHistoryReader | ArtifactFile | T-013/T-008 → auditoría/exports |
| JournalHistoryReader | JournalEntry | T-031 → T-032/T-055/T-068 |

Query exige entity_ids y source_ids (1..100), event_from<event_until, as_of, mode, limit1..100,
include_retracted y cursor/snapshot_id nullable al iniciar. Intervalo de eventos [from,until),
filtrado adicional available_at<=as_of. Ventana máxima31d por consulta, dividir ventanas mayores
sin asumir cobertura. Ledger event_time=occurred_at, available_at=recorded_at; wallet/trade usan
Observation normalizada; evidencia usa tiempo registrado, no filesystem mtime.

Orden ascendente (event_time,record_id,revision); se selecciona última revisión conocida en as_of
por identidad antes de ordenar. include_retracted=false excluye registros retractados a ese corte;
un evento histórico antes de retractación sigue existiendo. Source IDs y mode nunca se mezclan
para completar huecos. Histórico de autoría/ledger no sustituye lectura autoritativa para Risk.

Primera página fija snapshot_id a watermark inmutable (max committed sequence), expira15min;
páginas siguientes usan mismo corte. Cursor opaco autenticado liga hash de todos los filtros,
as_of, watermark y última tupla. Filtro distinto => CURSOR_MISMATCH; vencido => SNAPSHOT_EXPIRED;
reiniciar consulta con nuevo snapshot explícito. No offset ni NOW variable por página. Cursor
siguiente sólo si quedan filas; items vacíos con next_cursor=null puede ser un resultado completo.

coverage COMPLETE requiere unión de coverage_intervals que cubra cada source y todo el intervalo;
no exige que existan trades. PARTIAL/UNKNOWN expone intervalos y missing_source_ids. Error de
almacenamiento/proveedor => PortFailure, jamás página vacía COMPLETE. No llamar un proveedor
remoto desde una consulta histórica local para ocultar gaps; backfill es job separado con permiso.
Prueba: r1 event10:00 available10:01, r2 correction available10:05; as_of10:03 devuelve r1.
Con límite1 y dos filas de igual event_time, paginar por IDs sin duplicarlas ni perderlas.

## Lecturas autoritativas y recuperación

InstrumentReader selecciona revisión inmutable con available_at<=as_of; revision exacta si se
solicita. Risk usa as_of=Clock.now y comparación con catálogo vigente; replay usa su reloj. Otros
readers de reservas/órdenes/portfolio/control/modelo leen estado committed dentro de UoW y verifican
expected_revision cuando se proporciona; cache no autoriza efectos. OperationReader.lookup resuelve
idempotencia antes del CAS; NOT_FOUND es sólo ausencia probada. PermissionReader.at no permite
backdating para operaciones actuales: permiso actual y permiso histórico del dataset son dos checks.

BudgetLedger.settle mantiene cap en UNCERTAIN hasta comprobar costo real; SETTLED exige actual_usd
conocido; RELEASED exige evidencia no billable. No usar ledger financiero de activos para presupuesto
USD de APIs. Cualquier cambio después de timeout conserva la identidad de la reserva original.

Pruebas de contrato concretas anteriores se implementarán en T-008/T-009/T-010/T-011/T-013/T-028
según responsabilidad; cada ficha GD-10 determina qué fake/unit/DB es pertinente. Tests locales
no acreditan cobertura o permisos de un proveedor. Ningún puerto nuevo autoriza trading real.
