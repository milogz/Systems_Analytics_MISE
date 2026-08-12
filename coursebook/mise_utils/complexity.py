"""
Soporte para Semana 1: Complejidad — MISE Systems Analytics
==============================================================
Funciones de simulación y visualización para los conceptos
fundamentales de sistemas complejos:

- Feedback loops (refuerzo y balance)
- Emergencia (autómata celular de tráfico)
- Fat tails (distribuciones de cola pesada)
- Lock-in y dependencia de camino
- Tipping points (paisaje de potencial)
- Diagramas de lazo causal (CLD)

Todas las funciones devuelven datos listos para graficar.
El notebook se encarga de la narrativa pedagógica.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from . import viz


# ─────────────────────────────────────────────────────────────────────
# FEEDBACK LOOPS
# ─────────────────────────────────────────────────────────────────────

def simular_feedback_refuerzo(tasa_crecimiento=0.05, valor_inicial=100,
                               n_pasos=50):
    """
    Simula un loop de refuerzo (crecimiento exponencial).

    En cada paso el valor crece proporcionalmente a sí mismo:
        valor[t+1] = valor[t] * (1 + tasa_crecimiento)

    Parameters
    ----------
    tasa_crecimiento : float
        Tasa de crecimiento por paso (default 5 %).
    valor_inicial : float
        Valor en t = 0.
    n_pasos : int
        Número de pasos temporales.

    Returns
    -------
    dict con claves 't' (array) y 'valor' (array).
    """
    t = np.arange(n_pasos)
    valor = valor_inicial * (1 + tasa_crecimiento) ** t
    return {"t": t, "valor": valor}


def simular_termostato(temp_objetivo=22, temp_exterior=5,
                        k_calefaccion=0.3, k_perdida=0.1,
                        n_pasos=100, temp_inicial=10):
    """
    Simula un termostato (feedback de balance / goal-seeking).

    Modelo:
        dT/dt = k_calefaccion * (T_obj - T) - k_perdida * (T - T_ext)

    Parameters
    ----------
    temp_objetivo : float
        Temperatura deseada (°C).
    temp_exterior : float
        Temperatura exterior constante (°C).
    k_calefaccion : float
        Ganancia del sistema de calefacción.
    k_perdida : float
        Tasa de pérdida de calor al exterior.
    n_pasos : int
        Número de pasos.
    temp_inicial : float
        Temperatura interior en t = 0.

    Returns
    -------
    dict con claves 't', 'temperatura', 'temp_objetivo' (arrays).
    """
    t = np.arange(n_pasos)
    temperatura = np.zeros(n_pasos)
    temperatura[0] = temp_inicial

    dt = 0.1  # paso de integración

    for i in range(1, n_pasos):
        calefaccion = k_calefaccion * (temp_objetivo - temperatura[i - 1])
        perdida = k_perdida * (temperatura[i - 1] - temp_exterior)
        temperatura[i] = temperatura[i - 1] + dt * (calefaccion - perdida)

    return {
        "t": t,
        "temperatura": temperatura,
        "temp_objetivo": np.full(n_pasos, temp_objetivo),
    }


# ─────────────────────────────────────────────────────────────────────
# EMERGENCIA: AUTÓMATA CELULAR DE TRÁFICO (Nagel-Schreckenberg)
# ─────────────────────────────────────────────────────────────────────

def simular_trafico(n_autos=30, n_celdas=100, v_max=5,
                     prob_frenado=0.3, n_pasos=200, seed=42):
    """
    Modelo simplificado de Nagel-Schreckenberg para tráfico vehicular.

    Reglas por paso:
        1. Aceleración: v → min(v + 1, v_max)
        2. Frenado por distancia: v → min(v, gap - 1)
        3. Frenado aleatorio: con probabilidad prob_frenado, v → max(v - 1, 0)
        4. Movimiento: x → x + v  (periódico)

    Parameters
    ----------
    n_autos : int
        Número de autos en la carretera circular.
    n_celdas : int
        Longitud del anillo (celdas).
    v_max : int
        Velocidad máxima.
    prob_frenado : float
        Probabilidad de frenado aleatorio.
    n_pasos : int
        Número de iteraciones.
    seed : int
        Semilla aleatoria.

    Returns
    -------
    dict con claves:
        'historial_posiciones': lista de arrays (posiciones por paso)
        'velocidad_promedio': array de velocidades promedio por paso
        'densidad': float (n_autos / n_celdas)
    """
    rng = np.random.default_rng(seed)

    # Inicializar posiciones y velocidades
    posiciones = np.sort(rng.choice(n_celdas, size=n_autos, replace=False))
    velocidades = rng.integers(0, v_max + 1, size=n_autos)

    historial_posiciones = []
    velocidad_promedio = np.zeros(n_pasos)

    for step in range(n_pasos):
        historial_posiciones.append(posiciones.copy())

        # Ordenar por posición para calcular gaps
        orden = np.argsort(posiciones)
        posiciones = posiciones[orden]
        velocidades = velocidades[orden]

        for i in range(n_autos):
            siguiente = (i + 1) % n_autos
            gap = (posiciones[siguiente] - posiciones[i]) % n_celdas

            # 1. Aceleración
            velocidades[i] = min(velocidades[i] + 1, v_max)

            # 2. Frenado por distancia al auto de adelante
            velocidades[i] = min(velocidades[i], gap - 1)
            velocidades[i] = max(velocidades[i], 0)

            # 3. Frenado aleatorio
            if rng.random() < prob_frenado and velocidades[i] > 0:
                velocidades[i] -= 1

        velocidad_promedio[step] = velocidades.mean()

        # 4. Movimiento
        posiciones = (posiciones + velocidades) % n_celdas

    return {
        "historial_posiciones": historial_posiciones,
        "velocidad_promedio": velocidad_promedio,
        "densidad": n_autos / n_celdas,
    }


def plot_diagrama_espacio_tiempo(resultado_trafico, ax=None):
    """
    Dibuja diagrama espacio-tiempo del tráfico.

    Construye una imagen rasterizada donde cada pixel negro
    representa un auto en una posición y paso temporal.
    Los atascos se ven como bandas diagonales que se propagan
    hacia atrás (ondas de densidad).

    Parameters
    ----------
    resultado_trafico : dict
        Salida de simular_trafico().
    ax : matplotlib.axes.Axes, optional
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    historial = resultado_trafico["historial_posiciones"]
    n_pasos = len(historial)
    n_celdas = 100  # default

    # Detectar tamaño de carretera
    if len(historial) > 0:
        max_pos = max(p.max() for p in historial if len(p) > 0)
        n_celdas = int(max_pos) + 1

    # Construir imagen binaria (mucho más visible que scatter)
    grid = np.ones((n_pasos, n_celdas))  # blanco = vacío
    for t in range(n_pasos):
        pos = historial[t].astype(int)
        pos = pos[pos < n_celdas]  # safety
        grid[t, pos] = 0  # negro = auto

    ax.imshow(grid, cmap="gray", aspect="auto",
              interpolation="none", vmin=0, vmax=1)

    ax.set_xlabel("Posición en la carretera (celda)")
    ax.set_ylabel("Tiempo (paso)")
    densidad = resultado_trafico.get("densidad", 0)
    n_autos = int(densidad * n_celdas)
    ax.set_title(f"{n_autos} autos (densidad={densidad*100:.0f}%)",
                 fontsize=12, fontweight="bold")

    return ax


