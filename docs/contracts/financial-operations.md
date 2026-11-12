# Contratos financieros normativos — draft 1.2

Fecha: 2026-11-06. ADR-019. Propietario C-LEDGER; autorización de reservas C-RISK.
Este documento define comportamiento futuro y casos sintéticos. No ordena transferencias reales.

## Identidad, unidades y cuentas

Money siempre contiene asset_id, atoms entero decimal string y decimals del registro inmutable.
JournalLine expresa delta firmado en átomos; no admite -0. La suma de signed_atoms de cada
JournalEntry por asset_id debe ser exactamente cero, con al menos un débito y un crédito no nulos.
Una conversión nunca suma cantidades de activos distintos. Se conservan límites de doc08:
78 dígitos para átomos, 20 enteros/18 fraccionarios para derivados, sin float monetario.
Todos los importes de comandos deben ser positivos; una fee cero se omite, no produce journal.

LedgerAccount es una cuenta lógica de (portfolio, custody, mode, asset, role), no una dirección
ni una capacidad de transferir fondos. Cuenta cerrada rechaza nuevos posts. Toda move debe tener
source != destination y ambas cuentas en el mismo portfolio/mode/asset. External y clearing
también pertenecen al portfolio; no representan fondos disponibles. UNIQUE sobre esa tupla,
con ID estable y metadatos inmutables; cambiar custodia implica nuevo registro.

| Rol | Saldo / proyección |
|---|---|
| AVAILABLE | Átomos propios libres; saldo >= 0 |
| RESERVED | Átomos propios inmovilizados; saldo >= 0, desglosado por reservation_id |
| RENT_LOCKED | Depósito recuperable; >= 0; no disponible para negociar |
| COLLATERAL | Garantía aislada del instrumento; >= 0; no disponible spot |
| EXTERNAL | Contrapartida de capital externo observado; admite signo |
| FEE_EXPENSE | Acumulación de gastos por activo; admite reversos exactos |
| TRADE_CLEARING | Contrapartida del intercambio por activo; no saldo propio |
| ADJUSTMENT_CLEARING | Contrapartida de diferencia demostrada y aprobada |
| PNL_CLEARING | Contrapartida de liquidación de PnL derivado observado |

Saldo propio total por activo = AVAILABLE + RESERVED + RENT_LOCKED + COLLATERAL.
Position.quantity_atoms spot = AVAILABLE + RESERVED; reserved_atoms = RESERVED. Disponible =
quantity_atoms - reserved_atoms. No restar reservas otra vez de AVAILABLE. Rent y collateral
son posiciones restringidas separadas para NAV. PortfolioView sólo se marca reconciled cuando
la cobertura de todas sus cuentas y efectos es completa. UNKNOWN no es importe cero.

## Comando, resultado y máquina de registro

LedgerPostRequest tiene operation_id, idempotency_key, portfolio_id, mode, expected_portfolio_revision,
actor_id, occurred_at, available_at, evidence_ids, operation y payload discriminado. Las variantes
están en domain.schema.json. occurred_at identifica el hecho y available_at su conocimiento local;
posted_at es JournalEntry.recorded_at asignado por Clock. No retrofechar disponibilidad.
LedgerPostResult devuelve POSTED o DUPLICATE, journal original y revisión resultante.
Errores: FinancialError; nunca devolver éxito sin commit durable.

El registro de operación usa RECEIVED → VERIFIED → POSTED. RECEIVED/VERIFIED pueden pasar a
REJECTED con error tipado. Evidencia insuficiente conserva PENDING_EVIDENCE hasta nueva evidencia;
no genera journal ni saldo disponible. Un journal POSTED es inmutable; su rectificación crea otro
journal enlazado, no lo muta a una versión nueva. A timeout de DB, el cliente consulta por la misma
idempotency_key; mientras no pueda resolverla, devuelve UNKNOWN_OUTCOME y no cambia la clave.

La aplicación resuelve actor_id desde contexto autenticado, nunca confía en un actor del payload.
Writer verifica propietario del caso de uso y sus permisos. API y LLM no pueden postear balances.
No hay ruta HTTP nueva de transferencia ni endpoint público LedgerWriter.

Antes del commit: validar schema/unidades, resolver cuentas y evidencia, adquirir lock de portfolio,
comprobar revisión, autorización, límites y unicidad. UNIQUE(portfolio_id, mode, idempotency_key),
UNIQUE(portfolio_id, mode, operation_id) y UNIQUE(portfolio_id, mode, external_effect_key) para hechos
externos. El hash canónico del comando excluye expected_portfolio_revision y tiempos de solicitud;
conserva operation_id, actor, modo, operación, payload, occurred_at y evidence_ids ordenados.
Consultar dedup ANTES del CAS: misma clave y mismo hash devuelve original incluso con revisión vieja;
misma clave con efecto distinto => IDEMPOTENCY_CONFLICT; ninguna nueva línea ni evento.

