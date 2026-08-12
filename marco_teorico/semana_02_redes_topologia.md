# Semana 2 — Redes complejas: la estructura oculta de los sistemas energéticos

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

> *"La forma en que las cosas están conectadas importa tanto como las cosas en sí mismas."*
> — Albert-László Barabási

---

## 1. Apertura: ¿Por qué pensar en redes?

Abra el mapa del Sistema Interconectado Nacional (SIN) de Colombia publicado por la UPME. Verá líneas de transmisión que cruzan cordilleras, conectan ciudades costeras con centros industriales del interior, y llevan la energía de las hidroeléctricas de Antioquia hasta la península de La Guajira. Lo que está mirando es, literalmente, una **red**: un conjunto de puntos (subestaciones) conectados por líneas (circuitos de transmisión).

Ahora considere una pregunta aparentemente sencilla: *¿qué pasaría si la subestación más conectada del país falla?* La respuesta no depende solo de la capacidad de esa subestación ni de la demanda que atiende. Depende de **cómo está conectada al resto del sistema** — de su posición en la red. Una subestación que funciona como puente único entre dos regiones es cualitativamente diferente de una que tiene múltiples rutas alternativas, incluso si ambas manejan la misma potencia.

Esta es la idea central de este capítulo: **la topología de las conexiones determina el comportamiento del sistema tanto como la capacidad de los componentes individuales**. En la planificación energética tradicional, pensamos en capacidades: MW de generación, MVA de transformación, km de línea. Pero rara vez analizamos la *estructura* de las conexiones como un objeto de estudio en sí mismo. La ciencia de redes nos da el lenguaje y las herramientas para hacerlo.

### ¿Qué revelan las redes que el análisis tradicional no?

El análisis convencional de sistemas de potencia evalúa flujos de carga, despacho económico y estabilidad transitoria. Son herramientas indispensables. Pero operan sobre el sistema *como está configurado en un momento dado*, sin preguntarse qué tan vulnerable es la *estructura misma* de ese sistema. El análisis de redes complementa esta mirada al responder preguntas como:

- ¿Cuáles son los **cuellos de botella topológicos** del SIN — las subestaciones cuya falla desconecta regiones enteras?
- ¿La red de transmisión colombiana se parece más a una **malla uniforme** o a un sistema con unos pocos **nodos dominantes** de los que depende todo?
- ¿La conexión de los nuevos parques eólicos en La Guajira hace al sistema **más robusto** o introduce nuevas **fragilidades**?
- ¿Qué tan rápido se **propaga una falla** desde un punto del sistema al resto?

Para responder estas preguntas, necesitamos un lenguaje formal. Ese lenguaje es la **teoría de grafos** (graph theory), y su aplicación a sistemas del mundo real es lo que llamamos **ciencia de redes** (network science).

---

## 2. Fundamentos: el lenguaje de las redes

### 2.1 Nodos y aristas: los ladrillos básicos

Una red (o **grafo**, graph) se compone de dos elementos:

- **Nodos** (nodes o vertices): las entidades del sistema. En el SIN, los nodos son las subestaciones de transmisión.
- **Aristas** (edges o links): las conexiones entre entidades. En el SIN, las aristas son las líneas de transmisión y los transformadores que conectan subestaciones.

Formalmente, un grafo $G$ se define como un par $G = (V, E)$ donde $V$ es el conjunto de nodos (vértices) y $E$ es el conjunto de aristas. Cada arista conecta un par de nodos: si los nodos $i$ y $j$ están conectados, escribimos $(i, j) \in E$.

> **Ejemplo de referencia**: Para construir intuición, trabajaremos con una red pequeña de 6 nodos que representa un sistema eléctrico simplificado. Imagine 6 subestaciones que llamaremos $A$, $B$, $C$, $D$, $E$ y $F$, con las siguientes conexiones:
>
> - $A$ se conecta con $B$, $C$ y $D$
> - $B$ se conecta con $A$, $C$ y $E$
> - $C$ se conecta con $A$, $B$ y $D$
> - $D$ se conecta con $A$, $C$ y $F$
> - $E$ se conecta con $B$ solamente
> - $F$ se conecta con $D$ solamente
>
> Note que $A$, $B$, $C$ y $D$ forman un núcleo densamente conectado, mientras que $E$ y $F$ son nodos periféricos con una sola conexión cada uno.

### 2.2 Grafos dirigidos vs. no dirigidos

Cuando solo nos importa si dos subestaciones están **físicamente conectadas** — es decir, si existe una línea de transmisión entre ellas —, usamos un **grafo no dirigido** (undirected graph): la arista $(A, B)$ es la misma que $(B, A)$.

Pero en otros contextos la dirección importa. Si queremos modelar el **flujo de potencia activa** por las líneas, necesitamos un **grafo dirigido** (directed graph o dígrafo): la arista $(A, B)$ indica que fluye potencia de $A$ hacia $B$, lo cual es diferente de $(B, A)$. Las flechas importan.

| Tipo de grafo | Cuándo usarlo en energía | Ejemplo |
|---|---|---|
| No dirigido | Conectividad física, topología del STN | ¿Están conectadas las subestaciones Primavera y Bacatá? |
| Dirigido | Flujos de potencia, transacciones comerciales | ¿En qué dirección fluye la energía entre Antioquia y la Costa? |

Para el análisis topológico de este capítulo, trabajaremos principalmente con **grafos no dirigidos**: nos interesa la *estructura de conexiones*, no la dirección de los flujos en un instante dado.

### 2.3 Grafos ponderados: no todas las conexiones son iguales

En un grafo simple, una arista solo dice "existe conexión" o "no existe conexión". Pero una línea de transmisión de 500 kV con capacidad de 1,500 MW no es igual a una de 110 kV con capacidad de 100 MW. Para capturar estas diferencias, usamos **grafos ponderados** (weighted graphs): cada arista tiene un peso $w_{ij}$ que representa alguna propiedad cuantitativa.

En el contexto del SIN, los pesos pueden representar:

- **Capacidad de transmisión** (MW): cuánta potencia puede fluir por la línea.
- **Impedancia** (Ω): la resistencia eléctrica de la línea (a mayor impedancia, mayor dificultad para transmitir).
- **Distancia** (km): la longitud física de la línea.

La elección del peso depende de la pregunta que queremos responder. Si nos preguntamos por la capacidad del sistema, ponderamos por MW. Si nos preguntamos por la propagación de fallas eléctricas, ponderamos por impedancia.

### 2.4 La matriz de adyacencia: la red como números

