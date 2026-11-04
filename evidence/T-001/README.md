# Evidencia de bootstrap T-001

Base remota: `28d60a237dc0b6944f2cfacc9bbdbb2b8a650a06` (README inicial).

Alcance implementado: estructura, dependencias fijadas, comandos de desarrollo,
CI y documentación importada. El contrato Settings pertenece a T-003; no se agregó
configuración runtime, lógica financiera, servicios ni un dashboard.

Los archivos `setup.log` y `check.log` registran los comandos ejecutados en este
entorno. El reporte `../../audit/validation.json` detalla la validación documental.
La CI remota y sus resultados se consultan en Actions para el commit correspondiente.
Los números Q-001–Q-144 siguen identificando criterios del backlog; no son 144 tests.

Las pruebas del validador cubren DAG válido y cíclico, dependencia ausente,
referencia externa o rota, deriva de tablas y ejemplos positivos/negativos incorrectos.
No se adjudican pruebas de integración o financieras a este bootstrap.

`lock-negative.log` registra el rechazo de un pyproject modificado sin actualizar su lock.
