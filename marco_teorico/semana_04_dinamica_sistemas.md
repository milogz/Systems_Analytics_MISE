# Semana 4 — Dinámica de Sistemas I: Stocks, Flujos y el Ciclo de Inversión

## Marco Teórico · Systems Analytics — MISE, Universidad de los Andes

---

## 1. Apertura: ¿por qué el sector eléctrico oscila?

El sector eléctrico es, en esencia, uno de los sistemas más complejos diseñados y operados por la humanidad. Se caracteriza fundamentalmente por la interacción simultánea e ininterrumpida de múltiples agentes (generadores, transmisores, comercializadores, consumidores, reguladores y operadores) bajo condiciones de profunda incertidumbre, retardo y una marcada no-linealidad. Al observar con detenimiento la gráfica histórica de la capacidad instalada y los precios de bolsa en el Mercado de Energía Mayorista (MEM) de Colombia entre los años 2000 y 2024, un patrón fundamental y recurrente salta a la vista: las oscilaciones profundas y sostenidas a lo largo de los años.

Los precios de la energía en bolsa no se mantienen, ni de cerca, en un equilibrio estático dictado por la intersección teórica de curvas de oferta y demanda convencionales. Por el contrario, exhiben ciclos marcados de alzas abruptas (a menudo exacerbadas por eventos climáticos extremos como el fenómeno de El Niño) seguidas de caídas igualmente pronunciadas que pueden prolongarse durante años. Simultáneamente, la capacidad instalada de generación del país no crece de manera suave y continua alineada con la demanda, sino que crece a "saltos" — periodos de masiva entrada de nuevos proyectos (boom constructivo) seguidos de largos periodos de sequía de inversiones, muchas veces desfasados temporalmente de las necesidades inmediatas de la demanda eléctrica.

Para entender por qué ocurre esto, debemos revisar cómo se toman las decisiones de inversión en el mundo real. Las herramientas tradicionales de evaluación financiera, como el Valor Presente Neto (VPN) y la Tasa Interna de Retorno (TIR), han sido durante décadas el estándar de oro en las juntas directivas para decidir si un proyecto de generación (por ejemplo, una nueva hidroeléctrica de 500 MW o un gran parque solar) sigue adelante o no. Sin embargo, estas metodologías asumen condiciones determinísticas (o estocásticas pero simples) y son inherentemente estáticas y lineales en su concepción del tiempo y del entorno.

El VPN analiza un proyecto en aislamiento absoluto. Un analista financiero proyecta flujos de caja a 20 o 30 años hacia el futuro, asumiendo una senda de precios de la energía que, generalmente, es una extrapolación del presente o un promedio histórico, descuenta estos flujos a una tasa determinada por el costo de capital (WACC) y llega a un número. Si el VPN es positivo, el proyecto es "viable". Sin embargo, estas métricas *no capturan las oscilaciones endógenas* del mercado, ni tienen en cuenta que el proyecto evaluado no está solo en el universo.

Pensemos en lo que sucede en la realidad: un VPN altísimamente positivo calculado hoy probablemente se basa en que los precios actuales del mercado (y las proyecciones inmediatas) están altos. El problema fundamental es que el analista ignora que esos mismos precios altos están actuando como una "señal de humo" visible para *todos los demás agentes del mercado*. Mientras la Empresa A aprueba su proyecto con base en esos precios atractivos, las Empresas B, C y D están haciendo exactamente lo mismo en sus respectivas juntas directivas. Inician la construcción casi en simultáneo.

Dado que la construcción de infraestructura energética toma años (retardo material), durante un largo tiempo la escasez persiste y los precios siguen altos, lo que puede inducir a las Empresas E y F a entrar al juego de forma tardía. Años después, cuando todos estos proyectos superan sus fases de construcción y licenciamiento ambiental, entran en operación comercial casi al mismo tiempo. El resultado es inevitable: una sobreoferta masiva de energía inunda el sistema. Los precios colapsan drásticamente, destruyendo el valor proyectado original y haciendo que el VPN que justificó la inversión resulte ser una ficción. Este colapso de precios ahora frena cualquier nueva inversión. Y así, el ciclo se reinicia.

Este es un fallo sistémico. Históricamente, en Colombia, este patrón se hizo particularmente visible antes y después de la crisis del apagón de 1992-1993, y se transformó con la introducción de la Resolución CREG 071 de 2006, la cual instituyó el Cargo por Confiabilidad. Aunque el Cargo por Confiabilidad buscaba proveer una señal de largo plazo para garantizar la energía firme del sistema y mitigar la volatilidad extrema (especialmente durante fenómenos de El Niño), las oscilaciones en los precios de bolsa y en los ciclos de inversión continuaron manifestándose debido a los profundos retardos estructurales y a las respuestas adaptativas de los agentes ante la regulación.

En la Semana 1, utilizamos los Diagramas de Lazos Causales (CLDs, por sus siglas en inglés, *Causal Loop Diagrams*) para mapear este tipo de relaciones dentro del sistema energético. Los CLDs nos permitieron entender cualitativamente *qué* variables se conectan con cuáles. Nos permitieron trazar líneas claras mostrando que, por ejemplo, un aumento en el precio fomenta la inversión (+), y que una mayor inversión eventualmente incrementa la capacidad instalada (+), la cual a su vez aumenta el margen de reserva (+), disminuyendo finalmente el precio (−).

Sin embargo, a pesar de ser una herramienta conceptual poderosa para revelar la estructura subyacente, los CLDs tienen una limitación fundamental insalvable: son puramente estáticos en términos cuantitativos. Un CLD nos dice *qué* variable se conecta con cuál, y en qué dirección de influencia (positiva o negativa), pero no nos dice ni *cuánto* ni *cuándo*. No podemos saber si un retraso de 3 años genera oscilaciones suaves o destructivas, o si una caída de 10% en el precio reduce la inversión en un 5% o en un 50%. No podemos simular el comportamiento en el tiempo de un diagrama causal de manera rigurosa. Un CLD, por sí solo, no puede "correr" en un computador.

Para responder al *cuánto* y al *cuándo*, y para probar la verdadera robustez de nuestras hipótesis sistémicas, necesitamos dar el gran salto analítico desde el mapeo cualitativo hacia el modelamiento y la simulación cuantitativa rigurosa: necesitamos la **Dinámica de Sistemas** (System Dynamics o SD).

La Dinámica de Sistemas, desarrollada originalmente por Jay Forrester en el MIT en la década de 1950, nos permite tomar un modelo mental o un mapa causal y convertirlo en un sistema formal de ecuaciones diferenciales y algebraicas que podemos simular explícitamente en el tiempo utilizando herramientas computacionales. Esta metodología es el puente entre la comprensión teórica de la complejidad y el análisis riguroso de políticas. Nos permite observar directamente las consecuencias dinámicas de las interconexiones, medir el impacto preciso de los retardos y simular las no-linealidades, revelando exactamente cómo la estructura interna y física del sistema es la responsable de generar los comportamientos cíclicos y oscilatorios que observamos desconcertados en la realidad del mercado eléctrico.

---

## 2. La metáfora de la bañera: stocks y flujos

Para comprender verdaderamente y aplicar la Dinámica de Sistemas, debemos desaprender ciertas formas estáticas de ver el mundo y adoptar un nuevo vocabulario fundamental. El universo de la dinámica de sistemas, desde esta perspectiva analítica, no está compuesto por meras "variables" flotando sin distinción, sino que está rigurosamente estructurado por dos tipos de entidades elementales: los **stocks** (acumulaciones o niveles) y los **flujos** (tasas de cambio). La metáfora más intuitiva, poderosa y universalmente utilizada para entender esta distinción crítica es la de una bañera.

### El Concepto de Stock (Nivel)

> **Definición formal de Stock:** Un stock representa una acumulación de algo físico o inmaterial a lo largo del tiempo. Es la memoria del sistema. Los stocks definen el estado del sistema en cualquier instante dado e introducen demoras e inercia en la dinámica general.

En nuestra metáfora, el stock es, muy simplemente, la cantidad total de agua que se encuentra contenida dentro de la bañera en un segundo preciso.

