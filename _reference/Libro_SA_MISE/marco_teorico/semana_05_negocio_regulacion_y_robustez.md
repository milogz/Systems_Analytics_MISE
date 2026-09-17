# Semana 5. Del comportamiento del modelo a la decisión económica


## Primera capa. Elegir un plan cuando el futuro no viene con probabilidades

Un grupo organiza una actividad al aire libre. Puede pagar un salón, alquilar una cubierta o aceptar el riesgo de lluvia. El salón cuesta incluso si hace buen tiempo. La opción barata puede salir cara si llueve. No necesitamos empezar por el sector eléctrico para entender que «mejor» depende del escenario y de quién asume la pérdida.

Construiremos una tabla de costos. Primero elegimos la opción de menor costo en cada escenario, como si conociéramos el futuro. Después medimos cuánto cuesta habernos equivocado respecto de esa referencia. Esa diferencia es arrepentimiento. No es una emoción ni una probabilidad; es una comparación condicionada al escenario y a las alternativas consideradas.

Una opción puede minimizar el peor arrepentimiento y seguir excediendo el presupuesto. Por eso pondremos al lado desempeño absoluto y restricciones. Este pequeño ejemplo prepara un hábito profesional: no confundir un ranking atractivo con una decisión admisible.

## Segunda capa. Separar lo que decidimos de lo que nos ocurre

La estructura XLRM organiza incertidumbres externas, palancas controlables, relaciones del modelo y métricas. En la actividad, el clima es incertidumbre; alquilar es palanca; la relación costo–clima es modelo; el gasto y la cancelación son métricas. Si damos al organizador control sobre la lluvia, el problema deja de representar la decisión.

En una simulación energética también hay que cuidar esa separación. Retraso de una obra puede ser escenario; una mejora específica de coordinación puede ser intervención. Cambiar arbitrariamente el parámetro demora no demuestra que una reforma consiga ese cambio. Hay dos preguntas: qué ocurriría si cambiara y qué acción real podría producirlo.

La sensibilidad estudia cómo cambia el resultado cuando cambia una entrada. La robustez compara desempeño bajo varias condiciones. Ninguna asigna probabilidades por sí sola. Si usamos escenarios sin probabilidades, no llamaremos valor esperado al promedio de sus resultados. Y si añadimos una alternativa, puede cambiar el arrepentimiento de todas las demás: la referencia forma parte del problema.

El modelo financiero exige además una secuencia. Construir cuesta antes de producir; una demora posterga ingresos; un contrato redistribuye exposición. Pondremos cada flujo en su fecha, con unidades monetarias coherentes. El valor presente no explica toda la conveniencia social, pero sí obliga a mostrar quién desembolsa y quién recibe.

## Tercera capa. Una política puede cambiar incentivos y trasladar riesgos

El original proponía discutir el Cargo por Confiabilidad, las renovables y las decisiones de inversión como partes de un sistema. Conservamos esa ambición. La pregunta no se resuelve añadiendo un número al precio de bolsa: hay que explicar obligación, elegibilidad, remuneración y respuesta esperada, verificando el marco aplicable. La lectura de la [CREG 071 de 2006](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0071_2006.htm) debe acompañarse de sus modificaciones y del objeto preciso del encargo.

La mirada económica convencional ayuda a estimar costos, riesgo, contratos y bienestar. La mirada sistémica pregunta por adaptación, entrada y retiro, aprendizaje, interacción con infraestructura y consecuencias diferidas. Una remuneración puede mejorar incentivos bajo ciertas condiciones y producir efectos distributivos que merecen análisis. Afirmar de antemano que estabiliza todo o que necesariamente crea un lock-in reemplaza la investigación por una conclusión.

En el caso distinguiremos tres planos: desempeño físico de una respuesta a estrés, costo o caja bajo supuestos y viabilidad institucional. La planta solar de 20 MW será una perspectiva empresarial complementaria. Su VPN no será el indicador que decida una política nacional. El ejercicio de portafolio sectorial usará métricas físicas y costos docentes separados, con una frontera explícita respecto de una evaluación de expansión real.


## Desarrollo y contraste profesional

**Pregunta:** ¿bajo qué condiciones una intervención crea valor y resulta aceptable? RAC3 y RAC4. Entrega: alternativas comparables, caja, escenario adverso, arrepentimiento y condiciones de validez. Ninguna estrategia tiene reservado el primer puesto.

