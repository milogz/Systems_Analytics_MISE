# Semana 6 — Gobernanza, Justicia Energética y la Dimensión Humana

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

---

## 1. Apertura: El Límite de los Modelos Cuantitativos

Hasta la semana anterior, hemos construido y calibrado modelos formales que describen el Sistema Interconectado Nacional (SIN) con un alto grado de rigor matemático. Hemos utilizado grafos para entender la topología de la red de transmisión y sus vulnerabilidades frente a fallas en cascada (Complejidad y Redes). Hemos formulado ecuaciones diferenciales, stocks y flujos para capturar las dinámicas de inversión, los retardos de construcción y el comportamiento oscilatorio de los mercados de energía (Dinámica de Sistemas). 

Desde la perspectiva puramente cuantitativa, si un proyecto eólico de 205 MW tiene una Tasa Interna de Retorno (TIR) superior al costo de capital (WACC), si el nodo de conexión en el Sistema de Transmisión Nacional (STN) tiene capacidad de transporte disponible, y si los vientos tienen un factor de planta superior al 45%, el proyecto debería construirse y operar exitosamente. El modelo indica "viabilidad".

Sin embargo, la realidad del desarrollo de infraestructura energética en Colombia demuestra cotidianamente que estas condiciones son necesarias, pero profundamente insuficientes. Los modelos matemáticos que hemos desarrollado hasta ahora sufren de una limitación ontológica fundamental: asumen que el sistema opera en un vacío institucional y social. Asumen que las decisiones se toman por un planificador central o por mercados perfectamente eficientes, ignorando que el territorio donde se emplaza la infraestructura está habitado, tiene historia, derechos adquiridos y sistemas de gobernanza superpuestos.

El caso ancla de esta semana es el **Proyecto Eólico Windpeshi**. Diseñado por Enel Green Power para inyectar 205 MW al SIN desde el municipio de Uribia, en La Guajira, representaba una inversión superior a los 400 millones de dólares. Tenía el recurso eólico, el músculo financiero, la viabilidad técnica y el respaldo de la política nacional de transición energética. Sin embargo, en mayo de 2023, tras años de retrasos, bloqueos y conflictos irresolubles con las comunidades Wayúu del área de influencia, Enel tomó la decisión de suspender indefinidamente el proyecto.

¿Por qué falló Windpeshi? No falló por un error en el cálculo del flujo de potencia, ni por una caída imprevista en el precio de escasez. Falló porque la viabilidad de un proyecto energético en el siglo XXI depende críticamente de la **Licencia Social para Operar (LSO)** y de una gobernanza territorial efectiva. 

Esta semana transitamos hacia el cuarto "importa" de nuestro curso: **importa lo humano**. Aprenderemos a integrar la dimensión social, ambiental y de gobernanza a nuestro análisis sistémico, reconociendo que los conflictos sociales no son "externalidades" o "ruido" en el modelo, sino bucles de retroalimentación estructurales que pueden alterar drásticamente el comportamiento del sistema, llegando incluso a detenerlo.

---

## 2. El Proyecto Energético como Sistema Socio-Técnico-Ambiental

Para analizar casos como Windpeshi sin caer en simplificaciones reduccionistas (como culpar exclusivamente a "la empresa" o a "la comunidad"), necesitamos un marco conceptual que reconozca la pluralidad de actores, intereses y reglas del juego.

### 2.1 El Framework Multi-Capa

La propuesta central de esta semana es que cualquier infraestructura energética debe analizarse simultáneamente a través de cuatro capas acopladas:

1. **Capa Física (Topología y Flujos):** La red eléctrica, los nodos, las líneas de transmisión, las restricciones térmicas y de voltaje. Es el dominio de la física de potencia y la topología de grafos (NetworkX).
2. **Capa de Mercado (Dinámica Económica):** Los precios, los incentivos de inversión, los despachos, el Cargo por Confiabilidad. Es el dominio de la Dinámica de Sistemas (S&F).
3. **Capa de Actores (Red Social):** El ecosistema de organizaciones, instituciones e individuos que interactúan. Aquí encontramos relaciones de poder, contratos, alianzas y conflictos.
4. **Capa de Gobernanza (Reglas e Instituciones):** Las normas formales (leyes, licencias, consultas previas) e informales (usos y costumbres territoriales) que regulan la interacción en la capa de actores.