Toda la información de un grafo puede codificarse en una **matriz de adyacencia** (adjacency matrix) $\mathbf{A}$. Para un grafo de $N$ nodos, $\mathbf{A}$ es una matriz de $N \times N$ donde:

$$A_{ij} = \begin{cases} 1 & \text{si existe una arista entre } i \text{ y } j \\ 0 & \text{en caso contrario} \end{cases}$$

Para grafos no dirigidos, la matriz es simétrica: $A_{ij} = A_{ji}$. Para grafos ponderados, reemplazamos el $1$ por el peso $w_{ij}$.

Volviendo a nuestro ejemplo de 6 nodos ($A, B, C, D, E, F$), la matriz de adyacencia es:

$$\mathbf{A} = \begin{pmatrix} 0 & 1 & 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \end{pmatrix}$$

Esta representación puede parecer redundante para una red pequeña, pero es la forma en que las computadoras almacenan y manipulan redes. Cuando el SIN tiene más de 500 subestaciones, es imposible razonar "a ojo" sobre la estructura — necesitamos la matriz y los algoritmos que operan sobre ella.

### 2.5 Vecinos, caminos y componentes conectados

Con el grafo definido, podemos hablar de relaciones entre nodos:

- **Vecinos** (neighbors): los nodos directamente conectados a un nodo dado. En nuestro ejemplo, los vecinos de $A$ son $\{B, C, D\}$. Los vecinos de $E$ son solo $\{B\}$.

- **Camino** (path): una secuencia de nodos conectados por aristas sin repetir nodos. Por ejemplo, para ir de $E$ a $F$ podemos seguir: $E \to B \to A \to D \to F$ (un camino de longitud 4) o $E \to B \to C \to D \to F$ (también longitud 4). No hay un camino más corto.

- **Camino más corto** (shortest path): el camino entre dos nodos que usa el menor número de aristas. La longitud del camino más corto entre $i$ y $j$ se llama la **distancia geodésica** $d(i, j)$.

- **Componente conectado** (connected component): un subconjunto de nodos donde existe al menos un camino entre cualquier par. En nuestro ejemplo, todos los nodos forman un solo componente conectado. Pero si eliminamos el nodo $B$, el nodo $E$ quedaría **desconectado** del resto — formaría su propio componente. Esta situación en el SIN equivaldría a una isla eléctrica: una región que pierde conectividad con el sistema principal.

> **Interpretación energética**: Un componente conectado en el grafo del SIN corresponde a una zona eléctrica operando de forma autónoma. En condiciones normales, el SIN es un solo componente conectado. Cuando se produce un apagón regional — como el que afectó la Costa Caribe colombiana en varias ocasiones —, la red se fragmenta en múltiples componentes. Contar los componentes conectados después de simular una falla nos dice cuántas "islas eléctricas" se forman.

---

## 3. Métricas de redes: ¿qué nos dicen sobre el sistema?

Tener el grafo es solo el primer paso. Las **métricas de red** nos permiten cuantificar propiedades de la estructura que son invisibles a simple vista. Para cada métrica seguiremos el mismo esquema: significado intuitivo → definición formal → interpretación energética → decisiones que informa.

### 3.1 Métricas locales (de nodo)

Estas métricas caracterizan a cada nodo individual — nos dicen qué tan importante, central o redundante es un nodo específico dentro de la red.

#### Grado (*degree*)

**Intuición**: El grado de un nodo es simplemente su número de conexiones directas. Un nodo con muchas conexiones es un "hub"; uno con pocas es periférico.

**Definición formal**: Para un nodo $i$ en un grafo no dirigido, el grado $k_i$ es:

$$k_i = \sum_{j=1}^{N} A_{ij}$$

Es decir, la suma de la fila $i$ de la matriz de adyacencia.

**En nuestro ejemplo**: $k_A = 3$, $k_B = 3$, $k_C = 3$, $k_D = 3$, $k_E = 1$, $k_F = 1$. Los nodos del núcleo ($A$–$D$) tienen grado 3, mientras que los periféricos ($E$, $F$) tienen grado 1.

**Interpretación energética**: El grado de una subestación indica cuántas líneas de transmisión llegan a ella. Subestaciones como Bacatá (en Cundinamarca) o Cerromatoso (en Córdoba) tienen grados altos porque concentran múltiples líneas de transmisión de distintas direcciones. Una subestación con grado 1 — como las que alimentan zonas no interconectadas o terminales de distribución — es especialmente vulnerable: si su única línea falla, queda aislada.

**Decisión que informa**: Identificar nodos de bajo grado ayuda a priorizar proyectos de redundancia. Un nodo con $k=1$ es un candidato natural para una segunda línea.

#### Centralidad de intermediación (*betweenness centrality*)

**Intuición**: Imagine que toda la comunicación entre nodos debe fluir por los caminos más cortos. La centralidad de intermediación mide **cuántos de esos caminos pasan por un nodo dado**. Un nodo con alta intermediación es un "cuello de botella": si lo eliminamos, muchos pares de nodos pierden su ruta más eficiente.

**Definición formal**: Para un nodo $v$:

$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

donde $\sigma_{st}$ es el número total de caminos más cortos entre $s$ y $t$, y $\sigma_{st}(v)$ es el número de esos caminos que pasan por $v$. Frecuentemente se normaliza dividiendo por $(N-1)(N-2)/2$ para que el valor esté entre 0 y 1.

**En nuestro ejemplo**: El nodo $B$ tiene alta intermediación porque es el **único** camino para que $E$ se comunique con cualquier otro nodo. Si removemos $B$, el nodo $E$ queda completamente aislado. De manera análoga, $D$ es el único camino para $F$.

**Interpretación energética**: Una subestación con alta centralidad de intermediación es un **cuello de botella sistémico**. No necesariamente es la que más potencia maneja, sino la que está en una posición topológica crítica. Si falla, obliga a los flujos de potencia a tomar rutas mucho más largas (si existen), con las consecuentes pérdidas y congestiones. En el SIN colombiano, las subestaciones que conectan la Costa Caribe con el interior del país (por los corredores de transmisión que cruzan Santander o el Bajo Cauca) probablemente tienen alta intermediación.

**Decisión que informa**: Los nodos de alta intermediación deben ser prioridad en planes de mantenimiento, refuerzo y protección.

#### Centralidad de cercanía (*closeness centrality*)

**Intuición**: Un nodo es "cercano" al resto de la red si puede alcanzar a todos los demás nodos en pocos pasos. Es una medida de qué tan *accesible* es un nodo, o equivalentemente, qué tan rápido se propaga una perturbación desde ese nodo.

