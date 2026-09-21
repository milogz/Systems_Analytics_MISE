# Ejemplos guiados — Semana 4

**Para qué sirve:** Traducir mecanismos a stocks y flujos, y comprobar unidades, comportamiento y procedencia de parámetros.

Material del equipo docente de **Systems Analytics — MISE**. Los [ejemplos y simuladores del curso](https://pozost.github.io/Systems-Analytics-Guias/) presentan procedimientos resueltos que preparan la práctica y el proyecto integrador.

**Tiempo del recorrido seleccionado: 65 minutos.** Empiece por los fragmentos de la tabla; los desarrollos restantes son opcionales. Las soluciones permiten autocorregirse y no crean entregas adicionales.

## Selección y secuencia

| Recurso | Qué recorrer |
|---|---|
| [4.01 · Del diagrama causal al modelo: cuánto, cuándo y por cuánto tiempo](https://pozost.github.io/Systems-Analytics-Guias/semana4/01-del-cld-al-modelo.html) | Tabla de decisiones al pasar del CLD a stocks, flujos y auxiliares. |
| [4.07 · Consistencia dimensional y validación: someter el modelo a pruebas para romperlo](https://pozost.github.io/Systems-Analytics-Guias/semana4/07-consistencia-validacion.html) | Ejemplo de revisión dimensional y condiciones extremas. |
| [4.08 · Calibración: afinar el modelo clavija por clavija](https://pozost.github.io/Systems-Analytics-Guias/semana4/08-calibracion.html) | Procedencia de parámetros y ejemplo de límites del ajuste; priorice la interpretación del ajuste. |
| [4.03 · La ecuación del stock y la integración numérica: la contabilidad paso a paso](https://pozost.github.io/Systems-Analytics-Guias/semana4/03-formalismo-integracion.html) | Ejemplo de artefacto numérico y comprobación de convergencia; adaptar la comprobación al integrador del curso. |

## Antes, durante y después

1. **Antes:** formule una predicción o identifique qué paso no sabría resolver sin ayuda.
2. **Durante:** siga el razonamiento del ejemplo, revise unidades/supuestos y compare su predicción con la explicación. Si el simulador no está disponible, utilice el ejemplo resuelto y ejecute el experimento equivalente de la práctica computacional cuando corresponda.
3. **Después:** Complete la ficha de comprobación incluida abajo sobre su propio modelo. Identifique qué observación podría refutar su explicación. Si no dispone de una serie suficiente, reduzca o revise el alcance con el tutor; declarar un dato sintético no satisface por sí solo la calibración empírica.

## Criterios de interpretación

Aplique los procedimientos al modelo de la práctica. Antes de comparar resultados, compruebe las ecuaciones, condiciones iniciales, unidades y parámetros de cada modelo.

Consulte la [guía semanal](guia.md) y la [guía del proyecto](../proyecto/guia.md) para identificar las actividades y entregas correspondientes. Justifique las decisiones de modelado de su caso con su pregunta y evidencia.

## Ficha de comprobación del modelo propio

Complete este registro dentro del repositorio o avance en preparación, no como una entrega adicional.

| Elemento | Registro necesario |
|---|---|
| Stock/flujo/auxiliar | Nombre, función, unidad y ecuación; balance y condición inicial de cada stock. |
| Parámetro | Valor, unidad, fuente/fecha, clasificación (medición, estimación, ajuste o supuesto) y rango defendible. |
| Prueba dimensional | Una ecuación comprobada término a término y cualquier corrección necesaria. |
| Condición extrema | Entrada elegida, comportamiento esperado antes de correr y resultado observado. |
| Comprobación numérica | Integrador/configuración, métrica comparada y diferencia al refinar la configuración. |
| Contraste con datos | Serie y procedencia, período utilizado, comportamiento reproducido y discrepancia. |
| Límite | Qué parámetro o mecanismo no distingue la evidencia y qué dato adicional ayudaría. |

Con `solve_ivp`, compare una métrica al ajustar tolerancias o paso máximo. Cambiar solamente los tiempos donde solicita la salida (`t_eval`) no equivale a reducir el paso interno. Una curva estable numéricamente todavía puede provenir de una estructura inadecuada.

Si usa la prueba de la fotografía, confirme además que la variable cambia por acumulación de flujos: observar un precio en un instante no lo convierte en stock. En un contraste histórico distinga datos observados, series pedagógicas y resultados simulados antes de interpretar el ajuste.


**Continuar:** [lectura](lectura.md) · [guía y hito de esta semana](guia.md) · [lenguaje común](../proyecto/lenguaje_comun.md).
