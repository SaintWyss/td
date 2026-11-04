# Inteligencia y seguridad de Solana

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Descubrimiento y cobertura

Primera integración: Raydium CPMM, programa `CPMMoo8L3F4NbTegBCKVNunggL7H1ZpdTHKxQB5qKP1C` documentado [S12], sujeto a cotejo on-chain. `logsSubscribe` por programa alimenta candidatos; luego `getTransaction` y cuentas verifican inicialización y mints. No reconocer una string de log como prueba suficiente. Fijar layout/IDL al commit inspeccionado; upgrade desconocido pone decoder en cuarentena. El decodificador de swaps es una tarea diferente del de creación.

WSS no aporta replay durable. Guardar última firma/slot finalizado; recuperar páginas por dirección con solapamiento y dedup tras desconexión. Si no se puede cerrar el hueco, registrar cobertura `GAP`, sin inventar ausencia de actividad. La cobertura declarada es «pools del programa y versión soportados durante ventanas observadas», no todos los tokens de Solana ni primera compra mundial.

Estado de pool: DISCOVERED → VALIDATED/UNSUPPORTED → OBSERVING → ELIGIBLE/INELIGIBLE → INACTIVE. Elegibilidad es evaluación temporal, puede revocarse. La edad nace de creación on-chain cuando se conoce, y se diferencia de first_seen. Una nueva ruta Jupiter no modifica la fecha de descubrimiento retrospectivamente.

## TokenAssessment

Lee owner del mint y programa, decimals, supply, mint authority, freeze authority, extensiones, cuentas/vaults y último slot. No confundir top token accounts con wallets: agrupar owners y distinguir vaults de protocolos identificados, con evidencia. Mostrar concentración bruta y ajustada; si sólo hay top holders, indicar cobertura y no calcular Gini poblacional ficticio.

MVP bloquea entradas con mint/freeze authority activa, Token-2022, programa/extension desconocida, snapshot crítico vencido, concentración top10 ajustada >50% o top1 >20%, reservas estimadas <USD50.000, antigüedad <30 min, o ausencia de ruta inversa para tamaño propuesto. Estos límites son políticas conservadoras de paper y parámetros de experimento, no clasificación legal de un token.

Extensiones posteriores: TransferFeeConfig exige fee actual/próximo epoch y cap; PermanentDelegate, TransferHook no auditado, NonTransferable, DefaultAccountState frozen, Pausable/confidential/extension desconocida bloquean ejecución. No usar UI amount de tokens con escalado/interés como cantidad atómica. Una simulación exitosa y una quote inversa no garantizan venta futura.

## Riesgo de pool y actividad

Leer reservas reales, owner de vaults, config mutable, permisos de upgrade y cambios abruptos. CLMM/DLMM necesitan ticks/bins completos para profundidad; no inferir liquidez ejecutable desde TVL. Liquidez bloqueada/quemada requiere evidencia de mecanismo y vencimiento, nunca etiqueta del proveedor como prueba absoluta.

Reglas de anomalía: volumen por wallet extremo, ciclos repetidos de compra/venta, compradores concentrados, retiradas >30% en 5 min y actividad correlacionada. Se reporta «patrón compatible con actividad artificial», con confianza/limitaciones. No se identifican personas por wallet ni se atribuye intención privada. Operar contra posibles pumps exige el mismo filtro; TD no coordina compras ni manipulación.