**Definición formal**: Para un nodo $i$:

$$C_C(i) = \frac{N - 1}{\sum_{j \neq i} d(i, j)}$$

donde $d(i, j)$ es la distancia geodésica (camino más corto) entre $i$ y $j$.

**En nuestro ejemplo**: Los nodos $A$, $B$, $C$ y $D$ tienen alta cercanía porque están a pocos pasos de todos los demás. Los nodos $E$ y $F$ tienen baja cercanía porque deben atravesar varios intermediarios para llegar a nodos distantes.

**Interpretación energética**: Una subestación con alta cercanía está topológicamente "en el centro" del sistema. Una perturbación originada allí (un cortocircuito, una sobrecarga) alcanza al resto del sistema más rápidamente. Inversamente, una señal de control emitida desde un centro de despacho cercano a este nodo llega a más partes del sistema con menor retardo.

#### Coeficiente de clustering (agrupamiento)

**Intuición**: El clustering mide qué tan conectados están los vecinos de un nodo **entre sí**. Si los tres amigos de una persona se conocen entre ellos, el clustering es alto. Si ninguno se conoce, es bajo. En redes, un alto clustering indica **redundancia local**: si un nodo falla, sus vecinos aún están conectados entre sí.

**Definición formal**: Para un nodo $i$ con grado $k_i$:

$$C_i = \frac{2 \cdot T_i}{k_i(k_i - 1)}$$

donde $T_i$ es el número de aristas que existen entre los vecinos de $i$. El denominador $k_i(k_i-1)/2$ es el máximo número posible de aristas entre $k_i$ vecinos. Note que $0 \leq C_i \leq 1$.

**En nuestro ejemplo**: Los vecinos de $A$ son $\{B, C, D\}$. ¿Cuántas aristas hay entre ellos? $B$–$C$ existe, pero $B$–$D$ no existe, y $C$–$D$ existe. Son 2 aristas de un máximo de 3, así que $C_A = 2 \cdot 2 / (3 \cdot 2) = 2/3 \approx 0.67$. Para los nodos $E$ y $F$, el clustering no está definido (o se define como 0) porque tienen grado 1 y no se puede formar un triángulo.

**Interpretación energética**: Una subestación con alto clustering pertenece a una zona de la red donde hay **múltiples rutas alternativas** entre los nodos cercanos. Si esa subestación falla, la energía puede redistribuirse localmente porque los vecinos mantienen conexiones entre sí. Por el contrario, un clustering bajo indica una configuración radial, con pocas alternativas y mayor riesgo de desconexión local.

### 3.2 Métricas globales (de red)

Estas métricas caracterizan la **red completa** — nos dan una vista panorámica de la estructura del sistema.

#### Densidad (*density*)

**Intuición**: ¿Qué fracción de todas las conexiones posibles existen realmente?

**Definición formal**: Para un grafo no dirigido con $N$ nodos y $L$ aristas:

$$\rho = \frac{2L}{N(N-1)}$$

El denominador $N(N-1)/2$ es el número máximo de aristas posibles. Una red completa (todos conectados con todos) tiene $\rho = 1$. Una red sin aristas tiene $\rho = 0$.

**En nuestro ejemplo**: $N = 6$, $L = 7$ (cuente las aristas), así que $\rho = 14/30 = 0.47$.

**Interpretación energética**: Las redes eléctricas reales tienen densidades muy bajas, típicamente $\rho < 0.05$. Construir líneas de transmisión es caro y tiene restricciones geográficas y ambientales; no es viable conectar "todo con todo". Una densidad baja no es necesariamente un problema — muchas redes eficientes son dispersas —, pero indica que **cada conexión es proporcionalmente más importante**.

#### Diámetro (*diameter*)

**Intuición**: El diámetro es la distancia más larga entre cualquier par de nodos, considerando siempre los caminos más cortos. Es el "peor caso" de qué tan lejos pueden estar dos puntos de la red.

**Definición formal**:

$$\text{diámetro}(G) = \max_{i,j \in V} d(i,j)$$

**En nuestro ejemplo**: La mayor distancia es entre $E$ y $F$: $E \to B \to A \to D \to F$ o $E \to B \to C \to D \to F$, ambas de longitud 4. Así que el diámetro es 4.

**Interpretación energética**: Un diámetro grande significa que existen pares de nodos que están topológicamente muy "lejos". En términos de propagación de disturbios, regulación de frecuencia o redistribución de carga después de una falla, estas distancias largas implican **retardos y pérdidas**.

#### Longitud promedio de camino (*average path length*)

**Intuición**: En promedio, ¿cuántos "saltos" hay que dar para ir de un nodo cualquiera a otro?

**Definición formal**:

$$\langle d \rangle = \frac{1}{N(N-1)} \sum_{i \neq j} d(i,j)$$

**En nuestro ejemplo**: Sumando todas las distancias entre todos los pares de nodos y dividiendo por $6 \times 5 = 30$, obtenemos $\langle d \rangle \approx 2.07$.

**Interpretación energética**: Una longitud promedio de camino baja indica que el sistema es compacto y que los flujos de potencia pueden redistribuirse eficientemente. Redes con longitudes promedio altas son más susceptibles a congestiones regionales.

#### Distribución de grado (*degree distribution*)

**Intuición**: Si hacemos un histograma de los grados de todos los nodos — ¿cuántos nodos tienen grado 1, cuántos grado 2, cuántos grado 3, etc.? — obtenemos la **distribución de grado**. Esta es probablemente la métrica **más importante** de una red, porque su forma nos dice mucho sobre las propiedades globales del sistema.

**Definición formal**: $P(k)$ es la probabilidad de que un nodo elegido al azar tenga grado $k$. Equivalentemente, es la fracción de nodos con grado $k$.

**En nuestro ejemplo**: $P(1) = 2/6 = 1/3$ (nodos $E$ y $F$), $P(3) = 4/6 = 2/3$ (nodos $A$–$D$), y $P(k) = 0$ para cualquier otro $k$. Este ejemplo es demasiado pequeño para revelar patrones interesantes, pero cuando analicemos redes de cientos de nodos, la *forma* de $P(k)$ será reveladora.

---

## 4. Topologías de red: ¿qué forma tiene nuestro sistema?

Ahora llegamos al corazón conceptual de este capítulo. No todas las redes son iguales. La ciencia de redes ha identificado tres grandes familias de topologías, cada una con propiedades radicalmente diferentes. Conocer a cuál se parece nuestro sistema eléctrico determina qué vulnerabilidades tiene y qué estrategias de protección funcionan.

