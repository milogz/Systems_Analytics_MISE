# Proyecto integrador: del caso a una recomendación defendible

Esta guía establece el propósito, las entregas y los criterios de evaluación del proyecto integrador de **Systems Analytics — MISE**. Utilícela junto con las guías semanales para planificar el trabajo del grupo.

## Propósito y resultados de aprendizaje

En grupos de tres, analicen un proyecto o sistema energético colombiano real para un decisor explícito. Integren complejidad (RAC 1), redes (RAC 2), dinámica de sistemas e incertidumbre (RAC 3) y dimensión social, ambiental, ética, gobernanza y comunicación (RAC 4). Los casos y simulaciones del curso ayudan a aprender el método; la estructura del caso propio debe justificarse con su pregunta y evidencia.

## Entregas y dedicación

| Semana | Producto o revisión | Peso en la nota del curso |
|---|---|---:|
| S1 | Ficha: caso, decisor, pregunta, fuentes y roles | Sin nota |
| S2 | Esquema de redes y revisión/aprobación del caso | Sin nota |
| S3 | Avance 1: caso y complejidad, 1.500 palabras | 5 % |
| S4 | Ensayo del modelo en Lab 3 y trabajo hacia Avance 2 | Sin nuevo avance del proyecto |
| S5 | Avance 2: modelo calibrado, 2.000 palabras | 5 % |
| S6 | Role-play y diagnóstico de gobernanza; trabajo hacia Avance 3 | Actividad del curso; no un nuevo avance |
| S7 | Avance 3: escenarios, robustez y gobernanza, 2.500 palabras | 5 % |
| S8 | Informe de 5.000–7.000 palabras | 25 % |
| S8 | Panel de 15 minutos más preguntas | 5 % |

El proyecto suma **45 %**; las demás actividades del curso suman 55 % y mantienen su distribución oficial. El proyecto comprende siete entregas: ficha, esquema, tres avances, informe y panel. Lab 3 y role-play preparan la elaboración de los avances. Las fechas concretas y la programación del panel se consultan en el aula virtual.

Los avances son piezas que se revisan e integran, no documentos adicionales que deban copiarse íntegros en el informe. La realimentación debe incorporarse antes de la entrega siguiente. Sin caso aprobado no se califica el Avance 1.

## Elección y viabilidad del caso

Los casos sugeridos son Windpeshi/ola eólica guajira, El Paso solar, Hidroituango, solar distribuida urbana, hidrógeno verde en La Guajira y microrredes en ZNI. Para un caso libre, justifiquen los siguientes criterios: ancla colombiana y decisor, datos accesibles, riqueza dinámica, red pertinente, gobernanza sustantiva y distancia de los ejemplos publicados. La riqueza dinámica del caso libre debe admitir al menos tres stocks con retroalimentación y retardos no triviales. No agreguen stocks artificiales para aumentar el tamaño del modelo.

Empiecen buscando datos en S1 y revisen su disponibilidad con el tutor en S2. Una aprobación debe considerar si la pregunta se puede investigar con los recursos y el tiempo disponibles.


## Avance 1: explicar la complejidad

**S3 · 1.500 palabras · RAC 1.** Justifiquen al menos tres retroalimentaciones, dos no linealidades y un evento extremo, con CLD y notación consistente. Expliquen la frontera, el problema y la pregunta del decisor. Conserven el análisis de redes de S2–S3 para su sección del informe: no reemplaza este diagnóstico.

| Criterio | Peso |
|---|---:|
| Delimitación y pregunta | 15 % |
| Retroalimentaciones | 30 % |
| No linealidades | 20 % |
| Evento extremo | 15 % |
| CLD y notación | 10 % |
| Redacción y fuentes | 10 % |

Para profundizar, relacionen las no linealidades con consecuencias dinámicas y discutan dominancia de lazos con evidencia. Preparación: ejemplos de S1 y revisión en S3.

## Avance 2: modelar y comprobar

**S5 · 2.000 palabras · RAC 3.** Presenten el modelo calibrado con datos colombianos, análisis de ciclos y retardos, sensibilidad y normativa aplicable. Expliquen variables, unidades, parámetros, condiciones iniciales y límites del modelo. Referencien el código reproducible.