Los stocks se miden en un instante específico del tiempo absoluto. Si detuviéramos el reloj del universo de golpe, congelando todo movimiento, podríamos medir o contar un stock. Podríamos contar exactamente cuántos Megavatios (MW) de capacidad están instalados hoy en el Sistema Interconectado Nacional, podríamos contar exactamente cuántos millones de pesos hay en la cuenta bancaria de una empresa generadora a las 23:59 del 31 de diciembre, o podríamos medir el volumen exacto de agua almacenada en el embalse del Guavio. Incluso los conceptos inmateriales pueden ser modelados como stocks: el nivel de confianza de los inversionistas institucionales en la regulación del país, el conocimiento acumulado en una organización, o el grado de aceptación social de un proyecto eólico en La Guajira.

### El Concepto de Flujo (Tasa de cambio)

> **Definición formal de Flujo:** Un flujo representa la tasa a la cual un stock está cambiando en el tiempo. Los flujos son las acciones, los procesos y las actividades que llenan o vacían los stocks. Un flujo no puede existir sin un horizonte temporal sobre el cual actuar.

Siguiendo con la metáfora, el grifo abierto que vierte agua frenéticamente en la bañera representa el *flujo de entrada*, mientras que el desagüe abierto por donde el agua escapa y se pierde representa el *flujo de salida*.

A diferencia de los stocks, los flujos siempre, invariablemente, se miden por unidad de tiempo. Nunca podemos hablar de un flujo sin hacer referencia a un intervalo temporal. Un flujo se mide en litros por *minuto*, en nuevos MW instalados por *año*, en dólares gastados por *mes*, en gigavatios-hora generados por *día*.

### La Ecuación Fundamental

La relación matemática intrínseca entre stocks y flujos constituye el corazón de la Dinámica de Sistemas. Se define matemáticamente mediante una ecuación diferencial fundamental, que no es otra cosa que el principio básico de conservación o balance de masas:

$$ \frac{dS(t)}{dt} = F_{entrada}(t) - F_{salida}(t) $$

Donde:
- $S(t)$ es el valor del Stock en el instante $t$.
- $\frac{dS(t)}{dt}$ es la derivada del stock con respecto al tiempo, es decir, su tasa de cambio instantánea.
- $F_{entrada}(t)$ es la suma de todas las tasas de flujo que ingresan y aumentan el stock.
- $F_{salida}(t)$ es la suma de todas las tasas de flujo que salen y disminuyen el stock.

Si queremos conocer el nivel absoluto del stock en un tiempo futuro $t$, simplemente integramos esta ecuación diferencial desde un tiempo inicial $t_0$ hasta $t$:

$$ S(t) = S(t_0) + \int_{t_0}^{t} \left[ F_{entrada}(\tau) - F_{salida}(\tau) \right] d\tau $$

Esta ecuación integral revela una verdad filosófica y práctica profunda sobre los sistemas: el estado actual del sistema ($S(t)$) depende inexorablemente de su pasado histórico ($S(t_0)$) y de la acumulación histórica de todas las acciones (flujos netos) a lo largo del tiempo. Los sistemas con grandes stocks tienen una enorme "inercia", no pueden cambiar de estado de manera instantánea, independientemente de lo grandes que sean los flujos. Una bañera vacía no se llena en cero segundos, sin importar qué tan abierto esté el grifo. Esta inercia es la semilla de los retardos en el sistema eléctrico.

### La Prueba de la Fotografía

A pesar de su aparente simplicidad, distinguir correctamente entre stocks y flujos puede ser extremadamente confuso en la práctica profesional, incluso para analistas con profunda formación matemática. Por lo tanto, en la Dinámica de Sistemas empleamos una **regla heurística** fundamental, simple pero infalible: "La Prueba de la Fotografía".

Imagine que tiene una cámara mágica que puede tomar una fotografía perfecta, congelando el universo entero en un instante preciso. Observe la fotografía estática resultante.
- **Si puede observar, contar o medir la variable en esa fotografía inmóvil, entonces la variable es indiscutiblemente un STOCK.** Por ejemplo, en una foto de una represa, puede ver el nivel del agua. En un balance general al 31 de diciembre, puede leer la deuda total.
- **Si no puede observar la variable en la fotografía, y requiere de una cámara de video (una grabación a lo largo de un período de tiempo) para poder medirla, entonces la variable es un FLUJO.** En una fotografía instantánea, el agua saliendo del grifo aparece congelada en el aire; es imposible saber si está saliendo a 1 litro por segundo o a 10 litros por segundo. Necesita filmarla durante, digamos, 5 segundos, recolectar el agua y medir el volumen para calcular la tasa. De igual forma, en un estado de resultados anuales, las ventas o los ingresos son flujos que ocurrieron *durante* todo el año.

### Ejemplos Didácticos Comparativos

Para afianzar el concepto, desarrollemos múltiples ejemplos contrastantes:

**Ejemplo 1: Dinámica Poblacional (El modelo canónico)**
Consideremos el modelo más básico de la población humana de un territorio (como Colombia).
- **Stock:** La población total (número de habitantes). Si congelo el tiempo el día del censo, puedo contar a cada habitante. Unidades: Personas.
- **Flujos de entrada:** La tasa de nacimientos (natalidad) y la tasa de inmigración hacia el territorio. Unidades: Personas / Año.
- **Flujos de salida:** La tasa de muertes (mortalidad) y la tasa de emigración del territorio. Unidades: Personas / Año.
*Dinámica:* La población de Colombia no cambia abruptamente de la noche a la mañana. Crece gradualmente día tras día a través del lento goteo acumulativo del flujo neto (Nacimientos + Inmigrantes - Muertes - Emigrantes).

**Ejemplo 2: Infraestructura del Mercado Eléctrico (El núcleo de este capítulo)**
Consideremos la capacidad instalada total de generación eléctrica en un país.
- **Stock:** La Capacidad Instalada Total operando en el sistema. Si congelo el sistema hoy, XM (el operador del mercado en Colombia) me puede decir que tenemos exactamente X cantidad de Megavatios (MW) instalados. Unidades: MW.
- **Flujos de entrada:** La Puesta en Operación Comercial de nuevas plantas de generación. Plantas hidroeléctricas, parques solares o térmicas que terminan su construcción y se conectan a la red. Unidades: MW / Mes o MW / Año.
- **Flujos de salida:** El Retiro o desmantelamiento de plantas generadoras viejas o económicamente inviables que salen definitivamente del sistema. Unidades: MW / Año.

**Ejemplo 3: Finanzas Corporativas de una Generadora**
- **Stock:** El Saldo de la Deuda de la empresa con los bancos, o el Balance de Caja. (Visible en el Balance General estático). Unidades: Millones de Dólares.
- **Flujo de entrada:** Nuevos desembolsos de créditos adquiridos, o los ingresos operativos por venta de energía a lo largo del mes. (Visible en el Estado de Resultados o Flujo de Efectivo). Unidades: Millones de Dólares / Mes.
- **Flujo de salida:** Amortizaciones al capital de la deuda, pagos de intereses, gastos operativos, dividendos pagados. Unidades: Millones de Dólares / Mes.

### Errores Comunes (Clave Pedagógica Crítica)

El error más frecuente, peligroso y extendido en estudiantes y analistas al iniciar en este campo es confundir flagrantemente stocks con flujos. Esta confusión no es meramente semántica; destruye completamente la validez matemática del modelo.

Por ejemplo, es muy común escuchar en medios o informes a analistas hablar del "déficit de energía de este año" como si fuera una acumulación estática que debemos "atacar", cuando en realidad el déficit energético es un flujo (una tasa a la cual estamos consumiendo más energía de la que podemos generar de forma sostenida, digamos en GWh / mes).

Otro error enorme en modelamiento corporativo es tratar el "Gasto de Capital" (CAPEX anual, que representa una inversión a lo largo del tiempo, por ende un flujo) como si fuera el activo fijo mismo (el stock físico de la planta construida).

La regla de oro para evitar este desastre es la verificación constante de la coherencia dimensional. Jamás se puede sumar directamente un stock y un flujo. La ecuación $Stock(t) = Stock(t-1) + Flujo$ es lógicamente defectuosa si no se multiplica el flujo por el intervalo de tiempo discreto $dt$. Es decir, $MW + (MW / Año)$ es dimensionalmente absurdo, como sumar manzanas y velocidades. La forma correcta en tiempo discreto (Euler) es $MW(hoy) = MW(ayer) + \left( \frac{MW}{A\tilde{n}o} \right) \cdot (1 \ A\tilde{n}o)$. Confundir estas naturalezas conduce inexorablemente a modelos que exhibirán fallas estructurales grotescas al ser simulados en Python o cualquier otra plataforma.

