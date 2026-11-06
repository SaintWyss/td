# Backtesting y contabilidad

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Motor de eventos

Replay ordena por `available_at`, secuencia de origen y ID como desempate estable. En t sólo se entregan datos disponibles. El mismo evaluador de estrategia y riesgo se usa en paper. Reloj, aleatoriedad, precios y ejecución son puertos inyectados. Fijar semilla, build, dataset manifest, configuración y política. Determinismo de CPU se exige; GPU puede tener tolerancia explícita y no se usa para reconciliación monetaria.

Dos niveles: exploratorio con OHLCV/costos asumidos y confirmatorio con granularidad suficiente para la estrategia. Una vela de un minuto no valida scalping de un segundo, orden intrabar de stop/target ni prioridad en un libro. Cuando ambos extremos tocan barreras en la misma vela, usar peor caso o excluir el experimento confirmatorio, nunca escoger el orden rentable.

## Modelos de ejecución

AMM CPMM: reservas y fees observadas por evento, tamaño con impacto, latencia antes de consultar estado ejecutable y salida inversa. CLMM/bin y router multihop necesitan estado completo o quote archivada; si falta, `UNSUPPORTED_SIMULATION`. Una quote es oferta estimada, no fill garantizado. Paper aplica escenario base y estresado con rechazo, slippage adicional y latencia medida; no simula poder comprar cantidad infinita al cierre de vela.

CLOB: consumir profundidad sucesivamente; órdenes pasivas requieren modelo conservador de cola y cancelación, sin fills por simple toque. Congestión, fees de fallos, rent/ATA y wraps tienen entradas separadas. Router fees incluidas en `out_amount` no se descuentan otra vez. La simulación documenta qué fees son incluidas y cuáles adicionales.

## Libro contable

Journal de doble entrada por activo: balances de cash/inventory/fees/external flows y cuenta de contrapartida, cantidades atómicas con signo. Suma por activo de cada asiento=0; una conversión es dos pares contables, no sumar SOL y USDC en una igualdad. Fees separadas; rent recuperable es activo restringido, no pérdida inmediata; rent irrecuperable es gasto. FIFO calcula costo realizado; cada fill y fee externa tiene effect_key única.

NAV = efectivo convertido + valor conservador de liquidación de inventario − obligaciones. Registrar mid mark y liquidation mark por separado. Si desaparece liquidez, liquidación puede ser cero aunque haya un último precio alto. No eliminar el token del historial. PnL no realizado cambia con marks; depósitos/retiros no son rendimiento.

## Salida del experimento

Reporte con curva diaria, trades, abstenciones, exposición, costos desglosados, cobertura, comparación emparejada, incertidumbre y fallos. Baselines comparten universo y calendario: buy-and-hold desde primera elegibilidad conocida, límites de capital equivalentes y tratamiento de tokens muertos. BTC/SOL buy-and-hold es referencia de mercado adicional, no sustituto del benchmark comparable.

Pruebas golden incluyen un swap rentable bruto pero negativo neto, token ilíquido, fee de fallo, duplicado, ingreso externo, price gap, salida parcial CEX y corte entre fill/journal. Golden esperado se calcula manualmente en fixture; no se obtiene llamando a la función bajo prueba.

## Contratos financieros R2

[Operaciones, instrumentos y unidades](contracts/financial-operations.md) y ADR-019 especifican
LedgerPostRequest, LedgerPostResult, ReconciliationRequest y catálogo Instrument. Son normativos
para depósitos/rent/fees/reservas/reversos y liquidación; LedgerWriter ya no recibe Fill aislado.
Los metadatos de Instrument y los escenarios son requisitos de implementación, no servicios activos.
