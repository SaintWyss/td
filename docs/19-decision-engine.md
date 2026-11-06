# Motor de decisión y abstención

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Entrada y procedimiento

`DecisionContext` contiene FeatureSnapshot, señales vigentes, TokenAssessment, PortfolioView, modelos/estrategias aprobados para paper, política y cobertura. Evaluación pura en orden fijo:

1. Validar identidad, timestamps, calidad y versiones. Si falta un input crítico, `NO_TRADE/DATA_INCOMPLETE`.
2. Excluir instrumentos no elegibles, estrategias no certificadas y predicciones expiradas. Registrar cada causa.
3. Verificar expectativa calculada para tamaño orientativo, costos y horizonte comparable. Un forecast bruto no se resta dos veces: marcar `cost_basis`.
4. Aplicar umbral preregistrado: límite inferior de expectativa neta >0 y mejora mínima sobre baseline según experimento. No interpretar probabilidad de alza como tamaño.
5. Ordenar candidatos por retorno neto conservador sobre pérdida estresada; empate por menor costo, luego strategy_id. Límite una entrada por instrumento por ventana de 60 s.
6. Solicitar dimensionamiento y reserva a Risk con nueva quote; si tamaño altera costo, reevaluar neto. Máximo dos iteraciones para evitar loops.
7. Guardar Decision y causas, incluso abstenciones, con IDs de evidencia, modelo, política, snapshot y correlation_id.

El score tiene significado dentro de un mismo horizonte/unidad. No comparar arbitrariamente retorno a 30 s y 4 h sin llevarlos al modelo de utilidad preregistrado. Inicialmente un solo horizonte operativo evita ese problema.

## NO_TRADE

Códigos estables: DATA_INCOMPLETE, DATA_STALE, TOKEN_UNSUPPORTED, TOKEN_RISK, NO_ROUTE, COST_EXCEEDS_EDGE, LOW_CONFIDENCE, STRATEGY_DISABLED, MODEL_EXPIRED, RISK_DENIED, BUDGET_EXHAUSTED, POSITION_PENDING, SYSTEM_HALTED y NO_SIGNAL. Se permite más de un código; el principal sigue el orden de controles. La UI muestra explicación basada en hechos, no una narrativa inventada.

## Qué no decide

Decision no modifica límites, no firma, no promueve modelos y no convierte un resultado de LLM en reserva. Las reglas de decisión son versionadas y ensayadas; el motor estadístico puede abstenerse por incertidumbre, Risk puede vetar aun con señal fuerte.

Pruebas: datos futuros, probabilidad alta con costos negativos, dos señales idénticas, modelos vencidos, quote que cambia tamaño y conflicto de policy revision. Fixture positivo verifica candidato y reserva; fixture negativo verifica ausencia total de intención ejecutable. Reproducir mismo contexto produce mismo resultado y hash, salvo IDs generados por el caso de uso fuera del dominio.

## Contratos R2 normativos

Leer [features y estrategias](contracts/features-and-strategies.md), `contracts/feature-catalog.json` y `contracts/strategy-specs.json`. Esos contratos precisan las entradas, ventanas, estimandos, salidas puras y reglas de disponibilidad de esta revisión.