---

## 3. Los bloques de construcción de un modelo SD

Para estructurar modelos cuantitativos rigurosos y comunicables que puedan ser compartidos, revisados y validados por la comunidad técnica, la Dinámica de Sistemas emplea una notación formal visual estandarizada internacionalmente. Este lenguaje visual se plasma en lo que se conoce como el **Diagrama de Stocks y Flujos** (S&F Diagram).

El Diagrama de S&F no es simplemente un dibujo bonito; es una representación isomórfica (1 a 1) del sistema subyacente de ecuaciones diferenciales. Detrás de cada símbolo hay una matemática estricta. Esta notación consta de los siguientes elementos o "bloques de construcción":

### La Notación Visual

1. **Stocks (Acumulaciones / Niveles):**
   - **Símbolo:** Se dibujan de manera estricta como **rectángulos** (cajas).
   - **Significado:** Como discutimos, representan la acumulación de entidades.
   - **Analogía Matemática:** Representan las variables de estado ($x(t), y(t), z(t)$) del sistema dinámico. Son los resultados de las integraciones.

2. **Flujos (Tasas de cambio):**
   - **Símbolo:** Se dibujan como **flechas de doble línea** (como un tubo hueco por donde fluye líquido) que tienen una **válvula** (un círculo o un ícono de pajarita / reloj de arena) adherida en la mitad. El flujo siempre apunta hacia un stock (llenándolo) o desde un stock (vaciándolo), conectando a veces con "nubes" que representan orígenes o destinos fuera de los límites de nuestro modelo (fuentes y sumideros infinitos).
   - **Significado:** Representan el ritmo al cual el contenido material pasa hacia o desde el stock.
   - **Analogía Matemática:** Son las ecuaciones diferenciales en sí mismas, las derivadas con respecto al tiempo ($dx/dt, dy/dt$). La válvula representa la ecuación que calcula el valor del flujo en cada instante $t$.

3. **Auxiliares o Convertidores (Variables Intermedias):**
   - **Símbolo:** Se representan convencionalmente como simples **círculos** que contienen texto, o a veces solo como el nombre de la variable "flotando" en el espacio, pero claramente sin cajas ni tuberías.
   - **Significado:** Son piezas clave que permiten desglosar cálculos complejos. Se utilizan para almacenar constantes del sistema, parámetros exógenos fijos, o funciones algebraicas intermedias que toman información de varias partes del sistema y determinan el comportamiento final de las válvulas de flujo. Hacen que el modelo sea legible al fragmentar una enorme ecuación de flujo en sub-ecuaciones comprensibles.
   - **Analogía Matemática:** Son las funciones puramente algebraicas e instantáneas ($a = f(x, y)$), sin memoria ni acumulación.

4. **Conectores o Flechas de Información:**
   - **Símbolo:** Son **flechas de línea simple**, delgadas y frecuentemente curvas.
   - **Significado:** Transmiten *información* sobre el valor instantáneo de un stock o de una variable auxiliar hacia otra variable auxiliar o hacia una válvula de flujo.
   - **Característica Crítica:** Los conectores **no mueven material**. El hecho de que yo lea el termómetro del agua de la bañera (y envíe esa *información* a mi cerebro para cerrar la válvula) no saca ni una sola gota de agua de la bañera. Las flechas de información se utilizan para construir los enlaces causales que dictan las políticas y las decisiones dentro del modelo. Son los nervios del sistema.

### Tabla de Equivalencias y Coherencia

Para asegurar que un modelo es sólido, cada elemento debe estar meticulosamente definido. Observe la siguiente tabla que ejemplifica los bloques de construcción aplicados al sistema hidrológico de un embalse de generación eléctrica:

| Variable del Sistema | Tipo de Elemento SD | Unidades Físicas (Ejemplo) | Ecuación / Naturaleza Matemática |
| :--- | :--- | :--- | :--- |
| **Nivel del Embalse** | Stock (Caja) | Hectómetros cúbicos ($hm^3$) | $S(t_0) + \int_{t_0}^{t} (Aportes - Descargas - Vertimientos) d\tau$ |
| **Aportes (Lluvias/Río)** | Flujo de Entrada (Válvula) | $hm^3 / d\acute{\imath}a$ | Serie de tiempo exógena o dependiente del clima (ENSO). |
| **Descargas (Turbinado)** | Flujo de Salida (Válvula) | $hm^3 / d\acute{\imath}a$ | Función auxiliar de la Demanda de Energía, Precio, y reglas de operación de la planta. |
| **Capacidad Máxima** | Variable Auxiliar (Constante) | $hm^3$ | Valor fijo por diseño de la presa ($ej. 1,200 \ hm^3$). |
| **Porcentaje de Llenado** | Variable Auxiliar (Cálculo) | Adimensional (Fracción $0-1$ o $\%$) | Ecuación algebraica pura: `Nivel del Embalse / Capacidad Máxima` |
| **Decisión de Despacho** | Flecha de Información | No aplica (transmite el valor) | El operador observa (conector) el 'Porcentaje de Llenado' para determinar las 'Descargas'. |

### Ejemplo Trabajado Paso a Paso: Construyendo el Modelo de la Bañera Completo

Para dominar la construcción estructural, diseñemos desde cero un modelo SD mental de nuestra bañera que busca autogestionar su nivel de agua, emulando la gestión corporativa de un inventario o de capacidad en el sector.

1. **Definir el Estado Principal:** Comenzamos dibujando un rectángulo central grande. Lo etiquetamos `Agua en la bañera`. Este es nuestro stock.
2. **Definir los Procesos Físicos (Línea Principal):** Trazamos una tubería de doble línea entrando por la izquierda del rectángulo. Dibujamos una nube en su inicio (fuente infinita de agua), le ponemos una válvula en medio y la llamamos `Flujo de Grifo` (entrada). Luego trazamos otra tubería saliendo por la derecha del rectángulo hacia otra nube (drenaje), con su propia válvula, llamada `Flujo de Desagüe` (salida).
3. **Mecánica del Desagüe (Física):** El agua no drena mágicamente a un ritmo fijo. La física (presión hidrostática) dicta que a mayor volumen (y altura) de agua en la bañera, más fuerte será la presión sobre el orificio de salida, incrementando la tasa de flujo. Para representar esto, trazamos una *flecha de información* curva desde el rectángulo `Agua en la bañera` hacia la válvula `Flujo de Desagüe`.
4. **Parámetro del Desagüe:** Dibujamos un círculo auxiliar llamado `Constante de Drenaje` (basada en el tamaño del hueco) y conectamos una flecha de información desde él hacia el `Flujo de Desagüe`.
5. **Ecuación Resultante de Salida:** La válvula procesa esa información: `Flujo de Desagüe = Agua en la bañera * Constante de Drenaje`. Dimensionalidad: $[Litros] * [1/Minutos] = [Litros/Minuto]$. ¡Es coherente!
6. **Mecánica del Grifo (Política / Toma de Decisiones):** Queremos mantener el agua en un nivel ideal. Dibujamos un círculo auxiliar llamado `Nivel Deseado` (una meta en nuestra mente).
7. **El Bucle de Información (El "Cerebro"):** Trazamos una flecha de información desde el `Agua en la bañera` hacia un nuevo círculo auxiliar llamado `Brecha de Agua (Gap)`. Trazamos otra flecha desde `Nivel Deseado` hacia la misma `Brecha de Agua`. La ecuación en este auxiliar es simplemente: `Brecha = Nivel Deseado - Agua en la bañera`.
8. **Decisión Final:** Trazamos una flecha de información desde la `Brecha de Agua` hacia la válvula `Flujo de Grifo`. El comportamiento lógico es que nosotros abriremos el grifo proporcionalmente al error percibido. Así, `Flujo de Grifo = Brecha de Agua / Tiempo de Ajuste` (donde 'Tiempo de Ajuste' es nuestra velocidad de reacción mental y física).

Acabamos de transformar una simple bañera estática en un sistema cibernético dinámico realimentado, capturando simultáneamente procesos físicos inevitables y políticas de toma de decisión gerencial (humana). Este es el poder estructural del diagrama S&F.

---

## 4. Retroalimentación cuantitativa y las ecuaciones del comportamiento

