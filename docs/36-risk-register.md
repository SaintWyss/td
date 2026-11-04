# Registro de riesgos

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Probabilidad e impacto son evaluaciones cualitativas de diseño, no frecuencias medidas. El responsable actualiza estado/evidencia en cada gate oincidente; riesgo residual nunca se convierte en garantía.

| ID / riesgo | Prob. / impacto | Responsable y disparador | Mitigación / residual | Gate |
|---|---|---|---|---|
| RK-01 Sesgo de supervivencia | Alta/Crítico | C-LAB: Universo construido desde trending | Cohortes prospectivas y muertos; residual: Históricos incompletos pueden impedir inferencia | G-DATA |
| RK-02 Look-ahead/leakage | Alta/Crítico | C-LAB: Feature o label disponible después de decisión | Timestamps propios,purging,holdout; residual: Pretraining desconocido requiere prospectivo | G-LAB |
| RK-03 Overfitting/multiplicidad | Alta/Alto | C-LAB: Muchas variantes y reporte ganador | Preregistro/trials/Holm/DSR; residual: Poder limitado en regímenes raros | G-PAPER |
| RK-04 Liquidez/rug | Alta/Crítico | C-RISK: Ruta desaparece oretirada abrupta | Full-loss sizing y bloqueo nuevas entradas; residual: Stop no garantiza salida | G-RISK |
| RK-05 Autoridades/extensiones | Alta/Crítico | C-SOLANA: Hook,delegate,freeze o programa desconocido | Fail-closed/allowlist/snapshot; residual: Cambios después de observación | G-SOLANA |
| RK-06 Doble operación | Media/Crítico | C-EXEC: Timeout y reenvío con nueva firma | Persistencia previa y UNKNOWN; residual: RPCs pueden compartir falla | G-READINESS |
| RK-07 Reorg/finalidad | Media/Alto | C-EXEC: CONFIRMED pierde inclusión | No asentar final sin reconciliar; residual: Finalidad no elimina toda falla de datos | G-READINESS |
| RK-08 Contabilidad incorrecta | Media/Crítico | C-LEDGER: Fee duplicada/depósito como PnL | Double-entry/golden/conciliación; residual: Datos externos incompletos | G-LAB |
| RK-09 Prompt injection | Alta/Alto | C-AI: Fuente pide activar herramientas | Sin secretos/tools críticos,schemas y allowlists; residual: Extracciones falsas aún posibles | G-RESEARCH |
| RK-10 Robo de wallet | Media/Crítico | C-EXEC: Host/dependencia/signer comprometido | Aislamiento,capital acotado,inspección; residual: Clave deSolana sigue dando poder sobre fondos | G-READINESS |
| RK-11 SSRF/XSS | Media/Alto | C-API: URL interna/HTML de noticias | Egress policy,escape,CSP; residual: Parser nuevo requiere nueva prueba | G-OPS |
| RK-12 Licencia/permiso | Alta/Alto | C-RESEARCH: Datos públicos asumidos libres paraML | Grants por finalidad y revocación; residual: Cambios de términos | G-RESEARCH |
| RK-13 Costo API | Media/Alto | C-OPS: Poll de todos los pools oloopLLM | Reservas,budgets,dedup,cuotas; residual: Overages/factura tardía | G-OPS |
| RK-14 Apagado del escritorio | Alta/Alto | C-OPS: Heartbeat desaparece | Sesiones/gaps/restore;sinlive intermitente; residual: SinVPS no hay disponibilidad continua | G-OPS |
| RK-15 Datos spoofed/proveedor | Media/Alto | C-DATA: Schema drift oprecio incoherente | Contraste,hash,quarantine; residual: Proveedores correlacionados | G-DATA |
| RK-16 Wallet score engañoso | Alta/Alto | C-TRADERS: Costos/hedges invisibles | PnL observable/null,cohortesPIT; residual: No conocer exposición externa | G-TRADER |
| RK-17 Modelo degradado | Alta/Alto | C-LEARN: Calibración/costo empeoran | Drift y retiro;no autopromoción; residual: Detección tardía | G-LEARNING |
| RK-18 Stablecoin/depeg | Media/Alto | C-RISK: USDC se aleja deUSD | Valoración separada,stress y caps; residual: Correlación de pools | G-RISK |
| RK-19 Derivados/hedge | Media/Crítico | C-RISK: Funding gira oleg falla | Sandbox,margin tiers,peor pierna; residual: Liquidación/counterparty | G-FUSION |
| RK-20 Regulatorio Argentina | Media/Alto | C-OPS: Cambio de actividad a terceros/señales | Revisión aplicada antes de lanzamiento; residual: Normas pueden cambiar | G-READINESS |
| RK-21 Exceso de alcance | Alta/Alto | C-CORE: Muchos adapters antes de baseline | MVP y gates de valor por fase; residual: Proyecto individual requiere tiempo | G-FOUNDATION |
| RK-22 Falsa completitud de agentes | Alta/Alto | C-CORE: DONE sin pruebas ocontrato inventado | Tareas atómicas,evidencia y reviewer; residual: QA estática no prueba comportamiento | G-FOUNDATION |
