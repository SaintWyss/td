# Requisitos no funcionales y medición

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Los siguientes valores son **objetivos de diseño**, no mediciones realizadas. T-001 fija dependencias reproducibles; las tareas de rendimiento miden estos objetivos en el hardware efectivo y conservan CPU, RAM, carga, duración y percentiles.

| ID | Objetivo inicial | Método / reacción si falla |
|---|---|---|
| NF-01 | Dominio sin red, reloj global ni proveedores | Prueba de importaciones; cualquier dependencia inversa bloquea integración |
| NF-02 | Cero decisiones con entradas futuras o faltantes críticas | Fixtures de disponibilidad y replay; invalidar evaluación |
| NF-03 | Cero duplicados económicos ante entrega repetida | 100 repeticiones y crash en cada frontera transaccional |
| NF-04 | Riesgo p99 ≤50 ms a 20 evaluaciones/s, sin red | Dataset sintético de 100 posiciones; si falla, reducir concurrencia |
| NF-05 | API de lectura p95 ≤300 ms con 5 clientes y 100 activos | Carga de 10 min; paginación ≤100, rango histórico acotado |
| NF-06 | Procesar sostenidamente 20 eventos/s; buffer ≤10.000 | Carga de 30 min y ráfaga 100/s durante 60 s; lag visible |
| NF-07 | Memoria total de servicios ≤8 GiB sin entrenamiento | RSS/cgroup cada 10 s; jobs no superan 4 GiB adicionales |
| NF-08 | Reinicio paper recuperable ≤15 min | Corte de procesos, restauración de outbox y conciliación |
| NF-09 | Backup laboratorio RPO ≤24 h, RTO ≤4 h | Restaurar en directorio aislado y verificar hashes |
| NF-10 | Sin claves en logs, repositorio o UI | Escaneo y fixtures con secretos señuelo |
| NF-11 | Cambios financieros auditados antes de confirmar API | Interrumpir almacenamiento: fallo cerrado |
| NF-12 | Resultado repetible con dataset/config/código idénticos | Hash estable para CPU determinista; tolerancia ML explicitada |
| NF-13 | No navegación exclusiva por color; teclado y etiquetas | Prueba de UI y contraste de alertas |
| NF-14 | Gasto reservado antes de llamada externa | 20 solicitudes concurrentes al borde del presupuesto |

No hay SLO de disponibilidad 24/7 durante apagados del escritorio. Cada sesión paper registra horas activas, gaps y condición de salida. La disponibilidad futura será objetivo 99,5% mensual medido en VPS, sólo después de financiar observación continua. Sin disponibilidad demostrada se bloquea cualquier prueba real con posiciones abiertas.

Latencia de proveedores no está prometida: medir llegada menos timestamp fuente, duración cliente y retraso de finalización por separado. Un promedio bajo no compensa colas largas en p99. El reloj UTC se sincroniza; si la desviación estimada supera 500 ms se suspenden entradas de horizontes cortos. Duraciones y deadlines locales usan reloj monotónico.

Se aplican límites de tamaño: respuestas crudas 2 MiB por request configurable por adaptador, texto LLM 16.000 tokens, salida 2.000, un entrenamiento pesado simultáneo. Truncar silenciosamente está prohibido; se devuelve `TOO_LARGE` o se pagina con contrato explícito.
