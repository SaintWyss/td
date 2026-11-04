# Flujo de datos

```mermaid
flowchart TD
  SRC["Proveedor"] --> RAW["Raw con hash y recepción"]
  RAW --> V{"Schema y permisos"}
  V -->|"válido"| CAN["Canonical versionado"]
  V -->|"inválido"| Q["Cuarentena"]
  CAN --> PIT["Join por disponibilidad"]
  PIT --> DS["Dataset manifest"]
  PIT --> F["Snapshot online"]
  DS --> REP["Replay"]
  F --> DEC["Decisión"]
  REP --> EV["Evaluación"]
  DEC --> EV
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
