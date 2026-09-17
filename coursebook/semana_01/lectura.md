# Semana 1 — ¿Qué es la complejidad y por qué importa en energía?

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

## Del pensamiento lineal al pensamiento complejo en sistemas energéticos

---

## 1. Apertura: ¿Por qué necesitamos pensar diferente?

Imagine que usted es consultor y le piden evaluar la viabilidad de un nuevo parque solar de 200 MW en La Guajira. Usted hace lo que aprendió: proyecta los ingresos con un precio de energía estimado, descuenta los flujos de caja a una tasa apropiada, calcula el Valor Presente Neto (VPN) y la Tasa Interna de Retorno (TIR), y ejecuta un análisis de sensibilidad variando ±20% el precio de la energía, el costo de los módulos y la tasa de descuento. El resultado es positivo: el proyecto es "viable."

Seis meses después, una sequía extrema asociada a El Niño dispara los precios de bolsa. La entrada del parque solar se retrasa por problemas de consulta previa. La línea de transmisión que conectaría el parque al Sistema Interconectado Nacional (SIN) no está lista. Otros generadores térmicos, anticipando la escasez, acumulan gas y elevan sus ofertas. El regulador, presionado políticamente, modifica las reglas del Cargo por Confiabilidad. Los precios oscilan violentamente. El VPN que usted calculó resulta irrelevante — no porque los números estuvieran mal, sino porque el *marco mental* era insuficiente.

Este no es un escenario hipotético. Es, en esencia, lo que ocurrió durante la crisis de El Niño 2015–2016 en Colombia, una crisis que costó billones de pesos, llevó al sistema al borde del racionamiento, y que los modelos convencionales no anticiparon.

### Los límites del análisis convencional

Las herramientas clásicas de evaluación de proyectos —VPN, TIR, análisis de sensibilidad estático, punto de equilibrio— fueron diseñadas para un mundo donde se cumplen ciertas condiciones implícitas:

- **Independencia**: las variables clave (precio, demanda, costo) se mueven de manera relativamente independiente.
- **Proporcionalidad**: un cambio del 10% en un insumo produce un cambio proporcional en el resultado.
- **Estabilidad estructural**: las "reglas del juego" (regulación, tecnologías disponibles, actores) no cambian fundamentalmente durante el horizonte del proyecto.
- **Distribuciones bien comportadas**: los riesgos siguen distribuciones normales (gaussianas) donde los eventos extremos son prácticamente imposibles.

En un sistema energético real, *ninguna* de estas condiciones se cumple plenamente. El precio de la energía en bolsa no es independiente de la hidrología, que no es independiente del clima global (El Niño), que no es independiente de las decisiones de los generadores térmicos, que no son independientes del precio de la energía en bolsa. Estamos ante un *círculo*, no ante una línea recta. Y ese círculo puede amplificarse.

### ¿Por qué los sistemas energéticos son fundamentalmente diferentes?

Un puente, un motor diésel o un circuito electrónico son problemas de ingeniería donde, con suficiente conocimiento de los componentes, podemos predecir el comportamiento del sistema completo. Un sistema energético no funciona así. En el sistema eléctrico colombiano interactúan simultáneamente:

- **Física**: flujos de potencia gobernados por las leyes de Kirchhoff en una red de transmisión de más de 27,000 km.
- **Hidrología y clima**: embalses cuyo nivel depende de patrones climáticos globales como ENSO (El Niño–Southern Oscillation).
- **Mercados**: un mercado mayorista donde generadores ofertan cada hora y los precios se forman por mérito económico.
- **Regulación**: un marco institucional (CREG, XM, UPME, MME) que establece reglas que los agentes interpretan y explotan estratégicamente.
- **Comportamiento humano**: generadores que aprenden, inversionistas que reaccionan a señales de precio, comunidades que se oponen o apoyan proyectos, consumidores que responden (o no) a incentivos.
- **Tecnología**: la entrada acelerada de Fuentes No Convencionales de Energía Renovable (FNCER) que cambia la estructura misma del sistema.

Cuando todos estos elementos interactúan, el resultado no es simplemente la "suma de las partes". El sistema produce comportamientos que ningún componente individual genera por sí solo: oscilaciones de precios, ciclos de inversión, crisis repentinas, transiciones tecnológicas que se aceleran inesperadamente. A estos comportamientos los llamaremos *emergentes*, y su estudio es el corazón de la ciencia de la complejidad.

### El rompecabezas de El Niño 2015–2016

Entre octubre de 2015 y abril de 2016, Colombia enfrentó uno de los episodios de El Niño más intensos registrados. Los niveles de los embalses cayeron por debajo del 30% de su capacidad útil. El precio de bolsa de energía se disparó desde aproximadamente 150 COP/kWh a más de 700 COP/kWh en pocos meses. El país estuvo a semanas del racionamiento — algo que no ocurría desde 1992.

¿Por qué fue tan severa esta crisis? No fue solo la sequía. Fue la *interacción* entre múltiples factores que se reforzaron mutuamente:

1. La reducción de aportes hídricos redujo la generación hidroeléctrica disponible.
2. La mayor demanda de generación térmica elevó el consumo de gas natural y combustibles líquidos.
3. Los generadores térmicos, enfrentando restricciones de suministro de gas, ofertaron a precios más altos.
4. Los precios elevados en bolsa activaron señales de escasez en el mercado.
5. Los generadores hidráulicos, ante la incertidumbre sobre la duración de El Niño, retuvieron agua en los embalses (comportamiento racional individual que agravó la escasez colectiva).
6. El regulador intervino con resoluciones de emergencia que cambiaron las reglas del juego a mitad de la crisis.
7. Cada una de estas respuestas afectó a las demás, creando espirales de retroalimentación.

Ningún modelo lineal — por sofisticado que fuera su análisis de sensibilidad — podía capturar esta cadena de retroalimentaciones, decisiones adaptativas y efectos no lineales. Necesitamos un marco diferente. Ese marco es el **pensamiento complejo** (*complex systems thinking*), y este capítulo es su introducción.

---

## 2. Complicado vs. complejo: la distinción fundamental

Antes de definir formalmente qué es un sistema complejo, necesitamos deshacernos de una confusión común. En el lenguaje cotidiano usamos "complicado" y "complejo" como sinónimos. En la ciencia de sistemas, son categorías radicalmente diferentes.

### Lo complicado: muchas partes, pero predecible

Un **sistema complicado** tiene muchos componentes, pero su comportamiento puede —en principio— predecirse si conocemos todas las partes y sus relaciones. Ejemplos:

- Un **avión Boeing 787**: tiene más de 2.3 millones de componentes, pero cada uno cumple una función específica. Si desmontamos el avión pieza por pieza y lo volvemos a armar, funciona exactamente igual. No hay sorpresas. Los ingenieros pueden predecir su comportamiento con modelos detallados.
- Un **reloj suizo**: miles de engranajes interconectados con precisión extrema. Cada engranaje tiene una función determinada. Si uno falla, sabemos exactamente cuál es el efecto.
- La **resolución de un sistema de ecuaciones lineales grande**: puede tener miles de variables, pero hay un algoritmo para resolverlo y el resultado es determinista.

La palabra clave es *predecible*. Un sistema complicado puede requerir enorme esfuerzo de análisis, pero existe una relación clara entre las partes y el todo. Los expertos pueden descomponerlo, analizarlo por partes, y reconstruir el comportamiento global.

### Lo complejo: interacciones que generan sorpresas

Un **sistema complejo** también tiene muchos componentes, pero aquí las interacciones entre ellos generan comportamientos que no se pueden deducir —ni siquiera en principio— del análisis de los componentes individuales. Ejemplos:

- Una **ciudad**: millones de personas tomando decisiones individuales (dónde vivir, dónde trabajar, qué comprar) producen patrones urbanos (barrios, congestión, gentrificación) que nadie diseñó. No podemos predecir la ciudad estudiando a cada persona por separado.
- Un **ecosistema**: la interacción entre especies, clima y geografía produce dinámicas (extinciones, invasiones, ciclos de población) imposibles de deducir del estudio aislado de cada especie.
- El **tráfico vehicular**: cada conductor toma decisiones racionales individuales (elegir la ruta más rápida), pero el resultado colectivo es un embotellamiento — algo que ningún conductor quiere ni causa individualmente.

| Característica | Complicado | Complejo |
|---|---|---|
| Relación partes-todo | El todo es la suma de las partes | El todo es *más* que la suma de las partes |
| Predicción | Difícil pero posible con suficiente información | Fundamentalmente limitada; sorpresas son normales |
| Respuesta a perturbaciones | Proporcional y localizada | Puede ser desproporcionada y propagarse |
| Descomposición | Se puede analizar por partes y reconstruir | Descomponer destruye las propiedades del sistema |
| Ejemplo canónico | Un avión | Una bandada de pájaros |
| Ejemplo energético | Una turbina de gas (compleja internamente, pero predecible) | El mercado eléctrico colombiano |

### El sistema eléctrico colombiano: ¿complicado o complejo?

El SIN colombiano es, sin duda, **complejo**. ¿Quiénes son los "agentes" (los componentes que interactúan)?

- **Generadores**: ~70 agentes con plantas hidráulicas, térmicas, eólicas y solares, que toman decisiones de oferta cada hora basándose en sus costos, expectativas de precio y estrategia.
- **El operador del sistema (XM)**: despacha la generación por orden de mérito, gestiona restricciones de transmisión, administra el mercado.
- **El regulador (CREG)**: define las reglas del mercado, los cargos, los mecanismos de confiabilidad.
- **El planificador (UPME)**: decide la expansión de transmisión y generación a largo plazo.
- **Los consumidores**: responden (o no) a señales de precio, adoptan (o no) nuevas tecnologías como techos solares.
- **Las comunidades**: en La Guajira, la consulta previa Wayuu es determinante para la viabilidad de proyectos eólicos.
- **El clima**: El Niño y La Niña modulan la disponibilidad hídrica de forma no determinista.
- **Los inversionistas**: responden a señales de rentabilidad con retardos de 3–7 años (el tiempo de construcción de una planta).

¿Qué *interacciones* existen? Los generadores ofertan al mercado. El precio de bolsa depende de las ofertas. Los inversionistas observan los precios para decidir si construir nuevas plantas. La CREG observa el mercado y cambia las reglas. Los generadores se adaptan a las nuevas reglas. El clima afecta los embalses, que afectan las ofertas hidráulicas, que afectan los precios. Las comunidades Wayuu afectan los cronogramas de los proyectos eólicos, que afectan la capacidad futura, que afecta los precios futuros.

¿Qué *emerge*? El precio de bolsa no es diseñado por nadie — emerge de las interacciones entre todos los agentes. Los ciclos de sobreinversión y escasez no son planeados — emergen de los retardos entre la decisión de invertir y la entrada en operación. Las crisis como la de El Niño 2015–2016 no son causadas por un solo factor — emergen de la combinación de retroalimentaciones.

---

## 3. Los conceptos clave de la complejidad

En esta sección presentamos los siete conceptos fundamentales de la complejidad, uno por uno. Para cada concepto seguiremos la misma estructura: primero una explicación intuitiva, luego un ejemplo concreto del sector energético, después una definición más formal, y finalmente las implicaciones para la toma de decisiones.

### 3.1 Retroalimentación (*feedback*)

**Intuición:** Imagine que está en una sala de conferencias con un micrófono conectado a un parlante. Si acerca el micrófono al parlante, el sonido del parlante entra al micrófono, se amplifica, sale por el parlante, vuelve al micrófono, se amplifica más, y en segundos se produce un chirrido ensordecedor. Eso es un ciclo de **retroalimentación positiva** (*positive feedback* o *reinforcing loop*): un efecto que se refuerza a sí mismo.

Ahora imagine el termostato de un aire acondicionado. Cuando la temperatura sube, el termostato enciende el aire frío. El aire frío baja la temperatura. Cuando baja lo suficiente, el termostato apaga el aire. La temperatura sube de nuevo. Eso es un ciclo de **retroalimentación negativa** (*negative feedback* o *balancing loop*): un efecto que se contrarresta y busca un equilibrio.

**Ejemplo energético — el ciclo precio-inversión-capacidad:**

El mercado eléctrico colombiano tiene un ciclo de retroalimentación fundamental:

1. Cuando la demanda crece más rápido que la capacidad instalada, hay escasez relativa → los precios suben.
2. Los precios altos atraen inversión → se inician nuevos proyectos de generación.
3. Después de 3–5 años de construcción, las nuevas plantas entran en operación → la capacidad aumenta.
4. El exceso de capacidad genera sobreoferta → los precios bajan.
5. Los precios bajos desincentivan la inversión → no se construyen nuevas plantas.
6. Mientras tanto, la demanda sigue creciendo → eventual escasez → el ciclo se repite.

Este es un ciclo de retroalimentación negativa (busca el equilibrio entre oferta y demanda), pero el *retardo* de 3–5 años entre la señal de precio y la entrada de nueva capacidad genera oscilaciones. El sistema nunca está en equilibrio: siempre está persiguiéndolo.

**Definición formal:** Una **retroalimentación** es una estructura circular de causalidad en la que la variable de salida de un proceso influye en la variable de entrada del mismo proceso. Un *ciclo de refuerzo* (R) amplifica las desviaciones; un *ciclo de balance* (B) las contrarresta. Formalmente, si tenemos una cadena causal $A \rightarrow B \rightarrow C \rightarrow A$, existe retroalimentación si el efecto neto de una perturbación en $A$, al recorrer todo el ciclo, regresa a $A$ reforzando (R) o contrarrestando (B) la perturbación original.

**Implicación para decisiones:** Cuando interviene en un sistema con retroalimentación, el efecto de su intervención no es lineal ni inmediato. Una política que parece correcta en el corto plazo puede generar efectos perversos en el largo plazo a través de los ciclos de retroalimentación. Por ejemplo, subsidiar la generación térmica durante El Niño resuelve la crisis inmediata, pero puede crear un ciclo de dependencia que desincentiva la diversificación.

### 3.2 No linealidad

**Intuición:** En un sistema lineal, si duplico la causa, duplico el efecto. Si empujo un carrito con el doble de fuerza, se mueve con el doble de velocidad. La vida cotidiana nos entrena a pensar linealmente. Pero muchos fenómenos reales no funcionan así: a veces un pequeño empujón no produce efecto visible, y luego un empujón apenas un poco mayor produce un cambio enorme. Piense en una represa: puede acumular agua sin problema hasta cierto nivel. Un centímetro más y se desborda.

**Ejemplo energético — el gas y las cascadas de costos:**

Considere qué pasa cuando el precio del gas natural se duplica en Colombia. Si el sistema fuera lineal, el costo promedio de generación aumentaría proporcionalmente a la participación del gas en la mezcla (~30%). Pero lo que realmente ocurre es:

1. Los generadores térmicos a gas ofertan más caro → salen del orden de mérito en condiciones normales.
2. Se despachan plantas más costosas (combustibles líquidos) → el precio de bolsa sube mucho más que proporcional.
3. Los generadores hidráulicos, viendo precios altos, elevan el "valor del agua" y retienen agua en embalses para vender a precios futuros aún más altos.
4. La retención reduce la oferta hidráulica disponible → se despachan aún más térmicas costosas.
5. El precio de bolsa se puede multiplicar por 5 o más, no por 2.

El efecto es **no lineal**: una duplicación del precio del gas puede quintuplicar el precio de la energía en bolsa. La relación entre causa y efecto no es proporcional — tiene umbrales, saltos y amplificaciones.

**Definición formal:** Un sistema es **no lineal** cuando la respuesta no es proporcional al estímulo. Matemáticamente, un sistema lineal satisface el principio de superposición: $f(a + b) = f(a) + f(b)$ y $f(\alpha \cdot a) = \alpha \cdot f(a)$. Si cualquiera de estas propiedades se viola, el sistema es no lineal. En la práctica, casi todos los sistemas reales de interés son no lineales; la linealidad es la excepción.

**Implicación para decisiones:** Los análisis de sensibilidad convencionales asumen linealidad implícita: "si el precio del gas varía ±20%, el VPN varía ±X%." Esto es peligrosamente engañoso en sistemas no lineales. Los resultados dependen de *dónde* se está en el espacio de estados. Un cambio del 5% puede no importar en condiciones normales, pero puede ser catastrófico si el sistema ya está cerca de un umbral. Necesitamos herramientas que capturen estas no linealidades — como la dinámica de sistemas (Semanas 4–5).

### 3.3 Emergencia

**Intuición:** Considere una bandada de estorninos al atardecer. Miles de pájaros se mueven en patrones fluidos y coordinados que parecen coreografiados. Pero no hay coreógrafo. Ningún pájaro tiene un plan para la bandada. Cada pájaro sigue tres reglas simples: (1) mantente cerca de tus vecinos, (2) evita chocar con ellos, (3) vuela en la dirección promedio del grupo. De estas reglas individuales simples emerge un patrón colectivo complejo y bello. Ese patrón no existe en ningún pájaro individual — es una propiedad del *sistema*.

**Ejemplo energético — el precio de bolsa como propiedad emergente:**

El precio de la energía en la bolsa del mercado mayorista colombiano no es fijado por nadie. No es una decisión de XM, ni de la CREG, ni de ningún generador individual. Es el resultado de un proceso donde:

- Cada generador presenta una oferta de precio y cantidad para cada hora del día siguiente.
- XM ordena las ofertas de menor a mayor precio (curva de oferta por mérito).
- La oferta que cubre el último kWh de demanda fija el precio para todos.

El precio resultante es una **propiedad emergente**: surge de las interacciones entre los agentes individuales (las ofertas), la estructura del mercado (el mecanismo de despacho por mérito) y las restricciones físicas (disponibilidad hídrica, capacidad de transmisión). Ningún agente individual controla el precio, pero todos lo influyen. Y el precio, a su vez, influye en las decisiones futuras de todos los agentes.

**Definición formal:** Una propiedad es **emergente** cuando pertenece al sistema como un todo y no puede atribuirse a ninguno de sus componentes individuales. Formalmente, si el sistema $S$ está compuesto por los agentes $\{a_1, a_2, ..., a_n\}$, una propiedad $P$ de $S$ es emergente si $P$ no aparece en el análisis de ningún $a_i$ individual ni puede deducirse de la simple suma de propiedades de los $a_i$.

Es importante enfatizar que la emergencia no es mística ni mágica. Tiene **mecanismos concretos**: las reglas de interacción entre los agentes, combinadas con la estructura de sus conexiones y las restricciones del entorno, producen patrones a nivel macro. Si cambiamos las reglas de interacción (por ejemplo, cambiamos el mecanismo de despacho por mérito), cambian las propiedades emergentes (el patrón de precios).

**Implicación para decisiones:** Si el comportamiento del sistema es emergente, no podemos controlarlo directamente. No podemos "fijar" el precio de bolsa ordenándole a cada generador qué ofertar (eso destruiría el mecanismo de mercado). Pero *sí* podemos influir en él cambiando las reglas de interacción — las "reglas del juego." Esto es exactamente lo que hace la regulación. Entender la emergencia nos dice dónde buscar las palancas: no en los componentes individuales, sino en las *reglas de interacción* y la *estructura de conexiones*.

### 3.4 Adaptación y aprendizaje (efectos de memoria)

**Intuición:** Un termostato simple siempre reacciona igual: si la temperatura sube, enfría; si baja, calienta. No tiene memoria, no aprende. Pero los agentes en un sistema energético sí aprenden: recuerdan lo que pasó antes, ajustan sus estrategias, anticipan el futuro basándose en el pasado. Un generador que fue sorprendido por El Niño de 1997–1998 se comportó diferente durante El Niño de 2015–2016. La historia importa.

**Ejemplo energético — generadores que aprenden:**

Después de la crisis de El Niño 1997–1998, que llevó a un racionamiento eléctrico de un año, el sector colombiano introdujo el Cargo por Confiabilidad (CxC) para garantizar respaldo firme. Los generadores aprendieron a valorar la energía firme y a gestionar sus contratos de gas con más cuidado. El regulador aprendió que necesitaba un mecanismo de incentivo para la disponibilidad.

Cuando llegó El Niño 2015–2016, los agentes se comportaron de forma diferente a 1998:

- Algunos generadores habían almacenado combustibles líquidos con anticipación.
- El CxC estaba vigente como mecanismo de respaldo (aunque mostró limitaciones).
- Los generadores hidráulicos gestionaron los embalses con estrategias más conservadoras.
- El regulador intervino más rápidamente con resoluciones de emergencia.

El sistema "recordaba" la crisis anterior. Pero esa memoria no eliminó la crisis — la transformó. Los agentes que habían aprendido de 1998 actuaron de formas que a veces mejoraron y a veces empeoraron la situación de 2016. La adaptación no garantiza mejora; solo garantiza que el sistema no repite exactamente el mismo patrón.

**Definición formal:** Un **sistema adaptativo complejo** (*complex adaptive system*, CAS) es un sistema compuesto por agentes que: (1) tienen *reglas de decisión* que guían su comportamiento, (2) *aprenden* y modifican esas reglas basándose en la experiencia pasada, y (3) sus interacciones producen propiedades emergentes que, a su vez, afectan las condiciones en las que los agentes toman decisiones futuras. Los **efectos de memoria** (*memory effects*) son la manifestación de este aprendizaje: el comportamiento del sistema en el tiempo $t$ depende no solo del estado actual sino de la trayectoria histórica.

**Implicación para decisiones:** Si los agentes se adaptan, las políticas que funcionaron ayer pueden no funcionar mañana. Los agentes aprenden a "jugar" las reglas del regulador. El regulador debe entonces anticipar la adaptación de los agentes y diseñar reglas que sean robustas ante comportamiento estratégico — un problema fundamentalmente diferente al de diseñar un puente o un circuito.

### 3.5 Cisnes negros y eventos extremos

**Intuición:** Antes del descubrimiento de Australia, todos los cisnes observados en Europa eran blancos. La afirmación "todos los cisnes son blancos" parecía sólida — confirmada por millones de observaciones. Bastó un solo cisne negro para refutarla. Nassim Nicholas Taleb usa esta metáfora para describir eventos qué son: (1) raros e inesperados, (2) de enorme impacto, y (3) retrospectivamente explicables (después de que ocurren, todos dicen "era obvio").

