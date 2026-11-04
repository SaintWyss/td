# Arquitectura de IA y contratos de agentes

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Un «agente» es un componente acotado con entradas, salidas, permiso y presupuesto; no implica un LLM. Mercado, on-chain y anomalías calculan features deterministas/ML. Social extrae eventos. Investigador propone hipótesis. Traders calcula observables. Predictor produce distribuciones. Decision y Risk no invocan un LLM para autorizar órdenes.

## Gateway LLM

Puerto `extract(ExtractionRequest) -> ExtractionResult` y `propose(HypothesisRequest) -> Hypothesis`. Entradas incluyen textos autorizados, IDs de evidencia, tarea, prompt_hash, schema_hash, deadline y presupuesto. Salida estricta tipada con `abstain`, referencias existentes, entidades resueltas por mint y claims separados de observaciones. El modelo no proporciona URLs que el backend visite sin validar.

Selección inicial: `gpt-6-luna` para extracción; `gpt-6.1-sol` para investigación limitada. Fallback barato `claude-haiku-5-5`; `gemini-3.1-flash-lite` como tercer candidato. IDs y tarifas se verificaron documentalmente [S17–S21]; acceso de cuenta y compatibilidad de cada esquema se prueban antes de activarlo. No se selecciona por popularidad: un conjunto humano de 200 ejemplos, 20% adversariales y holdout separado exige ≥95% exactitud de campos críticos, 100% de referencias resolubles y ninguna llamada no permitida. Estos son umbrales de ingeniería que se miden, no resultados ya obtenidos.

El esquema canónico puede usar reglas que el proveedor no admite. Cada adaptador compila un subconjunto de salida, y después valida localmente contra JSON Schema completo y reglas semánticas. Respuesta bien formada puede seguir siendo falsa. Refusal, truncamiento, timeout y citación inventada devuelven abstención o cuarentena; nunca BUY como fallback.

## Recursos y costos

Reservar costo máximo por tokens antes de invocar. Entrada ≤16k, salida ≤2k; máximo 2 llamadas concurrentes, 10/min locales, deadline extracción 20 s e investigación 90 s. Extracción reintenta una vez sólo si resta deadline/costo; investigación hasta dos. El SDK puede cobrar respuestas fallidas: conservar usage real cuando exista, estimación conservadora cuando no. No asumir temperatura idéntica o determinismo entre proveedores.

Caché: hash de texto autorizado normalizado + prompt/schema/model/config + grant revision. TTL hasta 24 h limitado por permiso; revocación invalida caché y derivados afectables. Fallback sólo a modelos certificados para ese contrato; no cambiar durante un experimento congelado sin abrir otra variante.

## Seguridad del razonamiento

Los documentos son datos no confiables. Prompt fijo, campos separados, sin ejecución de texto, sin shell, sin claves, sin acceso directo a SQL o signer. Retrieval atraviesa allowlist, bloqueo SSRF y controles de tamaño/MIME. Los agentes pueden pedir operaciones tipadas de lectura; la aplicación autoriza cada llamada. Se registra evidencia estructurada y resumen de decisión, no se exige almacenar razonamiento privado del proveedor.
