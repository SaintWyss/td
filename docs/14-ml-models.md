# Modelos predictivos y selección tecnológica

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Primera comparación cerrada

Target: distribución del retorno liquidable neto a 5 minutos de tokens elegibles de S02, con etiquetas censuradas cuando no se observa salida; nunca borrar esas filas como si fueran éxitos. Usar retornos de reserva/quote y costos de ida y vuelta; no el máximo de vela. Features: retornos 1/5/15 min, log-volumen, aceleración, volatilidad, participantes únicos observables, concentración, cambio de reservas, coste cotizado y edad del pool. La disponibilidad de cada feature determina el instante utilizable.

Baseline 0: efectivo; baseline 1: regla S02; baseline 2: regresión logística regularizada. Primer challenger: LightGBM CPU, probabilidades calibradas y regresión cuantílica. Entrenar máximo 4 h/4 GiB/8 hilos, early stopping en validación interna. Semillas y límites se congelan. Una calibración isotónica requiere muestra suficiente; por defecto Platt con split temporal separado. No calibrar sobre test/holdout.

| Tecnología | Decisión concreta | Motivo y experimento |
|---|---|---|
| LightGBM [S22] | Principal tabular CPU | Control de complejidad, datos mixtos; comparar 12 configuraciones predefinidas |
| XGBoost [S23] | Challenger | Mismo target/folds/budget; sólo promover si mejora material robusta |
| AR/naive/EWMA | Baselines | Detectar mejoras ilusorias frente a persistencia/volatilidad simple |
| Kronos-mini/small [S24] | Benchmark posterior, congelado | K-lines; no implica ejecución rentable; evaluar contaminación del pretraining y costo local |
| Chronos-Bolt-tiny [S25] | Benchmark compacto | Cuantiles de series; adaptar target sin usar covariables futuras |
| TimesFM [S26] | 2.5 sujeto a revisión de checkpoint; 3.0 bloqueado para producción | La licencia del código no habilita los pesos 3.0 para uso comercial/productivo |
| FinBERT [S27] | Candidato de NLP, bloqueado hasta revisar pesos/dataset | Sentimiento financiero no equivale a lenguaje de memecoins; aviso de licencia distingue artefactos |
| FinGPT [S28] | Investigación posterior | No entrenar LLM generalista; verificar modelo base, LoRA, corpus y derechos antes de prueba |
| DeepLOB-like [S29] | Sólo mercado con L2 real | Paper original sobre libros, no reservas AMM; exigir snapshots/deltas íntegros |
| Isolation Forest + reglas robustas | Anomalías V2/V9 | Entrenar sólo train; reportar rareza, no fraude ni probabilidad sin calibración |
| Ensemble logístico | V9 | Meta-features out-of-fold temporales; evita leakage del stacking |
| FinRL/RL [S30] | Experimento V10 condicionado | Simulador primero validado, benchmark fijo; recompensa neta con penalidad de riesgo, sin promoción automática |

No se predetermina ganador. Artefactos registran versión exacta de librería, hash de pesos/tokenizer, licencia de código/pesos/datos por separado, corte de preentrenamiento conocido o desconocido, commit, seed, entorno y resultados. Un modelo preentrenado con fecha de corte incierta puede participar en diagnóstico; no prueba independencia de un backtest histórico. El paper prospectivo comienza después de congelar el artefacto.

GPU opcional: perfil inicial máximo 6 GiB de VRAM verificada, batch reducido; OOM aborta job y limpia contexto, no reinicia ingesta. No entrenar durante operaciones que dependan del mismo host si la contención viola SLO. Optuna puede añadirse con número de ensayos registrado; cada nuevo trial cuenta para selección múltiple.
