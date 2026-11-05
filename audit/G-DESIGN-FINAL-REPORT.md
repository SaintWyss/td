# G-DESIGN — informe final de auditoría TD

Fecha de cierre documental: 2026-11-04 (Argentina). **Dictamen: NOT_READY.**
Este es el cierre de la revisión y sus correcciones verificadas; no una aprobación del gate.

## Identificación y alcance

- Repositorio privado: https://github.com/SaintWyss/td.
- SHA base de main: `155f8064417f4d62541d247abe56024cb6b9e165`.
- Árbol base: `40afc8a3754e3fcc583d82f8a1409960cf806ef4`.
- Rama: `audit/g-design-blueprint-finalization`; main se conserva sin merge.
- SHA final del contenido auditado: se registra en `g-design/delivery.json` al publicar el commit
  de correcciones. El commit posterior sólo consolida evidencia y este informe. El SHA del propio
  informe se obtiene con `git log -1 --format=%H -- audit/G-DESIGN-FINAL-REPORT.md`; no se inventa
  un hash autorreferencial. El PR identifica inequívocamente el tip de entrega.

El inventario base contiene **315 archivos** con hashes y tamaños. Se revisaron los **40 documentos
principales, 16 ADR originales, 20 estrategias y 144 fichas** (220 documentos), además de los
**2 ADR nuevos**: 222 registros en `g-design/reviewed-files.json`. Los **12 Mermaid** se revisan
separadamente con fuentes, renders y hashes. Se revisaron los **102 $defs originales** y las
**4 solicitudes nuevas**: 106 registros en `g-design/contract-review.json`.

Las cifras miden cobertura de revisión, no corrección completa. Las 20 estrategias siguen
necesitando los inputs y features señalados en GD-11. No se afirma que cada línea de los 315
archivos haya sido probada semánticamente. Se conservaron consigna e investigación originales
(`docs/evidence/input-brief.txt`, `input-research.md`) y se contrastó su cobertura en
`docs/evidence/research-review.md`. No se reconstruyeron antecedentes ausentes.

## Metodología y estado inicial

Se comprobaron main, historial, ramas, PR y CI antes de editar. La rama propia estaba en la base;
no había otros PR ni cambios remotos de implementación. T-001 tenía CI aprobada. Se conservaron
su evidencia y `audit/validation.json`; la ejecución de baseline también pasó `make check`
(`g-design/logs/baseline-check.*`). Ese PASS era estructural y no acreditaba seguridad financiera.

La revisión combina lectura por documento/ficha/definición, contraste entre productores y
consumidores, trazabilidad, análisis de estados y fallos, consultas de fuentes primarias,
mutaciones adversariales del validador y revisión visual. El catálogo de fuentes tiene 41
entradas (40 originales y la referencia de generación TypeScript); describe consulta,
limitaciones y licencias por finalidad. No se hicieron llamadas autenticadas a proveedores.

## Correcciones incorporadas

1. Rangos exactos para NUMERIC(38,18), shares como decimal string, enteros seguros para JSON/TS,
   signo/cero, unidad explícita de riesgo y distinción entre decimals observables u8 y soportados.
2. Reserva e intención enlazadas por todos sus efectos autorizados; hash no sustituye decodificación.
   Risk debe releer estado autoritativo bajo lock; aprobación/denegación tienen condiciones distintas.
3. Firma devuelve bytes; PREPARED no inventa una firma; reserva ATTEMPTED antes de pedirla.
   Persistencia antes de envío, retry del mismo payload, UNKNOWN conserva fondos y reconciliación
   confirma journal/reserva/proyección/outbox/RECONCILED en una transacción local.
4. Máquinas explícitas de attempt, reservation, control y job, además de órdenes Solana y CEX.
   Guards y alcanzabilidad comprobados; ausencia de RPC no prueba fracaso ni expiración segura.
5. Grants con almacenamiento, método/prefijo y procesador; permiso antes de persistir contenido,
   revalidación por etapa y tratamiento explícito de revocación.
6. Probabilidad calibrada separada de regresores de cuantiles/media; bloque temporal de calibración
   separado de selección y test. No se alteraron umbrales para producir alpha artificial.
7. Negativos con omisión única y motivo esperado; 24 vectores de frontera; 6 pruebas adversariales
   adicionales (12 en total). Requests de lectura/budget reemplazan DTO de respuesta usados como input.
8. Mapping de 144 tareas a rutas por responsabilidad; corrección de dependencias de sesiones/audit
   con DB y eliminación de dependencias impropias. T-002/T-004/T-005 tienen I/O y aceptación concretos.
