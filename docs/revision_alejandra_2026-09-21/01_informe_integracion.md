# Integración de las guías de Alejandra en SA-MISE

**Balance editorial y propuesta de intervención mínima · 21 de septiembre de 2026**

## Recomendación

Conservar el curso publicado y reconocer las guías de Alejandra como una **ruta de acompañamiento vinculada a las actividades existentes**. Seleccionar explicaciones, ejercicios resueltos y pautas de revisión; mantener una sola secuencia de evaluación, un solo conjunto de notebooks oficiales y una sola Saga Colombia.

El mayor aporte no es completar un temario ausente. Es ayudar al estudiante a pasar de entender un concepto a usarlo con criterio: formular un mapa causal, comprobar un modelo, justificar sus parámetros, interpretar sus límites y defender una recomendación.

La revisión de las 56 unidades encontró **29 con núcleo ya cubierto y 27 con desarrollo específico parcialmente cubierto**. No son porcentajes de aprendizaje ni medidas de calidad. Todas tienen un antecedente temático; varias incluyen subtemas que no localicé desarrollados en nuestra versión. La [matriz completa](02_matriz_56_guias.md) separa ambos niveles y documenta cada correspondencia.

## 1. Alcance y método

Se compararon **34 páginas del curso vigente** —introducción, contexto, preludio y semanas 1–8, incluyendo lecturas, guías y notebooks publicados— con **63 páginas de Alejandra**: portada, seis índices semanales y 56 unidades. Fuentes: [curso SA-MISE](https://milogz.github.io/Systems_Analytics_MISE/intro.html) y [guías de Alejandra](https://pozost.github.io/Systems-Analytics-Guias/).

La unidad de comparación fue el contenido y la actividad, no el título. Se contrastaron explicaciones, ejemplos, ejercicios, instrucciones de evaluación, código visible y resultados publicados. Se buscó también en práctica y Saga para evitar declarar ausente algo que sí aparece fuera de la lectura. Se conservó un inventario con URL y huella de los archivos consultados en [fuentes_consultadas.json](fuentes_consultadas.json).

No se usaron como base las versiones alternativas de `_reference/Libro_SA_MISE` o `_reference/Caso_Consultoria_SA_MISE`. La estructura local se inspeccionó únicamente para proponer dónde editar después. La referencia sustantiva es el HTML público consultado, que puede cambiar tras esta fecha.

**Límites concretos:** se revisaron los contenidos y las salidas publicadas, pero no se ejecutaron todas las combinaciones de los simuladores ni se reprodujeron los laboratorios. Las guías mencionan notas en PDF y fichas entregadas en sesión; no se localizaron enlaces descargables a esos materiales dentro del corpus recorrido. Tampoco se verificó independientemente cada cifra histórica, disposición normativa o noticia citada. Los hallazgos sobre cobertura son firmes respecto de las páginas revisadas; los resultados numéricos y afirmaciones coyunturales siguen siendo afirmaciones de sus respectivas fuentes.

## 2. Qué ya estaba cubierto

| Bloque | Cobertura vigente | Qué aporta principalmente Alejandra |
|---|---|---|
| Complejidad | Adaptación, emergencia, no linealidad, trayectoria, extremos, lazos y CLD. [Lectura S1](https://milogz.github.io/Systems_Analytics_MISE/semana_01/lectura.html); [Práctica S1](https://milogz.github.io/Systems_Analytics_MISE/semana_01/notebook.html). | Más procedimientos y ejercicios para reconocer mecanismos y revisar el mapa. |
| Redes | Métricas, ER/BA/WS, colas, robustez, N-1 y cascadas. [Lectura S2](https://milogz.github.io/Systems_Analytics_MISE/semana_02/lectura.html); [Saga S2](https://milogz.github.io/Systems_Analytics_MISE/semana_02/caso_colombia.html). | Precauciones de interpretación, comparación entre modelos y técnicas adicionales. |
| Difusión y actores | Bass, umbrales, contagio, comunidades, bipartitas y adopción solar. [Lectura S3](https://milogz.github.io/Systems_Analytics_MISE/semana_03/lectura.html); [Saga S3](https://milogz.github.io/Systems_Analytics_MISE/semana_03/caso_colombia.html). | Presupuesto comparable, consecuencias distributivas, trazabilidad de relaciones y límites de agregación. |
| Dinámica de sistemas | Bañera, stocks/flujos, ecuaciones, retardos, ciclo de inversión, parametrización y comparación histórica. [Lectura S4](https://milogz.github.io/Systems_Analytics_MISE/semana_04/lectura.html); [Saga S4](https://milogz.github.io/Systems_Analytics_MISE/semana_04/caso_colombia.html). | Comprobaciones organizadas, convergencia numérica e identificabilidad de parámetros. |
| Políticas e incertidumbre | Meadows, CxC/FNCER, sensibilidad, escenarios, robustez, minimax regret y referencias a XLRM/RDM. [Lectura S5](https://milogz.github.io/Systems_Analytics_MISE/semana_05/lectura.html); [Saga S5](https://milogz.github.io/Systems_Analytics_MISE/semana_05/caso_colombia.html). | Interacciones, vulnerabilidad de estrategias y señales concretas de adaptación. |
| Gobernanza | Cuatro capas, Ostrom, justicia distributiva/procedimental/reconocimiento, consulta, licencia social y Windpeshi. [Lectura S6](https://milogz.github.io/Systems_Analytics_MISE/semana_06/lectura.html); [Saga S6](https://milogz.github.io/Systems_Analytics_MISE/semana_06/caso_colombia.html). | Matrices resueltas y conexión más explícita entre evidencia, relaciones e instituciones. |
| Comunicación | Pirámide, cadena de evidencia, memo, recomendaciones condicionadas y revisión por pares. [Lectura S7](https://milogz.github.io/Systems_Analytics_MISE/semana_07/lectura.html). | Ejercicios de adaptación por audiencia y revisión de gráficos; corresponde a nuestra S7. |

La enseñanza por niveles y las actividades computacionales tampoco son nuevas para nuestro material: la práctica ya distingue intuición, energía y aplicación profesional. La diferencia de las guías está en la regularidad del acompañamiento: pregunta inicial, explicación gradual, predicción, simulación, explicación del resultado y autoevaluación. Conviene atribuir ese aporte pedagógico con precisión, sin presentar los temas compartidos como incorporaciones nuevas.

Nuestro preludio, el contexto transversal, TASCOI/CATWOE, los arquetipos de SD, la continuidad de la Saga y el taller de integración/cierre siguen cumpliendo funciones propias. Las seis semanas de guías no reemplazan por sí solas la arquitectura completa de ocho semanas del curso.

## 3. Qué falta o está menos desarrollado, y qué vale incorporar

### Prioridad alta: mejorar el uso de herramientas que ya enseñamos

**Revisión sistemática del CLD.** Ya hay lazos y mapas; falta hacer tan visible el procedimiento de construcción y autocorrección. Seleccionar la pauta de [1.10 · El mapa causal de la crisis](https://pozost.github.io/Systems-Analytics-Guias/semana1/10-mapa-causal.html) para revisar el trabajo existente. No trasladar automáticamente sus cantidades mínimas de lazos o anotaciones a nuestra rúbrica.

**Interpretación de redes y decisiones de difusión.** La práctica puede ganar en claridad al explicitar qué mide la robustez topológica y qué no prueba sobre operación eléctrica, y al exigir procedencia de los vínculos de actores. En difusión, la comparación de políticas a igual presupuesto y por grupos sociales conecta S3 con S6. Fuentes: [2.08 · Robustez y criterio N-1](https://pozost.github.io/Systems-Analytics-Guias/semana2/08-robustez-n1.html), [3.05 · Intervenir la difusión: semillas, subsidios y puntos de inflexión](https://pozost.github.io/Systems-Analytics-Guias/semana3/05-intervenir-difusion.html), [3.06 · Redes de actores y comunidades: quién se mueve con quién](https://pozost.github.io/Systems-Analytics-Guias/semana3/06-redes-actores.html).

**Validación, calibración e identificabilidad.** No falta la palabra «validación»: nuestra [Saga S4](https://milogz.github.io/Systems_Analytics_MISE/semana_04/caso_colombia.html#validacion-con-datos-historicos) ya compara trayectorias y la [Lectura S5](https://milogz.github.io/Systems_Analytics_MISE/semana_05/lectura.html#analisis-de-sensibilidad) incluye condiciones extremas. Falta una secuencia igualmente explícita de comprobaciones, origen de parámetros y límites del ajuste. [4.03 · La ecuación del stock y la integración numérica: la contabilidad paso a paso](https://pozost.github.io/Systems-Analytics-Guias/semana4/03-formalismo-integracion.html), [4.07 · Consistencia dimensional y validación: someter el modelo a pruebas para romperlo](https://pozost.github.io/Systems-Analytics-Guias/semana4/07-consistencia-validacion.html) y [4.08 · Calibración: afinar el modelo clavija por clavija](https://pozost.github.io/Systems-Analytics-Guias/semana4/08-calibracion.html) ofrecen el complemento más importante para el rigor del proyecto.

**Sensibilidad y adaptación con evidencia.** El tornado y minimax regret ya existen. Conviene reforzar que el parámetro importante depende de la métrica y del rango, explorar una interacción sencilla y terminar con una señal observable que haría revisar la recomendación. Usar [5.05 · Análisis de sensibilidad](https://pozost.github.io/Systems-Analytics-Guias/semana5/05-sensibilidad.html) y [5.09 · Introducción a la toma de decisiones robusta (RDM)](https://pozost.github.io/Systems-Analytics-Guias/semana5/09-rdm.html); no convertir PRIM ni miles de futuros en un nuevo requisito.

**Gobernanza que se pueda documentar.** La novedad útil no son Ostrom o las tres justicias, ya incluidos. Es sistematizar el diagnóstico: observación, fuente, hipótesis pendiente y consecuencia para la decisión. [6.04 · Justicia energética](https://pozost.github.io/Systems-Analytics-Guias/semana6/04-justicia-energetica.html) y [6.06 · Redes de actores con poder e intereses](https://pozost.github.io/Systems-Analytics-Guias/semana6/06-redes-actores.html) fortalecen nuestra actividad existente.

### Segunda prioridad: subtemas nuevos que conviene dejar seleccionables

No localicé un desarrollo equivalente de Cynefin e iceberg (1.01–1.02), Jensen (1.04), urna de Pólya (1.05), Braess (1.06), factor de coincidencia/falacia de composición (1.07), histéresis formal (1.09), articulaciones y cortes (2.03), centralidad de autovector (2.04), estimación de colas mediante CCDF/umbral (2.07), exposición por contraparte (3.07), parámetro aparente de Bass condicionado por la red (3.08), funciones de tabla (4.04) y comparación de órdenes de retardo (4.06). Sus enlaces y antecedentes están en la matriz.

Son aportes reales, pero no todos justifican tiempo obligatorio. Priorizaría **articulaciones/cortes, límites del ajuste de Bass y contraste entre formas de retardo** si más adelante hay espacio. Cynefin, Braess, formalismo de colas y los otros ejemplos pueden permanecer en un banco optativo. Incorporar todo ahora contradiría la decisión docente de mantener la versión manejable.

## 4. Diferencias que deben armonizarse antes de enlazar como lectura obligatoria

Estas observaciones son sobre la compatibilidad de los dos materiales. No pretenden atribuir errores exclusivamente a uno de ellos.

| Punto | Evidencia y problema | Resolución mínima propuesta |
|---|---|---|
| Red y diagnóstico topológico | Nuestra [Lectura S2](https://milogz.github.io/Systems_Analytics_MISE/semana_02/lectura.html#topologias-de-red-que-forma-tiene-nuestro-sistema) asocia el SIN con una red libre de escala. [2.06 · Modelos de red](https://pozost.github.io/Systems-Analytics-Guias/semana2/06-modelos-de-red.html) encuentra cola exponencial en su STN estilizado. Nuestra [Saga S2](https://milogz.github.io/Systems_Analytics_MISE/semana_02/caso_colombia.html#el-stn-como-grafo) muestra 45 nodos/52 enlaces; la guía trabaja con 100/131. | Aclarar que son grafos distintos y que tener hubs no demuestra una ley de potencia. No usar una simulación sintética para clasificar el SIN real. El contraste exige datos y método comunes. |
| Alcance del test N-1 | Ya explicamos limitaciones eléctricas, pero la Saga usa el nombre «Test N-1» para un análisis del grafo. [2.08 · Robustez y criterio N-1](https://pozost.github.io/Systems-Analytics-Guias/semana2/08-robustez-n1.html) insiste en la distinción. | Añadir junto al resultado: «Prueba topológica de contingencia simple; no certifica cumplimiento eléctrico N-1». Conservar el ejercicio. |
| Datos, ajuste y validación | En [Saga S4](https://milogz.github.io/Systems_Analytics_MISE/semana_04/caso_colombia.html#validacion-con-datos-historicos) conviven una nota de datos sintéticos y rótulos de precio real/XM. El preludio también incorpora datos para parametrizar. No hay que suponer que todas las series tienen igual procedencia. | Identificar, serie por serie, dato observado, aproximación y simulación. Reservar «validación empírica» para una comparación justificable; de otro modo, llamarla contraste de comportamiento. La guía 4.08 ayuda a corregirlo. |
| Oscilación no automática | Nuestra S4 usa formulaciones de inevitabilidad; [5.03 · Balance más retardo: oscilación](https://pozost.github.io/Systems-Analytics-Guias/semana5/03-balance-retardo-oscilacion.html) propone fórmulas/umbrales ilustrativos de retardo y ajuste. | Escribir que la oscilación depende de estructura, ganancia, forma del retardo y parámetros. No aplicar umbrales de un modelo a otro. |
| CxC, estrategias y resultados | Ambos materiales simplifican la política, pero no con las mismas ecuaciones; [5.04 · Políticas y puntos de apalancamiento](https://pozost.github.io/Systems-Analytics-Guias/semana5/04-politicas-apalancamiento.html) distingue prima fija y regla de subasta. Las tablas de [Saga S5](https://milogz.github.io/Systems_Analytics_MISE/semana_05/caso_colombia.html) y [5.10 · El modelo con Cargo por Confiabilidad y FNCER](https://pozost.github.io/Systems-Analytics-Guias/semana5/10-modelo-politicas.html) no comparten necesariamente estrategias, métricas ni supuestos. | Rotular cada representación como estilizada. Pedir interpretación condicional; no importar el «ganador» ni afirmar que la simulación demuestra el efecto histórico del CxC. |
| Variables sociales | Nuestra [Lectura S6](https://milogz.github.io/Systems_Analytics_MISE/semana_06/lectura.html) pide evitar índices sociales inventados. [6.02 · El proyecto como sistema socio-técnico-ambiental](https://pozost.github.io/Systems-Analytics-Guias/semana6/02-sistema-sociotecnico.html) representa confianza/agravio y retrasos endógenos. | Mantener esos modelos como explicaciones hipotéticas. Para el proyecto, usar evidencia cualitativa y escenarios de retraso; cuantificar solo si se justifican medición y estructura. |
| Redes y tipos de variables | Nuestra [Lectura S3](https://milogz.github.io/Systems_Analytics_MISE/semana_03/lectura.html#cierre-del-modulo-de-redes-que-aprendimos-y-que-falta) separa redes y cantidades continuas de manera muy tajante. La «fotografía» de S4 puede confundir auxiliares medibles en un instante con stocks. | Precisar que red/SD responde a distintas preguntas y niveles de agregación; un estado en red puede ser continuo. Identificar stocks por acumulación y balance, además de la heurística de la foto. |
| Calendario y evaluación | Las guías remiten a Laboratorios 1–4 y contienen exigencias particulares de avances; comunicación aparece en su S6. Nuestro [Lectura S7](https://milogz.github.io/Systems_Analytics_MISE/semana_07/lectura.html) admite memo de 1–2 páginas y las guías semanales fijan actividades/entregables. | Mantener instrucciones oficiales actuales. Enlaces con sección y propósito, no «haga todo lo que pide esta página». Comunicación de Alejandra se ubica en nuestra S7. |
| Fechas y ejemplos | Hay series de nuestro curso con corte 2024 y referencias de las guías a 2025–2026; hay redes y volúmenes explícitamente inventados. | Declarar corte temporal y naturaleza del dato; actualizar una ficha compartida solo cuando se haya comprobado su fuente. No mezclar automáticamente series o cifras. |
| Motores computacionales | El curso usa `mise_utils` y la Saga guarda estado; las guías citan `mise_sd` y simuladores de navegador. La propia guía 3.08 advierte diferencias entre realizaciones de redes. | Enlazar como apoyo conceptual. Mantener el código vigente como actividad oficial; ninguna nueva instalación ni promesa de equivalencia numérica. |

Además, conviene evitar importar como reglas universales algunas simplificaciones de las guías: que toda exponencial real desemboca necesariamente en una S (5.01), que variar una sola incertidumbre nunca cambia el orden de estrategias (5.07), o que cumplir una lista institucional garantiza éxito (6.03). Pueden servir como intuiciones situadas, con condiciones explícitas. Es una razón adicional para seleccionar secciones y no declarar todas las guías obligatorias de una vez.

## 5. Paquete concreto de integración mínima

Propongo **siete bloques de acompañamiento**, uno en cada guía de S1–S7. Cada bloque diría qué sección consultar, para qué sirve y qué parte de la actividad vigente ayuda a resolver. Las páginas completas seguirían siendo opcionales. Los tiempos siguientes son presupuestos editoriales propuestos para fragmentos seleccionados, no tiempos medidos ni la suma de páginas completas.

| Paquete y destino | Sección de Alejandra a seleccionar | Uso en la actividad vigente | Tiempo y sustitución |
|---|---|---|---|
| **P1 · S1, mapa causal** | 1.10: procedimiento y errores frecuentes. | Revisar dirección/signo, retardos y mecanismo del CLD que ya se pide. | 15 min dentro de preparación del mapa. |
| **P2 · S2, interpretación del grafo** | 2.08: errores y resumen de alcance de robustez/N-1. | Explicar qué significa el resultado topológico y qué comprobación eléctrica falta. | 10 min de la lectura de resultados. |
| **P3 · S3, difusión y actores** | 3.05: contraste distributivo; 3.06: errores de interpretación de vínculos/comunidades. | Reformular una respuesta de política y documentar un vínculo del mapa actual. | 20 min de interpretación; sin nuevas corridas obligatorias. |
| **P4 · S4, comprobar antes de concluir** | 4.07: pruebas; 4.08: procedencia e identificabilidad; 4.03: convergencia. | Revisar el modelo con la ficha propuesta abajo. | 30 min del trabajo de revisión/calibración ya previsto. |
| **P5 · S5, sensibilidad y decisión** | 5.05: métrica/rangos/interacción; 5.09: plan adaptativo. | Dar una condición de fallo y una señal de revisión a la recomendación actual. | 25 min del análisis del Avance 2; no sumar otra entrega. |
| **P6 · S6, evidencia institucional** | 6.04: matriz; 6.06: evidencia y límites de la red. | Completar el diagnóstico de justicia y actores que alimenta el juego de roles. | 20 min de preparación existente. |
| **P7 · S7, comunicación** | 6.07: versiones por audiencia y errores gráficos. | Revisar el memo y una figura del informe actual. | 15 min del taller de redacción. |

El paquete suma **135 minutos repartidos en siete semanas**, absorbidos por tareas existentes mediante sustitución de lectura/revisión. Si el equipo solo dispone de capacidad para tres bloques, empezaría por **P4, P5 y P6** (75 minutos repartidos), y dejaría los demás optativos durante esta cohorte.

**Ficha P4 propuesta — una tabla dentro del trabajo actual:** variable o parámetro; unidad; procedencia (medición/estimación/ajuste/supuesto); rango; prueba aplicada; resultado; limitación. Las pruebas cubrirían balance/unidades, un extremo, sensibilidad numérica y contraste de comportamiento. Con `solve_ivp`, la sensibilidad numérica se comprueba ajustando tolerancias o paso máximo y contrastando una métrica; reducir solo los tiempos solicitados para graficar no equivale a controlar el paso interno. La ficha comienza como ayuda de revisión, sin cambiar pesos de calificación.

**Pregunta P5 propuesta:** «¿Con qué cambio plausible de supuestos dejaría de recomendar esta estrategia, y qué indicador verificable le avisaría a tiempo?». La respuesta se incorpora a la recomendación que ya se entrega. No se exige adoptar los escenarios ni las estrategias de las guías.

**Matriz P6 propuesta:** dimensión de justicia o vínculo institucional; observación; fuente; hipótesis pendiente; consecuencia para la decisión. Una casilla sin evidencia se marca como hipótesis por verificar, no se rellena con una puntuación inventada.

### Por qué no añadir las 56 páginas como lectura obligatoria

Los tiempos publicados en los índices de Alejandra suman:

| Semana de las guías | Unidades | Minutos publicados | Equivalente |
|---|---:|---:|---:|
| [Semana 1](https://pozost.github.io/Systems-Analytics-Guias/semana1/index.html) | 10 | 620 | 10 h 20 min |
| [Semana 2](https://pozost.github.io/Systems-Analytics-Guias/semana2/index.html) | 10 | 645 | 10 h 45 min |
| [Semana 3](https://pozost.github.io/Systems-Analytics-Guias/semana3/index.html) | 9 | 655 | 10 h 55 min |
| [Semana 4](https://pozost.github.io/Systems-Analytics-Guias/semana4/index.html) | 9 | 595 | 9 h 55 min |
| [Semana 5](https://pozost.github.io/Systems-Analytics-Guias/semana5/index.html) | 10 | 625 | 10 h 25 min |
| [Semana 6](https://pozost.github.io/Systems-Analytics-Guias/semana6/index.html) | 8 | 465 | 7 h 45 min |

**Total: 3605 minutos, es decir, 60 h 05 min.** Es la suma de las tablas, no una medición independiente del tiempo del estudiante; puede contener actividades equivalentes a las actuales. Precisamente por ese solapamiento, sumarla como trabajo adicional duplicaría gran parte del curso. Por ejemplo, nuestra [guía S5](https://milogz.github.io/Systems_Analytics_MISE/semana_05/guia.html#distribucion-del-tiempo) ya distribuye 12 horas entre lectura, actividades, proyecto y sesión.

## 6. Cómo incorporarlo sin crear dos cursos paralelos

**Primera intervención, solo editorial.** Añadir una referencia transversal a las guías en la introducción y un bloque P1–P7 en `coursebook/semana_XX/guia.md`. Los bloques incluyen autoría, enlace, sección, propósito y carácter de apoyo. La matriz completa queda como documento docente, no como otra ruta obligatoria para el estudiante. No hace falta tocar el índice general, cambiar el orden de capítulos o integrar JavaScript externo.

**Ajustes puntuales después de la conversación docente.** Corregir los rótulos o frases de compatibilidad identificados en §4 y, si el equipo adopta las fichas, añadirlas a las actividades existentes. Las lecturas se editan en `marco_teorico/`; la práctica y Saga, en `notebooks/`. `build_book.py` genera las copias de lectura y notebooks en `coursebook/`, por lo que no conviene editar solo esas copias. Esto evita que el siguiente ensamblado borre las mejoras.

**Autoría visible.** Texto propuesto: «Acompañamiento de Alejandra, co-líder del curso: [título y enlace]. Sección sugerida: [nombre]. Úsela para [propósito] en la actividad de esta semana». Si posteriormente se adapta un ejercicio dentro de nuestros archivos, atribuir la adaptación en ese lugar, conservar la referencia a su fuente y acordar con ella la versión. En la primera intervención basta con enlaces; así su material conserva identidad, actualización y reconocimiento.

**Una sola instrucción evaluable.** En el bloque general indicar: «Las guías amplían y acompañan el curso. Para entregas, extensión y evaluación, siga la guía semanal de SA-MISE». Esto resuelve referencias a otros laboratorios o requisitos sin desvalorizar el recurso.

**Comprobación antes de publicar.** Verificar los enlaces y secciones elegidas, probar los simuladores que se recomienden efectivamente, cotejar datos/etiquetas que acompañen esos ejemplos y reconstruir el libro. El trabajo realizado aquí es la revisión y la propuesta; no constituye esa prueba de ejecución ni una publicación.

## 7. Balance para la conversación con Alejandra

El reconocimiento propuesto tiene tres formas: **usar explícitamente sus pautas en siete momentos del curso**, **ofrecer sus guías como explicación alternativa de los temas compartidos** y **preservar sus desarrollos más avanzados como profundización**. «Ya cubierto» significa que no hace falta repetir el tema, no que su trabajo carezca de valor.

La conversación puede concentrarse en tres decisiones concretas: cuáles de P1–P7 activar en esta cohorte; qué formulación común adoptar para redes, validación y modelos de política; y cómo quiere que aparezca la atribución. Hay un [balance breve listo para compartir](03_balance_para_alejandra.md), redactado como propuesta, sin dar por acordada la integración.

## Documentos y trazabilidad

- [Matriz completa: 56 guías, evidencia y destino](02_matriz_56_guias.md).
- [Balance breve para Alejandra](03_balance_para_alejandra.md).
- [Inventario de fuentes y huellas](fuentes_consultadas.json).
- [Matriz estructurada](matriz_56_guias.json).

Solo se añadieron documentos de revisión. No se modificaron lecturas, notebooks, guías semanales, evaluación ni el sitio publicado.
