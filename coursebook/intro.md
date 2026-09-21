# Análisis de Sistemas para la Industria Energética

Bienvenido al material del curso **Systems Analytics** de la Maestría en Innovación de Sistemas Energéticos (MISE), Universidad de los Andes.

---

## Visión del curso

Este curso forma profesionales capaces de analizar proyectos energéticos como **sistemas complejos**, integrando herramientas cuantitativas con la dimensión social, ambiental y de gobernanza que determina la viabilidad real de los proyectos.

El análisis convencional de proyectos — VPN, TIR, sensibilidad estática — no es suficiente cuando el sistema exhibe retroalimentaciones, retardos, comportamientos emergentes y futuros radicalmente inciertos. Systems Analytics equipa al estudiante con tres pilares complementarios:

1. **Pensamiento de complejidad** — adaptación, no linealidad, eventos extremos
2. **Análisis de redes complejas** — la estructura de la infraestructura y las interacciones sociales
3. **Dinámica de sistemas** — la evolución temporal del sistema bajo políticas e incertidumbre

La integración de estos tres pilares, aplicados a casos reales del sector eléctrico colombiano, constituye el diferencial formativo del curso.

---

## El arco narrativo: cinco cosas que importan

El curso progresa a través de una secuencia de descubrimientos que van de lo técnico a lo humano:

```{mermaid}
graph TD
    A["Preludio: ¿Por qué la complejidad<br>importa?"] --> B["S1: El SIN es un sistema complejo"]
    B --> C["S2: La estructura importa<br>(topología → vulnerabilidades)"]
    B --> D["S3: Los actores importan<br>(difusión, poder, comunidades)"]
    C --> E["S4: El tiempo importa<br>(retardos → oscilaciones)"]
    D --> E
    E --> F["S5: La incertidumbre importa<br>(escenarios, robustez)"]
    F --> G["S6: Lo humano importa<br>(gobernanza, justicia, consulta previa)"]
    G --> H["S7–S8: Integrar y recomendar"]
```

1. **La complejidad importa** — los modelos lineales fallan en sistemas con retroalimentación, retardos y adaptación
2. **La estructura importa** — la topología de la red determina dónde se propagan las fallas y cómo fluye el poder
3. **El tiempo importa** — los retardos de construcción generan oscilaciones endógenas que ningún shock externo explica
4. **La incertidumbre importa** — no buscar la decisión óptima sino la decisión robusta ante futuros que no controlamos
5. **Lo humano importa** — la gobernanza, la justicia energética y la consulta previa son la meta-capa que condiciona todo lo demás

---

## Un recorrido semanal en dos bloques

Empiece por la **guía semanal**: indica resultado esperado, selección de recursos, tiempo e hito del proyecto.

| Bloque | Recursos y propósito |
|---|---|
| **Lecciones** | Lectura y videos/quices del aula virtual para comprender; ejemplos guiados para observar el procedimiento; práctica computacional para ejecutar e interpretar. |
| **Proyecto** | Un tramo de la Saga Colombia para observar la aplicación y el trabajo del caso propio para construir evidencia del informe. |

La biblioteca completa sigue disponible. La guía distingue el recorrido principal de la profundización: no se suman todas las páginas, videos y variantes como carga obligatoria. Consulte en el aula virtual los videos y actividades correspondientes a cada semana.

La [guía del proyecto](proyecto/guia.md) establece las entregas, la estructura del informe y los criterios de evaluación. Las [convenciones comunes](proyecto/lenguaje_comun.md) aclaran cómo pasar entre modelos y recursos.

---

## Estructura del curso

| Semana | Tema | Herramientas | Caso Colombia |
|--------|------|-------------|---------------|
| **Preludio** | Fundamentos científicos de la complejidad | Mapa logístico, Lorenz, distribuciones de cola pesada | Radiografía de datos del SIN |
| **1** | ¿Qué significa "sistémico"? | CLDs, vocabulario de complejidad, autómatas celulares | Identidad del SIN |
| **2** | Redes I: topología y vulnerabilidades | NetworkX, centralidad, N-1, cascadas | Estructura física del STN |
| **3** | Redes II: actores y difusión | Comunidades, Bass, contagio complejo | Estructura social y mercado |
| **4** | Dinámica de sistemas I: stocks y flujos | Modelos SD, retroalimentación, retardos | Dinámica temporal del SIN |
| **5** | Dinámica de sistemas II: políticas y escenarios | Escenarios, minimax regret, tornado | Políticas y escenarios |
| **6** | Gobernanza, justicia y la dimensión humana | Ostrom, Sovacool, consulta previa | Gobernanza y justicia energética |
| **7** | Integración y consultoría sistémica | Integración multi-capa, comunicación | Síntesis ejecutiva |
| **8** | Horizontes futuros y cierre | ABM, RDM, ML — el primer piso, no el techo | Presentaciones finales |

---

## El Caso Colombia: consultoría sistémica del SIN

Además de los laboratorios semanales, el curso integra un ejercicio longitudinal de **consultoría sistémica** sobre el Sistema Interconectado Nacional (SIN), que combina datos públicos del sector, representaciones simplificadas y experimentos pedagógicos. En cada ejercicio distinga la procedencia de los datos y los supuestos del modelo; una red estilizada o una trayectoria simulada no son observaciones del sistema real.

El Caso Colombia recorre 8 notebooks que aplican progresivamente las herramientas de cada semana a un problema real. Cada notebook incluye recuadros **"Dos Miradas"** que contrastan lo que revelaría un análisis convencional versus lo que aporta la perspectiva de sistemas complejos.

El análisis se construye acumulativamente a través de capas:

**Identidad** → **Estructura física** → **Estructura social** → **Dinámica** → **Política** → **Gobernanza** → **Síntesis**

---

## Datos reales

Los análisis están respaldados por datos públicos verificables:

- **Precios de bolsa**: serie horaria 2000–2024 (>9,000 días)
- **Generación**: serie horaria 2000–2024 por recurso
- **Embalses**: nivel diario agregado 2003–2024
- **Demanda**: máxima diaria y comercial horaria
- **Plantas**: 2,293 recursos registrados con tipo, fuente y empresa

Fuente: [API pública de XM S.A. E.S.P.](https://servapibi.xm.com.co)

---

## Requisitos

- Python 3.9+
- Jupyter Notebook o JupyterLab
- Librerías: `numpy`, `pandas`, `matplotlib`, `networkx`, `scipy`

---

## Cómo usar este material

1. Abra la guía de la semana y revise qué debe poder explicar o producir.
2. Recorra las secciones de lectura y los videos/quices indicados en el aula virtual.
3. Siga la selección de ejemplos guiados y aplique el procedimiento en la práctica.
4. Consulte el fragmento de Saga Colombia señalado y transfiera el aprendizaje al caso propio.
5. Revise el hito y conserve la evidencia en el repositorio del proyecto.

Los notebooks conservan sus resultados guardados para facilitar la lectura. Para el proyecto, el grupo debe poder ejecutar el código que genera sus propias tablas y figuras. Los contenidos avanzados y las variantes no seleccionadas permanecen como profundización.
