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

## Tres líneas de contenido por semana

Cada semana del curso opera en **tres líneas paralelas** que se refuerzan mutuamente:

| Línea | Propósito | Formato |
|-------|-----------|---------|
| **Lectura teórica** | Fundamentación conceptual, histórica y científica | Markdown — lectura guiada |
| **Práctica computacional** | Laboratorio con herramientas reproducibles | Jupyter Notebook interactivo |
| **Caso Colombia** | Aplicación al Sistema Interconectado Nacional | Jupyter Notebook — consultoría sistémica |

Adicionalmente, cada semana incluye una **Guía Semanal** con las lecturas recomendadas, actividades de evaluación, entregas del proyecto integrador y distribución del tiempo.

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

Además de los laboratorios semanales, el curso integra un ejercicio longitudinal de **consultoría sistémica** sobre el Sistema Interconectado Nacional (SIN), construido con **datos reales de 25 años** provenientes de la API pública de XM (operador del mercado eléctrico colombiano).

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

Navega por la barra lateral para acceder a cada semana. Dentro de cada semana encontrarás:

1. **Guía Semanal** — mapa de la semana con lecturas, actividades y entregas
2. **Lectura teórica** — fundamentación conceptual
3. **Práctica computacional** — laboratorio con código interactivo en Python
4. **Caso Colombia** — aplicación al Sistema Interconectado Nacional

Los notebooks están pre-ejecutados para que puedas ver los resultados sin necesidad de correr código. Si deseas experimentar, descarga el notebook y ejecútalo en tu entorno local.
