# Semana 3. Mercado, actores y adopción: hacer que la red signifique algo


## Primera capa. Enterarse de algo y comprometerse con ello

Imagina dos conversaciones entre amigos. En la primera, alguien cuenta que mañana cambia el lugar de una reunión. Un solo contacto puede bastar para que otra persona se entere. En la segunda, alguien propone participar en una compra colectiva costosa. Conocer la propuesta no significa aceptarla: pueden hacer falta varias referencias, financiación y confianza. Si modelamos ambos procesos con la misma regla, habremos borrado una diferencia que importa.

Recuperemos la red de la semana anterior. Pintemos de otro color a quienes conocen el rumor. El dibujo sigue teniendo las mismas amistades, pero ahora los nodos tienen estado. Una fotografía responde quién está informado. Varias fotografías ordenadas muestran una difusión. Antes de ejecutar, elige dos semillas y anticipa por dónde viajará la información.

## Segunda capa. Darle una regla y un reloj a la red

En un contagio simple, un susceptible recibe información con cierta probabilidad por contacto. Si tiene m vecinos informados y cada contacto es independiente con probabilidad p, la probabilidad de recibirla en una ronda es 1−(1−p)^m. Primero calculamos el complemento: ningún contacto tuvo éxito. Después restamos de uno. La independencia es un supuesto de este cálculo, no una propiedad universal de conversaciones reales.

En un modelo de umbral, el nodo adopta cuando una fracción suficiente de sus vecinos ya adoptó. Si necesita al menos la mitad y tiene cuatro vecinos, uno no basta y dos sí. Definiremos adopción irreversible: quien adoptó conserva su estado. Si quisiéramos abandono, deberíamos escribir otra regla. Para un nodo aislado, definimos que no hay contagio social; no dividimos por cero.

El reloj también importa. En actualización síncrona, todos observan la ronda anterior. Copiamos ese estado antes de modificarlo. Si actualizamos sobre la misma lista, un nodo que acaba de adoptar puede contagiar dentro de la misma ronda: sin querer, habremos cambiado el experimento. El notebook hará visible esa decisión de programación.

¿Un puente acelera siempre una difusión? Puede facilitar que una noticia cruce entre grupos, pero no dar suficiente refuerzo a alguien con umbral alto. Tampoco clustering alto garantiza una cascada. La combinación entre red, semillas y regla decide la trayectoria. Comparar mecanismos requiere conservar controles y repetir realizaciones cuando hay azar.

La curva de Bass cambia de escala. En vez de representar personas, estudia una fracción agregada F y una tasa `(p+qF)(1−F)`. El primer término permite adopción sin vecinos representados; el segundo amplifica con la adopción acumulada; el último reduce el mercado restante. Bass no es una traducción exacta de cualquier red de umbrales. Una curva en S puede tener mecanismos diferentes, por lo que ajustarla no identifica automáticamente imitación social.

## Tercera capa. Mercados y actores sin confundir sus redes

En el sector eléctrico conviven redes físicas, propiedad empresarial, contratos, competencias institucionales y comunicación. Un enlace de propiedad no equivale a una conversación; una competencia normativa no equivale a influencia informal. Una red de actores útil conserva el tipo de relación y su fuente. Una red vistosa que mezcla todos los enlaces puede generar un ranking sin interpretación defendible.

Para pensar en adopción solar, la evaluación económica aporta costos, ahorro, restricciones de ingreso y financiación. La perspectiva de difusión añade hipótesis sobre información, visibilidad y aprendizaje. Si hay instalaciones cercanas, podría haber contagio; también podrían compartir ingreso, recurso solar o proveedor. Para distinguir esas explicaciones hacen falta datos y un diseño de contraste. No basta con mostrar agrupamiento espacial.

Una intervención en comunicación puede tener poco efecto si el obstáculo es crédito o conexión. Una reducción de costo puede tener poco efecto si nadie comprende el contrato o confía en el proveedor. La consultoría debe averiguar qué mecanismo limita la decisión antes de elegir una palanca. El modelo ayuda a formular y comparar posibilidades; la investigación empírica debe decir cuáles son relevantes.

Finalmente, no confundamos producir con vender ni vender con capturar el precio promedio. El perfil horario de generación pondera la exposición económica. Esta es otra forma de interacción sistémica: varias plantas que producen juntas pueden enfrentar condiciones comunes. En la práctica haremos primero la aritmética de precio capturado y después discutiremos qué modelo adicional permitiría estudiar la formación de ese precio.


