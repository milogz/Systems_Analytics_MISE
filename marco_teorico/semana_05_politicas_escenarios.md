# Semana 5 — Dinámica de Sistemas II: Políticas, Escenarios e Incertidumbre

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

---

## 1. Apertura: ¿Funcionó el Cargo por Confiabilidad?

El Cargo por Confiabilidad (CxC), implementado mediante la Resolución CREG 071 de 2006, representa una de las intervenciones de política más significativas, complejas y debatidas en la historia del mercado eléctrico colombiano. Para comprender su impacto desde la perspectiva de la analítica de sistemas, debemos retroceder a los orígenes del mercado mayorista y entender el problema estructural que el CxC pretendía resolver. Tras el severo racionamiento eléctrico de 1992-1993, ocasionado por el fenómeno de El Niño y exacerbado por la falta de previsión y el deterioro del parque generador público, Colombia reestructuró su sector eléctrico. Se pasó de un monopolio estatal a un mercado competitivo, inspirado en las reformas del Reino Unido. 

En este nuevo diseño, se adoptó inicialmente un esquema de mercado de energía ("energy-only market") complementado con un cargo por capacidad. Sin embargo, se hizo evidente con el tiempo que un mercado que solo remunera la energía generada no proveía incentivos suficientes ni señales de largo plazo adecuadas para garantizar la expansión óptima de la capacidad de respaldo, específicamente la capacidad térmica necesaria para cubrir la demanda durante eventos de sequía extrema. En un país donde cerca del 70% de la energía proviene de fuentes hidroeléctricas, la vulnerabilidad hidrológica es el principal riesgo sistémico. Las termoeléctricas (a gas, carbón o líquidos) operan pocas horas al año durante periodos de hidrología normal, lo qué significa que sus ingresos son esporádicos y altamente inciertos. Sin una garantía de ingresos fijos, los inversionistas no tienen el caso de negocio para construir plantas costosas que podrían estar apagadas el 80% del tiempo, a pesar de que el sistema las necesita desesperadamente durante un Niño.

El diseño del CxC introdujo un cambio fundamental en las reglas del juego: un pago fijo (expresado en dólares por megavatio-hora, USD/MWh) a los generadores por mantener una "capacidad firme" disponible. A cambio de este pago constante y predecible que estabiliza sus flujos de caja, los generadores asumen la obligación de entregar energía al sistema a un precio predeterminado (el Precio de Escasez) cuando el precio de bolsa supera este umbral. Esta intervención buscaba mitigar el riesgo de inversión para las tecnologías de respaldo, asegurando así la confiabilidad del suministro eléctrico ante las peores condiciones climáticas. 

Desde su implementación, el CxC ha superado varias pruebas de estrés, incluyendo los intensos fenómenos de El Niño de 2009-2010 y 2015-2016. Durante estas crisis, el país evitó el racionamiento, lo cual es frecuentemente citado por la Comisión de Regulación de Energía y Gas (CREG) y los defensores del mecanismo como prueba innegable de su éxito. El sistema demostró ser resiliente, y las plantas térmicas, en su mayoría, respondieron cuando fueron llamadas a despachar.

Sin embargo, al analizar los datos recientes de la evolución de la matriz energética y observar los resultados de las subastas de expansión y de Fuentes No Convencionales de Energía Renovable (FNCER) realizadas entre 2019 y 2024, surge una paradoja crítica desde la perspectiva de la dinámica de sistemas y la teoría de la dependencia del camino (*path dependence*). La pregunta fundamental es: ¿el CxC estabilizó el sistema de forma eficiente, o creó un *lock-in* (bloqueo) tecnológico hacia la generación térmica convencional?

Al asegurar ingresos estables a largo plazo para las plantas térmicas fósiles, la política pudo haber retrasado involuntariamente la adopción de tecnologías renovables más limpias. Las métricas para definir la Energía Firme para el Cargo por Confiabilidad (ENFICC) favorecen inherentemente a las tecnologías despachables y penalizan a las tecnologías intermitentes como la solar y la eólica, cuyas ENFICC resultan ser fracciones pequeñas de su capacidad instalada real. Esto alteró los ciclos de inversión natural del mercado. Mientras en otros mercados las renovables experimentaban un auge impulsado por la caída radical de sus costos de capital, en Colombia el esquema regulatorio seguía atrayendo capital primariamente hacia plantas de gas y líquidos para asegurar la confiabilidad, creando dependencias estructurales a largo plazo (contratos de suministro de combustibles, infraestructura de ductos, lobbies institucionales).

La Ley 2099 de 2021 (Ley de Transición Energética) y resoluciones posteriores han intentado nivelar el campo de juego, integrando el almacenamiento y ajustando las reglas para promover las FNCER. Pero la paradoja persiste: las políticas diseñadas para resolver la crisis de ayer a menudo se convierten en las barreras para la innovación de mañana. En las próximas secciones, desglosaremos esta dinámica utilizando el lenguaje de stocks, flujos y lazos de retroalimentación.

---

## 2. Intervenciones de política en modelos SD