## La unidad de decisión

El desarrollador evalúa flujos de su proyecto; el usuario, costo y calidad de suministro; el planificador, desempeño del sistema; el regulador, reglas e incentivos. Una reducción del precio spot puede beneficiar compradores y reducir ingresos de generadores, sin representar en igual magnitud ahorro de recursos. Un precio es también una transferencia entre agentes. No debe renombrarse costo total del sistema.

Comparar alternativas exige misma base y horizonte. Si una alternativa recibe activos iniciales adicionales sin CAPEX, la ventaja ya está introducida antes de simular. Las opciones docentes son no construir, construir 20 MW solares mercantes o construir los mismos 20 MW con un PPA sobre parte de la producción. El capital se paga explícitamente. No construir fija la referencia incremental; no implica ausencia de costos para todo el sistema eléctrico.

## Caja transparente

La producción anual simplificada es `capacidad_MW × 8760 × factor_planta`, con degradación declarada. Se usa un año operativo normalizado para valoración de largo plazo; no es la agregación de registros horarios de un año bisiesto. Los ingresos usan MWh × 1000 × COP/kWh. Se descuentan CAPEX y OPEX antes de calcular `VPN = sum(flujo_t / (1+r)^t)`.

El modelo es en COP constantes del ejercicio y tasa real. Los supuestos de CAPEX, OPEX y precio no son cotizaciones verificadas ni valores recomendados para una inversión real. No incluye deuda, impuestos, depreciación fiscal, capital de trabajo, valor terminal, garantías ni costos específicos de conexión. El VPN es antes de impuestos y sin deuda; no llamarlo retorno del accionista.

La demora retrasa ingresos con CAPEX desembolsado en t=0. Es un supuesto adverso claro. Si el contrato de obra permite diferir CAPEX, cambiará el resultado. El modelo permite observar el efecto temporal, pero no presume que toda demora sea administrativa o evitable.

> **Alerta del consultor.** Usar un precio nominal histórico como flujo futuro constante y descontarlo con tasa real mezcla bases. No hay corrección invisible: o construyes flujos nominales y tasa nominal coherentes, o flujos reales y tasa real, documentando inflación y moneda.

## Regulación como mecanismo

Para representar CxC deben distinguirse energía firme certificable, obligaciones asignadas, remuneración y condiciones de cumplimiento/activación. No se añade por defecto ingreso por cada MW instalado. La práctica financiera omite ingresos CxC porque no tiene ENFICC validada ni OEF asignada; esto evita dar rentas regulatorias imaginarias a la alternativa solar.

Como ejercicio dimensional separado, `OEF_kWh × precio_cargo_USD_kWh × TRM_COP_USD` permite comprobar una remuneración bruta hipotética para un período compatible. No reproduce liquidación, indexación, garantías o exposición por incumplimiento. Cada cantidad debe corresponder a ese período. La aplicación profesional exige la norma y situación del activo a la fecha de decisión. [CREG 071 de 2006 y modificaciones](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0071_2006.htm).