## Desarrollo y contraste profesional

**Pregunta:** ¿quién participa, cómo se distribuye la exposición económica y qué evidencia hace falta para hablar de poder o difusión? RAC2 y RAC4. Entrega: mercado relevante y red de relaciones documentadas, con un análisis de concentración y otro de adopción claramente delimitados.

## Cuatro redes diferentes

La red física describe conexiones eléctricas; la de propiedad, control societario; la contractual, derechos y obligaciones comerciales; la institucional, competencias y procedimientos. Una misma organización aparece en varias capas. El acoplamiento consiste en explicar cómo una relación afecta otra: por ejemplo, retraso de conexión → menor producción → compras para atender un contrato de volumen fijo. Superponer dibujos no demuestra ese mecanismo.

En el mercado eléctrico deben distinguirse actividad y entidad. Un agente puede participar en varias actividades y un grupo económico puede controlar varias sociedades. Para una ficha histórica, registrar nombre, código, control y fecha evita contar como competidores independientes sociedades bajo un mismo control sin justificarlo. Un catálogo de recursos tampoco equivale a listado de empresas.

Las competencias de política, regulación, planeación, operación, vigilancia y licenciamiento son diferentes. El mapa no atribuye a UPME la capacidad de decidir unilateralmente inversiones de todos los agentes ni de resolver todos los permisos. Cada arista institucional debe contener tipo de relación y referencia documental.

## Concentración antes que juicio sobre competencia

Para participaciones `s_i` que sumen 1, `HHI = sum((100 × s_i)^2)`. El resultado cambia con la definición de mercado: capacidad instalada, energía producida durante el año, energía firme o ventas en un segmento no son denominadores intercambiables. La concentración de producción puede variar con hidrología y disponibilidad aun sin cambio de propiedad.

La función del curso rechaza participaciones incompletas. Renormalizar a cien una muestra solo calcula concentración dentro de esa muestra; no recupera la del mercado nacional. Agrupar todo el resto como una empresa puede exagerar su concentración; ignorarlo puede subestimarla. El error del denominador debe resolverse antes de poner colores de «competitivo» o «concentrado».

La práctica agrupa producción observada de los recursos disponibles por código de empresa y conserva registros sin identificación. Ese resultado es descriptivo del extracto, no un HHI validado del MEM. Hablar de poder de mercado requiere estudiar capacidad de afectar resultados en condiciones específicas, demanda residual, restricciones, contratos y comportamiento. Un índice por sí solo no demuestra abuso ni captura.

> **Alerta del consultor.** Cuando el número parece preciso, revisa primero el universo. Un HHI con decimales construido sobre 86,6% de participaciones no gana validez por tener más cifras.

## Precio observado, precio capturado e ingreso

El promedio de cotizaciones horarias no es el ingreso unitario de una planta. Su precio capturado se calcula `sum(P_h × E_h) / sum(E_h)`, con intervalos y fronteras coherentes. Una solar produce poco o nada en ciertas horas; no captura en igual proporción todas las cotizaciones. El ingreso depende además del contrato y de las liquidaciones aplicables.

La práctica utiliza un perfil horario ficticio para mostrar esta diferencia y lo rotula como sintético. No lo combina con historia real para anunciar rentabilidad de una planta colombiana. Para esa aplicación harían falta producción horaria propia o estimada y validada, disponibilidad/conexión, pérdidas y cláusulas contractuales.

Un PPA pay-as-produced remunera producción efectiva según condiciones pactadas. Un compromiso de cantidades fijas puede exigir comprar energía cuando la planta no genera. La cobertura reduce una exposición y crea otras: contraparte, perfil, volumen, indexación y garantías. «Tener PPA» no es una variable binaria equivalente a ausencia de riesgo.

## Bass y contagio como hipótesis de adopción

El modelo de Bass expresa `dF/dt = (p + qF)(1−F)`, donde F es fracción del mercado potencial. p y q resumen mecanismos de adopción dentro de esa formulación. Su interpretación empírica depende de medir adoptantes, definir población y estimar con datos adecuados. MW instalados no son automáticamente número de hogares adoptantes.

La libreta genera una serie sintética y recupera sus parámetros: sirve para entender estimación y ruido. No descubre mecanismos colombianos. Una q mayor que p no demuestra que la influencia social importe más que el costo. Subsidios, financiación, precios de equipos y cambios regulatorios pueden producir trayectorias similares.

