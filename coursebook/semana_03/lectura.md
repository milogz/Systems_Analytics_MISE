# Semana 3 — Dinámica sobre Redes y Redes de Actores: Más Allá de la Estructura Estática

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

---

## 1. Apertura: de la fotografía a la película

La Semana 2 nos dio un conjunto de herramientas poderoso: aprendimos a traducir infraestructura eléctrica en grafos, a calcular métricas de centralidad, a identificar nodos críticos y a entender la paradoja "robusto pero frágil". Sin embargo, todo ese análisis comparte una limitación fundamental: es **estático**. Tomamos una fotografía del sistema — la topología del STN en un instante — y la analizamos como si estuviera congelada en el tiempo.

Pero los sistemas energéticos no están congelados. Las tecnologías se difunden: un vecino instala paneles solares y su vecina empieza a considerarlo. Los actores forman alianzas: un generador firma contratos con comercializadores, un regulador emite una resolución que reconfigura las relaciones de mercado. La información se propaga: un rumor sobre un subsidio viaja por redes sociales, una falla eléctrica desencadena una cascada de sobrecargas en milisegundos.

Consideremos un dato revelador: la adopción de techos solares en Colombia entre 2017 y 2024 no siguió una trayectoria lineal. Si graficamos las instalaciones acumuladas, vemos una **curva en S** — crecimiento lento inicial, aceleración dramática alrededor de 2020-2021, y un principio de desaceleración cuando el mercado empieza a saturarse en ciertos segmentos. Un modelo puramente económico — basado en el valor presente neto (VPN) de la inversión — predeciría que todos los usuarios para quienes el VPN es positivo adoptarían de inmediato. Pero no es así. La adopción es gradual, desigual geográficamente, y muestra claros patrones de agrupamiento espacial: en ciertos barrios de Medellín o Bogotá hay muchas instalaciones, mientras que barrios económicamente similares apenas tienen una.

¿Por qué? Porque la decisión de adoptar no depende solo de la economía individual, sino de **a cuántos vecinos, amigos o colegas vemos que ya adoptaron**. En otras palabras: la **estructura de la red social** determina *cómo* se difunde una tecnología, no solo *si* se difunde.

Esta semana damos el salto de la fotografía a la película. Aprenderemos a poner los nodos de una red "en movimiento" — a darles estados que cambian en el tiempo según reglas que dependen de sus vecinos. Y extenderemos el análisis de redes más allá de la infraestructura física: las mismas herramientas que usamos para analizar subestaciones y líneas de transmisión nos permiten analizar **actores** — generadores, reguladores, comunidades, inversionistas — y sus relaciones.

---

## 2. Dinámica sobre redes: nodos con estado

### La idea fundamental

En la Semana 2, un nodo era simplemente un punto con propiedades topológicas: tenía grado, betweenness, pertenecía a cierta componente conecta. Pero el nodo no *hacía* nada. No cambiaba.

Ahora le agregamos una dimensión nueva: cada nodo tiene un **estado** (*state*). Por ejemplo:

- En un modelo de adopción tecnológica: el estado puede ser **"adoptó"** o **"no adoptó"** (binario).
- En un modelo de difusión de información: **"informado"** o **"no informado"**.
- En un modelo de falla en cascada: **"operativo"** o **"fallado"**.
- En un modelo más sofisticado: el estado podría ser un número continuo — el nivel de convicción de un actor, la carga de un transformador, el precio en un nodo del mercado.

Lo que hace que la red "cobre vida" es una **regla de actualización** (*update rule*): una función que dice cómo cambia el estado de un nodo en función de los estados de sus **vecinos**. Formalmente, si $s_i(t)$ es el estado del nodo $i$ en el tiempo $t$, y $\mathcal{N}(i)$ es el conjunto de vecinos de $i$, entonces:

$$s_i(t+1) = f\Big(s_i(t), \{s_j(t) : j \in \mathcal{N}(i)\}\Big)$$

Esta ecuación, simple en apariencia, es la puerta de entrada a fenómenos extraordinariamente ricos: difusión de tecnologías, cascadas de fallas, propagación de pánico financiero, formación de consenso social.

### Modos de actualización

Existen dos formas principales de actualizar los estados:

- **Actualización sincrónica**: todos los nodos actualizan su estado simultáneamente, usando los estados del paso anterior. Es como si todos los actores tomaran sus decisiones al mismo tiempo, sin ver las decisiones de los demás en esa ronda.
- **Actualización asincrónica**: los nodos actualizan uno por uno, en un orden (que puede ser aleatorio). Cuando un nodo actualiza, ya "ve" los nuevos estados de los vecinos que actualizaron antes que él.

La elección importa. En muchos modelos de difusión tecnológica, la actualización asincrónica es más realista: las personas no toman decisiones simultáneamente, sino secuencialmente, influidas por lo que ven alrededor.

### Contraste con la Semana 2

| Semana 2: Red estática | Semana 3: Dinámica sobre la red |
|---|---|
| Nodo = punto con propiedades topológicas | Nodo = entidad con estado que cambia |
| Pregunta: ¿cuál es la estructura? | Pregunta: ¿cómo evoluciona el comportamiento? |
| Análisis: métricas, centralidad, vulnerabilidad | Análisis: difusión, cascadas, adopción |
| Tiempo: ausente | Tiempo: variable central |
| Resultado: mapa de vulnerabilidades | Resultado: trayectoria de adopción/falla |

La topología sigue siendo crucial — es el "tablero de juego" sobre el cual se despliega la dinámica — pero ahora el interés está en la **película**, no solo en la fotografía.

