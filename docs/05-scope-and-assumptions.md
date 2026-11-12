# Alcance, supuestos y dependencias

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

## Primera entrega utilizable: MVP-PAPER

Incluye V0–V6, estrategia S02 momentum y controles S18 de tendencia como benchmark, ingesta prospectiva de pools Raydium CPMM aprobados, extracción de autoridades, concentración observable, evaluación de venta por cotización inversa, dataset temporal, replay, LightGBM, riesgo, contabilidad paper y panel mínimo. La detección temprana S01 se ejecuta primero como observación. Los datos pueden demostrar que ningún token supera el filtro.

Token-2022 se decodifica y observa desde V2, pero queda fuera de entradas automáticas de MVP-PAPER. Su admisión posterior exige lista de extensiones soportadas, fee accounting y pruebas de rutas. No se excluye de datasets ni estadísticas de universo: figura como no elegible, con la causa que se conocía en cada instante.

## Alcance posterior definido

V7 investigación y fuentes; V8 wallets; V9 fusión, anomalías avanzadas y estrategias adicionales; V10 aprendizaje; V11 panel y recuperación completa; V12 ejecución de laboratorio con transacciones sintéticas/devnet, validación de preparación y expediente humano. Market making, grid, arbitraje, funding y delta-neutral tienen especificación y tareas, pero no son parte del criterio de cierre del MVP.

La producción con dinero real no se activa dentro de esta entrega ni por completar el roadmap. Se diseña el camino restringido y su activación requiere otra decisión documentada del propietario. Derivados reales, custodia de terceros y distribución comercial están bloqueados hasta evaluar mercado, permisos y obligaciones específicas.

## Supuestos explícitos

El hardware descrito procede de la consigna; no fue inspeccionado. VRAM, espacio libre, temperaturas y ancho de banda deben medirse antes de jobs grandes. Se presupone Linux x86-64, Docker Engine y acceso SSH por claves; la instalación exacta es parte de V0. Todos los límites numéricos de riesgo son políticas iniciales de laboratorio, no recomendaciones para invertir.

No hay históricos completos contratados ni SLA contratado. No se asume acceso retrospectivo a balances, holders o liquidez porque una API permita consultar el estado actual. Datos históricos obtenidos hoy no reciben un falso `available_at` de ayer. Pueden servir para experimentos exploratorios con latencia asumida, etiquetados como tales; no sostienen promoción sin validación prospectiva.

## Estados de dependencia

`OPEN` exige verificación; `VERIFIED_DOCUMENTATION` significa documentación pública leída; `VERIFIED_RUNTIME` exige prueba autorizada de la cuenta; `ACCEPTED` requiere evidencia y aprobación aplicable; `REJECTED` deshabilita el componente. Todo bloqueo tiene alcance local en `38-external-dependencies.md`. Se puede desarrollar contra fixtures mientras la integración externa permanece bloqueada.
