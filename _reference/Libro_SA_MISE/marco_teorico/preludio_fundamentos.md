# Preludio. Cuando conocer las reglas no basta para anticipar la historia

Imagina que puedes repetir un experimento conservando exactamente sus reglas. ¿Obtendrás siempre una trayectoria parecida si cambias apenas el punto de partida? Nuestra intuición suele contestar que sí. Un poco más de demanda debería necesitar un poco más de oferta; una demora ligeramente mayor debería producir un atraso ligeramente mayor. Gran parte de la ingeniería puede trabajar con aproximaciones de este tipo, dentro de rangos definidos. Este curso comienza preguntando cuándo dejan de ser suficientes.

No necesitamos abandonar las matemáticas para hacerlo. Al contrario: necesitamos mirar con más cuidado qué permiten las ecuaciones, qué medimos y qué interacciones hemos excluido. La complejidad tiene fundamentos científicos; llamarla «sistémica» no concede permiso para explicar cualquier cosa con una metáfora.

## Primera capa: tres puertas para la curiosidad

### Poincaré: de una posición futura a la geometría del movimiento

La historia del problema de los tres cuerpos, que abría el material original, sigue siendo una buena invitación. Añadir un cuerpo a un sistema gravitatorio no consiste simplemente en repetir tres veces la solución de dos cuerpos: cada movimiento cambia las fuerzas que reciben los demás. Poincaré ayudó a establecer una mirada cualitativa sobre esas trayectorias y su estructura. La pregunta puede pasar de «¿dónde estará exactamente?» a «¿qué tipos de movimiento admite este sistema?».

Hay que cuidar el alcance de esa historia. No todos los movimientos de tres cuerpos son caóticos y existen soluciones especiales. La dificultad no se resume en que nadie pueda escribir ninguna solución analítica. Tampoco se sigue que un mercado, por tener muchos actores, deba ser caótico. Lo transferible es una forma de preguntar por interacciones y estabilidad; la identificación de caos en otro objeto exige trabajo adicional.

Prueba una analogía cotidiana. Tres personas coordinan una reunión y cada una cambia de horario al conocer el cambio de las otras. La dificultad ya no está solo en las agendas individuales: está también en la regla de revisión. ¿Se anuncian todos los cambios simultáneamente? ¿Se respeta el último compromiso? Esa regla forma parte del sistema que intentamos comprender.

### Lorenz: reglas deterministas, trayectorias sensibles