---

## 3. Modelos de difusión y contagio

### 3.1 Contagio simple (modelo SI/SIR adaptado)

#### Intuición

Imagine que en un barrio de Medellín, un vecino se entera de un subsidio del gobierno para instalar paneles solares (Ley 1715 de 2014, ampliada por la Ley 2099 de 2021). Cada vez que habla con otro vecino, hay una cierta probabilidad de que le transmita la información. Si el vecino se entera, a su vez empieza a contárselo a sus conocidos. Este proceso es análogo al contagio de un virus: cada contacto con un "infectado" (informado) tiene una probabilidad independiente de transmitir la "infección" (información).

#### Definición formal

En el modelo **SI** (*Susceptible-Infected*), cada nodo está en uno de dos estados:

- **S** (Susceptible): no ha recibido la información / no ha adoptado.
- **I** (Infectado/Informado): ya tiene la información / ya adoptó.

La regla de actualización es:

> En cada paso de tiempo, cada nodo susceptible $i$ tiene una probabilidad $p$ de "contagiarse" por cada vecino infectado $j \in \mathcal{N}(i)$.

La probabilidad de que $i$ permanezca susceptible después de un paso es:

$$P(s_i(t+1) = S \mid s_i(t) = S) = (1-p)^{k_i^I(t)}$$

donde $k_i^I(t)$ es el número de vecinos de $i$ que están en estado I en el tiempo $t$. Entonces la probabilidad de contagio es:

$$P(s_i(t+1) = I \mid s_i(t) = S) = 1 - (1-p)^{k_i^I(t)}$$

Note algo importante: basta **un solo** contacto exitoso para contagiarse. Tener más vecinos infectados simplemente aumenta la probabilidad, pero no hay un umbral mínimo. Esto es lo que define el contagio como "simple".

#### Aplicación energética

Este modelo funciona bien para modelar la **difusión de información** sobre subsidios, regulaciones o nuevas tecnologías a través de redes sociales. En el sector energético colombiano, cuando la CREG emite una resolución que permite la autogeneración a pequeña escala, la noticia no llega simultáneamente a todos los potenciales beneficiarios. Se difunde a través de redes profesionales, gremios (ACOLGÉN, SER Colombia), redes sociales y conversaciones personales.

#### ¿Qué predice?

- La velocidad de difusión depende de la **densidad de la red** y de la presencia de **hubs** (nodos de alto grado). Un hub informado contagia a muchos vecinos rápidamente.
- En redes con distribución de grado tipo ley de potencia (*scale-free*), la difusión es explosiva: no existe un umbral epidémico — incluso con $p$ muy pequeño, la información eventualmente llega a toda la red.
- La difusión es más rápida en redes con bajo coeficiente de agrupamiento (*clustering*): los puentes entre comunidades permiten que la información salte entre grupos distantes.

### 3.2 Contagio complejo (Centola & Macy)

#### Intuición

Enterarse de que existe un subsidio solar es una cosa; decidir invertir 20 millones de pesos en una instalación fotovoltaica es otra muy diferente. Para tomar esa decisión, la mayoría de las personas necesitan más que un solo vecino que les cuente: necesitan ver que **varios** de sus conocidos ya lo hicieron. Necesitan evidencia social múltiple.

Esto se conoce como **contagio complejo** (*complex contagion*), un concepto desarrollado por Damon Centola y Michael Macy. La diferencia fundamental con el contagio simple es:

> En el contagio complejo, un nodo necesita **refuerzo social múltiple** — exposición a múltiples vecinos adoptantes — para cambiar de estado.

#### Definición formal

La regla de actualización cambia radicalmente:

> El nodo $i$ adopta en el paso $t+1$ si y solo si la fracción de sus vecinos que ya adoptaron supera un umbral $\phi_i$:

$$s_i(t+1) = \begin{cases} 1 & \text{si } \frac{k_i^I(t)}{k_i} \geq \phi_i \\ 0 & \text{en caso contrario} \end{cases}$$

donde $k_i$ es el grado total del nodo $i$ y $k_i^I(t)$ es la cantidad de vecinos adoptantes.

#### ¿Por qué esto cambia todo?

El resultado más sorprendente del contagio complejo es que invierte la relación entre topología y difusión:

| Propiedad | Contagio simple | Contagio complejo |
|---|---|---|
| Puentes débiles (entre comunidades) | Aceleran la difusión | No ayudan (un solo contacto no basta) |
| Clustering alto | Retarda la difusión | **Favorece** la difusión |
| Hubs | Aceleran la difusión | Pueden retardarla (necesitan más vecinos) |

En el contagio complejo, el **agrupamiento** (*clustering*) es beneficioso porque crea grupos donde los nodos comparten muchos vecinos. Dentro de un grupo denso, si unos pocos adoptan, la fracción de vecinos adoptantes sube rápidamente para los demás, disparando una cascada local. Esto explica por qué la adopción de tecnologías frecuentemente ocurre en **clústeres geográficos**: los barrios donde varios vecinos instalan paneles solares ven adopción acelerada, mientras que barrios aislados — incluso con la misma economía — se quedan atrás.

#### Aplicación energética

La adopción de techos solares en Colombia muestra claros patrones de contagio complejo:

1. **Clústeres espaciales**: en Medellín, conjuntos residenciales con alta visibilidad de instalaciones solares muestran tasas de adopción significativamente mayores.
2. **Efecto demostración**: no basta con saber que la tecnología existe; los potenciales adoptantes necesitan ver varias instalaciones funcionando, hablar con varios vecinos satisfechos, y percibir que "es lo normal" en su entorno.
3. **Adopción de vehículos eléctricos**: sigue un patrón similar. La infraestructura de carga visible y la presencia de múltiples conocidos con VE reducen la incertidumbre percibida.

