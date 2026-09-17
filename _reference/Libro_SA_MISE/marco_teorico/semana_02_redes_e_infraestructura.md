# Semana 2. Redes: estructura, flujos y límites de una recomendación


## Primera capa. Seis amigos y una conversación que depende de un puente

Volvamos al ejemplo pequeño que hacía útil el material original. A, B, C y D forman un grupo; E solo conversa con B y F solo conversa con D. Dibujemos las amistades A–B, A–C, A–D, B–C, B–E, C–D y D–F. Son siete enlaces. No hay todavía electricidad ni un modelo de influencia: solo una relación declarada, «conversa con».

¿Quién tiene más amigos? Los cuatro del núcleo tienen tres. ¿Quién conecta a alguien que, de otro modo, quedaría aislado? B y D. Dos preguntas razonables producen distinciones diferentes. Antes de calcular una centralidad, el estudiante ya puede reconocer por qué «importancia» necesita una definición.

Ahora quita B. E queda separado, aunque A, C y D todavía pueden conversar. Añade una amistad E–F y repite. La modificación crea una ruta alternativa. No hemos descubierto que cualquier enlace sea conveniente: debemos preguntar qué relación representa, qué costo tiene y para qué proceso importa.

## Segunda capa. Aprender a leer un grafo, paso a paso

Un grafo G=(V,E) contiene nodos y enlaces. La letra E del conjunto de enlaces no debe confundirse con el nombre del amigo E. Empezaremos dibujando, después enumeraremos vecinos y finalmente construiremos una matriz. En la fila A de la matriz de adyacencia escribimos uno en las columnas B, C y D; cero en las demás. La suma de esa fila es el grado de A. Así una fórmula nace de una operación que ya entendemos.

Un camino es una secuencia de enlaces. Entre E y F hay una ruta E–B–A–D–F y otra E–B–C–D–F. Ambas tienen cuatro enlaces. La distancia topológica mide ese número mínimo de pasos. No mide kilómetros, milisegundos ni potencia. Si damos pesos a los enlaces, debemos explicar si son distancias que se suman, capacidades o alguna otra propiedad: no todos los algoritmos interpretan un peso de la misma manera.

La intermediación distribuye crédito entre los caminos mínimos que atraviesan cada nodo. B obtiene crédito al conectar E con el resto. Cuando hay varias rutas mínimas, cada una aporta una fracción. Esto ayuda a detectar intermediarios en la estructura definida. Todavía no hemos supuesto que un rumor, una persona o un electrón siga un camino mínimo.

El clustering pregunta qué tanto se conectan entre sí los vecinos de un nodo. Los vecinos de A son B, C y D; entre ellos existen B–C y C–D: dos de tres enlaces posibles. Su clustering es 2/3. La densidad de todo el grafo compara siete enlaces con los quince posibles entre seis personas: 7/15. Practicaremos ambos cálculos antes de pedirlos a NetworkX.

## Tercera capa. Del amigo que conecta al equipo que transporta

Podemos representar una red eléctrica con nodos y enlaces, pero debemos volver a definirlos. Una barra, una subestación y una empresa son objetos distintos. Si agregamos varias barras en un nodo, podemos esconder restricciones internas. Un plano ayuda a construir una hipótesis de conectividad; no contiene necesariamente reactancias, límites ni estados operativos.

Aquí la comparación con el análisis eléctrico es decisiva. La topología ofrece una vista rápida de redundancias y dependencias estructurales. El flujo de potencia determina distribuciones compatibles con ecuaciones físicas y condiciones de operación. La electricidad no selecciona el camino geográfico más corto. Una línea nueva puede redistribuir flujos por toda la malla; contar una ruta adicional no basta para afirmar que resolvimos una congestión.

Haremos una transición deliberada entre dos ejemplos. Los seis amigos enseñan métricas. Las cinco barras ficticias A–E enseñan flujo DC. Que se repitan letras no significa que se trate del mismo grafo ni de la misma relación. El contraste es precisamente el aprendizaje: conservar una herramienta matemática exige revisar su interpretación al cambiar de dominio.

Después compararemos familias de redes y ataques algorítmicos. Conservaremos el entusiasmo por sus comportamientos diferentes, pero no elegiremos una familia para Colombia mirando solo la forma de un dibujo. La pregunta profesional será qué representación y qué estudio adicional hacen falta para evaluar una decisión de infraestructura.


## Desarrollo y contraste profesional

