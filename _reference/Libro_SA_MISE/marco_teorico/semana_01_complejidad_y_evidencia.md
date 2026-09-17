# Semana 1. Pensar sistémicamente y responder por la evidencia


## Primera capa. El trancón que nadie quiso producir

Imagina una vía circular con vehículos que intentan conservar una distancia cómoda. Nadie quiere crear un trancón. Sin embargo, un conductor frena, el siguiente responde un poco después y una perturbación puede amplificarse. Para investigar esa posibilidad tenemos que especificar cómo responde cada conductor. La palabra «emergencia» describe el resultado colectivo; no reemplaza la regla que lo genera.

Detengamos la escena. Una fotografía nos permite contar carros y medir distancias. Una película muestra cómo cambian esas distancias y quién reacciona a quién. Ambas miradas son útiles. Una carretera con una restricción geométrica requiere ingeniería vial; una onda de frenado requiere además estudiar interacciones y tiempos de respuesta. El análisis sistémico añade preguntas a la descripción, no vuelve innecesaria la descripción.

Antes de pasar a energía, haz una predicción: si todos reaccionaran más rápido, ¿mejoraría siempre el tráfico? Falta saber con qué intensidad corrigen y qué información observan. Una reacción fuerte ante una señal atrasada puede sobrecorregir. Una reacción suave puede amortiguar. «Más rápido» no define por sí solo una buena política.

En el notebook usaremos primero una cola de vehículos, más sencilla que un modelo de ondas: llegan carros y una intersección los atiende. Dos calendarios pueden tener igual número de llegadas y diferente cola máxima. Así vemos una primera limitación del promedio sin exigir todavía teoría de tráfico. No atribuiremos a ese ejercicio una explicación completa de las ondas de frenado; esa diferencia entre la historia y el modelo debe quedar visible.

## Segunda capa. Del relato a variables que se puedan discutir

Recuperemos el recorrido del original: complicado, complejo, retroalimentación, no linealidad, emergencia, adaptación y memoria. La distinción sirve para buscar mecanismos. Una máquina con muchas piezas puede ser predecible dentro de un régimen; una interacción entre pocas reglas puede producir comportamientos difíciles de anticipar. Esto no divide todos los objetos en dos cajas excluyentes. El SIN necesita tanto ingeniería detallada de componentes como estudio de sus interacciones.

Llamemos Q a los vehículos esperando, a a las llegadas por minuto y s a la capacidad de atención por minuto. Si Q es positivo, la diferencia a−s cambia la cola. Si Q llega a cero, no permitimos una cola negativa: la salida efectiva queda limitada por los vehículos disponibles. Esa restricción introduce una respuesta por tramos. Ya tenemos estado, flujos, regla y frontera; ahora podemos construir una simulación y comprobar conservación.

Miremos otra situación: un rumor. Contar cuántas personas lo escucharon no describe quién se lo puede contar a quién. La misma cantidad inicial de informados puede producir historias diferentes si están concentrados en un grupo o repartidos entre varios. En la semana 3 convertiremos esa intuición en un grafo con estados. La complejidad deja de ser un adjetivo y se vuelve una comparación reproducible.

Un diagrama causal permite preparar esa comparación. Si cambiamos «mala coordinación» por «tiempo entre conocer una decisión ajena y revisar la propia», la flecha se vuelve más discutible y más útil. La precisión no elimina la dimensión social: evita atribuirle cualquier resultado sin evidencia.

## Tercera capa. ¿Qué historia estamos contando sobre el SIN?

Imagina una reunión durante una condición hidrológica exigente. Alguien presenta demanda anual, otro capacidad instalada, otro precio de bolsa y otro fechas de entrada de proyectos. Cada cifra puede estar bien calculada y, aun así, no responder la misma pregunta. La energía anual no garantiza potencia disponible en cada hora; una planta anunciada no equivale a una planta operativa; un precio observado no revela por sí solo la causa de su movimiento.

El enfoque sistémico propone conectar esas piezas mediante hipótesis: menores aportes reducen opciones de operación; la sustitución por térmicas puede depender de combustible; las señales económicas llegan a inversionistas con distintas restricciones; las nuevas obras tienen demoras. Cada vínculo exige evidencia y puede competir con otra explicación. El relato es el comienzo del análisis, no su conclusión.

Una evaluación convencional bien hecha ya puede incluir incertidumbre y restricciones. Su contribución es indispensable para cuantificar demanda, balances, costos y operación. La aproximación sistémica agrega especial valor cuando la decisión modifica la conducta de otros, cuando un efecto se devuelve al origen o cuando una intervención desplaza el problema. Si la pregunta es un balance contable, hacerlo correctamente es suficiente; no hay que adornarlo con un modelo complejo.