### 3.3 Modelos de umbral (Granovetter, Watts)

#### Intuición

Mark Granovetter, en un artículo seminal de 1978, propuso una idea elegante: cada persona tiene un **umbral** personal de adopción — el porcentaje de su entorno que debe haber adoptado antes de que ella adopte. Este umbral varía de persona a persona: los "innovadores" tienen umbral bajo (adoptan aunque nadie a su alrededor lo haya hecho), mientras que los "rezagados" tienen umbral alto (solo adoptan cuando casi todos ya lo hicieron).

#### Definición formal

Cada nodo $i$ tiene un umbral $\theta_i$ extraído de una distribución poblacional $F(\theta)$. El nodo adopta cuando:

$$\frac{|\{j \in \mathcal{N}(i) : s_j = 1\}|}{|\mathcal{N}(i)|} \geq \theta_i$$

La pregunta clave es: **dada una distribución de umbrales $F(\theta)$ y una topología de red, ¿cuándo puede una pequeña semilla de adoptantes iniciales desencadenar una cascada global?**

#### La condición de cascada de Watts

Duncan Watts (2002) formalizó esta pregunta para redes aleatorias. El resultado, expresado intuitivamente:

> Una cascada global es posible si y solo si existe una "masa crítica" de nodos **vulnerables** — nodos con umbral suficientemente bajo como para ser activados por un solo vecino adoptante.

Formalmente, un nodo con grado $k$ y umbral $\theta$ es **vulnerable** si $\theta \leq 1/k$ (basta que uno de sus $k$ vecinos adopte para que él también lo haga). La condición de cascada requiere que estos nodos vulnerables formen un **componente conectado gigante** en la red — es decir, que estén suficientemente interconectados entre sí como para transmitir la cascada de uno a otro.

Este resultado tiene implicaciones profundas para la política energética:

- No basta con que la tecnología sea económicamente viable para "todo el mundo".
- La distribución de umbrales en la población — que depende de factores culturales, de aversión al riesgo, de confianza en la tecnología — es tan importante como la economía.
- La topología de la red — cómo están conectados los potenciales adoptantes — determina si una cascada puede propagarse.

#### Aplicación energética: ¿cuándo "despega" la solar distribuida?

En el contexto colombiano, la condición de cascada de Watts nos dice que:

1. **La semilla importa**: no es lo mismo comenzar la adopción con un usuario aislado que con un grupo de vecinos interconectados.
2. **Las redes profesionales son palancas**: ingenieros que trabajan en el sector y que instalan paneles en sus casas pueden actuar como "nodos semilla" que inician cascadas en sus redes sociales.
3. **Los subsidios deben ser estratégicos**: en lugar de distribuir subsidios uniformemente, la teoría de cascadas sugiere concentrarlos en comunidades donde la densidad de conexiones sociales maximice la probabilidad de cascada.

### 3.4 Modelo de Bass: difusión a nivel agregado

#### Intuición

Frank Bass (1969) propuso un modelo de difusión de innovaciones que captura dos fuerzas:

1. **Influencia externa** (publicidad, política pública, regulación): las personas adoptan porque reciben información de fuentes externas al sistema social.
2. **Influencia interna** (imitación, boca a boca, contagio social): las personas adoptan porque ven que otros lo han hecho.

El modelo de Bass es, en cierto sentido, la versión **agregada** ("de campo medio" o *mean-field*) de los modelos de umbral que acabamos de ver: en lugar de modelar nodo por nodo, modela la fracción total de adoptantes como una cantidad continua.

#### Definición formal

Sea $F(t)$ la fracción acumulada de adoptantes al tiempo $t$. La tasa de adopción es:

$$\frac{dF}{dt} = \big(p + q \cdot F(t)\big) \cdot \big(1 - F(t)\big)$$

donde:

- $p$ = **coeficiente de innovación**: tasa de adopción por influencia externa (publicidad, regulación, incentivos gubernamentales).
- $q$ = **coeficiente de imitación**: tasa de adopción por influencia de otros adoptantes (efecto red, contagio social).
- $(1 - F(t))$ = fracción de no adoptantes restantes (mercado potencial remanente).

La solución analítica produce la característica **curva en S**:

$$F(t) = \frac{1 - e^{-(p+q)t}}{1 + \frac{q}{p} e^{-(p+q)t}}$$

#### Los parámetros cuentan una historia

- Si $p \gg q$: la adopción es impulsada principalmente por factores externos (subsidios, mandatos regulatorios). La curva crece rápido al inicio y luego se satura.
- Si $q \gg p$: la adopción es impulsada por imitación social. La curva tiene un arranque lento (pocos adoptantes iniciales para imitar) seguido de una aceleración explosiva.
- La mayoría de las tecnologías energéticas muestran $q > p$: la imitación domina sobre la publicidad.

#### Aplicación energética: FNCER en Colombia

El modelo de Bass permite estimar los parámetros $p$ y $q$ a partir de datos históricos de adopción. Para la energía solar distribuida en Colombia:

- Los incentivos tributarios de la Ley 1715/2014 y la Ley 2099/2021 operan como el coeficiente $p$.
- La visibilidad de instalaciones, la recomendación boca a boca y la reducción de incertidumbre operan como el coeficiente $q$.
- Un $q$ alto sugiere que la política más efectiva no es un subsidio masivo, sino facilitar las condiciones para que el efecto imitación se active — por ejemplo, haciendo visibles las instalaciones existentes y facilitando el intercambio de experiencias entre usuarios.

