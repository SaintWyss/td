# Estado del proyecto

Actualización: 2026-11-04 (Argentina). Estado: **base de desarrollo y diseño en borrador**.

## Incorporado en este bootstrap

- Repositorio privado, estructura hexagonal Python y workspace TypeScript.
- Dependencias de desarrollo fijadas, comandos Make y CI con permisos de lectura.
- Validador offline de contratos, ejemplos, referencias y trazabilidad.
- Pruebas que introducen errores para comprobar que el gate los detecta.
- Sincronización reproducible del backlog, requisitos y matriz desde sus JSON.
- Corrección de discrepancias del informe previo en T-054, T-056, T-106,
  T-123, T-125 y T-141; fase R-106 sincronizada con el catálogo.
- README y plan de pruebas corregidos: ya no afirman que existen SVG,
  un manifiesto de release o verificaciones de producto todavía ausentes.

Los resultados estructurales están en [audit/validation.json](../../audit/validation.json).
Los logs de bootstrap y su alcance están en [evidence/T-001](../../evidence/T-001/README.md).
La existencia de una ficha o esquema no equivale a implementación.

## Pendiente, en orden recomendado

1. Revisar el detalle semántico de contratos y fichas: unidades, relaciones entre
   campos, nombres de archivos definitivos y casos negativos específicos.
2. Completar V0 por dependencias: cantidades exactas (T-002), configuración y
   permisos (T-003), generación del cliente tipado (T-004), límites de importación
   (T-005), identidad, auditoría y migraciones (T-006 a T-009).
3. Incorporar proveedores con fixtures y permisos comprobados; después, ingesta
   temporal, cobertura y decodificación Solana. Sin claves o llamadas reales en CI.
4. Construir replay, contabilidad, costos y evaluación estadística antes de paper.
5. Implementar UI y operaciones conforme al backlog; probar restauración,
   consumo de RAM y ejecución intermitente en el hardware objetivo.

## Límites de la revisión

- Las 20 reglas semánticas son especificaciones pendientes de pruebas de producto.
- Los diagramas no tienen renders verificados. Los enlaces se comprueban por
  existencia de archivo, no por anchor ni vigencia de páginas externas.
- El borrador puede conservar problemas editoriales y decisiones por revisar.
- Los originales y el informe histórico no se reescriben como si sus comprobaciones
  hubieran ocurrido antes. Consultar la fecha y el alcance de cada evidencia.
- No se probaron estrategias con datos adecuados ni se demostró alpha.
- No están implementados controles de riesgo, sesiones, ledger, firmas o servicios.
- Escaneo de dependencias/secretos automatizado, SBOM, integración, E2E, chaos,
  protección de rama y releases quedan pendientes. CI es un check, no una regla
  de protección de rama obligatoria.

Este repositorio no activa live ni habilita acceso de terceros. La política y los
permisos descritos son requisitos que deberá cumplir una implementación futura.
