# Contratos semánticos complementarios

## Signed transaction protocol

`SigningRequest` incluye intent vinculado a chain/wallet, bytes sin firmar, hash de mensaje/cuentas resueltas, evidencia de simulación y aprobación. El signer recibe la solicitud por socket local autenticado; recupera reserva y LiveApproval desde almacenamiento sólo lectura y compara release/policy/epoch/expiry. Para devnet, aprobación de entorno devnet y claves de prueba, jamás reutilizar una live. La firma se devuelve sin enviar; Coordinator persiste bytes+firma antes de I/O.

No debe firmar mensajes arbitrarios, instrucciones de transferencia ajenas al swap, cambio de autoridad, delegates nuevos, cuentas de destino distintas ni rent/priority fees sobre cap. ATA create/wrap/unwrap sólo si corresponden a mint/wallet propios y se contabilizan. Inspección de address lookup tables utiliza el estado/slot de simulación; cambiar bytes/cuentas exige nueva validación y reserva vigente.

## RPC/raw y canonical

Observation.kind resuelve en `observation-kinds.json`; artifact.payload debe validar ese schema después de parsing. Raw preserva formato original permitido y hash; canonical no se limita a JSON arbitrario. Trade identity = chain+signature+instruction_index+decoder_revision; correcciones no duplican volumen. Lectura de getAccountInfo sigue referencia RPC oficial antes de integrar; cualquier formato no revisado se bloquea, no se adivina.

## Exportaciones

POST exports devuelve Job; al terminar, metadata de resultado incluye ticket opaco de descarga actor-bound, con vigencia60 s, hash de archivo y MIME. GET download requiere sesión/ticket, consume atómicamente y entrega `Cache-Control:no-store`. No loggear query ticket. Revocar sesión revoca tickets. Rango máximo 31 días en export inicial; mayores se fraccionan. Falta permiso actual devuelve403 incluso si job fue creado antes.

## Derivados en sandbox

MarginSnapshot debe provenir de tabla de tiers/cálculo oficial del venue elegido. Para simulador genérico: maintenance_margin=sum(notional_tier*rate_tier)+fixed_adjustment, con escala/signo/collateral documentados en fixture del venue. Si no hay tiers válidos, ninguna nueva posición. Stress: precio±20%, funding adverso3 liquidaciones consecutivas y hedge inaccesible; evaluar peor pérdida por pierna. No afirmar que neutralidad delta elimina liquidación o basis.

## Composición de salidas

Si una estrategia usa S19, `effective_max_hold=min(strategy.hold_s,S19.max_hold_s)` y el gatillo de riesgo tiene prioridad sobre alpha. Una salida es reduce-only sobre balance no reservado por otra salida; un intento incierto impide duplicar venta. Requote y rechazo conservan posición abierta y alerta.

## Partiales CEX

CexChildOrder tiene máquina propia. Parent Order conserva intención/reserva; actualizaciones parciales nunca usan la atomicidad Solana. Un cancel request puede competir con fill: procesar fill primero si ocurrido, deduplicar por trade ID y liberar sólo remanente confirmado cancelado. UNKNOWN conserva exposición máxima.