En estadística, la distribución normal (gaussiana) predice que los eventos extremos son extraordinariamente raros. Si los precios de bolsa siguieran una distribución normal, un precio 5 desviaciones estándar por encima de la media debería ocurrir cada 14,000 años. En la práctica, en el mercado eléctrico colombiano, estos eventos ocurren cada pocos años. ¿Por qué? Porque los precios de bolsa no siguen una distribución normal — siguen distribuciones de **colas pesadas** (*fat tails*), donde los eventos extremos son mucho más frecuentes de lo que la estadística convencional predice.

**Ejemplo energético — El Niño 2015–2016 como cisne negro:**

Los modelos de riesgo del sector eléctrico colombiano utilizaban escenarios hidrológicos basados en la serie histórica de aportes. El Niño de 2015–2016 resultó ser uno de los tres más intensos desde que se tienen registros. Los precios de bolsa alcanzaron niveles que los modelos de riesgo convencionales consideraban "virtualmente imposibles." Si se hubiera modelado la distribución de precios como gaussiana, la probabilidad de observar los precios de febrero-marzo de 2016 habría sido del orden de $10^{-6}$ — una en un millón. Pero ocurrió.

La razón es que las retroalimentaciones positivas del sistema (las espirales descritas en la sección anterior) amplifican las perturbaciones extremas. La distribución resultante no es gaussiana; tiene colas pesadas. En lenguaje técnico, exhibe **curtosis excesiva** (*leptokurtosis*): los eventos extremos son más probables de lo que esperaríamos bajo supuestos gaussianos.

**Definición formal:** Un **cisne negro** (Taleb, 2007) es un evento que cumple tres criterios: (1) está fuera del rango de las expectativas normales basadas en la experiencia previa; (2) tiene un impacto extremo; y (3) la naturaleza humana busca explicaciones *ex post* que lo hacen parecer predecible en retrospectiva. Estadísticamente, los cisnes negros son síntomas de distribuciones con **colas pesadas** (*heavy-tailed distributions*), donde la probabilidad de eventos extremos decae más lentamente que en una gaussiana. Una distribución de colas pesadas común es la **ley de potencia** (*power law*): $P(X > x) \propto x^{-\alpha}$, donde $\alpha$ es el exponente de la cola. (Nota: en la Semana 2, cuando apliquemos leyes de potencia a distribuciones de grado en redes, usaremos la convención $P(k) \sim k^{-\gamma}$, donde $\gamma$ es el exponente del grado. Son la misma familia matemática en contextos distintos.) Volveremos a las leyes de potencia en la Semana 2 cuando analicemos redes.

**Implicación para decisiones:** Si su análisis de riesgo asume una distribución gaussiana, está subestimando sistemáticamente la probabilidad de eventos catastróficos. En el sector energético colombiano, esto tiene consecuencias concretas: subvalorar el riesgo de sequías extremas, de fallas en cascada del sistema de transmisión, o de crisis de suministro de gas. La gestión del riesgo en sistemas complejos requiere abandonar la distribución normal como supuesto por defecto y trabajar con distribuciones que reconozcan la existencia de colas pesadas. En la Semana 5, cuando abordemos la toma de decisiones bajo incertidumbre profunda, retomaremos este punto.

**Evidencia empírica (Saga 0 — Radiografía de Datos):** El análisis de 25 años de precios de bolsa del SIN colombiano confirma esta hipótesis con datos reales. Los precios diarios muestran una curtosis de 22.2 (vs. 3 para una distribución gaussiana) y un ratio max/min de 131x. El precio máximo histórico (~2,800 COP/kWh, El Niño 2015) es 15 veces mayor que el promedio histórico (180 COP/kWh). Un analista que modele los precios como gaussianos subestimaría la probabilidad de crisis por un factor considerable. Este resultado empírico será el punto de partida para el modelo de dinámica de sistemas (Semana 4).

### 3.6 Dependencia del camino y *lock-in*

**Intuición:** ¿Por qué el teclado de su computador tiene las letras organizadas en el orden QWERTY? No es porque sea la disposición más eficiente — de hecho, existen disposiciones (como Dvorak) que permiten escribir más rápido. El teclado QWERTY fue diseñado en la década de 1870 para *evitar* que las barras mecánicas de las máquinas de escribir se trabaran, separando las letras más frecuentes. Ese problema desapareció con los teclados electrónicos, pero para entonces ya había millones de personas entrenadas en QWERTY, millones de teclados fabricados, y un ecosistema completo que hacía prohibitivamente costoso cambiar. El sistema quedó *atrapado* (*locked in*) en una solución subóptima por una decisión tomada 150 años atrás.

**Ejemplo energético — el *lock-in* térmico en Colombia:**

Colombia tiene un enorme potencial de energía renovable: uno de los mejores recursos solares de América Latina en La Guajira y los Santanderes, y un recurso eólico de clase mundial en La Guajira. Sin embargo, la matriz de generación sigue teniendo una componente térmica significativa (~30% de la capacidad instalada), y el Cargo por Confiabilidad ha sido históricamente más favorable para plantas térmicas que para renovables.

¿Por qué? Dependencia del camino:

1. En la década de 1990, tras la privatización del sector, se invirtió fuertemente en plantas térmicas a gas porque era la tecnología más competitiva en ese momento.
2. Se construyó infraestructura de gasoductos para abastecer esas plantas.
3. Se diseñó el CxC con métricas de energía firme que favorecían a las plantas que podían garantizar generación constante (térmicas) sobre las intermitentes (renovables).
4. Se crearon contratos de largo plazo de suministro de gas y de energía firme.
5. Se formó un ecosistema de empresas, empleos, conocimientos y lobbies alrededor de la generación térmica.

Cada decisión reforzó las anteriores. Hoy, cambiar hacia renovables requiere no solo que las renovables sean más baratas (ya lo son), sino deshacer todo ese ecosistema: renegociar contratos, rediseñar el CxC, construir nueva infraestructura de transmisión, reentrenar personal, superar la resistencia de los actores incumbentes. El sistema está *locked in*.

**Definición formal:** Existe **dependencia del camino** (*path dependence*) cuando el estado actual del sistema no puede entenderse únicamente a partir de las condiciones presentes; la historia de decisiones pasadas y eventos pasados condiciona el rango de opciones disponibles hoy. Un sistema está en ***lock-in*** cuando los costos de transición hacia una alternativa superior son tan altos que el sistema permanece en un estado subóptimo, reforzado por rendimientos crecientes de adopción (*increasing returns*), infraestructura hundida (*sunk infrastructure*), y complementariedades institucionales.

**Implicación para decisiones:** La dependencia del camino implica que *cuándo* se toma una decisión importa tanto como *qué* decisión se toma. Las decisiones de hoy no solo afectan el presente — moldean el espacio de posibilidades futuras. Invertir en infraestructura de gas natural hoy puede parecer económicamente eficiente a corto plazo, pero puede dificultar la transición renovable durante décadas. El análisis de proyectos debe considerar explícitamente el riesgo de *lock-in*.

### 3.7 Puntos de inflexión (*tipping points*)

**Intuición:** Imagine que empuja una bola que está en la cima de una colina. Si la empuja un poco, la bola se queda donde está (más o menos). Si la empuja un poco más, sigue sin moverse mucho. Pero hay un punto — el borde de la colina — donde un empujón apenas perceptible más hace que la bola caiga al otro lado y ruede sin detenerse. El sistema pasa de un estado (estable en la cima) a otro cualitativamente diferente (rodando valle abajo). Ese punto es un **punto de inflexión** (*tipping point*).

**Ejemplo energético — la curva de adopción solar:**