## Operaciones y reglas específicas

Cada move produce exactamente source:-amount y destination:+amount. Los roles siguientes son
restricciones normativas, no sugerencias. Ledger calcula líneas; no acepta JournalEntry del cliente.

| operation / payload | Precondición y autoridad | Efecto / postcondición | Error / recuperación |
|---|---|---|---|
| DEPOSIT / ExternalFlowCommand | Reconciler; hecho externo finalizado, identidad/monto verificados o funding sintético PAPER con manifest | EXTERNAL → AVAILABLE; suma propia sube, capital externo sube por igual, rendimiento no cambia | UNVERIFIED_EFFECT mantiene PENDING_EVIDENCE; repetir misma effect_key |
| WITHDRAWAL / ExternalFlowCommand | Reconciler; retiro ya observado, no una orden; cobertura completa y saldo disponible suficiente | AVAILABLE → EXTERNAL; capital externo neto baja, no pérdida | Si contradice proyección, congelar portfolio y reconstruir historial; no inventar saldo ni tomar una reserva ajena |
| RENT LOCK / RentCommand | Reconciler; cuenta/address y depósito on-chain comprobados | AVAILABLE → RENT_LOCKED; saldo propio total no cambia | UNVERIFIED_EFFECT; reintento por efecto de account creation |
| RENT RETURN / RentCommand | Reconciler; cierre y abono finalizados; misma cuenta/asset | RENT_LOCKED → AVAILABLE por monto recuperado | No asumir retorno total; remanente sigue restringido hasta evidencia |
| RENT WRITE_OFF / RentCommand | Reconciler + aprobación de pérdida demostrada | RENT_LOCKED → FEE_EXPENSE; pérdida explícita | No inferir pérdida de timeout; evidencia/approval exigidos por actor-context |
| FEE / FeePostingCommand | Reconciler; fee externa finalizada y no incluida en fill; identidad de pagador | RESERVED o AVAILABLE → FEE_EXPENSE; una línea económica por categoría/índice | INCLUDED_FEE se rechaza como INVALID_AMOUNT; fee desconocida mantiene portfolio no reconciled |
| ADJUSTMENT / AdjustmentCommand | Operador autorizado + evidencia independiente; causa OPENING_BALANCE/VERIFIED_EXTERNAL_DIFFERENCE/RECOVERED_MISSING_EFFECT | ADJUSTMENT_CLEARING ↔ AVAILABLE según diferencia demostrada, nunca compensación arbitraria | UNAUTHORIZED_ACTOR o UNVERIFIED_EFFECT; mantener congelado hasta resolución |
| RESERVE / ReservationPostingCommand | Sólo Risk; reserva nueva ACTIVE, revisión 0; misma transacción de autorización y binding | AVAILABLE → RESERVED por cada activo; entrada+fee se agregan si mismo activo; asignación única por reserva | INSUFFICIENT_AVAILABLE o STALE_REVISION no escribe nada |
| RELEASE / ReservationPostingCommand | Sólo Risk/reconciler; ACTIVE antes de firma o finalización autoritativa de ATTEMPTED | RESERVED → AVAILABLE únicamente remanente de esa reserva; estado RELEASED/CONSUMED consistente | RESERVATION_COMMITTED ante UNKNOWN; no TTL para ATTEMPTED |
| INTERNAL_TRANSFER / InternalTransferCommand | Caso de uso Ledger autorizado; misma custodia y mismo activo | AVAILABLE → RENT_LOCKED o COLLATERAL, o retorno a AVAILABLE; no cambia capital ni saldo total | Custodia distinta => UNVERIFIED_EFFECT: se necesita transferencia externa observada, no mover dinero por ledger |
| TRADE / TradePostingCommand | Reconciler; Fill finalizado; binding, cantidades y reserva coinciden | RESERVED → TRADE_CLEARING del input; TRADE_CLEARING → AVAILABLE del output; dos pares independientes | RESERVATION_MISMATCH, UNVERIFIED_EFFECT; no journal con sólo una pierna |
| REVERSAL / ReversalCommand | Reconciler + aprobación; original POSTED, mismo portfolio/mode; aún no revertido | Todas las líneas del original negadas exactamente; reverses_entry_id; una sola reversión permitida | ALREADY_REVERSED devuelve rechazo sin efecto; insuficiencia congela/reconstruye antes de corregir |
| DERIVATIVE_SETTLEMENT / DerivativeSettlementCommand | Reconciler sandbox; liquidación/funding/PnL final observado, instrumento lineal soportado | PNL_CLEARING ↔ COLLATERAL en settlement asset; signología según beneficio/pérdida | UNSUPPORTED_MARGIN o UNVERIFIED_EFFECT; ningún cambio por mark no realizado |

