# Bitácora razonada de revisión

El material anterior permanece intacto. Esta edición incorpora correcciones en el texto y en los cálculos, no solo una lista final de advertencias.

| Problema anterior | Transformación aplicada | Aprendizaje incorporado | Dónde se comprueba |
|---|---|---|---|
| Potencia media y balance de energía llamados reserva | Magnitudes separadas; calendario correcto; sin indicador falso de reserva | Elegir variable antes de interpretar | S1/S4; caso 00; `datos.py` |
| Años parciales mezclados con completos | Cobertura diaria explícita y corte 2024 | Comparabilidad temporal | Caso 00 y pruebas |
| Máximo producido llamado capacidad instalada | Renombrado y categoría sin clasificar conservada | Proxy y censo no son equivalentes | S3; caso 01/03 |
| Curtosis/lag como demostración causal | Exceso de curtosis; hipótesis rivales; ajuste de demanda con prueba temporal | Diferenciar asociación, ajuste e identificación | S1/S4; caso 00/04 |
| Grafo sintético como STN validado | Red A–E ficticia con comparación DC | Topología no certifica seguridad | S2; caso 02 |
| N-1 cuenta todos por `or True` | Contingencias independientes por línea y balance verificable | Definir falla y métrica | `modelos.py`; tests |
| Cascada, nodos y mejora 3x prefijados | Eliminadas afirmaciones no calculadas | Resultado antes que narrativa | S2; caso 02 |
| Ciclos de precio prefijados | Modelo genérico explícito de ajuste; sin precio colombiano ficticio | Explorar condiciones de comportamiento | S4 |
| Falta de agua y Niño inactivo | Balance mensual de almacén; factor de aportes activo y probado | Mecanismo físico y agregación temporal | S4; caso 04 |
| Factor de planta llamado firmeza | Variables separadas; ENFICC/OEF no inventadas | Potencia, energía y obligaciones | S4/S5 |
| Monedas incompatibles en CxC/LCOE | Ejercicio dimensional separado; caja real COP explícita | Moneda, período y obligación | S5; caso 05 |
| Diversificada ganadora prefijada | Ranking desde resultados y admisibilidad separada | Robustez condicionada | S5; caso 05 |
| Comparación sin costo de activos | CAPEX/OPEX, no construir y PPA definido | Visión de negocio | S5; caso 05 |
| Centralidad interpretada como poder y Bass sintético como real | Universo y relación documentados; recuperación sintética rotulada | No convertir un mecanismo supuesto en hallazgo empírico | S3; caso 03 |
| Gobernanza con scores arbitrarios | Condiciones, evidencias y responsables; estados pendientes | Justicia cambia alternativas | S6; caso 06 |
| Síntesis reinicia trabajo | Estado JSON acumulativo con esquema y exportación real | Trazabilidad de la recomendación | Caso 00–07; tests |
| Libro incompleto y copias ambiguas | 8 lecturas, 8 prácticas, 8 integrados; compilación independiente | Fuente editable y publicación derivada | `construir.py`, TOC |

## Qué no se afirma haber resuelto

No se obtuvo un caso AC del SIN ni una reconstrucción auditada de toda su capacidad por recurso. No se calibró despacho nacional, ENFICC, precios futuros o rentabilidad de una planta real. El material enseña con historia observada, un componente empírico de demanda y modelos ilustrativos transparentes. Las brechas se convierten en parte del encargo y la evaluación, con solicitud de información y criterios de profundización.

## Finalización tras recuperar la sesión

Se recuperaron los borradores en las dos carpetas nuevas del repositorio. Se ampliaron los fundamentos de S1–S5 para conservar el desarrollo conceptual junto con las correcciones: complejidad y lazos; generadores y métricas de redes; difusión y reglas de actualización; ecuaciones y equilibrio dinámico; sensibilidad y decisión adaptativa. Las prácticas S2–S5 incorporan experimentos ejecutables adicionales con controles y preguntas abiertas.

Se añadió la matriz de alineación curricular, haciendo visible la frontera de la calibración empírica disponible. El ensamblador usa la correspondencia lectura–práctica del manifiesto y rechaza desajustes. Se corrigió la referencia sobre participación solar en CxC para apuntar al comunicado específico de asignaciones de XM. Los informes de verificación registran las ejecuciones realizadas y el control de entrega conserva hashes de los datos y de las fuentes.

## Versiones y mantenimiento

La fuente del paquete es `Libro SA-MISE/sa_mise`. La copia del caso se genera y verifica; no se mantienen implementaciones independientes. Las lecturas y prácticas son fuentes; los cuadernos integrados son derivados. Los guiones y PAyC originales no se editaron: esta edición define el contenido al cual deberán alinearse cuando se actualice esa producción.


## Edición didáctica del 15 de septiembre de 2026

Se recupera el recorrido original de tres capas y las dos miradas: lo que oculta una simplificación y lo que agrega una interacción, ponderado frente al análisis especializado. Se añade preludio científico con prácticas; las lecturas recuperan situaciones y razonamiento acompañado; las prácticas añaden cálculos pequeños, predicciones y discusión. El caso vuelve a decisiones del SIN y conserva caja solar como ventana empresarial.

Se conserva el rigor de unidades, cobertura, balances, persistencia y validación delimitada. Se añaden contraste de perfiles horarios, asociación con controles aditivos, aportes de igual total y diferente secuencia, estrés combinado, costo parcial de respuestas y efecto de entrada tardía. No se afirma calibración de operación/expansión nacional. Los originales se mantienen intactos; la edición anterior revisada queda respaldada fuera de las fuentes activas.
