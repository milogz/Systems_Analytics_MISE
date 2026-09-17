# Guía Semanal — Semana 2: Redes I — Topología, Vulnerabilidades y Confiabilidad

> "La estructura del sistema eléctrico determina cómo y por dónde colapsa."

## Caso Ancla

**El Sistema de Transmisión Nacional (STN) colombiano como grafo.**
Se traduce la infraestructura física a una red compleja para calcular métricas, identificar nodos críticos (vulnerabilidades) y evaluar la confiabilidad operativa ante fallas en cascada y criterios N-1.

## Objetivos de la Semana

- Traducir infraestructura de sistemas energéticos en un grafo analizable computacionalmente.
- Calcular e interpretar métricas de centralidad locales y topología global (criterio N-1).
- Identificar la paradoja "robusto pero frágil" simulando fallas en cascada en la red eléctrica.

## Material del Curso

| Componente | Descripción |
|---|---|
| **Lectura teórica** | [semana_02_redes_topologia.md] Grafos, métricas de centralidad, leyes de potencia y criterio N-1. |
| **Práctica computacional** | [semana_02_redes_topologia.ipynb] Construcción de redes con NetworkX, métricas y ataques a hubs. |
| **Caso Colombia** | [saga_02_estructura_fisica.ipynb] Diagnóstico N-1 y simulación de fallas sobre el STN real colombiano. |

## Lecturas y Recursos Recomendados

### Obligatorias
- *Network Science* (Cap. 2–4) — Albert-László Barabási.
- *The Power Grid as a Complex Network* — Pagani & Aiello (extractos).
- *Plan de Expansión de Referencia (Transmisión)* — UPME.

### Recomendadas
- Informe de confiabilidad del STN — XM.
- *Networks: An Introduction* (Cap. 6–8) — M.E.J. Newman.

## Actividades de Evaluación

| Actividad | Descripción | Modalidad | Peso |
|---|---|---|---|
| Quizzes | Evaluaciones sobre conceptos de redes y topologías | Autónomo | Evaluado |
| Lab 1 | Análisis de red del STN en Python (Notebook + informe) | Autónomo | Evaluado |
| Foro asíncrono | Discusión sobre la distribución de grado del STN y su resiliencia | Autónomo | Evaluado |

## Proyecto Integrador

Identificar las redes relevantes del caso del grupo (red física, red de actores, o red regulatoria). Definir nodos, aristas y tipo de relación. Entrega: esquema de redes + 600 palabras.

## Conexión con la Saga Colombia

El notebook `saga_02_estructura_fisica` carga los datos geográficos y eléctricos del STN. El estudiante visualizará un dashboard con la resiliencia del sistema frente a fallas provocadas, evaluando si nuestra red soporta bien eventos aleatorios pero es frágil ante ataques selectivos.

## Distribución del Tiempo

| Actividad | Horas |
|---|---|
| Video-lecciones con quizzes | 2.5 |
| Lectura dirigida | 1.5 |
| Laboratorio / ejercicio aplicado | 3.0 |
| Actividades asíncronas | 1.0 |
| Proyecto integrador | 2.0 |
| Sesión sincrónica | 2.0 |
| **Total** | **12** |
