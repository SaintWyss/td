# Costos y sostenibilidad

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Tarifas consultadas y presupuesto

Las tarifas de datos figuran en el catálogo; sólo se contratarían después del onboarding. LLM por millón de tokens en modalidad estándar consultada: GPT-6 Luna USD0,10 entrada/0,50 salida; GPT-6.1 Sol USD2/10 [S17]; Haiku 5.5 contexto corto USD0,10/0,50 [S19]; Gemini 3.1 Flash-Lite USD0,25/1,50 [S21]. No son costos de suscripciones ChatGPT/Claude. Validar tarifa, región, thinking, cache y herramienta facturable en factura real.

Ejemplo estimado, no gasto ejecutado: 500 extracciones/día × (1.000 input +250 output) ×30 =15M input y3,75M output. A tarifa Luna: USD3,375. Veinte investigaciones/día × (8.000+1.000) ×30 con Sol =4,8M input y0,6M output =USD15,60. Total tokens USD18,975; reservar USD25–30 para variación y fallos. Búsqueda/feeds externos, impuestos, electricidad y almacenamiento se agregan; no están incluidos en el cálculo.

| Perfil | Presupuesto mensual propuesto | Naturaleza |
|---|---:|---|
| Laboratorio local sin LLM | USD0–15 + electricidad | Estimación; datasets/fixtures y cuotas gratuitas, cobertura limitada |
| Paper con RPC Developer + LLM cap25 + backup estimado5–15 | USD79–89 + impuestos/energía | 49 documentados + límites/estimaciones |
| Paper anterior + Birdeye Lite | USD118–128 | Integración opcional; revisar CU/retención |
| Continuidad VPS | añadir USD15–40 | Estimación de planificación, proveedor no contratado |
| Datos premium/latencia extrema | sin presupuesto aprobado | Bloqueado hasta cotización y evidencia de valor |

## Control económico

Cap inicial total configurable USD100/mes, por defecto sin suscripciones habilitadas; no significa autorización de compra. Habilitar la variante con Birdeye requiere aumentar presupuesto revisado. LLM cap25 mensual, daily2 y por job0,50 extracción/2 investigación como límites máximos; estimar peor caso antes de llamada y liquidar contra usage. Jobs pequeños no necesitan gastar su cap.

Presupuesto usa reserva transaccional, currency USD, día UTC y tarifa versionada. Fallos inciertos mantienen reserva conservadora hasta conocer usage o cierre contable; alertas cuando consumo estimado difiere de factura. Reducción automática: dedup→caché→modelo barato certificado→menor frecuencia→abstenerse. Nunca omitir riesgo o conciliación para financiar research.

Infra/capital se separan: PnL de ejecución descuenta fees/impacto/financiación; PnL económico descuenta además APIs, cómputo, datos y almacenamiento asignados. Reportar ambos para evitar mostrar una estrategia positiva sólo porque ignora costo fijo.

Electricidad: medir kWh con potencia media y horas reales; fórmula kW×horas×tarifa local. No convertir USD a ARS usando cotización inventada. Hardware nuevo no es requisito inicial; si el dataset supera cuota, reducir universo o archivar antes de proponer compra.
