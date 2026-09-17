# Semana 8 — Horizontes Futuros y Cierre: El Primer Piso, No el Techo

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

---

## 1. El Arco del Curso en Retrospectiva

Llegamos a la cumbre de este trayecto formativo. En la Semana 1 partimos de una pregunta provocadora e incómoda: *¿Por qué el análisis convencional de ingeniería y economía falla sistemáticamente al predecir y gestionar las crisis del sector energético?* 

Exploramos respuestas a lo largo de las semanas siguientes descubriendo cinco axiomas fundamentales, los **"Cinco Importa"**:
1. **Importa la Complejidad:** Comprendimos que el SIN no es una máquina predecible (complicada), sino un sistema vivo que exhibe no linealidad, adaptación, retroalimentaciones y dependencia del camino (Path Dependence).
2. **Importa la Estructura (Redes):** Visualizamos cómo la arquitectura topológica condiciona los flujos. Una falla menor, dependiendo de su posición en la red (centralidad, intermediación), puede desencadenar cascadas catastróficas.
3. **Importa el Tiempo (Dinámica de Sistemas):** Destruimos la ilusión del equilibrio estático. Aprendimos que los retrasos en la toma de decisiones y en la construcción de infraestructura (stocks y flujos) son los motores que generan los ciclos perversos de escasez y sobreoferta.
4. **Importa la Incertidumbre (Escenarios):** Reconocimos la arrogancia de la predicción determinista de largo plazo. El futuro no se predice; se exploran los espacios de vulnerabilidad a través de escenarios múltiples y se diseñan políticas robustas.
5. **Importa lo Humano (Gobernanza):** Finalmente, en las Semanas 6 y 7, aceptamos que los modelos matemáticos colapsan si ignoran el territorio. La viabilidad técnica no sobrevive sin la justicia procedimental y la gobernanza policéntrica.

Al llegar a esta Semana 8, ustedes han completado y defendido un Informe de Consultoría Sistémica (su Proyecto Integrador). Han demostrado capacidad para orquestar estas herramientas frente a un caso real y espinoso del contexto colombiano (la Saga Colombia). 

Sin embargo, el objetivo pedagógico de este cierre es transmitir un mensaje crucial de humildad intelectual: **El toolkit de este curso es el primer piso, no el techo de la disciplina.** Hemos construido los cimientos fundamentales, pero el campo de la analítica de sistemas y la modelación energética contemporánea se extiende mucho más allá. 

En esta lección final, mapearemos las fronteras metodológicas de la disciplina. El propósito es que sepan hacia dónde dirigir sus próximos pasos, dependiendo de los problemas profesionales que enfrenten en sus carreras.

---

## 2. Horizontes de Profundización Metodológica

El análisis de sistemas ha experimentado una revolución computacional en las últimas dos décadas. Las herramientas que utilizamos en clase (NetworkX, formulaciones base de SD en Python) son robustas, pero representan enfoques agregados o estructurales básicos. Cuando los sistemas exhiben heterogeneidad extrema, incertidumbre profunda o comportamientos emergentes a microescala, necesitamos saltar a la siguiente generación de modelos.

### 2.1 Modelado Basado en Agentes (Agent-Based Modeling - ABM)
*Simulando desde abajo hacia arriba (Bottom-Up)*

La Dinámica de Sistemas (SD) es poderosa, pero agrupa a las entidades. Un stock puede representar "Capacidad Térmica Total", asumiendo un comportamiento promedio del sector. Pero, ¿qué ocurre cuando el comportamiento del sistema depende críticamente de las decisiones idiosincráticas, estrategias competitivas y reglas de aprendizaje de actores individuales, heterogéneos y espacialmente distribuidos?

El **Modelado Basado en Agentes (ABM)** responde a esta necesidad. En un ABM, no modelamos ecuaciones macro, sino reglas micro. Programamos "agentes" (un prosumidor solar, una comercializadora de energía, un regulador local). Cada agente tiene atributos, una porción de territorio, una red de vecinos y un conjunto de heurísticas para tomar decisiones (ej. "Instalaré paneles solares si el precio sube por encima de $X$ y si al menos dos de mis vecinos ya los tienen").

El comportamiento agregado del sistema —la adopción masiva, la congestión de la red, el colapso de precios— **emerge** espontáneamente de millones de micro-interacciones.

*   **Casos de uso energético:** Adopción de generación distribuida (techos solares), diseño de mercados mayoristas bajo estrategias de *bidding* (ofertas) oportunistas de generadores, dinámica de adopción de vehículos eléctricos, micro-redes transaccionales comunitarias (P2P).
*   **Herramientas clave:** La librería `Mesa` en Python, o la plataforma NetLogo (desarrollada por Uri Wilensky) para prototipado rápido.
*   **Referencias:** Wilensky & Rand (2015), y los trabajos pioneros de Weidlich & Veit (2008) sobre mercados mayoristas eléctricos modelados con agentes.

### 2.2 Decision Making under Deep Uncertainty (DMDU) y Robust Decision Making (RDM)
*Del "Análisis de Escenarios" al "Muestreo Masivo Computacional"*

En el curso aprendimos a diseñar 4 o 5 escenarios contrastantes (ej. Alta demanda/Baja hidrología vs. Baja demanda/Alta hidrología). Pero, ¿qué pasa cuando la incertidumbre es tan profunda que ni siquiera podemos acordar las probabilidades de los eventos (ej. impacto exacto del cambio climático sobre los aportes hídricos en el año 2040)?