En el ámbito de la Dinámica de Sistemas (SD), un modelo no es solo una representación pasiva del mundo; es un laboratorio virtual para la experimentación de políticas. Una política se entiende como un cambio deliberado, exógeno o endógeno, en la estructura o en los parámetros del sistema, diseñado con el fin explícito de modificar su comportamiento futuro, corregir trayectorias indeseables o mitigar oscilaciones perniciosas. Para intervenir eficazmente, el analista debe entender con precisión quirúrgica dónde se "inserta" la política en el diagrama de Stocks y Flujos (S&F).

En la arquitectura matemática y conceptual de un modelo SD, existen cuatro tipos principales de intervenciones o "puntos de palanca", ordenados desde el más superficial hasta el más profundo:

1. **Sobre flujos (Cambio de Parámetros):** Esta es la forma más común y tradicional de intervención gubernamental. Actúa alterando las constantes o parámetros que rigen las tasas de cambio (los flujos) sin alterar la estructura topológica del modelo. 
   - *Ejemplos:* Cambiar la tasa de un impuesto a las emisiones de carbono, incrementar un subsidio a los bienes de capital para plantas solares, ajustar la tasa de interés de referencia. 
   - *Dinámica:* Matemáticamente, esto cambia el valor de $k$ en una ecuación diferencial como $\frac{dS}{dt} = k \cdot S$. El impacto suele ser cuantitativo, pero rara vez cambia cualitativamente el régimen del sistema.

2. **Sobre stocks (Amortiguadores y Reservas):** Implica modificar físicamente los niveles de acumulación, ya sea inyectando o extrayendo recursos del sistema de forma directa, o estableciendo nuevas capacidades de almacenamiento estratégico.
   - *Ejemplos:* La construcción de una planta regasificadora (FSRU) como la de SPEC en Cartagena, que actúa como un amortiguador (*buffer*) para el stock de gas natural disponible en el país; o las reservas estratégicas de petróleo.
   - *Dinámica:* Aumenta la inercia del sistema, permitiendo absorber shocks externos (como la interrupción de un gasoducto o una sequía) antes de que estos se propaguen como señales extremas de precios.

3. **Sobre información (Señales y Retardos):** Modifica la forma en que los actores dentro del sistema perciben el estado del mundo y toman decisiones. Esto implica alterar la red de conexiones de información (las flechas delgadas en un diagrama S&F).
   - *Ejemplos:* Reducir los tiempos de trámite de licencias ambientales (disminuyendo un retardo material), implementar medidores inteligentes (smart meters) que brinden señales de precio en tiempo real a los consumidores, o publicar reportes diarios de disponibilidad hídrica.
   - *Dinámica:* Reducir los retardos (*delays*) de información o de percepción frecuentemente ayuda a estabilizar los sistemas oscilatorios. Cuando los agentes reaccionan a información más fresca, se reduce el sobreimpulso (*overshoot*) característico de los ciclos de inversión.

4. **Sobre estructura (Regulación y Nuevas Reglas):** La intervención más profunda. Implica rediseñar el mapa causal, añadiendo nuevos ciclos de retroalimentación, eliminando ciclos existentes o cambiando el objetivo intrínseco del sistema.
   - *Ejemplos:* Pasar de un mercado de energía puro a uno con mercado de capacidad (como el CxC); implementar normativas de despacho vinculantes; establecer subastas de contratación a largo plazo exclusivas para tecnologías limpias.
   - *Dinámica:* Altera radicalmente las ecuaciones diferenciales que gobiernan el sistema, creando dinámicas de convergencia donde antes había divergencia, o introduciendo nuevas interacciones no lineales.

A continuación, resumimos estas intervenciones en el contexto del sector eléctrico:

| Política / Intervención | Dónde actúa en el modelo (Estructura S&F) | Qué ciclo (loop) de retroalimentación modifica |
| :--- | :--- | :--- |
| **Subsidios de capital a FNCER** | Parámetro en el flujo de decisión de inversión | Acelera el ciclo de refuerzo (R) de adopción y aprendizaje tecnológico |
| **Cargo por Confiabilidad (CxC)** | Crea un nuevo flujo de ingresos estable (Información/Estructura) | Atenúa el ciclo de balance (B) con retardo (oscilaciones de capacidad); crea un loop de refuerzo de incumbencia térmica |
| **Transparencia de datos de embalses** | Conector de información hacia expectativas | Acorta los retardos en el ciclo de fijación de precios, reduciendo oscilaciones a corto plazo |
| **Subastas de Contratos de Largo Plazo (PPA)**| Nueva estructura en la asignación de riesgo | Transforma la decisión de inversión de un proceso de mercado spot a un proceso planificado centralizado |

### La Jerarquía de los Puntos de Apalancamiento

Esta tipología resuena profundamente con el célebre ensayo de la pensadora de sistemas Donella Meadows, *"Leverage Points: Places to Intervene in a System"* (1999). Meadows identificó 12 niveles de intervención, argumentando que los analistas y los políticos suelen gastar enormes cantidades de energía peleando en los niveles de menor apalancamiento (como ajustar los parámetros, tarifas y subsidios, es decir, intervenciones sobre los flujos), cuando en realidad estos cambios rara vez resuelven problemas estructurales. 

Si un sistema eléctrico es propenso a ciclos inestables debido a sus profundos retardos de construcción y a su inelasticidad de demanda, un subsidio o un impuesto solo moverá las oscilaciones un poco hacia arriba o hacia abajo, pero no las detendrá. 