9. Diagramas corregidos y revisados, niveles de evidencia y URL/limitaciones de bibliografía explícitos.
   ADR-017 registra ruptura del draft de contratos; ADR-018 registra rutas y delegabilidad.

`g-design/contract-migrations.json` conserva antes/después y `path-migrations.json` los destinos.
No se implementó producto, se usaron claves privadas ni se habilitó live.

## Hallazgos y bloqueos

Registro completo: [findings.json](g-design/findings.json), con ubicación, evidencia, impacto,
corrección, dependencias, estado y criterio de resolución. «RESOLVED_DOCUMENTARY» significa
corrección de especificación, nunca comportamiento del producto probado.

| ID | Severidad | Resultado / trabajo pendiente |
|---|---|---|
| GD-01 | BLOCKER | Corregido: precisión, rangos y unidades |
| GD-02 | BLOCKER | Corregido: binding Risk/reserva/intención |
| GD-03 | BLOCKER | Corregido: bytes firmados y durabilidad |
| GD-04 | MAJOR | Corregido: negativos que antes podían fallar por una causa incidental |
| GD-05 | BLOCKER | Corregido: máquinas, guards y reconciliación atómica |
| GD-06 | BLOCKER | Corregido: permisos y persistencia |
| GD-07 | MAJOR | Corregido: calibración frente a cuantiles |
| GD-08 | MAJOR | Corregido: rutas/dependencias y tres fichas fundacionales; GD-10 sigue abierto |
| GD-09 | BLOCKER | **OPEN:** comandos contables para depósito/retiro/rent/ajuste e Instrument/unidades de margen/legs |
| GD-10 | MAJOR | **OPEN:** 140 fichas necesitan interfaces, errores y oracles de aceptación concretos |
| GD-11 | BLOCKER | **OPEN:** catálogo de features, inputs de 20 estrategias y binding Prediction/Decision |
| GD-12 | MAJOR | **OPEN:** Clock/Id/UoW/JobQueue/AuditSink/EvidenceReader y requests de historial completos |
| GD-13 | MAJOR | Corregido: 12 renders y 12 revisiones visuales; evidencia en visual-review.json |
| GD-14 | MINOR | Corregido: referencias y alcance documental de fuentes |
| GD-15 | EXTERNAL_DEPENDENCY | **OPEN:** verificaciones ED-01–ED-12; no son defectos documentales por sí mismas |
| GD-16 | RESEARCH_GATE | **OPEN:** datasets y experimentación cuantitativa |
| GD-17 | MAJOR | **OPEN:** escenarios semánticos enlazados con valores y oracles independientes |

Se registraron **17 hallazgos: 10 RESOLVED_DOCUMENTARY y 7 OPEN** (5 de diseño, 1 externo y 1 experimental).
GD-09/GD-11 son los **dos BLOCKER documentales abiertos**. GD-10/GD-12/GD-17 son tres MAJOR
abiertos. Son pendientes de diseño corregibles; no se los presenta como bloqueos externos ni
como trabajo ya completado. La misión no alcanzó READY_FOR_IMPLEMENTATION. No basta con añadir
campos o texto genérico: cada cierre necesita revisar consumidores, unidades, errores y casos
numéricos. Transferir esas decisiones a los agentes implementadores incumpliría el objetivo.

## Delegabilidad

[Matriz legible](g-design/delegability.md) y [144 registros completos](g-design/delegability.json).
T-001: DONE_VERIFIED; T-002/T-004/T-005: DESIGN_READY local; las restantes **140: NEEDS_SPEC**.
Ninguna nueva tarea tiene TASK_READY mientras G-DESIGN esté NOT_READY. La primera fila delegable
corresponde a una tarea ya terminada y no autoriza volver a ejecutarla.

La matriz conserva fase, dependencias, objetivo/negativo leído, razón concreta, referencias,
hallazgos, gate, estado externo, empírico y live. La ausencia de ciclos y la resolución de IDs
pasan; no equivalen a suficiencia semántica. Los IDs históricos corregidos del bootstrap siguen
sin divergencia en tablas regeneradas. No se aumentó arbitrariamente el número de tareas.

## Evaluación de los 17 criterios del gate

