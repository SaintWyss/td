# Catálogo de fuentes y adaptadores

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Consulta documental: 2026-11-03. Las rutas de este apartado son externas verificadas por documentación; las de OpenAPI son propuestas de TD. No se hizo una llamada autenticada ni una prueba de latencia. Los precios son referencias USD antes de impuestos, sujetos al checkout y a condiciones de cuenta.

| Fuente | Uso y acceso documentado | Límite/costo observado | Decisión y verificación pendiente |
|---|---|---|---|
| Helius [S01,S02] | RPC Solana estándar, archivo y herramientas de transacciones | Free: 1M créditos/mes y 10 RPS; Developer: USD49, 10M y 50 RPS. Métodos cuestan créditos distintos | Principal RPC; medir consumo real. No usar precio promocional de Parsed Events ya vencido |
| Solana RPC [S03–S06] | logsSubscribe; getSignaturesForAddress; getTransaction; sendTransaction | Cuota depende del proveedor | Puerto portable. HTTP de recuperación por cursor y WSS por programa. Endpoint público sólo desarrollo |
| DEX Screener [S07] | `/token-pairs/v1/{chainId}/{tokenAddress}` y `/tokens/v1/{chainId}/{tokenAddresses}` | 300 requests/min para estos recursos; hasta 30 addresses en batch de tokens | Enriquecimiento; no censo de nuevos mints ni histórico point-in-time garantizado |
| Birdeye [S08,S09] | OHLCV, trades, holders y seguridad según plan | Standard 30k CU/1 RPS; Lite USD39/2,5M CU/15 RPS; Premium USD199/20M/50 RPS y WSS | Opcional. Contratar sólo tras medir cobertura y permiso de retención/ML; no afirmar histórico completo |
| Jupiter [S10,S11] | `https://api.jup.ag/swap/v2/order`, `/build`, `/execute` según camino | Keyless 30/min; Free con key 60/min; límites por organización | MVP sólo `/order` para quote. El modo real futuro usa `/build` y envío RPC propio para restringir rutas; fees según respuesta/documentación |
| Raydium [S12] | Programa CPMM y referencias oficiales de cuentas | No se verificó SLA ni precio de archivo | Decoder inicial; cotejar programa, layout e historial de upgrades antes de activar |
| Kraken [S13] | WebSocket v2 `book` para L2 con checksum; otros canales sujetos a su spec | Acceso público de mercado; restricciones y cuotas por contrato | Controles BTC/ETH/SOL, sin trading real CEX inicial |
| Noticias oficiales | Comunicados, calendario, repositorios académicos y feeds licenciados | Retención, redistribución y latencia variables | Empezar con URLs permitidas por SourceGrant; fechas de revisión explícitas |
| Telegram [S14] | Uso IA restringido; excepciones sujetas a consentimiento contextual de usuarios relevantes | Ser miembro o admin no acredita permiso general | Deshabilitado hasta revisión por fuente/finalidad |
| Reddit y X [S15,S16] | Términos de API y políticas de uso | No se verificó licencia suficiente para este proyecto | Deshabilitados. No inferir autorización a partir de acceso técnico |
| News premium / perfiles CEX | Tree/DB/Whale Alert/Lookonchain, rankings y plataformas citadas en informe | No se verificó contrato, API de exportación o costo aplicable | Candidatos de investigación, sin integración comprometida |

## Contrato operativo común

`ConnectorCapabilities`: historial mínimo real, timestamp fuente, cursor, reorgs, granularidad, cuotas, permiso de guardar, usar en inferencia, entrenar y redistribuir. El adaptador conserva payload permitido, evidencia, parser version y calidad; nunca entrega objetos del SDK al dominio.

Lecturas: timeout connect 3 s, total 10 s; hasta 3 intentos con backoff exponencial y jitter, respetando Retry-After; circuit breaker tras 5 fallos consecutivos, prueba única a los 60 s. Cada proveedor tiene limitador global compartido; varios workers no multiplican cuotas. 401/403 bloquean y alertan; 429 difiere; esquema desconocido va a cuarentena. La configuración interna comienza al 50% de la cuota documentada y reserva margen para reconciliación.

Latencia, completitud y derechos son dimensiones distintas. Ningún fallback reemplaza un precio por otro silenciosamente: cambia source_id, registra el evento y exige equivalencia de unidad, reloj, finalidad y frescura. Cuando falta equivalencia, NO_TRADE. En Solana, un segundo RPC sirve para contraste; no garantiza independencia si ambos usan la misma infraestructura.

Los enlaces oficiales y sus afirmaciones verificadas se registran una sola vez en `evidence/sources.json` y `evidence/research-review.md`. Cada adaptador exige fixtures obtenidos legalmente, mínimos y sin credenciales.