Por el contrario, los puntos de mayor apalancamiento residen en el rediseño de las reglas (la regulación que altera la estructura S&F) y los objetivos del sistema. El diseño del Cargo por Confiabilidad, al cambiar las reglas fundamentales de cómo se remunera el capital, actuó en un nivel alto de apalancamiento. Cambió la meta implícita de los inversionistas de "maximizar las ventas de energía cuando los precios son altos" a "asegurar el pago por capacidad minimizando los costos de disponibilidad". 

Entender que "cambiar parámetros es débil, pero cambiar la estructura del sistema es poderoso" es la lección principal del modelado de políticas. Nos obliga a buscar soluciones que modifiquen la red causal, en lugar de simplemente inyectar dinero para forzar al sistema en contra de su propia tendencia natural.

---

## 3. El CxC como intervención sistémica

Para visualizar verdaderamente el impacto del Cargo por Confiabilidad, debemos mapearlo como una intervención sistémica sobre el diagrama base del mercado eléctrico. Recordemos de la semana anterior que el mercado de energía "energy-only" sufre de un bucle pernicioso: el ciclo de Inversión y Escasez. 

En el modelo sin CxC, la decisión de construir una nueva planta térmica dependía de proyectar el precio spot (precio de bolsa) a futuro. Dado que las térmicas (especialmente las de ciclo simple) solo despachan en escasez, su viabilidad requería proyectar precios spot astronómicos durante eventos de El Niño. 
El lazo de retroalimentación era: *Menor Margen de Reserva → Mayor Probabilidad de Escasez → Mayores Precios Spot Proyectados → Aumenta Rentabilidad Esperada → Inicio de Inversión Térmica → (Retardo de Construcción) → Aumento de Capacidad → Aumenta Margen de Reserva.*
Este es un clásico ciclo de balance (B) con un gran retardo, que matemáticamente genera oscilaciones violentas (*boom and bust*), donde largos periodos de sequía de inversión son seguidos por pánicos y sobre-construcción.

### La mecánica estructural del CxC

El Cargo por Confiabilidad intervino en esta estructura modificando radicalmente las reglas de remuneración. Se diseñó como un esquema de opciones (call options) de confiabilidad. Los generadores reciben un pago fijo regular (el Cargo) por la cantidad de Energía Firme (ENFICC) que pueden certificar. A cambio, cuando el precio de bolsa supera el "Precio de Escasez", ellos deben devolver la diferencia, asegurando así a la demanda.

Al mapear el CxC en nuestro modelo S&F, añadimos un nuevo flujo continuo de "Ingresos por Capacidad" a la ecuación de caja de las termoeléctricas, paralelo al esporádico flujo de "Ingresos Spot". 

El lazo que se crea es un potente ciclo estabilizador:
1. **Ingreso fijo y garantizado** proveniente del CxC.
2. **Reducción sustancial del riesgo financiero** (menor costo promedio ponderado de capital, WACC).
3. **Incentivo constante para la inversión y el mantenimiento** de capacidad firme.
4. **Disponibilidad térmica asegurada** incluso en ausencia de altas rentas de escasez.

Esto soluciona elegantemente el problema del *missing money* (dinero faltante) típico de los mercados marginalistas, amortiguando las oscilaciones de la inversión térmica. Al simular el modelo con esta intervención, las curvas de capacidad instalada se alisan; el margen de reserva se mantiene más cercano al nivel óptimo regulatorio y los picos extremos de precios al consumidor durante las sequías se recortan mediante el techo del Precio de Escasez.

### La paradoja del Lock-in Térmico

Sin embargo, como dicta un axioma informal de la dinámica de sistemas, "las soluciones de hoy son los problemas de mañana". El CxC, al funcionar exactamente cómo se diseñó, introdujo consecuencias sistémicas no previstas a largo plazo. 

La metodología para calcular la ENFICC —la métrica de cuánta firmeza aporta una planta— fue calibrada basándose en perfiles de tecnologías convencionales (hídrica con embalse y termoeléctrica). Las plantas térmicas a gas y carbón pueden certificar altos niveles de ENFICC en relación con su capacidad instalada, otorgándoles flujos de caja masivos provenientes del esquema. 

En contraste, cuando las renovables intermitentes (solar fotovoltaica y eólica) empezaron a volverse competitivas en el mundo, en Colombia enfrentaron una barrera sistémica. Debido a su variabilidad, se les asignó metodológicamente una ENFICC baja. Por lo tanto, un inversionista que evaluara un proyecto solar en Colombia encontraba que no podía acceder a la misma tajada del generoso pago por confiabilidad que subsidiaba a las térmicas. 

Este bucle estabilizador para las térmicas se convirtió en un mecanismo de exclusión implícita. Las termoeléctricas, con ingresos garantizados a 10 o 20 años, afianzaron su posición dominante, justificando la firma de contratos rígidos de largo plazo para suministro de gas natural y carbón, y promoviendo la expansión de gasoductos (infraestructura hundida). Todo este ecosistema forma un ciclo de refuerzo (*lock-in* institucional y físico): 
*Ingresos CxC → Inversión térmica y contratos de gas a largo plazo → Lobby y poder de mercado de incumbentes fósiles → Regulación que mantiene la centralidad de la energía firme tradicional → Más ingresos CxC.*

