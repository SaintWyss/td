# Observabilidad y respuesta operativa

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Logs estructurados JSON con trace_id, job_id, event_id, source_id, strategy_id y env; cantidades económicas van como strings. Redactar URLs con claves, headers y textos privados. OpenTelemetry instrumenta latencia y correlación; métricas exportadas localmente y dashboard operacional ligero. Prometheus/Grafana se activan en perfil ops si caben en memoria; no son dependencias del dominio.

| Señal | Umbral inicial / acción |
|---|---|
| market_age >15 s o quote_age >2 s | Denegar entrada dependiente |
| lag ingesta >30 s por 60 s | Alertar, reducir backlog y marcar calidad |
| heartbeat ausente >45 s | Worker unhealthy; leases se resuelven con fencing |
| posición/ledger discrepante | HALTED cartera, incidente y conciliación |
| UNKNOWN transacción >30 s | Alerta prioritaria; mantener reserva, seguir verificando |
| gasto reservado+real ≥80%/100% cap | Alertar / bloquear trabajos no críticos |
| errores 401/403 proveedor | Deshabilitar conector; no martillar reintentos |
| drift/missingness según política | Suspender estrategia o shadow; revisar |
| disco 80%/90% | Frenar backfill / secundarios; preservar estado financiero |
| backup >24 h o restore fallido | Alerta; gate operativo bloqueado |

Alertas tienen fingerprint, severidad, first_seen, last_seen, contador, estado y actor de acknowledge. Acknowledge no resuelve el fallo ni habilita trading. Canales iniciales: panel y logs locales; notificaciones externas sólo si el propietario configura destinatario y autoriza, sin enviar mensajes desde esta entrega.

## SLI y runbooks

Medir disponibilidad durante ventana declarada, tasa de eventos válidos, cobertura, retraso de finalización, cotizaciones por señal, rechazos y costo por experimento. Ningún dashboard oculta períodos negativos o gaps. Métricas de negocio separan PnL paper de real, capital de rendimiento, fees de infraestructura y señal de ejecución.

Runbook RPC caído: breaker, source unhealthy, NO_TRADE, recuperación de cursor y gaps. DB caída: ningún efecto económico nuevo, spool acotado sólo raw permitido, replay cuando vuelva. Cuota agotada: prioridad conciliación, parar research y backfill. Worker crash: lease y fencing, no doble envío. Drift: retirar entradas del modelo y conservar gestión de salidas. Host offline: cierre de sesión paper y gap, sin inventar fills durante apagado.

La auditoría enlaza actor/comando/policy hash y resultado. No usar logs como único ledger. Para incidentes conservar un bundle saneado con versión, ventana, métricas, eventos y acciones; el secreto comprometido no se incluye como evidencia.
