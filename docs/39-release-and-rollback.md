# Releases, rollback y recuperación

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Identidad de release

ReleaseManifest incluye version semver, commit, dependency lock hashes, contratos, migraciones compatibles, configuration hash, image digests, modelo/decoder/policy revisions y evidencia de gates. Documentación y producto versionan separadamente; este blueprint es 1.0.0, no una release ejecutable.

## Rollback por tipo

Código: detener entradas, conciliar pendientes, volver a imagen compatible y smoke. DB: preferir migraciones expand/contract; rollback sólo si backward compatible y probado. Ledger: corregir mediante asientos compensatorios autorizados, no UPDATE/DELETE de fills finales. Modelo: reasignar artefacto anterior compatible, sin borrar predicciones. Fuente: deshabilitar, marcar cobertura y revisar derivados. Contrato: conservar lector histórico o migrar con manifest, nunca reinterpretar unidad monetaria.

Un rollback no cancela una transacción firmada ni revierte blockchain. Antes de cualquier reanudación consultar intentos, firmas, saldos, fees y reservas externas. Reiniciar desde backup antiguo sin reconciliación puede duplicar operaciones: modo inicial HALTED, `control_epoch` nuevo y ninguna firma hasta resolver discrepancias.

## Backup y restore

Diario: dump/snapshot consistente de PostgreSQL más manifiestos y archivos referenciados, hashes y cifrado. Guardar clave separada. Semanal: prueba de restore aislada sobre fixtures o datos permitidos, verificar hashes, foreign keys, journal balanceado, outbox receipts y asignaciones de modelos. Retención inicial 7 diarios, 4 semanales, 3 mensuales sujeto a grant; revocaciones se propagan según obligación legal aplicable.

RPO laboratorio24 h/RTO4 h son objetivos. Para live futuro, RPO financiero local por WAL archivado objetivo≤1 min y RTO≤30 min, además de recuperación desde hechos de cadena; ambos deben demostrarse en infraestructura continua y no se atribuyen al escritorio intermitente.

## Reanudación

Checklist concreto: integridad de backup; permisos/secretos rotados si necesario; schemas compatibles; reloj/cobertura; saldo y ledger conciliados; sin intentos UNKNOWN no acotados; política actual; budget; alertas críticas resueltas; aprobación de actor. Reanudar primero lectura/shadow, luego paper. El estado RUNNING anterior nunca se restaura automáticamente desde backup.

El reporte del incidente contiene impacto, intervalo, datos faltantes, posiciones, acciones, evidencia y prevención. Una prueba fallida actualiza riesgo y bloquea sólo el gate correspondiente. No se declara recuperación completada porque el contenedor aparezca healthy.
