# Inteligencia de wallets y traders

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Qué se puede observar

Wallet no equivale a persona ni cartera completa. Un mismo operador puede usar múltiples cuentas, CEX, préstamos o hedges invisibles. La agrupación se etiqueta hipótesis, con señales y confianza, sin doxxing. Transferencia no es venta; entrada de tokens no es compra; airdrop no tiene costo de adquisición necesariamente cero.

Puerto `TraderProfiler.build(WalletHistory, ValuationPolicy) -> TraderProfile`. Reconstruir token accounts por owner, swaps, wraps SOL/wSOL, comisiones, depósitos/retiros y transferencias. Mantener inventario FIFO para PnL realizado observable y valor de liquidación conservador para no realizado. Lotes cuyo costo se desconoce quedan `UNKNOWN_COST`; ROI agregado puede ser null. Fees SOL convertidas al precio conocido en ese momento, con evidencia.

## Evaluación temporal

Selección de wallets sólo con ventana train terminada. Registrar todas las candidatas, incluidas perdedoras, inactivas y con cobertura incompleta. Medir cobertura de transacciones, edad observada, PnL neto, drawdown, duración, turnover, concentración y estabilidad por régimen. Depositar dinero no eleva retorno; usar TWR entre flujos externos conocidos y no estimar capital total desde un ranking público.

Score de investigación: percentiles winsorizados de retorno neto y estabilidad menos drawdown/concentración/costos, calculados dentro de cohortes comparables. Con menos de 90 días observados o cobertura <95%, mostrar perfil descriptivo sin habilitar copy. Son filtros de calidad iniciales; no garantizan skill. Bootstrap por bloques de días y clusters evita considerar cada wallet correlacionada como evidencia independiente.

## Copy trading filtrado

S10 reproduce una señal después de su disponibilidad propia, latencia de detección, decisión y ejecución. No usa precio del trader líder ni su tamaño relativo si capital no observable. Se solicita nueva quote para el tamaño del follower, límites de riesgo propios y TTL de señal. No copiar si el activo ya tuvo un movimiento >umbral predefinido o si la ventaja estimada no cubre costos. Salidas pueden llegar tarde: límite temporal propio y seguimiento independiente.

S11 usa flujo agregado de wallets seleccionadas previamente, sin copiar cada trade. Comparar contra wallets aleatorias emparejadas por edad/actividad y contra versión sin inteligencia de traders. Ningún ranking ganador del período test se introduce en train.

## Fallos y pruebas

Historial truncado crea `coverage=PARTIAL`, no PnL cero. Transacción null o reorg conserva registro provisional hasta resolver. Fixtures incluyen transferencias propias, airdrops, inversión con costo desconocido, cuentas cerradas, rutas multihop y fees fallidas. Perfil aprobado requiere balances reconstruidos consistentes con snapshots observados dentro de tolerancia atómica explicada. Diferencias no resueltas deshabilitan el score financiero, preservando métricas de actividad válidas.

## Entradas y temporalidad R2

[Features y estrategias](contracts/features-and-strategies.md) fija fuente, unidad, ventana, disponibilidad y estimando. El catálogo tipado `contracts/feature-catalog.json` es normativo para producir/consumir features; `contracts/strategy-specs.json` contiene las 20 evaluaciones. No reemplazar datos faltantes por valores de conveniencia.