La paradoja es clara: el CxC es una política de enorme éxito para garantizar la luz en los Niños históricos, pero al mitigar tan eficientemente el riesgo fósil, actuó como un bloqueador de la transición energética al desincentivar la penetración acelerada de fuentes alternativas. Esto ilustra magistralmente cómo la robustez estática (asegurar el corto plazo) puede comprometer la resiliencia evolutiva (adaptarse a nuevas tecnologías a largo plazo).

## 4. FNCER: la disrupción renovable

A pesar de las inercias estructurales como el Cargo por Confiabilidad, la revolución de las Fuentes No Convencionales de Energía Renovable (FNCER) terminó llegando a Colombia, impulsada principalmente por tendencias tecnológicas globales indetenibles. La dinámica de sistemas nos proporciona las herramientas ideales para entender por qué la inserción masiva de energía solar fotovoltaica y eólica no es simplemente una adición a la matriz energética, sino una disrupción que altera fundamentalmente el comportamiento del mercado en su conjunto.

La característica económica definitoria de la energía solar y eólica es que tienen costos de capital (CAPEX) significativos, pero un costo marginal de operación (OPEX y costo de combustible) prácticamente de cero. El sol y el viento son gratuitos y no requieren extracción, transporte ni procesamiento. En un mercado eléctrico liberalizado como el colombiano, donde el despacho de las plantas se realiza siguiendo el "orden de mérito" —se despachan primero las plantas más baratas y el precio de bolsa es fijado por la planta más cara necesaria para cubrir la demanda—, el impacto de los costos marginales cero es profundo.

Cuando entran en operación grandes bloques de capacidad FNCER, estas plantas se ubican al principio del orden de mérito. Esto desplaza sistemáticamente la curva de oferta agregada hacia la derecha. El resultado inmediato es el famoso ***merit order effect* (efecto del orden de mérito)**: las plantas térmicas, con sus altos costos de combustibles fósiles, son empujadas fuera del despacho base, y el precio de compensación del mercado (precio spot) disminuye drásticamente, especialmente durante las horas de sol o alta pluviosidad.

### El nuevo loop: La espiral deflacionaria térmica

Este fenómeno introduce un nuevo e importantísimo lazo de retroalimentación en el sistema. Anteriormente, las termoeléctricas dependían de las horas marginales para rentabilizar sus inversiones por encima del CxC. Ahora enfrentamos este ciclo:
1. **Entrada de mayor capacidad FNCER.**
2. **Mayor oferta con costo marginal nulo.**
3. **Caída del precio spot promedio en el mercado mayorista.**
4. **Desplazamiento y menor despacho de las plantas térmicas (menor factor de planta).**
5. **Reducción drástica de los ingresos y rentabilidad de la generación térmica.**
6. **Las térmicas se vuelven comercialmente menos atractivas y el capital huye hacia las renovables.**

Este es un **ciclo de refuerzo (R)** que actúa en detrimento de la tecnología incumbente. A medida que las FNCER hunden los precios spot, destruyen el caso de negocio de cualquier futura inversión térmica sin fuertes subsidios estatales. Algunos académicos han alertado sobre el riesgo de una "espiral deflacionaria", donde el mercado pierde tanta capacidad térmica (que se retira prematuramente por falta de ingresos operativos) que la confiabilidad del sistema ante una sequía (cuando el sol no brilla lo suficiente o hay intermitencia prolongada) queda seriamente comprometida. Esta es la tensión fundamental de la transición energética moderna.

### Dinámica de costos: La curva de aprendizaje

Para modelar la penetración de las FNCER de manera realista, no podemos tratar su costo como una constante exógena. Históricamente, el costo de los módulos solares y turbinas eólicas ha experimentado descensos exponenciales asombrosos. En dinámica de sistemas, esto se modela utilizando la **Ley de Wright** o curvas de aprendizaje (*learning curves*).

La Ley de Wright postula que por cada duplicación en la capacidad acumulada producida de una tecnología a nivel global, su costo unitario cae en un porcentaje constante (la tasa de aprendizaje, que ronda el 20-25% para la energía solar fotovoltaica). Esto genera un poderoso ciclo virtuoso:
*Mayor adopción global → Mayor experiencia en manufactura, economías de escala e innovación → Caída en los costos de capital (CAPEX) → Aumento de la competitividad frente a tecnologías fósiles → Mayor adopción global.*

En nuestro modelo, las FNCER se representan como un nuevo **stock** de capacidad. Su dinámica de crecimiento es diferente a la de las hidráulicas y térmicas: están impulsadas fuertemente por la caída de costos (flujo de inversión facilitado) y políticas de subastas de largo plazo (como las exitosas rondas promovidas en Colombia desde 2019). Este stock interactúa con el sistema antiguo robándole participación de mercado y reescribiendo la ecuación de formación de precios.

---

## 5. Escenarios: pensar en futuros radicalmente diferentes