#### Conexión con los modelos de red

El modelo de Bass asume una población homogénea y bien mezclada — todos interactúan con todos por igual. Esta es su limitación. Los modelos de umbral y contagio complejo sobre redes **desagregan** esta dinámica: permiten ver que la difusión no ocurre uniformemente sino a lo largo de las conexiones de la red, con velocidades que dependen de la topología local. El modelo de Bass es el promedio; los modelos de red revelan la heterogeneidad oculta detrás de ese promedio.

---

## 4. Fallas en cascada como dinámica sobre redes

En la Semana 2 introdujimos las fallas en cascada usando el modelo de capacidad-carga (Motter-Lai): cuando un nodo falla, su carga se redistribuye entre los nodos vecinos, potencialmente sobrecargándolos y causando nuevas fallas. Ahora podemos entender este fenómeno como un caso particular de **dinámica sobre redes**.

### La cascada como proceso temporal

Reescribamos la falla en cascada como una secuencia temporal explícita:

1. **$t=0$**: Un nodo $i_0$ falla (por ataque dirigido, falla mecánica o evento natural).
2. **$t=1$**: La carga de $i_0$ se redistribuye entre sus vecinos. Los nodos cuya nueva carga supera su capacidad fallan.
3. **$t=2$**: La carga de los nodos que fallaron en $t=1$ se redistribuye. Nuevos nodos pueden fallar.
4. **$t=k$**: El proceso continúa hasta que no se producen nuevas fallas (equilibrio) o hasta el colapso total.

Formalmente, si $L_i(t)$ es la carga del nodo $i$ en el paso $t$ y $C_i$ es su capacidad máxima:

$$s_i(t+1) = \begin{cases} \text{fallado} & \text{si } L_i(t) > C_i \\ \text{operativo} & \text{en caso contrario} \end{cases}$$

La redistribución de carga sigue alguna regla que depende de la topología — por ejemplo, la carga se reparte proporcionalmente entre los vecinos operativos del nodo fallado.

### El papel de la topología en el tamaño de la cascada

La topología determina dos cosas cruciales:

1. **La vulnerabilidad inicial**: qué nodos, al fallar, disparan la cascada más grande (típicamente los de mayor betweenness, como vimos en la Semana 2).
2. **La propagación**: cómo se ramifica la cascada a través de la red. En redes altamente conectadas, una falla puede propagarse ampliamente; en redes modularizadas, la cascada puede quedar contenida dentro de un módulo.

### Robusto-pero-frágil, ahora con dinámica

La paradoja "robusto pero frágil" de la Semana 2 adquiere una dimensión temporal. Las redes tipo ley de potencia (*scale-free*):

- Son **robustas** a fallas aleatorias no solo topológicamente, sino también dinámicamente: las fallas aleatorias rara vez desencadenan cascadas grandes porque los nodos de bajo grado tienen poca carga para redistribuir.
- Son **frágiles** a ataques dirigidos no solo porque la red se desconecta, sino porque la cascada dinámica es explosiva: la falla de un hub redistribuye una cantidad enorme de carga, sobrecargando múltiples nodos simultáneamente, que a su vez redistribuyen más carga.

El apagón del noreste de Estados Unidos en 2003, que mencionamos en las Semanas 1 y 2, es un ejemplo canónico: una falla local en Ohio desencadenó una cascada que se propagó a través de la red eléctrica interconectada, dejando sin electricidad a 55 millones de personas. La dinámica temporal fue clave: la cascada se desarrolló en aproximadamente 9 minutos, demasiado rápido para que los operadores intervinieran eficazmente.

---

## 5. Redes de actores y stakeholders

### 5.1 Del cable al actor

Hasta ahora hemos usado las redes para representar infraestructura física: subestaciones conectadas por líneas de transmisión. Pero las herramientas de análisis de redes son igualmente poderosas — y a veces más reveladoras — cuando las aplicamos a **relaciones sociales, institucionales y comerciales**.

En una red de actores del sistema energético:

- **Nodos** = actores: generadores (EPM, Enel, Celsia), comercializadores, el regulador (CREG), el operador del mercado (XM), comunidades locales, inversionistas, ONGs ambientales, ministerios (MME, MinAmbiente), autoridades ambientales (ANLA), gremios (ACOLGÉN, SER Colombia).
- **Aristas** = relaciones: contratos de compraventa de energía, relaciones de supervisión regulatoria, flujos de información, alianzas estratégicas, relaciones de conflicto, dependencia financiera.

Las redes de actores suelen tener propiedades que las redes físicas no tienen:

- **Direccionalidad**: la relación "A regula a B" no es simétrica. Se modelan como **grafos dirigidos**.
- **Múltiples tipos de relación**: dos actores pueden estar conectados por un contrato comercial y simultáneamente por una relación de supervisión. Esto da lugar a **redes multiplex** (varias capas de relación sobre los mismos nodos).
- **Pesos variables**: la intensidad de una relación (por ejemplo, el volumen de energía transado) se modela con **aristas ponderadas**.

### 5.2 El mercado mayorista colombiano como red

El mercado mayorista de energía de Colombia, operado por XM, ofrece un caso fascinante de análisis de redes. En este mercado, los **generadores** venden energía a los **comercializadores**, quienes a su vez la venden a los usuarios finales.

Podemos construir un grafo donde:

- **Nodo tipo 1**: generadores (Emgea-EPM, Enel-Emgesa, Celsia, ISAGEN, AES Colombia, etc.).
- **Nodo tipo 2**: comercializadores (que pueden ser las mismas empresas u otras).
- **Aristas**: contratos bilaterales, con peso proporcional al volumen de energía transado (en GWh).

#### ¿Qué nos dice la centralidad?

Las métricas de centralidad, que en la Semana 2 aplicamos a subestaciones, adquieren un significado nuevo:

- **Centralidad de grado** alta = un actor con muchos contratos o relaciones comerciales. Indica **diversificación** o **dominancia de mercado** según el contexto.
- **Centralidad de intermediación** (*betweenness*) alta = un actor que conecta grupos de actores que de otro modo estarían desconectados. En el mercado, podría ser un comercializador que sirve de puente entre generadores grandes y pequeños comercializadores regionales. Este actor tiene **poder de intermediación**.
- **Centralidad de cercanía** (*closeness*) alta = un actor que puede llegar rápida y eficientemente a todos los demás. En una red de influencia política, esto indica capacidad de hacer *lobby* efectivo.

#### ¿Y si un hub sale del mercado?

Aquí es donde la teoría de la Semana 2 sobre redes "libres de escala" se vuelve un instrumento de análisis de **riesgo sistémico**. Si la red de contratos del mercado mayorista es concentrada — pocos actores participan en la mayor parte del volumen transado — entonces la salida abrupta de un actor dominante (por quiebra, por decisión regulatoria, o por un evento extraordinario) podría:

1. Dejar a múltiples comercializadores sin suministro contratado.
2. Forzar a esos comercializadores a comprar en bolsa, disparando los precios.
3. Generar un efecto en cascada donde otros actores con contratos vinculados se ven afectados.

Este análisis no es hipotético: la concentración del mercado mayorista colombiano ha sido objeto de debate regulatorio durante años.

### 5.3 Redes bipartitas y de afiliación

#### ¿Qué es una red bipartita?

Una red **bipartita** (*bipartite network*) es un grafo con dos tipos de nodos, donde las aristas solo conectan nodos de tipos diferentes — nunca dos nodos del mismo tipo. Formalmente, el conjunto de nodos $V$ se particiona en dos conjuntos disjuntos $V_1$ y $V_2$, y toda arista $e \in E$ conecta un nodo de $V_1$ con un nodo de $V_2$.

Ejemplos en el sector energético:

| $V_1$ (Tipo 1) | $V_2$ (Tipo 2) | Arista |
|---|---|---|
| Generadores | Comercializadores | Contrato bilateral |
| Proyectos FNCER | Comunidades afectadas | Proceso de consulta/impacto |
| Empresas | Tecnologías | Adopción/inversión |
| Reguladores | Regulaciones | Autoría/emisión |

#### Proyecciones de redes bipartitas

Una operación clave es la **proyección**: a partir de una red bipartita, podemos crear una red de un solo tipo de nodo. En la proyección sobre $V_1$, dos nodos de tipo 1 están conectados si comparten al menos un vecino de tipo 2.

**Ejemplo concreto**: si tenemos la red bipartita generadores-comercializadores, la proyección sobre generadores crea una red donde dos generadores están conectados si venden a al menos un comercializador en común. Esta red de proyección revela **competencia directa**: los generadores conectados compiten por los mismos clientes.

Similarmente, la proyección sobre comercializadores crea una red donde dos comercializadores están conectados si compran a al menos un generador en común. Esto revela **dependencia compartida**: si ese generador falla, ambos comercializadores se ven afectados.

#### Redes de afiliación

Las redes bipartitas donde un tipo de nodo representa una "membresía" o "afiliación" se llaman **redes de afiliación** (*affiliation networks*). Por ejemplo:

- Actores del sector energético afiliados a gremios o mesas de trabajo regulatorias.
- Investigadores afiliados a proyectos de I+D en energía.
- Comunidades afectadas por múltiples proyectos energéticos.

La proyección de estas redes revela estructuras sociales ocultas: ¿qué actores se encuentran recurrentemente en los mismos espacios? ¿Qué comunidades enfrentan impactos acumulativos de múltiples proyectos?

---

## 6. Detección de comunidades

### ¿Qué es una comunidad en una red?

En el análisis de redes, una **comunidad** (*community*) o **módulo** es un grupo de nodos que están más densamente conectados entre sí que con el resto de la red. No hay una definición única y universal, pero la intuición es clara: son "clústeres" naturales dentro de la red.

En el contexto energético:

- En la red del STN: las comunidades podrían corresponder a regiones del sistema (Costa Atlántica, Antioquia, Centro, Suroccidente) que están internamente bien conectadas pero con pocas líneas de interconexión entre ellas.
- En la red de actores del mercado: las comunidades podrían revelar "bloques" de generadores y comercializadores que operan preferentemente entre sí.
- En una red de adopción solar: las comunidades podrían corresponder a barrios o grupos sociales donde la adopción se difunde internamente.

### Modularidad como medida

La medida más usada para evaluar la calidad de una partición en comunidades es la **modularidad** (*modularity*), propuesta por Newman y Girvan (2004):

$$Q = \frac{1}{2m} \sum_{ij} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)$$

donde:

- $A_{ij}$ es la entrada de la matriz de adyacencia (1 si hay arista, 0 si no).
- $k_i, k_j$ son los grados de los nodos $i$ y $j$.
- $m$ es el número total de aristas.
- $c_i$ es la comunidad asignada al nodo $i$.
- $\delta(c_i, c_j) = 1$ si $i$ y $j$ están en la misma comunidad, 0 en caso contrario.