**Pregunta:** ¿qué información agrega la topología y qué falta para recomendar una obra eléctrica? RAC2: construir una representación consistente e interpretar métricas sin confundirlas con seguridad. Entregable: comparación topológica y eléctrica de un caso pequeño, más ficha de datos faltantes del proyecto colombiano.

## Construir la red antes de medirla

Un grafo tiene nodos y aristas cuyo significado debe definirse. Una barra, una subestación completa, una planta y una empresa no son objetos intercambiables. Agregar todas las barras de una subestación en un nodo puede ocultar redundancia, transformadores y configuración. Una arista contractual representa un acuerdo; una línea eléctrica transporta potencia según leyes físicas. Compartir propietario no crea una línea de transmisión.

En un grafo simple se pierde la multiplicidad de circuitos. En uno dirigido se declara una dirección; para una red AC, dibujar una flecha no determina el sentido físico permanente del flujo. Los atributos importan: impedancia, tensión, límites y fecha de operación. «Ponderado» solo es útil si se dice qué pesa y por qué: kilómetros y reactancia producen caminos distintos.

La densidad `2m/[n(n−1)]` describe cuántos enlaces hay respecto de un grafo completo. El grado cuenta conexiones; la intermediación resume presencia en caminos mínimos; el clustering mide cierre local de triángulos. La centralidad no tiene unidades MW. Un nodo central puede ser relevante para formular preguntas, pero su ranking depende de la frontera, agregación y definición de distancia.

## La electricidad no escoge un único camino mínimo

### Métricas y modelos de referencia

Para un grafo simple no dirigido, la matriz de adyacencia A tiene Aij=1 cuando existe el enlace i–j. El grado es la suma de su fila. La intermediación suma, para cada par de nodos distintos del nodo analizado, la fracción de caminos mínimos que pasa por él; su normalización debe declararse. En un camino A–B–C, B conecta el único recorrido entre extremos. En un triángulo hay rutas directas entre cada par y esa intermediación desaparece, aunque las líneas sigan transportando potencia.

El coeficiente local de clustering es `2 × enlaces_entre_vecinos / [k × (k−1)]` para k≥2. La longitud media de camino resume distancias entre pares; no está definida de la misma manera cuando hay pares desconectados. Si se calcula solo en la componente mayor, reportar también qué fracción de nodos se excluyó. De lo contrario, una red degradada puede parecer mejor porque desaparecieron los pares difíciles de conectar.

Tres familias ayudan a formular comparaciones:

| Modelo | Regla generadora | Pregunta que permite explorar | Límite |
|---|---|---|---|
| Erdős–Rényi | Cada par se conecta con probabilidad p | Qué ocurre sin preferencia estructural entre pares | No impone geografía, tensión ni planificación |
| Watts–Strogatz | Anillo local con reconexión aleatoria de enlaces | Cómo coexisten agrupamiento y atajos | El anillo es una hipótesis docente |
| Barabási–Albert | Crecimiento con preferencia por nodos de mayor grado | Cómo una regla genera heterogeneidad de grado | No prueba que el SIN creció con esa regla |

Comparar tamaño, densidad realizada y varias semillas antes de atribuir un resultado a la familia. En redes pequeñas, diferencias de número de enlaces pueden explicar más que la etiqueta del generador. La práctica reporta esos controles y la componente mayor; no selecciona una familia como descripción validada del país.

Una ley de potencia plantea una relación de escala para la cola de una distribución. Una recta aparente en ejes logarítmicos no basta: hacen falta umbral de cola, estimación, incertidumbre y contraste con alternativas. Tampoco se deduce una distribución de magnitudes de apagón a partir de la distribución de grados. La red, el mecanismo de propagación y la observación son tres objetos distintos.

### Degradación y cascadas: dos experimentos diferentes

Eliminar nodos al azar y eliminar primero los de mayor grado son intervenciones algorítmicas distintas. Debe indicarse si el ranking es inicial o se recalcula después de cada salida. La respuesta puede medirse como tamaño de la componente mayor dividido por el número **original** de nodos. Usar como denominador solo los sobrevivientes puede esconder el daño.

Una cascada requiere además una regla que provoque salidas secundarias. Un ejemplo abstracto fija capacidad de nodo como `(1+alpha) × carga_inicial`, recalcula una carga de caminos tras una perturbación y elimina sobrecargados hasta estabilizar. Enseña dependencia y realimentación; esa carga no es MW, alpha no es rating de línea y el paso no es segundo. Para un estudio eléctrico hay que sustituir la regla por flujos y acciones pertinentes. La práctica DC que sigue hace explícito el primer paso físico, sin afirmar que ya reproduce una cascada real.

