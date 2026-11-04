> Informe histórico anterior al bootstrap. Sus pendientes reflejan ese momento; para el estado vigente consultar ../current.md.

# Informe de estado de TD — trabajo detenido

Fecha de referencia: **3 de noviembre de 2026, Argentina**. Estado: **borrador documental avanzado; auditoría y entrega final pendientes**.

Este informe responde al pedido de detener el trabajo y explicar lo revisado y lo que falta. La comprobación de estado se limitó a inventariar archivos, leer apartados relevantes, comparar algunos registros y comprobar sintaxis JSON. No se continuó la construcción del blueprint ni se implementó el producto.

## 1. Diagnóstico general

Se leyó la consigna y el informe de investigación completos, se consultaron fuentes externas y se escribió una primera versión extensa de la especificación. El resultado tiene cobertura documental amplia, pero **no está listo para entregarlo sin supervisión a una IA implementadora**.

La diferencia es concreta: existen documentos, contratos y tareas, pero falta demostrar su consistencia. Además, hay errores conocidos de sincronización entre archivos y afirmaciones anticipadas sobre verificaciones todavía no ejecutadas. La denominación interna «1.0.0» no debe interpretarse como release validada.

No asigno un porcentaje de avance: contar archivos no mide la calidad ni la completitud de una especificación. El estado correcto es «redactado en gran parte; revisión de ingeniería pendiente».

## 2. Material revisado

### Documentos de entrada

- **Texto pegado(1).txt:** consigna completa de 1.047 líneas y 31.089 bytes. Contiene visión, foco Solana, hardware, módulos, estrategias, seguridad, validación científica, estructura documental y protocolo para agentes.
- **deep-research.md:** informe completo de 467 líneas y 35.364 bytes.
- La copia de `deep-research.md` adjunta y la del proyecto se compararon por bytes y resultaron idénticas.

El informe contiene referencias internas del tipo `turn...` y `filecite` que, dentro del Markdown entregado, no constituyen una bibliografía autosuficiente. Sus afirmaciones se trataron como antecedentes que requieren verificación. El material primario del experimento de siete días mencionado en ese informe no estaba adjunto.

### Investigación externa realizada

Se registraron **40 referencias**. El grado de comprobación varía: algunas permitieron confirmar una capacidad o restricción; otras sólo identifican documentación cuya aplicación concreta sigue pendiente.

| Área | Fuentes consultadas | Alcance real de la revisión |
|---|---|---|
| Solana | RPC oficial, logsSubscribe, getSignaturesForAddress, getTransaction, sendTransaction y extensiones de tokens | Semántica de lectura, envío, confirmación, versiones y riesgos de extensiones |
| Datos y DEX | Helius, Jupiter, DEX Screener, Birdeye y Raydium | Documentación de APIs, cuotas, tarifas, rutas y programas; sin prueba autenticada |
| CLOB | Documentación de Kraken | L2, snapshots, actualizaciones y checksum; sin conexión operativa ensayada |
| LLM | Documentación de OpenAI, Anthropic y Google | IDs, precios publicados y formatos estructurados; sin canary de cuenta |
| ML | LightGBM, XGBoost, Kronos, Chronos, TimesFM, FinBERT, FinGPT y FinRL | Existencia, propósito y avisos de licencia; sin instalación o benchmark de esos modelos |
| Frameworks | FreqAI, Hummingbot Condor y LEAN | Comparación arquitectónica; no se integraron |
| Validación científica | DeepLOB, Lo/Mamaysky/Wang y Deflated Sharpe Ratio | Fuentes primarias para fundamentos y límites; no reproducidos experimentalmente |
| Fuentes sociales | Telegram, Reddit y X | Restricciones y necesidad de autorización por finalidad; no permisos otorgados a TD |
| Argentina | Textos oficiales RG 1058/2025 y RG 1172/2026 | Identificación del marco y necesidad de revisar actividad concreta; no dictamen jurídico |
| Backend | PostgreSQL, Pydantic y FastAPI | Documentación general para sustentar selección; compatibilidad del stack no instalada ni probada |

