# Requisitos funcionales trazables

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Requisitos derivados de la consigna con IDs estables. `requirements.json` es el registro normativo; cada fila tiene componente, contrato, tarea, prueba y criterio. Los estados son diseño, no implementación.

| ID | Fase | Requisito verificable | Componente |
|---|---|---|---|
| R-001 | V0 | Crear estructura hexagonal, locks y targets verify-spec/lint/typecheck/test-unit; copiar este paquete sin implementar negocio | C-CORE |
| R-002 | V0 | Value objects de átomos y decimal, conversión por decimals y redondeo hacia abajo | C-CORE |
| R-003 | V0 | Cargar config strict y grants sólo de fuentes documentadas aceptadas por operador; live siempre false en perfiles normales | C-CORE |
| R-004 | V0 | Integrar schemas canónicos, validadores locales y generación TypeScript OpenAPI con diff de contratos | C-API |
| R-005 | V0 | Regla automatizada impide imports de SDK, ORM y HTTP desde domain y strategies | C-CORE |
| R-006 | V0 | Bootstrap usuario local, Argon2id, login rate-limited y cookie opaca con expiración; logout revoca servidor | C-API |
| R-007 | V0 | Middleware por rol, CSRF y clave de comando con huella actor/env/path/payload y conflicto409 | C-API |
| R-008 | V0 | Append con hash anterior, actor y resultado; permisos niegan UPDATE/DELETE a runtime | C-CORE |
| R-009 | V0 | Crear tablas de identidad, observaciones, grants, jobs y outbox con claves únicas y migraciones expand | C-DATA |
| R-010 | V1 | Escribir evento con agregado y consumir con receipt único; lease60s heartbeat15s y fencing | C-DATA |
| R-011 | V1 | Reservar peor costo bajo transacción y reconciliar usage; contabilizar UNCERTAIN conservador | C-OPS |
| R-012 | V1 | Limiter compartido por organización, timeouts y jitter acotados;401/403 bloquean y429 difiere | C-DATA |
| R-013 | V1 | Escribir tmp fsync hash rename y registrar evidencia; recuperación de huérfanos sin borrar referenciados | C-DATA |
| R-014 | V1 | Adaptar getAccountInfo/getTransaction/getSignaturesForAddress con timestamp propio y versión admitida | C-DATA |
| R-015 | V1 | Abrir WSS con un mentions por suscripción, heartbeat y recepción durable por firma/slot | C-DATA |
| R-016 | V1 | Recuperar páginas before/until con solapamiento, dedup y watermark finalizado | C-DATA |
| R-017 | V1 | Batch tokens máximo30 y mapear pairs con source/fecha; no generar universo desde populares | C-DATA |
| R-018 | V1 | GET order de sólo cotización y mapping de cantidades,fees,route,timestamp; no firmar ni ejecutar | C-EXEC |
| R-019 | V1 | Validar schemas, unidades, tiempos, duplicados y retractaciones con versión de parser | C-DATA |
| R-020 | V1 | Materializar intervalos observados/gaps y membresía histórica sin borrar tokens muertos | C-DATA |
| R-021 | V2 | Validar programa e instrucciones/cuentas de inicialización usando layout fijado; distinguir mint y pool | C-SOLANA |
| R-022 | V2 | Reconstruir swaps y cambios de vault con cantidades atómicas y fees por versión | C-SOLANA |
| R-023 | V2 | Decodificar owner,decimals,supply,mint/freeze authority con evidencia de slot | C-SOLANA |
| R-024 | V2 | Enumerar TLV/extensiones y cambios de fees/epoch; observar pero bloquear entradas MVP | C-SOLANA |
| R-025 | V2 | Agrupar token accounts por owner, separar vaults identificados y reportar cobertura | C-SOLANA |
| R-026 | V2 | Aplicar policy temporal y tamaños cotizables, concentración y edad; persistir causas | C-SOLANA |
| R-027 | V2 | Detectar concentración de flujo,ciclos y retiro abrupto con reglas versionadas y evidencia | C-SOLANA |
| R-028 | V3 | Calcular retornos,volumen,volatilidad,compradores y missingness sólo con available_at pasado | C-ML |
| R-029 | V3 | Exportar Parquet con hashes,universo,cobertura y permisos; incluir fallidos y censura | C-LAB |
| R-030 | V3 | Generar folds temporales y eliminar solapamientos de etiquetas; registrar acceso al holdout | C-LAB |
| R-031 | V3 | Postear fills/fees con effect_key único y suma cero por activo en una transacción | C-LEDGER |
| R-032 | V3 | Reconstruir lotes,costo,realizado,no realizado y marca liquidable; separar flujos externos | C-LEDGER |
| R-033 | V3 | Ordenar eventos por disponibilidad y ejecutar mismas interfaces de señales/riesgo con seed | C-LAB |
| R-034 | V3 | Simular reservas por evento,fees y latencia; no usar cierre de vela ni descontar fee dos veces | C-LAB |
| R-035 | V3 | Reejecutar con slippage2x,fees1.5x,latencia y pérdida total; versionar escenario | C-LAB |
| R-036 | V3 | Calcular métricas doc23,bootstrap por bloques,comparación emparejada y Holm; exportar supuestos | C-LAB |
| R-037 | V3 | Congelar hipótesis,trial_family,max_trials y criterios antes de acceso holdout | C-LAB |
| R-038 | V4 | Entrenar logística regularizada con scaler train-only y artefacto reproducible | C-ML |
| R-039 | V4 | Entrenar12 configs preregistradas como máximo,8 hilos4GiB y early stopping interno | C-ML |
| R-040 | V4 | Ajustar Platt en validación temporal separada y emitir cuantiles ordenados con TTL | C-ML |
| R-041 | V4 | Registrar hashes,licencias,cutoff,feature schema y estado sin autopromoción | C-ML |
| R-042 | V4 | Comparar mismo target,folds y presupuesto contra LightGBM sin cambiar champion | C-ML |
| R-043 | V4 | Adaptador mini/small con contexto permitido y medición RAM/VRAM; metadata de pretraining | C-ML |
| R-044 | V4 | Adapter forecast a target común y cuantiles con datos pasados; medir costo local | C-ML |
| R-045 | V4 | Verificar checkpoint/licencia; sólo benchmark autorizado;3.0 no productivo por aviso consultado | C-ML |
| R-046 | V7 | Evaluar checkpoint autorizado en corpus humano de dominio, con evidencia de licencia de pesos/datos | C-AI |
| R-047 | V7 | Comparar artefacto específico/base/LoRA autorizado contra extracción API con budget fijo | C-AI |
| R-048 | V9 | Entrenar red acotada sólo con L2 íntegro y folds por tiempo/instrumento | C-ML |
| R-049 | V5 | Aplicar secuencia determinista,TTL,edge neto y desempate; persistir abstenciones | C-DECISION |
| R-050 | V5 | Implementar caps de policy,full-loss memecoin y rounding down; desconocido deniega | C-RISK |
| R-051 | V5 | Bloqueo de portfolio,exposición pending,expiry segura y unique decision con outbox | C-RISK |
| R-052 | V5 | Control durable con epoch; HALT inmediato,RESUME sólo paper reautenticado | C-RISK |
| R-053 | V6 | Implementar transiciones normativas y guards con versiones; efecto durable por paso | C-EXEC |
| R-054 | V6 | Crear fill simulado con quote disponible,latencia y failure model; conservar simulated true | C-EXEC |
| R-055 | V6 | Conciliar órdenes,fills,reservas y balances reconstruidos antes de liberar exposición | C-EXEC |
| R-056 | V6 | Persistir start/end,config,coverage,checkpoint y estado paused al reiniciar | C-EXEC |
| R-057 | V6 | Mostrar entorno,modo,decisiones,órdenes,stale y HALT; polling5s y permisos | C-API |
| R-058 | V7 | Aprobar/revocar finalidades con evidencia y propagar expiración a caches/datasets/modelos | C-RESEARCH |
| R-059 | V7 | HTTPS limitado,validación DNS/redirecciones,MIME/tamaño y evidencia; sin shell | C-RESEARCH |
| R-060 | V7 | Mapear request/schema al SDK oficial,validar localmente,usage/deadline y abstención | C-AI |
| R-061 | V7 | Certificar contrato con Haiku y permitir fallback sólo con misma evaluación/costo | C-AI |
| R-062 | V7 | Certificar Flash-Lite con esquema compatible y tratamiento de datos elegido | C-AI |
| R-063 | V7 | Prompt versionado identifica mint/contexto,claims,evidencia y abstención con corpus humano | C-AI |
| R-064 | V7 | Canonical URL/hash/similitud y cluster de sindicación; revisiones append-only | C-RESEARCH |
| R-065 | V7 | Proponer mecanismo,target,placebo/rechazo y ejecutar sólo plantillas admitidas con2 jobs/día | C-RESEARCH |
| R-066 | V7 | Guardar claims,relaciones,contradicciones y conclusiones negativas con búsqueda textual | C-RESEARCH |
| R-067 | V8 | Reconstruir swaps,transferencias,wraps,fees y ownership sin inferir persona | C-TRADERS |
| R-068 | V8 | FIFO por wallet con lotes UNKNOWN_COST y TWR sólo con flujos/capital observables | C-TRADERS |
| R-069 | V8 | Score por train con cobertura>=95%/90 días,clusters y selección congelada | C-TRADERS |
| R-070 | V9 | Meta-modelo logístico con señales OOF disponibles y ablaciones completas | C-ML |
| R-071 | V9 | Calcular volatilidad/tendencia/liquidez y thresholds train-only con histéresis | C-ML |
| R-072 | V10 | Unir predicción con resultado observable sólo al vencer horizonte y conservar censura/correcciones | C-LEARN |
| R-073 | V10 | Medir missingness/calibración/costos y deshabilitar entradas del modelo según política | C-LEARN |
| R-074 | V10 | Revisar gates/reportes y asignar champion en paper con compare-and-swap humano | C-LEARN |
| R-075 | V10 | Reasignar anterior compatible conservando predicciones y política de posiciones | C-LEARN |
| R-076 | V10 | Experimento FinRL con simulador validado,recompensa neta/caps y benchmark fijo | C-ML |
| R-077 | V11 | Pantalla inicio/fuentes conlag,cobertura,permisos y errores saneados | C-API |
| R-078 | V11 | Tabla filtros/as_of y drawer de mint/pool/assessment con desconocidos visibles | C-API |
| R-079 | V11 | Mostrar PnL observable,unknown_cost,cohortes y selección temporal | C-API |
| R-080 | V11 | Fuentes,claims,contradicciones y jobs con permisos de visualización | C-API |
| R-081 | V11 | Timeline evidencia→señal→riesgo→orden→ledger y rechazo visible | C-API |
| R-082 | V11 | Mostrar folds,trials negativos,baselines,CI y consumo del holdout; crear job typed | C-API |
| R-083 | V11 | Comparación champion/challenger,licencias,drift y reautenticación para promover | C-API |
| R-084 | V11 | Reservado/real/estimado por proveedor y tarifa con alerts80/100% | C-API |
| R-085 | V11 | Lectura paginada y jobs export con rango/rol/expiry; config sólo lectura | C-API |
| R-086 | V11 | Servicios no root,puertos privados,volúmenes separados,limits y arranque paused | C-OPS |
| R-087 | V11 | SnapshotDB+manifests+archivos referenciados con hashes/retención y clave separada | C-OPS |
| R-088 | V11 | Restaurar en entorno aislado,verificar hashes/journal/receipts y nuevo control_epoch | C-OPS |
| R-089 | V11 | Instrumentar lag,deadlines,budget,pending,leases y redacción de secretos;alertas dedup | C-OPS |
| R-090 | V11 | Ejecutar drillsRPC caída,DB caída,disco lleno,clock drift y restart con reporte | C-OPS |
| R-091 | V11 | Generar SBOM,scan CVE/secrets,locks y excepción con expiración sólo si admisible | C-OPS |
| R-092 | V11 | Manifest código/config/modelo/contrato y expand-contract con prueba de rollback | C-OPS |
| R-093 | V12 | Daemon sin acceso LLM valida aprobación/binding/epoch/expiry y claves sólo devnet | C-EXEC |
| R-094 | V12 | Resolver cuentas e instrucciones y verificar efectos permitidos/fees antes de firma | C-EXEC |
| R-095 | V12 | Adaptar build documentado con fixtures y permitir sólo rutas inspeccionadas | C-EXEC |
| R-096 | V12 | Simular commitment consistente,verificar balances/fees y lastValidBlockHeight; invalidar build viejo | C-EXEC |
| R-097 | V12 | Persistir bytes/signature antes de enviar;timeout conserva UNKNOWN y mismo payload | C-EXEC |
| R-098 | V12 | Consultar status/tx,balance y fee;finalizar/reconciliar;contrasteRPC para incertidumbre | C-EXEC |
| R-099 | V12 | Invalidar writers viejos con epoch y comprobar modo justo antes de firma | C-EXEC |
| R-100 | V9 | Snapshot+deltas y checksum,orden preciso y capability para replay;referencia pública documentada | C-DATA |
| R-101 | V9 | Modelo child orders conpartial fills/cancel/replace y reserva compartida;sin endpoint real | C-EXEC |
| R-102 | V9 | Contrato de tiers/mark/index/funding conocido y escenario peor pierna;instrumento no certificado denegado | C-RISK |
| R-103 | V9 | Reservar todas piernas y probar atomicidad declarada;cross-venue no atómico sólo simulación | C-EXEC |
| R-104 | V12 | Compilar gates,evidencia jurídica/costos/auditoría y disponibilidad;dejar live false | C-OPS |
| R-105 | V2 | Registrar toda creación validada; observar30 min; comparar cohortes por actividad inicial. No genera entrada MVP. En fase experimental sólo pasar a S02 si cumple elegibilidad. | C-STRATEGY |
| R-106 | V3 | Comparar cohorte completa contra lista retrospectiva popular; medir recall en intervalo auditado, no en toda cadena. | C-LAB |
| R-107 | V5 | Con barra cerrada, r5m>0 y volumen1m/mediana20 barras previas>=2; breakout del máximo5 barras previas y compradores únicos no decrecientes. Requiere30 min de historia y filtros. Comprar sólo al siguiente estado ejecutable. | C-STRATEGY |
| R-108 | V5 | Golden cruce de umbral; baseline sin compradores; fees+50% y slippage×2; placebo de timestamps. | C-LAB |
| R-109 | V9 | Cada segundo, desequilibrio de volumen comprador/vendedor10 s>0,3 y microretorno positivo; entrada sólo si edge neto inferior95%>0 y delay p99<horizonte/5. | C-STRATEGY |
| R-110 | V9 | Replay por evento con latencias1×/2×/5×; rechazar si no conserva ventaja estresada. | C-LAB |
| R-111 | V9 | z=(price−VWAP60)/std60; long si z<=−2 y régimen no tendencial; sin short en spot. VWAP/std sólo pasado. | C-STRATEGY |
| R-112 | V9 | Serie con salto permanente y reversión; no martingala; comparar compra aleatoria emparejada. | C-LAB |
| R-113 | V9 | close_t>max(high de20 barras anteriores) y volume_t>1,5×mediana previa; excluir la barra actual del canal. | C-STRATEGY |
| R-114 | V9 | Fixture que detecta leakage de incluir high actual; comparar breakout sin volumen. | C-LAB |
| R-115 | V9 | Marcar low por debajo del mínimo20; long sólo si una barra posterior dentro de3 min cierra otra vez encima del nivel, con spread admisible. No conocer cierre futuro al marcar. | C-STRATEGY |
| R-116 | V9 | Secuencia paso a paso; mismo low/high con orden distinto; prueba en régimen tendencial. | C-LAB |
| R-117 | V9 | I=(sum bidqty top5−sum askqty top5)/(suma total); long si I>0,6 durante3 updates y flujo comprador neto5 s>0; bloquear checksum inválido. | C-STRATEGY |
| R-118 | V9 | Deltas fuera de orden, cola conservadora, spoof-like cancel; DeepLOB opcional sólo challenger. | C-LAB |
| R-119 | V9 | Clasificar evento predefinido, dos orígenes independientes o comunicado primario; dirección positiva y entidad inequívoca; ejecutar después deavailable_at con decay exponencial60 min. | C-STRATEGY |
| R-120 | V9 | Ablación sin noticia y timestamps desplazados; corpus evaluado por humanos; impedir rumor sin contraste. | C-LAB |
| R-121 | V9 | z de menciones1 h respecto7 días, ponderado por diversidad de autores; long si z>2 y sentimiento>0,6, sólo con100 mensajes autorizados y al menos5 orígenes. | C-STRATEGY |
| R-122 | V9 | Remover fuentes duplicadas, control atención sin sentimiento y placebo por bloques. | C-LAB |
| R-123 | V8 | Wallet previamente elegida y coverage>=0,95; señal de compra recibida; nueva quote; rechazar si precio ya avanzó>2% o edge no cubre costos. Tamaño del follower lo fija Risk. | C-STRATEGY |
| R-124 | V8 | Follower no usa precio líder; wallets aleatorias emparejadas y cohortes ganadoras/perdedoras. | C-LAB |
| R-125 | V8 | Tres clusters independientes seleccionados en train con entradas netas en5 min; long sólo si score de cohortes>percentil80 train y quote apta. | C-STRATEGY |
| R-126 | V8 | Ablación de wallet-score, selección aleatoria y exclusión de cluster dominante. | C-LAB |
| R-127 | V9 | Liquidez ejecutable a impacto1% crece>20% en10 min y persiste3 snapshots; flujo comprador positivo; long sólo si riesgo de retiro evaluado. | C-STRATEGY |
| R-128 | V9 | Retiro súbito, liquidez unilateral y ruta que desaparece; no usar TVL como depth. | C-LAB |
| R-129 | V9 | Cinco niveles simétricos alrededor de mid congelado, spacing=max(50bps,2×costo roundtrip); cotizar compras/ventas sólo con inventario propio y reserva por orden. Sin aumentar tamaño tras pérdida. | C-STRATEGY |
| R-130 | V9 | Trayectoria monotónica debe perder/controlar y parar; fills conservadores y cancel parcial. | C-LAB |
| R-131 | V9 | Cotizar bid/ask a mid±max(2 ticks,1,5×fee_equiv), skew alejando lado que aumenta inventario; post-only cuando capability certificada. | C-STRATEGY |
| R-132 | V9 | Modelo de cola independiente y worst-case doble fill; comparar no cotizar en volatilidad. | C-LAB |
| R-133 | V9 | Comparar ida/vuelta para mismo tamaño; enviar sólo bundle de transacción atómica decodificada con min_profit>cost+buffer. Cross-venue no atómico sólo paper y exposición de leg explícita. | C-STRATEGY |
| R-134 | V9 | Simular una pierna falla, expira quote y cambio de reservas; rechazar sin atomicidad certificada. | C-LAB |
| R-135 | V9 | Long spot/short perp igual delta sólo si funding esperado conservador24 h supera todos los costos+buffer; no asumir funding futuro fijo. | C-STRATEGY |
| R-136 | V9 | Funding revierte, mark diverge, leg falla y retiro suspendido; no usar tasa realizada futura. | C-LAB |
| R-137 | V9 | Portfolio objetivo delta0; rebalance si abs(delta_notional)/NAV>0,02; respetar margen/counterparty y reservar piernas conjuntamente. No introducir opciones sin capability/modelo nuevo. | C-STRATEGY |
| R-138 | V9 | Shock de precio, margin-call y hedge unavailable; validar exposición residual por peor leg. | C-LAB |
| R-139 | V3 | Long si EMA20 cruza sobreEMA60 con60 barras completas; efectivo si cruce contrario. Sin look-ahead ni short. | C-STRATEGY |
| R-140 | V3 | Golden de EMA/crossover, mercado lateral, monotónico y misma asignación que benchmark. | C-LAB |
| R-141 | V5 | No abre. Prioridad: riesgo crítico→intentar cierre seguro; luego tiempo máximo, stop observado, trailing, reversión. Reduce-only verdadero, nunca vende más que balance disponible. | C-STRATEGY |
| R-142 | V5 | Quote desaparece, doble evento de cierre, pending previo y balance menor al solicitado. | C-LAB |
| R-143 | V9 | Clasificar con umbrales train congelados de volatilidad/tendencia; seleccionar estrategia aprobada con mayor utilidad conservadora por régimen; si ninguna cumple NO_TRADE. Histeresis2 ventanas. | C-STRATEGY |
| R-144 | V9 | Comparar pesos fijos, selector aleatorio y simple siempre-momentum; contar todos los trials. | C-LAB |
