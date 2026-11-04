# Arquitectura general

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Unidad de implementación

Repositorio único con `backend/src/td/{domain,application,ports,adapters,entrypoints}`, `web/`, `tests/`, `infra/`, `config/` y este `docs/`. Los módulos del dominio agrupan ingesta normalizada, inteligencia, investigación, experimentos, estrategias, riesgo, ejecución y contabilidad. Las entidades no importan FastAPI, ORM, SDKs ni modelos LLM.

Los casos de uso coordinan puertos; adaptadores traducen RPC/HTTP, SQL y archivos. El composition root resuelve dependencias explícitas. Una estrategia implementa `evaluate(FeatureSnapshot, PortfolioView, StrategyConfig) -> Signal | Abstention`. Riesgo consume valores tipados y devuelve `RiskAssessment`; sólo una reserva persistida habilita un `ExecutionIntent`. GRASP: Portfolio conoce exposición, TokenAssessment conoce elegibilidad, ExecutionCoordinator conoce transiciones, Ledger conoce efectos contables. No se distribuyen invariantes en controladores.

## Procesos y fronteras

`api`: autenticación, lecturas y comandos humanos. `collector`: conectores, normalización y watermarks. `worker`: jobs de features, evaluación, paper y conciliación. `trainer`: proceso por lotes con recursos acotados. `researcher`: acceso LLM y egress de fuentes permitidas; no posee credenciales financieras. PostgreSQL es estado transaccional; archivos Parquet son históricos inmutables referenciados por manifiestos. No se añade un servidor de objetos local hasta necesitarlo.

La ejecución real futura usa `executor` y `signer` separados, identidades y permisos propios. El monolito modular es una unidad de código, no una razón para compartir claves. El signer no se distribuye ni se inicia en perfiles `dev`, `research` o `paper`.

## Consistencia

El productor escribe entidad y outbox en una transacción. El consumidor inserta su recibo de deduplicación y efecto en otra. Entrega al menos una vez; no se promete exactly-once de red. Los efectos económicos son idempotentes por índices únicos. Reintentar una lectura es distinto de volver a firmar una transacción.

Reserva de riesgo y contador de cartera se actualizan bajo bloqueo de la fila de cartera y versión optimista. Operaciones externas ocurren fuera de la transacción SQL; su intento durable se registra antes. Cualquier resultado incierto se reconcilia antes de liberar reservas o emitir reemplazos.

## Decisiones comparadas

FastAPI/Pydantic simplifican validación y OpenAPI; PostgreSQL evita coordinar tres sistemas al inicio; Parquet separa scans analíticos del OLTP. Redis queda descartado como autoridad de saldo y no se necesita para el MVP. FreqAI/LEAN son referencias y controles externos posibles; no son el núcleo porque el universo de mints, slots, programas y swaps exige contratos explícitos propios. Condor valida la idea de separar razonamiento de ejecución, pero no sustituye las pruebas de riesgo de TD.

Los ADR contienen razones, alternativas rechazadas y consecuencias. Los doce diagramas están en `diagrams/`; muestran fronteras lógicas y despliegue propuesto, no servicios existentes.
