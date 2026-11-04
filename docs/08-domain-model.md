# Modelo de dominio e invariantes

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Identidad y agregados

`Asset` usa `chain_id + mint/address`; `Instrument` añade venue y quote. SOL nativo y wSOL conservan identidades distintas y una relación de envoltura; no se unen por ticker. `Pool` conserva programa, versión de decoder, mints, vaults y estado observado. `SourceGrant` representa permisos por finalidad y expiración. `Observation` y `FeatureSnapshot` conservan evidencia, calidad, tiempos y versiones.

`Experiment` congela dataset, hipótesis, configuraciones y pruebas ensayadas. `ModelArtifact` contiene pesos, hash, entorno, lineage y licencia. `Signal` es una propuesta estadística; `Decision` incluye abstención o candidato; `RiskAssessment` no es una firma. `Reservation` inmoviliza presupuesto y versión de política. `Order` representa intención económica; `Attempt` representa una transacción firmada concreta. `Fill` y `JournalEntry` son hechos; `Position` y `PortfolioView` son proyecciones reconstruibles.

## Invariantes normativas

- INV-01: dinero y cantidades se transportan como strings decimales/enteros. No `float` para saldos, fees ni comparación de límites.
- INV-02: toda feature cumple `available_at <= decision_at`; faltantes no se rellenan con información posterior.
- INV-03: cada evento tiene dedup key, evidencia y versión de esquema; revisiones no sobrescriben hechos.
- INV-04: ninguna entrada sin elegibilidad, calidad, vigencia y reserva atómica.
- INV-05: exposición incluye posiciones, reservas y escenarios máximos de intentos inciertos.
- INV-06: sólo signer autorizado puede firmar; LLM, UI e investigador carecen de ese puerto y credencial.
- INV-07: `send accepted` no equivale a fill. Saldo se deriva de hechos confirmados y conciliados.
- INV-08: timeout con envío posible conserva reserva y entra en reconciliación; nunca recompone ciegamente.
- INV-09: un fill genera un único journal balanceado; duplicarlo no altera saldos.
- INV-10: política de seguridad sólo cambia con versión, actor y auditoría; no por output de IA.
- INV-11: `NO_TRADE` es resultado normal con códigos; desconocido no significa aprobado.
- INV-12: fuente sin permiso para la finalidad concreta no ingresa a extracción, entrenamiento ni distribución.
- INV-13: holdout consumido queda marcado; no vuelve a llamarse no visto.
- INV-14: promoción requiere reporte congelado; un entrenamiento no cambia champion.
- INV-15: `HALTED` bloquea firmas nuevas; operaciones ya emitidas pueden finalizar y deben conciliarse.
- INV-16: restore/rollback jamás revierte la blockchain; proyecta hechos externos antes de reanudar.
- INV-17: retirar liquidez no garantiza que el stop tenga mercado; se conserva pérdida y posición no liquidable.
- INV-18: sin secretos de ejecución y sin aprobación live vigente, la configuración efectiva es paper o investigación.

## Reglas semánticas

La API valida sintaxis; la aplicación valida relaciones y autorización. Por ejemplo, `filled_atoms <= requested_atoms`, `q05 <= q50 <= q95`, origen de evidencia, balance de journal por activo, expiración y finalidad de grants necesitan validadores semánticos además de JSON Schema. Los tests negativos están catalogados en `contracts/semantic-rules.json`. El versionado de una entidad no permite reemplazar el historial: cada transición incrementa `revision` y produce evento.
