# Motor determinista de riesgo

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

La política canónica está en `contracts/policy-defaults.json`. Sólo Risk puede crear una reserva. Cualquier error de parser, dato crítico ausente, conflicto o estado desconocido deniega nuevas entradas; no se convierte en aprobación parcial.

## Límites iniciales de laboratorio

NAV paper inicial: 10.000 USDC. Pérdida estresada por operación ≤0,5% NAV; exposición por activo ≤1%; total invertido ≤10%; máximo cinco posiciones; máximo una intención pendiente por activo. Pérdida diaria ≥2% o semanal ≥5% activa CLOSE_ONLY; drawdown desde máximo ≥10% activa HALTED. Día/semana contables UTC, semana lunes; incluir fees, realizado y valoración conservadora. Reiniciar proceso no reinicia pérdidas ni high-water mark.

Para memecoins se dimensiona con pérdida posible del 100% del notional más fees máximas: `q <= min(0.005*NAV/(price*(1+cost_buffer)), asset_cap_remaining/price, total_cap_remaining/price, executable_size_cap)`. No reducir pérdida estresada a la distancia de stop. El tamaño final se redondea hacia abajo a átomos; si queda cero, denegar. Sin NAV confiable o conversión USDC/USD válida, no abrir.

Frescura: features mercado ≤15 s, assessment token ≤60 s, quote de ejecución ≤2 s. Estos deadlines pertenecen al perfil de laboratorio y se medirán; un proveedor lento puede hacer imposible operar y ello es resultado válido. Impacto ≤100 bps; slippage máximo 100 bps; costo ida/vuelta ≤200 bps y además inferior al edge conservador. Son filtros de admisión, no garantía de precio.

## Reserva atómica

Bloquear fila Portfolio, leer positions + reservas + intentos inciertos, comprobar mode/policy revision, límites y saldo; insertar Reservation única por decision_id y actualizar revision; commit con outbox. Lease de entrada 5 s. Si no hay intento firmado al expirar, liberar mediante transición durable. Si hay envío posible, mantener exposición hasta conciliación. Fencing token invalida writers antiguos. Dos solicitudes concurrentes que excedan el límite no pueden ser aceptadas juntas.

El permiso vincula wallet, chain, input/output mint, amount/max_input, min_output, programas permitidos, fees máximas, quote_hash, policy_revision, fencing_token y expiry. Antes de firma, el executor revalida modo, reserva y simulación. El signer inspecciona bytes/lookup tables y vinculación, no confía en etiquetas ni mensajes LLM.

## Modos y salidas

RUNNING permite evaluar; CLOSE_ONLY prohíbe aumentar exposición y autoriza únicamente ventas que reduzcan posición, dentro de integridad, fees y programas permitidos. HALTED bloquea firmas nuevas incluidas salidas; un operador puede solicitar CLOSE_ONLY tras revisar el incidente. No ordenar una venta masiva ciega. El kill switch es durable, incrementa control_epoch y hace que futuras firmas fallen, pero no cancela transacciones ya emitidas.

Datos de alpha vencidos no impiden por sí solos una salida de riesgo; siguen siendo obligatorios balances, identidad, quote, fee cap y control de posición. Cuando no hay mercado de salida, marcar UNLIQUIDATABLE y estimar pérdida conservadora. No anunciar cierre sin fill. Cualquier cambio que relaje límites requiere revisión humana y versión; endurecer puede automatizarse si está autorizado por política.
