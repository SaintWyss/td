# Features, estrategias y Decision — contrato normativo 1.2

Fecha 2026-11-06. ADR-020. `feature-catalog.json` define 62 variables individualmente;
`strategy-specs.json` fija las entradas y las reglas de las 20 estrategias. Sus fichas conservan
hipótesis, riesgos y experimento; la sección R2 elimina ambigüedades de cálculo. No hay estrategias
aprobadas por crear estos contratos. `enabled=false` sigue siendo el valor de los ejemplos.

## Fuentes, resolución y tiempo

Una feature se identifica por (feature_id, definition_version, instrument_id, revision,
window_start, window_end, available_at, source_ids). `name` es el nombre canónico sin prefijo F-;
no se admite un nombre libre como forma de descubrir un cálculo. FeatureValue.value es decimal
string o null; conteos y códigos de régimen se codifican como enteros decimales en ese campo.
Los tipos observados/derivados/estimados/predichos están separados en el catálogo. Un score de
sentimiento o anomalía no es probabilidad. Los importes originales permanecen en átomos exactos.

Las fuentes son contratos normalizados, no promesas de campos de una API. El adaptador debe
probar el mapping desde su payload autorizado y conservar parser_version, raw hash y Observation.
Trade agrega trader_address nullable; si el decoder no lo resuelve no se calcula unique_buyers.
Bar se deriva de Trade con cobertura, orden y decimales del instrumento; no de un precio agregado
sin volumen. Los eventos BAR/DERIVATIVE/SOCIAL son clases de Observation, no nuevos permisos.
Open interest, liquidaciones, noticias y sentimiento pueden quedar EXTERNAL_BLOCKED aunque su
contrato local esté completo. Licencia ausente impide obtener/guardar los datos, incluso para replay.

Todas las ventanas usan UTC. Barras [start,end), sólo cerradas con end<=decision_at; agregados
por eventos (t-window,t]. Un evento exactamente en end pertenece a la barra siguiente. availability
se fija al completar normalización/validación; >=received_at y >=tiempos de todas las dependencias.
El reloj histórico usa available_at, nunca published_at como sustituto. Seleccionar la última
revisión cuya disponibilidad sea <=decision_at; una corrección posterior nunca cambia el pasado.
Empate se resuelve por (available_at, revision, id). Fuentes sin event_time pueden usarse para
noticias según recepción, pero no para crear retrospectivamente barras o intervalos de swaps.

Cobertura completa significa que todo el intervalo consultado tiene cobertura certificada del
source universe declarado. No equivale a conocer toda la blockchain. No rellenar huecos de swaps,
precios, holders ni mensajes con ceros. Una ventana sin trades es MISSING para OHLC y ratios;
conteo cero sólo es observable con cobertura completa y semántica de conteo declarada. Correcciones
se agregan con nueva disponibilidad. Cada feature INVALID/MISSING/STALE invalida sólo las familias
que la requieren. Null no se transforma en cero ni en señal de salida ejecutada.

Se calcula con enteros o Decimal precisión 80; divisiones, sqrt/exp se redondean HALF_EVEN a 18
fraccionarios al publicar el derivado; overflow del rango NUMERIC(38,18) => NUMERIC_OVERFLOW.
Para dinero rigen floor de créditos y ceil de débitos; esa regla no se sustituye por HALF_EVEN.
Cada valor expira según su validity_s, también limitado por expiración de la fuente. Bar de minuto
publicada tarde no extiende la ventana ni hace válido un dato que ya llegó viejo.

Los tamaños/configs de ventanas en 1.2 son los del catálogo y ejemplos preregistrados. Cambiar
lookback, resolución o definición requiere nuevos IDs/versiones y manifest, no reutilizar una
feature 60s para una estrategia que pide 5s. Umbrales comparativos pueden preregistrarse con una
nueva StrategyConfig.version y un trial; no se ajustan después del holdout.

## StrategyInput y salida pura

StrategyInput materializa instrumento, decision_at, snapshot e historial, portfolio, config, policy,
assessment, cost, modelos/predicciones y contextos tipados: bars, books, news, social, wallet_flows,
trader_profiles, derivatives, margin, leg_instruments/quotes, regime/utilities, memory, quote y
exit_context. Arrays irrelevantes quedan vacíos; margin/regime/quote pueden ser null cuando no
se requieren. Cada fila de strategy-specs fija contexto mínimo y algoritmo: no alcanza validar
el JSON si falta ese contexto o no coincide el instrumento, versión, universo, tiempo o permiso.

El evaluador no lee DB/reloj/red. Memory viene del caller y Signal.next_memory es una propuesta
persistida por CAS(snapshot hash, strategy version, memory version) una sola vez. Repetición del
mismo snapshot no aumenta confirmaciones ni reinicia deadline. Las estrategias sin memory previa
usan estado inicial vacío; no se inventan cruces, niveles o máximos retrospectivos.

Signal.side BUY/SELL describe la dirección primaria, y legs contiene propuestas de instrumentos,
ratios, limit prices, post_only y reduce_only, nunca reservas autorizadas. S13 define cinco niveles
por lado (diez propuestas); S14 dos cotizaciones; S15/S16/S17 dos a cuatro piernas. S20 emite
ABSTAIN/META_SELECTION con selected_strategy_id; el orquestador evalúa esa estrategia una vez,
sin recursión S20 ni suma de señales. S01 sólo observa. S19 sólo propone reducción; no abre.
ExitContext proporciona posición, saldo libre, pending_close, critical_risk, reversal_received,
stop_loss_bps e inverse_quote. Un cierre incierto impide otro; falta de ruta produce UNLIQUIDATABLE.

