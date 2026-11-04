# Despliegue y entornos

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Perfiles `dev`, `research`, `paper` y futuro `live` tienen DB, directorios, usuarios, claves y redes independientes. Los nombres de entorno forman parte de IDs de comandos y claves de idempotencia. Fixtures sintéticos se usan en CI. No usar backup real con secretos en pruebas públicas.

Docker Compose inicia servicios sin privilegios, filesystem raíz read-only cuando compatible, volúmenes explícitos, límites de CPU/RAM, healthchecks y redes privadas. API escucha localhost por defecto; acceso portátil vía túnel SSH. Imágenes se fijan por digest en la tarea de bootstrap y se actualizan mediante revisión. La entrega documental no afirma cuáles digests existen hoy.

## Secuencia de release

1. Congelar commit, lockfiles, schema hashes, configuración y manifiesto.
2. Ejecutar CI y validadores; generar SBOM y evidencia de seguridad.
3. Detener nuevas entradas, esperar/reconciliar pendientes y snapshot consistente.
4. Aplicar migración expand compatible, desplegar versión candidata sin habilitar estrategias.
5. Smoke de lectura, permisos, cola, conciliación, costos y dashboard.
6. Iniciar shadow, comparar proyecciones y habilitar sólo paper aprobado.
7. Mantener versión anterior disponible; no borrar columnas hasta ventana de rollback validada.

Jobs de migración tienen credencial distinta y no se ejecutan al azar en cada worker. Migraciones financieras destructivas requieren procedimiento específico; no usar `drop/recreate` como recuperación. Esquema mínimo y máximo soportado se declara en manifest de release.

## Configuración

Settings Pydantic strict sin defaults secretos. Variables distinguen rutas, endpoints permitidos, referencias de secreto y límites; parseo al arrancar falla con mensaje saneado. `LIVE_ENABLED=false` es sólo una barrera adicional: perfiles normales carecen de signer, claves y ruta HTTP de activación. Falta de configuración crítica impide el proceso afectado, sin derribar lectura histórica segura.

Promover artifact ML no redeploya todo el producto: cambia assignment versionado tras validación. Un artefacto incompatible con schema de features se rechaza antes de cargar. El release conserva migraciones de datos y versión de decoders para reproducir cohortes anteriores.

Pruebas de instalación en máquina limpia o contenedor, puertos no expuestos, reinicio host, rollback compatible y corrupción de volumen de prueba. No prometer disponibilidad mientras el escritorio está apagado.
