# Flujo de datos

```mermaid
flowchart TD
  SRC["Proveedor"] --> G{"Permiso de acceso y almacenamiento"}
  G -->|"no"| B["Bloqueada sin persistir contenido"]
  G -->|"sí"| RAW["Raw con hash y recepción"]
  RAW --> P{"Permiso vigente"}
  P -->|"no"| T["Revocar; borrar o retener según política"]
  P -->|"sí"| V{"Schema válido"}
  V -->|"sí"| CAN["Canonical versionado"]
  V -->|"no"| Q["Cuarentena autorizada"]
  CAN --> PIT["Join por disponibilidad"]
  PIT --> DS["Dataset manifest"]
  PIT --> F["Snapshot online"]
  DS --> REP["Replay"]
  F --> DEC["Decisión"]
  REP --> EV["Evaluación"]
  DEC --> EV
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
