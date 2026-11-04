# Validación estadística y falsación

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Diseño antes de observar resultados

Preregistrar mecanismo, universo, disponibilidad, target, horizonte, costos, métrica primaria, comparación, tamaño mínimo detectable y máximo de ensayos. Separar desarrollo, validación interna, tests walk-forward y holdout final. Folds iniciales: train 60 días, validación 14, test 14; expandir o rodar según preregistro. Sin 120 días de cobertura, ejecutar sólo exploración o esperar recolección, sin inventar historia.

Purging elimina observaciones de train cuyos intervalos de etiqueta se solapan con validación/test. Embargo mínimo=max horizonte etiqueta y duración prevista de operación; si esquema de folds incorpora datos posteriores al test, aplicar además separación al reinicio de train. Features con ventana retrospectiva sólo usan pasado disponible; escaladores, imputación, selección de features y calibración se ajustan en train. Mantener grupos de token/pool para evitar duplicados cruzados; evaluar generalización a tokens no vistos separadamente.

Holdout: últimos 30 días independientes, acceso único tras congelar propuesta y artefactos. Accesos quedan auditados; cualquier inspección lo convierte en test consumido. Reutilizarlo para tuning exige nueva evaluación prospectiva. Pretraining con corte desconocido impide llamar ciego al histórico de un modelo fundacional.

## Comparación y multiplicidad

Métrica primaria: diferencia media de retornos netos diarios emparejados contra baseline comparable, más expectativa neta por operación como diagnóstico. Registrar trials fallidos, descartados y manuales; no sólo los guardados por una herramienta. Máximo inicial 12 configuraciones por familia y 4 familias por ciclo. Holm con alpha familiar 0,05 para hipótesis confirmatorias; selección de hiperparámetros queda dentro de validación interna. DSR/PSR se reportan con supuestos y número de trials [S31], sin tratarlos como garantía.

Bootstrap por bloques temporales (inicial 7 días, sensibilidad 1/3/14) y clusters de activos/cohortes, 5.000 réplicas seed fija. Reportar n, días, exposición, autocorrelación y dependencia entre wallets. El intervalo debe reflejar correlación y selección; un test i.i.d. sobre miles de ticks no acredita miles de muestras independientes.

## Gates financieros de investigación

Para pasar a candidato paper: límite inferior 95% de expectativa neta >0 y diferencia de retorno diario >0 después de corrección; max drawdown ≤10% en simulación, ninguna violación de límites y resultado neto no negativo con slippage×2/fees+50%. Un escenario de pérdida total de token debe respetar presupuesto estresado. Si el intervalo incluye cero: INCONCLUSIVE; si inferioridad/costos eliminan ventaja: REJECTED. No forzar tamaño de muestra con más trades correlacionados.

Paper prospectivo mínimo 90 días calendario con cobertura ≥95% de sesiones declaradas, evaluación en fechas preregistradas, y muestra efectiva suficiente para el efecto mínimo definido mediante simulación de potencia sobre train. Noventa días no garantizan poder estadístico ni acceso a todos los regímenes. Si faltan regímenes relevantes, restringir alcance o continuar observación. No fijar «35 operaciones» como evidencia suficiente.

## Métricas obligatorias

Expectativa=promedio PnL neto por trade y por notional; win rate=ganadores/trades cerrados; profit factor=ganancias/pérdidas absolutas (sin pérdidas: indefinido, no infinito probatorio). Sharpe sobre retornos diarios netos con anualización sqrt(365) cripto y autocorrelación informada; Sortino usa downside a MAR=0. Drawdown desde máximo de NAV ajustado por flujos; CVaR95 promedio de pérdidas del peor 5% con advertencia de muestra. Turnover=notional negociado/NAV medio. Calibración: Brier, reliability bins y cobertura de cuantiles. Retorno, PnL realizado/no realizado, costos, latencia y persistencia por régimen siempre acompañan estos ratios.

Ablaciones mercado-only, +on-chain, +social, +traders, conjunto completo; placebos con desplazamiento temporal en bloques y señales aleatorias emparejadas. No confundir una asociación social con causalidad. Resultado negativo es conocimiento y motivo válido para no continuar.
