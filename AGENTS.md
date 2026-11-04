# Trabajo en TD

## Alcance y evidencia

- Leer README, docs/status/current.md, docs/37-agent-implementation-guide.md y la ficha de tarea.
- El blueprint es un borrador de diseño. No interpretar una ficha o contrato como código existente.
- Trabajar una tarea coherente por cambio. Sustituir paths provisionales `t_NNN.py` por nombres de dominio y documentar el mapping.
- No activar live, firmar transacciones, manejar claves privadas, contratar proveedores ni desplegar como efecto lateral.
- No modificar límites o criterios estadísticos para hacer pasar un resultado.
- No guardar secretos, datasets privados, logs sin sanear ni credenciales en Git.

## Estructura

Dominio y puertos no dependen de FastAPI, ORM, SDKs, red ni LLM.
Los casos de uso coordinan puertos; los adaptadores resuelven infraestructura.
No implementar componentes enteros con base en stubs o nombres del backlog.

## Comprobaciones

Ejecutar `make setup` al preparar el entorno y `make check` antes de integrar.
Cuando cambien tasks/index.json o requirements.json, ejecutar `make docs-sync`.
Agregar pruebas de comportamiento para código de negocio, incluido el caso adversarial.
Registrar lo ejecutado y sus límites. No llamar DONE a una tarea sin evidencia;
ni atribuir pruebas de producto, alpha o APIs externas a validaciones documentales.

Los cambios de arquitectura necesitan ADR; las correcciones editoriales no.
No ampliar el alcance de una solicitud hacia trading real o publicación pública.
