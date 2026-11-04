# Roadmap por versiones, épicas y gates

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Las versiones son incrementos de capacidad, no fechas ni promesas de rentabilidad. Un desarrollador individual trabaja por gates; estimaciones se revisan tras las primeras cinco tareas. Cada tarea tiene fase, épica y feature en `tasks/index.json`.

| Fase | Resultado | Gate de salida |
|---|---|---|
| V0 | Repositorio, contratos, CI, auth, dinero exacto, config y auditoría | G-FOUNDATION |
| V1 | RPC/enriquecimiento, raw, cursor, calidad, outbox y cuotas | G-DATA |
| V2 | Pools CPMM, tokens, extensiones, concentración, liquidez y anomalías básicas | G-SOLANA |
| V3 | Dataset PIT, folds, ledger, replay, costos, estadísticas y baselines | G-LAB técnico; estrategia puede ser rechazada |
| V4 | Modelos CPU, calibración, registry y challengers | G-MODEL |
| V5 | Estrategias, Decision, riesgo/reservas, modos y salidas | G-RISK |
| V6 | Paper prospectivo, reconciliación, panel mínimo y reporte | MVP-PAPER; G-PAPER financiero sólo cuando exista evidencia |
| V7 | Grants, extracción multi API, investigación y conocimiento | G-RESEARCH |
| V8 | Wallets, perfiles temporales y copy simulado | G-TRADER |
| V9 | Fusión, regímenes, anomalías avanzadas y familias adicionales | G-FUSION por familia |
| V10 | Outcomes, drift, challenger, promoción y rollback de modelo | G-LEARNING |
| V11 | Panel completo, backup/restore, presupuesto y seguridad operacional | G-OPS |
| V12 | Harness de ejecución, signer aislado, devnet, ensayo de fallos y expediente | G-READINESS; sigue sin autorización live |

Panel, autenticación, alertas y backups básicos empiezan en V0–V6. V11 completa y endurece; no se deja seguridad para el final. Las familias avanzadas se especifican desde ahora y se implementan sólo tras sus capacidades de venue/datos. V12 no obliga a implementarlas todas si han sido rechazadas científicamente; conserva el motivo.

## Dependencias y ejecución

Tareas se seleccionan topológicamente de `tasks/index.json`; sólo una tarea en progreso por agente. No hay implementación paralela implícita. Una tarea bloqueada por fuente no frena dinero exacto, fixture, UI o contratos independientes. En cada gate revisar costo real, cobertura y complejidad antes de ampliar.

Orden recomendado: completar V0; probar una vertical de ingesta→evidencia→lectura; luego Solana; luego replay y validación; sólo después ML. Paper comienza con regla sencilla y datos íntegros; no necesita todos los LLM ni wallets.

Estimación orientativa de esfuerzo total no se presenta como plazo contractual: la investigación, adquisición de datos y 90 días prospectivos no se comprimen aumentando agentes. La entrega software puede terminar con estrategias REJECTED y sin live. El informe final de cada fase enumera capacidades terminadas, evidencia, bloqueos externos y qué se decidió no construir por falta de valor.
