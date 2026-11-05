# Pipeline de ejecución futura

```mermaid
sequenceDiagram
  participant C as Coordinator
  participant R as Risk DB
  participant S as Signer
  participant N as Solana RPC
  C->>R: Reserve and bind intent
  R-->>C: Reservation and epoch
  C->>N: Build-state simulation
  N-->>C: Simulation evidence
  C->>R: Persist PREPARED and reserve ATTEMPTED
  C->>S: Validated signing request
  S->>R: Verify active epoch and permit
  S-->>C: Signed bytes and signature
  C->>R: Persist SIGNED and exact bytes before send
  C->>N: Send same signed bytes
  alt Confirmation known
    N-->>C: Status and finality
    C->>R: Atomic journal, reserve, projection and RECONCILED
  else Timeout or conflict
    C->>R: UNKNOWN and retain reserve
    C->>N: Query signature and balances
  end
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
