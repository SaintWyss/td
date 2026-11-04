# Pipeline ML

```mermaid
flowchart TD
  DS["Dataset congelado"] --> SPL["Folds / purging"]
  SPL --> TR["Train y calibración interna"]
  TR --> REG["Artefacto challenger"]
  REG --> VAL["Test / holdout único"]
  VAL --> G{"Gates científicos"}
  G -->|"falla"| REJ["Rechazado o inconcluso"]
  G -->|"pasa"| PAPER["Shadow / paper prospectivo"]
  PAPER --> HUMAN{"Revisión humana"}
  HUMAN -->|"aprueba"| CH["Champion paper"]
  HUMAN -->|"rechaza"| REJ
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