Al integrar el comportamiento de las tecnologías tradicionales, la intervención regulatoria (CxC) y las disrupciones tecnológicas (FNCER), nuestro modelo de dinámica de sistemas se vuelve capaz de simular trayectorias ricas y complejas. Sin embargo, surge un problema epistemológico masivo: los resultados del modelo dependen de los parámetros de entrada. ¿Cómo introducimos el crecimiento de la demanda para el 2040? ¿Cuál será el precio internacional del gas natural? ¿Qué tan frecuente será el fenómeno de El Niño? 

En la planificación convencional (evaluación de proyectos clásica), la tendencia ha sido hacer pronósticos. Se toma una tendencia histórica, se le aplica un modelo econométrico, se calcula un escenario "base" y tal vez se añaden variaciones estocásticas asumiendo distribuciones de probabilidad normales.

Frank Knight, en su obra seminal *Risk, Uncertainty and Profit* (1921), y más tarde John Maynard Keynes, trazaron una distinción filosófica y práctica qué es central para la analítica de sistemas: la diferencia entre **riesgo** e **incertidumbre profunda** (*deep uncertainty*).
- **Riesgo** se refiere a situaciones donde no conocemos el resultado específico, pero conocemos todas las posibilidades y podemos asignarles distribuciones de probabilidad rigurosas basadas en datos históricos. (Ej. Tirar un dado, o la hidrología histórica colombiana asumiendo clima estacionario).
- **Incertidumbre Profunda** se refiere a situaciones donde el sistema es tan complejo, o los cambios estructurales son tan inéditos (cambio climático, disrupción tecnológica masiva, geopolítica), que ni siquiera podemos acordar un modelo único, los resultados posibles, o las probabilidades. No podemos usar promedios matemáticos de manera sensata.

Para abordar la política energética bajo incertidumbre profunda, debemos abandonar la pretensión de predecir el futuro mediante proyecciones puntuales, y abrazar el **pensamiento de escenarios**. 

Un escenario no es una predicción, ni un caso "alto, medio, bajo" de una sola variable. Es una narrativa coherente sobre un futuro cualitativamente distinto, construida combinando conjuntos plausibles de variables exógenas. Esta metodología fue pionera por los equipos de planeación estratégica de Royal Dutch Shell en la década de 1970, permitiéndoles anticipar y sobrevivir a los shocks petroleros mucho mejor que sus competidores.

El método más robusto para diseñar escenarios es la **Caja Morfológica** (*Morphological box method*). Se identifican las 3 o 4 dimensiones más críticas e inciertas (ej. ritmo de electrificación, precio de los fósiles, cambio climático), y se definen estados extremos para cada una. Al cruzar estas dimensiones, se genera un abanico de futuros radicalmente disímiles.

El propósito de los escenarios en dinámica de sistemas es estresar el modelo. Corremos el sistema bajo estas diferentes combinaciones no para averiguar "cuál es el más probable", sino para identificar las vulnerabilidades de nuestras políticas. 

---

## 6. Robustez sobre optimalidad

Cuando los tomadores de decisiones enfrentan múltiples escenarios futuros qué son profundamente inciertos, el enfoque convencional es tratar de encontrar la política "óptima" bajo el escenario que consideran más probable. Matemáticamente, esto equivale a optimizar el sistema (minimizar costos o maximizar beneficios) apostando a que una predicción específica se cumplirá. El peligro es obvio: si el futuro diverge de la predicción, la política óptima para ese mundo imaginario suele ser desastrosa en el mundo real. Es una estrategia frágil.

En el paradigma de Systems Analytics bajo incertidumbre profunda, sustituimos la búsqueda de la *optimalidad* por la búsqueda de la **robustez**. Una política robusta no necesariamente arroja el mejor resultado absoluto en un escenario específico, pero funciona razonablemente bien y evita resultados catastróficos en *todos* los escenarios posibles. Prefiere una ganancia modesta segura sobre la posibilidad de una gran ganancia a costa de un riesgo de ruina.

El marco teórico de la **Toma de Decisiones Robustas (Robust Decision Making, RDM)**, desarrollado extensamente por la RAND Corporation, formaliza este enfoque. RDM invierte el proceso de planeación tradicional: en lugar de predecir primero y planear después (predict-then-act), RDM prueba múltiples políticas contra cientos o miles de escenarios para descubrir bajo qué condiciones fallan, y luego refina las políticas para hacerlas resilientes.

### La Tabla de Robustez y el Minimax Regret

El corazón del método RDM, de forma simplificada, es la evaluación estructurada a través de una tabla de robustez. Esta matriz cruza las **Estrategias** (las políticas que controlamos) contra los **Escenarios** (los estados del mundo que no controlamos), y en cada intersección calcula el desempeño del sistema (ej. el costo total del sistema eléctrico en trillones de pesos).

Para elegir la estrategia más robusta, empleamos el criterio de **Minimax Regret** (minimizar el arrepentimiento máximo), derivado de la teoría de juegos y la toma de decisiones. 
El "regret" (arrepentimiento o costo de oportunidad) se define como la diferencia entre el desempeño de una estrategia en un escenario determinado y el desempeño de la *mejor* estrategia posible en ese mismo escenario. Representa "cuánto peor nos fue por no haber adivinado el futuro correctamente".

