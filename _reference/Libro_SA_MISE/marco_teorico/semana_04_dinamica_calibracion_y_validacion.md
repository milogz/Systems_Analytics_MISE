# Semana 4. Dinámica: construir y contrastar mecanismos


## Primera capa. La bañera: ver la memoria del sistema

Antes de mirar una central hidroeléctrica, abre mentalmente un grifo. La bañera contiene 20 litros; entran cinco litros por minuto y salen tres. ¿Cuánto habrá después de diez minutos? La diferencia de dos litros por minuto añade veinte litros: habrá cuarenta, suponiendo que no desborde y que ambos flujos permanezcan constantes. La cuenta es sencilla; distinguir qué se acumula y qué cambia esa acumulación es la parte fundamental.

Ahora reduce la entrada de cinco a cuatro. ¿Baja el agua? No: sigue entrando más de lo que sale. El nivel continúa creciendo, aunque más despacio. Este es un error frecuente al leer gráficas: confundir una reducción de la tasa de crecimiento con una reducción del nivel. El notebook dibuja ambos para que podamos observarlo.

La prueba de la fotografía del original sigue siendo útil. Una foto puede representar agua almacenada en un instante. Para interpretar litros por minuto necesitamos un intervalo y una convención de medida. En un modelo social también podemos representar memoria, pero llamar «stock» a confianza no la convierte en una cantidad directamente medible. Hay que definir indicador, mecanismo y observación.

## Segunda capa. Construir la ecuación antes de llamar al integrador

Escribimos `S(t+dt)=S(t)+dt*(entrada−salida)`. Si S está en litros y los flujos en litros/minuto, dt debe estar en minutos. Multiplicar flujo por duración produce litros. Una comprobación dimensional tan pequeña evita trasladar errores grandes a los modelos energéticos.

Con flujos constantes existe una solución exacta: `S(t)=S0+(entrada−salida)*t`. La compararemos con nuestra tabla. Después haremos que la salida dependa del nivel: `salida=k*S`. Es una aproximación lineal de vaciado, útil para aprender realimentación; no es la ley exacta de un orificio bajo gravedad. Su unidad exige k en 1/minuto. Con entrada constante, el equilibrio es entrada/k, no cero.

La solución de ese segundo modelo es `S(t)=entrada/k+(S0−entrada/k)*exp(−k*t)`. Si aumentamos k, cambia el nivel de equilibrio y también la rapidez de acercamiento. Al interpretar una curva, separaremos ambos efectos. Esta comprobación analítica permite detectar si el programa representa realmente la ecuación.

Ahora aparece la ducha del relato original. Cuando giramos la llave, el agua que sentimos puede reflejar una decisión anterior. Si volvemos a corregir antes de observar su efecto, podemos sobrepasar la temperatura buscada. No todas las demoras producen oscilación: importan intensidad de respuesta y estructura. En el modelo de inversión observaremos esa combinación sin anunciar el resultado antes de calcularlo.

El Beer Game introduce otra memoria: pedidos en tránsito. Si cada participante responde solo a su inventario y olvida lo ya pedido, puede pedir demasiado. El paralelo con proyectos en construcción es fértil: la capacidad futura depende de lo que ya está en pipeline. El modelo profesional tendría que distinguir fechas, probabilidad de terminación y restricciones; una demora promedio es una simplificación que debemos reconocer.

## Tercera capa. Agua hoy, servicio mañana y decisiones que tardan

El almacenamiento vuelve importante el orden de los eventos. Dos años con iguales aportes totales pueden producir resultados diferentes si cambia su secuencia y existe un límite de embalse. Un período abundante puede causar vertimientos; el agua que no cabe no queda disponible para una sequía posterior. En el caso haremos precisamente ese experimento, con aportes sintéticos y balances auditables.

La planificación hidrotérmica incorpora representación de operación, incertidumbre y valor del agua. Es el estudio pertinente cuando necesitamos evaluar abastecimiento con suficiente detalle. La dinámica de sistemas ayuda a explorar cómo inversión, expectativas y demoras modifican la capacidad futura. Ninguna sustituye automáticamente a la otra. Podemos conectar una hipótesis de entrada de proyectos con escenarios de operación sin pretender que un modelo pequeño resuelva todo.

La comparación contra estadísticas históricas sigue siendo indispensable. Ajustar una tendencia de demanda permite aprender calibración y prueba temporal, pero no calibra el embalse ni las decisiones de inversión. Nuestro trabajo profesional consiste en conservar esa frontera y proponer cómo cruzarla con observaciones pertinentes, no en renombrar un ejercicio como validación nacional.


