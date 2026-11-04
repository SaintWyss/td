# Visión de producto y casos de uso

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Usuario y resultados

El operador inicial es Santiago, dueño del entorno y de los experimentos. Un analista puede consultar resultados; un investigador puede solicitar jobs; un operador puede detener y reanudar paper; un aprobador revisa fuentes y promociones. Son permisos, no cuatro personas obligatorias. En un proyecto individual la revisión humana separa momentos y queda registrada; no se la describe como independencia organizacional.

UC-01: registrar un nuevo pool, comprobar su programa y su mint, marcar elegibilidad y conservar causas de rechazo. UC-02: reconstruir qué datos estaban disponibles al emitir una predicción. UC-03: comparar momentum contra efectivo, buy-and-hold comparable y reglas sencillas. UC-04: operar en paper y reconstruir reservas, fills y PnL tras un corte. UC-05: formular una hipótesis a partir de eventos autorizados y registrar su rechazo o aceptación experimental. UC-06: evaluar wallets sin atribuirles intenciones privadas. UC-07: detectar degradación y retirar un modelo. UC-08: detener entradas, reconciliar y restaurar con supervisión.

Cada caso produce evidencia exportable: IDs, versiones, timestamps, razones y limitaciones. La interfaz diferencia `observado`, `inferido`, `desconocido` y `simulado`; un riesgo desconocido nunca aparece como seguro. Las predicciones muestran horizonte, intervalo, versión y fecha de expiración. La rentabilidad de una wallet se llama «PnL observable» cuando falta parte del inventario o del costo de adquisición.

## Valor y límites

Éxito de ingeniería: reconstrucción reproducible y control de fallos. Éxito científico: hipótesis falsables y estimación fuera de muestra. Éxito financiero: ventaja neta y riesgo admisible demostrados de forma prospectiva. Ninguno implica automáticamente el siguiente.

No son objetivos: garantizar ingresos, manipular precios, acceder a información privada, recolectar indiscriminadamente comunidades o imitar estrategias de celebridades. No se prestan servicios de custodia o ejecución a terceros dentro del alcance actual.

## Evolución sin reescritura

`InstrumentId` identifica cadena/venue y dirección canónica; el ticker es una etiqueta no única. `VenueCapabilities` declara AMM, CLOB, spot, perpetuo, fills parciales y atomicidad. Las estrategias solicitan capacidades: un detector de imbalance de L2 no puede ejecutarse sobre reservas de un AMM como si fueran un libro de órdenes.

Los mercados futuros heredan el motor de evidencia, carteras, riesgo y permisos; agregan adaptadores, convenciones de calendario, moneda, liquidación, comisiones y reglas de margen. Esto requiere trabajo específico, pero no cambia los contratos de aprobación y auditoría. La aceptación de cada mercado depende de un certificado de capacidades y fixtures, no de la mera presencia de un nombre en una configuración.
