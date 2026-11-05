# Guía de implementación para agentes

Versión documental: **1.1.0-draft** · Fecha: **2026-11-04** · Proyecto: **TD**

## Paquete de contexto mínimo

Leer la tarea asignada, `00-index.md`, `08-domain-model.md`, ADR referidos, documentos de su componente, schemas pertinentes y archivos actuales del repo. No cargar todo el corpus en cada prompt. Antes de editar: git status, rama, HEAD y AGENTS.md aplicables; conservar cambios ajenos. Crear rama de tarea. No push/merge ni activar servicios externos sin autorización vigente.

## Procedimiento obligatorio

1. Confirmar dependencias terminadas con evidencia y contrato versionado. Si falta un dato externo, trabajar sólo con fixtures y marcar integración bloqueada.
2. Enumerar archivos dentro del alcance y leer implementaciones existentes. No crear un segundo modelo de dominio por comodidad.
3. Escribir prueba de comportamiento y caso adversarial indicado; para un cambio pequeño reversible puede bastar prueba existente pertinente, pero invariantes financieras requieren tests propios.
4. Implementar caso de uso/puerto/adaptador mínimo, sin modificar arquitectura ni añadir dependencias no justificadas.
5. Ejecutar selector de tarea, checks del módulo y gates relevantes. Una integración no validada no se declara operativa.
6. Revisar diff, secretos, contratos generados y cobertura de errores. Actualizar evidencia y estado.
7. Entregar reporte con commit/diff/comandos/exit codes/fallos/bloqueos. Terminar la tarea; no iniciar otra automáticamente salvo instrucción de coordinación.

## Precedencia y contradicciones

Orden: instrucciones vigentes del propietario → invariantes de seguridad y ADR aceptados aplicables → contrato normativo versionado → requisito/criterio → tarea → ejemplos. Una tarea no puede relajar un ADR. Si contrato y política contradicen una invariante, bloquear sólo efecto afectado y registrar `SPEC-CONFLICT` con ambas referencias, comportamiento seguro provisional y decisión necesaria. No asumir que precedencia autoriza romper otra parte; revisar impacto y aprobar una revisión documental.

Cambios de contrato requieren delta explícito, ejemplos positivo/negativo, migración y versión. Prohibido inventar una ruta externa, inferir permission scopes o sustituir UNKNOWN por cero. Estado de tarea: TODO, READY, IN_PROGRESS, BLOCKED, REVIEW, DONE, REJECTED. DONE exige evidencia; REJECTED para estrategia no significa bug resuelto.

## Estado vigente y primera tarea posterior al gate

G-DESIGN está NOT_READY. Leer `../audit/g-design/delegability.json` y el informe antes de seleccionar tareas. T-001 ya está DONE con evidencia; T-002 será la primera después del gate, pues depende sólo de T-001. T-004/T-005 también tienen diseño local concreto, pero ninguna está habilitada todavía. No suplir GD-09/GD-11/GD-12/GD-17 ni los contratos de las 140 fichas NEEDS_SPEC durante implementación.

T-001 preparó repositorio, documentación y comandos de validación de base. No implementa colectores, trading o entrenamiento. Ejecutar el validador documental incluido antes y después de integrarlo. Dependencias exactas se resuelven a versiones disponibles y lockfiles durante esa tarea; no copiar supuestos de compatibilidad como resultados de instalación.

El template `tasks/AGENT_TASK_PROMPT.md` es el texto de encargo reutilizable. `tasks/evidence.schema.json` valida el reporte; `tasks/index.json` aporta el DAG; la selección exige además delegability.json, G-DESIGN aprobado y evidencia DONE de dependencias. Cada tarea especifica archivos previstos, límites y pruebas. El agente debe detenerse si descubre una API externa distinta de la evidencia, preservando los otros módulos.