INTERNAL_TRANSFER con custody distinto no equivale a transferencia bancaria/on-chain: la operación
real queda fuera de alcance. Un par de hechos externos correlacionados requiere ReconciliationRequest.
PAPER capital inicial sólo DEPOSIT sintético con evidencia de configuración, una vez por portfolio;
no existe saldo inicial fuera de journal. Los comandos no autorizan depósitos/retiros reales.

Reversal corrige un registro erróneo, no deshace blockchain. Corrección = REVERSAL + comando correcto
con nueva operation_id/effect_key y evidencia que explica ambos, en la misma UoW cuando corresponda.
No puede usarse para liberar fondos de un intento incierto. Los reversos de reserva actualizan
su proyección y estado en la misma transacción, o se rechazan. El original queda consultable.

## Reconciliación, reservas y recuperación

ReconciliationRequest agrupa comandos concretos, finality_evidence_ids, órdenes y finalización de
reservas. Los comandos comparten portfolio/mode y expected_portfolio_revision inicial. Se validan
contra un estado de trabajo secuencial bajo un único lock y la revisión de cartera sube una vez.
Cada JournalEntry tiene ID propio; cada efecto e idempotency key es único. ReconciliationResult
sólo se entrega después del commit. Si cualquier comando falla, ninguno escribe ni emite evento.

Orden de efectos: consumo de input reservado, fees no incluidas, output recibido, liberación de
remanentes, finalización de reserva, proyección, RECONCILED, audit/outbox. Reconciler no reutiliza
fondos liberados para abrir otra operación en el mismo batch. Para una reserva con input y fee
del mismo activo se reserva su suma; el fill y las fees consumen subasignaciones sin excederla.
Fallo confirmado puede consumir sólo fee y liberar el resto; expiración verificada sin fee libera
el total. CONFIRMED insuficiente para journal definitivo: se exige finality del modo/venue.

Eventos existentes journal.recorded y execution.reported se escriben en outbox local atómicamente
con IDs estables; retries no publican duplicados lógicos. Cambio de reserva produce risk.assessed
sólo al autorizar y audit record en cada transición; no inventar una nueva autorización al liberar.
Consumidores deduplican por event_id. Caída antes del commit => rollback; después => lookup devuelve
resultado original. Caída tras envío externo => UNKNOWN y reservas ATTEMPTED persistentes.

Un saldo externo que contradice el ledger crea evidencia y congela entradas (reconciled=false,
CLOSE_ONLY/HALTED según policy). El hecho no se descarta: se conserva PENDING_EVIDENCE/RECONCILIATION
hasta reconstruir su causalidad, identificar reservas afectadas y publicar el batch correcto.
La UI muestra diferencia conocida y cobertura; no presenta el saldo contable previo como disponible.

## Instrumentos, valoración y contratos lineales

Instrument es catálogo versionado, no permiso operativo. ID se registra por venue+tipo+activos+
pool/contrato/expiry; nunca por ticker. Consumidores enlazan instrument_id/revision. Revision
inmutable registra fees/tick/lot/capacidades disponibles en t. Cambiar tick no modifica órdenes viejas:
requiere nueva validación/cancelación conforme al estado real.

TOKEN_SPOT es una ficha de tenencia: no se ejecuta sin SPOT_PAIR/AMM_POOL/CEX_SPOT asociado.
SPOT_PAIR expresa relación de intercambio; AMM_POOL la liga a programa/pool y precisión de activos;
CEX_SPOT expresa reglas de libro del venue. BASE_ATOM significa átomos del activo base. El precio
es quote major por base major. Cantidad q = quantity / 10**base_decimals. Notional exacto = q*p;
al convertir a átomos quote, debitar ceil y acreditar floor. quantity_step/minimum_quantity se
expresan en la unidad declarada, y minimum_notional en quote Money. Fuera de lot/tick no se corrige
silenciosamente: OFF_LOT/OFF_TICK. El sizing previo puede redondear según doc08 y volver a validar.
AMM no tiene tick discreto (price_tick=null); la quote y el min_output limitan la ejecución.