En lo que sigue leeremos indicadores históricos y ensayaremos hipótesis causales. El propósito es aprender a sostener dos afirmaciones al mismo tiempo: el sistema contiene interacciones importantes y los datos disponibles no identifican automáticamente todas ellas.


## Desarrollo y contraste profesional

**Pregunta de trabajo:** ¿cómo cambia la evaluación de un proyecto cuando su resultado depende del comportamiento de otros actores, del clima y de la infraestructura compartida?

**Al terminar:** podrás delimitar un sistema, construir hipótesis causales alternativas y distinguir observación, exploración y evaluación condicionada. Evidencia para RAC1 y RAC4: una ficha de decisión y un mapa causal argumentado. 

## Del proyecto aislado al sistema

Un proyecto solar tiene equipos, inversión, costos e ingresos. También necesita conexión, puede producir cuando otras solares producen, depende de contratos y se realiza en un territorio. Una mejora tecnológica puede reducir su costo por MWh y, simultáneamente, la expansión conjunta de proyectos similares puede reducir el precio que capturan. El análisis de sistemas permite formular esa interacción. La evaluación financiera permite comprobar su consecuencia para la caja. Ambos trabajos se necesitan.

El sistema no coincide automáticamente con el país. Si la decisión es firmar un PPA para una planta, la frontera debe incluir comprador, perfil de producción, mercado de liquidación y obligaciones contractuales. Si es reforzar una red, cambian frontera, datos y criterios. Delimitar significa declarar qué se incluye, qué se trata como externo y qué podría invalidar esa separación.

Un sistema complejo puede combinar heterogeneidad, adaptación, no linealidad y retroalimentación. Tener muchos componentes no demuestra todos esos atributos. Llamar «emergente» a un apagón tampoco explica su mecanismo. El consultor debe pasar de la etiqueta a una cadena contrastable: qué perturbación ocurre, qué equipos o decisiones responden y qué restricciones propagan sus efectos.

## Causalidad, polaridades y lazos

### Fundamentos: del atributo al mecanismo

**No linealidad** significa que duplicar una entrada no necesariamente duplica la respuesta. Una restricción de transmisión ilustra una respuesta por tramos: por debajo del límite una inyección adicional puede ser admisible; al alcanzarlo, requiere otra acción operativa. El umbral no demuestra por sí solo una transición irreversible. Para hablar de un punto de inflexión hay que especificar estado, mecanismo y persistencia del cambio.

**Emergencia** es una propiedad colectiva que resulta de interacciones. Una concentración de producción al mediodía puede surgir de decisiones individuales similares, aunque ninguna empresa busque reducir el precio que todas capturan. No hace falta suponer irracionalidad. **Adaptación** añade cambio de reglas o expectativas: después de observar menores ingresos, los agentes pueden modificar contratos, diseños o calendarios. Un modelo de parámetros fijos deja fuera esa respuesta salvo que la represente expresamente.

**Dependencia del camino** significa que decisiones anteriores condicionan opciones actuales: activos durables, contratos y conocimiento adquirido hacen que cambiar de trayectoria tenga costos. No toda inversión hundida es ineficiente ni todo cambio tecnológico elimina esa dependencia. La pregunta profesional es qué parte del costo es recuperable y qué alternativas quedan abiertas en cada fecha.

La distinción entre complicado y complejo es útil para elegir modelos, pero no divide profesiones: un flujo de potencia detallado puede ser necesario para una red compleja, y un análisis de incentivos puede ser simple. El criterio es qué interacción importa para la decisión. El modelo sistémico complementa estudios eléctricos, económicos e institucionales; no los invalida por llamarlos convencionales.

### Cómo construir un mapa que se pueda discutir

Partir de una trayectoria problemática —por ejemplo, atrasos e ingresos menores a los esperados— y definir variables que puedan aumentar o disminuir. «Regulación» es demasiado amplia; «tiempo entre solicitud completa y decisión de conexión» tiene un significado verificable. Para cada flecha anotar mecanismo, demora, evidencia y explicación rival. Separar las relaciones documentadas de las hipótesis con un atributo, no solo un color difícil de reproducir.

Recorrer cada circuito contando signos negativos: un número par corresponde a retroalimentación reforzadora y uno impar a balanceadora bajo las polaridades declaradas. Esto clasifica el circuito; no determina cuál domina ni resuelve la trayectoria del sistema. La magnitud, los stocks, las restricciones y las demoras se especifican al convertir el mapa en ecuaciones.

**Ejemplo de revisión:** precio esperado → inicio de proyectos → capacidad → holgura → precio esperado es un lazo balanceador si la holgura reduce precio y los otros enlaces son positivos. Añadir «proyectos en construcción conocidos → menor necesidad de iniciar proyectos» introduce anticipación que puede reducir sobreinversión. El estudiante debe justificar si los agentes observan y creen ese pipeline; no asignarles expectativas perfectas por comodidad.

