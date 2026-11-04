# Motor de estrategias y catálogo experimental

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

El catálogo normativo está en `strategies/catalog.json` y las fichas S01–S20 en `strategies/`. Contiene las 19 familias pedidas más selección por régimen como metapolítica: descubrimiento, momentum, scalping, reversión, breakout, false breakout, imbalance, noticias, sentimiento, copy, smart money, liquidez, grid, market making, arbitraje, funding, delta-neutral, tendencia, salida dinámica y régimen. Los números son IDs estables y no orden de implementación.

## Puerto y ciclo

Cada estrategia implementa `evaluate(snapshot, portfolio_view, config) -> Signal | Abstention`. Inputs son inmutables, tienen as_of, available_at, quality y hashes. El contrato `StrategyConfig` fija familia, versión, parámetros, capacidades y horizonte. No tiene SDK, HTTP, acceso a DB, wallet ni promotor de modelos. Un mismo código de señales se usa en replay y paper; sólo cambia el adaptador de reloj/datos/ejecución.

Una señal declara `instrument_id`, lado, horizonte, expectativa neta estimada, incertidumbre, TTL, evidencias y motivos de salida. La estrategia propone; Decision selecciona; Risk veta y dimensiona. La ausencia de señal es explícita y contabilizada. Estrategias deshabilitadas no producen señales operables.

## Ciclo de vida

DRAFT → SPECIFIED → BACKTESTING → REJECTED o PAPER_CANDIDATE → PAPER_RUNNING → REVIEWED → RETIRED/READY_FOR_REVIEW. `READY_FOR_REVIEW` no habilita live. Cambiar parámetros, target o universo genera versión y nueva familia de ensayos cuando corresponda. Un cambio después de observar holdout no «corrige» retroactivamente un resultado fallido.

Todas las fichas heredan G-DATA, G-LAB y G-PAPER de `34-acceptance-criteria.md`, límites `contracts/policy-defaults.json` y pruebas de costos/latencia/cobertura. Además tienen hipótesis, algoritmo preciso, datos, entradas/salidas, riesgos, experimentos y condiciones particulares. La elegibilidad depende de VenueCapabilities: L2 para imbalance/making; funding/margen para derivados; atomicidad o hedge explícito para arbitraje.

## Composición

Primera versión opera S02 y evalúa S18 como control. S01 observa desde V2. S19 es política de salida, nunca genera entrada. S20 selecciona estrategias con features de régimen conocidas en t, entrenadas sólo en pasado. No se suman señales correlacionadas como oportunidades independientes: agrupar por instrumento y ventana; Decision elige a lo sumo una entrada por instrumento/ventana y Risk cuenta exposición conjunta.

Los parámetros en fichas son valores iniciales de laboratorio para preregistrar; no recomendaciones de rentabilidad. Los agentes no ajustan un umbral hasta que «pase»: cualquier búsqueda debe quedar registrada como ensayo. La falta de datos adecuados rechaza el experimento, no justifica un backtest con supuestos favorables.