### 4.1 Redes aleatorias: Erdős-Rényi

**El modelo**: En 1959, Paul Erdős y Alfréd Rényi propusieron el modelo más simple de red: tome $N$ nodos y conecte cada par posible con una probabilidad $p$, de manera independiente. El resultado es una red donde todos los nodos tienen *aproximadamente* el mismo número de conexiones.

**Distribución de grado**: Sigue una distribución de **Poisson**:

$$P(k) = \frac{e^{-\langle k \rangle} \langle k \rangle^k}{k!}$$

donde $\langle k \rangle = p(N-1)$ es el grado promedio. La distribución es simétrica y concentrada alrededor de la media, con una "cola" que decae exponencialmente rápido. Es extremadamente improbable encontrar un nodo con un grado mucho mayor que el promedio.

**Analogía energética**: Imagine un sistema eléctrico hipotético donde cada subestación tiene más o menos el mismo número de líneas de transmisión — quizá 3, 4 o 5 — y no existen subestaciones "gigantes" que concentren decenas de conexiones. Este sistema sería democrático: ningún nodo es significativamente más importante que los demás.

**Propiedades clave**:
- Todos los nodos son "iguales en importancia"
- Resistente a ataques dirigidos (no hay nodos críticos obvios)
- Pero tampoco tiene la eficiencia de ciertas estructuras jerárquicas

### 4.2 Redes libres de escala: Barabási-Albert

**El modelo**: En 1999, Albert-László Barabási y Réka Albert observaron que muchas redes del mundo real no siguen el modelo aleatorio. En su lugar, descubrieron que tienen unos pocos nodos con un número enormemente alto de conexiones (*hubs*) y muchos nodos con muy pocas conexiones. Propusieron un mecanismo generativo simple: **enlace preferencial** (preferential attachment) — "los ricos se hacen más ricos". Cuando un nuevo nodo se une a la red, es más probable que se conecte a un nodo que ya tiene muchas conexiones.

**Distribución de grado**: Sigue una **ley de potencia** (power law):

$$P(k) \sim k^{-\gamma}$$

donde $\gamma$ es el exponente de la ley de potencia, típicamente entre 2 y 3 para redes reales. En escala logarítmica, esta distribución aparece como una línea recta. A diferencia de la distribución de Poisson, la distribución de ley de potencia tiene una "cola pesada" (fat tail): la probabilidad de encontrar nodos con grados extremadamente altos es mucho mayor de lo que sugeriría una distribución gaussiana o Poisson.

**Analogía energética**: El SIN colombiano tiene características de red libre de escala. Unas pocas subestaciones principales — como Bacatá (500/230 kV), Cerromatoso (500/230 kV), La Virginia (230 kV), San Carlos (500/230 kV) — concentran un número desproporcionadamente alto de conexiones, mientras que la gran mayoría de subestaciones regionales tienen solo 2 o 3 líneas. No es una coincidencia: los sistemas eléctricos crecen por enlace preferencial. Cuando se planifica una nueva línea, es natural conectarla a una subestación existente que ya es un nodo importante del sistema — es más eficiente y más económico que crear infraestructura desde cero en un punto remoto.

**Propiedades clave**:
- **Hubs**: existencia de nodos con grado mucho mayor que el promedio
- **Tolerancia a fallas aleatorias** pero **vulnerabilidad a ataques dirigidos** (esto es la paradoja "robusto pero frágil" que veremos en detalle más adelante)
- Distancias promedio cortas (propiedad de mundo pequeño)

### 4.3 Redes de mundo pequeño: Watts-Strogatz

**El modelo**: En 1998, Duncan Watts y Steven Strogatz propusieron un modelo que captura una propiedad sorprendente de muchas redes reales: tienen **alto clustering** (los vecinos de un nodo tienden a conocerse entre sí) y al mismo tiempo **caminos cortos** entre nodos distantes. Esto se logra comenzando con una red regular (como un anillo donde cada nodo se conecta a sus vecinos más cercanos) y luego "reconectando" aleatoriamente algunas aristas para crear "atajos" de largo alcance.

**Analogía energética**: En el sistema de transmisión, las subestaciones de una misma región (por ejemplo, las del Valle del Cauca) están densamente conectadas entre sí (alto clustering), pero también existen líneas de transmisión de larga distancia (como los corredores 500 kV) que conectan regiones lejanas — estos son los "atajos" que hacen al mundo pequeño. El resultado: cualquier subestación del país puede alcanzar a cualquier otra en relativamente pocos saltos, a pesar de que la red no es densa globalmente.

**Propiedades clave**:
- **Alto clustering + caminos cortos**: lo mejor de ambos mundos
- El alto clustering provee redundancia local
- Los atajos proveen eficiencia global

### 4.4 Comparación de topologías

| Propiedad | Aleatoria (E-R) | Libre de escala (B-A) | Mundo pequeño (W-S) |
|---|---|---|---|
| Distribución de grado | Poisson (simétrica) | Ley de potencia (cola pesada) | Similar a regular pero con atajos |
| Hubs | No | Sí (pocos, muy conectados) | Posibles pero no necesarios |
| Clustering | Bajo | Bajo a medio | **Alto** |
| Camino promedio | Corto | **Muy corto** | Corto |
| Robustez a fallas aleatorias | Media | **Alta** | Media |
| Robustez a ataques dirigidos | Media | **Baja** | Media-alta |

---

## 5. Leyes de potencia y toma de decisiones

Esta sección es un puente conceptual crucial entre la ciencia de redes y la toma de decisiones en el sector energético. Merece atención especial.

### 5.1 ¿Qué es una ley de potencia?

Decimos que una variable aleatoria sigue una **ley de potencia** (power law) si su distribución de probabilidad decrece como una potencia del valor observado:

$$P(X \geq x) \sim x^{-\alpha + 1} \quad \text{o equivalentemente} \quad P(X = x) \sim x^{-\alpha}$$

En contraste, una distribución **gaussiana** (normal) decrece como $e^{-x^2}$ — exponencialmente rápido. La diferencia práctica es enorme:

| Distribución | Probabilidad de un evento 10x más grande que la media |
|---|---|
| Gaussiana | Prácticamente cero ($\sim 10^{-23}$) |
| Ley de potencia ($\alpha = 2.5$) | Aproximadamente $10^{-1.5} \approx 3\%$ |