Un mapa útil termina con una pregunta de contraste: ¿una demora física, un cambio de expectativas o una restricción financiera explica mejor la trayectoria observada? La evidencia necesaria será distinta para cada mecanismo. Esta pregunta conecta el mapa con la práctica estadística y con el encargo del caso.

En un diagrama causal, una flecha positiva indica que, manteniendo lo demás constante, un aumento en el origen tiende a aumentar el destino respecto de lo que habría sucedido. Una flecha negativa indica la respuesta contraria. No significa «bueno» o «malo», ni identifica la magnitud de un efecto.

Considérese capacidad disponible → holgura → precio esperado → inicio de proyectos → capacidad disponible. Mayor holgura puede reducir el precio; mayor precio esperado puede estimular proyectos. El producto de las polaridades del circuito determina si es reforzador o balanceador. Es indispensable cerrar el circuito: «precio alto → inversión» es un vínculo, no un lazo completo.

La puesta en servicio introduce una demora. Una respuesta balanceadora con demora puede oscilar bajo ciertos parámetros y reglas; no está obligada a hacerlo. Exceso de ganancia, expectativas, restricciones de financiación y el pipeline conocido pueden cambiar el resultado. El mapa causal es una hipótesis sobre estos vínculos, no evidencia de su existencia ni una ecuación ya calibrada.

## Extremos: aprender a leer lo que el indicador dice

La distribución histórica del precio puede ser asimétrica y tener observaciones extremas. Un histograma no distingue entre una única distribución estable y una mezcla de regímenes: sequía, cambios regulatorios, inflación, combustible y estructura de oferta. La curtosis muestral es sensible a extremos; pandas informa **exceso de curtosis**, cuyo referente normal es cero. No identifica por sí sola una ley de potencia ni la probabilidad futura de una crisis.

Para comparar años lejanos hay que distinguir COP corrientes de COP constantes. Sin una serie de deflactor y una base declarada, la gráfica permanece nominal. Si se usa un índice de precios, la transformación es `precio_real_t = precio_nominal_t × índice_base / índice_t`, con índices positivos, frecuencia alineada y propósito económico justificado. No hay deflactor incluido en estos extractos; por eso la práctica no simula una corrección monetaria inexistente.

> **Alerta del consultor.** Un máximo dividido por un mínimo mide un rango relativo observado. No equivale a «veces más volátil» ni a una probabilidad de pérdida. Escoger el indicador empieza por la pregunta: dispersión diaria, ingreso expuesto, pérdida máxima o costo de abastecimiento requieren medidas distintas.

## El registro de afirmaciones

Cada afirmación del caso tiene cinco campos: resultado; fuente y cobertura; transformación; nivel de evidencia; límite para decidir. «La energía generada aumentó entre dos años completos» es descripción. «Una demora puede amplificar una oscilación» es exploración. «Conviene contratar una fracción de producción bajo estas condiciones» exige una comparación económica y contractual explícita.

Tres explicaciones pueden competir por el mismo precio alto: menor disponibilidad hídrica, mayor costo térmico y condiciones comerciales de oferta. Su coexistencia hace valioso el enfoque sistémico; también hace más difícil identificar cada efecto. Buscar evidencia que refute la primera explicación evita construir todo el proyecto para confirmar una intuición inicial.

## Aplicación y entrega

La práctica recalcula precios desde columnas horarias, excluye años incompletos y examina distribución y evolución. No deriva política de inversión de esa estadística. Antes de ejecutar, anticipa qué cambia si se incluye 2025 parcial. Después explica la diferencia entre disponibilidad del archivo y comparabilidad del período.

Entrega una página: decisor, decisión, frontera, dos hipótesis rivales y dos datos que permitirían discriminarlas. Incluye un lazo cerrado, con polaridades y demora. La calidad se mide por coherencia y trazabilidad, no por cantidad de flechas. Pregunta de defensa: **¿qué observación te haría cambiar el mapa?**

Lecturas de acompañamiento: Meadows, *Thinking in Systems*; Bale, Varga y Foxon, *Energy and complexity: New ways forward*; Scheffer et al., *Early-warning signals for critical transitions*, disponibles o referenciadas en el material anterior. Conservar su contexto: un método de alerta en un sistema no se transfiere al SIN sin validación.

## Antes de cerrar la lectura

Vuelve al ejemplo inicial y explica qué relación conserva con el problema energético y cuál deja de ser válida. Lleva al notebook una predicción escrita. Después de calcular, distingue observación, explicación del mecanismo y consecuencia para la decisión. Si no coinciden, revisa primero la transformación y después tu hipótesis.
