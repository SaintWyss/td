# Investigación autónoma y conocimiento

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Pipeline: propuesta de fuente → revisión de permiso → fetch acotado → deduplicación → extracción → contraste → hipótesis → preregistro → experimento → revisión → conocimiento versionado. El investigador puede descubrir candidatos, pero no autoaprobar una licencia, comprar un feed ni ejecutar código arbitrario.

## Registros

`SourceGrant` incluye titular, URL base permitida, rutas/métodos, evidencia contractual, finalidades independientes (`display`, `inference`, `training`, `redistribution`), retención, jurisdicción, revisión y expiración. Para nuevas fuentes, permiso desconocido equivale a bloqueado. La aprobación de una finalidad no habilita las demás. Revocar frena jobs, purga texto/caché según obligación y marca datasets/modelos derivados para revisión.

`ResearchClaim` contiene texto de afirmación, tipo observado/inferido/rumor, evidencias, disponibilidad, entidades y confianza del extractor separada de confianza factual. Dos sitios sindicando una misma noticia cuentan como un origen. Canonical URL, hash de contenido y similitud lexical agrupan duplicados; el grafo conserva relaciones de copia. Una noticia corregida agrega revisión.

`Hypothesis` especifica mecanismo económico, universo, target, horizonte, features, placebo, costos, criterio de rechazo, familia de pruebas y presupuesto. Ejemplo: aceleración de compradores únicos agrega expectativa neta sobre momentum puro. No se acepta «el token se ve fuerte» ni elegir umbrales mirando el holdout.

## Autonomía limitada

El scheduler revisa fuentes cada intervalo contratado, asigna un máximo de 20 documentos y 5 hipótesis diarias, y no más de 2 experimentos nuevos/día. Experimentos se ejecutan sólo sobre plantillas y librerías admitidas, sin `eval`, shell ni descarga de paquetes sugeridos por el texto. Workflows tienen 6 pasos máximos y deadline de 10 min; el agotamiento produce PARTIAL con evidencia utilizable.

Conocimiento en PostgreSQL: claims, entidades, relaciones y evidencias; búsqueda textual inicial, sin grafo externo o base vectorial obligatoria. Embeddings se incorporan sólo si mejora recuperación medida y el permiso permite enviarlos al proveedor. Una conclusión rechazada queda en registro para evitar repetir búsquedas; no se borra para mejorar apariencia.

## Defensa y validación

Fetcher bloquea localhost, RFC1918, link-local y metadata cloud; resuelve y verifica DNS en cada redirección; sólo HTTPS/443 y dominios permitidos. Descargas ≤2 MiB, sin archivos ejecutables, OCR o parsing en proceso aislado cuando se incorpore multimodalidad. Instrucciones incrustadas no cambian rol, herramienta o política. Suite adversarial incluye órdenes de revelar claves, activar live, ignorar límites, URLs internas y fuentes falsas.

Se mide precisión de entidades, evidencia válida, duplicados, contradicciones y costo por hipótesis evaluable. El desempeño de extracción no demuestra alpha; las features sociales pasan las mismas ablaciones y pruebas netas que mercado-only.