El error analítico más común en la ingeniería tradicional es optimizar la Capa 1 y la Capa 2, asumiendo que las Capas 3 y 4 se adaptarán automáticamente. El pensamiento sistémico nos obliga a ver las **interdependencias**. Un retraso en la Capa 4 (ej. falta de acuerdo en una consulta previa) altera la Capa 2 (destruye el Valor Presente Neto por el aumento del costo de capital inmovilizado) y pone en riesgo la Capa 1 (el sistema se vuelve más vulnerable a un déficit de energía).

### 2.2 Gobernanza Policéntrica: La Perspectiva de Elinor Ostrom

Cuando hablamos de gobernanza en el sector eléctrico, a menudo pensamos erróneamente en un sistema "monocéntrico" donde el Ministerio de Minas y Energía o la CREG dictan las reglas y el resto obedece. La realidad, especialmente en los territorios donde se despliegan las Fuentes No Convencionales de Energía Renovable (FNCER), es de una **gobernanza policéntrica**.

La Premio Nobel de Economía Elinor Ostrom dedicó su vida a estudiar cómo las sociedades gobiernan los Recursos de Uso Común (Common-Pool Resources - CPR). Si bien el SIN no es exactamente un pastizal o un banco de pesca tradicional, el despliegue territorial de las renovables (el uso del suelo, el impacto visual, las externalidades locales vs. beneficios nacionales) comparte características de problemas de acción colectiva.

Ostrom identificó que los sistemas de gobernanza exitosos y resilientes no dependen del control estatal total ni de la privatización absoluta, sino de múltiples centros de autoridad superpuestos que interactúan bajo reglas claras. Sus **8 Principios de Diseño para Instituciones Sostenibles** son profundamente aplicables al desarrollo de proyectos FNCER en Colombia:

1. **Límites claramente definidos:** ¿Quién tiene derecho a participar y quién no? En Windpeshi, la delimitación del "área de influencia directa" fue una de las principales fuentes de conflicto. Las comunidades exigen límites basados en el uso ancestral del territorio, no en radios kilométricos definidos desde Bogotá.
2. **Coherencia entre reglas y condiciones locales:** Los beneficios y costos deben estar balanceados. ¿Por qué una comunidad local debería aceptar el impacto de un parque eólico si la energía se va al STN y ellos siguen pagando tarifas altas o careciendo del servicio?
3. **Arreglos de elección colectiva:** Los afectados por las reglas deben poder participar en su modificación. La consulta previa (cuando funciona bien) es la materialización de este principio.
4. **Monitoreo:** Quienes auditan las condiciones deben rendir cuentas. (Ej. el papel de la ANLA y las corporaciones autónomas regionales).
5. **Sanciones graduadas:** Las violaciones a los acuerdos deben tener consecuencias proporcionales.
6. **Mecanismos de resolución de conflictos:** Acceso a instancias locales, de bajo costo y rápidas para resolver disputas. El bloqueo de vías en La Guajira es, a menudo, la manifestación de la ausencia de mecanismos formales efectivos de resolución.
7. **Reconocimiento mínimo de derechos de organización:** El Estado (gobierno central) no debe cuestionar el derecho de los usuarios a auto-organizarse.
8. **Empresas anidadas (Gobernanza policéntrica):** Para recursos que son parte de sistemas mayores, la gobernanza debe organizarse en múltiples capas anidadas. Desde el cabildo indígena local, pasando por la alcaldía de Uribia, la gobernación departamental, hasta el Ministerio del Interior y la CREG.

En el análisis sistémico de proyectos, utilizar a Ostrom significa mapear explícitamente cuáles de estos principios están fallando. Cuando fallan los mecanismos de resolución de conflictos (Principio 6), las partes recurren a vías de hecho (bloqueos), lo que introduce un retardo catastrófico en el modelo económico del proyecto.

---

## 3. Justicia Energética: Más Allá del Menor Costo

El diseño regulatorio tradicional del sector eléctrico (Ley 142/143 de 1994) está optimizado para la **eficiencia económica** y la **confiabilidad**. El mandato de la CREG es proveer energía al menor costo posible para el usuario final garantizando que la luz no se apague. 

Sin embargo, la Transición Energética Justa exige incorporar un tercer pilar: la **Justicia Energética**. Basándonos en el marco teórico de Benjamin Sovacool y otros pensadores críticos (Sovacool et al., 2017), la justicia energética no es un concepto etéreo; se puede y se debe operacionalizar en tres dimensiones observables:

### 3.1 Justicia Distributiva
*¿Cómo se reparten los costos, beneficios y riesgos del sistema energético?*