En una distribución gaussiana, eventos extremos son esencialmente imposibles. En una ley de potencia, son **raros pero no despreciables** — y su impacto puede ser catastrófico.

### 5.2 ¿Por qué importa para los sistemas energéticos?

En la Semana 1 hablamos de los **cisnes negros** (black swans): eventos de baja probabilidad pero alto impacto que los modelos convencionales no anticipan. Ahora podemos darle una base cuantitativa a esa idea.

Considere la distribución de tamaños de apagones en sistemas eléctricos. Estudios empíricos (Carreras et al., 2004; Dobson et al., 2007) han documentado que **la distribución del tamaño de los apagones sigue una ley de potencia**: hay muchos apagones pequeños y pocos grandes, pero los grandes son mucho más frecuentes de lo que una distribución normal predecería. Un apagón que afecta 10 millones de personas no es "10 veces" más raro que uno que afecta 1 millón — es quizá solo 3 veces más raro.

Esto tiene implicaciones profundas para la evaluación de riesgo:

1. **El análisis basado en promedios es engañoso**: El "apagón promedio" es pequeño y manejable. Pero el riesgo total del sistema está dominado por los eventos extremos en la cola de la distribución.

2. **Los métodos estándar subestiman el riesgo**: Si un planificador asume que los tamaños de apagones siguen una distribución normal y estima que un apagón de cierta magnitud tiene una probabilidad de 1 en 10,000 años, la realidad (bajo una ley de potencia) podría ser 1 en 50 años.

3. **El "peor caso razonable" es mucho peor de lo que pensamos**: Los escenarios de estrés diseñados bajo supuestos gaussianos son insuficientes.

### 5.3 El cambio de paradigma: del pensamiento en promedios al pensamiento en colas

La ciencia de redes nos obliga a cambiar nuestra forma de pensar sobre el riesgo:

- **Pensamiento tradicional**: "¿Cuál es la falla más probable? Diseñemos para ella."
- **Pensamiento de colas pesadas**: "¿Cuáles son las fallas que, aunque improbables, serían catastróficas? ¿Qué tan improbables son *realmente*? ¿Estamos seguros de que nuestros modelos de probabilidad son correctos?"

Este cambio de paradigma conecta directamente con la paradoja "robusto pero frágil" que exploraremos a continuación.

---

## 6. La paradoja "robusto pero frágil"

### 6.1 Robustez ante fallas aleatorias

Considere una red libre de escala con hubs prominentes. Si una falla ocurre **al azar** — un cortocircuito, un rayo, un error de mantenimiento —, ¿a qué nodo afectará más probablemente? Dado que la mayoría de los nodos tienen pocas conexiones (recuerde la ley de potencia: muchos nodos de grado bajo, pocos de grado alto), es estadísticamente mucho más probable que la falla afecte a un nodo periférico de grado bajo. Cuando un nodo periférico falla, el impacto en la red global es mínimo: se pierde una conexión marginal, pero la estructura esencial del sistema — sostenida por los hubs — permanece intacta.

Esto se puede cuantificar simulando la remoción aleatoria de nodos: incluso después de remover un porcentaje significativo de nodos al azar (digamos el 20%), la red libre de escala mantiene su conectividad — el componente gigante (el grupo más grande de nodos conectados) apenas se reduce.

### 6.2 Fragilidad ante ataques dirigidos

Ahora considere un escenario diferente: un atacante (o una secuencia desafortunada de eventos correlacionados) que deliberadamente apunta a los **hubs**. Si se remueve el nodo de mayor grado, la red pierde su principal articulador. Si se remueve el segundo hub, se pierde la segunda conexión más importante. Con la remoción de unos pocos hubs (quizá el 5% de los nodos), la red libre de escala se fragmenta completamente en componentes desconectados.

Esta asimetría es la **paradoja "robusto pero frágil"** (robust yet fragile):

> **Las redes libres de escala son extraordinariamente resistentes a fallas aleatorias pero catastróficamente vulnerables a ataques dirigidos contra sus hubs.**

### 6.3 Implicaciones para la seguridad del SIN

Si el SIN colombiano tiene características de red libre de escala — como la evidencia empírica sugiere — entonces:

- **Buena noticia**: El sistema tolerará bien las fallas aleatorias cotidianas (rayos, errores humanos aislados, fallas de equipos individuales). Estas fallas afectarán mayormente a nodos periféricos de bajo grado sin consecuencias sistémicas.

- **Mala noticia**: El sistema es vulnerable a eventos que afecten selectivamente a los hubs. Estos eventos no tienen que ser "ataques" en sentido militar — pueden ser desastres naturales que afecten una región donde se concentran varios hubs (un terremoto en el Eje Cafetero, por ejemplo, podría afectar subestaciones clave como La Virginia y San Carlos), o fallas correlacionadas durante condiciones extremas (El Niño que reduce simultáneamente la generación hidráulica en múltiples embalses conectados a los mismos hubs de transmisión).

---

## 7. El criterio N-1 y sus limitaciones

### 7.1 ¿Qué es el criterio N-1?

En la práctica de planificación y operación del sistema de transmisión colombiano — regulada por la UPME (planificación) y operada por XM —, el criterio más utilizado para evaluar la confiabilidad es el **criterio N-1**:

> **El sistema debe ser capaz de operar de manera segura después de la pérdida de cualquier elemento individual** (una línea, un transformador, una unidad de generación).

Formalmente, si el sistema tiene $N$ elementos, se evalúan $N$ escenarios de contingencia, cada uno removiendo un solo elemento, y se verifica que en ninguno de ellos se produzcan violaciones de límites térmicos, de tensión o de estabilidad.

### 7.2 Lo que el N-1 captura bien

El criterio N-1 es una herramienta probada y valiosa que:

- Identifica elementos cuya pérdida individual causa problemas inmediatos.
- Es computacionalmente manejable: solo requiere $N$ simulaciones de flujo de carga.
- Proporciona un estándar mínimo de confiabilidad que el sistema debe cumplir.
- Es la base de la planificación de expansión del STN en Colombia.

### 7.3 Lo que el N-1 NO captura

Desde la perspectiva de redes complejas, el criterio N-1 tiene limitaciones fundamentales:

1. **Fallas correlacionadas**: El N-1 evalúa la pérdida de **un solo** elemento. Pero en la realidad, las fallas rara vez son independientes. Un evento climático severo puede causar la pérdida simultánea de varias líneas. Las fallas en cascada — donde la falla de un elemento sobrecarga a los vecinos, provocando fallas adicionales — son, por definición, eventos de múltiples elementos. El criterio N-1 no evalúa estas situaciones (el criterio N-2 lo hace parcialmente, pero es exponencialmente más costoso y tampoco captura cascadas largas).

