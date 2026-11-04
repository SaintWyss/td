# C4 Container

```mermaid
flowchart TD
  WEB["Web privada"] --> API["API / sesiones"]
  API --> DB["PostgreSQL / outbox"]
  COL["Collector"] --> DB
  COL --> RAW["Raw / Parquet"]
  WORK["Worker / paper"] --> DB
  WORK --> RAW
  TRAIN["Trainer por lotes"] --> RAW
  TRAIN --> DB
  RES["Researcher sin claves financieras"] --> DB
  API --> OPS["Observabilidad"]
  WORK --> OPS
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