## Desarrollo y contraste profesional

**Pregunta:** ¿cómo distinguir un modelo que ejecuta de uno que representa adecuadamente la pregunta? RAC3. Entrega: ecuaciones y unidades, un experimento de mecanismo, un ajuste empírico delimitado y evidencia de validación.

## Stocks y flujos con dimensiones

Un stock acumula: agua almacenada en m³, energía almacenada en MWh equivalentes, capacidad construida en MW. Un flujo cambia el stock por unidad de tiempo: m³/s, MWh/mes o MW/año. La ecuación general `stock_final = stock_inicial + entradas − salidas` exige que las cantidades integradas compartan unidad y período.

Demanda de potencia es una tasa de uso de energía. Puede representarse como variable de estado de una ecuación de crecimiento, pero no es un inventario físico de electricidad. Un cambio de MW pico no informa directamente el crecimiento de GWh anuales: también importa la curva de carga.

Un embalse expresado en porcentaje necesita denominador para convertirse en volumen o energía. El porcentaje agregado de la serie suministrada se conserva como indicador; no lo multiplicamos por una capacidad arbitraria para inventar energía disponible. El modelo docente usa un **almacén ficticio en MWh equivalentes**, con conversión agua–energía constante. Omite variación de cabeza, eficiencia, cascadas y restricciones ambientales; esas omisiones delimitan sus usos.

## El modelo de embalse energético

Cada mes recibe aportes sintéticos, atiende producción hidro y vierte el excedente que no cabe. Se verifican dos balances independientes:

`almacén_final = almacén_inicial + aportes − hidro − vertimiento`;

`demanda = solar + hidro + térmica + faltante`.

Los límites mensuales de generación se construyen como `MW × horas_del_mes`. Los aportes y el almacén limitan energía; la turbina limita potencia. La regla docente atiende solar, luego hidro disponible y después térmica. Es miope: no optimiza el valor futuro del agua. Una política que conserve agua para meses secos puede producir trayectorias diferentes y es una extensión justificable.

El faltante mensual mide demanda no atendida **dentro del balance ilustrativo**. La agregación puede ocultar déficit en la noche o problemas horarios aunque el mes balancee. No es LOLE ni estimación de racionamiento colombiano. El costo variable usa supuestos explícitos y no es precio de bolsa.

> **Alerta del consultor.** MW × factor de planta no se convierte por el nombre de la variable en potencia firme. El factor resume utilización energética; la suficiencia requiere atender el patrón temporal y las condiciones críticas pertinentes.

## Retardos y retroalimentación

En `puesta_en_servicio = pipeline / demora`, una fracción del pipeline sale desde el primer instante. Es una demora de primer orden, no una espera fija para cada obra. Para representar hitos o cohortes pueden necesitarse varias etapas o fechas de entrada específicas. Toda decisión de agregación debe explicarse.

La práctica conserva un modelo genérico de inversión que ajusta capacidad hacia un objetivo fijo. Las tasas están en MW/año. Se comparan respuestas al cambiar demora y sensibilidad; se registran sobrepasos o convergencia en vez de anunciar oscilaciones antes de ejecutar. El modelo no fija precio colombiano ni ofrece predicción de expansión.

La relación entre capacidad, expectativas, precio y construcción es una hipótesis útil; para aplicarla hacen falta datos de proyectos, decisiones y disponibilidad. Crecimiento de generación también cambia por despacho, clima y demanda. Correlacionarlo con precio no estima de forma identificada el tiempo físico de construcción.

## Calibración que realmente ocurre

Calibrar es estimar parámetros de una estructura especificada con observaciones pertinentes y un criterio. En la práctica se ajusta una tendencia exponencial a **demanda pico** usando años completos hasta 2018 y se evalúa en 2019–2024. Se informa MAE en MW por partición. Es un componente empírico simple para aprender el procedimiento, no validación del modelo completo de inversión ni pronóstico oficial.

Los años de prueba no se usan para elegir el parámetro. Cambiar la fecha de partición después de mirar el error requiere declararlo: de otro modo deja de ser una prueba independiente. El crecimiento estimado se puede comparar con escenarios exógenos, pero no transportar automáticamente a energía, precio o adopción.

