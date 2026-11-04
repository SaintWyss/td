# Contratos de eventos y jobs

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

`contracts/events.json` enumera tipos, productor, consumidores y payload; `EventEnvelope` define versión, event_id, correlation_id, causation_id, occurred_at, available_at, aggregate_id, aggregate_revision, dedup_key y payload. El tipo debe corresponder exactamente al schema del payload. No hay bus externo en V0–V6.

## Entrega y orden

Outbox es transaccional con el agregado. Worker toma filas mediante lease y `FOR UPDATE SKIP LOCKED`, publica a handlers locales y confirma sólo tras guardar efecto y receipt único. Un crash puede repetir entrega. Se ordena por agregado y revisión, no por reloj global ni por orden de llegada de diferentes fuentes. Revisión faltante aparca el evento y pide replay; revisión duplicada se reconoce sin efecto.

Reintentos internos: 1, 2, 4, 8, 16 s más jitter; máximo 5 antes de dead letter. El handler financiero no inventa un fill para desbloquear su cola. DLQ conserva causa, versión y evidencia saneada; reprocess requiere actor y misma idempotencia. Un evento inválido no se descarta en silencio ni bloquea todos los agregados.

## Jobs durables

Estados: QUEUED → RUNNING → SUCCEEDED/FAILED/CANCELLED; RUNNING con lease vencido vuelve a QUEUED sólo si es idempotente. Job incluye `kind`, input_artifact_hash, config_hash, seed, attempts, lease_owner, lease_until, progress y resultado. El lease dura 60 s, heartbeat cada 15 s; una fencing version rechaza escrituras del worker viejo. Cancelar entrenamiento produce checkpoint opcional y estado terminal; cancelar un envío incierto sólo solicita conciliación.

No se mezclan colas: prioridad 0 reconciliación y riesgo; 1 ingesta; 2 paper y features; 3 research; 4 backfill/entrenamiento. Dos workers ligeros máximos y un entrenamiento. Saturación frena nuevas tareas de baja prioridad, preserva evidencia y muestra lag. La expiración de señales puede volver inútiles jobs en cola; devolver EXPIRED sin evaluar mercado viejo.

## Compatibilidad

Cambios aditivos crean minor de contrato sólo si lectores toleran el campo; con `additionalProperties=false`, incluso una adición requiere desplegar consumidores compatibles antes del productor. Breaking cambia event_type con sufijo v2. El registro mantiene v1 durante replay de históricos. Payload corrupto va a cuarentena con hash; jamás se «arregla» suponiendo la unidad.

La auditoría local es append-only por permisos, con cadena de hashes y anclaje diario en backup separado. Es tamper-evident, no mágicamente inmutable frente a root o al propietario de la DB. Este límite forma parte del modelo de amenazas.