2. **Importancia topológica**: El N-1 evalúa cada elemento con la misma prioridad. Pero como hemos visto, no todos los nodos son iguales en una red libre de escala. La falla de un hub es cualitativamente diferente de la falla de un nodo periférico. El análisis de redes permite **priorizar** qué contingencias N-1 son realmente críticas.

3. **Ataques dirigidos**: El N-1 evalúa fallas *aleatorias* (cualquier elemento). No evalúa la vulnerabilidad ante secuencias estratégicas de fallas que apunten a los nodos topológicamente más críticos. Como vimos en la paradoja "robusto pero frágil", esta es precisamente la vulnerabilidad más peligrosa de las redes libres de escala.

4. **Propagación dinámica**: El N-1 evalúa el estado estacionario después de perder un elemento. No modela la *dinámica* de cómo una falla se propaga y amplifica a través de la red en los segundos y minutos posteriores al evento inicial.

### 7.4 N-1 + redes: una combinación más poderosa

El mensaje no es que el N-1 sea inútil — es que es **necesario pero no suficiente**. El análisis de redes lo complementa de maneras específicas:

- **Priorización**: En vez de evaluar las $N$ contingencias con igual peso, usamos métricas de centralidad para enfocarnos en las contingencias que involucran nodos de alta intermediación.
- **Más allá de N-1**: Simulamos fallas en cascada para evaluar el impacto de la falla de un elemento no solo en los flujos de carga inmediatos, sino en la propagación topológica de sobrecargas.
- **Diseño resiliente**: Usamos el análisis de topología para identificar dónde agregar redundancia (nuevas líneas, nuevas subestaciones) de manera que el sistema sea menos dependiente de hubs individuales.

---

## 8. Fallas en cascada: el modelo capacidad-carga

### 8.1 La intuición

Una falla en cascada ocurre cuando la falla de un componente causa la sobrecarga y posterior falla de otros componentes, que a su vez sobrecargan a más componentes, y así sucesivamente hasta que una fracción significativa del sistema colapsa. Es como una fila de fichas de dominó: la caída de una provoca la caída de la siguiente, pero aquí las "fichas" son nodos de una red y las "caídas" son sobrecargas.

Los apagones masivos más recordados del siglo XXI siguieron exactamente este patrón:

- **Noreste de EE.UU., agosto 2003**: Una línea de transmisión en Ohio tocó un árbol y provocó un cortocircuito. La carga se redistribuyó a líneas vecinas, que se sobrecargaron y fallaron. En menos de 3 horas, una cascada dejó sin electricidad a 55 millones de personas en 8 estados y parte de Canadá.

- **India, julio 2012**: El apagón más grande de la historia afectó a 620 millones de personas en 22 estados. La falla inicial fue una sobrecarga en la red norte que se propagó por cascada a la red este y noreste.

### 8.2 El modelo de Motter-Lai

En 2002, Adilson Motter y Ying-Cheng Lai propusieron un modelo elegante para estudiar fallas en cascada en redes complejas. La idea es sencilla:

1. **Cada nodo tiene una carga y una capacidad**: La carga $L_i$ de un nodo $i$ es proporcional a su importancia topológica, medida por su centralidad de intermediación. La capacidad $C_i$ es la carga máxima que puede soportar, y se define como:

$$C_i = (1 + \alpha) \cdot L_i^{(0)}$$

donde $L_i^{(0)}$ es la carga inicial del nodo y $\alpha > 0$ es un **margen de tolerancia**. Si $\alpha = 0.2$, cada nodo puede soportar un 20% más de carga que su carga inicial.

2. **Cuando un nodo falla, su carga se redistribuye**: Si un nodo es removido de la red (por falla), los caminos más cortos del sistema cambian. Esto modifica la centralidad de intermediación de todos los demás nodos — es decir, su carga cambia.

3. **Si algún nodo excede su capacidad, falla**: Después de la redistribución, si algún nodo $j$ tiene $L_j > C_j$, falla también. Esto provoca otra redistribución, que puede causar más fallas, y así sucesivamente.

### 8.3 Algoritmo de cascada (pseudocódigo)

```
ENTRADA: Grafo G, margen de tolerancia α, nodo_inicial_a_remover

1. Calcular carga inicial L₀(i) = betweenness(i) para todo nodo i
2. Calcular capacidad C(i) = (1 + α) × L₀(i) para todo nodo i
3. Remover nodo_inicial de G
4. nodos_fallados ← {nodo_inicial}

5. REPETIR:
   a. Recalcular cargas: L(i) = betweenness(i) en el grafo modificado
   b. nuevas_fallas ← {i : L(i) > C(i) y i ∉ nodos_fallados}
   c. SI nuevas_fallas está vacío:
        TERMINAR (la cascada se detuvo)
   d. Remover todos los nodos de nuevas_fallas del grafo
   e. nodos_fallados ← nodos_fallados ∪ nuevas_fallas

6. SALIDA: Fracción de nodos supervivientes = 1 − |nodos_fallados| / N
```

### 8.4 ¿Qué revela el modelo?

El modelo de Motter-Lai captura dinámicas esenciales:

- **El margen importa**: Con márgenes altos ($\alpha$ grande), las cascadas se detienen rápidamente porque los nodos tienen capacidad de sobra para absorber la carga redistribuida. Con márgenes bajos, incluso la remoción de un solo nodo puede colapsar toda la red.

- **La topología importa**: En redes libres de escala, la remoción de un hub produce cascadas mucho más devastadoras que la remoción de un nodo periférico — la redistribución de carga del hub es masiva y sobrecarga rápidamente a sus vecinos.

- **La comparación ataque dirigido vs. falla aleatoria es reveladora**: Si simulamos la remoción de nodos al azar y graficamos la fracción de red superviviente, la red libre de escala se degrada gradualmente. Pero si removemos nodos en orden de mayor intermediación (ataque dirigido), la red colapsa abruptamente después de remover solo unos pocos nodos. Esta es la paradoja "robusto pero frágil" vista en acción dinámica.

### 8.5 Limitaciones del modelo