Históricamente, los grandes centros urbanos (Bogotá, Medellín) concentran los beneficios (energía confiable y barata para la industria y los hogares), mientras que las externalidades negativas (inundación de valles, desplazamiento, impacto visual, fragmentación de ecosistemas) recaen desproporcionadamente sobre comunidades rurales, campesinas, afrodescendientes e indígenas.

En el caso de las FNCER en La Guajira, la paradoja distributiva es flagrante: el departamento posee el mejor recurso eólico y solar del país, destinado a descarbonizar el SIN, pero simultáneamente tiene unos de los índices más bajos de cobertura y calidad del servicio eléctrico a nivel local. Un proyecto como Windpeshi es sistémicamente insostenible si la matriz distributiva percibe una extracción neta de valor del territorio.

### 3.2 Justicia Procedimental
*¿Quién participa en la toma de decisiones y con qué nivel de influencia real?*

No basta con que la distribución sea equitativa; el proceso para llegar a ella debe ser justo. La justicia procedimental implica acceso a información oportuna, transparente y comprensible, y la capacidad de influir en el diseño del proyecto, no solo "socializar" una decisión ya tomada en las juntas directivas corporativas.

La asimetría de información es un problema sistémico masivo aquí. Cuando un desarrollador llega con estudios técnicos complejos (flujos AC, estudios de ruido) que la comunidad no tiene la capacidad técnica ni financiera de contra-argumentar, la justicia procedimental se fractura.

### 3.3 Justicia de Reconocimiento
*¿Se reconocen, valoran y respetan las diferentes identidades culturales, valores y formas de relacionarse con el territorio?*

Esta es la dimensión más profunda y, a menudo, la que genera los conflictos más intratables. Para un ingeniero de planeación de la UPME, el territorio es un polígono con coordenadas geográficas, potencial de recurso (W/m2) y restricciones ambientales. Para una comunidad Wayúu, ese mismo territorio está interconectado con sitios sagrados, cementerios ancestrales, rutas de pastoreo y una cosmogonía específica. 

Si el marco institucional del proyecto no reconoce la legitimidad de esta segunda visión del mundo, el conflicto es inevitable. Reconocer no significa necesariamente detener el proyecto, sino incorporarlo en el diseño y en las lógicas de compensación.

---

## 4. La Consulta Previa como Dinámica Sistémica

El mecanismo jurídico institucionalizado en Colombia para tramitar la interacción entre infraestructura e identidades étnicas es el derecho fundamental a la **Consulta Previa**, anclado en el Convenio 169 de la OIT y la Ley 21 de 1991.

Desde la perspectiva jurídica tradicional, la consulta previa suele verse como un trámite, un obstáculo administrativo ("check-the-box") necesario para obtener la licencia ambiental. Desde la Analítica de Sistemas, la consulta previa es un **ciclo de retroalimentación crítica (feedback loop)**.

### Modelando la Consulta Previa

Imaginemos un diagrama causal simple. 
- Aumenta la inversión en el proyecto $\rightarrow$ Aumenta la necesidad de acceso al territorio.
- Si el proceso de Consulta Previa se gestiona bajo el paradigma del "trámite" (baja participación real, desconfianza), Aumenta la percepción de injusticia procedimental.
- A mayor percepción de injusticia $\rightarrow$ Mayor probabilidad de conflictos socio-ambientales y bloqueos.
- Mayor número de bloqueos $\rightarrow$ Aumentan los retardos de construcción (Construction Delays).
- Mayores retardos $\rightarrow$ Aumento de los costos de capital (Cost Overruns) y deterioro del VPN.
- Caída crítica del VPN $\rightarrow$ Decisión de cancelación del proyecto (como en Windpeshi).

**¿Qué nos enseña este modelo?** Que la eficiencia aparente de "acelerar" la consulta reduciendo su calidad participativa genera, paradójicamente, un retardo mucho mayor en el mediano plazo debido al conflicto. Es el arquetipo de "soluciones que fallan" (fixes that fail).

En La Guajira, la atomización de las comunidades (hay cientos de autoridades tradicionales reconocidas) introdujo una complejidad enorme en la capa de red de actores. Identificar *quién* es el representante legítimo para la consulta se convirtió en un cuello de botella institucional que el Estado (Dirección de la Autoridad Nacional de Consulta Previa - DANCP) no tuvo la capacidad de procesar al ritmo que demandaba la urgencia de la transición energética.

---

## 5. El Role-Play: Negociación Multi-Actor

Entender la teoría es el primer paso, pero los sistemas sociales son inherentemente experienciales. Durante la sesión sincrónica de esta semana, ejecutaremos una simulación de rol basada en los conflictos reales de la expansión de las FNCER en el norte de Colombia. 