El CxC no debe equipararse a una transferencia exclusiva a térmicas. La subasta realizada en 2024 incluyó proyectos solares; la mezcla adjudicada no es lo mismo que energía firme entregada ni capacidad puesta en servicio. [XM, certificación de asignaciones de OEF de la subasta de 2024](https://www.xm.com.co/noticias/6803-con-la-certificacion-del-100-de-las-plantas-con-asignacion-de-oef-en-la-subasta-de).

## Escenarios y arrepentimiento

Un escenario es una combinación coherente de condiciones externas; una alternativa contiene decisiones controlables por el actor. Se separan X —incertidumbres—, L —palancas—, R —relaciones/modelo— y M —métricas—. Cambiar el precio capturado no es lo mismo que cambiar el contrato, aunque ambos afecten ingresos.

Para maximizar VPN, arrepentimiento = mejor VPN del escenario − VPN de la alternativa. El minimax elige menor máximo arrepentimiento. Se informa también el mínimo VPN: una alternativa relativamente buena puede seguir destruyendo valor. La tabla financiera no certifica viabilidad de conexión, derechos o suficiencia nacional. Si hay empates se conservan, no se decide por orden alfabético.

Los cuatro escenarios docentes no tienen probabilidades asignadas ni agotan el futuro. Precio capturado bajo, conexión tardía y menor producción estresan mecanismos distintos. Agregar escenarios adversos combinados permite examinar si cambia el ranking. Sensibilidad de un parámetro no determina automáticamente la mejor política: el actor puede no controlarlo o hacerlo a un costo omitido.

## Entrega y defensa

### Sensibilidad, incertidumbre y reglas de decisión

Una sensibilidad local cambia un parámetro manteniendo los demás. Es útil para detectar una conversión incorrecta o identificar qué supuestos afectan la caja en un entorno dado. Su ranking depende del rango escogido: un ±20% en CAPEX no equivale a dos años de demora. La práctica reporta el rango junto con el cambio de VPN; no lo convierte en una jerarquía causal del sistema eléctrico.

La incertidumbre conjunta exige combinaciones: producción baja y conexión tardía pueden coincidir. No hay probabilidades justificadas en el ejercicio; por eso no se presenta un VPN esperado ni una probabilidad de éxito. Un muestreo uniforme de rangos elegidos por el analista tampoco representa automáticamente probabilidades del mundo. Puede servir para explorar cobertura del espacio y encontrar vulnerabilidades, con esa etiqueta explícita.

Antes de usar arrepentimiento, fijar dirección de mejora y restricciones. Si la métrica es VPN, el mejor valor es el máximo. Si es costo, el mejor es el mínimo. «No construir» tiene VPN incremental cero; ello no implica que satisfaga una obligación de abastecimiento si el decisor fuera un comprador obligado a servir demanda. Cambiar el decisor exige reformular alternativas y referencia.

Una regla robusta puede exigir VPN no negativo en los escenarios examinados y condiciones no financieras verificadas. Si todas las inversiones fallan esa prueba, estudiar o no construir puede ser coherente. Si se acepta alguna pérdida, definir quién la acepta y por qué. Los pesos de una evaluación multicriterio expresan preferencias, no leyes naturales; revisar cambios de ranking ante otros pesos y no compensar restricciones obligatorias con una puntuación favorable.

### Diseño adaptativo y valor de información

Una decisión adaptativa especifica acción inicial, indicador observable, umbral, revisión y acción posterior. En el caso, podría reservarse una fase de estudios y revisar al recibir recurso solar y conexión. El valor de esperar depende de costos, vencimientos y opciones comerciales que aquí no están modelados. «Esperar siempre» no se deduce de reconocer incertidumbre.

El precio de equilibrio es el precio capturado que hace VPN=0 bajo un contrato y otros supuestos fijos. No es precio mínimo regulatorio ni pronóstico. Con más PPA, cambia la exposición al precio spot; con cobertura total, variar ese precio puede no cambiar la caja y dejar de existir un umbral único. La raíz numérica necesita comprobar primero que el intervalo contiene un cruce.

Priorizar estudios comparando qué decisión podrían cambiar: una cotización de CAPEX más precisa, un estudio de recurso o la confirmación del calendario de conexión. Sin probabilidades no se calcula honestamente un valor esperado de información; sí se puede mostrar cuánto varía la elección bajo resultados plausibles y contrastarlo con costo y plazo del estudio. Esa discusión conecta incertidumbre con una acción concreta de consultoría.

Presenta supuestos monetarios y físicos, tabla de caja, comparación, restricciones pendientes y recomendación condicionada. Incluye la alternativa no construir y explica qué dato puede alterar la elección. Si todas incumplen una restricción, reporta que ninguna es admisible; minimax no elimina ese hecho. Pregunta de defensa: **¿qué riesgo conserva el PPA de tu propuesta y quién lo asume?**

Lecturas: Hallegatte, *Strategies to adapt to an uncertain climate change*, y trabajos de decisión bajo incertidumbre del programa original. Robustez, optimización y valoración son herramientas complementarias cuyo criterio debe declararse.

## Antes de cerrar la lectura

Vuelve al ejemplo inicial y explica qué relación conserva con el problema energético y cuál deja de ser válida. Lleva al notebook una predicción escrita. Después de calcular, distingue observación, explicación del mecanismo y consecuencia para la decisión. Si no coinciden, revisa primero la transformación y después tu hipótesis.