| Criterio | Peso |
|---|---:|
| Formulación | 25 % |
| Calibración con datos colombianos | 25 % |
| Ciclos y retardos | 20 % |
| Sensibilidad | 15 % |
| Normativa aplicable | 10 % |
| Reproducibilidad y redacción | 5 % |

La discusión de identificabilidad distingue el nivel sobresaliente: qué combinaciones de parámetros no pueden separarse con los datos disponibles. No confundan esta profundización con un requisito de usar un estimador avanzado. Las pruebas y la ficha de S4 ayudan a todos los niveles. Declarar datos sintéticos es obligatorio cuando corresponda, pero no sustituye la calibración con datos que exige el avance. No fuercen oscilaciones si el modelo justificado no las produce: analicen sus condiciones y límites.

## Avance 3: escenarios, robustez y gobernanza

**S7 · 2.500 palabras · RAC 3 y 4.** Justifiquen los ejes de incertidumbre, al menos cuatro escenarios de mundos distintos, una tabla preliminar de al menos tres estrategias por cuatro escenarios y el plan de ensamble. Incorporen la dimensión social y de gobernanza; relacionen las restricciones con las estrategias.

| Criterio | Peso |
|---|---:|
| Ejes de incertidumbre | 20 % |
| Escenarios | 25 % |
| Robustez preliminar | 25 % |
| Dimensión social y gobernanza | 20 % |
| Plan de ensamble | 10 % |

Analicen si el orden de preferencia de las estrategias cambia entre escenarios. Expliquen tanto los cambios como la estabilidad de los resultados a partir de los supuestos y la evidencia.

## Informe final y panel

**S8 · 5.000–7.000 palabras**, más un resumen ejecutivo de **una página fuera del conteo** y apéndice A con enlace al repositorio. Distribución orientativa del cuerpo (los números aproximados no son mínimos por sección):

| Sección | Contenido | Orientación |
|---|---|---:|
| 1 | Caso y contexto: decisor, pregunta, frontera, fuentes | ~700 |
| 2 | Análisis de complejidad: lazos, no linealidades y extremos | ~800 |
| 3 | Análisis de redes: representación, evidencia y diagnóstico | ~900 |
| 4 | Modelo de dinámica de sistemas: estructura, calibración y pruebas | ~1.200 |
| 5 | Dimensión social, ambiental, ética y gobernanza | ~900 |
| 6 | Recomendaciones estratégicas: escenarios, robustez y condiciones | ~900 |
| 7 | Limitaciones y horizonte | ~400 |

Incluyan al menos cuatro escenarios y una tabla de robustez con arrepentimiento. El plan adaptativo con contingencias y señales de vigilancia es una profundización para el desempeño sobresaliente.

| Criterio del informe | Peso |
|---|---:|
| Resumen ejecutivo | 10 % |
| Caso y complejidad | 10 % |
| Redes | 15 % |
| Modelo dinámico | 20 % |
| Gobernanza y justicia | 15 % |
| Escenarios, robustez y recomendaciones | 20 % |
| Limitaciones y reproducibilidad | 10 % |

En el **panel**, los tres integrantes presentan y responden ante audiencias técnicas y no técnicas. Criterios: mensaje/estructura 25 %, defensa técnica 30 %, visualización honesta 20 %, tiempo/equipo 15 % y audiencia no técnica 10 %. Ensayen desde S5 una pregunta sobre el mecanismo y otra sobre las condiciones de validez.

## Calidad, autoría y evidencia

Cada cifra lleva fuente o etiqueta de dato sintético. Distingan lo observado de lo estimado, ajustado o supuesto. El evaluador debe poder regenerar tablas y figuras con las instrucciones del repositorio. Documenten fuentes, transformaciones, dependencias y acceso a los datos.

El diseño del modelo debe responder al caso analizado; cambiar los nombres de un ejemplo no constituye una adaptación justificada. Reutilicen herramientas y código con atribución y respetando sus condiciones de uso; justifiquen las variables, relaciones y frontera del caso propio. Una explicación de qué se reutilizó y qué se decidió específicamente para el caso hace visible esa diferencia.

Los cuatro niveles de desempeño son insuficiente (0–59 %), aceptable (60–74 %), bueno (75–89 %) y sobresaliente (90–100 %). El logro mínimo requerido es **70 %**: no se debe confundir el inicio del nivel aceptable con ese umbral. Utilice las rúbricas de evaluación publicadas en el aula virtual para revisar cada entrega.