LINEAR_FUTURE/LINEAR_PERPETUAL son futuros cash-settled lineales con margin aislado en quote,
settlement=quote=collateral, sin colateral cruzado ni inversos/quanto. Otros modelos devuelven
UNSUPPORTED_MARGIN. Quantity CONTRACT_LOT es número entero de lotes; cada lote representa
base_atoms_per_contract_lot. Base económica = lots*multiplier/10**base_decimals.
Notional = abs(base_económica)*mark en settlement major. PnL realizado = signed_base*(exit-entry),
fee aparte; mark no realizado sólo cambia valoración, nunca journal de cash.

MarginTier aplica al notional total, tramos ordenados estrictamente por upper bound, último
límite cubre posición entera; no extrapolar fuera de tabla. initial_margin_ratio >=
maintenance_margin_ratio > 0 y <= 1; max_leverage >= 1 y no permite superar 1/initial_ratio.
IM requerida = ceil(notional*IMR en settlement atoms) + fee buffer; MM análoga. Falta de tier,
mark/index/FX o cobertura => rechazo. Cambio de tier necesita revalidar, nunca liberar garantía
por dato viejo. Funding positivo paga long y recibe short: -signed_base*mark*rate por intervalo;
rate es observado por funding_interval_s, no tasa anual ni predicción del siguiente pago.
Créditos se redondean floor, débitos ceil; remanente subátomo queda en evidencia de cálculo,
no se transforma en balance. Instrument expiry sólo para futuros; perpetuo expiry=null.

FeeSchedule declara maker/taker bps y asset; maker puede ser negativo (rebate). El laboratorio
no usa rebates como ingreso antes de confirmación; su evidencia se contabiliza como liquidación
positiva aparte, no como fee negativa. Rate/asset deben coincidir con unidad de cálculo del venue.

MarginSnapshot conserva sus nombres históricos: position_notional, collateral y maintenance_margin
son settlement major; mark/index son quote major/base major; position_contract_lots lleva signo.
CexChildOrder.requested_atoms/filled_atoms significan BASE_ATOM o CONTRACT_LOT según quantity_unit
explícita; 0 <= filled <= requested. requested > 0. Estos nombres se conservan por trazabilidad,
no implican que un contrato sea una moneda. Limit_price usa unidad de Instrument.

LegPlan tiene 2–4 LegInstruction ordenadas, cada quantity/unit/instrument/revision explícito.
Ratios son racionales positivos (numerator/denominator), side determina signo. intent_ids coincide
exactamente con legs sin duplicados. worst_unhedged_loss se expresa en loss_asset_id major, e
incluye fees de salida; no se suma USDC y SOL. max_leg_skew_ms limita la antigüedad de quotes;
hedge_deadline_ms limita exposición sin cubrir, ambos medidos con Clock monotónico del proceso.
Persistir deadline UTC de recuperación; un reinicio no lo extiende.

Atomic=true sólo con certificado de una transacción que agrupa todas las piernas en el mismo
venue/chain y decodificación completa. Cross-venue siempre false. Al fallar una pierna, dejar de
emitir, solicitar cancelación, reconciliar UNKNOWN y sólo después proponer reducción bajo Risk.
No reenviar otra pierna por timeout ni prometer cobertura exacta. Margin/LegPlan no habilitan live.
VenueExecutionIntent se valida por Risk de venue y no se pasa al signer Solana. Sus cantidades,
collateral/fee caps, instrumento/revisión, side, limit_price, TIF, epoch y expiry quedan vinculados
a una reserva de venue. La solicitud HTTP nunca elige libremente reservation_id.

## Consumo y pruebas

T-031 implementará cuentas/posts y oracles; T-032 proyecciones/FIFO/NAV; T-050/T-051 reservas bajo
lock; T-054/T-055 paper/reconciliación; T-068 valuación de historial; T-098 reconciliación Solana;
T-101 libro y parciales; T-102 margin; T-103 legs. El harness T-033 consume puertos con fixtures,
no implementa estos casos de uso anticipadamente. T-093 firma sólo ExecutionIntent spot Solana.
Todos deben leer este contrato y escenarios; la reescritura de fichas viene después de estabilizar
GD-09/GD-11/GD-12. Validación documental de escenarios no implementa el ledger del producto.

## Precisiones de binding y evolución de eventos

