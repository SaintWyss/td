# Backlog de implementación

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Cada tarea tiene ficha completa en `tasks/`, metadatos en `tasks/index.json` y prueba/criterio en la matriz. Seleccionar READY con dependencias DONE; la numeración no reemplaza el orden topológico. Las tareas de benchmark pueden quedar REJECTED científicamente aunque el adaptador sea correcto.

| Tarea | Fase / prioridad | Feature y objetivo | Dependencias |
|---|---|---|---|
| [T-001](tasks/T-001.md) | V0 / P0 | Bootstrap y comandos del repositorio | — |
| [T-002](tasks/T-002.md) | V0 / P0 | Cantidades y monedas exactas | T-001 |
| [T-003](tasks/T-003.md) | V0 / P0 | Settings y catálogo inicial de permisos | T-001, T-002 |
| [T-004](tasks/T-004.md) | V0 / P0 | Validación de contratos y cliente tipado | T-001 |
| [T-005](tasks/T-005.md) | V0 / P0 | Límites de importación | T-001 |
| [T-006](tasks/T-006.md) | V0 / P0 | Sesión local segura | T-003, T-004 |
| [T-007](tasks/T-007.md) | V0 / P0 | Roles CSRF e idempotencia HTTP | T-006 |
| [T-008](tasks/T-008.md) | V0 / P0 | Auditoría append-only | T-003 |
| [T-009](tasks/T-009.md) | V0 / P0 | Esquema SQL y migración fundacional | T-002, T-003, T-004 |
| [T-010](tasks/T-010.md) | V1 / P0 | Outbox receipts y leases | T-008, T-009 |
| [T-011](tasks/T-011.md) | V1 / P1 | Reservas de presupuesto API | T-009, T-010 |
| [T-012](tasks/T-012.md) | V1 / P1 | Limitador retries y breaker de proveedores | T-010, T-011 |
| [T-013](tasks/T-013.md) | V1 / P1 | Raw store y manifests atómicos | T-009 |
| [T-014](tasks/T-014.md) | V1 / P1 | Lecturas Solana RPC normalizadas | T-012, T-013 |
| [T-015](tasks/T-015.md) | V1 / P1 | Suscripción logs por programa | T-014 |
| [T-016](tasks/T-016.md) | V1 / P1 | Backfill y recuperación por cursor | T-014, T-015 |
| [T-017](tasks/T-017.md) | V1 / P1 | Enriquecimiento DEX Screener | T-012, T-013 |
| [T-018](tasks/T-018.md) | V1 / P1 | Cotizaciones Jupiter V2 | T-012, T-013 |
| [T-019](tasks/T-019.md) | V1 / P1 | Reglas de calidad y cuarentena | T-014, T-017 |
| [T-020](tasks/T-020.md) | V1 / P1 | Cobertura y universo temporal | T-016, T-019 |
| [T-021](tasks/T-021.md) | V2 / P1 | Decoder creación de pools CPMM | T-015, T-019, T-020 |
| [T-022](tasks/T-022.md) | V2 / P1 | Decoder swaps y reservas CPMM | T-021 |
| [T-023](tasks/T-023.md) | V2 / P1 | Mint y autoridades SPL | T-014, T-021 |
| [T-024](tasks/T-024.md) | V2 / P1 | Extensiones Token-2022 | T-023 |
| [T-025](tasks/T-025.md) | V2 / P1 | Concentración de holders | T-023 |
| [T-026](tasks/T-026.md) | V2 / P1 | Liquidez elegibilidad y ruta inversa | T-018, T-022, T-024, T-025 |
| [T-027](tasks/T-027.md) | V2 / P1 | Anomalías observables básicas | T-022, T-025 |
| [T-028](tasks/T-028.md) | V3 / P1 | Features temporales deterministas | T-020, T-022 |
| [T-029](tasks/T-029.md) | V3 / P1 | Dataset congelado y manifiesto | T-013, T-020, T-028 |
| [T-030](tasks/T-030.md) | V3 / P1 | Splits purging embargo y holdout | T-029 |
| [T-031](tasks/T-031.md) | V3 / P0 | Asientos balanceados por activo | T-002, T-009 |
| [T-032](tasks/T-032.md) | V3 / P0 | FIFO posiciones y NAV | T-031 |
| [T-033](tasks/T-033.md) | V3 / P1 | Replay con reloj inyectado | T-028, T-029, T-030, T-031 |
| [T-034](tasks/T-034.md) | V3 / P1 | Fill model CPMM y fee ledger | T-018, T-022, T-033 |
| [T-035](tasks/T-035.md) | V3 / P1 | Escenarios de costo latencia y liquidez | T-034 |
| [T-036](tasks/T-036.md) | V3 / P1 | Métricas intervalos y multiplicidad | T-030, T-032, T-035 |
| [T-037](tasks/T-037.md) | V3 / P1 | Preregistro y registro de ensayos | T-030, T-036 |
| [T-038](tasks/T-038.md) | V4 / P1 | Baseline logístico temporal | T-028, T-030, T-037 |
| [T-039](tasks/T-039.md) | V4 / P1 | LightGBM CPU acotado | T-038 |
| [T-040](tasks/T-040.md) | V4 / P1 | Calibración y predicción tipada | T-039 |
| [T-041](tasks/T-041.md) | V4 / P1 | Registro de modelos y lineage | T-038, T-040 |
| [T-042](tasks/T-042.md) | V4 / P1 | Challenger XGBoost | T-041 |
| [T-043](tasks/T-043.md) | V4 / P1 | Benchmark Kronos compacto | T-041 |
| [T-044](tasks/T-044.md) | V4 / P1 | Benchmark Chronos-Bolt tiny | T-041 |
| [T-045](tasks/T-045.md) | V4 / P1 | Admisión y benchmark TimesFM | T-041 |
| [T-046](tasks/T-046.md) | V7 / P2 | Admisión FinBERT | T-041 |
| [T-047](tasks/T-047.md) | V7 / P2 | Admisión FinGPT | T-041 |
| [T-048](tasks/T-048.md) | V9 / P2 | Benchmark L2 DeepLOB-like | T-041, T-100 |
| [T-049](tasks/T-049.md) | V5 / P1 | Decisión y NO_TRADE | T-026, T-040, T-041, T-028 |
| [T-050](tasks/T-050.md) | V5 / P0 | Sizing y límites deterministas | T-026, T-032, T-049 |
| [T-051](tasks/T-051.md) | V5 / P0 | Reservas concurrentes y fencing | T-009, T-050 |
| [T-052](tasks/T-052.md) | V5 / P0 | Modos kill switch y close-only | T-007, T-008, T-051 |
| [T-053](tasks/T-053.md) | V6 / P1 | Máquina de órdenes paper | T-051, T-052 |
| [T-054](tasks/T-054.md) | V6 / P1 | Paper fills y costos prospectivos | T-034, T-053, T-107, T-141 |
| [T-055](tasks/T-055.md) | V6 / P1 | Reconciliación paper y ledger | T-031, T-032, T-054 |
| [T-056](tasks/T-056.md) | V6 / P1 | Sesiones paper y recuperación | T-020, T-055, T-108, T-140 |
| [T-057](tasks/T-057.md) | V6 / P1 | Panel mínimo de control | T-007, T-052, T-056 |
| [T-058](tasks/T-058.md) | V7 / P2 | Grants revocación y derivados | T-003, T-009, T-041 |
| [T-059](tasks/T-059.md) | V7 / P2 | Fetcher con allowlist y SSRF | T-012, T-013, T-058 |
| [T-060](tasks/T-060.md) | V7 / P2 | Adapter OpenAI estructurado | T-011, T-012, T-041, T-058 |
| [T-061](tasks/T-061.md) | V7 / P2 | Adapter Anthropic y fallback | T-060 |
| [T-062](tasks/T-062.md) | V7 / P2 | Adapter Gemini y fallback | T-060 |
| [T-063](tasks/T-063.md) | V7 / P2 | Extracción entidades y sentimiento | T-059, T-060 |
| [T-064](tasks/T-064.md) | V7 / P2 | Deduplicación y orígenes | T-063 |
| [T-065](tasks/T-065.md) | V7 / P2 | Hipótesis y jobs limitados | T-037, T-064 |
| [T-066](tasks/T-066.md) | V7 / P2 | Conocimiento versionado | T-064, T-065 |
| [T-067](tasks/T-067.md) | V8 / P2 | Historial de wallets y tipos de flujos | T-014, T-016, T-022 |
| [T-068](tasks/T-068.md) | V8 / P2 | Inventario PnL observable y cobertura | T-031, T-032, T-067 |
| [T-069](tasks/T-069.md) | V8 / P2 | Cohortes y selección ex ante | T-030, T-036, T-068 |
| [T-070](tasks/T-070.md) | V9 / P2 | Fusión temporal OOF | T-040, T-063, T-069 |
| [T-071](tasks/T-071.md) | V9 / P2 | Features de régimen | T-028, T-030 |
| [T-072](tasks/T-072.md) | V10 / P2 | Outcomes maduros y censura | T-040, T-055 |
| [T-073](tasks/T-073.md) | V10 / P2 | Drift y retirada segura | T-072 |
| [T-074](tasks/T-074.md) | V10 / P2 | Promoción CAS con evidencia | T-007, T-008, T-036, T-041, T-072 |
| [T-075](tasks/T-075.md) | V10 / P2 | Rollback de artefacto | T-074 |
| [T-076](tasks/T-076.md) | V10 / P2 | Sandbox RL condicionado | T-035, T-041, T-072 |
| [T-077](tasks/T-077.md) | V11 / P2 | Vista estado conectores y alertas | T-057, T-089 |
| [T-078](tasks/T-078.md) | V11 / P2 | Vista tokens y evidencia | T-026, T-057 |
| [T-079](tasks/T-079.md) | V11 / P2 | Vista traders y cobertura | T-057, T-069 |
| [T-080](tasks/T-080.md) | V11 / P2 | Vista investigación e hipótesis | T-057, T-066 |
| [T-081](tasks/T-081.md) | V11 / P2 | Vista estrategias decisiones y paper | T-055, T-057 |
| [T-082](tasks/T-082.md) | V11 / P2 | Vista experimentos y holdout | T-037, T-057 |
| [T-083](tasks/T-083.md) | V11 / P2 | Vista modelos y promociones | T-057, T-074 |
| [T-084](tasks/T-084.md) | V11 / P2 | Vista costos y límites | T-011, T-057 |
| [T-085](tasks/T-085.md) | V11 / P2 | Auditoría exportación y configuración | T-008, T-057 |
| [T-086](tasks/T-086.md) | V11 / P2 | Compose perfiles y aislamiento | T-003, T-007, T-052 |
| [T-087](tasks/T-087.md) | V11 / P2 | Backup cifrado consistente | T-013, T-031, T-086 |
| [T-088](tasks/T-088.md) | V11 / P2 | Restore aislado y conciliación | T-055, T-087 |
| [T-089](tasks/T-089.md) | V11 / P2 | Métricas logs y correlación | T-008, T-010, T-012 |
| [T-090](tasks/T-090.md) | V11 / P2 | Runbooks e incidentes probados | T-052, T-088, T-089 |
| [T-091](tasks/T-091.md) | V11 / P2 | SBOM dependencia y secret gates | T-001, T-086 |
| [T-092](tasks/T-092.md) | V11 / P2 | Release y rollback compatible | T-075, T-088, T-091 |
| [T-093](tasks/T-093.md) | V12 / P2 | Política del signer aislado | T-051, T-052, T-086 |
| [T-094](tasks/T-094.md) | V12 / P2 | Decoder de transacción y lookup tables | T-024, T-093 |
| [T-095](tasks/T-095.md) | V12 / P2 | Build Jupiter restringido | T-018, T-094 |
| [T-096](tasks/T-096.md) | V12 / P2 | Simulación preflight y validez | T-095 |
| [T-097](tasks/T-097.md) | V12 / P2 | Envío durable y UNKNOWN | T-053, T-093, T-096 |
| [T-098](tasks/T-098.md) | V12 / P2 | Confirmación finality y reorg | T-055, T-097 |
| [T-099](tasks/T-099.md) | V12 / P2 | Fencing y kill switch en firma | T-052, T-098 |
| [T-100](tasks/T-100.md) | V9 / P2 | L2 Kraken y certificación de CLOB | T-012, T-013, T-019 |
| [T-101](tasks/T-101.md) | V9 / P2 | Órdenes CEX y cancel races en sandbox | T-053, T-100 |
| [T-102](tasks/T-102.md) | V9 / P0 | Margen y riesgo de piernas derivados sandbox | T-050, T-101 |
| [T-103](tasks/T-103.md) | V9 / P2 | Arbitraje multi-leg atómico sandbox | T-034, T-051, T-101 |
| [T-104](tasks/T-104.md) | V12 / P2 | Expediente de preparación operativa | T-036, T-074, T-090, T-092, T-099 |
| [T-105](tasks/T-105.md) | V2 / P1 | S01 — evaluador puro: Descubrimiento temprano | T-021, T-026 |
| [T-106](tasks/T-106.md) | V3 / P1 | S01 — experimento y falsación | T-105, T-035, T-036, T-037 |
| [T-107](tasks/T-107.md) | V5 / P1 | S02 — evaluador puro: Momentum | T-028, T-049, T-050 |
| [T-108](tasks/T-108.md) | V5 / P1 | S02 — experimento y falsación | T-107, T-035, T-036, T-037 |
| [T-109](tasks/T-109.md) | V9 / P2 | S03 — evaluador puro: Scalping | T-034, T-100, T-101 |
| [T-110](tasks/T-110.md) | V9 / P2 | S03 — experimento y falsación | T-109, T-035, T-036, T-037 |
| [T-111](tasks/T-111.md) | V9 / P2 | S04 — evaluador puro: Mean reversion | T-028, T-071 |
| [T-112](tasks/T-112.md) | V9 / P2 | S04 — experimento y falsación | T-111, T-035, T-036, T-037 |
| [T-113](tasks/T-113.md) | V9 / P2 | S05 — evaluador puro: Breakout | T-028, T-050 |
| [T-114](tasks/T-114.md) | V9 / P2 | S05 — experimento y falsación | T-113, T-035, T-036, T-037 |
| [T-115](tasks/T-115.md) | V9 / P2 | S06 — evaluador puro: False breakout | T-028, T-050 |
| [T-116](tasks/T-116.md) | V9 / P2 | S06 — experimento y falsación | T-115, T-035, T-036, T-037 |
| [T-117](tasks/T-117.md) | V9 / P2 | S07 — evaluador puro: Order-flow imbalance | T-100, T-101 |
| [T-118](tasks/T-118.md) | V9 / P2 | S07 — experimento y falsación | T-117, T-035, T-036, T-037 |
| [T-119](tasks/T-119.md) | V9 / P2 | S08 — evaluador puro: Noticias | T-063, T-064, T-065 |
| [T-120](tasks/T-120.md) | V9 / P2 | S08 — experimento y falsación | T-119, T-035, T-036, T-037 |
| [T-121](tasks/T-121.md) | V9 / P2 | S09 — evaluador puro: Sentimiento | T-063, T-064, T-070 |
| [T-122](tasks/T-122.md) | V9 / P2 | S09 — experimento y falsación | T-121, T-035, T-036, T-037 |
| [T-123](tasks/T-123.md) | V8 / P2 | S10 — evaluador puro: Copy trading filtrado | T-069, T-055 |
| [T-124](tasks/T-124.md) | V8 / P2 | S10 — experimento y falsación | T-123, T-035, T-036, T-037 |
| [T-125](tasks/T-125.md) | V8 / P2 | S11 — evaluador puro: Smart-money agregado | T-069, T-036 |
| [T-126](tasks/T-126.md) | V8 / P2 | S11 — experimento y falsación | T-125, T-035, T-036, T-037 |
| [T-127](tasks/T-127.md) | V9 / P2 | S12 — evaluador puro: Liquidez | T-026, T-034 |
| [T-128](tasks/T-128.md) | V9 / P2 | S12 — experimento y falsación | T-127, T-035, T-036, T-037 |
| [T-129](tasks/T-129.md) | V9 / P2 | S13 — evaluador puro: Grid | T-101, T-071 |
| [T-130](tasks/T-130.md) | V9 / P2 | S13 — experimento y falsación | T-129, T-035, T-036, T-037 |
| [T-131](tasks/T-131.md) | V9 / P2 | S14 — evaluador puro: Market making | T-101, T-100 |
| [T-132](tasks/T-132.md) | V9 / P2 | S14 — experimento y falsación | T-131, T-035, T-036, T-037 |
| [T-133](tasks/T-133.md) | V9 / P2 | S15 — evaluador puro: Arbitraje | T-103 |
| [T-134](tasks/T-134.md) | V9 / P2 | S15 — experimento y falsación | T-133, T-035, T-036, T-037 |
| [T-135](tasks/T-135.md) | V9 / P2 | S16 — evaluador puro: Funding-rate arbitrage | T-102 |
| [T-136](tasks/T-136.md) | V9 / P2 | S16 — experimento y falsación | T-135, T-035, T-036, T-037 |
| [T-137](tasks/T-137.md) | V9 / P2 | S17 — evaluador puro: Delta-neutral | T-102 |
| [T-138](tasks/T-138.md) | V9 / P2 | S17 — experimento y falsación | T-137, T-035, T-036, T-037 |
| [T-139](tasks/T-139.md) | V3 / P1 | S18 — evaluador puro: Seguimiento de tendencias | T-028, T-033 |
| [T-140](tasks/T-140.md) | V3 / P1 | S18 — experimento y falsación | T-139, T-035, T-036, T-037 |
| [T-141](tasks/T-141.md) | V5 / P1 | S19 — evaluador puro: Gestión dinámica de salida | T-051, T-049, T-032 |
| [T-142](tasks/T-142.md) | V5 / P1 | S19 — experimento y falsación | T-141, T-035, T-036, T-037 |
| [T-143](tasks/T-143.md) | V9 / P2 | S20 — evaluador puro: Selección por regímenes | T-070, T-071 |
| [T-144](tasks/T-144.md) | V9 / P2 | S20 — experimento y falsación | T-143, T-035, T-036, T-037 |