**Lectura intuitiva**: la modularidad compara la densidad de aristas *dentro* de cada comunidad con la densidad que esperaríamos si las aristas estuvieran distribuidas al azar. Un valor de $Q$ cercano a 0 indica una partición no mejor que la aleatoria; valores de $Q > 0.3$ se consideran indicativos de estructura comunitaria significativa.

### Algoritmos de detección

Existen múltiples algoritmos para detectar comunidades. Los más utilizados en la práctica (implementados en NetworkX y bibliotecas como `community` o `leidenalg`):

- **Louvain**: algoritmo voraz que optimiza la modularidad iterativamente. Rápido y efectivo para redes grandes.
- **Leiden**: mejora sobre Louvain con garantías teóricas más fuertes.
- **Girvan-Newman**: basado en la remoción iterativa de aristas con mayor betweenness.

En el Laboratorio 2 de esta semana, los estudiantes aplicarán detección de comunidades a la red de actores del mercado mayorista colombiano para identificar clústeres de mercado y evaluar si la estructura modular del mercado tiene implicaciones de riesgo sistémico.

---

## 7. El caso de la semana: adopción de energía solar distribuida en Colombia

### Los datos

La generación distribuida en Colombia ha experimentado un crecimiento notable. Según datos de la UPME y del registro de autogeneración de XM, la capacidad instalada de techos solares pasó de menos de 10 MW en 2017 a más de 800 MW en 2024, con más de 6.000 instalaciones registradas. La curva de adopción acumulada muestra una forma inconfundible: la **curva en S**.

### ¿Por qué fallan los modelos puramente económicos?

Un modelo de decisión basado únicamente en el VPN predeciría que:

1. Todo usuario para quien el VPN es positivo (dados los precios de electricidad, el costo de los paneles y los incentivos tributarios) adoptaría inmediatamente.
2. La adopción sería un escalón: cero antes de que la tecnología sea viable, 100% después.
3. La distribución geográfica de la adopción sería uniforme entre usuarios con características económicas similares.

Ninguna de estas tres predicciones se cumple. La adopción es gradual, sigue una S, y muestra fuertes patrones geográficos. ¿Qué falta?

### El papel del contagio social

La explicación reside en los mecanismos de contagio social que hemos estudiado:

1. **Visibilidad**: las instalaciones solares son **visibles** — se ven en los techos. Cada instalación es un "anuncio" permanente para los vecinos. Esto genera el efecto de imitación ($q$) en el modelo de Bass.

2. **Contagio complejo**: instalar paneles solares es una decisión costosa e irreversible. La mayoría de las personas necesitan ver a **varios** vecinos o conocidos con la tecnología antes de dar el paso. Esto explica la formación de clústeres geográficos.

3. **Heterogeneidad de umbrales**: los "innovadores" (ingenieros del sector, ambientalistas convencidos, entusiastas tecnológicos) tienen umbrales bajos — adoptan temprano, a menudo por motivaciones no puramente económicas. Ellos sirven como semilla. La "mayoría temprana" tiene umbrales intermedios y necesita ver al innovador vecino y a un par de conocidos más. La "mayoría tardía" y los "rezagados" esperan hasta que sea casi la norma.

4. **Efecto red local**: en conjuntos residenciales o barrios con asociaciones de vecinos fuertes, la adopción se difunde más rápido porque las conexiones sociales son más densas (alto clustering).

### Aplicación conceptual de los modelos

Podemos usar los modelos de esta semana para interpretar la curva observada:

- **Fase 1 (2017-2019): arranque lento**. Pocos innovadores. El modelo de Bass con $p$ pequeño (poca publicidad, incentivos poco conocidos) y $q$ que aún no opera (pocos adoptantes para imitar).

- **Fase 2 (2020-2022): aceleración**. La Ley 2099 (2021) aumenta $p$ (más incentivos, más visibilidad regulatoria). Simultáneamente, los adoptantes tempranos generan el efecto de imitación ($q$ se activa). La combinación es explosiva: $dF/dt = (p + qF)(1-F)$ crece rápidamente cuando $F$ empieza a ser apreciable.

- **Fase 3 (2023-2024): saturación incipiente**. El mercado de early adopters se va agotando. $(1-F)$ disminuye. La tasa de crecimiento empieza a desacelerarse, formando la parte superior de la S.

### Implicaciones para política pública

La teoría de difusión en redes ofrece recomendaciones concretas:

1. **Focalizar los subsidios iniciales** en comunidades con alta densidad de conexiones sociales (conjuntos residenciales, barrios con organizaciones comunitarias activas) para maximizar la cascada de adopción.

2. **Hacer visible lo invisible**: programas que muestren las instalaciones existentes y sus resultados (ahorro real, confiabilidad) amplifican el coeficiente $q$.

3. **Identificar y apoyar a los "nodos semilla"**: profesionales del sector, líderes comunitarios, figuras públicas locales. Un innovador bien conectado puede disparar una cascada que un subsidio uniforme no logra.

4. **No subestimar la estructura social**: dos municipios con idénticas condiciones de radiación solar y capacidad económica pueden tener tasas de adopción dramáticamente diferentes si uno tiene redes sociales más densas y el otro tiene una población más fragmentada.

---

## 8. Cierre del módulo de redes: ¿qué aprendimos y qué falta?

### Lo que las redes SÍ pueden hacer

En dos semanas hemos construido un arsenal analítico considerable:

