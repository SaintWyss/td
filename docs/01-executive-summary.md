# Blueprint de TD: decisión ejecutiva

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

TD será una plataforma privada de investigación cuantitativa, inteligencia de Solana y simulación de trading. El primer producto utilizable es **MVP-PAPER**, entregado al cerrar V6: descubre pools del universo soportado, conserva evidencia temporal, evalúa momentum, rechaza activos no elegibles, simula operaciones y explica cada decisión. No se entrega un bot rentable por definición; se entrega una forma reproducible de determinar si existe alguna estrategia defendible.

La especialización inicial es Solana, incluidos tokens emergentes. BTC, ETH y SOL son controles líquidos para validar infraestructura, no sustituyen el universo pedido. La cobertura inicial se limita a pools Raydium CPMM decodificados; los demás protocolos se registran como no soportados hasta disponer de un adaptador aprobado. Detectar un mint no equivale a detectar un mercado negociable.

## Decisiones cerradas

- Monolito modular Python 3.12, FastAPI, Pydantic 2, PostgreSQL 17, Parquet y DuckDB. React/TypeScript con Vite para interfaz. Procesos de API, ingesta y jobs separados, mismo repositorio y versión.
- Cola durable y outbox en PostgreSQL; sin Kafka, Redis ni Kubernetes inicialmente. Un único escritor de reservas de riesgo por cartera, con transacciones y fencing.
- Helius RPC como transporte inicial de Solana, protocolo RPC estándar como puerto portable. DEX Screener sólo enriquece. Jupiter Swap V2 aporta cotizaciones; la primera versión no firma ni envía transacciones.
- Reglas simples y LightGBM CPU como primeros modelos; XGBoost y modelos fundacionales sólo challengers. Los LLM extraen e investigan fuera del camino de ejecución.
- Operaciones spot, long-only, sin crédito, sin apalancamiento y sin fondos de terceros. USDC es unidad de cuenta operativa; USD se registra aparte con su conversión observada, sin asumir paridad perpetua.
- Autonomía para recolectar, proponer y ejecutar experimentos ya autorizados. Incorporar fuentes, promover modelos y habilitar dinero real son decisiones separadas con evidencia.

## Qué queda realmente listo

Este paquete especifica requisitos, contratos, estados, interfaces, límites, estrategias, tareas y pruebas esperadas. Los validadores incluidos comprueban el paquete documental; no son pruebas del producto. Ninguna API autenticada, hardware del usuario, estrategia o despliegue ha sido ensayado durante esta entrega. La existencia de una API en su documentación no demuestra acceso efectivo ni cumplimiento del SLO.

La ruta crítica es V0 → V1 → V2 → V3 → V4 → V5 → V6. V7–V10 agregan investigación, traders, fusión y aprendizaje. Seguridad, panel mínimo y observabilidad empiezan en V0 y crecen hasta V11; V12 evalúa preparación operativa. Las estrategias avanzadas se incorporan según sus dependencias, sin forzar su aprobación financiera.

## Condiciones que pueden detener la inversión

Falta de datos point-in-time, cobertura insuficiente de tokens fallidos, costos que eliminan el margen, intervalos de confianza inconcluyentes o restauración insegura justifican detener una estrategia o una fase. Si no aparece ventaja, TD sigue siendo útil como terminal de análisis y laboratorio. No se convierte el fracaso estadístico en una promesa de que un modelo más grande lo resolverá.

El siguiente trabajo implementable es **T-001**, descrito en `tasks/T-001.md`. Primero se crea el repositorio y se verifica el baseline documental. No se necesitan cuentas pagas ni claves de wallets para empezar.