En contagio por umbral, un nodo adopta cuando suficiente proporción de vecinos lo hace. Los puentes entre comunidades pueden facilitar exposición, pero no garantizan contagio complejo cuando faltan contactos reforzadores. Comparar topologías exige mismas reglas, semillas, tamaño y varias realizaciones. La recomendación de focalizar incentivos requiere también criterios de acceso y equidad.

## Avance y evaluación

### Formular la dinámica sobre la red

Asignar a cada nodo un estado xi(t): 0 sin adopción y 1 con adopción. En un contagio simple, un contacto puede activar el cambio con probabilidad beta; con k vecinos activos e intentos independientes la probabilidad por paso es `1−(1−beta)^k`. Beta tiene sentido solo respecto del paso temporal y del mecanismo elegido. Adoptar equipamiento no es equivalente a recibir información: puede exigir crédito, techo disponible o autorización.

En un modelo de umbral irreversible, el nodo inactivo cambia a 1 cuando `vecinos_activos / grado ≥ umbral_i`. Una semilla empieza activa; los nodos aislados necesitan una regla explícita y en la práctica permanecen en su estado inicial. Con actualización síncrona todas las decisiones usan el estado anterior. Actualizar nodos uno por uno usando estados recién cambiados puede acelerar la difusión por un artefacto de orden. El algoritmo de la práctica usa actualización síncrona y se detiene cuando no hay cambios.

En contagio complejo varias exposiciones pueden ser necesarias. Una conexión que sirve de atajo informativo puede ser insuficiente para superar un umbral, mientras un grupo cohesionado brinda refuerzo. Ninguna estructura gana para todo umbral y toda semilla. Antes de ejecutar, predecir qué sucederá al agrupar las semillas o dispersarlas; después explicar qué regla produjo el contraste.

Bass es una descripción agregada distinta: F(t) representa fracción acumulada de una población potencial fija y p, q son tasas por unidad de tiempo. Con F(0)=0, la solución utilizada es `(1−exp(−(p+q)t)) / (1+(q/p)exp(−(p+q)t))`, para p>0. Si el mercado potencial cambia o casi no se observa saturación, diferentes parámetros pueden explicar la misma trayectoria. Recuperar parámetros sintéticos es una prueba de estimación, mientras atribuir adopción a mecanismos sociales necesita un diseño empírico adicional.

### Relaciones, comunidades y agentes

Una red bipartita separa, por ejemplo, empresas y proyectos. Proyectarla sobre empresas conecta a quienes comparten un proyecto; eso no prueba que tengan contratos entre sí. Registrar el peso como número de proyectos compartidos y revisar si un proyecto grande crea artificialmente una comunidad densa. La proyección pierde información de la otra capa y debe conservarse el original para interpretar resultados.

Los algoritmos de comunidades buscan agrupamientos según un objetivo estructural. La modularidad compara enlaces internos con una referencia aleatoria asociada al grado. Puede variar con resolución y semilla; una comunidad matemática no demuestra coordinación comercial o acuerdo ilegal. El expediente debe diferenciar asociación documentada, resultado del algoritmo e interpretación.

Un modelo basado en agentes añade estados, recursos y reglas de decisión heterogéneas. Puede representar hogares con distinto acceso a crédito o empresas con contratos diferentes. Requiere declarar inicialización, reglas, calendario, interacción y observables; ejecutar varias semillas y contrastar patrones. No basta cambiar el nombre de nodos por agentes. Una extensión válida del caso sería preguntar si restricciones de financiación explican una difusión lenta que el Bass agregado atribuye a q, especificando cómo comparar ambas hipótesis con observaciones.

Presenta una red pequeña con evidencia por arista. Elige una métrica y explica qué pregunta responde. Formula una hipótesis comercial y otra de adopción con al menos una explicación alternativa. El checkpoint integra la frontera de S1 y la infraestructura de S2. Pregunta de defensa: **¿qué parte de tu conclusión cambiaría al agrupar agentes por control económico o al cambiar el contrato?**

Lecturas: Granovetter sobre umbrales y Centola/Macy sobre contagios complejos, del material original. Usar sus mecanismos como hipótesis comparables, no como sustituto de evidencia sectorial.

## Antes de cerrar la lectura

Vuelve al ejemplo inicial y explica qué relación conserva con el problema energético y cuál deja de ser válida. Lleva al notebook una predicción escrita. Después de calcular, distingue observación, explicación del mecanismo y consecuencia para la decisión. Si no coinciden, revisa primero la transformación y después tu hipótesis.