Cada estudiante asumirá uno de cuatro roles, con incentivos, métricas de éxito y restricciones radicalmente distintas:

1. **El Desarrollador (Empresa de Generación):** Su objetivo es el *Time-to-Market*. Cada mes de retraso le cuesta millones de dólares en capital inmovilizado y pone en riesgo el cumplimiento de sus contratos de largo plazo (PPA) o sus obligaciones de Cargo por Confiabilidad.
2. **El Líder Comunitario (Autoridad Tradicional):** Su objetivo es proteger el tejido social y asegurar la justicia distributiva. Demanda participación accionaria, empleo local y respeto por las rutas ancestrales. Su tiempo no está regido por cronogramas financieros.
3. **El Regulador/Planeador (CREG/UPME):** Su objetivo es la confiabilidad del SIN. Necesita que los megavatios entren a tiempo para evitar un racionamiento a nivel nacional durante el próximo fenómeno de El Niño. Presiona por la celeridad.
4. **La Autoridad Ambiental/Social (ANLA/MinInterior):** Su objetivo es el cumplimiento normativo estricto. Debe velar por la protección de la biodiversidad y el respeto al debido proceso de la consulta previa, sirviendo como garante de derechos en medio de la presión de los otros actores.

El objetivo del role-play no es "llegar a un acuerdo rápido", sino experimentar vivencialmente la **complejidad institucional** y la **inconmensurabilidad de los valores** (lo que no se puede traducir simplemente a dólares). ¿Cómo se negocia cuando el desarrollador habla el lenguaje del VPN y la comunidad habla el lenguaje de la supervivencia cultural?

---

## 6. Conexión con el Proyecto Integrador y la Saga Colombia

Para el informe final de consultoría, no se espera que ustedes "resuelvan" el problema sociopolítico de su caso de estudio con una fórmula mágica. Lo que se exige como analistas sistémicos es **rigor en la integración**:

1. **Evitar la ficción cuantitativa:** No se inventen un "índice social" arbitrario para meterlo en la ecuación del modelo de Dinámica de Sistemas. Si hay una restricción territorial no resuelta, declárenla como una restricción dura (hard constraint) cualitativa que condiciona el escenario.
2. **Trazar los retardos:** Utilicen el modelo de System Dynamics para simular qué le ocurre financieramente al proyecto si la conflictividad genera un retraso de 12, 24 o 36 meses. ¿En qué punto el proyecto cruza el umbral de inviabilidad?
3. **Identificar condiciones de admisibilidad:** Apliquen el marco de justicia de Sovacool y los principios de Ostrom para auditar el proyecto. ¿Falla en la justicia procedimental? Documenten la evidencia.
4. **Recomendaciones sistémicas:** Sus recomendaciones deben abordar las cuatro capas. No basta con sugerir "cambiar el trazado de la línea de transmisión" (Capa 1). Deben especificar los requerimientos en la Capa 3 (qué actores deben coordinarse) y en la Capa 4 (qué reglas de gobernanza deben modificarse).

El caso Windpeshi no es una anomalía; es una ventana al futuro del desarrollo de infraestructura. La transición energética en Colombia (Saga Colombia) será justa y territorialmente anclada, o simplemente no será. La viabilidad técnica y financiera es el boleto de entrada; la gobernanza y la legitimidad social son el permiso de permanencia.

---

### Lecturas Recomendadas (Referencias)

*   **Ostrom, E. (1990).** *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press. (Lectura de Capítulos 1 y 3 para comprender los principios de diseño).
*   **Sovacool, B. K., Burke, M., Baker, L., Kotikalapudi, C. K., & Wlokas, H. (2017).** *New frontiers and conceptual frameworks for energy justice*. Energy Policy, 105, 677-691.
*   **Contraloría General de la República (2022).** *Evaluación a las políticas públicas y la gestión institucional relacionada con el desarrollo de Fuentes No Convencionales de Energía Renovable (FNCER) en el departamento de La Guajira.* Informes sectoriales.
*   **Ministerio del Interior (Colombia).** Marco Normativo y jurisprudencial sobre la Consulta Previa (Convenio 169 de la OIT y Ley 21 de 1991).

---

**Actividad Autónoma de Preparación:**
Antes de la sesión, revisen el expediente resumido del caso Windpeshi y completen su ficha de rol. Identifiquen su "BATNA" (Best Alternative to a Negotiated Agreement) o "MAPAN" en español. ¿Qué pasa con su actor si el proyecto fracasa? ¿Quién asume el costo?
