# Pipeline de investigación

```mermaid
flowchart TD
  C["Fuente candidata"] --> P{"Permiso por finalidad"}
  P -->|"no"| B["Bloqueada"]
  P -->|"sí"| D["Fetch y deduplicación"]
  D --> E["Extracción tipada"]
  E --> X{"Evidencia y contraste"}
  X -->|"insuficiente"| AB["Abstención / rumor"]
  X -->|"suficiente"| H["Hipótesis preregistrada"]
  H --> J["Experimento autorizado"]
  J --> K["Conocimiento con veredicto"]
```

Vista de diseño. Las relaciones financieras y estados normativos se detallan en los contratos y documentos de dominio. Ninguna flecha implica autorización live ni servicio ya desplegado.