El marco de la Toma de Decisiones bajo Incertidumbre Profunda (DMDU) y su principal metodología, el **Robust Decision Making (RDM)**, invierten el paradigma tradicional (predict-then-act). En lugar de predecir un futuro y optimizar, el RDM utiliza el poder computacional para generar decenas de miles de futuros plausibles combinando todas las incertidumbres imaginables (mediante muestreos como el Hypercubo Latino).

Luego, utilizando algoritmos de descubrimiento de datos (como PRIM - Patient Rule Induction Method), identifica automáticamente en qué zonas o bajo qué condiciones específicas las políticas fallan de manera catastrófica (las vulnerabilidades). El objetivo cambia de "optimizar el valor esperado" a "minimizar el arrepentimiento máximo" (*minimax regret*).

*   **Casos de uso energético:** Planificación de expansión de la transmisión a 30 años; diseño de políticas de transición hacia el hidrógeno verde bajo alta incertidumbre tecnológica.
*   **Herramientas clave:** Framework XLRM de la RAND Corporation; librerías como `Rhodium` o la herramienta Exploratory Modelling and Analysis (EMA) Workbench en Python.
*   **Referencias:** Marchau et al. (2019), y las publicaciones fundamentales de la RAND Corporation.

### 2.3 Machine Learning Avanzado aplicado a Redes y Sistemas Energéticos
*Extrayendo patrones ocultos con Inteligencia Artificial*

Mientras el ABM y el RDM son herramientas deductivas (basadas en reglas), el Machine Learning (ML) y el Deep Learning son herramientas inductivas (basadas en el descubrimiento de patrones empíricos masivos). Constituyen el complemento natural a la analítica de sistemas para mejorar los pronósticos de las variables exógenas y analizar topologías complejas.

La frontera actual es la intersección entre la teoría de redes y el aprendizaje profundo: **Las Redes Neuronales de Grafos (Graph Neural Networks - GNN)**. Una GNN puede "aprender" la física y el comportamiento de la red eléctrica directamente de datos históricos, permitiendo predecir fallas en cascada, identificar zonas de vulnerabilidad o pronosticar la congestión del STN en fracciones de segundo, algo que a un simulador tradicional le tomaría horas.

*   **Casos de uso energético:** Predicción de demanda a muy corto plazo (usando series temporales tipo LSTM o Transformers); mantenimiento predictivo de infraestructura; estimación de estado en redes de distribución activas usando GNN.
*   **Herramientas clave:** `PyTorch Geometric`, ecosistema de Scikit-Learn y TensorFlow.
*   **Referencias:** Hamilton (Graph Representation Learning) y literatura emergente en revistas como *Energy and AI*.

### 2.4 Flujo de Potencia Óptimo y Modelado Físico Realista (OPF)
*De la topología pura a la física AC de potencia*

Nuestra aproximación a las redes con NetworkX fue topológica (nodos y aristas abstractas) o a lo sumo un flujo lineal (DC). Sin embargo, en el mundo real, los electrones siguen las leyes de Kirchhoff, y la red debe manejar potencia reactiva, límites de voltaje y estabilidad transitoria. 

El paso natural para quien desee especializarse en la operación física del mercado es dominar modelos de simulación eléctrica formal.

*   **Casos de uso energético:** Análisis riguroso de congestión de red, evaluación técnica de solicitudes de conexión de nuevas granjas solares, despacho económico detallado.
*   **Herramientas clave:** Librerías especializadas en Python como `pandapower` o `PyPSA` (Python for Power System Analysis).

---

## 3. Metacognición: ¿Cómo Cambió el Pensamiento?

La transformación fundamental que este programa busca instigar no reside en que aprendan la sintaxis de un lenguaje de programación particular. Las herramientas cambian y los lenguajes quedan obsoletos. La transformación reside en la arquitectura mental con la que abordan los problemas.

Un profesional clásico reacciona a los eventos (*events*), trata de prever el comportamiento histórico (patrones), pero a menudo ignora la estructura subyacente. Un analista sistémico, ante el mismo problema, pregunta primero: **¿Cuál es la estructura de incentivos, retardos y topología que está obligando al sistema a comportarse de esta manera reiterada?**

El curso intentó responder, mediante herramientas, a la angustia que produce gestionar infraestructuras críticas en tiempos de crisis climática y volatilidad política. El sector energético colombiano (Saga Colombia) será el escenario de algunas de las decisiones más complejas, costosas e impactantes del país durante los próximos 30 años. Decisiones sobre embalses, interconexiones internacionales, minería crítica para almacenamiento e impuestos al carbono.

Ustedes tienen ahora el marco analítico, el vocabulario formal y las capacidades cuantitativas para elevar la calidad de esos debates, evitando las falsas dicotomías, desmontando las predicciones infundadas y proponiendo intervenciones que, con rigor ético y metodológico, generen resiliencia estructural.

### Actividad de Cierre
En el foro final del curso o en su documento de reflexión individual metacognitiva:
Reflexionen sobre cómo interpretarían hoy, bajo el prisma de estas 8 semanas, la próxima noticia de un "apagón", el retraso de una mega-obra hidráulica o el bloqueo social de un proyecto solar. ¿Qué preguntas harían ahora que no hacían el primer día de clases?

---
*Fin del programa. El sistema está ahora en sus manos.*