**Ejemplo Numérico Aplicado:**
Supongamos que el regulador debe elegir entre tres estrategias para la expansión de generación en Colombia:
1. **Estrategia A (Térmica Centralizada):** Mantener fuertes incentivos al gas.
2. **Estrategia B (Renovable Agresiva):** Subsidios enormes a eólica/solar, eliminar térmicas.
3. **Estrategia C (Diversificada):** Balance entre base renovable y respaldo térmico moderado.

Y enfrentamos tres Escenarios Futuros (los valores son Costo Total en Unidades Arbitrarias, donde *menor* es mejor):
- Escenario 1 (Status Quo Climático y Fósil Barato): A=100, B=130, C=110
- Escenario 2 (Super-Niño con Gas Caro): A=180, B=140, C=120
- Escenario 3 (Revolución Solar con Clima Húmedo): A=140, B=80, C=90

Cálculo del Regret (Costo - Mejor Costo del Escenario):
- En Escenario 1 (Mejor es A=100): Regret(A)=0, Regret(B)=30, Regret(C)=10
- En Escenario 2 (Mejor es C=120): Regret(A)=60, Regret(B)=20, Regret(C)=0
- En Escenario 3 (Mejor es B=80): Regret(A)=60, Regret(B)=0, Regret(C)=10

Determinación del Arrepentimiento Máximo (Max Regret) por Estrategia:
- Estrategia A: Max Regret = 60 (ocurre en Esc. 2 y 3)
- Estrategia B: Max Regret = 30 (ocurre en Esc. 1)
- Estrategia C: Max Regret = 10 (ocurre en Esc. 1 y 3)

**Decisión Minimax:** La regla Minimax Regret nos indica escoger la estrategia que tiene el menor arrepentimiento máximo. En este caso, escogemos la **Estrategia C (Diversificada)**, cuyo peor arrepentimiento posible es de solo 10 unidades. 
Observe la profunda implicación conceptual: La Estrategia C *no fue la estrategia óptima ganadora en la mayoría de los escenarios* (perdió ante A en el Escenario 1 y ante B en el Escenario 3). Si hubiéramos asignado probabilidades ilusorias, podríamos haber elegido equivocadamente. Sin embargo, la estrategia diversificada garantiza evitar el desastre (evita la exposición al gas carísimo del Esc. 2 de la térmica, y evita el sobrecosto innecesario del Esc. 1 de la renovable pura). 

En el sector energético, la diversificación sistemáticamente surge como la estrategia más robusta ante la incertidumbre climática y tecnológica. Modelar esto formalmente en Dinámica de Sistemas ofrece una justificación cuantitativa y científica irrefutable a favor de carteras de inversión equilibradas.

## 7. Análisis de sensibilidad

Antes de confiar ciegamente en las tablas de robustez, el modelador debe someter su simulación de dinámica de sistemas a rigurosas pruebas de sensibilidad. El análisis de sensibilidad no pretende predecir el futuro, sino diagnosticar el modelo en sí mismo: nos permite entender qué supuestos, parámetros o estructuras matemáticas son las verdaderas fuerzas motoras que impulsan los resultados (outputs). 

1. **Análisis OAT (One-at-a-time):** Es la técnica fundamental, en la que se varía un solo parámetro a la vez, manteniendo todos los demás estrictamente en sus valores base. Aunque limitado (porque ignora las interacciones sinérgicas entre múltiples variables), es el primer paso indispensable para verificar la coherencia mecánica de las ecuaciones. 

2. **Diagrama de Tornado (Tornado Diagram):** Esta visualización jerarquiza la importancia de los parámetros evaluados. En el eje horizontal se grafica el rango de impacto sobre un indicador clave (por ejemplo, el precio promedio de la energía a 2030), y en el eje vertical se ubican las variables, ordenadas de mayor a menor impacto (formando un embudo que asemeja un tornado). El analista y el formulador de políticas pueden ver inmediatamente dónde está el mayor riesgo. Si el costo del combustible térmico encabeza el tornado, el sistema es altamente vulnerable a mercados de commodities extranjeros, lo que justifica enfocar los esfuerzos en mitigar ese factor.

3. **Pruebas de Condiciones Extremas (Extreme Condition Tests):** Un modelo de dinámica de sistemas robusto debe mantener la coherencia lógica frente a entradas absurdas o extremas, sin "romperse" matemáticamente. ¿Qué pasa si el costo de los paneles solares cae literalmente a cero? El modelo no debería proyectar capacidades instaladas infinitas (porque existen límites estructurales como área disponible o requerimientos de reserva técnica). ¿Qué pasa si los aportes hídricos caen a cero durante 36 meses? El nivel de los embalses nunca debe hacerse negativo, la demanda racionada debe aumentar y las térmicas despacharse a plena capacidad. Si un modelo falla pruebas extremas, su formulación ecuacional en condiciones normales es estructuralmente sospechosa.

4. **Validación Estructural y Conductual:** Todo esto forma parte de la validación del modelo. El éxito de un modelo SD no se mide primariamente por su capacidad de ajustar con $R^2$ alto una serie de tiempo del pasado, sino por su fidelidad estructural para reproducir los patrones de comportamiento fundamentales (oscilaciones, tipping points) observados en la realidad empírica.

---

## 8. El caso: CxC + FNCER bajo 4 escenarios