En la Semana 1 introdujimos la idea cualitativa de que los bucles de retroalimentación (Feedback Loops) en un mapa causal determinan el comportamiento global. Vimos que existen bucles de refuerzo (R, positivos) que generan inestabilidad y bucles de balance (B, negativos) que buscan la estabilidad y el equilibrio. En Dinámica de Sistemas, debemos cruzar el puente hacia la formalidad absoluta, traduciendo esos simples signos de '+' y '−' de los CLDs en ecuaciones dinámicas continuas, explícitas y exactas.

Es a través del análisis de estas ecuaciones estructurales que descubrimos cómo la estructura genera el comportamiento.

### Lazo R Cuantitativo: El Crecimiento Exponencial Inevitable

Un bucle de refuerzo (Reforcing Loop) puro, sin restricciones, ocurre dinámicamente cuando un stock determina directa o indirectamente su propio flujo de entrada en proporción directa a su tamaño actual. Mientras más grande es el stock, mayor es el flujo que se le añade, haciendo que el stock crezca aún más rápido, en un ciclo virtuoso o vicioso incesante.

**La Ecuación Diferencial:**
La forma matemática más pura y canónica de un bucle de refuerzo es:
$$ \frac{dN(t)}{dt} = r \cdot N(t) $$

Donde:
- $N(t)$ es el valor numérico del stock (por ejemplo, población, dinero en el banco, MW eólicos instalados en una curva temprana de adopción tecnológica, infecciones en una pandemia).
- $r$ es la "tasa fraccional de crecimiento" neta (natalidad menos mortalidad, tasa de interés, factor de contagio). Se mide en unidades de $[1/Tiempo]$.

**La Solución Analítica y el Comportamiento:**
Cualquier estudiante de cálculo diferencial sabe que la única función qué es proporcional a su propia derivada es la función exponencial. Al resolver la ecuación por separación de variables, obtenemos la solución analítica exacta:
$$ N(t) = N_0 \cdot e^{r \cdot t} $$

Donde $N_0$ es el valor inicial del stock en el tiempo $t=0$, y $e$ es la base de los logaritmos naturales (aproximadamente 2.71828).
Esta solución genera la curva clásica de **crecimiento exponencial**. El comportamiento es engañoso: al principio, si $N_0$ es pequeño, el crecimiento parece lento, aburrido y lineal. Pero, inexorablemente, a medida que $N$ aumenta, el flujo ($r \cdot N$) se vuelve masivo, y la curva se dispara hacia arriba (como el "palo de hockey"). Este es el motor del interés compuesto financiero, de las burbujas de mercado y de la rápida penetración tecnológica cuando se cruza el *tipping point*. Físicamente, en un mundo finito, ningún ciclo 'R' puede persistir para siempre sin chocar eventualmente contra límites físicos o recursos finitos.

### Lazo B Cuantitativo: La Búsqueda de Meta y Convergencia Asintótica

Un bucle de balance (Balancing o Goal-Seeking Loop) puro ocurre cuando la estructura del sistema está diseñada explícitamente para buscar, mantener o alcanzar un objetivo específico o un estado de equilibrio en el tiempo, corrigiendo continuamente las desviaciones.

**La Ecuación Diferencial:**
El mecanismo fundamental de este ciclo requiere que el flujo actuante se ajuste siempre en proporción directa a la "brecha" (el error o *gap*) que existe entre el objetivo deseado y el estado actual real que posee el stock.
$$ \frac{dS(t)}{dt} = k \cdot (Objetivo - S(t)) $$

Donde:
- $S(t)$ es el stock actual.
- $Objetivo$ es la meta fija deseada (el nivel de inventario ideal, la temperatura del termostato, la capacidad firme requerida por el país).
- $k$ representa la "velocidad de ajuste". Dimensionalmente, $k$ es igual a $1 / \text{Tiempo de Ajuste}$.

**La Solución Analítica y el Comportamiento:**
Esta es una ecuación diferencial lineal de primer orden no homogénea. Su solución exacta, asumiendo un objetivo constante, es:
$$ S(t) = Objetivo - (Objetivo - S_0) \cdot e^{-k \cdot t} $$

Analizando esta ecuación, observamos que genera un comportamiento de **convergencia asintótica** suave. A medida que el tiempo avanza ($t \rightarrow \infty$), el término $e^{-k \cdot t}$ tiende a cero rápidamente (porque el exponente es negativo, denotando amortiguación). El sistema cierra suavemente la brecha y el stock $S(t)$ aterriza sobre el $Objetivo$ sin jamás sobrepasarlo, de una manera grácil y perfectamente calibrada. El sistema parece tener un control absoluto de sí mismo.

**¡PERO AQUÍ ESTÁ EL PROBLEMA CRÍTICO Y LA REVELACIÓN DE LA DINÁMICA DE SISTEMAS!**
El universo real (y particularmente el sector energético y de infraestructura colombiana) **casi nunca** funciona con bucles de balance puros y perfectamente instantáneos. En el mundo real, la información no viaja al instante, los informes toman meses en prepararse, las políticas tardan en diseñarse y, vitalmente, los proyectos físicos (el concreto y el acero) toman años en materializarse, fraguar y conectarse. Hay demoras.

### Lazo B con Retardo Temporal: El Génesis Matemático de las Oscilaciones

¿Qué sucede estructuralmente si existe una demora severa (un retardo o *delay*) entre el instante en que el sistema mide la brecha existente, toma la decisión correctiva de invertir o actuar, y el instante en que el efecto real y físico de dicha acción finalmente impacta y altera el estado del stock?
Esta pregunta aparentemente trivial es el núcleo de las crisis cíclicas de la economía moderna.

**La Ecuación Diferencial con Retraso (Delay Differential Equation - DDE):**
Modifiquemos ligeramente nuestra ecuación anterior para introducir una ceguera temporal:
$$ \frac{dS(t)}{dt} = k \cdot (Objetivo - S(t-\tau)) $$

Donde $\tau$ (letra griega *tau*) representa un tiempo de retardo duro y explícito. La ecuación nos dice: la tasa de cambio del stock hoy (en el instante $t$) no responde a la realidad de hoy, sino a la información obsoleta o a las decisiones tomadas hace $\tau$ unidades de tiempo atrás, basadas en el estado $S(t-\tau)$.

**El Comportamiento Matemático y Físico (Oscilación):**
A diferencia de las ecuaciones diferenciales ordinarias, las ecuaciones con retardo (DDE) requieren condiciones iniciales sobre todo un intervalo histórico, no solo un punto, y su espacio de soluciones es de dimensión infinita.
Dinámicamente, lo que ocurre es un desastre organizacional: El tomador de decisiones (el gobierno, el mercado, el inversionista) observa que el sistema está lejos del objetivo. Toma una acción correctiva agresiva abriendo una válvula. El sistema inicia la corrección. Sin embargo, debido al retardo $\tau$, la información de que el stock está mejorando o el flujo que efectivamente engrosaría el stock no llega de inmediato.
El tomador de decisiones percibe erróneamente que "nada ha pasado" o "la acción no fue suficiente". Sigue acelerando, sigue invirtiendo dinero a manos llenas. Finalmente, en el futuro, todas las decisiones acumuladas en el "tubo del retardo" llegan de golpe al stock simultáneamente. El stock no solo alcanza el objetivo, sino que lo pulveriza hacia arriba. Esto se llama **sobreimpulso (overshoot)**.

Al darse cuenta de que ahora hay un exceso grotesco (la oferta es muchísimo mayor que la demanda, los precios se desploman al piso), el decisor entra en pánico, frena toda inversión a cero y comienza a desmantelar. Pero, de nuevo, la escasez futura que esta falta de inversión generará no será visible hasta años después. El stock cae vertiginosamente, se hunde por debajo del objetivo (undershoot), disparando de nuevo alarmas frenéticas de escasez y pánico de apagón.
Según la ganancia, los parámetros y la forma del retardo, el sistema puede converger suavemente, sobrepasar la meta u oscilar. Un lazo de balance con retardo no garantiza un ciclo límite; el régimen debe comprobarse en las ecuaciones y mediante simulación.

> **EL INSIGHT CLAVE:** Esta demostración matemática establece de manera irrefutable que **la sola introducción estructural de un retardo (delay) temporal tiene el poder absoluto de convertir un bucle de balance que fue diseñado para ser inherentemente estable e inteligente, en un sistema crónicamente inestable que oscila de un extremo de crisis a otro sin fin aparente.**

