# Modelo de dominio e invariantes

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

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

## Aritmética normativa del draft 1.1 (ADR-017)

`Money.atoms` es entero decimal no negativo de hasta 78 dígitos; cero es conocido,
null es desconocido sólo donde el schema lo permite. `asset_id` resuelve un registro
inmutable de cadena+dirección canónica; validar su coincidencia con `decimals`.
Un ticker jamás es clave financiera. SPL supply y balances se comprueban además contra
u64 en el adaptador; 78 dígitos es capacidad interna, no autorización de rango on-chain.

Asset/MintSnapshot conservan decimals u8 (0–255) observados. El motor Money soporta
0–38: un mint superior se observa pero se marca UNSUPPORTED_PRECISION y no se negocia.
No reducir decimals ni truncar supply para hacerlo elegible. MintSnapshot sólo representa
una decodificación completa: authority=null significa ausencia comprobada de autoridad;
lectura ausente/incompleta produce Observation UNKNOWN, nunca un MintSnapshot inventado.
PoolSnapshot permite reservas null; null o reserva cero impide elegibilidad, con motivos distintos.

Los decimales derivados usan máximo 20 dígitos enteros y 18 fraccionarios, compatibles
con NUMERIC(38,18). Sin exponentes, NaN, infinity, separadores, ceros iniciales o -0.
Exactitud de atoms no depende de NUMERIC(38,18): almacenamiento NUMERIC(78,0).
Python: enteros arbitrarios para productos/división euclídea; no usar Decimal con contexto
por defecto de 28 dígitos. Conversión humana = atoms / 10**decimals exacta; si no cabe en
el tipo derivado, error NUMERIC_OVERFLOW, sin saturar. La presentación puede mostrar más
decimales mediante string exacto sin persistirlo como decimal derivado.

Redondeo por finalidad: gasto/tamaño de entrada hacia abajo; fees y exposición reservada
hacia arriba; precio límite de compra hacia abajo y de venta hacia arriba al tick del venue;
PnL firmado con ROUND_HALF_EVEN a escala declarada sólo al presentar/agregar, conservar
asientos atómicos originales. Underflow de una cantidad positiva a cero devuelve
BELOW_MIN_UNIT y abstención. Nunca convertir float a Decimal para recuperar precisión perdida.

Enteros JSON no monetarios están acotados a 2**53-1 para transporte TypeScript seguro.
Un slot/contador externo mayor se rechaza como UNSUPPORTED_RANGE conservando raw;
no se redondea. Extenderlos a string exige nueva versión. Porcentajes de holders usados
por Risk son strings decimales [0,1], leídos exactamente desde el texto. Probabilidades
ML y métricas no monetarias pueden ser float finito; no son balances ni caps financieros.

## Contratos financieros R2

[Operaciones, instrumentos y unidades](contracts/financial-operations.md) y ADR-019 especifican
LedgerPostRequest, LedgerPostResult, ReconciliationRequest y catálogo Instrument. Son normativos
para depósitos/rent/fees/reservas/reversos y liquidación; LedgerWriter ya no recibe Fill aislado.
Los metadatos de Instrument y los escenarios son requisitos de implementación, no servicios activos.
