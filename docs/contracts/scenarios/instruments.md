# Oracles independientes de instrumentos — R2

Todos los valores son sintéticos. Contratos: Instrument, MarginSnapshot, LegPlan,
VenueExecutionIntent; reglas en `../financial-operations.md`. Errores sin journal ni envío.
Las cuentas iniciales y finales son idénticas salvo que se declare una liquidación en FIN-13.
Los cálculos siguientes son referencias manuales para T-050/T-100/T-101/T-102/T-103;
no constituyen pruebas de un motor implementado. Requisitos R-050/R-100/R-101/R-102/R-103.

| ID | Entrada concreta / unidad | Operación y resultado esperado | Invariante / negativo |
|---|---|---|---|
| INS-01 | SOL 9 decimales; USDC 6; 1,250,000,000 base atoms, precio 100 USDC/SOL | 1.25 SOL × 100 = 125 USDC = 125,000,000 quote atoms; BUY debita ese notional | Instrument.quantity_unit=BASE_ATOM; nunca interpretar átomos como contratos |
| INS-02 | 10 CONTRACT_LOT; multiplier=10,000,000 SOL atoms/lot; SOL decimals=9; mark=150 | base económica=0.1 SOL; notional=15 USDC; IMR=0.1, MMR=0.05, fee buffer=0.01 USDC: IM=1.51, MM=0.76 USDC | Margen aislado quote=settlement=collateral; si asset difiere, UNSUPPORTED_MARGIN |
| INS-03 | Mismos 10 lotes long; entry=100, exit=150 | PnL realizado=0.1×(150−100)=5 USDC; FIN-13 define post +5 collateral | Mark=150 sin cierre sólo PnL no realizado; journal vacío |
| INS-04 | 10 lotes long; base=0.1 SOL, mark=150, funding rate=0.001/8h | Pago=−0.1×150×0.001=−0.015 USDC=−15,000 atoms; short cobra +15,000 | Una liquidación por intervalo/effect_key; no extrapolar próximo funding |
| INS-05 | CEX spot tick=0.05; lot step=100,000 SOL atoms | Limit 100.03 → OFF_TICK; quantity 150,000 → OFF_LOT; 100.05 y 200,000 sí satisfacen tick/lot | Ningún redondeo silencioso dentro de submit; no mutación al fallar |
| INS-06 | USDC 6 decimales; crédito exacto=0.0000019; débito exacto=0.0000011 | floor crédito=1 atom; ceil débito=2 atoms; residuos=0.9 y 0.9 micro-USDC en evidencia | No persistir float; no crear saldo con residuos subátomo |
| INS-07 | Dos piernas, +1 SOL spot y −100 lotes lineales de 0.01 SOL | Delta base=1−100×0.01=0; primera leg fill +1 y segunda UNKNOWN → delta conocida +1, exposición de segunda desconocida | Cancelar/reconciliar antes de proponer hedge; no prometer neutralidad; cross-venue atomic=false |
| INS-08 | Una fee maker −2 bps; notional 100 USDC | Rebate potencial=0.02 USDC, journal vacío hasta evidencia; confirmado=20,000 USDC atoms vía REBATE | No reducir fee cap por ingreso no confirmado; FIN-14 ilustra post |
| INS-09 | IMR=0.1, MMR=0.05, max_leverage=20 | 1/IMR=10; catálogo inconsistente → UNSUPPORTED_MARGIN | No aprobar 20× ni modificar el tier; registrar evidencia y cuarentena |
| INS-10 | Long 1 SOL@100 y short 100 lotes@100; quote skew 201ms; cap 200ms | LegPlan se rechaza EXPIRED antes de reservar/emitir | Igual a 200ms admisible temporalmente; los demás gates siguen obligatorios |

Validación futura: assertions exactas de Decimal/enteros y estados, incluyendo el caso inválido
por fila. Comparar magnitudes en la unidad declarada; no tolerancias de floats. Los valores
esperados derivan de multiplicación/división y redondeo escritos aquí, no del código bajo prueba.