---

## 5. Retardos: el motor incesante de las oscilaciones y el caos en la infraestructura

Habiendo demostrado matemáticamente la importancia suprema de los retardos, debemos explorar su fenomenología en el sector eléctrico. Los retardos (delays) son elementos omnipresentes, tenaces y fundamentalmente imposibles de eliminar de los sistemas de infraestructura pesada. Son el verdadero motor subyacente e invisible detrás de la dinámica fuertemente cíclica que castiga los balances corporativos y la confiabilidad del servicio.

En el lenguaje de SD, existen dos grandes familias o categorías principales de retardos:

### 1. Retardos Materiales (Material Delays)

Un retardo material es el tiempo estrictamente físico, regido por las leyes del universo o de la burocracia humana, que toma transformar, transportar, construir o desplazar un material de un estado físico a otro. Representan la conservación de masa o energía en tránsito, el pipeline, el "Work In Progress" (WIP) de la industria.

En el sector eléctrico colombiano, el retardo material más colosal y de mayor impacto económico es la fase de Construcción y Licenciamiento de un megaproyecto.
Desde el momento decisivo en que una junta directiva toma la Decisión Final de Inversión (FID - Final Investment Decision) motivada por altos precios o una subasta del Cargo por Confiabilidad, hasta el anhelado día en que una nueva central hidroeléctrica de 500 MW alcanza su Operación Comercial (COD - Commercial Operation Date), transcurre un abismo de tiempo.
Históricamente en el país, construir una hidroeléctrica mayor toma entre 4 a 7 años, enfrentando rigurosos retos de ingeniería civil, topografía compleja de los Andes, y largos procesos de licenciamiento ambiental (Autoridad Nacional de Licencias Ambientales - ANLA) y de consulta previa con comunidades locales. Incluso en proyectos teóricamente "más rápidos", como granjas solares o parques eólicos, los retardos para construir o expandir las imprescindibles redes de alta tensión por parte del operador transmisor pueden añadir años al proceso.
Durante todos estos años de espera del retardo material, los cientos de millones de dólares están inmovilizados, la planta no despacha un solo kilovatio a la red y, por lo tanto, no contribuye a bajar los altos precios que motivaron su construcción inicial.

### 2. Retardos de Información (Information Delays)

Un retardo de información, a diferencia del material, es un proceso inmaterial de orden psicológico, institucional o cognitivo. Es el tiempo, a menudo muy prolongado, que le toma a los seres humanos (o a instituciones colectivas completas) percibir la realidad de un cambio en el entorno subyacente, procesar conscientemente esa información entrante filtrándola de los ruidos aleatorios diarios (señal vs ruido), cambiar sus modelos mentales arraigados, modificar sus creencias y convicciones institucionales, y finalmente reaccionar formulando nuevas políticas u ordenando acciones.
Los retardos de información representan un suavizado exponencial (exponential smoothing) de la realidad.

Por ejemplo, consideremos la percepción de los agentes ante un incremento súbito del precio de la energía en la bolsa. Si el precio se dispara durante el mes de mayo, los grandes inversionistas o los miembros de la junta directiva no ordenan inmediatamente la construcción de plantas por billones de pesos. La psicología humana y la aversión al riesgo entran en juego; pensarán: *"Es un pico estacional, es un ruido coyuntural por mantenimiento de líneas, pasará rápido, esperemos a ver qué hace el mercado"*. Solo si el precio se mantiene obstinadamente alto durante 6, 8 o 12 meses consecutivos, la inercia cognitiva se rompe y los tomadores de decisiones actualizan sus pronósticos y admiten que el incremento de precio indica una escasez de oferta verdaderamente sistémica y de carácter tendencial (estructural), desencadenando así el flujo de decisiones financieras. Esta demora psicológica suma valiosos meses o años a la ceguera del sistema.

### ¿Por qué los retardos son mortales para la estabilidad?

Los retardos son profundamente desestabilizadores y "peligrosos" porque traen como consecuencia la dislocación y el desacople temporal de las acciones correctivas con respecto a sus impactos futuros.

En la vida humana diaria e intuitiva (pensamiento lineal y de corto plazo), operamos asumiendo que "causa y efecto están próximos en el tiempo y el espacio". Pero en sistemas con retardos largos, este atajo evolutivo mental es la receta del desastre: la decisión que resulta matemática y contextualmente "correcta, racional y justificada" en el tiempo actual $t$ basándose en la información visible en el hoy, puede llegar a ser una decisión trágicamente catastrófica en el tiempo futuro $t + 5$ años. ¿Por qué? Porque cuando se complete el retardo de 5 años para que el proyecto nazca, las condiciones exógenas e interconectadas del sistema completo ya han mutado dramáticamente (quizás la economía entró en recesión derrumbando el consumo de energía, o lo qué es peor, porque docenas de competidores cayeron exactamente en la misma trampa ilusoria y tomaron colectivamente la misma decisión "racional" al mismo tiempo que nosotros, generando un colapso del mercado).

### La Analogía de la Ducha (La alegoría perfecta)

Para cimentar definitivamente esta idea del "sobreimpulso inducido por la demora", recurrimos a un clásico de la literatura de complejidad de John Sterman: La analogía del usuario de hotel y la ducha engañosa.

Imagínese que usted entra por primera vez a un cuarto de hotel antiguo con una plomería pésimamente diseñada, en la que hay un retardo masivo de 10 o 15 segundos entre el giro de la perilla del grifo y el momento en que el agua con la nueva mezcla de temperaturas sale por la alcachofa de la ducha e impacta su cuerpo.
Entra con confianza a la ducha. El agua está asquerosamente fría. Su objetivo (la meta) es agua templada y agradable. Usted es el agente racional.
- $t=0$: El error (gap) entre la meta y la realidad es grande. Usted gira bruscamente la perilla hacia la marca roja de agua caliente.
- $t=2$ segundos: El agua sobre su espalda sigue congelada. Su cerebro lineal dice: "la acción fue insuficiente". Gira la perilla aún más hacia el rojo para "acelerar".
- $t=5$ segundos: Sigue helada. Usted, perdiendo la paciencia, gira la perilla hasta el tope extremo de calor máximo.
- $t=12$ segundos: ¡Peligro! El "pipeline" (retardo material de la tubería) finalmente entrega la mezcla acumulada. Un chorro de agua hirviendo le quema la espalda. Su error ahora es positivo y extremo.
- $t=13$ segundos: Por instinto de supervivencia de un choque térmico, da un manotazo frenético a la perilla girándola violenta y totalmente hacia la marca azul de agua fría para contrarrestar la quemadura.
- $t=16$ segundos: Continúa saliendo agua hirviendo (el nuevo retardo). Usted empuja la perilla más, asegurándose de que esté trabada en frío absoluto.
- $t=25$ segundos: El retardo culmina y llega el impacto: un torrente de agua glacial. Se vuelve a congelar.

El resultado trágico e inevitable de esta falta de sincronía es que el usuario (el tomador de decisiones) pasa toda su estadía dentro del sistema amplificando caóticamente el error de forma ininterrumpida, reaccionando siempre de forma exagerada ante información atrasada, oscilando brutalmente entre estados de congelación y quemadura severa. Jamás encuentra el equilibrio asintótico templado que quería.

**La traducción directa al mercado eléctrico:**
En el mercado, el gerente y su junta directiva ocupan el lugar del pobre usuario de la ducha, el precio de escasez (el mercado local o spot) es la sensación térmica dolorosa del agua fría en la espalda, y la decisión de firmar y emitir nueva deuda para construir y echar a andar una planta de generación es el acto de girar la perilla de la plomería de control de temperatura.