El catálogo detallado está en `docs/evidence/sources.md` y `sources.json`, dentro del archivo de borrador que acompaña este informe.

## 3. Hallazgos que cambiaron el diseño

### 3.1. Solana debe ser el universo principal

El informe sugería comenzar con BTC/ETH. La consigna pide especialización inicial en Solana y tokens emergentes. El borrador adopta Solana como universo principal y utiliza BTC, ETH y SOL como controles comparativos.

Se propuso comenzar con **Raydium CPMM** y ampliar protocolos mediante adaptadores. Es una delimitación de cobertura para el hardware y presupuesto disponibles; todavía debe revisarse si representa suficientemente las oportunidades que querés investigar. No permite afirmar que se observan todos los tokens o lanzamientos de Solana.

### 3.2. Descubrimiento y backtesting necesitan datos de fracasos

Un listado de tokens populares no representa el universo histórico. El diseño registra primeras observaciones, tokens desaparecidos, pools sin salida y períodos sin datos. La fecha de recepción propia se distingue de la fecha declarada por el proveedor.

Tampoco se puede validar scalping de segundos con velas de un minuto ni reconstruir ejecución real a partir del máximo o cierre de una vela.

### 3.3. Jupiter requiere un contrato actualizado

La documentación recuperada describe Swap API V2. El borrador propone cotizaciones para el laboratorio y un camino futuro restringido para construir, inspeccionar y enviar transacciones. La integración detallada de build, fixtures y disponibilidad de cuenta sigue pendiente.

