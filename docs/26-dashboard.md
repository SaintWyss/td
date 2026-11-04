# Dashboard: navegación, estados y acciones

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Aplicación privada React/TypeScript, diseño escritorio con navegación lateral y resumen móvil legible. Cabecera siempre visible con entorno, modo, freshness global y control HALT. El entorno paper lleva etiqueta persistente; los valores simulados no parecen balances reales. El frontend no conserva secretos de proveedores ni wallets.

| Pantalla | Componentes y contenido | API y acción |
|---|---|---|
| Inicio | Estado de servicios, lag, presupuesto, modo, alertas activas, NAV paper | GET `/v1/system`; POST `/v1/control` |
| Fuentes | Conector, cuota, errores, gaps, permisos y expiración | GET `/v1/sources`; POST `/v1/source-grants` |
| Tokens | Tabla filtrada por edad/elegibilidad, evidencia de mint/pool, concentración, rutas | GET `/v1/assets`; GET `/v1/assets/{id}` |
| Wallets | Cobertura, PnL observable, inventario desconocido, cohortes | GET `/v1/traders`; GET `/v1/traders/{id}` |
| Investigación | Claims con fuente/recepción, contradicciones, hipótesis y resultados | GET `/v1/research`; POST `/v1/research-jobs` |
| Estrategias | Versión, estado, métricas, parámetros de sólo lectura, motivos de rechazo | GET `/v1/strategies` |
| Decisiones | NO_TRADE/candidato, razones, inputs, versiones y reserva | GET `/v1/decisions`; GET `/v1/decisions/{id}` |
| Paper | Órdenes, intentos, fills, curvas, contabilidad y cobertura | GET `/v1/orders`; GET `/v1/portfolio`; POST `/v1/paper-sessions` |
| Experimentos | Folds, costos, baselines, holdout consumido, trials negativos | GET/POST `/v1/experiments`; GET `/v1/jobs/{id}` |
| Modelos | Champion/challenger, hash, licencia, drift, comparación | GET `/v1/models`; POST `/v1/promotions` |
| Costos | Reservado/consumido/estimado por proveedor y tarea | GET `/v1/costs` |
| Operaciones | Incidentes, auditoría, backups, exportaciones, configuración versionada | GET `/v1/audit`; GET `/v1/alerts`; POST `/v1/exports` |

## Estados comunes

Cada panel implementa loading, empty, fresh, stale, partial, unauthorized y error. Empty no significa cero riesgo o cero pérdidas. `as_of` es visible; stale muestra valores anteriores con fecha y desactiva acciones dependientes. Gráficos de precio indican gaps y no conectan segmentos como observación continua. Un ticker duplicado muestra dirección abreviada y chain; copiar revela ID completo.

El drawer de decisión permite recorrer evidencia→features→señal→riesgo→orden→ledger. El usuario diferencia datos observados de inferencias. Los motivos técnicos detallados van en expansión; la acción principal usa lenguaje simple. Una alerta de liquidez ausente dice «No hay salida cotizada para este tamaño», no «el sistema está seguro».

## Mutaciones sensibles

HALT se ejecuta inmediatamente con audit ID; no hay confirmación que retrase detener. Reanudar y pasar a CLOSE_ONLY muestran alcance y requieren reautenticación/revisión esperada. Cambiar límites se realiza por configuración revisada en repo, no sliders activos en V0–V6. Promoción muestra artefactos y gates, nunca un único número de accuracy. Activar dinero real no es un toggle del panel.

Pruebas E2E de permisos, teclado, contrastes, fechas y unidades, stale-data, offline, 409 y duplicado de comando. Polling no repite POST; retry usa misma idempotency key. Se usa format local del usuario para hora, manteniendo UTC en exportación y tooltip.
