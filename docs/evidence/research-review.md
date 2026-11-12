# ETAPA A: auditoría de la investigación

Se leyó la consigna completa (1.047 líneas) y el informe completo (467 líneas, 35.364 bytes). La copia del proyecto y el adjunto son idénticos por bytes; sus hashes figuran en el manifest. El informe es fuente de hipótesis y contexto, no autoridad para APIs o rentabilidad. Sus marcadores `turn...` y `filecite` no son enlaces recuperables dentro del archivo; no se presentan como verificados. No se recibió el video/experimento de siete días al que alude.

| Afirmación/familia del informe | Veredicto de esta revisión | Efecto en diseño |
|---|---|---|
| Más datos/IA podrían aportar señales complementarias | Hipótesis razonable, no ventaja demostrada | Fusión después de baselines y ablaciones |
| Lo/Mamaysky/Wang muestran información incremental | Verificado en fuente primaria S37 | No trasladar automáticamente a memecoins actuales |
| DeepLOB predice desde LOB | Verificado S29, dominio diferente | No usar reservas AMM como L2 |
| FreqAI/Condor/LEAN existen | Verificado S34–S36 | Referencias; núcleo propio acotado por razones del ADR |
| Kronos y modelos financieros pueden ayudar | Existencia verificada S24; PnL no probado | Challenger con costo/contaminación medidos |
| Papers sociales2025/2026, SD-FMM, Hawkes/spoofability | No se resolvió cada paper desde marcadores del informe | No usar cifras ni conclusiones como gate; investigación bibliográfica pendiente por hipótesis |
| Rendimientos de Medallion/Thorp/Rotter/BNF | No auditados en esta entrega | Se excluyen de expectativas económicas y sizing |
| Bot Claude ganó13%, BTC21%, 35 operaciones | Material primario ausente | Ejemplo no verificable; no entra en métricas |
| Hyperliquid hasta2.000 fills y rankings CEX | No verificado para integración actual | Puertos futuros; no endpoint inventado ni dependencia MVP |
| Listados de noticias y foros | No acreditan derecho de ingesta IA | SourceGrant por finalidad |
| Telegram con consentimiento | Restricción verificada S14; caso concreto pendiente | Deshabilitado hasta evidencia aplicable |
| Pasar texto a features reduce problema contractual | Insuficiente como permiso | Misma revisión de finalidad/retención/derivados |
| Reddit/X autorizan con API | No se demuestra por mero acceso | Conectores bloqueados |
| Precio GPT-5.6 citado | No guía selección actual | Tarifas/IDs nuevos verificados S17–S21; account test pendiente |
| Open source implica uso permitido de pesos/datos | Incorrecto como generalización | TimesFM3.0/FinBERT tienen advertencias específicas |
| RG1058 y RG1172 | Textos oficiales localizados S32/S33 | Mantener revisión jurídica aplicada y actualizable |
| Costos POC30–150/mes | Estimación amplia, no cotización | Presupuesto por carga, cuotas y facturas en doc31 |
| BTC/ETH primero | Conflicto con foco Solana de la consigna | Solana es universo principal; BTC/ETH/SOL controles |
| Holdout enero–septiembre2026 | Sólo ejemplo del informe; datos no suministrados | No fingir dataset existente; recolección prospectiva |
| Un stop garantiza salida | Informe ya lo limita; se conserva | Pérdida estresada100% de token; liquidez puede desaparecer |
| Autonomía de aprendizaje | Deseable bajo control | Entrenar ≠ promover; no autoautorizar live |

## Vacíos corregidos

Se incorporan universo point-in-time con muertos y gaps, timestamps de disponibilidad propia, límites de alcance por programa, distinción de balances de tokens/wallets, costos de fallos/rent, reorgs y resultado incierto, reserva concurrente, separación de signer, contabilidad por activo, límites presupuestarios transaccionales y muestreo temporal para selección de wallets.

Se reemplaza «experimento rentable» por protocolo falsable con base de costos y prueba prospectiva. No hay resultados financieros en esta especificación. Las hipótesis pueden quedar INCONCLUSIVE o REJECTED. No se necesita resolver la biografía de traders famosos para construir el laboratorio.

Las fuentes dinámicas se consultaron el2026-11-03; no se garantiza que permanezcan iguales cuando se implemente. Las tareas de onboarding deben volver a cotejar esquemas, licencias, cuotas y versiones. Rutas antiguas de Raydium devolvieron404; se resolvió la referencia actual de programas. La ruta específica de lista Birdeye no pudo recuperarse: no se fija como contrato externo.

## Revisión G-DESIGN, 2026-11-04

La consigna y el informe originales están íntegros en input-brief.txt/input-research.md.
Se conserva su texto histórico y sus citas internas sin fingir que son enlaces portables.
Las afirmaciones adoptadas tienen fuentes S01–S41. Los retornos de Medallion/Thorp,
entrevistas de scalpers y cifras de estudios sociales citados sólo con IDs internos se
clasifican como ANTECEDENTE_NO_VERIFICADO en esta auditoría; no fundamentan límites,
licencias, selección de wallets ni promesas de TD. No se reconstruyeron esos papers.

Cobertura de la consigna: Solana/seguridad docs16/20; APIs docs10/13; hardware doc27;
research/IA docs13–15; 20 familias doc18/strategies; ejecución doc21; riesgo doc20;
ciencia docs22–24; seguridad doc25; UI doc26; arquitectura docs06–12; roadmap docs32–37.
Esta correspondencia demuestra localización, no completitud: los huecos operativos
GD-09–GD-12 impiden delegar el diseño íntegro. El plan 90/180/365 del antecedente es
orientativo; los gates prevalecen sobre calendario.

Se verificaron documentos primarios para Solana, Jupiter, Raydium, DEX Screener,
proveedores LLM, modelos y normas CNV. Se reparó la URL de precios Birdeye (404 anterior)
y se recuperó el abstract de NBER por búsqueda oficial tras 403 directo. Sólo evidencia
documental; no se hicieron llamadas de mercado, firma, pagos ni canaries autenticados.

CNV: se recuperaron RG1058/2025 y RG1172/2026 (publicada 15/10/2026), que modifica el
régimen PSAV. Esto identifica normativa a revisar, no certifica la situación jurídica de
TD. Antes de capital real, servicios a terceros, señales comerciales o custodia: dictamen
profesional sobre actividad concreta, jurisdicción, impuestos, datos y obligaciones vigentes.
Telegram/Reddit/X permanecen BLOCKED para fuentes reales sin grant; licencia de código,
pesos, corpus, API, almacenamiento, ML y redistribución se evalúan separadamente.
