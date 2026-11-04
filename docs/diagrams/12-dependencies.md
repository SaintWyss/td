# Dependencias de código

```mermaid
flowchart TD
  ENTRY["Entrypoints / API"] --> APP["Application cases"]
  ADAPT["Adapters: SQL / HTTP / ML"] --> PORT["Ports"]
  APP --> PORT
  APP --> DOMAIN["Domain"]
  PORT --> DOMAIN
  ROOT["Composition root"] --> ENTRY
  ROOT --> ADAPT
  WEB["Web TypeScript"] --> CLIENT["Generated API client"]
  CLIENT --> ENTRY
  TEST["Tests / fixtures"] --> APP
  TEST --> ADAPT
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