| # | Criterio | Resultado |
|---|---|---|
| 1 | Sin BLOCKER documentales | FAIL: GD-09/GD-11 |
| 2 | Sin MAJOR que afecten tareas implementables | FAIL global; sólo 3 fichas de diseño local concreto |
| 3 | Contratos relevantes coherentes y suficientes | FAIL: GD-09/GD-11/GD-12 |
| 4 | Esquemas y ejemplos pasan validaciones definidas | PASS estructural; GD-17 impide atribuir semántica completa |
| 5 | Grafo consistente | PASS estructural, dependencias revisadas; suficiencia ligada a GD-10 |
| 6 | Trazabilidad completa | PASS de IDs/cobertura; oracles de pruebas aún GD-10/GD-17 |
| 7 | Tareas especificadas para agentes | FAIL: 140 NEEDS_SPEC |
| 8 | Interfaces críticas explícitas | FAIL: GD-09/GD-11/GD-12 |
| 9 | Invariantes financieras suficientes | FAIL: contratos/escenarios contables pendientes |
| 10 | Máquinas de ejecución/reconciliación | PASS documental tras correcciones; no runtime |
| 11 | Diagramas revisados | PASS: 12 renders/inspecciones, fuentes incrustadas y evidencia por archivo |
| 12 | Fuentes/permisos con niveles | PASS documental, ningún proveedor probado en runtime |
| 13 | Supuestos etiquetados | PASS: provisional, PROPOSED/BLOCKED, EXPERIMENT_PENDING |
| 14 | Riesgos/owners/gates posteriores | PASS documental: 22 riesgos y 12 dependencias; ejecución pendiente |
| 15 | No afirmar pruebas inexistentes | PASS: forma, runtime y evidencia empírica separados |
| 16 | Checks aplicables pasan | Ver validation.json; el PASS no es G-DESIGN aprobado |
| 17 | Informe y evidencia reproducible | Este informe, inventarios, migraciones, matrices, logs y PR |

## Validación realizada y límites

Comandos, tiempos, versiones y códigos de salida: [validation.json](g-design/validation.json),
[logs](g-design/logs/). `make check` incluye JSON Schema/OpenAPI, ejemplos, referencias, DAG,
tablas, Ruff, mypy, TypeScript y 12 pruebas de herramientas. `sync_docs.py --check` comprueba
regeneración sin modificaciones. `git diff --check` verifica whitespace. Al incluir logs nuevos, el check staged estricto señala
líneas vacías finales del stdout capturado; se conserva esa salida y se repite con
`core.whitespace=-blank-at-eof`, sin modificar logs ni omitir otros errores de whitespace. Los vectores incluyen
casos válidos e inválidos con keyword/path esperado. Las 20 SEM explicitan campos, pruebas y
fases, pero sus invariantes de runtime siguen sin implementar.

Los SVG son artefactos revisables. `diagrams-final/render.json` registra renderer, comandos,
hashes y códigos; `visual-review.json` registra inspección y límites. Se conservan intentos
fallidos: opción CLI antigua, browser ausente y extracción incompleta del browser. No se
presentan como renders válidos. El navegador de QA y sus dependencias son herramientas locales,
no dependencias ni nuevas capacidades del producto.

Mypy valida el esqueleto Python y TypeScript el workspace inicial. No se ejecutaron pruebas
financieras de producto, servicios PostgreSQL, integración on-chain/CEX, E2E, chaos, restauración,
benchmark de hardware, escaneo completo de seguridad, generación del cliente final ni estimación
de rentabilidad. Los ejemplos positivos acreditan forma, no un libro contable consistente.

## Dependencias externas, investigación y riesgos residuales

ED-01–ED-12 conservan owner, procedimiento y alcance bloqueado. Requieren según el caso cuentas
con cuotas/permisos, respuestas reales saneadas, formatos on-chain, derechos de almacenamiento
inferencia/entrenamiento/redistribución, licencias de código/pesos/datasets y hardware medido.
Las consultas a documentación no prueban SLAs ni acceso. La cobertura V1 de Raydium CPMM no se
extrapola a todos los lanzamientos de Solana. La revisión regulatoria es una referencia vigente
con límites; no certifica la situación jurídica del proyecto.

Datos point-in-time, cobertura de fallidos/ilíquidos, potencia estadística, costos, holdout
virgen y paper prospectivo son gates experimentales. Se admite REJECTED/INCONCLUSIVE.
No hay ventaja estadística demostrada ni autorización financiera. **LIVE_NOT_AUTHORIZED**.

## Git y continuación

El [PR de revisión](https://github.com/SaintWyss/td/pulls) y `g-design/delivery.json` identifican
commits exactos, estado de CI y alcance de entrega. No se hizo merge ni force push. La CI del PR
valida herramientas/documentación, no concede aprobación G-DESIGN.

El siguiente trabajo sigue siendo diseño: cerrar GD-09/GD-11, propagar contratos a GD-12,
construir escenarios GD-17 y reescribir las fichas GD-10 con sus oracles. Reauditar el gate.
**Después de aprobar G-DESIGN**, T-002 es la primera tarea: depende sólo de T-001 DONE y es
un módulo puro sin red, DB ni permisos externos. T-004/T-005 también tienen dependencia única
en T-001. Esta auditoría no ejecuta ninguna de ellas.
