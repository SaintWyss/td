# C4 Context

```mermaid
flowchart TD
  U["Santiago / operador"] -->|"consulta y control"| TD["TD: laboratorio privado"]
  TD -->|"lectura autorizada"| DATA["APIs de mercado y Solana"]
  TD -->|"extracción acotada"| AI["APIs LLM"]
  TD -->|"evidencia y resultados"| U
  NEWS["Fuentes con permiso"] -->|"datos no confiables"| TD
  TD -.->|"futuro con aprobación"| CHAIN["Red / venue de ejecución"]
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