1. Perciben precios de bolsa sostenidamente altísimos *hoy*. Sufren porque sus previsiones o compras están al límite.
2. Deciden abrir la llave fuertemente e iniciar la construcción masiva y riesgosa de una central (y las demás empresas competidoras hacen lo mismo casi simultáneamente sin contarlo).
3. La central entra en el purgatorio del "Pipeline de Proyectos en Construcción" que, como nuestra tubería de hotel, toma inexorables años. Durante todo ese calvario (por ej., 4 largos años), el proyecto consume ingentes cantidades de flujo de caja libre, pero no inyecta ni un solo megavatio al saturado mercado; por ende, no mueve la aguja del precio, el cual se mantiene engañosamente alto y estresante, emitiendo falsas señales de mayor "sed" de inversión al resto del país, motivando un acopio de capital irracional y sucesivas e iterativas oleadas de proyectos.
4. En el año 4 o 5, la primera oleada de megaproyectos sale del tubo; al año siguiente, sale la segunda, y así. Una catarata monstruosa de oferta de energía inunda repentinamente los nodos de conexión de la red.
5. El sistema sufre de un ataque agudo de sobrecapacidad endémica (sobreoferta de potencia firme) frente a una demanda deprimida. La consecuencia ineludible bajo un esquema de despacho económico competitivo es que los precios colapsan rápida, drástica y destructivamente. El "agua está hirviendo" de sobreoferta.
6. Ahora todas las empresas tienen sus balances generales teñidos de rojo carmesí: cargan pasivos y deudas colosales atados a sus costosas plantas nuevas, pero sus ingresos operacionales están deprimidos por la ruina de los precios. El pánico se apodera. Ordenan inmediatamente un congelamiento drástico, absoluto y dogmático, impidiendo cualquier nueva inversión a 10 años, desmantelando los equipos de ingeniería temprana. Giran la perilla frenéticamente hacia el "congelamiento" de la inversión (el agua fría).
7. La demanda subyacente, impasible, sigue un lento y silencioso arrastre ascendente cada año asociado al PIB; mientras tanto, el retardo asegura que no haya nueva oferta. Inevitablemente, a largo plazo la capacidad sobrante es digerida y desaparece. Los precios de bolsa repuntan... un nuevo pánico de escasez, y la junta directiva repite su trágico destino. Así es como la dinámica interna domina la realidad de los ciclos.

---

## 6. El caso: el ciclo de inversión-capacidad colombiano y sus oscilaciones

En Colombia, tras el monumental racionamiento, crisis y apagones ocurridos durante las sequías vinculadas a El Niño a principios de los años noventa y la posterior modernización y total reestructuración y privatización parcial del sector (hacia un mercado desregulado competitivo administrado centralmente), el comportamiento endógeno y dinámico del mercado ha estado poderosamente marcado por estos dramáticos ciclos de capital e inversión. La Resolución CREG 071 de 2006 (la metodología fundamental del "Cargo por Confiabilidad") introdujo fuertes incentivos remuneratorios a mediano plazo para garantizar que las plantas de última hora estuviesen disponibles cuando los aportes hidrológicos (lluvia) fallaran, buscando domar el precio, pero la macroestructura cíclica ha persistido notablemente, ya que los retardos estructurales son imposibles de legislar o eliminar por decreto del regulador.

Vamos a detallar rigurosamente la construcción del modelo clásico en Dinámica de Sistemas (una variante sofisticada de modelo predador-presa del tipo Goodwin y los trabajos fundacionales de Ford, Sterman, y Arango/Larsen sobre mercados eléctricos) de este fenómeno cíclico en el mercado de energía.

### Definición de los Sectores y Estructuras Fundamentales (Stocks y Flujos)

Para modelar matemáticamente las entrañas de este mercado, definimos y aislamos estrictamente tres grandes stocks o variables de estado que determinan inercialmente las condiciones físicas y financieras del sistema. Toda la dinámica emerge de estos tres tanques:

1. `Capacidad_Instalada` (Unidades: Megavatios, MW): Este es el inventario tangible y visible que opera despachando energía al país. Refleja exclusivamente el acervo acumulado de todas las plantas de generación que están construidas, probadas, sincronizadas y físicamente operando inyectando energía a la red interconectada.
2. `Proyectos_en_Construccion` (Unidades: MW): Este stock funciona matemáticamente como un "estado de retardo" (un *delay state* de orden mayor). Representa todo el volumen en megavatios (agregado país) de los proyectos "en el limbo del pipeline": los diseños ya aprobados (FID), el acero en transporte marítimo, el concreto vertiéndose en el cañón, la tuneladora activa, pero que **aún no aportan** ningún megavatio de oferta ni presionan los precios a la baja porque están atrapados transitando la demora. Son una fuerza oculta latente.
3. `Demanda_Base_Proyectada` (Unidades: MW Pico o GWh requeridos por periodo de análisis prolongado): Refleja de manera simplificada las necesidades energéticas crecientes del crecimiento de la población, el auge de centros de datos, o la electrificación general (movilidad, calefacción) y los requerimientos tendenciales de un país en desarrollo.

### Modelado de las Tasas de Cambio Críticas (Flujos)

Las tasas de transformación que bombean o drenan los stocks antes mencionados, impulsando así toda la inestabilidad y el tiempo, se parametrizan en:

- `Flujo: inicio_de_nuevos_proyectos` (Unidades: $MW/\text{A\tilde{n}o}$): Este flujo representa la tasa activa en la cual juntas y financistas abren nuevas llaves y empujan MW a fase constructiva (entra al stock `Proyectos_en_Construccion`). Está gobernado absoluta e integralmente por la rentabilidad financiera esperada de mediano y largo plazo, la cual, a falta de futuros perfectos líquidos profundos de 10 años, depende fuertemente como proxi anclado del precio actual y sus pronósticos adaptativos.
- `Flujo: puesta_en_servicio_comercial` (Unidades: $MW/\text{A\tilde{n}o}$): El flujo crítico material. Sale incesantemente de `Proyectos_en_Construccion` y deposita su carga en `Capacidad_Instalada`. Matemáticamente, en primera aproximación, representa un retardo exponencial (o una cadena de Erlang de demoras tipo *pipeline*) igual a: $\text{Puesta\_en\_Servicio} = \frac{\text{Proyectos\_en\_Construccion}}{\text{Tiempo\_Construccion\_Promedio}}$. Aquí reside el embudo físico y regulatorio temporal (los $\tau$ años de la construcción pesada e hidroléctrica).
- `Flujo: retiro_y_obsolescencia` (Unidades: $MW/\text{A\tilde{n}o}$): Es el goteo final (vaciado) que extrae MW funcionales fuera de la `Capacidad_Instalada` porque las plantas cumplen su rígida vida contable (p.ej., 40 a 50 años térmico o hidroeléctrico), padecen colapsos mecánicos irremediables o caen victimas inexorables ante normativas de carbono.
- `Flujo: crecimiento_agregado_demanda` (Unidades: $MW/\text{A\tilde{n}o}$): Una válvula que incrementa continuamente, inyectando presión exógena (aunque predecible a grandes trazos) sobre el stock vital de consumo, usualmente indexado a la elasticidad-ingreso, PIB país y población.

### La Función de Retroalimentación y la Matemática No-Lineal (Auxiliares Críticos)

¿Cómo unimos todos estos subsistemas mecánicos en un círculo de retroalimentación? Con el mercado, la información económica y los conectores (nervios).

- `Auxiliar: gap_oferta_demanda` (El Margen o Reservas Técnicas). Se define estructuralmente como un comparador de tensiones. Mide la diferencia fundamental relativa entre la demanda máxima estresada y la capacidad de reserva en firme total asegurada que brinda la base `Capacidad_Instalada` despachable.
- `Auxiliar: precio_esperado_de_bolsa_y_escasez`. **Aquí reside un hallazgo monumental y crítico sobre la no-linealidad que estudiamos de soslayo en la Semana 1.** El precio del mercado libre de energía *no* responde o escala de forma lineal apaciguada con respecto a la caída del margen de seguridad del sistema eléctrico. Presenta un quiebre agresivo.
  * Si el sistema país detenta un holgado margen de reserva (alta `Capacidad_Instalada` oprimida deprimida contra baja `Demanda`), los algoritmos de despacho por orden de demérito ubican generadores muy eficientes fijando el precio (renovables, hidráulicas base) que luchan a la baja por despachar y ofertan costos marginales diminutos. El precio del mercado es muy bajo y peligrosamente plano, un desierto sin señales fuertes ante sobreinversiones pasadas.
  * Sin embargo, cuando la holgura y el margen técnico se deteriora (ya sea porque subió la demanda silente por 5 años sin inversiones simultáneas, o un El Niño masivo evapora los embalses restando energía firme hidráulica y provocando sequía hidroeléctrica despachable real), el sistema requiere irremediablemente forzar, arrancar y despachar centrales de generación carísimas que usan costosos e ineficientes combustibles pesados (Acpm importado, Diésel logístico en camiones, Gas Natural importado ultra caro en FSRU (regasificadoras marinas en costas de Cartagena y Pacífico)).
  * El despacho pasa abruptamente a usar estas tecnologías en el fondo de curva, generando que el precio del mercado salte repentinamente de forma brutal, **exponencial**, marcando $2X, 3X, 5X$ e incluso $10X$ múltiplos frente a los niveles confortables estáticos. Por ende, la curva de la función de 'precio vs capacidad relativa' dibuja de forma irrefutable un patrón exponencial y severamente asimétrico de "palo de hockey". Esta profunda no-linealidad amplifica de manera aterradora cualquier mínima insuficiencia relativa en el balance o brecha `gap_oferta_demanda`, disparando sirenas estrepitosas en los análisis bancarios.

