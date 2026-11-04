# C4 Component: decisión y ejecución

```mermaid
flowchart TD
  F["FeatureSnapshot"] --> ST["Strategy evaluator"]
  ST --> DEC["Decision / abstención"]
  DEC --> R["Risk / reserva atómica"]
  R --> EX["Execution coordinator"]
  EX --> P["Paper adapter"]
  EX -.-> LIVE["Signer futuro aislado"]
  P --> REC["Reconciler"]
  LIVE -.-> REC
  REC --> LED["Ledger"]
  LED --> PV["Portfolio projection"]
  PV --> R
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
