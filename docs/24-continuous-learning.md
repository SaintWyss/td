# Aprendizaje continuo y promoción

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

El ciclo almacena predicción al emitirla, outcome cuando madura su horizonte y correcciones por calidad. No se etiqueta hasta que la salida ejecutable es observable; resultado desconocido sigue desconocido. Cada resultado conserva model/config/dataset/prompt/source revisions y costo.

Drift de entrada: distribución de features, missingness, elegibilidad y latencia. Drift de desempeño: calibración, retorno neto, fill ratio y costos por ventanas; separar cambio real de selección causada por gaps. Umbral de alerta inicial PSI>0,2 en feature crítica o missingness>5%, ambos sostenidos dos ventanas; son heurísticas que se calibran con falsas alarmas, no pruebas suficientes de drift económico.

## Champion/challenger

Reentrenar crea challenger inmutable en job aislado con manifest hash, environment lock, licencia y reporte. Champion sigue activo. La asignación efectiva es un registro versionado por estrategia/entorno. Promover exige G-LAB y G-PAPER aplicables, comparación emparejada, revisión humana y versión esperada. Dos aprobaciones concurrentes no pueden ambas ganar: compare-and-swap.

Los LLM pueden proponer reentrenamiento y resumir evidencia. No pueden aprobar su propia salida, editar métricas ni cambiar conjunto holdout. En un proyecto individual, una segunda revisión técnica externa sería deseable antes de live; mientras no exista, ese gate queda sin cumplir según política operativa.

## Seguridad de artefactos

Descargar sólo repositorios/checkpoints permitidos, con hash y licencia; no activar `trust_remote_code` por conveniencia. Preferir formatos seguros de pesos; pickle sólo de origen propio verificado y en sandbox, nunca desde una fuente externa sin revisión. El registro impide path traversal y sustitución de archivos. Al cargar, comprobar hash y schema de features, orden/unidades y rango de entrenamiento.

## Retirada y rollback

Si champion se degrada, se deshabilitan nuevas entradas de su estrategia, se preserva gestión de posiciones y se evalúa fallback baseline previamente aprobado; no se cambia a un challenger sin evidencia. Rollback mueve la asignación a artefacto previo compatible después de revisar dataset/feature version y exposición. No reescribe predicciones ya emitidas.

Estado de modelo: REGISTERED → VALIDATED → SHADOW → PAPER_APPROVED → CHAMPION → RETIRED. Transición a CHAMPION es humana, reversible y auditada. Gates de retorno no se bypassan por baja latencia o mejor accuracy. RL queda en sandbox hasta validar simulador y demostrar mejora frente a políticas simples con el mismo presupuesto de pruebas.
