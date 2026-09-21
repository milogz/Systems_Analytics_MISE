# Integración de Alejandra: revisión y rescate

**Actualización:** la integración `1588e92` ya se incorporó a `main` en la carpeta habitual `Systems_Analytics_MISE`, por solicitud del usuario. No se hizo push. El respaldo local anterior está en `backup/antes_integracion_alejandra_2026-09-21/`, con ZIP, manifiesto, historial Git y `LEEME_RESTAURACION.md`. Consulte [ESTADO_EN_CARPETA_PRINCIPAL.md](ESTADO_EN_CARPETA_PRINCIPAL.md) para el estado actual. El resto de este documento conserva el registro de preparación aislada.

Estado de origen: `ec92151bf372d0c6beafda514459fc30ce6f715b` (main). Trabajo aislado en `codex/integracion-alejandra`; no se publica ni se modifica main por preparar esta copia.

## Puntos de rescate

- Respaldo íntegro del espacio original: `C:\Users\ch.gomez171\.codex\visualizations\2026\09\14\01a0a173-373d-7402-a876-6bdf54866113\rescate_integracion_alejandra\workspace_antes.zip`. Incluye archivos no registrados e ignorados; `.git` se conserva por separado como bundle.
- Manifiesto SHA-256: `C:\Users\ch.gomez171\.codex\visualizations\2026\09\14\01a0a173-373d-7402-a876-6bdf54866113\rescate_integracion_alejandra\manifest.json`.
- Historial Git verificado: `C:\Users\ch.gomez171\.codex\visualizations\2026\09\14\01a0a173-373d-7402-a876-6bdf54866113\rescate_integracion_alejandra\historia_antes.bundle`.
- Guías originales legibles en `docs/integracion_alejandra/guias_anteriores/`.

Para inspeccionar o recuperar, **extraer el ZIP en una carpeta nueva**, cotejar el manifiesto y copiar únicamente los archivos deseados. No extraer encima de trabajo posterior. El bundle permite clonar el historial en otra carpeta. Mientras main permanezca intacto, basta volver a esa copia para seguir usando el material anterior. Si esta rama se integra después, revertir su commit de integración restaura los archivos afectados sin reescribir historia.

## Alcance de la intervención

Ocho guías de ruta, siete páginas de ejemplos seleccionados con enlaces y atribución, una guía transversal del proyecto y convenciones comunes. Lecturas y notebooks completos conservados. Se corrigen especificaciones incompatibles del informe y afirmaciones puntuales; `cambios_conceptuales.json` registra texto anterior/nuevo. Las Sagas reciben notas de alcance en Markdown, conservando exactamente sus celdas de código y salidas guardadas.

El PDF del proyecto se distribuye sin modificaciones. Sus propuestas de rediseño finales no se convierten en reglas aprobadas. Los ejemplos de tres proyectos mencionados en el PDF no se asignan sin sus archivos. Los videos/quices remiten al LMS sin afirmar que ya estén disponibles.

## Revisión docente antes de publicar

La ruta reserva 12 h/semana: tiempos presupuestados, no medidos. Seleccionar videos y quices dentro de ese presupuesto, no acumular todos. Acordar la articulación del ejercicio Windpeshi con el taller manteniendo la distribución del 55 % fuera del proyecto. Confirmar la disponibilidad de realimentación antes de cada avance. No cambiar rúbricas para forzar oscilaciones o inversiones de ranking: documentar resultados honestos y discutir discrepancias con el tutor.

Los simuladores externos se usan como recursos explicativos, con alternativas mediante ejemplos resueltos. La compilación del libro no equivale a ejecutar o certificar todos los modelos. Las notas de alcance mejoran la interpretación; no reemplazan una auditoría empírica ni una actualización de las series.