Es importante señalar que el modelo de Motter-Lai es una **abstracción**. Los sistemas eléctricos reales tienen dinámicas mucho más complejas (protecciones, regulación de frecuencia, redespacho, intervención de operadores). Pero el modelo captura la esencia del fenómeno: la interdependencia topológica entre componentes amplifica las fallas. Los modelos más sofisticados de cascadas en redes eléctricas (como los de Carreras, Lynch, Dobson y colaboradores) incorporan flujos de potencia DC o AC, pero la lección fundamental es la misma.

---

## 9. El caso de la semana: el SIN como red

### 9.1 Construyendo el grafo del SIN

El Sistema de Transmisión Nacional (STN) colombiano opera en los niveles de tensión de 500 kV, 230 kV y 110 kV. Para construir su representación como grafo:

- **Nodos**: Cada subestación del STN es un nodo. El sistema tiene más de 80 subestaciones principales en 500 kV y 230 kV, y varios cientos en 110 kV.
- **Aristas**: Cada circuito de transmisión que conecta dos subestaciones es una arista. Las líneas de doble circuito pueden representarse como dos aristas paralelas o como una sola arista con peso doble, dependiendo del análisis.
- **Pesos**: La capacidad térmica de la línea (en MVA o MW) es un peso natural. La impedancia de la línea es otro.

### 9.2 ¿Qué revela el análisis topológico?

Aunque el análisis detallado se realizará en el laboratorio con datos reales, podemos anticipar varios hallazgos basados en la estructura conocida del SIN:

**Distribución de grado**: El STN colombiano probablemente muestra una distribución de grado con cola pesada, con unas pocas subestaciones de grado alto (Bacatá, Cerromatoso, La Virginia, San Carlos, Primavera, Guatiguará) y muchas subestaciones de grado bajo (terminales regionales, subestaciones de paso). Esto es consistente con una red que ha crecido orgánicamente durante décadas, donde las nuevas líneas tienden a conectarse a nodos ya prominentes.

**Centralidad de intermediación**: Las subestaciones que funcionan como "puentes" entre regiones tendrán alta intermediación. Los corredores de transmisión que conectan la Costa Caribe con el interior (a través de subestaciones en Santander y el Bajo Cauca) o que conectan el suroccidente con el centro (a través del Eje Cafetero) son candidatos a contener nodos de alta intermediación. Estos son los **cuellos de botella topológicos** del sistema.

**Clustering**: Las subestaciones dentro de una misma área operativa (por ejemplo, las del área Antioquia o las del área Bogotá) probablemente muestran alto clustering — están densamente conectadas entre sí. Pero la conectividad *entre* áreas depende de pocos corredores de larga distancia.

**La conexión de La Guajira**: La integración de los parques eólicos de La Guajira al SIN es un caso fascinante desde la perspectiva de redes. La Guajira es geográficamente periférica — se conecta al sistema principal a través de un corredor de transmisión relativamente estrecho. Si las líneas colectoras y los circuitos principales (como Colectora–Cuestecitas–Copey) representan los únicos caminos de salida de varios GW de capacidad eólica, entonces:

- El grado de los nodos de conexión será alto (muchos parques alimentando pocas subestaciones colectoras).
- La intermediación de estos nodos será muy alta (todo el flujo de exportación eólica pasa por ellos).
- El clustering local será bajo (los parques se conectan a las colectoras, pero no entre sí).

Esta configuración crea un **punto de falla sistémico**: un evento que afecte la línea colectora principal podría desconectar simultáneamente toda la capacidad eólica de La Guajira del SIN. Este riesgo es difícil de detectar con un análisis N-1 convencional (que evalúa un elemento a la vez), pero es inmediatamente visible en el análisis de centralidad de intermediación.

### 9.3 Preguntas que responde el análisis de redes

| Pregunta de planificación | Herramienta de redes |
|---|---|
| ¿Cuáles son las subestaciones más críticas del SIN? | Centralidad de intermediación + grado |
| ¿Dónde conviene agregar una nueva línea para aumentar la resiliencia? | Análisis de componentes conectados después de remoción de hubs |
| ¿Es la conexión de La Guajira un punto de falla sistémico? | Centralidad de intermediación del corredor colector |
| ¿Cuántos apagones regionales puede tolerar el sistema? | Simulación de cascadas con diferentes márgenes |
| ¿El sistema es más vulnerable a fallas aleatorias o a eventos correlacionados? | Comparación de curvas de robustez (ataque aleatorio vs. dirigido) |
| ¿Cómo cambia la vulnerabilidad del sistema con la expansión planificada? | Recalcular métricas con y sin los proyectos del Plan de Expansión |

### 9.4 Lo que el análisis de redes NO reemplaza

Es fundamental ser honestos sobre los límites de la herramienta. El análisis de redes **no reemplaza** el análisis de flujos de potencia, la simulación de estabilidad transitoria o el estudio de cortocircuitos. Estos análisis consideran la física del sistema eléctrico (impedancias, tensiones, ángulos, potencia reactiva) que el grafo topológico ignora. El análisis de redes opera a un nivel de abstracción más alto: ve la *estructura* de las conexiones, pero no la *física* de los flujos. Su valor está en revelar vulnerabilidades estructurales que la perspectiva componente-por-componente no puede ver, y en complementar — no sustituir — las herramientas tradicionales de ingeniería eléctrica.

---

## 10. Conexión con lo que sigue

### 10.1 La limitación de la foto fija

Todo lo que hemos hecho en este capítulo es análisis **estático**: tomamos una foto de la red tal como es en un instante dado y la analizamos. Pero los sistemas energéticos no son estáticos:

- Las redes de actores evolucionan: nuevos inversionistas entran, reguladores cambian reglas, comunidades se organizan.
- La adopción de tecnologías se difunde a través de las redes sociales.
- Las fallas en cascada son procesos *dinámicos* que ocurren en tiempo real.

### 10.2 La Semana 3: dinámica sobre redes y redes de actores

La próxima semana extenderemos nuestro análisis en dos direcciones:

1. **Dinámica sobre redes**: Los nodos no son solo puntos pasivos — tienen *estados* que cambian en función de los estados de sus vecinos. Estudiaremos modelos de difusión, contagio y adopción tecnológica. ¿Por qué la adopción de techos solares en Colombia no sigue un modelo puramente económico? Porque depende de la estructura de la red social: quién conoce a quién, quién influye a quién, quién confía en quién.

2. **Redes de actores**: Aplicaremos las mismas herramientas de redes a las relaciones entre actores del sistema energético: reguladores (CREG), operadores (XM), generadores, comercializadores, comunidades. Construiremos y analizaremos una red de actores del mercado mayorista colombiano para identificar nodos dominantes y vulnerabilidades institucionales.