# ─────────────────────────────────────────────────────────────────────
# FAT TAILS / DISTRIBUCIONES
# ─────────────────────────────────────────────────────────────────────

def generar_muestras_comparacion(n=5000, alpha=2.5, seed=42):
    """
    Genera muestras de Gaussiana vs Power-law para comparar.

    Ambas distribuciones se normalizan para tener la misma media y
    varianza, facilitando la comparación visual de las colas.

    Parameters
    ----------
    n : int
        Número de muestras.
    alpha : float
        Exponente de la ley de potencia (Pareto).
    seed : int
        Semilla aleatoria.

    Returns
    -------
    dict con claves 'gaussiana' y 'power_law' (arrays).
    """
    rng = np.random.default_rng(seed)

    # Power-law (Pareto) con exponente alpha
    power_law = (rng.pareto(alpha, size=n) + 1)

    # Normalizar: misma media y std que la gaussiana
    media_pl = power_law.mean()
    std_pl = power_law.std()

    gaussiana = rng.normal(loc=media_pl, scale=std_pl, size=n)

    return {
        "gaussiana": gaussiana,
        "power_law": power_law,
    }


def tabla_probabilidades_extremas(sigmas=[3, 4, 5, 6], alpha=2.5):
    """
    Calcula P(X > μ + kσ) para Gaussiana vs Power-law.

    Muestra cómo los eventos extremos son mucho más probables
    bajo distribuciones de cola pesada.

    Parameters
    ----------
    sigmas : list of float
        Múltiplos de desviación estándar para evaluar.
    alpha : float
        Exponente de la ley de potencia.

    Returns
    -------
    pandas.DataFrame con columnas: sigma, P_gaussiana, P_power_law, ratio.
    """
    from scipy import stats

    resultados = []
    for k in sigmas:
        # Gaussiana: probabilidad en la cola
        p_gauss = stats.norm.sf(k)  # 1 - CDF(k)

        # Power-law (Pareto): P(X > x) = x^(-alpha) para x >= 1
        # Normalizar: x = 1 + k * sigma_pareto / media_pareto
        # Para Pareto con shape alpha: mean = alpha/(alpha-1), var = alpha/((alpha-1)^2*(alpha-2))
        if alpha > 2:
            media_pareto = alpha / (alpha - 1)
            std_pareto = np.sqrt(alpha / ((alpha - 1)**2 * (alpha - 2)))
            x_umbral = media_pareto + k * std_pareto
            p_pareto = x_umbral ** (-alpha) if x_umbral > 1 else 1.0
        else:
            p_pareto = np.nan

        ratio = p_pareto / p_gauss if p_gauss > 0 else np.inf

        resultados.append({
            "σ": f"{k}σ",
            "P(Gaussiana)": f"{p_gauss:.2e}",
            "P(Power-law)": f"{p_pareto:.2e}",
            "Ratio (PL/G)": f"{ratio:.0f}×",
        })

    return pd.DataFrame(resultados)


