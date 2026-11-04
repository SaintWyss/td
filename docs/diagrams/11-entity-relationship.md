# Modelo entidad-relación

```mermaid
erDiagram
  SOURCE ||--o{ OBSERVATION : supplies
  ASSET ||--o{ OBSERVATION : describes
  OBSERVATION }o--o{ DATASET : included
  DATASET ||--o{ EXPERIMENT : evaluates
  EXPERIMENT ||--o{ MODEL : trains
  MODEL ||--o{ PREDICTION : emits
  PREDICTION }o--o{ DECISION : supports
  PORTFOLIO ||--o{ RESERVATION : owns
  DECISION ||--o| RESERVATION : requests
  RESERVATION ||--o| ORDER : authorizes
  ORDER ||--o{ ATTEMPT : attempts
  ATTEMPT ||--o{ FILL : yields
  FILL ||--|| JOURNAL : posts
  JOURNAL ||--|{ JOURNAL_LINE : contains
  ASSET ||--o{ JOURNAL_LINE : denominates
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