Sintetizando los conceptos abordados en esta sesión, construiremos un experimento final integrado simulando el caso colombiano. Analizaremos las implicaciones de mantener el Cargo por Confiabilidad (diseñado para una matriz hidro-térmica) frente a la penetración masiva de FNCER.

Construiremos un diseño experimental factorial enfrentando las decisiones de política (Estrategias) a los futuros plausibles (Escenarios).

**Los 4 Escenarios de Futuro Incierto:**
1. **BAU (Business As Usual):** Continuación de las tendencias de la última década. Crecimiento moderado de demanda, hidrología con variabilidad histórica conocida, y reducción parsimoniosa de costos de capital FNCER.
2. **Gas Shock (Choque de Combustibles Fósiles):** Una interrupción masiva de importaciones, declive prematuro de reservas de gas nacional o disrupción geopolítica que dispara los precios del GNV, del carbón y los combustibles líquidos de respaldo a precios prohibitivos.
3. **Solar Revolution (Revolución Renovable Exponencial):** Disrupción tecnológica acelerada. Los costos de los módulos solares y el almacenamiento en baterías colapsan de precio. El almacenamiento viable soluciona sustancialmente el problema de intermitencia sin necesidad de termoeléctricas.
4. **El Niño Extremo + Demanda Alta:** La pesadilla climática. Fenómenos de El Niño se vuelven el doble de severos y prolongados por el cambio climático severo, ocurriendo simultáneamente con un salto disruptivo en la demanda eléctrica (por ejemplo, debido a la electrificación rápida del transporte).

**Las 3 Estrategias Regulatorias (Intervenciones de Estructura/Información):**
- **S1: Conservadora (CxC Reforzado):** Se prioriza la seguridad energética tradicional. Se aumentan las subastas del Cargo por Confiabilidad asegurando nuevas termoeléctricas a gas de ciclo combinado y terminales de regasificación, limitando la integración de FNCER si comprometen la estabilidad del sistema por intermitencia.
- **S2: Agresiva Renovable (Fin del CxC Fósil):** Desmonte del subsidio del CxC a plantas que emiten carbono. Todos los recursos se desvían a masivas subastas de contratos PPA (Power Purchase Agreements) para asegurar inversión en eólica y solar. Las térmicas quedan libradas a la dinámica pura del mercado spot.
- **S3: Diversificada (Transición Justa / Híbrida):** Se mantiene un CxC ajustado y decreciente para un parque térmico de respaldo estratégico mínimo, mientras se escala agresivamente y a través de mecanismos separados una vasta flota de FNCER y baterías. 

**Resultados de la Simulación en la Tabla de Robustez:**
Al ejecutar nuestro modelo Dinámico con $Ecuaciones \times Parámetros$ para las 12 combinaciones, emergen patrones reveladores en los indicadores de confiabilidad (horas de racionamiento) y costo económico (tarifa final).
- La estrategia **S1 (Conservadora)** salva al sistema sin problemas en el Escenario 4 (El Niño), pero resulta catastróficamente costosa en el Escenario 3 (Revolución Solar), y genera altas facturas de la luz ante el *Gas Shock*.
- La estrategia **S2 (Agresiva Renovable)** brilla como la política más barata y óptima bajo los Escenarios 1 y 3. El costo promedio de la energía cae enormemente. Sin embargo, frente al Escenario 4 (El Niño Extremo), el modelo estalla: el racionamiento de energía es brutal por la ausencia de firmeza térmica y los costos de destrucción económica son astronómicos.
- La estrategia **S3 (Diversificada)**. Siguiendo el método de Minimax Regret discutido anteriormente, al compilar todos los arrepentimientos máximos, S3 emerge como la recomendación indiscutible de política. 

La interpretación cualitativa de este ejercicio cuantitativo es poderosa: la política regulatoria no debe aferrarse rígidamente ni a los fantasmas del pasado (obsesión por firmeza fósil absoluta) ni a los entusiasmos irreales del futuro (solarización sin respaldo). La modelación sistémica prueba que el abandono abrupto de la estructura del CxC antes de que exista almacenamiento masivo es profundamente arriesgado, pero su mantenimiento irrestricto crea una ineficiencia letal. La reforma paulatina —donde se diseña la obsolescencia programada de la vieja estructura— es el único camino robusto.

---

## 9. Cierre del módulo SD

Al llegar a la conclusión del bloque metodológico de Dinámica de Sistemas (SD) del curso de Systems Analytics, es fundamental hacer un balance honesto de los superpoderes, pero también de los puntos ciegos estructurales, de la herramienta que acabamos de dominar.

A través del lenguaje de stocks y flujos, hemos sido capaces de formular representaciones cuantitativas que capturan las características esenciales de los sistemas complejos reales que la econometría clásica ignora. La Dinámica de Sistemas nos ha permitido demostrar cómo los *retardos temporales* (como el tiempo de licenciamiento ambiental de una represa), los *bucles de retroalimentación* y la *acumulación física* en sí misma explican las formidables oscilaciones de ciclos económicos en el sector eléctrico, y por qué intervenciones superficiales terminan en fracaso rotundo (fixes that fail).

