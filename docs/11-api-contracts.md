# Contratos de API interna

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

La fuente normativa es `contracts/openapi.json` (OpenAPI 3.1). `contracts/domain.schema.json` define los payloads compartidos; se empaquetan en OpenAPI para generar clientes. Las rutas `/v1/...` son diseño de TD, no endpoints de proveedores. No existe ruta pública para firmar, enviar a mainnet, retirar fondos ni desactivar controles de riesgo.

## Semántica HTTP

Lecturas paginadas devuelven `items`, `next_cursor`, `as_of` y `data_status`. Cursor opaco base64url autenticado con HMAC incluye filtros, orden `(created_at,id)` y expiración 15 min; inválido=400, vencido=410. Límite 1–100, default 50. No se expone acceso SQL ni filtros arbitrarios. El usuario ve una vista por entorno; no puede mezclar paper y real.

Comandos mutantes exigen sesión, rol, CSRF y `Idempotency-Key` UUID. La huella incluye método, ruta, actor, entorno y JSON canónico. Misma clave+payload devuelve resultado previo; payload distinto=409. Se conserva clave durante 30 días y permanentemente para comandos con efecto financiero. La respuesta 202 indica job aceptado, no tarea completada. El cliente consulta `/v1/jobs/{id}`.

Errores usan `Problem`: código estable, status, detalle saneado, request_id y retryable. 401 sin sesión, 403 rol, 404 inexistente/inaccesible, 409 revisión conflictiva, 422 semántica inválida, 429 cuota, 503 dependencia. No filtrar stacktrace, tokens, seeds ni URL autenticada.

## Autenticación y autorización

Sesión opaca en cookie Secure/HttpOnly/SameSite=Strict; servidor almacena hash, expiración absoluta 8 h e inactividad 30 min. Login con usuario local, Argon2id y rate limit por cuenta/IP; permisos explícitos reader, researcher, operator, approver. No autorregistro. Bootstrap por CLI local de un solo uso, sin contraseña por defecto. Reautenticación de ≤5 min para reanudar, aprobar fuente y promover. Viewer sólo GET; researcher experimentos; operator halt/close-only/paper; approver permisos y promociones.

Mutaciones de recursos versionados incorporan `expected_revision`; falla concurrente=409 con revisión actual. Las respuestas de listado no contienen texto fuente no autorizado. Exportaciones son jobs con límites de rango, autorización al crear y al descargar, URL de un uso y caducidad.

## Tiempo real y evolución

MVP usa polling cada 5 s visible en pantalla; se pausa en pestaña oculta y aplica backoff. Históricos no se descargan completos. SSE puede añadirse mediante nuevo contrato; no se presume existente. Cambios incompatibles crean `/v2`, no se reinterpretan campos monetarios de `/v1`. Clientes TypeScript se generan de OpenAPI; un cambio de esquema exige ejemplos y prueba de compatibilidad.

Prueba crítica: el actor reader no puede iniciar paper ni cambiar grants aunque construya HTTP manualmente. La UI deshabilitada no es el control de acceso.

## Compatibilidad y reautenticación del draft 1.1

Schema canónico y OpenAPI empaquetado deben coincidir. T-004 generará tipos en
`web/src/api/generated/schema.d.ts` y wrapper en `web/src/api/client.ts`; no usar Number
para atoms/decimales. Tool propuesto: openapi-typescript 7, versión patch exacta y lock
verificados en T-004 antes de instalar; el cliente no se implementa durante G-DESIGN.
Fixtures de TypeScript deben rechazar dinero number y exigir manejo explícito de null.

Reautenticación reutiliza POST `/v1/session`: si ya existe sesión, exige Origin válido
+ CSRF actual, verifica la contraseña y rota sesión/token antes de actualizar authenticated_at
interno. Login inicial exige Origin/Host allowlist y JSON, sin sesión previa; no guardar
contraseña/cookie en registros de idempotencia. Todo endpoint sensible comprueba edad
<5 minutos en servidor. Los roles son conjuntos explícitos sin jerarquía implícita:
operator no implica approver. HALT conserva autenticación y auditoría aunque no pida una
segunda confirmación. Consultas por ID filtran actor/entorno/grants antes de responder.

## Puertos e historiales R2

[Contratos auxiliares](contracts/auxiliary-ports.md) y `contracts/ports.json` fijan métodos, contexto, errores, deadline, cancelación y recuperación. Las consultas históricas tienen schemas por tipo, corte de disponibilidad, snapshot estable y cobertura explícita. No interpretar páginas vacías como cobertura garantizada.