Una señal heurística BUY no inventa expected_net_return ni lower_net_return: quedan null hasta
que exista una estimación compatible aprobada. Sirve para evaluar la hipótesis en replay; Decision
no la convierte en candidato operativo sin evidencia neta. El estado inicial del oracle STR-Sxx
habilita exclusivamente el evaluador aislado con fixtures; no modifica StrategyConfig global.
Instrumentos soportados expresan diseño; VenueCapabilities/ED y autorización siguen siendo gates.

## Predicción tipada

Prediction incluye model_id/version/state, universo, instrumento/revisión, snapshot/features,
issued_at, available_at, expires_at, horizonte, target, cost_basis, incertidumbre y evidencia.
issued_at es fin de inferencia, available_at>=issued_at, expires_at>available_at. Expirar no equivale
a retirar modelo; se comprueban ambos. Feature IDs/versiones deben coincidir con feature_schema_hash
registrado y dataset lineage del modelo. Calidad PARTIAL/STALE nunca pasa Decision para abrir.

- CLASSIFICATION/NET_POSITIVE: probability_net_positive sólo con calibration_state=VALID,
  método PLATT/ISOTONIC, artifact y vencimiento vigentes. q05/q50/q95/expected_net_return=null.
  Score crudo permanece raw_score, no se renombra a probabilidad. Sin calibración, probabilidad=null.
- REGRESSION/NET_RETURN o FUNDING_RETURN: expected_net_return decimal, probabilidad y cuantiles
  null. uncertainty es error absoluto estimado fuera de muestra, en fracción de retorno.
- RETURN_DISTRIBUTION: q05<=q50<=q95 y expected_net_return, misma unidad de retorno; probabilidad
  null. Calibración de intervalos puede ser CONFORMAL con evidencia, no PLATT como falso estimador.
  uncertainty=q95-q05 (ancho del intervalo central90%). No es intervalo de confianza de la media.

`baseline_improvement_lower` es el límite inferior de mejora emparejada del experimento aprobado,
no el retorno pronosticado; null impide cumplir el gate de mejora. Estado del modelo se consulta
autoritativamente: copiar PAPER_APPROVED en Prediction no concede aprobación. Una clasificación
positiva por sí sola nunca establece retorno esperado positivo después de costos.

## DecisionContext y orden de evaluación

DecisionPolicy fija horizonte, universo, hashes/versiones aprobadas, umbral de retorno inferior,
mejora mínima, spread máximo, pérdida estresada y ventana60s. Los valores son de preregistro;
no se deducen del nombre de estrategia. El caso de uso carga estado autoritativo y llama al
DecisionEvaluator puro. Decision guarda prediction_ids, input_hash, policy_hash y evidencia.
`cost_estimate_id` referencia la evidencia inmutable de CostEstimate.

1. Identidad/unidad/versiones, cobertura y available_at<=decision_at de todos los inputs requeridos.
   Fallo: DATA_INCOMPLETE, DATA_STALE o INSTRUMENT_MISMATCH. Bloqueo del sistema: SYSTEM_HALTED.
2. Elegibilidad, permiso/capacidad y estrategia aprobada. NO_SIGNAL/STRATEGY_DISABLED/TOKEN_RISK.
   Recent_decisions de la misma ventana e instrumento impiden duplicado: POSITION_PENDING.
3. Modelo autoritativo PAPER_APPROVED/CHAMPION, exacto universo/horizonte/target NET_RETURN,
   inferencia vigente, calibration aplicable válida y features completas. MODEL_NOT_APPROVED,
   MODEL_EXPIRED, UNCALIBRATED, FEATURE_MISMATCH. Modelos SHADOW sirven sólo investigación.
4. Usar q05 de RETURN_DISTRIBUTION con calibración de intervalo vigente, o el lower bound de
   retorno de un experimento heurístico aprobado referenciado por Signal.evidence_ids. Regresión
   puntual no proporciona lower bound por restarle arbitrariamente uncertainty. Requerir
   lower_net_return>policy.min_lower_return y baseline_improvement_lower>=mínimo preregistrado.
   Ausencia/fracaso: LOW_CONFIDENCE o COST_EXCEEDS_EDGE. Si estimador ya es NET_TRADE, no restar
   dos veces el costo. NET_ECONOMIC agrega costo de investigación sólo cuando el estimando lo fija.
5. Comparar sólo mismo horizonte/unidad/cost basis; mayor lower_return/stressed_loss_fraction
   (positivo), menor costo, strategy_id ascendente. Una entrada por instrumento por ventana.
6. Producir CANDIDATE o NO_TRADE sin mutar reservas. El caso de uso solicita Risk después;
   si cambia tamaño/costo recomputa con nueva quote hasta dos iteraciones, luego NO_TRADE.
   La aprobación de Risk nunca se infiere de CANDIDATE. RISK_DENIED es resultado posterior auditado.

Las salidas reduce_only de S19 se evalúan con ExitContext y hechos de ejecución frescos, sin exigir
un modelo alpha. HALTED puede impedir envío según policy; no implica que la posición esté cerrada.
Motivos se conservan en orden anterior, principal primero; múltiples causas son permitidas.

## Evidencia de diseño

Los 20 oracles STR-S01..STR-S20, fórmulas y fronteras se fijaron antes del producto. El validador
comprueba IDs, dependencias, fuentes/fields, ventanas, cobertura20/20 y vínculos de tareas; no
simula estrategias ni reclama que sus salidas reales ya coincidan. GD-17 agrega escenarios de
rechazo y temporalidad; GD-10 enlaza cada tarea con los oracles y pruebas de implementación.
