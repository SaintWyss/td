# Estado del proyecto

Actualización: 2026-11-04 (Argentina). **G-DESIGN: NOT_READY**. Bootstrap T-001 completado;
no se implementaron T-002–T-144. Trading real: **LIVE_NOT_AUTHORIZED**.

## Evidencia y alcance

El [informe de auditoría](../../audit/G-DESIGN-FINAL-REPORT.md) registra alcance, SHA base,
contenido auditado y resultados. [Hallazgos](../../audit/g-design/findings.json) es el registro
de defectos; [delegabilidad](../../audit/g-design/delegability.json) contiene las 144 revisiones
individuales. Los checks estructurales pueden pasar mientras G-DESIGN permanece NOT_READY.

Se corrigieron precisión/unidades, binding de riesgo/firma, durabilidad y máquinas de estados,
permisos antes de almacenar, separación de calibración, negativos con motivo esperado y rutas
por dominio. Contratos 1.1.0-draft: 106 definiciones; 18 ADR; 12 diagramas renderizados y revisados.

## Bloqueos de diseño

- GD-09: comandos contables de depósitos, rent y ajustes; instrumentos y unidades de margen/legs.
- GD-11: catálogo de features y entradas suficientes para las 20 estrategias y Prediction/Decision.
- GD-12: puertos auxiliares y solicitudes de historial todavía insuficientes.
- GD-17: escenarios semánticos enlazados con oracles contables/temporales independientes.
- GD-10: 140 fichas requieren especificación concreta; corregir rutas no las vuelve delegables.

Son trabajo documental pendiente, no dependencias de APIs. No se difieren a implementadores.
T-002, T-004 y T-005 tienen **DESIGN_READY local**, pero **TASK_READY=false** por el gate global.
No interpretar el READY del historial de bootstrap como autorización vigente.

## Continuidad

Cerrar primero GD-09/GD-11 y sus consumidores; después GD-12/GD-17 y fichas GD-10.
Volver a auditar cada criterio de G-DESIGN. Tras su aprobación y autorización de implementación,
la primera tarea es T-002: sólo depende de T-001 DONE y no necesita red, DB ni credenciales.
T-004/T-005 también dependen sólo de T-001; pueden planificarse después del gate.

## Verificaciones posteriores

ED-01–ED-12 mantienen sus procedimientos, owners y gates: cuentas/proveedores, permisos por
finalidad, fixtures on-chain, datos prospectivos, licencias y capacidad real del hardware.
Experimentos: **EXPERIMENT_PENDING**; no hay alpha probado. Integraciones: no VERIFIED_RUNTIME.
No existen motor de riesgo, ledger, sesiones, signer ni dashboard funcionales. CI sólo verifica
bootstrap y documentación; no acredita seguridad operativa, integración, E2E, chaos, restore,
SBOM ni protección obligatoria de rama.

La evidencia original [T-001](../../evidence/T-001/README.md) y
[audit/validation.json](../../audit/validation.json) se preserva sin reescribir su historia.
