# Guía Semanal — Semana 4: Dinámica de Sistemas I — Stocks, Flujos y Retroalimentaciones

> "Modelando por qué el sector eléctrico oscila cíclicamente entre escasez y sobreoferta."

## Caso Ancla

**El ciclo de inversión-capacidad en generación eléctrica colombiana.**
Se pasa de dibujar mapas causales a crear modelos matemáticos simulables que representan los ciclos endógenos, donde los retardos en construcción provocan oscilaciones inevitables en los precios y capacidades del sistema.

## Objetivos de la Semana

- Diferenciar operativamente variables de stock (acumulación) y variables de flujo (tasas).
- Construir diagramas formales de Stocks y Flujos y traducirlos a ecuaciones diferenciales.
- Simular modelos de dinámica de sistemas (SD) con retardos en Python (`scipy.integrate`).

## Material del Curso

| Componente | Descripción |
|---|---|
| **Lectura teórica** | [semana_04_dinamica_sistemas.md] ODEs, lazos de balance/refuerzo y retardos materiales e informacionales. |
| **Práctica computacional** | [semana_04_dinamica_sistemas.ipynb] Construcción de modelos usando módulos SD y el ciclo del SIN. |
| **Caso Colombia** | [saga_04_dinamica.ipynb] Calibración del ciclo de inversión del mercado colombiano con datos de XM. |

## Lecturas y Recursos Recomendados

### Obligatorias
- *Business Dynamics* (Cap. 1–3) — John Sterman.
- *Thinking in Systems* (Cap. 3, arquetipos sistémicos) — Donella Meadows.
- Informe de operación del SIN — XM (datos históricos).

### Recomendadas
- *Cycles in deregulated electricity markets* — Arango & Larsen.
- Resolución CREG 071/2006 (guía de lectura).

## Actividades de Evaluación

| Actividad | Descripción | Modalidad | Peso |
|---|---|---|---|
| Quizzes | Identificación de stocks, flujos y retardos | Autónomo | Evaluado |
| Lab 3 | Notebook simulando el ciclo de inversión-capacidad (calibrado) | Autónomo | Evaluado |
| Foro asíncrono | Justificación de los stocks más críticos del sector eléctrico colombiano | Autónomo | Evaluado |

## Proyecto Integrador

Transformar el Diagrama de Lazos Causales (CLD) del caso del grupo en una estructura de stocks y flujos. Identificar variables clave, documentar supuestos y ecuaciones iniciales (1,200 palabras + diagrama).

## Conexión con la Saga Colombia

El `saga_04_dinamica` toma los datos históricos del SIN desde el 2000 hasta el 2024 para calibrar nuestro modelo base de 3 stocks. Se mostrará explícitamente cómo el retardo constructor determina la amplitud de la oscilación de precios en la Bolsa de Energía.

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