### El Cierre del Bucle (The Causal Loop Closure)

Finalmente, una gran y gruesa flecha curva de información macro cierra y sella un gigantesco anillo cibernético masivo de realimentación retardada (el Feedback Bucle Crítico): La señal amplificada no-linealmente de `precio_esperado_de_bolsa` viaja y se inyecta directamente al origen o control exógeno determinando el multiplicador de inversiones base del flujo primordial `inicio_de_nuevos_proyectos`. A medida que precios saltan violentos por la asimétrica escasez, inyectan euforia inversora extrema, descorchando masivas adiciones futuras al flujo de nuevas presas de agua, turbinas y acero al "pipeline retardado".


### Calibracion Realista y Resultados Dinamicos

Cuando calibramos este modelo con parametros colombianos historicos — un retardo de construccion promedio de $\tau \approx 4$ a $6$ años para grandes proyectos hidroelectricos, una vida util infraestructural de aproximadamente $40$ años, y un crecimiento tendencial de la demanda del $3\%$ al $4\%$ anual —, la simulación produce un resultado revelador.

Sin necesidad de introducir ninguna perturbacion externa (sin fenomenos de El Niño, sin crisis geopoliticas, sin shocks de precios de combustibles), el modelo genera endogenamente **oscilaciones sostenidas** con periodos de aproximadamente 7 a 12 años. Estas ondas alternan entre fases de sobreinversion euforica (boom) y fases prolongadas de sequia de inversión (bust), con los precios de bolsa oscilando violentamente entre picos de escasez y valles de sobreoferta.

Lo notable es que estas oscilaciones simuladas coinciden con los ciclos historicos observados en el mercado eléctrico colombiano desde la reestructuracion de los años noventa. Esto nos conduce al insight central de la Semana 4:

> **El modelo ilustra que una estructura con inversión, retardos y precios no lineales puede generar oscilaciones endógenas. Esto no determina por sí solo cuánto de las oscilaciones históricas proviene de esa estructura o de choques externos como El Niño; esa atribución requiere evidencia y contraste adicionales.**

Los fenomenos climaticos como El Niño actuan como **disparadores y amplificadores** de un ciclo que ya reside latente en la estructura del mercado. Aceleran la crisis, sincronizan las respuestas de los agentes y magnifican la amplitud de las oscilaciones, pero no las originan. Un modelo que culpa exclusivamente al clima por las crisis del sector esta confundiendo el catalizador con la causa raiz — un error analitico que conduce a politicas ineficaces.

**Parametros empiricos para la calibracion (Saga 0 — Radiografia de Datos):**

Los datos reales del SIN colombiano (fuente: API publica de XM, 2000-2025) permiten calibrar el modelo con evidencia empirica directa:

| Parametro del modelo | Valor supuesto | Valor empírico (XM) | Observacion |
|---------------------|---------------|---------------------|-------------|
| Precio de equilibrio | 150 COP/kWh | 180 COP/kWh (promedio 2000-2024) | El modelo subestima ligeramente el precio base |
| Precio maximo modelable | 600 COP/kWh | 2,822 COP/kWh (El Niño 2015) | El modelo subestima los picos por un factor de ~5x |
| Retardo de construccion | 4 años | 3-5 años (cross-correlacion precio-capacidad) | Confirmado empiricamente |
| Crecimiento de demanda | 2.5%/año | ~3%/año (crecimiento real 2000-2024) | El modelo subestima ligeramente |
| Generación 2024 | — | 83 TWh | Condicion de referencia para validacion |
| Demanda maxima 2024 | — | 11.7 GW | Techo de capacidad requerida |
| Relacion embalse-precio | Lineal (k_precio) | **Exponencial** (R$^2$ = 0.13 en log-space) | El modelo necesita no-linealidad exponencial |
| Curtosis de precios | Normal (3) | **22.2** | Confirma distribuciones fat-tailed |

Estos parametros se utilizan directamente en los notebooks de la Saga para calibrar y validar el modelo de inversión-capacidad.

---


## 7. Python para dinámica de sistemas

### Por que Python y no Vensim

La Dinámica de Sistemas tiene una larga tradicion de software especializado con interfaces graficas de arrastrar y soltar: Vensim, Stella/iThink, AnyLogic. Estas herramientas son excelentes para la ensenanza introductoria y para la comunicacion visual con stakeholders no tecnicos. Sin embargo, en un programa de maestria orientado a la analitica avanzada, optamos por Python por tres razones estrategicas:

1. **Reproducibilidad y control de versiones.** Un modelo en Python es codigo fuente puro: se versiona con Git, se revisa en pull requests, se documenta con docstrings. Un modelo en Vensim es un archivo binario opaco que no permite trazabilidad granular de cambios.

2. **Integracion con el ecosistema de datos.** Python permite conectar el modelo SD directamente con pipelines de datos reales (pandas), visualizacion avanzada (matplotlib, plotly), optimizacion (scipy.optimize), análisis de sensibilidad (SALib), y machine learning (scikit-learn). En Vensim, exportar resultados para cruzarlos con otras herramientas requiere pasos manuales fragiles.

3. **Escalabilidad y despliegue.** Un modelo en Python se puede empaquetar como API, desplegarse en la nube, integrarse en dashboards interactivos (Streamlit, Dash) y ejecutarse en paralelo para miles de escenarios. Estas capacidades son fundamentales para la toma de decisiones robusta que veremos en la Semana 5.

La desventaja es clara: Python requiere programar las ecuaciones explicitamente, sin la comodidad visual de arrastrar cajas. Pero esta desventaja es, en realidad, una virtud pedagogica: obliga al modelador a entender cada ecuacion, cada unidad dimensional y cada supuesto, en lugar de confiar ciegamente en una interfaz.

### Integracion numerica con `scipy.integrate.solve_ivp`

Para resolver sistemas de ecuaciones diferenciales ordinarias (EDOs) en Python, utilizamos la funcion `solve_ivp` del módulo `scipy.integrate`. Esta funcion implementa multiples metodos de integracion numerica (RK45, RK23, Radau, BDF) y maneja automaticamente el control de paso adaptativo para garantizar precision numerica.

El patron de diseno para cualquier modelo SD en Python sigue tres pasos:

1. **Definir la funcion del sistema** que recibe el tiempo $t$, el vector de estados $y$, y los parametros, y retorna el vector de derivadas $dy/dt$.
2. **Especificar condiciones iniciales** y el horizonte de simulación.
3. **Llamar a `solve_ivp`** y analizar los resultados.

```python
import numpy as np
from scipy.integrate import solve_ivp

# 1. Definir el sistema de ecuaciones (las valvulas del diagrama S&F)
def modelo_mercado_electrico(t, estado, params):
    cap_instalada, pipeline, demanda = estado
    
    # Auxiliares: gap y precio (no-linealidad exponencial)
    gap = (demanda - cap_instalada) / demanda
    precio = params['p0'] * np.exp(params['k_curva'] * gap)
    
    # Flujos
    inicio_proyectos = np.where(
        precio > params['umbral'],
        params['sensibilidad'] * (precio - params['umbral']), 0
    )
    puesta_en_servicio = pipeline / params['retardo_construccion']
    retiro = cap_instalada / params['vida_util']
    crec_demanda = demanda * params['tasa_crecimiento']
    
    # Derivadas (d/dt de cada stock)
    return [
        puesta_en_servicio - retiro,        # d(capacidad)/dt
        inicio_proyectos - puesta_en_servicio,  # d(pipeline)/dt
        crec_demanda                         # d(demanda)/dt
    ]

# 2. Condiciones iniciales y parametros
y0 = [15000, 2000, 14000]  # MW, MW, MW
params = {
    'p0': 80, 'k_curva': 8, 'umbral': 120,
    'sensibilidad': 15, 'retardo_construccion': 5,
    'vida_util': 40, 'tasa_crecimiento': 0.035
}

# 3. Resolver e integrar
sol = solve_ivp(
    fun=modelo_mercado_electrico,
    t_span=(0, 30), y0=y0,
    args=(params,),
    t_eval=np.linspace(0, 30, 360)
)
```