Lorenz estudió un modelo reducido de convección con tres ecuaciones no lineales. Bajo ciertos parámetros, pequeñas diferencias iniciales pueden crecer y producir trayectorias distintas. Determinismo describe la regla de evolución; predictibilidad práctica depende también de la precisión inicial y del horizonte. Son preguntas diferentes. La lectura fundacional es [Lorenz (1963)](https://doi.org/10.1175/1520-0469%281963%29020%3C0130%3ADNF%3E2.0.CO%3B2).

En la práctica dibujaremos dos trayectorias cercanas y su separación. Antes de observarlas, escribe tu expectativa. Después, distingue la separación entre estados de la forma global del atractor. Perder precisión sobre una trayectoria no implica perder toda información sobre el conjunto de comportamientos.

El ejemplo no es un pronóstico climático colombiano. Ni tres variables abstractas equivalen a tres variables observadas del SIN. Su valor didáctico es permitirnos observar un mecanismo que la intuición proporcional suele pasar por alto.

### Mandelbrot: la escala también forma parte de la pregunta

Ahora imagina que mides una costa con una regla larga y después con otra más corta. La segunda sigue entrantes que la primera omitió. El resultado depende de la resolución. La perspectiva fractal de Mandelbrot invita a estudiar irregularidad y escala; una figura rugosa no constituye por sí sola evidencia de autosimilitud. Véase [Mandelbrot (1967)](https://doi.org/10.1126/science.156.3775.636).

En energía, cambiar de datos horarios a anuales también altera lo visible, aunque eso no convierta automáticamente la serie en fractal. Un balance anual puede ocultar una restricción nocturna. Preguntar por la escala es una disciplina compartida; identificar una dimensión fractal es una afirmación adicional que habría que justificar.

## Segunda capa: una ecuación que podemos recorrer a mano

Consideremos el mapa logístico `x[t+1] = r*x[t]*(1-x[t])`, con x entre cero y uno y r entre cero y cuatro. x es un estado normalizado de un modelo discreto. La analogía de una población ayuda a leer el crecimiento y el freno, pero no certifica un modelo demográfico real. Tampoco debe confundirse este mapa con la ecuación logística continua de Verhulst: sus comportamientos no son intercambiables.

Empieza con x=0,2 y r=2,8. La siguiente iteración vale 2,8×0,2×0,8=0,448. La que sigue utiliza 0,448, no vuelve a utilizar el valor inicial. Esta sustitución repetida es toda la maquinaria del experimento. El término x permite crecer; el término 1−x reduce el resultado cuando el estado se acerca a uno. Que ambos se multipliquen impide leer la respuesta como una suma de efectos constantes.

Para encontrar estados fijos imponemos x siguiente igual a x actual. Aparecen cero y, cuando corresponde, 1−1/r. Encontrarlos no basta: hay que estudiar si pequeñas desviaciones disminuyen. La derivada del mapa es r(1−2x). Su valor absoluto local permite estudiar la estabilidad del punto fijo. Así conectamos una gráfica atractiva con una pregunta matemática precisa.

Al variar r podemos observar convergencia, ciclos y comportamientos caóticos. Las ventanas periódicas impiden afirmar que todo valor por encima de un único umbral sea caótico. El artículo de [May (1976)](https://www.nature.com/articles/261459a0) es una puerta de entrada a esta riqueza de los modelos discretos simples.

En el notebook primero calculamos unas pocas filas, después trazamos trayectorias y finalmente un diagrama de bifurcación. Descartamos un transitorio antes de dibujar los estados finales. Si no lo hacemos, podemos confundir el viaje hacia un atractor con el atractor mismo. Tampoco una gráfica irregular prueba caos: comparamos sensibilidad y recordamos los límites de precisión numérica.

## Tercera capa: clima, tecnología y decisiones de infraestructura

El SIN combina procesos con ritmos diferentes. La demanda cambia dentro del día; los embalses conservan memoria de aportes y operación; una obra requiere años; un contrato redistribuye exposición; los actores revisan expectativas. Una media anual puede ser correcta y, aun así, insuficiente para la decisión. La utilidad del enfoque sistémico aparece al especificar qué interacción conecta esas escalas.

ENSO ofrece un ejemplo especialmente importante. No es un reloj que garantice un Niño idéntico cada cierto número de años. Interesa estudiar intensidad, localización, duración y efectos regionales, y después la traducción de lluvia a aportes y de aportes a operación. El [IPCC AR6, capítulo 4](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-4/) distingue cambios de variabilidad de precipitación asociada a ENSO de cambios en su amplitud de temperatura superficial del mar. Una proyección global no entrega directamente aportes para una cuenca colombiana.

Por eso un «corrimiento de El Niño» debe convertirse en una hipótesis específica: ¿cambio de calendario, de patrón espacial o de distribución de intensidad? Se necesitan datos y modelos distintos para cada interpretación. En el curso desplazaremos y concentraremos aportes sintéticos conservando su total para examinar el efecto de la secuencia. Esa intervención demuestra sensibilidad de un almacén; no estima un cambio futuro de ENSO.

### Dos miradas que debemos aprender a ponderar

La estadística ofrece estimación, incertidumbre, contraste y referencias predictivas. No se reduce a extrapolar promedios ni está condenada a fallar ante la no linealidad. Un modelo estadístico flexible puede superar a un modelo mecanístico mal especificado. Lo que suele quedar fuera de una extrapolación sencilla es cómo respondería el sistema a reglas, interacciones o condiciones que no aparecen en la muestra.

El modelo sistémico hace explícita esa hipótesis de mecanismo. A cambio, introduce estructura y parámetros que pueden estar mal identificados. La comparación profesional consiste en preguntar qué aporta frente a una referencia, qué observaciones lo contradicen y si mejora una decisión. Una simulación vistosa no gana por su apariencia.

En una consultoría podemos combinar un pronóstico de demanda, un modelo eléctrico, escenarios hidrológicos y una representación de decisiones de inversión. No necesitamos forzar todos los problemas dentro de una sola herramienta. Primero identificamos la pregunta; después elegimos la combinación mínima que la puede responder.

**Para conversar antes de comenzar:** ¿qué indicador promedio utilizas habitualmente?, ¿qué secuencia o interacción podría quedar escondida detrás de él?, ¿qué observación permitiría comprobar si esa omisión importa? Guarda la respuesta. Al terminar el curso deberías poder volver a ella con un experimento, una evidencia y una decisión mejor delimitada.
