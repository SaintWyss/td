# Delegabilidad de las 144 tareas

T-001: terminada. Tres fichas tienen diseño local concreto; 140 necesitan especificación.
G-DESIGN NOT_READY bloquea TASK_READY. «Delegable» no significa permiso de ejecución.

| ID | Fase | Dependencias | Estado | Delegable | Bloqueo / siguiente especificación |
|---|---|---|---|---|---|
| T-001 | V0 | — | DONE_VERIFIED | Sí | DONE; no volver a ejecutar |
| T-002 | V0 | T-001 | DESIGN_READY | Sí | Diseño concreto revisado; implementación no ejecutada; requiere cierre global G-DESIGN. |
| T-003 | V0 | T-001, T-002 | NEEDS_SPEC | No | Completar interfaz concreta de configuración/permisos/transacción y errores por operación. |
| T-004 | V0 | T-001 | DESIGN_READY | Sí | Diseño concreto revisado; implementación no ejecutada; requiere cierre global G-DESIGN. |
| T-005 | V0 | T-001 | DESIGN_READY | Sí | Diseño concreto revisado; implementación no ejecutada; requiere cierre global G-DESIGN. |
| T-006 | V0 | T-003, T-004, T-009 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-007 | V0 | T-006 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-008 | V0 | T-003, T-009 | NEEDS_SPEC | No | Completar interfaz concreta de configuración/permisos/transacción y errores por operación. |
| T-009 | V0 | T-002, T-003, T-004 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-010 | V1 | T-008, T-009 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-011 | V1 | T-009, T-010 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-012 | V1 | T-010, T-011 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-013 | V1 | T-009 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-014 | V1 | T-012, T-013 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-015 | V1 | T-014 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-016 | V1 | T-014, T-015 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-017 | V1 | T-012, T-013 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-018 | V1 | T-012, T-013 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-019 | V1 | T-014, T-017 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-020 | V1 | T-016, T-019 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-021 | V2 | T-015, T-019, T-020 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-022 | V2 | T-021 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-023 | V2 | T-014, T-021 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-024 | V2 | T-023 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-025 | V2 | T-023 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-026 | V2 | T-018, T-022, T-024, T-025 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-027 | V2 | T-022, T-025 | NEEDS_SPEC | No | Fijar campos derivados, layout soportado y tabla de errores antes de delegar el decoder/evaluador; no basta un nombre de schema. |
| T-028 | V3 | T-020, T-022 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-029 | V3 | T-013, T-020, T-028 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-030 | V3 | T-029 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-031 | V3 | T-002, T-009 | NEEDS_SPEC | No | Completar comando de journal para depósitos/rent/correcciones y golden FIFO multi-activo sin fee duplicada. |
| T-032 | V3 | T-031 | NEEDS_SPEC | No | Completar comando de journal para depósitos/rent/correcciones y golden FIFO multi-activo sin fee duplicada. |
| T-033 | V3 | T-028, T-029, T-030, T-031 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-034 | V3 | T-018, T-022, T-033 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-035 | V3 | T-034 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-036 | V3 | T-030, T-032, T-035 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-037 | V3 | T-030, T-036 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-038 | V4 | T-028, T-030, T-037 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-039 | V4 | T-038 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-040 | V4 | T-039 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-041 | V4 | T-038, T-040 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-042 | V4 | T-041 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-043 | V4 | T-041 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-044 | V4 | T-041 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-045 | V4 | T-041 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-046 | V7 | T-041 | NEEDS_SPEC | No | Completar mapping request/response/refusal/usage y prueba de permiso por procesador, sin credenciales reales. |
| T-047 | V7 | T-041 | NEEDS_SPEC | No | Completar mapping request/response/refusal/usage y prueba de permiso por procesador, sin credenciales reales. |
| T-048 | V9 | T-041, T-100 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-049 | V5 | T-026, T-040, T-041, T-028 | NEEDS_SPEC | No | Completar enlace entre Prediction, Signal y DecisionContext y regla determinista de comparación. |
| T-050 | V5 | T-026, T-032, T-049 | NEEDS_SPEC | No | Completar oracle de sizing/reserva multi-activo y servicio transaccional; guardar prueba de carrera y pérdida total. |
| T-051 | V5 | T-009, T-050 | NEEDS_SPEC | No | Completar oracle de sizing/reserva multi-activo y servicio transaccional; guardar prueba de carrera y pérdida total. |
| T-052 | V5 | T-007, T-008, T-051 | NEEDS_SPEC | No | Completar oracle de sizing/reserva multi-activo y servicio transaccional; guardar prueba de carrera y pérdida total. |
| T-053 | V6 | T-051, T-052 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-054 | V6 | T-034, T-053, T-107, T-141 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-055 | V6 | T-031, T-032, T-054 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-056 | V6 | T-020, T-055, T-108, T-140 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-057 | V6 | T-007, T-052, T-056 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-058 | V7 | T-003, T-009, T-041 | NEEDS_SPEC | No | Completar request de hipótesis/job, permisos y materialización de conocimiento con oracle específico. |
| T-059 | V7 | T-012, T-013, T-058 | NEEDS_SPEC | No | Completar request de hipótesis/job, permisos y materialización de conocimiento con oracle específico. |
| T-060 | V7 | T-011, T-012, T-041, T-058 | NEEDS_SPEC | No | Completar mapping request/response/refusal/usage y prueba de permiso por procesador, sin credenciales reales. |
| T-061 | V7 | T-060 | NEEDS_SPEC | No | Completar mapping request/response/refusal/usage y prueba de permiso por procesador, sin credenciales reales. |
| T-062 | V7 | T-060 | NEEDS_SPEC | No | Completar mapping request/response/refusal/usage y prueba de permiso por procesador, sin credenciales reales. |
| T-063 | V7 | T-059, T-060 | NEEDS_SPEC | No | Completar mapping request/response/refusal/usage y prueba de permiso por procesador, sin credenciales reales. |
| T-064 | V7 | T-063 | NEEDS_SPEC | No | Completar request de hipótesis/job, permisos y materialización de conocimiento con oracle específico. |
| T-065 | V7 | T-037, T-064 | NEEDS_SPEC | No | Completar request de hipótesis/job, permisos y materialización de conocimiento con oracle específico. |
| T-066 | V7 | T-064, T-065 | NEEDS_SPEC | No | Completar request de hipótesis/job, permisos y materialización de conocimiento con oracle específico. |
| T-067 | V8 | T-014, T-016, T-022 | NEEDS_SPEC | No | Completar WalletHistory/ValuationPolicy y entradas parciales; una Observation no representa un historial. |
| T-068 | V8 | T-031, T-032, T-067 | NEEDS_SPEC | No | Completar WalletHistory/ValuationPolicy y entradas parciales; una Observation no representa un historial. |
| T-069 | V8 | T-030, T-036, T-068 | NEEDS_SPEC | No | Completar WalletHistory/ValuationPolicy y entradas parciales; una Observation no representa un historial. |
| T-070 | V9 | T-040, T-063, T-069 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-071 | V9 | T-028, T-030 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-072 | V10 | T-040, T-055 | NEEDS_SPEC | No | Completar política operativa de ventanas/drift/CAS y salidas observables con fixtures temporales. |
| T-073 | V10 | T-072 | NEEDS_SPEC | No | Completar política operativa de ventanas/drift/CAS y salidas observables con fixtures temporales. |
| T-074 | V10 | T-007, T-008, T-036, T-041, T-072 | NEEDS_SPEC | No | Completar política operativa de ventanas/drift/CAS y salidas observables con fixtures temporales. |
| T-075 | V10 | T-074 | NEEDS_SPEC | No | Completar política operativa de ventanas/drift/CAS y salidas observables con fixtures temporales. |
| T-076 | V10 | T-035, T-041, T-072 | NEEDS_SPEC | No | Precisar features/target y manifiesto de entrenamiento por tarea; revisar estimadores y compatibilidad exacta de salida. |
| T-077 | V11 | T-057, T-089 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-078 | V11 | T-026, T-057 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-079 | V11 | T-057, T-069 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-080 | V11 | T-057, T-066 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-081 | V11 | T-055, T-057 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-082 | V11 | T-037, T-057 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-083 | V11 | T-057, T-074 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-084 | V11 | T-011, T-057 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-085 | V11 | T-008, T-057 | NEEDS_SPEC | No | Completar contrato de vista/endpoint y estados de UI por acción; fijar permiso y E2E correspondiente. |
| T-086 | V11 | T-003, T-007, T-052 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-087 | V11 | T-013, T-031, T-086 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-088 | V11 | T-055, T-087 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-089 | V11 | T-008, T-010, T-012 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-090 | V11 | T-052, T-088, T-089 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-091 | V11 | T-001, T-086 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-092 | V11 | T-075, T-088, T-091 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-093 | V12 | T-051, T-052, T-086 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-094 | V12 | T-024, T-093 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-095 | V12 | T-018, T-094 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-096 | V12 | T-095 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-097 | V12 | T-053, T-093, T-096 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-098 | V12 | T-055, T-097 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-099 | V12 | T-052, T-098 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-100 | V9 | T-012, T-013, T-019 | NEEDS_SPEC | No | Cerrar requests/resultados por método y cursor, con fixture de paginación/calidad; Observation genérica no prueba cobertura. |
| T-101 | V9 | T-053, T-100 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-102 | V9 | T-050, T-101 | NEEDS_SPEC | No | Completar oracle de sizing/reserva multi-activo y servicio transaccional; guardar prueba de carrera y pérdida total. |
| T-103 | V9 | T-034, T-051, T-101 | NEEDS_SPEC | No | Completar interfaces de persistencia/conciliación y protocolo de recovery con fixtures de corte en cada frontera. |
| T-104 | V12 | T-036, T-074, T-090, T-092, T-099 | NEEDS_SPEC | No | Completar manifiesto/runbook/comando concreto y criterio de falla; no confundir alerta con recuperación. |
| T-105 | V2 | T-021, T-026 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-106 | V3 | T-105, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-107 | V5 | T-028, T-049, T-050 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-108 | V5 | T-107, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-109 | V9 | T-034, T-100, T-101 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-110 | V9 | T-109, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-111 | V9 | T-028, T-071 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-112 | V9 | T-111, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-113 | V9 | T-028, T-050 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-114 | V9 | T-113, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-115 | V9 | T-028, T-050 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-116 | V9 | T-115, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-117 | V9 | T-100, T-101 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-118 | V9 | T-117, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-119 | V9 | T-063, T-064, T-065 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-120 | V9 | T-119, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-121 | V9 | T-063, T-064, T-070 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-122 | V9 | T-121, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-123 | V8 | T-069, T-055 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-124 | V8 | T-123, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-125 | V8 | T-069, T-036 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-126 | V8 | T-125, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-127 | V9 | T-026, T-034 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-128 | V9 | T-127, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-129 | V9 | T-101, T-071 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-130 | V9 | T-129, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-131 | V9 | T-101, T-100 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-132 | V9 | T-131, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-133 | V9 | T-103 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-134 | V9 | T-133, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-135 | V9 | T-102 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-136 | V9 | T-135, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-137 | V9 | T-102 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-138 | V9 | T-137, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-139 | V3 | T-028, T-033 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-140 | V3 | T-139, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-141 | V5 | T-051, T-049, T-032 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-142 | V5 | T-141, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
| T-143 | V9 | T-070, T-071 | NEEDS_SPEC | No | Faltan nombres/unidades/ventanas de features consumidas y fixture de señal/salida con valores esperados. |
| T-144 | V9 | T-143, T-035, T-036, T-037 | NEEDS_SPEC | No | Completar contrato de ejecución de experimento y oracle numérico independiente; fijar datasets/splits/costos por versión. |