La aproximación DC ayuda a observar este límite sin requerir todavía flujo AC. Supone magnitudes de tensión cercanas a 1 pu, pequeñas diferencias angulares y pérdidas despreciables. Para una línea:

`P_ij [MW] = S_base [MVA] × (theta_i − theta_j) / x_ij [pu]`.

Se imponen balances nodales y se fija un ángulo de referencia. El programa resuelve las otras variables angulares. Cambiar una reactancia redistribuye flujos aun si los nodos y conexiones son idénticos: una métrica topológica sin ponderar no registra ese cambio.

Los cinco nodos A–E de la práctica son ficticios. Las inyecciones suman cero y los límites se asignan para aprender. Se comprueban balance y sobrecargas. Si la red se divide, no se inventa una solución: se registra que hacen falta balances por isla y acciones de redispatch o desconexión.

> **Alerta del consultor.** Conectividad es posibilidad topológica. Servicio exige potencia y energía disponibles, límites de equipos, tensión y estabilidad, además de reglas operativas. Una red conectada puede tener una línea sobrecargada; una isla puede tener recursos para abastecer parte de su carga. Contar componentes no cuantifica energía no servida.

## Qué significa una contingencia

Una prueba topológica quita un nodo o enlace y observa conectividad. Una evaluación eléctrica de contingencia retira un elemento definido y analiza el estado resultante bajo condiciones operativas específicas. Quitar progresivamente el 10%, 20% o 30% de nodos es un experimento de degradación; no equivale a contingencias simples independientes.

En la práctica se retira cada línea por separado, partiendo siempre del caso base. Se reportan islas y máxima utilización de líneas bajo despacho fijo DC. No se certifica N-1 integral: faltan reactivos, tensiones, estabilidad, protecciones, acciones correctivas y el conjunto aplicable de criterios. El [Código de Redes, CREG 025 de 1995](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0025_1995.htm) es un punto de entrada para identificar requisitos, verificando versión y modificaciones pertinentes al caso.

Una cascada por redistribución de centralidad enseña cómo una dependencia puede amplificar fallas. No representa necesariamente redistribución eléctrica ni actuación de protecciones. Si se conserva como ejercicio adicional, sus resultados deben medirse en nodos del modelo y pasos algorítmicos, nunca renombrarse usuarios afectados o minutos de apagón.

## De la métrica a la decisión de infraestructura

Una recomendación requiere alternativa física concreta, mecanismo de beneficio, escenarios de operación, costo y restricciones. Duplicar un circuito puede afectar confiabilidad de modo diferente a instalar compensación reactiva, almacenamiento o generación local. Betweenness no selecciona entre ellos. El almacenamiento requiere potencia, duración y energía para recargarse; «poner una batería en el nodo central» no constituye diseño.

El paquete mínimo para profundizar incluye unifilar fechado, barras/circuitos, parámetros y ratings, generación y cargas por escenario, contingencias, planes de expansión y restricciones de conexión. Si no está disponible, el entregable profesional puede ser un estudio preliminar que prioriza solicitudes de información. El mapa del SIN sirve de contexto, no se inventan impedancias para presentarlo como modelo validado.

## Práctica, discusión y avance

Compara el ranking de intermediación con los resultados DC. Modifica una reactancia conservando topología y explica qué cambió. Luego propone una acción en el sistema ficticio y muestra si mejora una contingencia y empeora otra. La métrica debe incluir beneficio y efecto adverso.

Para el caso colombiano entrega el esquema de infraestructura relevante, marcando explícitamente relaciones verificadas y pendientes. Incluye una ficha «dato → cálculo → decisión»: por ejemplo, límite térmico → utilización bajo contingencia → necesidad de estudiar redispatch o refuerzo. Pregunta de defensa: **¿podrías recomendar el mismo refuerzo si desconocieras las inyecciones?**

Lecturas: Watts y Strogatz sobre small-world; trabajos de vulnerabilidad estructural del material original. Comparar el objeto de cada paper con el objeto eléctrico real antes de transferir conclusiones.

## Antes de cerrar la lectura

Vuelve al ejemplo inicial y explica qué relación conserva con el problema energético y cuál deja de ser válida. Lleva al notebook una predicción escrita. Después de calcular, distingue observación, explicación del mecanismo y consecuencia para la decisión. Si no coinciden, revisa primero la transformación y después tu hipótesis.
