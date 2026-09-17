# Caso Consultoria Sistemica SA-MISE — edición didáctica

Esta edición recupera la secuencia **intuición → técnica → aplicación profesional**, con lectura acompañada de resultados. El libro contiene preludio y ocho semanas; el caso contiene ocho etapas centradas en decisiones del SIN. La aplicación solar es complementaria.

## Leer y trabajar

- Para leer y ejecutar en orden, usar `cuadernos_integrados/`: combina marco y práctica.
- Para editar narrativa, usar `marco_teorico/`; para editar experimentos, `practica_computacional/`.
- `construir.py` genera los integrados; nunca editar esas copias a mano.
- `python verificar.py` ejecuta pruebas y notebooks con kernels nuevos, y reensambla. El registro actual queda en `VERIFICACION.json`.
- `jupyter-book build .` genera HTML; `_build/` es una salida, no otra fuente.

Instalar `requirements.txt` en un entorno de Python compatible. La versión efectivamente probada queda en el registro de verificación. La publicación en GitHub Pages no se modifica con este paquete.

## Dos recorridos, componentes compartidos

Libro y caso conservan copias para poder usarse por separado. Los componentes comunes se mantienen en el libro y se sincronizan con `sincronizar_caso.py`, que registra hashes. Código, datos y pruebas compartidos no deben editarse de forma independiente en el caso. El documento `MAPA_EDITORIAL.md` distingue fuentes y derivados.

Los archivos históricos del proyecto no se modifican. Esta edición es una revisión docente, no aprobación institucional ni modelo calibrado del SIN. Las conclusiones de los estudiantes deben distinguir hechos observados, mecanismos ilustrados y evaluación condicionada.


## Verificación en entornos restringidos

`python verificar.py --local` ejecuta cada notebook en un proceso IPython nuevo y captura texto, tablas y figuras sin abrir puertos. Es la alternativa usada en esta entrega porque Windows impidió crear el archivo seguro de conexión de Jupyter. Comprueba las celdas, pero no el transporte del kernel ni la interfaz de Jupyter. El modo sin `--local` conserva la verificación con NotebookClient para un entorno que permita iniciarlo.

Para comparar el recorrido, consultar [GUIA_DE_LECTURA.md](GUIA_DE_LECTURA.md). La trazabilidad editorial de fuentes y copias está en [MAPA_EDITORIAL.md](MAPA_EDITORIAL.md).
