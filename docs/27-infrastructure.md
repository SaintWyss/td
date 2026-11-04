# Infraestructura ajustada al hardware

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Distribución inicial

Santiago-PC aloja PostgreSQL, colector, API, paper, histórico y jobs. saint-acer usa IDE, navegador, fixtures y túnel SSH. No replicar históricos completos al portátil ni levantar dos schedulers activos sobre la misma cartera. Si el escritorio se apaga, la sesión se pausa con gap explícito; la notebook no asume liderazgo financiero automáticamente.

| Recurso | Presupuesto de diseño |
|---|---|
| SO/escritorio/IDE | reservar 4 GiB RAM |
| PostgreSQL | 2 GiB, shared_buffers inicial 512 MiB, conexiones pool máximo 10 |
| Collector + API + workers | 2 GiB; workers ligeros 2 |
| Entrenamiento CPU | 4 GiB máximo, 8 hilos, un job |
| Margen | 4 GiB para caché, visualización y variación |
| GPU | opcional; verificar VRAM; presupuesto ≤6 GiB si equipo permite |
| Datos calientes NVMe | cuota inicial 100 GiB, ampliar sólo tras medir tasa |
| Histórico HDD | hasta 500 GiB de cuota; snapshot y backup independiente |

Son límites, no medición de memoria de librerías. Un perfil de entrenamiento puede requerir detener jobs secundarios. Swap no es solución para mantener latencia crítica.

## Capacidad de datos

A 10 eventos/s y 2 KiB crudos/evento: aproximadamente 1,65 GiB/día sin compresión, ~49,4 GiB/30 días. A 100/s: ~494 GiB/30 días. Agregar índices, duplicación de backup y formatos canónicos puede multiplicar almacenamiento. No prometer cubrir toda Solana con este presupuesto. Rate/cobertura se negocian mediante cohortes de programas/pools y downsampling analítico que preserva raw donde se requiere.

Colector mantiene canal de descubrimiento acotado y grupo activo máximo inicial 100 assets; suscripción no equivale a refrescar 100 quotes por segundo. Con Jupiter Free y límite interno conservador, sólo candidatos filtrados consumen quotes; reconciliación tiene prioridad. El tamaño de universo se ajusta a presupuesto real, y se registra el mecanismo de selección para evaluar sesgo.

## Continuidad

Arranque: DB → migraciones compatibles → API/observabilidad → collector → reconciler → paper paused → revisión → running. Un heartbeat de cada worker y control_epoch impiden doble liderazgo. Backup cifrado diario al HDD no cubre robo/incendio del mismo equipo: copia adicional fuera del host según presupuesto antes de live.

Futuro VPS: 2–4 vCPU, 4–8 GiB RAM y almacenamiento con snapshots como punto de partida a cotizar. Mantener entrenamiento en escritorio y enviar sólo artefactos verificados. El despliegue VPS se habilita tras benchmark y restore, no por instalar Docker. No hay alta disponibilidad real con un solo VPS; fallo de host sigue siendo un riesgo documentado.