La adopción de energía solar distribuida en muchos mercados ha seguido un patrón no lineal. Durante años, la penetración solar crece lentamente: los paneles son caros, pocos los conocen, la regulación no los favorece. Pero hay un punto donde confluyen tres factores:

1. El costo de los paneles cae por debajo de un umbral de paridad con la red (*grid parity*).
2. Suficientes vecinos instalan paneles como para que la tecnología se vuelva socialmente visible y confiable (contagio social).
3. La regulación se adapta para permitir medición neta (*net metering*) o esquemas equivalentes.

Cuando estos tres factores coinciden, la adopción pasa de crecimiento lento a exponencial. En Alemania, la Energiewende mostró exactamente este patrón: años de crecimiento modesto en los 2000 seguidos de una explosión de capacidad solar entre 2010 y 2013 que transformó la matriz energética más rápido de lo que cualquier planificador había previsto.

Otro ejemplo: el retiro de plantas de carbón. Cuando los costos de operación del carbón superan cierto umbral (por impuestos al CO₂, caída de precios renovables o presión regulatoria), no se retira una planta: se desencadena un efecto cascada donde el retiro de cada planta reduce las economías de escala del suministro de carbón, encarece las plantas restantes, y acelera el retiro de la siguiente. El sistema "pivota" de un régimen a otro.

**Definición formal:** Un **punto de inflexión** (*tipping point*) es un umbral crítico en un parámetro o variable de estado del sistema, más allá del cual el sistema transita de un régimen de comportamiento a otro cualitativamente diferente, a menudo de forma irreversible o muy difícil de revertir. Formalmente, puede modelarse como una **bifurcación** en un sistema dinámico: un valor del parámetro $p$ en el que la estructura cualitativa de las soluciones del sistema $\dot{x} = f(x, p)$ cambia.

**Implicación para decisiones:** Los puntos de inflexión implican que los cambios no son siempre graduales. Una política que parece tener un efecto marginal puede estar acercando el sistema al borde de un tipping point. Y una vez cruzado, el cambio puede ser irreversible. Esto tiene dos caras: el riesgo de cruzar un tipping point negativo (como un colapso de suministro) y la oportunidad de *catalizar* un tipping point positivo (como la adopción masiva de renovables). En la Semana 5, veremos cómo identificar estos puntos con modelos de dinámica de sistemas.

---

## 4. El Diagrama de Lazos Causales (CLD): primera herramienta

Ahora que tenemos el vocabulario de la complejidad, necesitamos una herramienta para *visualizar* la estructura de un sistema complejo. Esa herramienta es el **Diagrama de Lazos Causales** (*Causal Loop Diagram*, CLD), también conocido como mapa causal o diagrama causal. Es la primera —y más accesible— herramienta del pensamiento sistémico.

### ¿Qué es un CLD y por qué es útil?

Un CLD es un diagrama que muestra las relaciones causales entre las variables de un sistema y los ciclos de retroalimentación que generan. No es un modelo cuantitativo (no calcula nada), pero es extraordinariamente poderoso como herramienta de *pensamiento*: nos obliga a hacer explícitas las relaciones que intuimos, a identificar los ciclos de retroalimentación, y a comunicar nuestra comprensión del sistema a otros.

En las Semanas 4 y 5, transformaremos los CLDs en modelos cuantitativos de dinámica de sistemas (con stocks, flujos y ecuaciones). Pero el CLD viene primero porque captura la *estructura causal* del sistema antes de que nos perdamos en los detalles numéricos.

### Notación

Un CLD utiliza tres elementos:

**1. Variables:** Representadas con texto. Son magnitudes que pueden aumentar o disminuir. Ejemplos: *Precio de Bolsa*, *Nivel de Embalses*, *Inversión en Nuevas Plantas*, *Demanda Eléctrica*.

**2. Flechas con polaridad:** Una flecha de $A$ hacia $B$ indica que $A$ influye causalmente en $B$. La polaridad indica *cómo*:
- **Flecha con signo (+):** Si $A$ aumenta, $B$ tiende a aumentar (y si $A$ disminuye, $B$ tiende a disminuir). La relación es *en el mismo sentido*. Ejemplo: si aumenta la *Demanda Eléctrica*, aumenta el *Precio de Bolsa* (+).
- **Flecha con signo (−):** Si $A$ aumenta, $B$ tiende a disminuir (y viceversa). La relación es *en sentido contrario*. Ejemplo: si aumenta el *Nivel de Embalses*, disminuye el *Precio de Bolsa* (−), porque hay más agua disponible para generar.

> **Nota importante:** La polaridad indica la *dirección* de la influencia *ceteris paribus* (todo lo demás constante), no la dirección del cambio en un momento dado.

**3. Identificación de lazos:** Cuando las flechas forman un ciclo cerrado, se identifica con una etiqueta:
- **R (Refuerzo):** El ciclo amplifica los cambios. Se identifica cuando el número de flechas negativas en el ciclo es *par* (0, 2, 4...). Un ciclo R produce crecimiento exponencial (si el ciclo se activa en dirección positiva) o colapso exponencial (si se activa en dirección negativa).
- **B (Balance):** El ciclo se opone a los cambios y busca un equilibrio. Se identifica cuando el número de flechas negativas en el ciclo es *impar* (1, 3, 5...). Un ciclo B produce búsqueda de meta (*goal-seeking*), es decir, el sistema tiende hacia un valor estable.

### Cómo leer un CLD: trazar la historia

La clave para leer un CLD no es mirarlo como un diagrama estático, sino *recorrer las flechas contando una historia*. Comience en una variable, suponga que cambia, y siga las flechas preguntándose: "si esta variable aumenta, ¿qué pasa con la siguiente?"

**Ejemplo simple — el ciclo básico del mercado eléctrico:**

```
  Demanda Eléctrica ──(+)──→ Precio de Bolsa ──(+)──→ Inversión
        ↑                                                  │
        │                                                  │
        │              (retardo: 3-5 años)                 │
        │                                                  ↓
        └───────(−)──── Capacidad Instalada ←──(+)─── Construcción
```

Leamos la historia:
1. Si *Demanda Eléctrica* aumenta → *Precio de Bolsa* aumenta (+).
2. Si *Precio de Bolsa* aumenta → *Inversión* aumenta (+).
3. Si *Inversión* aumenta → *Construcción* de proyectos aumenta (+).
4. Si *Construcción* aumenta → *Capacidad Instalada* aumenta (+), pero con un retardo de 3–5 años.
5. Si *Capacidad Instalada* aumenta → la escasez relativa disminuye, y *Demanda Eléctrica* no cubierta disminuye (−) — o más precisamente, la brecha entre oferta y demanda que impulsa los precios disminuye.

Contemos las flechas negativas: hay una (−). Número impar → es un **ciclo de Balance (B)**. El sistema busca equilibrar oferta y demanda. Pero el retardo de 3–5 años entre inversión y entrada en operación causa que el sistema *oscile* alrededor del equilibrio en vez de converger suavemente.

### Ejemplo: CLD de la crisis de El Niño 2015–2016

Construyamos paso a paso un CLD que capture las dinámicas principales de la crisis. Empezamos con las variables clave:

**Variables del CLD:**
- Aportes Hídricos (nivel de lluvias que alimentan los embalses)
- Nivel de Embalses
- Generación Hidráulica Disponible
- Precio de Bolsa
- Generación Térmica Requerida
- Demanda de Gas Natural
- Precio del Gas
- Valor del Agua Percibido (expectativa de los generadores hidráulicos sobre el valor futuro del agua en embalses)
- Retención de Agua (decisión de los generadores de guardar agua para después)
- Intervención Regulatoria
- Confianza del Público

