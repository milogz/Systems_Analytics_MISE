# Analisis de Sistemas para la Industria Energetica

Bienvenido al material del curso **Analisis de Sistemas** de la Maestria en Ingenieria de Sistemas Energeticos (MISE), Universidad de los Andes.

## Sobre el curso

Este curso forma profesionales capaces de analizar proyectos energeticos como **sistemas complejos**, integrando herramientas cuantitativas (redes complejas, dinamica de sistemas, analisis de escenarios) con la dimension social, ambiental y de gobernanza que determina la viabilidad real de los proyectos.

El material se organiza en **semanas tematicas**. Cada semana contiene:

- **Lectura teorica**: fundamentacion conceptual, historica y cientifica del tema.
- **Notebook de practica**: laboratorio computacional con codigo interactivo en Python.

## Estructura del curso

| Semana | Tema | Herramientas |
|--------|------|-------------|
| **Preludio** | Fundamentos cientificos de la complejidad | Mapa logistico, Lorenz, distribuciones de cola pesada |
| **1** | Que significa "sistemico" | CLDs, vocabulario de complejidad, automatas celulares |
| **2** | Redes I: topologia y vulnerabilidades | NetworkX, centralidad, N-1, cascadas |
| **3** | Redes II: actores y difusion | Comunidades, Bass, contagio complejo |
| **4** | Dinamica de sistemas I: stocks y flujos | Modelos SD, retroalimentacion, retardos |
| **5** | Dinamica de sistemas II: politicas y escenarios | Escenarios, minimax regret, tornado |
| **Cierre** | Integracion, gobernanza y proyecto final | Ostrom, Sovacool, informe de consultoria |

## La Saga Colombia

Ademas de los laboratorios semanales, el curso incluye la **Saga Colombia**: un ejercicio de consultoria sistemica sobre el Sistema Interconectado Nacional (SIN), construido con **datos reales de 25 anos** provenientes de la API publica de XM (operador del mercado electrico colombiano).

La Saga recorre 8 notebooks (saga_00 a saga_07) que van desde la radiografia de datos hasta la sintesis ejecutiva, aplicando progresivamente las herramientas de cada semana a un problema real:

| Saga | Tema | Conexion semanal |
|------|------|-----------------|
| **0** | Radiografia de datos del SIN | Base empirica |
| **1** | Identidad del sistema | S1: Complejidad |
| **2** | Estructura fisica (red) | S2: Redes I |
| **3** | Estructura social (actores) | S3: Redes II |
| **4** | Dinamica de inversion-capacidad | S4: SD I |
| **5** | Politicas y escenarios | S5: SD II |
| **6** | Gobernanza y justicia | Cierre |
| **7** | Sintesis ejecutiva | Cierre |

Cada notebook de la saga incluye recuadros **"Dos Miradas"** que contrastan lo que revelaria un analisis convencional versus lo que aporta la perspectiva de sistemas complejos.

## Datos reales

Los analisis estan respaldados por datos publicos verificables:

- **Precios de bolsa**: serie horaria 2000-2025 (>9,000 dias)
- **Generacion**: serie horaria 2000-2025 por recurso
- **Embalses**: nivel diario agregado 2003-2025
- **Demanda**: maxima diaria y comercial horaria
- **Plantas**: 2,293 recursos registrados con tipo, fuente y empresa

Fuente: [API publica de XM S.A. E.S.P.](https://servapibi.xm.com.co)

## Requisitos

- Python 3.9+
- Jupyter Notebook o JupyterLab
- Librerias: `numpy`, `pandas`, `matplotlib`, `networkx`, `scipy`

## Como usar este material

Navega por la barra lateral para acceder a cada semana. Dentro de cada semana encontraras primero la lectura teorica y luego el notebook de practica.

Los notebooks estan pre-ejecutados para que puedas ver los resultados sin necesidad de correr codigo. Si deseas experimentar, descarga el notebook y ejecutalo en tu entorno local.
