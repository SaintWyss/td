# Criterios de aceptación y gates

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

Un gate tiene veredicto PASS/FAIL/INCONCLUSIVE/BLOCKED, evidencia hash, commit, fecha y revisor. No se aprueba por checklist sin ejecutar. Los umbrales numéricos son políticas iniciales del laboratorio, versionadas antes del experimento.

| Gate | Criterio verificable |
|---|---|
| G-FOUNDATION | Contratos válidos, límites de import, auth negativa, secretos ausentes, live inaccesible |
| G-DATA | Replay idempotente, tiempos propios, gaps visibles, grants y cuotas respetados, muestra con tokens fallidos |
| G-SOLANA | Decoder con fixtures y programa cotejado; extensiones desconocidas bloquean; concentración con cobertura |
| G-LAB | Dataset inmutable, splits/purging correctos, contabilidad golden, costos/latencia; no leakage probado por casos adversariales |
| G-MODEL | Hash/licencia/lineage completos, calibración separada y comparación con baseline bajo mismo presupuesto |
| G-RISK | Concurrencia no excede exposición, cap pérdida/fees, modo durable, desconocidos deniegan, ninguna ruta evita reserva |
| G-PAPER | Criterios del doc23, mínimo 90 días y potencia suficiente; costos estresados y límites; si faltan regímenes, alcance restringido o INCONCLUSIVE |
| G-RESEARCH | Fuentes autorizadas, referencias resolubles, no herramientas privilegiadas, suite injection/SSRF y budget concurrencia |
| G-TRADER | Transferencias/costos desconocidos tratados, ranking PIT, prueba follower con latencia y selección ex ante |
| G-FUSION | Meta-features OOF temporales, ablaciones/placebos, control de multiplicidad y mejora neta material |
| G-LEARNING | Entrenamiento no autopromueve; CAS, holdout consumido, rollback compatible y outcome no anticipado |
| G-OPS | Restore aislado demostrado, roles, incidentes, SLO medidos, dependencias actuales, costos reconciliados |
| G-READINESS | Simulación/decodificación, signer restringido, UNKNOWN/reorg/duplicado/expiración, reconciliación y auditoría independiente |

G-READINESS no concede autorización financiera. Live adicional requiere aprobación explícita del propietario ligada a wallet/chain/capital/estrategia/policy/build/fecha de expiración; revisión externa de seguridad/operación y marco contractual vigente; disponibilidad continua y fondo de fees; ensayo de kill switch y recuperación. Sin cualquiera de ellos el perfil live sigue bloqueado. La aprobación no puede generarla un LLM.

## Cierre documental

Comprobar 40 documentos requeridos, 12 diagramas, ADR, estrategias, contratos, ejemplos, tareas y trazabilidad sin IDs rotos. La auditoría distingue verificación estática ejecutada de pruebas futuras del producto. Las dependencias externas están declaradas con verificación y alcance bloqueado; no son secciones vacías ni hechos inventados.

Diseño completo significa alcance modelado y trabajo descompuesto. No significa cuenta de proveedor habilitada, licencia resuelta para toda fuente, ventaja demostrada ni software implementado. Esos estados permanecen explícitos hasta obtener evidencia real.