En los laboratorios del curso, utilizaremos el módulo `mise_utils.dynamics`, que encapsula esta logica en funciones de alto nivel como `modelo_inversion_con_cxc_fncer()` y `plot_ciclo_inversion()`, permitiendo enfocarse en la experimentacion de politicas sin preocuparse por la fontaneria numerica.

---

## 8. Arquetipos sistemicos: comprender antes de calcular

Antes de lanzar simulaciones masivas, el analista senior debe entrenar su capacidad de reconocer patrones. La literatura clasica de Dinámica de Sistemas (Senge, Sterman, Meadows) ha identificado un conjunto reducido de **arquetipos sistemicos**: combinaciones recurrentes de bucles de refuerzo y balance que generan patologias predecibles en organizaciones, mercados e industrias.

Estos arquetipos son herramientas de diagnostico rapido. Permiten al consultor mirar un sistema problematico y decir: *"Reconozco este patron — es un Fixes that Fail"*, antes de invertir semanas en construir un modelo completo.

### 1. Fixes that Fail (Soluciones contraproducentes)

**Estructura:** Un problema genera un sintoma doloroso. Se aplica una solucion rapida que alivia el sintoma inmediatamente (bucle B rapido), pero que produce consecuencias secundarias retardadas que empeoran el problema original (bucle R lento).

**Ejemplo energetico:** El gobierno impone un tope de precios al mercado spot durante una crisis de escasez para proteger al consumidor. El alivio es inmediato: las facturas no suben. Pero la consecuencia retardada es letal: al suprimir la senal de precio alto, se elimina el incentivo para que los inversionistas construyan nueva capacidad. Meses despues, la escasez se profundiza porque no hubo inversión, y el racionamiento se vuelve inevitable.

**Leccion:** La solucion rapida destruyo la senal que el sistema necesitaba para autocorregirse.

### 2. Shifting the Burden (Desplazamiento de la carga)

**Estructura:** Ante un problema cronico, se recurre repetidamente a una solucion sintomatica facil en lugar de abordar la solucion fundamental (mas dificil, mas lenta, pero duradera). Con el tiempo, la dependencia de la solucion sintomatica atrofia la capacidad del sistema para implementar la solucion real.

**Ejemplo energetico:** Colombia importa Gas Natural Licuado (GNL) a traves de plantas regasificadoras (FSRU) para cubrir deficits de gas durante picos de demanda, en lugar de invertir en exploracion y produccion domestica de gas o en diversificacion hacia renovables. Cada importacion resuelve la crisis inmediata, pero la dependencia creciente del GNL importado (con precios en dolares, sujeto a volatilidad geopolitica) debilita el incentivo para desarrollar alternativas locales. La capacidad domestica de produccion de gas declina por falta de inversión, haciendo al pais mas vulnerable a cada nueva crisis.

**Leccion:** La solucion sintomatica se convierte en adiccion, y la solucion fundamental se vuelve cada vez mas inalcanzable.

### 3. Limits to Growth (Limites al crecimiento)

**Estructura:** Un proceso de crecimiento exitoso (bucle R) eventualmente encuentra una restriccion o limite (bucle B) que frena o revierte el crecimiento. Cuanto mas exito tiene el proceso inicial, mas fuerte se activa el freno.

**Ejemplo energetico:** El boom de energía eolica en La Guajira colombiana (impulsado por excelentes condiciones de viento y costos decrecientes) choca contra los limites de la infraestructura de transmision. Las líneas de alta tension necesarias para evacuar la energía desde La Guajira hacia los centros de consumo toman años en construirse y enfrentan oposicion de comunidades indigenas. El resultado: miles de MW de proyectos eolicos aprobados y financiados que no pueden operar porque no hay red que los conecte.

**Leccion:** El exito del crecimiento genera su propia restriccion. La solucion no esta en empujar mas fuerte el motor de crecimiento (mas subastas eolicas), sino en aliviar el cuello de botella (acelerar la transmision).

### Aplicacion al sector colombiano

En la historia reciente del sector eléctrico colombiano, los tres arquetipos operan simultaneamente. Las intervenciones de precios para proteger consumidores (Fixes that Fail) conviven con la dependencia de importaciones de GNL (Shifting the Burden) y con el cuello de botella de transmision que frena las FNCER (Limits to Growth). Identificar cual arquetipo domina en cada coyuntura es el primer paso para disenar intervenciones que ataquen las causas estructurales, no los sintomas.

*(Referencia fundamental: Sterman, J. D. (2000). Business Dynamics, Cap. 5-6; Meadows, D. H. (2008). Thinking in Systems, Cap. 3; Senge, P. (1990). The Fifth Discipline, Cap. 6.)*

---

## 9. Resumen y puente a Semana 5

En esta Semana 4 hemos dado el salto desde el análisis cualitativo (CLDs) hacia el modelado cuantitativo riguroso. Los conceptos centrales que deben quedar consolidados son:

- **Stock y flujo** son los bloques fundamentales de todo modelo SD. La prueba de la fotografia distingue entre ambos de forma inequivoca.
- **La ecuacion fundamental** $dS/dt = F_{entrada} - F_{salida}$ es la base matematica de toda la simulación.
- **Los retardos** transforman bucles estabilizadores en osciladores. La analogia de la ducha y el ciclo de inversión colombiano son manifestaciones del mismo fenomeno estructural.
- **La no-linealidad** de la formacion de precios amplifica las oscilaciones, creando la asimetria caracteristica del "palo de hockey".
- **Los arquetipos** permiten diagnosticar patologias recurrentes sin necesidad de un modelo formal completo.
- **Python** es la plataforma que nos permite integrar todo esto en un flujo de trabajo reproducible y escalable.

En la **Semana 5**, daremos el siguiente paso: aprenderemos a **intervenir** en estos modelos y a **evaluar** nuestras intervenciones bajo incertidumbre. Pasaremos de preguntarnos "¿por que oscila el sistema?" a preguntarnos "¿que política funciona mejor cuando no sabemos que futuro enfrentamos?". Introduciremos el pensamiento de escenarios, las tablas de robustez y el criterio de Minimax Regret — herramientas que transforman al analista en consultor estrategico.

---

### Glosario

- **Stock (Nivel):** Variable de acumulacion, medible en un instante, representada como rectangulo en diagramas S&F. Unidades: [cantidad].
- **Flujo (Tasa):** Variable de cambio, medible solo durante un intervalo, representada como valvula. Unidades: [cantidad/tiempo].
- **Retardo (Delay):** Tiempo que transcurre entre una accion y su efecto. Puede ser material (construccion) o de informacion (percepcion).
- **Sobreimpulso (Overshoot):** Cuando un sistema con retardo sobrepasa su objetivo antes de corregir, generando oscilaciones.
- **Solve_ivp:** Funcion de `scipy.integrate` para resolver problemas de valor inicial en sistemas de EDOs.
- **Arquetipo sistemico:** Patron estructural recurrente de bucles de retroalimentacion que genera comportamientos problematicos predecibles.
- **Fixes that Fail:** Arquetipo donde una solucion rapida empeora el problema original a traves de consecuencias retardadas.
- **Shifting the Burden:** Arquetipo donde la dependencia de soluciones sintomaticas atrofia la capacidad de resolver el problema de raiz.
- **Limits to Growth:** Arquetipo donde un proceso exitoso de crecimiento activa restricciones que lo frenan.

### Referencias

- Arango, S., & Larsen, E. R. (2011). "Cycles in deregulated electricity markets: Empirical evidence from two decades". *Energy Policy*, 39(5), 2457-2466.
- Ford, A. (1997). "System Dynamics and the Electric Power Industry". *System Dynamics Review*, 13(1), 57-85.
- Forrester, J. W. (1961). *Industrial Dynamics*. MIT Press.
- Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Chelsea Green Publishing.
- Senge, P. (1990). *The Fifth Discipline: The Art and Practice of the Learning Organization*. Doubleday.
- Sterman, J. D. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World*. McGraw-Hill.
