# Motor de ejecución y reconciliación

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Separación de modos

`PaperExecutionPort` transforma intención aprobada en resultados simulados usando quotes/estado disponibles y un modelo de fills versionado. `SolanaExecutionPort` futuro prepara/simula/envía transacciones bajo signer aislado; inicialmente no se despliega. `CexExecutionPort` futuro declara fills parciales y cancelación. Los tres reciben ExecutionIntent y producen ExecutionReport/Fill; ninguno recibe instrucciones en lenguaje natural.

Orden y transacción son entidades distintas: Order es intención económica; Attempt tiene bytes_hash, signature conocida antes del envío, blockhash, lastValidBlockHeight, router, estado y timestamps. Un Order puede tener intentos secuenciales sólo cuando el anterior es terminal probado; no dos intentos con resultado incierto.

## Camino Solana futuro

Quote → reserva → build → decodificación completa de instrucciones/lookup tables → verificación de programas/mints/amounts/fees/destinatarios → simulación → firma → persistencia durable de bytes y signature → envío RPC → seguimiento → finalización → reconciliación → ledger. Si falla persistencia, no enviar. Si falla revalidación, descartar bytes y reserva no utilizada.

Se elige Jupiter V2 `/build` y envío RPC propio para controlar instrucciones y rechazar rutas no decodificadas. El MVP usa sólo quotes; la implementación futura debe verificar documentación completa del build y fixture de respuesta antes de habilitarlo. No reutilizar código de endpoints legacy por semejanza de nombres. Cambios de programa o formato de transacción bloquean firma hasta revisión.

RPC `sendTransaction` acepta envío sin confirmar ejecución [S03]. Timeout tras enviar implica UNKNOWN, nunca FAILED automático. Consultar signature y transacción, con dos proveedores cuando sea necesario. Puede retransmitirse **el mismo payload firmado** dentro de validez, no generar una nueva firma por timeout. Expiración se determina por lastValidBlockHeight/contexto, no por suponer 60 s exactos. Ausencia de status en un RPC no prueba inexistencia histórica.

## Estados normativos

`contracts/order-machine.json` contiene transiciones y efectos. Orden: CREATED → RISK_APPROVED → PREPARED → SUBMITTING → PENDING/UNKNOWN → CONFIRMED → FINALIZED → RECONCILED. Ramas REJECTED, CANCELLED antes de enviar, FAILED_CONFIRMED y EXPIRED_VERIFIED. CONFIRMED puede volver a UNKNOWN ante reversión; ledger final se asienta tras RECONCILED finalizado. Paper recorre estados equivalentes con flag simulated y sin firma de cadena.

Una transacción Solana es atómica para su ejecución de instrucciones: no etiquetar un swap fallido como fill parcial. Las fees de una transacción fallida confirmada sí se contabilizan. Parcialidad pertenece a órdenes CEX o a una estrategia compuesta de varias transacciones; cada leg tiene estado, reserva y riesgo de exposición residual.

## Fallos y cancelación

Una solicitud de cancelar un swap emitido significa detener nuevas emisiones y conciliar; no existe promesa de cancelación on-chain. Si hay disputa de balances/status, congelar activo/cartera y mantener reserva máxima. La recuperación consulta hechos externos, reconstruye proyecciones y no confía únicamente en última respuesta local. Sólo una reconciliación definitiva libera fondos.

MEV: límites de slippage, expiración corta, rutas permitidas y tamaño pequeño. No se afirma inmunidad. No se implementa front-running, wash trading ni manipulación. Un mecanismo de envío privado futuro requiere evaluación de confianza/costo y no altera las invariantes.
