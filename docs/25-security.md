# Seguridad y marco contractual

Versión documental: **1.0.0-draft** · Fecha: **2026-11-03** · Proyecto: **TD**

## Amenazas y fronteras

Actores: fuente maliciosa, proveedor comprometido, extensión de navegador, dependencia vulnerable, proceso investigador comprometido, error del operador y robo del host. Activos: claves, capital futuro, integridad del dataset, políticas, modelos y auditoría. Controles se prueban como propiedades de permisos y procesos, no sólo instrucciones del prompt.

Perfiles locales separados por Unix user, volumen, red y credenciales. Investigación sólo lee corpus autorizado y escribe propuestas; no accede a tablas financieras mutables. Worker paper no tiene seeds reales. Executor futuro recibe intents aprobados y credencial de signer acotada. Signer usa socket local autenticado, política propia y wallet dedicada de capital limitado; no tiene shell accesible al investigador. Claves de retiro CEX no se conceden. Una clave privada de Solana puede mover fondos por naturaleza: esa restricción no se resuelve con el checkbox «sin retiros», sino con aislamiento, inspección de transacción y capital limitado.

Secretos fuera del repo, archivos 0600/secret mounts, cifrado de disco y backups; no guardar seed en DB, prompt, logs, fixtures, navegador o variables VITE. Redactar headers, query keys y contenido sensible en trazas. SSH por claves, root login y password remotos deshabilitados; firewall privado, túnel SSH/VPN para dashboard, DB sin puerto público. TLS en accesos remotos; no `verify=False`.

## Aplicación y supply chain

Autenticación de sesiones y roles según API; CSRF, CORS con origen exacto, CSP sin inline arbitrario, escape de Markdown/HTML de fuentes, límites y auditoría. Entidades importadas validan URL, archivos y tamaños. Dependencias fijadas en lock, SBOM por release, escaneo de vulnerabilidades y secretos; vulnerabilidad crítica explotable bloquea release, excepción documentada con expiración y mitigación para otros casos. CI sin secrets de producción y sin privilegios para PRs no confiables.

## Permisos y Argentina

Los textos oficiales consultados incluyen RG 1058/2025 y RG 1172/2026 [S32,S33]. El primero diferencia intercambio por cuenta propia; el segundo modifica el régimen PSAV y categorías/obligaciones. El diseño se limita a investigación y posible capital propio. Esa delimitación no resuelve por sí sola impuestos, protección de datos, distribución de señales, valores negociables o intermediación: antes de live/comercialización se exige revisión actualizada de actividad concreta con profesional local, fecha y alcance. No extrapolar una excepción a un SaaS que ejecute fondos ajenos.

Telegram restringe usos IA y requiere evaluar excepciones y consentimiento contextual [S14]. Reddit/X permanecen desactivados sin permiso verificado [S15,S16]. Convertir texto en features no elimina obligaciones. SourceGrant verifica autorización para inferencia, entrenamiento, retención y redistribución por separado. Recolección pública de wallets tampoco autoriza combinar datos personales indiscriminadamente.

## Incidente

Detectar → HALTED durable → preservar logs/artefactos → aislar egress y credenciales afectadas → conciliar transacciones existentes → rotar claves fuera de canales de texto → restaurar aislado → revisión y reanudación explícita. Para sospecha de signer comprometido, suspenderlo; mover fondos reales sería una acción humana específica, no un playbook automatizado sin límites. RTO no obliga a reanudar si integridad no demostrada.