Referencia: [Jupiter Order & Execute](https://developers.jup.ag/docs/swap/order-and-execute) y [límites](https://developers.jup.ag/docs/portal/rate-limits).

### 3.4. Envío y ejecución son hechos distintos

Una respuesta exitosa de `sendTransaction` no garantiza confirmación. Se diseñaron estados de incertidumbre, persistencia de la firma antes del envío, reservas que no se liberan por un simple timeout y reconciliación antes de reemplazar intentos.

Se distingue la atomicidad de una transacción Solana de las ejecuciones parciales de una orden CEX o de una estrategia con varias piernas.

Referencia: [Solana sendTransaction](https://solana.com/docs/rpc/http/sendtransaction).

### 3.5. El código abierto no resuelve todas las licencias

La revisión encontró avisos específicos que distinguen código, pesos y datasets en TimesFM y FinBERT. El borrador exige revisar cada artefacto antes de admitirlo. No se considera que una licencia del repositorio habilite automáticamente todos sus checkpoints o corpus.

Referencias: [TimesFM](https://github.com/google-research/timesfm) y [FinBERT](https://github.com/ProsusAI/finBERT).

### 3.6. Las fuentes sociales quedan condicionadas a permisos

Pertenecer a un canal o poder consultar una API no acredita autorización para inferencia, entrenamiento, almacenamiento o redistribución. El borrador separa esas finalidades. Transformar texto en features no sustituye la revisión de permisos.

Telegram, Reddit y X no quedaron habilitados para TD. Referencia principal revisada: [Telegram Content Licensing](https://telegram.org/tos/content-licensing).

### 3.7. Predicción, rentabilidad y aprobación operativa se separan

El diseño diferencia calidad predictiva, expectativa neta, exposición, costos, resultados prospectivos y autorización de ejecución. Un modelo entrenado no se autopromueve. Un backtest positivo no habilita dinero real. Los stops se tratan como gatillos de salida que pueden fallar por falta de liquidez.

No se verificó rentabilidad de ninguna estrategia ni se suministró un dataset que permita hacerlo.

## 4. Decisiones escritas en el borrador

Estas son decisiones de diseño propuestas durante el trabajo; no resultados de benchmark ni autorizaciones para contratar o desplegar.

| Área | Dirección escrita |
|---|---|
| Producto inicial | Laboratorio de inteligencia Solana y paper trading |
| Arquitectura | Monolito modular con límites hexagonales y contratos tipados |
| Backend | Python 3.12, FastAPI y Pydantic 2 |
| Persistencia | PostgreSQL 17, outbox/receipts y Parquet con DuckDB para análisis |
| Interfaz | React, TypeScript y Vite |
| Operación local | Escritorio para datos, procesos y entrenamiento; portátil para desarrollo y control |
| ML inicial | Reglas sencillas, regresión logística y LightGBM CPU |
| LLM | Extracción e investigación fuera del camino de autorización financiera |
| Riesgo | Determinista, con reservas atómicas, límites y rechazo ante incertidumbre crítica |
| Ejecución | Paper primero; diseño de signer separado para una etapa futura |
| Estrategia inicial | Momentum, con tendencia como benchmark y descubrimiento como observación |
| Modelos posteriores | Challengers sujetos a licencia, recursos y evidencia |
| Disponibilidad | Sesiones y gaps explícitos; no asumir escritorio disponible 24/7 |
| Dinero real | Bloqueado; completar software no equivale a aprobarlo |

Los valores numéricos de riesgo, liquidez, antigüedad, cuotas internas, latencia y aceptación estadística son políticas iniciales de laboratorio. Todavía necesitan revisión de coherencia y calibración empírica. No son recomendaciones de inversión ni umbrales cuya eficacia se haya demostrado.

## 5. Archivos efectivamente existentes

El árbol del borrador contiene **273 archivos**, con **1.918.673 bytes** en total. Este inventario se comprobó al preparar el informe.

| Elemento | Cantidad | Estado |
|---|---:|---|
| Documentos principales 00–39 | 40 | Escritos; falta revisión final |
| ADR | 16 | Redactados; consistencia global pendiente |
| Componentes registrados | 16 | Responsabilidades y contratos propuestos |
| Fichas de estrategias/políticas | 20 | Algoritmos, parámetros y experimentos propuestos |
| Requisitos registrados | 144 | Mapeados a tareas, pruebas y aceptación |
| Fichas de tareas | 144 | 1 READY y 143 TODO en el índice; ninguna implementada |
| Diagramas Mermaid | 12 | Fuentes escritas; sin render ni validación visual |
| Definiciones en JSON Schema | 102 | Generadas; sin validación formal final |
| API interna | 31 rutas, 33 operaciones | Diseño OpenAPI; no API implementada |
| Referencias de fuentes | 40 | Registro documental; alcance de revisión variable |
| Riesgos | 22 | Registro cualitativo |
| Dependencias externas | 12 | Procedimientos y alcance bloqueado definidos |
| Archivos JSON | 22 | Todos parsean sintácticamente; eso no prueba sus esquemas |

Las veinte fichas cubren descubrimiento temprano, momentum, scalping, mean reversion, breakout, false breakout, order-flow imbalance, noticias, sentimiento, copy trading, smart money, liquidez, grid, market making, arbitraje, funding-rate arbitrage, delta-neutral, tendencia, gestión de salida y selección por regímenes.

Los contratos incluyen entidades, eventos, puertos, política, máquinas de estados, payloads de observaciones, solicitudes de firma y ejemplos sintéticos. Los ejemplos no representan datos de mercado ni evidencia financiera.

## 6. Comprobaciones realizadas y no realizadas

### Realizadas

- Lectura completa de ambos documentos suministrados.
- Comparación por bytes de las dos copias del informe.
- Consultas de documentación externa registradas.
- Escritura de los archivos descritos.
- Inventario de archivos y conteo de registros.
- Parseo de los 22 JSON: sin errores de sintaxis.
- Comparación puntual que confirmó seis discrepancias del backlog.
- Comprobación de ausencia de archivos de validación y renders que se mencionan en el texto.

### No realizadas

- Validación formal de todos los JSON Schema y sus ejemplos positivos/negativos.
- Validación integral de OpenAPI, referencias y compatibilidad de clientes.
- Verificación completa del grafo de tareas, fases, ciclos y prerrequisitos.
- Auditoría semántica completa de estados, cantidades, permisos, firma, margen y contabilidad.
- Render y revisión visual de los doce diagramas.
- Auditoría completa de trazabilidad contra cada punto de la consigna.
- Pruebas autenticadas de proveedores, cuotas, latencias o historial.
- Inspección del hardware del usuario.
- Instalación y prueba del stack del producto.
- Backtests, entrenamiento, paper trading o evaluación financiera.
- Auditoría externa de seguridad o revisión jurídica aplicada.

Se prepararon dependencias auxiliares para realizar QA documental, pero instalar herramientas no equivale a haber ejecutado la auditoría. No se crearon servicios del producto, wallets operativas, transacciones ni despliegues.

## 7. Problemas conocidos del borrador

### P-01. Afirmaciones anticipadas de validación

Redacté algunos pasajes como si el validador, su reporte, el manifiesto y los renders ya estuvieran disponibles. **Eso no corresponde al estado real alcanzado.**

Faltan estos archivos:

- `tools/validate_spec.py`
- `tools/requirements-qa.txt`
- `audit/validation.json`
- `manifest.json`

Tampoco hay SVG renderizados. Las carpetas `tools/` y `audit/` están vacías.

El README y `docs/30-testing.md` contienen referencias o afirmaciones sobre esos elementos. No deben usarse como prueba de que se validó el paquete. La siguiente revisión debe corregir las afirmaciones y, si se retoma, implementar y ejecutar las comprobaciones correspondientes.

### P-02. Backlog desactualizado respecto del índice

Se corrigieron dependencias y una fase en el índice de tareas y en fichas individuales, pero la tabla general se había generado antes. Se confirmaron estas discrepancias:

| Tarea | Índice actual | Tabla de backlog anterior |
|---|---|---|
| T-054, paper fills | Agrega T-107 y T-141 | No incluye esas dos dependencias |
| T-056, sesiones paper | Agrega T-108 y T-140 | No incluye esas dos dependencias |
| T-106, experimento S01 | Fase V3 | Figura V2 |
| T-123, copy trading | T-069 y T-055 | T-069 y T-101 |
| T-125, smart money | T-069 y T-036 | T-069 y T-070 |
| T-141, gestión de salida | T-051, T-049 y T-032 | T-051 y T-053 |

Son seis discrepancias confirmadas; no afirmo que sean las únicas. Falta revisar la matriz, las fases y los demás documentos relacionados.

### P-03. Contratos amplios todavía sin prueba de coherencia

Hay 102 definiciones y ejemplos generados. Falta verificar que las referencias resuelvan, los ejemplos sean válidos, los negativos fallen por el motivo correcto y los payloads expresen todo lo que necesitan los consumidores.

La validación sintáctica de JSON no demuestra coherencia de relaciones como expiración, reserva, saldo, orden de cuantiles, permisos o correspondencia entre los bytes firmados y el intent. Las reglas semánticas se escribieron, pero no se ejecutaron como pruebas del producto.

### P-04. Granularidad de tareas todavía no auditada

Las 144 fichas contienen objetivo, alcance, dependencias, archivos, pruebas y aceptación. Parte del contenido usa una plantilla común. Falta comprobar tarea por tarea que entradas, salidas y archivos sean suficientemente específicos para un agente de menor capacidad, que ninguna tarea oculte una implementación demasiado grande y que los comandos propuestos correspondan a los archivos previstos.

Los nombres de archivos basados en números de tarea también merecen revisión antes de convertirlos en estructura definitiva del código.

### P-05. Criterios numéricos sin calibración

Los umbrales de exposición, concentración, liquidez, antigüedad, costos y latencia se eligieron como punto de partida conservador. Falta comprobar compatibilidad entre ellos, carga de API, universo elegible y horizonte de estrategia. Una política demasiado restrictiva puede no admitir ningún activo; una demasiado laxa no debe justificarse por buscar mejores resultados.

También falta revisar que los mínimos temporales, la potencia estadística, los intervalos y el control de multiplicidad se implementen con hipótesis y supuestos consistentes.

### P-06. Calidad editorial y referencias cruzadas

Quedaron detalles de espaciado, identificadores, tablas y texto generado que necesitan limpieza. Además, algunas citas están representadas por IDs de fuente y requieren resolver navegación y enlaces para la entrega final. No se ha comprobado todo el paquete visualmente.

## 8. Investigación que sigue pendiente

1. Resolver la bibliografía exacta de los trabajos sociales de 2025/2026, SD-FMM y otros estudios citados mediante marcadores no portables.
2. No usar como evidencia financiera las cifras de traders célebres ni el experimento de siete días sin recuperar sus fuentes primarias. No son necesarias para empezar el laboratorio.
3. Confirmar acceso, retención, granularidad e histórico real de cada plan de datos.
4. Cotejar on-chain programas, layouts, upgrades y fixtures de los decoders.
5. Confirmar el contrato detallado de build y las rutas que realmente puede inspeccionar el executor.
6. Revisar licencias de checkpoints y datasets concretos, además del código.
7. Certificar modelos LLM en la cuenta elegida con contenido sintético, costos, errores y esquemas.
8. Obtener permisos concretos para cualquier fuente social o de noticias que se quiera activar.
9. Medir hardware, memoria, almacenamiento, red y recuperación.
10. Definir y certificar un venue para CLOB/derivados antes de implementar integración real de esas capacidades.
11. Revisar obligaciones aplicables en Argentina antes de operación real, venta de señales, SaaS o fondos de terceros.
12. Recolectar datos y producir evidencia cuantitativa. No existe todavía una estrategia ganadora demostrada.

## 9. Estado por etapa de la consigna

| Etapa | Estado al detenerse |
|---|---|
| A — Análisis de investigación | Documentos leídos y revisión crítica escrita; verificación bibliográfica parcial |
| B — Arquitectura y ADR | Borrador de arquitectura y 16 ADR redactados |
| C — Especificación completa | 40 documentos y contratos escritos; consistencia y completitud no certificadas |
| D — Roadmap | 144 tareas y trazabilidad generadas; discrepancias conocidas pendientes |
| E — Auditoría | No completada; no existe validador ni reporte final |
| F — Paquete para implementación | No existe release validada; se conserva un checkpoint del borrador |

## 10. Dirección recomendada si se retoma

El siguiente paso adecuado es **cerrar la calidad documental antes de implementar el producto**.

Orden propuesto:

1. Corregir afirmaciones prematuras y marcar inequívocamente el estado de borrador.
2. Unificar una fuente de verdad para tareas/requisitos y regenerar backlog y matriz.
3. Revisar contratos y estados críticos de riesgo, ejecución, contabilidad y firma.
4. Crear y ejecutar validación formal de schemas, ejemplos, OpenAPI, referencias y grafo.
5. Revisar granularidad de tareas y cobertura de la consigna.
6. Renderizar diagramas, revisarlos y corregir edición.
7. Resolver o delimitar cada dependencia externa con evidencia.
8. Generar manifiesto, reporte de auditoría y paquete final versionado.
9. Sólo después considerar T-001 como comienzo de la implementación, si se autoriza continuar.

El objetivo inmediato no debería ser agregar más estrategias o documentos. Ya existe suficiente material para que la próxima fase sea una revisión de consistencia y calidad.

## 11. Qué se conserva en esta entrega

- Este informe de estado.
- Una copia comprimida del árbol del borrador, sin corregir ni presentar como aprobado.
- Los scripts que generaron la documentación, como material de continuidad.
- Un inventario de checkpoint con rutas, tamaños y hashes, que sirve para preservar el estado y **no equivale al manifiesto de una release auditada**.

El trabajo queda detenido. No se continúa la elaboración ni la implementación del producto por efecto de entregar este informe.