### 10.3 Más adelante: la dimensión temporal

En las Semanas 4 y 5, daremos un salto conceptual: pasaremos de *redes* a *dinámica de sistemas*. Las redes nos dicen **cómo está conectado** el sistema; la dinámica de sistemas nos dice **cómo evoluciona en el tiempo**. La combinación de ambas perspectivas — estructura y comportamiento temporal — es lo que hace al análisis sistémico genuinamente poderoso.

---

## 11. Resumen y conceptos para llevar

### Conceptos clave de la semana

1. **Todo es una red**: El SIN es una red, pero también lo son los mercados eléctricos, las relaciones entre actores y las cadenas de suministro. La ciencia de redes proporciona un lenguaje unificado para analizarlas todas.

2. **La topología importa**: La *forma* de las conexiones determina las propiedades del sistema tanto como las capacidades de los componentes individuales.

3. **Las métricas de centralidad identifican nodos críticos**: El grado cuenta conexiones; la intermediación identifica cuellos de botella; la cercanía mide accesibilidad; el clustering mide redundancia local.

4. **La distribución de grado es la métrica más reveladora**: Su forma nos dice si el sistema es democrático (aleatorio) o tiene hubs dominantes (libre de escala).

5. **Las leyes de potencia cambian las reglas**: Los eventos extremos son mucho más frecuentes de lo que las distribuciones normales predicen. Nuestros métodos de evaluación de riesgo deben adaptarse.

6. **La paradoja "robusto pero frágil"**: Las redes con hubs resisten fallas aleatorias pero son vulnerables a ataques dirigidos — exactamente lo opuesto de lo que sugiere la intuición ingenua.

7. **El criterio N-1 es necesario pero no suficiente**: Captura fallas individuales independientes, pero no fallas correlacionadas, cascadas ni ataques dirigidos. El análisis de redes lo complementa.

8. **Las fallas en cascada son procesos topológicos**: La redistribución de carga después de una falla sigue la estructura de la red. El modelo capacidad-carga captura esta dinámica.

9. **La red del SIN revela vulnerabilidades ocultas**: Los corredores de transmisión que conectan regiones y los nodos colectores de generación renovable son puntos de falla sistémicos identificables mediante métricas de centralidad.

10. **Las redes son fotos fijas**: No capturan cómo el sistema evoluciona. Para eso necesitaremos la dinámica sobre redes (Semana 3) y la dinámica de sistemas (Semanas 4–5).

### Glosario de términos

| Término en español | Término en inglés | Definición breve |
|---|---|---|
| Nodo (vértice) | Node (vertex) | Entidad del sistema (subestación, actor, etc.) |
| Arista (enlace) | Edge (link) | Conexión entre dos nodos (línea de transmisión, relación) |
| Grafo | Graph | Conjunto de nodos y aristas |
| Grafo dirigido | Directed graph | Grafo donde las aristas tienen dirección |
| Grafo ponderado | Weighted graph | Grafo donde las aristas tienen un peso numérico |
| Matriz de adyacencia | Adjacency matrix | Representación matricial del grafo |
| Vecino | Neighbor | Nodo directamente conectado |
| Camino | Path | Secuencia de nodos conectados |
| Camino más corto | Shortest path | Camino con el menor número de aristas entre dos nodos |
| Componente conectado | Connected component | Subconjunto de nodos donde todos son alcanzables entre sí |
| Grado | Degree | Número de conexiones de un nodo |
| Centralidad de intermediación | Betweenness centrality | Fracción de caminos más cortos que pasan por un nodo |
| Centralidad de cercanía | Closeness centrality | Inverso de la distancia promedio a todos los demás nodos |
| Coeficiente de clustering | Clustering coefficient | Fracción de pares de vecinos que están conectados entre sí |
| Densidad | Density | Fracción de aristas existentes vs. posibles |
| Diámetro | Diameter | Mayor distancia (camino más corto) entre cualquier par de nodos |
| Distribución de grado | Degree distribution | Histograma de los grados de todos los nodos |
| Ley de potencia | Power law | Distribución de probabilidad $P(k) \sim k^{-\gamma}$ (cola pesada) |
| Red aleatoria | Random network (Erdős-Rényi) | Red donde las conexiones se forman al azar con igual probabilidad |
| Red libre de escala | Scale-free network | Red con distribución de grado de ley de potencia y hubs |
| Red de mundo pequeño | Small-world network | Red con alto clustering y caminos cortos |
| Hub | Hub | Nodo con un número desproporcionadamente alto de conexiones |
| Enlace preferencial | Preferential attachment | Mecanismo: nuevos nodos prefieren conectarse a nodos bien conectados |
| Criterio N-1 | N-1 criterion | El sistema opera seguro tras la pérdida de cualquier elemento individual |
| Falla en cascada | Cascading failure | Falla que se propaga por redistribución de carga en la red |
| Modelo de Motter-Lai | Motter-Lai model | Modelo de cascadas basado en capacidad, carga e intermediación |
| Robusto pero frágil | Robust yet fragile | Propiedad de redes libre de escala: resisten fallas aleatorias pero no ataques dirigidos |

---

### Referencias principales

- Barabási, A.-L. *Network Science*. Cambridge University Press. Disponible en acceso abierto: [networksciencebook.com](http://networksciencebook.com). Capítulos 2–4.
- Pagani, G. A. & Aiello, M. (2013). "The Power Grid as a Complex Network: A Survey." *Physica A*, 392(11), 2688–2700.
- Motter, A. E. & Lai, Y.-C. (2002). "Cascade-based attacks on complex networks." *Physical Review E*, 66, 065102.
- Carreras, B. A., Lynch, V. E., Dobson, I., & Newman, D. E. (2004). "Complex dynamics of blackouts in power transmission systems." *Chaos*, 14(3), 643–652.
- Albert, R., Albert, I., & Nakarado, G. L. (2004). "Structural vulnerability of the North American power grid." *Physical Review E*, 69, 025103.
- UPME. *Plan de Expansión de Referencia — Transmisión*. Versión más reciente disponible.
- XM. Informes de confiabilidad del STN.
- Newman, M. E. J. *Networks: An Introduction*. Oxford University Press. Capítulos 6–8 (recomendada).

---

*En la próxima semana, daremos vida a las redes: estudiaremos cómo los estados se propagan a través de la estructura de la red (difusión, contagio, adopción tecnológica) y construiremos las redes de actores del sistema energético colombiano. La estructura que hoy analizamos como foto fija se convertirá en un escenario donde ocurren procesos dinámicos.*
