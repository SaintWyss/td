# Evidencia documental

`validation.json` es una captura del validador estructural al preparar el bootstrap.
`make verify-spec` produce `latest.json` (ignorado por Git) para cada ejecución local.
Los checks fallan con código distinto de cero y el reporte enumera errores y límites.

No se valida un manifiesto de release ni comportamiento financiero. Un PASS indica
solamente que los checks descritos por el validador pasaron para ese árbol de archivos.
Las modificaciones futuras deben ejecutar nuevamente la CI y conservar su evidencia.
