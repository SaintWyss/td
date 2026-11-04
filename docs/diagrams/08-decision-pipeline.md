# Pipeline de decisión

```mermaid
flowchart TD
  I["Señales y contexto"] --> V{"Calidad y vigencia"}
  V -->|"falla"| NO["NO_TRADE con motivos"]
  V -->|"pasa"| E{"Edge neto conservador"}
  E -->|"no"| NO
  E -->|"sí"| R{"Riesgo y reserva"}
  R -->|"deniega"| NO
  R -->|"aprueba"| INT["Intent vinculado"]
  INT --> A["Auditoría durable"]
  NO --> A
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