VenueRiskAuthorizer.authorize(VenueRiskRequest) devuelve VenueRiskResult: DENIED sin reserva,
o APPROVED con VenueReservation creada junto con journal RESERVE y outbox. Relee portfolio,
Instrument revision, tiers y cobertura; la proposal no es permiso. Comprueba spot/collateral/fee
por activo, caps globales, exposición de todas las piernas, cuenta aislada y policy/control_epoch.
VenueExecutionIntent.intent_hash usa JSON canónico de todos sus campos salvo id, reservation_id e
intent_hash; incluye Instrument completo (revision y reglas), decision_id y fencing_token. La reserva
conserva ese hash y todos los límites. Antes de envío se compara objeto exacto + estado autoritativo.
Cambiar side, quantity, unit, TIF, limit, caps, Instrument o reduce_only invalida autorización.
Las reservas de venue usan la misma máquina ACTIVE/ATTEMPTED/CONSUMED/RELEASED. Los rechazos de
Risk no llaman Exec. No tratar un VenueReservation como Reservation spot mediante casts.

Reservation/ExecutionIntent/RiskAssessment spot incorporan rent_asset_id y max_rent_atoms.
Se reserva input + fee + rent por activo (sumar cuando coinciden), sin contabilizar rent como
fee. Los campos de rent e instrumento/revisión forman parte de intent_hash y del decoder signer.
ATA desconocida o gasto de rent mayor al cap => denegar. DENIED tiene todos los caps en cero.
Una pérdida total estresada puede incluir rent como pérdida potencial; NAV conserva su valor
recuperable sólo con evidencia. Esa decisión prudente no transforma el asiento en una comisión.

REBATE usa FeePostingCommand con rebate=true e included_in_fill=false; debe existir abono externo
confirmado y no incluido en output. TRADE_CLEARING → AVAILABLE, no fee negativa ni ingreso supuesto.
FEE exige rebate=false. Rent WRITE_OFF requiere approval_evidence_id no nulo y autenticado.

LedgerOperation materializa la máquina de registro (request/hash/state/journal/error/updated_at).
REJECTED no cambia balances; reintentar datos nuevos necesita nueva operación y causalidad explícita.
PENDING_EVIDENCE puede volver a VERIFIED con evidencia nueva, conservando la misma identidad económica;
la actualización de evidence_ids es una revisión de preparación auditada, anterior al hash definitivo
VERIFIED. Después de VERIFIED el payload es inmutable. POSTED no se vuelve a preparar.

Todos los eventos de este draft se etiquetan `.v2` y EventEnvelope.schema_version=2.0.0.
Los registros v1 históricos se conservan; se migran explícitamente con el registro R2 o se ponen
en cuarentena. No publicarlos como v2 cambiando sólo el nombre sin validar el payload completo.
No existen consumidores de producto desplegados; esto es migración de especificación preimplementación.

## Oracles y propiedad de efectos

Los 20 casos de `scenarios/financial.json` fijan comandos concretos, cuentas, saldos iniciales,
líneas esperadas, resultado, estado final y cálculo independiente. FIN-08 libera la totalidad
de reservation:1 (10 USDC); los 20 USDC restantes pertenecen a reservation:other. Una liberación
no puede consumir esa asignación ajena. FIN-15 prueba dedup con revisión obsoleta 7 frente a 8;
el journal original se devuelve sin avanzar la revisión. FIN-17 rechaza el post al llamador,
pero conserva la operación en PENDING_EVIDENCE: no es una pérdida ni una operación descartada.

Cada fee de Fill se registra exactamente una vez mediante FEE con effect_key derivada de
(venue, signature/order, fill index, fee category/index), en el mismo batch que TRADE. TRADE
registra exclusivamente input/output netos declarados; no suma automáticamente fee_atoms.
El adaptador documenta si la cotización ya deduce la fee del output: en ese caso queda incluida
en Fill/output y no se crea otro FEE. Un funding de derivado pertenece exclusivamente a
DERIVATIVE_SETTLEMENT (PNL_CLEARING/COLLATERAL), nunca a FEE ni a TRADE. Rebates confirmados
pertenecen a REBATE. La unicidad de external_effect_key abarca las distintas operaciones.

InstrumentReader será propietario de consulta del catálogo; ingestión T-022 y T-100 producen
revisiones certificadas de AMM/CLOB y T-102 de derivados sandbox, con evidencia y valid_from.
T-009 define sólo persistencia, no fabrica reglas de venue. Replay T-033 selecciona la revisión
disponible al tiempo simulado; T-049 decide compatibilidad; T-050/T-051 autorizan cantidades;
T-093/T-094 comparan instrumento, rent y todos los caps contra la decodificación. T-055/T-098
contabilizan únicamente efectos finalizados. Las interfaces auxiliares se completan en GD-12.

El validador documental verifica el tipado y la aritmética de estos resultados esperados,
incluido un reverso cuya identidad se compara por cuenta (el orden JSON no altera el asiento).
Las pruebas de mutación del validador detectan balances erróneos, conservación rota, cuentas de
reverso alteradas y liberación de UNKNOWN. No sustituyen las futuras pruebas de producto.
