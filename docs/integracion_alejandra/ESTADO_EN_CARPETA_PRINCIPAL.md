# Estado de la integración en la carpeta principal

La versión integrada está ahora en `Systems_Analytics_MISE`, rama `main`. Se incorporó mediante avance directo de `ec92151` a `1588e92`, sin reemplazar manualmente archivos ni reescribir el historial. No se hizo push ni se publicó desde esta tarea.

## Respaldo anterior

Carpeta local: `backup/antes_integracion_alejandra_2026-09-21/`.

- `workspace_antes.zip`: 1.385 archivos anteriores, incluyendo archivos sin registrar e ignorados, excepto `.git`.
- `manifest.json`: SHA-256 por archivo; se cotejó con el espacio principal antes del traslado.
- `historia_antes.bundle`: historial Git recuperable de la versión anterior.
- `LEEME_RESTAURACION.md`: estado pendiente previo y procedimiento de recuperación.

La carpeta `backup/` se excluye de Git. Es una copia local, no se sube a GitHub ni forma parte del libro. Las guías semanales anteriores también quedan registradas como archivos legibles en `docs/integracion_alejandra/guias_anteriores/`.

Para recuperar, extraiga el ZIP en una carpeta nueva y compare antes de copiar archivos; no sobrescriba trabajo posterior. Si la integración ya está publicada, puede revertirse su commit después de revisar las dependencias posteriores, sin forzar el historial remoto.

## Material activo y publicación

El índice y las guías activas viven en `coursebook/`. Las lecturas fuente están en `marco_teorico/` y los notebooks fuente en `notebooks/`; `build_book.py` ensambla sus copias. El PDF del proyecto se distribuye desde `coursebook/_static/proyecto_integrador_alejandra.pdf` sin modificaciones.

El siguiente push de `main` que incluya `1588e92` contiene cambios en las rutas que activan el flujo de GitHub Pages. Ese flujo ensambla y reconstruye el sitio. Las modificaciones locales ajenas a la integración se preservan: el PDF original y los informes de revisión continúan sin registrar, y la eliminación del archivo temporal de PowerPoint continúa pendiente. No hace falta incluir esos archivos para publicar el libro integrado.

La compilación y las comprobaciones de conservación se documentan en `VERIFICACION.md`. No se modificaron motores de simulación ni sus salidas. Sigue pendiente la inspección visual completa y la comprobación de ejecución de los simuladores externos.