- **Revelar estructura**: traducir sistemas complejos (infraestructura eléctrica, mercados, relaciones sociales) en grafos analizables.
- **Identificar nodos críticos**: betweenness, grado, centralidad de cercanía nos dicen dónde están los cuellos de botella y los actores clave.
- **Modelar difusión y cascadas**: los modelos de contagio y umbral predicen cómo se propagan tecnologías, información y fallas a través de la red.
- **Detectar comunidades**: la detección de módulos revela agrupamientos naturales en mercados, regiones y ecosistemas de actores.
- **Cuantificar vulnerabilidad**: la paradoja robusto-pero-frágil, verificada con ataques dirigidos y fallas aleatorias.

### Lo que las redes NO pueden hacer

Sin embargo, las redes tienen una **limitación fundamental** que nos obliga a buscar herramientas complementarias:

> Los modelos de redes de esta unidad representan conexiones y estados locales. Una red también puede tener estados continuos; cuando la pregunta se concentra en acumulaciones, flujos y retardos agregados, la dinámica de sistemas ofrece una representación complementaria. La elección depende de la pregunta y del nivel de agregación, no de una prohibición de usar cantidades continuas en redes.

Considere las siguientes preguntas que el análisis de redes no puede responder bien:

- ¿Cómo evoluciona el **precio de la electricidad** en el tiempo, y cómo responde a cambios en la capacidad instalada?
- ¿Cuánta **capacidad instalada** habrá en 2030 si se invierte a la tasa actual? ¿Y si cambia la regulación?
- ¿Cómo interactúan la **oferta**, la **demanda**, los **inventarios** de embalses y los **retardos** de construcción de nuevas plantas?

Estas preguntas involucran **stocks** (acumuladores: capacidad instalada, volumen de embalse, capital acumulado) y **flujos** (tasas: inversión por año, generación por hora, consumo por día) que evolucionan continuamente en el tiempo, con **retroalimentaciones** y **retardos**.

Este es precisamente el dominio de la **Dinámica de Sistemas** (*System Dynamics*), que estudiaremos en las Semanas 4 y 5.

### El puente conceptual

Piénselo así:

| Redes (Semanas 2-3) | Dinámica de Sistemas (Semanas 4-5) |
|---|---|
| Estructura: ¿quién está conectado con quién? | Comportamiento: ¿cómo cambian las cantidades en el tiempo? |
| Estados discretos: adoptó / no adoptó | Variables continuas: precio, capacidad, demanda |
| Topología como determinante | Retroalimentaciones y retardos como determinantes |
| Instantánea o dinámica de estados | Evolución temporal de acumulaciones y flujos |

Ambas perspectivas son complementarias, no competitivas. El análisis completo de un sistema energético requiere entender tanto su **estructura** (redes) como su **comportamiento temporal** (dinámica de sistemas). La Semana 6 mostrará cómo integrarlas.

---

## 9. Horizonte: modelamiento basado en agentes (ABM)

Antes de cerrar el módulo de redes, vale la pena señalar un camino natural de profundización que el curso no cubre en detalle pero que el estudiante debería conocer: el **modelamiento basado en agentes** (*Agent-Based Modeling*, ABM).

### De "nodos con reglas" a "agentes con estrategias"

En los modelos de esta semana, los nodos siguen reglas de actualización relativamente simples: adoptan si suficientes vecinos adoptaron, se contagian con cierta probabilidad, fallan si se sobrecargan. Pero en la realidad, los actores del sistema energético son mucho más sofisticados:

- Un generador no solo "opera" o "falla" — decide cuánto producir, a qué precio ofertar, si invierte en nueva capacidad.
- Una comunidad no solo "adopta" o "no adopta" — evalúa costos, negocia condiciones, observa el comportamiento de empresas y reguladores a lo largo del tiempo, aprende de experiencias pasadas.
- Un regulador no solo "regula" o "no regula" — ajusta sus reglas en función de los resultados observados, con retardos y con presiones políticas.

El ABM lleva el análisis de redes al siguiente nivel: los nodos se convierten en **agentes** con reglas de comportamiento heterogéneas, capacidad de aprendizaje, memoria y estrategia. Cada agente:

1. **Percibe** su entorno (incluyendo los estados de sus vecinos en la red).
2. **Decide** según una regla que puede ser tan simple como un umbral o tan compleja como un algoritmo de optimización.
3. **Actúa**, cambiando su estado y potencialmente el de su entorno.
4. **Aprende**, modificando sus reglas futuras en función de los resultados.

### Framework Mesa (Python)

En el ecosistema Python que usa este curso, la biblioteca **Mesa** proporciona un entorno para construir modelos ABM. Mesa permite definir agentes, ubicarlos en una red (o en un espacio geográfico), especificar sus reglas de comportamiento, y simular la evolución del sistema. Aunque no lo implementaremos en este curso, es la extensión natural para quien quiera profundizar.

### Ejemplo conceptual: mercado de energía peer-to-peer (P2P)

Imaginemos un barrio con 50 casas, algunas con paneles solares y baterías. En un mercado P2P:

- Cada casa es un **agente** con un perfil de generación y consumo.
- Los agentes pueden comprar y vender energía entre sí, negociando precios.
- Las decisiones de compra/venta dependen del precio, del nivel de carga de la batería, y de las estrategias aprendidas.
- La red de transacciones evoluciona: nuevas conexiones se forman, viejas se disuelven.

Un modelo ABM captura esta riqueza. Un modelo de redes puras no podría modelar la negociación de precios; un modelo de dinámica de sistemas no podría capturar la heterogeneidad de 50 agentes individuales. El ABM integra ambas dimensiones.

> **Nota**: el ABM no se evalúa en este curso. Se presenta como horizonte de profundización para el estudiante interesado en continuar su formación en análisis sistémico avanzado.