Sin embargo, como un telescopio diseñado para mirar galaxias masivas, SD es excelente para lo agregado, pero no fue diseñado para distinguir a los planetas individuales y sus lunas. 

**La gran limitación de la Dinámica de Sistemas:**
Un modelo S&F asume que los agentes dentro del sistema (los inversionistas, los consumidores, los generadores) son promedios agregados y homogéneos ("la demanda reacciona", "el inversionista invierte") o representados como ecuaciones mecánicas de fluidos. La Dinámica de Sistemas sufre para capturar adecuadamente la enorme *heterogeneidad, topología espacial y la agencia estratégica* de los individuos y las instituciones. Un embalse no es un simple balde que se vacía matemáticamente; es administrado por una junta directiva que analiza las ofertas de sus rivales y reacciona a los rumores del regulador usando teoría de juegos compleja. 

Si queremos modelar no solo el "funcionamiento" del mercado bajo reglas estáticas, sino la "gobernanza" del mercado, las negociaciones políticas, y cómo las estructuras de poder determinan las decisiones (¿por qué algunas comunidades bloquean líneas de transmisión eólicas, deteniendo todo un pipeline de capacidad?), necesitamos incorporar nuevas herramientas a nuestro arsenal.

Por ello, en las próximas semanas del programa pasaremos de los fluidos continuos a las entidades discretas y conectadas. Iniciaremos el módulo de Teoría de Redes Complejas y los Modelos Basados en Agentes (Agent-Based Modeling, ABM). Estas aproximaciones complementarán y llenarán el vacío de SD.

Al formular y correr sus modelos SD para los entregables de política pública, recuerden este aforismo fundamental para cualquier consultor de analítica:

> *"El modelo nunca sustituye el juicio y el debate del tomador de decisiones; su verdadero valor radica en informar y afinar dicho juicio, haciendo explícitos los sesgos y revelando futuros posibles."*

El diseño de políticas para un sector tan vital y volátil requiere combinar el rigor de las ecuaciones diferenciales robustas (lo técnico) con la legitimidad de las instituciones (lo político). Nuestro próximo destino metodológico profundizará en esta intersección. Bienvenidos al final de la Dinámica de Sistemas, y a las fronteras de la Gobernanza en la Semana 6.

---

### Glosario Completo

- **Cargo por Confiabilidad (CxC):** Esquema regulatorio colombiano diseñado para remunerar la disponibilidad de capacidad de generación firme frente a periodos críticos (sequías), mitigando la volatilidad del mercado mayorista.
- **Ciclo de Refuerzo / Balance:** Estructuras causales fundamentales en SD. Refuerzo amplifica perturbaciones (desestabiliza); Balance resiste perturbaciones buscando metas (estabiliza).
- **Curva de Aprendizaje (Ley de Wright):** Principio empírico que dicta que el costo unitario de una tecnología decae porcentualmente con cada duplicación de su producción global acumulada, crucial para explicar el abaratamiento de las renovables.
- **Incertidumbre Profunda (*Deep Uncertainty*):** Condiciones analíticas en las cuales expertos o modeladores no pueden conocer ni acordar modelos del sistema, distribuciones de probabilidad a variables clave, o la valoración de resultados deseados.
- **Lock-in Tecnológico/Estructural:** Situación de dependencia del camino (*path dependence*) donde un mercado queda atrapado usando un estándar subóptimo o antiguo porque el ecosistema e incentivos creados hacen prohibitivamente costosa la transición.
- **Minimax Regret (Arrepentimiento Mínimo Máximo):** Métrica decisional robusta de la teoría de juegos enfocada en seleccionar políticas cuyo peor resultado posible (comparado con la política óptima) produzca el menor daño (arrepentimiento).
- **Merit Order Effect (Efecto del Orden de Mérito):** Desplazamiento estructural de las curvas de costos de un mercado marginalista provocado por el despacho prioritario de tecnologías renovables de costo marginal cercano a cero, depreciando el precio general.
- **Robustez (*Robustness*):** En el contexto de evaluación de políticas, la capacidad de una estrategia de desempeñarse razonablemente bien frente a un amplio y exhaustivo abanico de escenarios futuros, sin colapsar.
- **Validación Estructural:** Proceso para comprobar empírica y lógicamente que las relaciones mecánicas descritas por las matemáticas del modelo SD reflejan la arquitectura causal genuina de la realidad.

### Referencias

- Arango, S., & Larsen, E. R. (2011). "Cycles in deregulated electricity markets: Empirical evidence from two decades". *Energy Policy*, 39(5), 2457-2466.
- Comisión de Regulación de Energía y Gas (CREG). Resolución CREG 071 de 2006 (Metodología para la remuneración del Cargo por Confiabilidad).
- Farmer, J. D. et al. (2019). "Sensitive intervention points in the post-carbon transition". *Science*, 364(6436), 132-134.
- Ley 2099 de 2021 (Ley de Transición Energética).
- Marchau, V. A. W. J., Walker, W. E., Bloemen, P. J. T. M., & Popper, S. W. (Eds.). (2019). *Decision Making under Deep Uncertainty: From Theory to Practice*. Springer Open (Acceso abierto).
- Meadows, D. H. (1999). *Leverage Points: Places to Intervene in a System*. The Sustainability Institute.
