# Dependencias externas y procedimiento de resolución

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Ninguna dependencia se cierra por suposición. El propietario del componente conserva evidencia fechada, identidad de cuenta/plan sin secretos, versión y decisión. VERIFIED_DOC no equivale a acceso contratado o prueba de producción.

| ID / responsable | Estado y procedimiento | Alcance bloqueado |
|---|---|---|
| ED-01 C-DATA | **Acceso de datos**. Doc pública disponible; cuenta no probada. Crear credenciales read-only fuera del repo; aceptar términos; consultar muestra con cuota y permisos; guardar resultado saneado y fecha. | Colectores autenticados; fixtures siguen disponibles |
| ED-02 C-OPS | **Cuotas y facturación**. Tarifas documentales; contrato/factura no comprobados. Registrar plan,unidad,CUs por método,overage y alertas; comparar100 requests autorizados con consumo del panel. | Carga continua y jobs que excedan presupuesto |
| ED-03 C-LAB | **Historia y cohortes**. No hay dataset entregado. Recolectar prospectivamente; auditar ventanas/mints muertos y gaps; verificar archivo por cuenta y permisos; si no alcanza, esperar o reducir horizonte. | Evaluación confirmatoria y scores de wallets; no bloquea motor local |
| ED-04 C-EXEC | **Cotización/rutas Jupiter**. Order/rate limits verificados; build detallado/fixtures pendientes. Revisar spec vigente de build; capturar quote/build sin firma autorizados; validar parser,route fees,tamaños,programas y TTL. | Quotes reales y preparación de transacciones; no bloquea paper fixture |
| ED-05 C-SOLANA | **Programas/layouts/upgrades Solana**. Programa documentado; bytecode/IDL no cotejado en red. Cotejar owner,program ID,upgrade authority,IDL/commit y fixtures; fijar decoders; desactivar en upgrade desconocido. | Decoder de producción y firma de rutas nuevas |
| ED-06 C-RESEARCH | **Permisos sociales/noticias**. Sin grant concreto. Obtener texto contractual/consentimiento aplicable por contexto y finalidad; revisar retención/revocación/envío a LLM y registrar evidencia. | Fuente individual y derivados; mercado-only continúa |
| ED-07 C-ML | **Licencias y compatibilidad de modelos**. Repos oficiales leídos; checkpoint exacto/lock sin instalar. Resolver versión,hash y licencia de código/pesos/datos/modelo base; probar carga aislada y recursos; rechazar si restricciones no permiten propósito. | Modelo específico; LightGBM baseline no depende de FinBERT/TimesFM |
| ED-08 C-EXEC | **Capacidades CLOB/venues**. Kraken L2 documentado; venue execution no elegido para live. Certificar tick/lot,fees,checksum,partial fills,cancel,rate limits y derechos; crear sandbox del adapter; no inventar endpoints. | Scalp/OFI/making/grid/cross-venue reales |
| ED-09 C-AI | **Cuentas LLM y formatos**. IDs/tarifas documentados; acceso no probado. Canary autorizado con texto sintético;validar schema,refusal,usage,deadline,datos/retención y budget; congelar config. | Proveedor individual; fallback sólo certificado |
| ED-10 C-OPS | **Hardware/backup/continuidad**. Hardware provisto por consigna, no medido. Inventariar RAM/VRAM/disco/red; benchmark de carga; restore cronometrado; cotizar VPS sólo si hace falta continuidad. | SLO y readiness; no obliga compra |
| ED-11 C-EXEC | **Preparación para ejecución futura**. No autorizado live. Usar devnet/claves de prueba;auditoría independiente y review jurídica;demostrar gates;si propietario decide, nueva aprobación limitada y con expiración. | Toda operación live; ninguna fase libera este bloqueo sola |
| ED-12 C-RISK | **Derivados y margen**. Sólo diseño/sandbox. Elegir venue permitido,consultar spec de contrato/funding/tiers y disponibilidad jurisdiccional;certificar risk adapter y obtener autorización específica. | Funding/delta-neutral reales y cualquier apalancamiento |

## Gestión

Cada verificación produce registro con evidencia, fecha, responsable, conclusión y próxima revisión. API/precio se revisa antes del onboarding y ante errores de contrato; permisos antes de nueva finalidad o expiración; modelos antes de nuevo checkpoint; regulación antes de actividad real/comercial. La revisión no es una automatización programada en esta entrega.

Mientras un proveedor está pendiente, las tareas locales usan fixtures y estado DISABLED. Un timeout de documentación se registra como acceso no verificado; no se sustituye por endpoint inventado. Si una fuente es rechazada definitivamente, eliminar sólo su activación, preservar contratos y evidencia de por qué se descartó.

La contratación de planes, creación de wallets con fondos y aceptación legal no se realizaron ni quedan autorizadas por este blueprint. La revisión del propietario se reserva para decisiones concretas: plan/costo/alcance, permiso aplicable, promoción y eventual operación real.