---

## 10. Resumen y conceptos para llevar

### Conceptos clave de la semana

1. **Dinámica sobre redes**: los nodos tienen estados que cambian en función de los estados de sus vecinos, siguiendo reglas de actualización.

2. **Contagio simple**: cada contacto con un adoptante tiene probabilidad independiente $p$ de causar adopción. Un solo contacto basta. Los hubs y los puentes entre comunidades aceleran la difusión.

3. **Contagio complejo**: la adopción requiere refuerzo social múltiple — ver a varios vecinos adoptantes. El clustering (agrupamiento) favorece la difusión. Explica los clústeres geográficos de adopción tecnológica.

4. **Modelos de umbral**: cada nodo tiene un umbral $\theta_i$ — la fracción de vecinos adoptantes necesaria para activarlo. La condición de cascada de Watts: una cascada global requiere un componente conectado de nodos vulnerables.

5. **Modelo de Bass**: difusión a nivel agregado con influencia externa ($p$) e imitación ($q$). Produce la curva en S. Es la versión de campo medio de los modelos de umbral.

6. **Fallas en cascada como dinámica**: proceso temporal de falla → redistribución → sobrecarga → nueva falla. La topología determina la velocidad y el alcance de la cascada.

7. **Redes de actores**: nodos = actores del sistema energético, aristas = relaciones (contractuales, de supervisión, de influencia). Las métricas de centralidad revelan poder de mercado y riesgo sistémico.

8. **Redes bipartitas**: dos tipos de nodos con aristas solo entre tipos distintos. Las proyecciones revelan competencia, dependencia compartida o comunidades ocultas.

9. **Detección de comunidades**: identificación de grupos densamente conectados. La modularidad $Q$ mide la calidad de la partición.

### Glosario de términos introducidos

| Término en español | Término en inglés | Definición breve |
|---|---|---|
| Contagio simple | Simple contagion | Modelo de difusión donde un solo contacto con un adoptante puede causar adopción |
| Contagio complejo | Complex contagion | Modelo de difusión que requiere refuerzo social múltiple para causar adopción |
| Umbral de adopción | Adoption threshold | Fracción mínima de vecinos adoptantes requerida para que un nodo adopte |
| Cascada global | Global cascade | Proceso donde una perturbación pequeña (semilla) activa una fracción macroscópica de la red |
| Nodo vulnerable | Vulnerable node | Nodo con umbral suficientemente bajo para ser activado por un solo vecino |
| Falla en cascada (temporal) | Cascading failure (dynamic) | Proceso temporal de falla → redistribución → sobrecarga → nueva falla, extendiendo la definición estática de la Semana 2 |
| Modelo de Bass | Bass diffusion model | Modelo agregado de difusión de innovaciones con coeficientes de innovación ($p$) e imitación ($q$) |
| Red bipartita | Bipartite network | Grafo con dos tipos de nodos donde las aristas solo conectan nodos de tipos distintos |
| Proyección | Projection | Red de un solo tipo de nodo derivada de una red bipartita |
| Comunidad / módulo | Community / module | Grupo de nodos más densamente conectados entre sí que con el resto de la red |
| Modularidad | Modularity | Métrica $Q$ que evalúa la calidad de una partición en comunidades |
| Regla de actualización | Update rule | Función que determina el nuevo estado de un nodo basándose en los estados de sus vecinos |
| ABM | Agent-Based Modeling | Modelamiento basado en agentes con comportamiento heterogéneo y capacidad de aprendizaje |

### Puente a la Semana 4

Tenemos la **estructura** (Semanas 2-3). Ahora necesitamos el **tiempo**.

En la Semana 4 aprenderemos a construir modelos de **dinámica de sistemas**: stocks que se acumulan, flujos que los llenan o vacían, retroalimentaciones que los conectan, y retardos que generan oscilaciones. Aplicaremos estas herramientas al ciclo de inversión-capacidad en generación eléctrica colombiana — una dinámica que explica por qué el sector oscila entre sobreinversión y escasez, y que los análisis estáticos de VPN jamás podrían capturar.

> *"Las redes nos dicen quién está conectado con quién. La dinámica de sistemas nos dice qué pasa con el tiempo. Para entender un sistema energético completo, necesitamos ambas."*

---

### Referencias principales

- Barabási, A.-L. (2016). *Network Science*. Cambridge University Press. Capítulos 5-6, 10. [Acceso abierto: networksciencebook.com]
- Bass, F. M. (1969). A new product growth for model consumer durables. *Management Science*, 15(5), 215-227.
- Centola, D. & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702-734.
- Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420-1443.
- Motter, A. E. & Lai, Y.-C. (2002). Cascade-based attacks on complex networks. *Physical Review E*, 66(6), 065102.
- Newman, M. E. J. & Girvan, M. (2004). Finding and evaluating community structure in networks. *Physical Review E*, 69(2), 026113.
- Rogers, E. M. (2003). *Diffusion of Innovations* (5ª ed.). Free Press.
- Watts, D. J. (2002). A simple model of global cascades on random networks. *Proceedings of the National Academy of Sciences*, 99(9), 5766-5771.

---

*En la Semana 4 daremos el salto de la estructura a la dinámica temporal. Aprenderemos a construir modelos de stocks y flujos — variables que se acumulan y se vacían con el tiempo — para simular el ciclo de inversión-capacidad en generación eléctrica colombiana. Las redes nos dijeron dónde están las vulnerabilidades; la dinámica de sistemas nos dirá qué pasa cuando las activamos.*
