# Motor de ejecución y reconciliación

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

## Separación de modos

`PaperExecutionPort` transforma intención aprobada en resultados simulados usando quotes/estado disponibles y un modelo de fills versionado. `SolanaExecutionPort` futuro prepara/simula/envía transacciones bajo signer aislado; inicialmente no se despliega. `CexExecutionPort` futuro declara fills parciales y cancelación. Los tres reciben ExecutionIntent y producen ExecutionReport/Fill; ninguno recibe instrucciones en lenguaje natural.

Orden y transacción son entidades distintas: Order es intención económica; Attempt tiene bytes_hash, signature conocida antes del envío, blockhash, lastValidBlockHeight, router, estado y timestamps. Un Order puede tener intentos secuenciales sólo cuando el anterior es terminal probado; no dos intentos con resultado incierto.

## Camino Solana futuro

Quote → reserva → build → decodificación completa de instrucciones/lookup tables → verificación de programas/mints/amounts/fees/destinatarios → simulación → firma → persistencia durable de bytes y signature → envío RPC → seguimiento → finalización → reconciliación con journal, reserva y proyección atómicos. Si falla persistencia, no enviar. Si falla revalidación antes de solicitar firma, descartar bytes no firmados y cancelar sólo una reserva ACTIVE. Una reserva ATTEMPTED conserva fondos hasta reconciliación autoritativa, incluso si la respuesta del signer se perdió.

Se elige Jupiter V2 `/build` y envío RPC propio para controlar instrucciones y rechazar rutas no decodificadas. El MVP usa sólo quotes; la implementación futura debe verificar documentación completa del build y fixture de respuesta antes de habilitarlo. No reutilizar código de endpoints legacy por semejanza de nombres. Cambios de programa o formato de transacción bloquean firma hasta revisión.

RPC `sendTransaction` acepta envío sin confirmar ejecución [S03]. Timeout tras enviar implica UNKNOWN, nunca FAILED automático. Consultar signature y transacción, con dos proveedores cuando sea necesario. Puede retransmitirse **el mismo payload firmado** dentro de validez, no generar una nueva firma por timeout. Expiración se determina por lastValidBlockHeight/contexto, no por suponer 60 s exactos. Ausencia de status en un RPC no prueba inexistencia histórica.

## Estados normativos

`contracts/order-machine.json` contiene transiciones y efectos. Orden: CREATED → RISK_APPROVED → PREPARED → SUBMITTING → PENDING/UNKNOWN → CONFIRMED → FINALIZED → RECONCILED. Ramas REJECTED, CANCELLED antes de enviar, FAILED_CONFIRMED y EXPIRED_VERIFIED. CONFIRMED puede volver a UNKNOWN ante reversión; journal final, reserva, proyección, outbox y RECONCILED se confirman en una única transacción local después de observar finality; no se publica RECONCILED antes del journal. Paper recorre estados equivalentes con flag simulated y sin firma de cadena.

Una transacción Solana es atómica para su ejecución de instrucciones: no etiquetar un swap fallido como fill parcial. Las fees de una transacción fallida confirmada sí se contabilizan. Parcialidad pertenece a órdenes CEX o a una estrategia compuesta de varias transacciones; cada leg tiene estado, reserva y riesgo de exposición residual.

## Fallos y cancelación

Una solicitud de cancelar un swap emitido significa detener nuevas emisiones y conciliar; no existe promesa de cancelación on-chain. Si hay disputa de balances/status, congelar activo/cartera y mantener reserva máxima. La recuperación consulta hechos externos, reconstruye proyecciones y no confía únicamente en última respuesta local. Sólo una reconciliación definitiva libera fondos.

MEV: límites de slippage, expiración corta, rutas permitidas y tamaño pequeño. No se afirma inmunidad. No se implementa front-running, wash trading ni manipulación. Un mecanismo de envío privado futuro requiere evaluación de confianza/costo y no altera las invariantes.

## Durabilidad, cancelación y reconciliación (ADR-017)

Máquinas complementarias: `contracts/lifecycle-machines.json` (attempt, reservation,
control, job); las reglas son especificación, no un ejecutor financiero implementado.
Antes de solicitar firma, marcar reserva ATTEMPTED durablemente: un crash no la libera.
Signer devuelve signed_transaction_b64, firma y hash. El coordinador verifica identidad
criptográfica y guarda artefacto duradero privado antes de SUBMITTING/envío; Attempt
referencia ese artefacto. Nunca se exponen bytes firmados por API de lectura o logs.
PREPARED admite bytes_hash/signature null. Una firma incierta conserva ATTEMPTED; una
respuesta de firma perdida se recupera por attempt_id, sin firmar otro mensaje.

Un único (order_id, attempt_id) puede estar potencialmente ejecutable. Retry de envío
reutiliza bytes y firma. Expiración local o RPC null no prueba ausencia: para
EXPIRED_VERIFIED hacen falta block height finalizado posterior al lastValidBlockHeight,
histórico completo de firma y saldos/fees reconciliados, contraste de proveedor y evidencia
sin gaps. Falta de cualquiera mantiene UNKNOWN. No introducir durable nonce en este diseño.
Una transacción firmada pero no enviada localmente todavía puede circular: CANCELLED
sólo antes de firma o con prueba de imposibilidad de envío, nunca por el mero timeout.

La reconciliación aplica evidencia finalizada → journal idempotente + ajuste/consumo de
reserva + proyección + estado RECONCILED + outbox, **en una transacción local**. Antes de
ese commit el estado continúa FINALIZED/FAILED_CONFIRMED/EXPIRED_VERIFIED. No exigir
RECONCILED para poder escribir el asiento: sería una dependencia circular. Fallo DB
revierte todo; retry devuelve el journal ya escrito mediante external_effect_key único.

Fill contiene flujo de intercambio neto y fee informativa. FeeEvent es el único dueño
de la contabilización de gastos adicionales de red/servicio; no volver a cobrar la fee
incluida en los importes netos del swap. Clave económica: chain/venue + signature/trade_id
+ categoría + índice de efecto + asset. Varias FeeEvent permiten fees en distintos activos.
Rent de ATA es depósito recuperable, no fee: requiere asiento de activo restringido y
reversión cuando se recupera. Transacción fallida puede generar sólo FeeEvent y ningún Fill.
Las interfaces para depósitos/rent y derivados necesitan el cierre registrado en GD-09;
no inferirlas de LedgerWriter.post(Fill).

Paper nunca firma: PREPARED→SUBMITTING exige persistir intent/seed/fill-model hash;
SUBMITTING→PENDING es aceptación del simulador y luego confirmación/finalidad simuladas.
Sus Attempt tienen simulated=true, firma/artefacto null; los IDs y efectos incluyen PAPER.
No presentar pruebas sobre fixtures como confirmación de red.