**Lazo B1 — Balance hídrico normal:**
Aportes Hídricos →(+) Nivel de Embalses →(+) Generación Hidráulica Disponible →(−) Precio de Bolsa →(−) Generación Térmica Requerida →(−) Demanda de Gas Natural. Este es el funcionamiento normal: cuando llueve, los embalses suben, se genera más hidráulica, los precios bajan, y se necesita menos térmica. Ciclo de balance que busca el equilibrio.

**Lazo R1 — Espiral de escasez (refuerzo):**
Precio de Bolsa →(+) Valor del Agua Percibido →(+) Retención de Agua →(−) Generación Hidráulica Disponible →(−) Precio de Bolsa. Leamos: si el precio sube, los generadores hidráulicos perciben que el agua vale más (podrían vender más caro después), retienen agua, lo que reduce la generación hidráulica disponible *ahora*, lo que sube el precio aún más. Dos flechas negativas (par) → **ciclo de Refuerzo (R)**. Este es el ciclo perverso que amplificó la crisis.

**Lazo R2 — Espiral térmica:**
Precio de Bolsa →(+) Generación Térmica Requerida →(+) Demanda de Gas Natural →(+) Precio del Gas →(+) Costos de Generación Térmica →(+) Precio de Bolsa. Cuando suben los precios, se despacha más térmica, lo cual sube la demanda (y el precio) del gas, lo cual encarece la generación térmica, lo cual sube los precios de bolsa. Cero flechas negativas → **ciclo de Refuerzo (R)**.

**Lazo B2 — Intervención regulatoria:**
Precio de Bolsa →(+) Presión Política →(+) Intervención Regulatoria →(−) Precio de Bolsa. Cuando los precios se disparan, la presión política lleva al regulador a intervenir (resoluciones de emergencia, topes de precio, obligaciones de generación), lo que reduce los precios. Ciclo de Balance. Pero la intervención llega con *retardo* y puede tener efectos secundarios no deseados.

**El disparador externo:**
El fenómeno de El Niño reduce los *Aportes Hídricos*. Esto no es parte de un ciclo interno del sistema — es una perturbación externa que activa los ciclos. Pero la severidad de la crisis no se explica por la perturbación sola; se explica por los ciclos de refuerzo R1 y R2 que amplifican la perturbación.

### Errores comunes en la construcción de CLDs

1. **Confundir correlación con causalidad:** Una flecha en un CLD debe representar una relación *causal*, no una mera correlación. Que dos variables se muevan juntas no significa que una cause la otra.

2. **Olvidar la pregunta "¿en el mismo sentido o en sentido contrario?":** La polaridad debe verificarse siempre con la pregunta: "Si A aumenta, *ceteris paribus*, ¿B aumenta (+) o disminuye (−)?"

3. **Incluir demasiadas variables:** Un CLD útil captura las variables y relaciones *esenciales*. Un CLD con 50 variables es ilegible y no aclara nada. Empezar con 5–8 variables y expandir según sea necesario.

4. **Olvidar los retardos:** Muchas relaciones causales no son instantáneas. El retardo entre inversión y capacidad instalada (3–5 años) es crucial para entender las oscilaciones. Los retardos se indican con dos líneas paralelas cruzando la flecha (‖).

5. **Confundir variables con acciones:** Las variables de un CLD son *magnitudes que pueden aumentar o disminuir* (Precio, Capacidad, Demanda), no acciones (construir, ofertar, regular). Las acciones son los mecanismos *detrás* de las flechas.

---

## 5. El caso de la semana: La crisis de El Niño 2015–2016

### Narrativa detallada

El fenómeno de El Niño es un calentamiento anómalo de las aguas superficiales del Océano Pacífico ecuatorial que reduce las precipitaciones en la región Andina colombiana. Colombia, con aproximadamente el 70% de su generación eléctrica proveniente de fuentes hidráulicas, es particularmente vulnerable a este fenómeno.

**Cronología de la crisis:**

*Julio–septiembre 2015:* Las agencias meteorológicas internacionales confirman un episodio de El Niño en desarrollo, con pronósticos de intensidad entre fuerte y muy fuerte. Los embalses del SIN comienzan a descender. Los aportes hídricos caen al 60% de la media histórica.

*Octubre–diciembre 2015:* Los embalses caen por debajo del 50% de su capacidad útil agregada. XM activa protocolos de seguimiento reforzado. Los precios de bolsa, que habían estado alrededor de 150–200 COP/kWh, superan los 300 COP/kWh. El gobierno declara alerta naranja.

*Enero–marzo 2016:* Los aportes hídricos alcanzan mínimos históricos en varias cuencas. Los embalses caen por debajo del 30%. Los precios de bolsa superan los 500 COP/kWh, llegando a picos superiores a 700 COP/kWh. Se presentan restricciones de suministro de gas natural. Varias plantas térmicas no pueden arrancar o tienen que operar con combustibles líquidos (diésel, fuel oil) mucho más costosos. Se habla abiertamente de un posible racionamiento.

*Abril–mayo 2016:* Las lluvias regresan gradualmente. Los embalses comienzan a recuperarse. Los precios se normalizan lentamente. Colombia evitó el racionamiento, pero apenas.

**Datos clave (fuente: XM, informes operativos 2015–2016):**
- El precio promedio de bolsa de 2015 fue ~180 COP/kWh; en el primer trimestre de 2016 superó los 450 COP/kWh.
- Los embalses agregados tocaron fondo alrededor del 27% de capacidad útil en marzo de 2016.
- La generación térmica pasó de cubrir ~20% de la demanda a más del 45% en los meses pico de la crisis.
- El sobrecosto para el sistema fue estimado en varios billones de pesos.

### ¿Por qué falló el análisis convencional?

Los modelos de planificación del sector (como los de UPME y XM) utilizaban escenarios hidrológicos basados en series históricas y simulaciones estocásticas con distribuciones que subestimaban la probabilidad de sequías extremas. Los análisis de riesgo de los generadores utilizaban VPN con sensibilidades que no capturaban las retroalimentaciones entre precios, retención hídrica y restricciones de gas.

Las razones fundamentales del fallo:

1. **No capturaban los ciclos de retroalimentación:** Los modelos trataban cada variable (hidrología, precios, generación térmica) de forma relativamente independiente, sin modelar los ciclos R1 y R2 descritos arriba.
2. **Asumían distribuciones gaussianas:** La probabilidad de aportes tan bajos como los observados era considerada negligible bajo las distribuciones calibradas con la serie histórica "normal".
3. **No modelaban la adaptación de los agentes:** Los generadores no son autómatas; cambian su comportamiento ante la crisis (retención de agua, acaparamiento de gas). Estos comportamientos estratégicos amplificaron la crisis.
4. **Ignoraban los efectos no lineales:** La relación entre nivel de embalses y precio no es lineal. Por debajo de cierto umbral (~35–40%), la relación se vuelve exponencial porque la escasez percibida se amplifica.

### Análisis a través del lente de la complejidad

Ahora veamos cómo cada concepto de la Sección 3 se manifiesta en la crisis:

| Concepto | Manifestación en la crisis |
|---|---|
| **Retroalimentación** | Lazo R1 (espiral de escasez: precio ↑ → retención de agua ↑ → menos hidro disponible → precio ↑). Lazo R2 (espiral térmica: precio ↑ → más térmica → más demanda de gas → gas más caro → precio ↑). |
| **No linealidad** | La relación embalse-precio es exponencial por debajo del 35%. Un 5% menos de embalse puede duplicar el precio. |
| **Emergencia** | El nivel de precios de crisis no fue decidido por nadie — emergió de las interacciones de todos los agentes. |
| **Adaptación** | Los generadores hidráulicos retuvieron agua (aprendieron de crisis anteriores que el agua sería más valiosa después). Los térmicos buscaron contratos spot de gas. El regulador emitió resoluciones de emergencia. |
| **Cisne negro** | La intensidad de El Niño 2015–2016 fue una de las tres mayores registradas. Los modelos estándar no asignaban probabilidad significativa a ese escenario. |
| **Dependencia del camino** | La dependencia del sector de ~70% hidro (decisión histórica desde los 1960s-70s) determinó la vulnerabilidad. El *lock-in* en una matriz hidroeléctrica hizo al sistema estructuralmente frágil ante sequías. |
| **Tipping point** | Hubo un umbral de embalses (~28–30%) por debajo del cual la retención hídrica se volvió masiva y los precios entraron en espiral. Si se hubiera cruzado un umbral inferior, el racionamiento habría sido inevitable. |

---

## 6. Tour de casos internacionales

La complejidad no es exclusiva del sistema colombiano. Los siguientes casos internacionales ilustran cada uno de los conceptos de este capítulo y demuestran que las lecciones son universales.

### Blackout del Noreste de EE.UU. (agosto 2003): fallas en cascada

El 14 de agosto de 2003, un apagón dejó sin electricidad a 55 millones de personas en el noreste de Estados Unidos y Canadá durante hasta 48 horas. La causa inicial fue trivial: unas líneas de transmisión en Ohio tocaron ramas de árboles no podadas. Pero el sistema de alarmas de la empresa FirstEnergy estaba caído (un *bug* de software), así que nadie detectó las fallas iniciales. La carga se redistribuyó a otras líneas, que se sobrecargaron y desconectaron, redistribuyendo la carga a las líneas restantes, que se sobrecargaron a su vez. En menos de 9 segundos, una falla local se propagó como una avalancha a través de la red de transmisión de todo el noreste del continente. Este caso ilustra la propiedad de los sistemas complejos en red de ser **robustos pero frágiles** (*robust-yet-fragile*): la red de transmisión es extremadamente robusta ante fallas aleatorias (un transformador aleatorio que falla no afecta al sistema), pero es frágil ante fallas en nodos críticos o ante *secuencias* específicas de fallas que activan cascadas.

### Blackout de India (julio 2012): escala y fragilidad

El 30 y 31 de julio de 2012, India sufrió los dos apagones más grandes de la historia. El primero afectó a 350 millones de personas; el segundo, al día siguiente, a 620 millones — casi el 10% de la población mundial. La causa combinó sobredemanda por una ola de calor, extracción excesiva de energía por parte de estados del norte que violaban sus cuotas asignadas, y una red de transmisión operando al límite de su capacidad. Este caso ilustra cómo la **escala** de un sistema complejo interconectado amplifica las consecuencias de fallas: un sistema que conecta a 1,300 millones de personas tiene modos de falla cualitativamente diferentes a uno que conecta a 50 millones. La interconexión que en tiempos normales permite compartir recursos eficientemente se convierte, en tiempos de estrés, en el canal por el que se propagan las fallas.

### Blackout de España y Portugal (abril 2025): interdependencia

El 28 de abril de 2025, un apagón masivo afectó a España y Portugal, dejando sin electricidad a aproximadamente 60 millones de personas durante varias horas. El evento, aún bajo investigación, ocurrió en un contexto de alta penetración de energía renovable variable (solar y eólica), desconexión de la interconexión con Francia, y una posible caída abrupta de generación solar combinada con oscilaciones de frecuencia que los mecanismos de inercia reducida del sistema no pudieron absorber. Este caso ilustra la **interdependencia** entre la transformación de la matriz energética y la estabilidad del sistema: la transición hacia renovables cambia la *naturaleza física* del sistema (menor inercia rotacional, mayor variabilidad) y crea nuevas vulnerabilidades que requieren nuevas soluciones sistémicas, no solo más capacidad instalada.

### La Energiewende alemana: no linealidad y tipping points en la adopción solar

Alemania inició su "giro energético" (*Energiewende*) en 2000 con la Ley de Energías Renovables (EEG), que estableció tarifas de alimentación (*feed-in tariffs*) garantizadas para energía solar. Durante la primera década, la penetración solar creció modestamente. Pero alrededor de 2010, la caída de costos de los módulos fotovoltaicos (que habían bajado ~75% en una década) cruzó un umbral de rentabilidad, y la adopción se aceleró dramáticamente: entre 2010 y 2013, Alemania instaló más capacidad solar que en toda la década anterior. Este caso ilustra un **tipping point** clásico: años de crecimiento lento seguidos de una transición explosiva cuando se cruza un umbral. También muestra la **no linealidad** de las transiciones: la reducción del subsidio que acompañó la caída de costos no frenó la adopción proporcionalmente, porque para entonces el ecosistema de instaladores, financiamiento y demanda social ya tenía masa crítica.

### Lock-in del gas natural en Colombia: dependencia del camino

Como discutimos en la Sección 3.6, Colombia desarrolló una infraestructura significativa de generación termoeléctrica a gas natural a partir de la década de 1990. Los gasoductos, las plantas, los contratos de suministro, las regulaciones (incluyendo el Cargo por Confiabilidad), los empleos y el conocimiento técnico generaron un ecosistema que se refuerza a sí mismo. Aun cuando las FNCER son ahora competitivas en costo, la transición enfrenta barreras sistémicas: falta de líneas de transmisión desde La Guajira, reglas del CxC diseñadas para firme térmico, contratos de largo plazo vigentes, y una cultura sectorial familiarizada con la operación térmica. Este caso colombiano es un ejemplo de **dependencia del camino y *lock-in*** con implicaciones directas para los proyectos de los estudiantes del curso.

---

## 7. Mapa del curso: de la intuición a las herramientas

Esta semana hemos construido una intuición cualitativa sobre la complejidad y sus conceptos clave. Hemos aprendido a "ver" retroalimentaciones, no linealidades, emergencia, adaptación, cisnes negros, dependencia del camino y tipping points en los sistemas energéticos. Y hemos introducido el CLD como primera herramienta para hacer visible la estructura del sistema.

Pero la intuición y los CLDs no son suficientes para tomar decisiones. Necesitamos herramientas cuantitativas que nos permitan:

1. **Analizar la estructura de las conexiones** del sistema (¿qué componentes están conectados? ¿cuáles son críticos? ¿qué pasa si falla uno?).
2. **Simular el comportamiento en el tiempo** del sistema (¿cómo evolucionan los precios, la capacidad, los embalses bajo diferentes escenarios y políticas?).

Para la primera necesidad, usaremos **análisis de redes complejas** (Semanas 2 y 3). Para la segunda, usaremos **dinámica de sistemas** (Semanas 4 y 5). El curso se estructura así:

```
SEMANA 1: Complejidad (vocabulario, intuición, CLD)
    ↓
    Lo cualitativo es necesario, pero no suficiente.
    Necesitamos formalizar la ESTRUCTURA y el COMPORTAMIENTO.
    ↓
┌──────────────────────────────┬──────────────────────────────────┐
│  SEMANAS 2–3: REDES          │  SEMANAS 4–5: DINÁMICA           │
│  (Estructura)                │  (Comportamiento en el tiempo)   │
│                              │                                  │
│  ¿Cómo están conectados     │  ¿Cómo cambian las variables     │
│  los componentes?            │  en el tiempo?                   │
│                              │                                  │
│  ¿Qué nodos son críticos?   │  ¿Qué produce las oscilaciones?  │
│                              │                                  │
│  ¿Cómo se propagan fallas   │  ¿Qué efecto tiene una política? │
│  o innovaciones?             │                                  │
│                              │  ¿Qué escenarios son posibles?   │
│  Herramientas: grafos,       │                                  │
│  métricas, centralidad,      │  Herramientas: stocks, flujos,   │
│  leyes de potencia,          │  ecuaciones diferenciales,       │
│  fallas en cascada           │  simulación, escenarios          │
│                              │                                  │
│  Software: NetworkX          │  Software: scipy, mise_sd        │
└──────────────────────────────┴──────────────────────────────────┘
    ↓                              ↓
    └──────────┬───────────────────┘
               ↓
    SEMANA 6: INTEGRACIÓN + GOBERNANZA
    Las herramientas cuantitativas no capturan todo.
    La dimensión social, ambiental y de gobernanza
    completa el análisis sistémico.
               ↓
    SEMANAS 7–8: PROYECTO INTEGRADOR
    Aplicar todo a un caso real colombiano.
    Producir un informe de consultoría sistémica.
```

### ¿Por qué necesitamos tanto redes como dinámica de sistemas?

Cada herramienta captura una dimensión que la otra no:

| Dimensión | Redes | Dinámica de Sistemas |
|---|---|---|
| Pregunta central | ¿Cómo está *estructurado* el sistema? | ¿Cómo se *comporta* el sistema en el tiempo? |
| Fortaleza | Identifica quién está conectado con quién, qué nodos son críticos, cómo se propagan efectos por la estructura | Simula cómo evolucionan las variables, captura retroalimentaciones y retardos, permite evaluar políticas |
| Limitación | Es un *snapshot* estático (no muestra evolución temporal, excepto en modelos de dinámica sobre redes) | No muestra la estructura de las conexiones individuales (trabaja con variables agregadas) |
| Ejemplo | "La subestación X es la más crítica del SIN" | "Si se duplica el retardo de construcción, las oscilaciones de precio se amplifican" |

Para un análisis sistémico completo de un proyecto energético, necesitamos ambas. Las redes nos dicen *dónde* están los puntos vulnerables y las palancas de cambio en la estructura. La dinámica de sistemas nos dice *qué pasa* cuando activamos esas palancas en el tiempo. La Semana 6 integrará ambos enfoques con la dimensión de gobernanza y justicia energética.

---

## 8. Conceptos clave de la semana

### Mensajes clave

- Los sistemas energéticos son **complejos**, no meramente complicados. No podemos entenderlos analizando cada componente por separado; las interacciones generan comportamientos emergentes.

- El **análisis convencional** (VPN, TIR, sensibilidad estática) es necesario pero insuficiente. Falla cuando el sistema tiene retroalimentaciones, no linealidades, agentes que se adaptan, y eventos extremos de colas pesadas.

- Los siete conceptos de la complejidad — **retroalimentación, no linealidad, emergencia, adaptación, cisnes negros, dependencia del camino y tipping points** — son las lentes que necesitamos para analizar proyectos energéticos de forma más realista.

- El **Diagrama de Lazos Causales (CLD)** es nuestra primera herramienta para hacer visible la estructura causal de un sistema. No es cuantitativo, pero es imprescindible para pensar con claridad antes de modelar.

- La **crisis de El Niño 2015–2016** ilustra todos estos conceptos: retroalimentaciones que amplificaron la sequía, no linealidades en la relación embalse-precio, emergencia del nivel de precios, adaptación de generadores y reguladores, un evento extremo que los modelos no anticiparon, y la dependencia del camino de una matriz dominada por hidroelectricidad.

- Este curso ofrece tres herramientas progresivas: **pensamiento complejo** (cualitativo, esta semana) → **redes** (estructura, semanas 2–3) → **dinámica de sistemas** (comportamiento temporal, semanas 4–5) → **integración con gobernanza** (semana 6).

### Glosario de términos introducidos

| Término en español | Término en inglés | Definición breve |
|---|---|---|
| Adaptación | Adaptation | Capacidad de los agentes de un sistema de modificar su comportamiento basándose en la experiencia. |
| Ciclo de balance | Balancing loop (B) | Ciclo de retroalimentación que contrarresta perturbaciones y busca un equilibrio. |
| Ciclo de refuerzo | Reinforcing loop (R) | Ciclo de retroalimentación que amplifica perturbaciones, generando crecimiento o colapso. |
| Cisne negro | Black swan | Evento raro, de alto impacto, e inesperado pero retrospectivamente explicable. |
| Colas pesadas | Fat tails / Heavy tails | Distribuciones de probabilidad donde los eventos extremos son más frecuentes que en una gaussiana. |
| Dependencia del camino | Path dependence | Condición donde el estado actual del sistema depende de su historia, no solo de las condiciones presentes. |
| Diagrama de Lazos Causales (CLD) | Causal Loop Diagram | Diagrama que muestra relaciones causales entre variables y los ciclos de retroalimentación que forman. |
| Efectos de memoria | Memory effects | Manifestación de la adaptación: el comportamiento del sistema depende de su trayectoria pasada. |
| Emergencia | Emergence | Propiedad del sistema como un todo que no puede atribuirse a ningún componente individual. |
| *Lock-in* | Lock-in | Estado donde el sistema está atrapado en una solución subóptima debido a rendimientos crecientes de adopción, infraestructura hundida y complementariedades. |
| No linealidad | Nonlinearity | Ausencia de proporcionalidad entre causa y efecto; el sistema viola el principio de superposición. |
| Punto de inflexión | Tipping point | Umbral crítico más allá del cual el sistema transita a un régimen de comportamiento cualitativamente diferente. |
| Retroalimentación | Feedback | Estructura circular de causalidad donde la salida de un proceso influye en su propia entrada. |
| Sistema adaptativo complejo | Complex adaptive system (CAS) | Sistema compuesto por agentes que interactúan, aprenden y producen propiedades emergentes. |
| Sistema complicado | Complicated system | Sistema con muchos componentes cuyo comportamiento es predecible con suficiente información. |
| Sistema complejo | Complex system | Sistema donde las interacciones entre componentes generan comportamientos impredecibles a nivel macro. |

---

### Lecturas recomendadas para esta semana

1. **Meadows, D. (2008).** *Thinking in Systems: A Primer.* Capítulos 1–2. — La introducción más accesible al pensamiento sistémico. Lectura obligatoria.
2. **Taleb, N. N. (2007).** *The Black Swan.* Extractos seleccionados. — La crítica definitiva a los modelos de riesgo basados en distribuciones gaussianas.
3. **UPME. (2020).** *Plan Energético Nacional 2020–2050.* Resumen ejecutivo. — Contexto del sector energético colombiano.
4. **XM. (2016).** *Informe de gestión de El Niño 2015–2016.* — Datos y narrativa oficial de la crisis.
5. **Mitchell, M. (2009).** *Complexity: A Guided Tour.* Capítulos 1–4. — Introducción rigurosa pero legible a la ciencia de la complejidad. Recomendada.
6. **Sterman, J. (2000).** *Business Dynamics.* Capítulo 1. — Motivación magistral de por qué necesitamos dinámica de sistemas. Recomendada.

---

*En la Semana 2 formalizaremos la estructura del sistema usando el lenguaje de las redes complejas. El mapa causal informal que dibujamos esta semana se convertirá en un grafo con métricas cuantitativas. Pasaremos de "el SIN es una red compleja" a "la subestación X tiene la mayor centralidad de intermediación del sistema, lo que la convierte en un cuello de botella crítico." De la intuición a la medición.*