# ─────────────────────────────────────────────────────────────────────
# LOCK-IN / DEPENDENCIA DE CAMINO
# ─────────────────────────────────────────────────────────────────────

def simular_lockin(n_agentes=200, n_pasos=100, ventaja_inicial=5,
                    rendimientos_crecientes=True, seed=42):
    """
    Simula competencia entre 2 estándares (A vs B).

    Si rendimientos_crecientes=True: la probabilidad de adoptar un
    estándar crece con su cuota de mercado (feedback positivo).
    Si False: elección puramente aleatoria (50/50).

    Parameters
    ----------
    n_agentes : int
        Número total de agentes.
    n_pasos : int
        Número de rondas de adopción.
    ventaja_inicial : int
        Número de adoptantes iniciales extra de A sobre B.
    rendimientos_crecientes : bool
        Si True, probabilidad proporcional al market share.
    seed : int
        Semilla aleatoria.

    Returns
    -------
    dict con claves 't', 'share_A', 'share_B' (arrays de proporción 0-1).
    """
    rng = np.random.default_rng(seed)

    # Estado inicial: ventaja para A
    adopcion_A = (n_agentes // 2) + ventaja_inicial
    adopcion_B = n_agentes // 2
    total = adopcion_A + adopcion_B

    t = np.arange(n_pasos)
    share_A = np.zeros(n_pasos)
    share_B = np.zeros(n_pasos)

    for paso in range(n_pasos):
        share_A[paso] = adopcion_A / total
        share_B[paso] = adopcion_B / total

        # Nuevos agentes adoptan
        nuevos = rng.integers(1, 4)  # 1-3 nuevos agentes por paso

        for _ in range(nuevos):
            if rendimientos_crecientes:
                prob_A = adopcion_A / total
            else:
                prob_A = 0.5

            if rng.random() < prob_A:
                adopcion_A += 1
            else:
                adopcion_B += 1
            total += 1

    return {"t": t, "share_A": share_A, "share_B": share_B}


# ─────────────────────────────────────────────────────────────────────
# TIPPING POINTS (PAISAJE DE POTENCIAL)
# ─────────────────────────────────────────────────────────────────────

def paisaje_potencial(x, parametro):
    """
    Potencial de doble pozo:  V(x) = x⁴/4 − parámetro·x²/2

    - parametro > 0: dos pozos (dos estados estables)
    - parametro ≤ 0: un solo pozo (un estado estable)

    Parameters
    ----------
    x : float or array
        Variable de estado.
    parametro : float
        Parámetro de bifurcación.

    Returns
    -------
    V : float or array
    """
    return x**4 / 4 - parametro * x**2 / 2


def plot_tipping_point(parametro, ax=None):
    """
    Dibuja el paisaje de energía potencial con una bola en el mínimo.

    Parameters
    ----------
    parametro : float
        Parámetro de bifurcación del potencial.
    ax : matplotlib.axes.Axes, optional
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    x = np.linspace(-3, 3, 300)
    V = paisaje_potencial(x, parametro)

    ax.plot(x, V, color=viz.COLORS["primary"], linewidth=2.5)
    ax.fill_between(x, V, V.max(), alpha=0.08, color=viz.COLORS["primary"])

    # Encontrar mínimos para colocar la bola
    from scipy.signal import argrelmin
    minimos = argrelmin(V, order=20)[0]

    if len(minimos) == 0:
        # Un solo mínimo en x=0
        idx_min = np.argmin(V)
        ax.plot(x[idx_min], V[idx_min], "o", color=viz.COLORS["accent"],
                markersize=18, zorder=5, markeredgecolor="white",
                markeredgewidth=2)
    else:
        for m in minimos:
            ax.plot(x[m], V[m], "o", color=viz.COLORS["accent"],
                    markersize=18, zorder=5, markeredgecolor="white",
                    markeredgewidth=2)

    # Estética
    estado = "Dos estados estables" if parametro > 0 else "Un estado estable"
    ax.set_title(f"Paisaje de potencial (r = {parametro:.1f}): {estado}",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("Estado del sistema")
    ax.set_ylabel("Energía potencial V(x)")
    ax.set_ylim(V.min() - 0.5, min(V.max(), 5))

    return ax


# ─────────────────────────────────────────────────────────────────────
# DIAGRAMAS DE LAZO CAUSAL (CLD)
# ─────────────────────────────────────────────────────────────────────

def dibujar_cld(variables, flechas, lazos=None, titulo=None, ax=None):
    """
    Dibuja un Diagrama de Lazo Causal (CLD) usando networkx.

    Parameters
    ----------
    variables : list of str
        Nombres de las variables del sistema.
    flechas : list of (str, str, str)
        Cada tupla es (origen, destino, polaridad) donde polaridad
        es '+' (refuerzo) o '-' (balance).
    lazos : list of (str, str, (float, float)), optional
        Cada tupla es (nombre, tipo, posicion_xy) donde:
        - nombre: etiqueta del lazo (e.g., 'R1', 'B1')
        - tipo: 'R' (refuerzo) o 'B' (balance)
        - posicion_xy: (x, y) para colocar la etiqueta
    titulo : str, optional
        Título del diagrama.
    ax : matplotlib.axes.Axes, optional

    Example
    -------
    >>> variables = ["Población", "Nacimientos", "Muertes"]
    >>> flechas = [("Población", "Nacimientos", "+"),
    ...            ("Nacimientos", "Población", "+"),
    ...            ("Población", "Muertes", "+"),
    ...            ("Muertes", "Población", "-")]
    >>> dibujar_cld(variables, flechas)
    """
    import networkx as nx

    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # Construir grafo dirigido
    G = nx.DiGraph()
    G.add_nodes_from(variables)

    for origen, destino, polaridad in flechas:
        G.add_edge(origen, destino, polaridad=polaridad)

    # Layout circular (funciona bien para CLDs)
    pos = nx.circular_layout(G)

    # Dibujar nodos
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_color="white",
        node_size=3000,
        edgecolors=viz.COLORS["primary"],
        linewidths=2.0,
    )

    # Etiquetas de nodos
    nx.draw_networkx_labels(
        G, pos, ax=ax,
        font_size=9,
        font_weight="bold",
        font_color="#1E293B",
    )

    # Dibujar flechas coloreadas por polaridad
    for origen, destino, polaridad in flechas:
        color = viz.COLORS["primary"] if polaridad == "+" else viz.COLORS["danger"]
        estilo = "solid" if polaridad == "+" else "dashed"

        nx.draw_networkx_edges(
            G, pos, ax=ax,
            edgelist=[(origen, destino)],
            edge_color=color,
            style=estilo,
            width=2.0,
            arrows=True,
            arrowsize=20,
            connectionstyle="arc3,rad=0.15",
            min_source_margin=30,
            min_target_margin=30,
        )

        # Etiqueta de polaridad en el borde
        x_mid = (pos[origen][0] + pos[destino][0]) / 2
        y_mid = (pos[origen][1] + pos[destino][1]) / 2
        # Desplazar ligeramente para no superponer
        dx = pos[destino][0] - pos[origen][0]
        dy = pos[destino][1] - pos[origen][1]
        norm = np.sqrt(dx**2 + dy**2) + 1e-8
        offset_x = -dy / norm * 0.08
        offset_y = dx / norm * 0.08
        ax.text(x_mid + offset_x, y_mid + offset_y, polaridad,
                fontsize=14, fontweight="bold", color=color,
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                          edgecolor="none", alpha=0.8))

    # Etiquetas de lazos
    if lazos:
        for nombre, tipo, (lx, ly) in lazos:
            color_lazo = viz.COLORS["primary"] if tipo == "R" else viz.COLORS["danger"]
            icono = "↻" if tipo == "R" else "↺"
            ax.text(lx, ly, f"{icono} {nombre}",
                    fontsize=16, fontweight="bold",
                    color=color_lazo, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.3",
                              facecolor="white", edgecolor=color_lazo,
                              linewidth=2, alpha=0.9))

    if titulo:
        ax.set_title(titulo, fontsize=14, fontweight="bold", pad=15)

    ax.axis("off")
    ax.set_aspect("equal")

    return ax


def cld_el_nino():
    """
    CLD pre-construido de la crisis de El Niño 2015-2016 en Colombia.

    Muestra 4 lazos interconectados:
    - R1: Espiral de precios (precio ↑ → costos ↑ → inflación ↑ → precio ↑)
    - B1: Respuesta regulatoria (precio ↑ → intervención → restricción demanda)
    - R2: Desinversión (precio bajo → poca inversión → escasez → precio alto)
    - B2: Señal hidrológica (sequía → embalses bajos → térmicas → emisiones
           → presión ambiental)

    Returns
    -------
    tuple (variables, flechas, lazos) lista para dibujar_cld().
    """
    variables = [
        "Sequía\n(El Niño)",
        "Nivel\nembalses",
        "Generación\nhidro",
        "Generación\ntérmica",
        "Precio\nbolsa",
        "Costos\nindustriales",
        "Demanda\neléctrica",
        "Inversión\nen capacidad",
    ]

    flechas = [
        # R1: Espiral de costos
        ("Sequía\n(El Niño)", "Nivel\nembalses", "-"),
        ("Nivel\nembalses", "Generación\nhidro", "+"),
        ("Generación\nhidro", "Generación\ntérmica", "-"),
        ("Generación\ntérmica", "Precio\nbolsa", "+"),
        ("Precio\nbolsa", "Costos\nindustriales", "+"),

        # B1: Respuesta regulatoria / demanda
        ("Precio\nbolsa", "Demanda\neléctrica", "-"),

        # R2: Ciclo inversión
        ("Precio\nbolsa", "Inversión\nen capacidad", "+"),
        ("Inversión\nen capacidad", "Generación\nhidro", "+"),

        # B2: Feedback demanda-precio
        ("Demanda\neléctrica", "Precio\nbolsa", "+"),
    ]

    lazos = [
        ("R1", "R", (-0.45, 0.0)),
        ("B1", "B", (0.45, -0.3)),
        ("R2", "R", (0.45, 0.3)),
        ("B2", "B", (-0.45, -0.45)),
    ]

    return variables, flechas, lazos