Una validación útil combina cuatro preguntas: ¿las ecuaciones representan el mecanismo?, ¿cierran unidades y balances?, ¿se comportan coherentemente en extremos?, ¿reproducen aspectos observados relevantes mejor que una referencia simple? Un R² alto no contesta todas. Tampoco reconocer límites exime de corregir un balance roto.

## Trabajo profesional y entrega

### Del diagrama a las ecuaciones ejecutables

En el modelo de inversión, C es capacidad operativa [MW], Q es pipeline [MW], D es demora [años], V es vida media [años] y C* es objetivo [MW]. Las ecuaciones son `dC/dt = Q/D − C/V` y `dQ/dt = inicio − Q/D`, con `inicio = max(0, C*/V + s(C*−C))`. La sensibilidad s tiene unidad 1/año. El término C*/V repone retiros en equilibrio y el segundo responde a la brecha. No hay precio endógeno: este modelo comprueba ajuste a un objetivo fijo, no ciclos de precios colombianos.

En equilibrio C=C* y Q=D×C*/V. El pipeline de equilibrio no es cero: compensa retiros. Esta solución analítica permite contrastar el programa sin depender de una gráfica convincente. Si la trayectoria converge a otro valor, primero revisar estructura, integración y horizonte. Un mayor D cambia tanto el tiempo de respuesta como el stock de proyectos necesario; no debe interpretarse aisladamente como trámites.

Euler aproxima `C(t+dt)=C(t)+dt×flujo_neto(t)`. Un paso demasiado grande puede crear oscilaciones o valores negativos que no pertenecen al sistema. El código utiliza un integrador adaptativo con tolerancias declaradas. Para una modificación material, comparar tolerancias y resolución temporal antes de explicar diferencias como fenómenos económicos. Aumentar el número de puntos de la gráfica no necesariamente cambia el paso interno del integrador.

### Identificación, referencia y extrapolación

Separar parámetros físicos documentados, parámetros estimados y supuestos. Dos parámetros pueden compensarse y producir la misma trayectoria; eso es un problema de identificación. Más observaciones de la misma variable no siempre lo resuelven: puede hacer falta observar pipeline, retiros o decisiones de inversión además de capacidad.

La prueba temporal de demanda debe compararse con una referencia que también use solo información de entrenamiento. La práctica añade «mantener el último máximo anual observado»: si una tendencia no mejora ese MAE fuera de muestra, su complejidad no queda justificada por ajuste dentro de muestra. Incluso si lo mejora, 2019–2024 es un único bloque histórico, no una garantía de desempeño futuro. Informar errores firmados y escenarios que tensionen la extrapolación, además de la media absoluta.

Al comparar precio y embalse, una asociación contemporánea no identifica la causalidad ni la dirección completa. Ambos pueden reaccionar al clima, la demanda y decisiones operativas; el almacenamiento también depende de la operación. Un rezago elegido por su máxima correlación necesita contraste y no equivale al plazo de construir una planta. Una hipótesis útil debe anticipar qué nueva observación discriminaría entre mecanismos.

La validación es específica al uso. Un balance mensual puede servir para explorar agotamiento estacional y ser insuficiente para evaluar potencia de punta. La frontera se decide antes de interpretar el resultado y se revisa si el encargo cambia. Documentar esa decisión es parte de la competencia de modelar.

Incluye una tabla por parámetro: significado, unidad, origen —estimado, documentado o supuesto—, rango y posibilidad de identificación. Para los supuestos, explica qué prueba les da credibilidad. Prueba aportes cero, mayor demanda y menor disponibilidad térmica; interpreta resultados y efectos no representados.

Entrega el diagrama, ecuaciones, balance, validación y una recomendación sobre **el siguiente análisis necesario**, antes de proponer inversión. Pregunta de defensa: **si el ajuste de demanda funciona, qué partes de tu modelo siguen sin validar?**

Lecturas: Sterman, *Business Dynamics*, y Ford, *Cycles in competitive electricity markets*. Como contraste profesional, el [PIEG de UPME](https://docs.upme.gov.co/SIMEC/Energia%20Electrica/PIEG/2025-2039/Plan_Generacion_2025-2039.pdf) documenta una planificación con escenarios, restricciones y modelos de operación/expansión; el ejercicio del curso tiene otra escala y alcance.

## Antes de cerrar la lectura

Vuelve al ejemplo inicial y explica qué relación conserva con el problema energético y cuál deja de ser válida. Lleva al notebook una predicción escrita. Después de calcular, distingue observación, explicación del mecanismo y consecuencia para la decisión. Si no coinciden, revisa primero la transformación y después tu hipótesis.
