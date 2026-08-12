"""
Soporte para Semana 3: Dinámica sobre Redes — MISE Systems Analytics
=====================================================================
Modelos de contagio (simple y complejo), cascadas por umbrales,
modelo de Bass, análisis de redes bipartitas y detección de comunidades.

Funciones de alto nivel para que el estudiante explore los conceptos
sin preocuparse por detalles de implementación.
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit
from . import viz


# ─────────────────────────────────────────────────────────────────────
# CONTAGIO SIMPLE (SI)
# ─────────────────────────────────────────────────────────────────────

def simular_contagio_simple(G, semillas, beta=0.1, n_pasos=30, seed=42):
    """
    Modelo SI (Susceptible → Infectado) sobre una red.

    En cada paso, cada nodo infectado intenta contagiar a cada vecino
    susceptible con probabilidad *beta*.

    Parameters
    ----------
    G : networkx.Graph
    semillas : set or list
        Nodos inicialmente infectados.
    beta : float
        Probabilidad de transmisión por arista por paso.
    n_pasos : int
    seed : int

    Returns
    -------
    historia : list[set]
        Lista de conjuntos; historia[t] = nodos infectados en el paso t.
    """
    rng = np.random.default_rng(seed)
    infectados = set(semillas)
    historia = [infectados.copy()]

    for _ in range(n_pasos):
        nuevos = set()
        for nodo in infectados:
            for vecino in G.neighbors(nodo):
                if vecino not in infectados and vecino not in nuevos:
                    if rng.random() < beta:
                        nuevos.add(vecino)
        infectados = infectados | nuevos
        historia.append(infectados.copy())
        # Parar si todos infectados
        if len(infectados) == len(G):
            break

    return historia


def curva_contagio(historia, N):
    """
    Convierte una historia de contagio en arrays numéricos.

    Parameters
    ----------
    historia : list[set]
    N : int
        Número total de nodos.

    Returns
    -------
    t : np.ndarray
    fraccion : np.ndarray
        Fracción de la población infectada en cada paso.
    """
    t = np.arange(len(historia))
    fraccion = np.array([len(s) / N for s in historia])
    return t, fraccion


def plot_propagacion(G, historia, layout=None, pasos_mostrar=None):
    """
    Visualización multi-panel de la propagación sobre la red.

    Parameters
    ----------
    G : networkx.Graph
    historia : list[set]
    layout : dict, optional
        Posiciones de nodos. Si None, se usa spring_layout.
    pasos_mostrar : list[int], optional
        Índices de pasos a mostrar. Si None, se seleccionan 6 automáticamente.

    Returns
    -------
    fig : matplotlib.figure.Figure
    """
    if layout is None:
        layout = nx.spring_layout(G, seed=42, k=1.5 / np.sqrt(max(len(G), 1)))

    if pasos_mostrar is None:
        n_total = len(historia)
        if n_total <= 6:
            pasos_mostrar = list(range(n_total))
        else:
            indices = np.linspace(0, n_total - 1, 6, dtype=int)
            pasos_mostrar = list(indices)

    n_panels = len(pasos_mostrar)
    cols = min(n_panels, 3)
    rows = (n_panels + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))
    if n_panels == 1:
        axes = np.array([axes])
    axes = np.array(axes).flatten()

    for idx, paso in enumerate(pasos_mostrar):
        ax = axes[idx]
        infectados = historia[min(paso, len(historia) - 1)]

        colores = [
            viz.COLORS["node_active"] if n in infectados
            else viz.COLORS["node_default"]
            for n in G.nodes()
        ]

        nx.draw_networkx_edges(G, layout, edge_color=viz.COLORS["edge_default"],
                               width=0.8, alpha=0.4, ax=ax)
        nx.draw_networkx_nodes(G, layout, node_color=colores,
                               node_size=150, ax=ax,
                               edgecolors="#334155", linewidths=0.8)

        frac = len(infectados) / len(G) * 100
        ax.set_title(f"Paso {paso} — {frac:.0f}% infectados",
                     fontsize=11, fontweight="bold")
        ax.axis("off")

    # Ocultar paneles sobrantes
    for idx in range(n_panels, len(axes)):
        axes[idx].set_visible(False)

    fig.suptitle("Propagación del contagio en la red",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────
# CONTAGIO COMPLEJO (MODELO DE UMBRALES)
# ─────────────────────────────────────────────────────────────────────

def simular_contagio_complejo(G, semillas, umbral=0.25, n_pasos=50, seed=42):
    """
    Modelo de umbrales (contagio complejo).

    Un nodo adopta si la fracción de sus vecinos que ya adoptaron
    es ≥ umbral. El umbral puede ser un float (igual para todos)
    o un dict {nodo: umbral}.

    Parameters
    ----------
    G : networkx.Graph
    semillas : set or list
    umbral : float or dict
        Si float, se aplica a todos los nodos.
        Si dict, {nodo: umbral_individual}.
    n_pasos : int
    seed : int

    Returns
    -------
    historia : list[set]
    """
    adoptantes = set(semillas)
    historia = [adoptantes.copy()]

    # Normalizar umbrales a diccionario
    if isinstance(umbral, (int, float)):
        umbrales = {n: float(umbral) for n in G.nodes()}
    else:
        umbrales = dict(umbral)

    for _ in range(n_pasos):
        nuevos = set()
        for nodo in G.nodes():
            if nodo not in adoptantes:
                grado = G.degree(nodo)
                if grado == 0:
                    continue
                vecinos_adoptantes = sum(
                    1 for v in G.neighbors(nodo) if v in adoptantes
                )
                fraccion = vecinos_adoptantes / grado
                if fraccion >= umbrales.get(nodo, 0.25):
                    nuevos.add(nodo)

        if not nuevos:
            break
        adoptantes = adoptantes | nuevos
        historia.append(adoptantes.copy())

    return historia


def comparar_simple_vs_complejo(G, semillas, beta, umbral,
                                 n_pasos=30, seed=42):
    """
    Ejecuta contagio simple y complejo, y grafica ambas curvas.

    Parameters
    ----------
    G : networkx.Graph
    semillas : set or list
    beta : float
    umbral : float or dict
    n_pasos : int
    seed : int

    Returns
    -------
    fig : matplotlib.figure.Figure
    """
    hist_simple = simular_contagio_simple(G, semillas, beta, n_pasos, seed)
    hist_complejo = simular_contagio_complejo(G, semillas, umbral, n_pasos, seed)

    N = len(G)
    t_s, f_s = curva_contagio(hist_simple, N)
    t_c, f_c = curva_contagio(hist_complejo, N)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Panel izquierdo: curvas de adopción
    ax1.plot(t_s, f_s * 100, color=viz.COLORS["danger"],
             linewidth=2.5, label=f"Simple (β={beta})")
    ax1.plot(t_c, f_c * 100, color=viz.COLORS["success"],
             linewidth=2.5, label=f"Complejo (θ={umbral})")
    ax1.fill_between(t_s, 0, f_s * 100, color=viz.COLORS["danger"], alpha=0.1)
    ax1.fill_between(t_c, 0, f_c * 100, color=viz.COLORS["success"], alpha=0.1)
    ax1.set_xlabel("Paso de tiempo")
    ax1.set_ylabel("% de la red adoptante")
    ax1.set_title("Contagio simple vs complejo", fontweight="bold")
    ax1.legend()
    ax1.set_ylim(0, 105)

    # Panel derecho: velocidad (nuevos por paso)
    nuevos_s = np.diff([len(s) for s in hist_simple])
    nuevos_c = np.diff([len(s) for s in hist_complejo])
    ax2.bar(range(len(nuevos_s)), nuevos_s, alpha=0.6,
            color=viz.COLORS["danger"], label="Simple")
    t_c_idx = range(len(nuevos_c))
    ax2.bar(t_c_idx, nuevos_c, alpha=0.6,
            color=viz.COLORS["success"], label="Complejo")
    ax2.set_xlabel("Paso de tiempo")
    ax2.set_ylabel("Nuevos adoptantes")
    ax2.set_title("Velocidad de adopción", fontweight="bold")
    ax2.legend()

    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────
# UMBRALES Y VENTANA DE CASCADA
# ─────────────────────────────────────────────────────────────────────

def generar_umbrales(G, distribucion='uniforme', mu=0.25, sigma=0.1, seed=42):
    """
    Genera umbrales de adopción para cada nodo.

    Parameters
    ----------
    G : networkx.Graph
    distribucion : str
        'uniforme' : U(0, 0.5)
        'normal'   : N(mu, sigma), truncado en [0, 1]
        'bimodal'  : mezcla de N(0.15, 0.05) y N(0.40, 0.05)
    mu : float
    sigma : float
    seed : int

    Returns
    -------
    dict : {nodo: umbral}
    """
    rng = np.random.default_rng(seed)
    nodos = list(G.nodes())
    n = len(nodos)

    if distribucion == 'uniforme':
        valores = rng.uniform(0, 0.5, size=n)
    elif distribucion == 'normal':
        valores = rng.normal(mu, sigma, size=n)
        valores = np.clip(valores, 0, 1)
    elif distribucion == 'bimodal':
        grupo = rng.random(size=n) < 0.5
        valores = np.where(
            grupo,
            rng.normal(0.15, 0.05, size=n),
            rng.normal(0.40, 0.05, size=n)
        )
        valores = np.clip(valores, 0, 1)
    else:
        raise ValueError(f"Distribución '{distribucion}' no reconocida. "
                         f"Use: 'uniforme', 'normal', 'bimodal'.")

    return dict(zip(nodos, valores))


def ventana_cascada(G, umbral_range=None, n_semillas=3,
                    n_repeticiones=20, seed=42):
    """
    Calcula la ventana de cascada: rango de umbrales que produce
    cascadas globales (>50% de la red adopta).

    Parameters
    ----------
    G : networkx.Graph
    umbral_range : array-like, optional
        Valores de umbral a probar. Default: np.linspace(0.05, 0.5, 20)
    n_semillas : int
        Número de semillas por repetición.
    n_repeticiones : int
    seed : int

    Returns
    -------
    umbrales : np.ndarray
    prob_cascada : np.ndarray
        Probabilidad de cascada global para cada umbral.
    """
    rng = np.random.default_rng(seed)
    nodos = list(G.nodes())

    if umbral_range is None:
        umbral_range = np.linspace(0.05, 0.5, 20)
    else:
        umbral_range = np.asarray(umbral_range)

    prob_cascada = np.zeros(len(umbral_range))

    for i, theta in enumerate(umbral_range):
        cascadas = 0
        for rep in range(n_repeticiones):
            semillas = set(rng.choice(nodos, size=min(n_semillas, len(nodos)),
                                       replace=False))
            hist = simular_contagio_complejo(G, semillas, umbral=theta,
                                             n_pasos=100)
            fraccion_final = len(hist[-1]) / len(G)
            if fraccion_final > 0.5:
                cascadas += 1
        prob_cascada[i] = cascadas / n_repeticiones

    return umbral_range, prob_cascada


# ─────────────────────────────────────────────────────────────────────
# MODELO DE BASS
# ─────────────────────────────────────────────────────────────────────

def bass_ode(t, F, p, q):
    """
    ODE del modelo de Bass.

    dF/dt = (p + q·F)(1 - F)

    Parameters
    ----------
    t : float — tiempo (no se usa explícitamente pero requerido por solve_ivp)
    F : float — fracción acumulada de adoptantes
    p : float — coeficiente de innovación
    q : float — coeficiente de imitación

    Returns
    -------
    dFdt : float
    """
    return (p + q * F) * (1 - F)


def bass_analitica(t, p, q):
    """
    Solución analítica del modelo de Bass.

    F(t) = (1 - exp(-(p+q)·t)) / (1 + (q/p)·exp(-(p+q)·t))

    Parameters
    ----------
    t : float or array — tiempo
    p : float — coeficiente de innovación
    q : float — coeficiente de imitación

    Returns
    -------
    F : float or array — fracción acumulada de adoptantes
    """
    t = np.asarray(t, dtype=float)
    exp_term = np.exp(-(p + q) * t)
    return (1 - exp_term) / (1 + (q / p) * exp_term)


def resolver_bass(p=0.01, q=0.3, T=30, F0=0.001):
    """
    Resuelve el modelo de Bass numéricamente.

    Parameters
    ----------
    p : float — coeficiente de innovación
    q : float — coeficiente de imitación
    T : float — horizonte temporal
    F0 : float — fracción inicial de adoptantes

    Returns
    -------
    t : np.ndarray — tiempos
    F : np.ndarray — fracción acumulada
    dFdt : np.ndarray — tasa de adopción (nuevos adoptantes / dt)
    """
    t_eval = np.linspace(0, T, 300)
    sol = solve_ivp(
        lambda t, F: bass_ode(t, F, p, q),
        [0, T], [F0],
        t_eval=t_eval,
        method='RK45',
        max_step=0.1
    )
    t = sol.t
    F = sol.y[0]
    dFdt = (p + q * F) * (1 - F)
    return t, F, dFdt


def ajustar_bass(años, datos_normalizados):
    """
    Ajusta los parámetros p y q del modelo de Bass a datos empíricos.

    Parameters
    ----------
    años : array-like
        Años (se normalizan a t = año - año_min).
    datos_normalizados : array-like
        Fracción acumulada de adopción (entre 0 y 1).

    Returns
    -------
    p_opt : float — coeficiente de innovación óptimo
    q_opt : float — coeficiente de imitación óptimo
    F_ajustada : np.ndarray — curva ajustada
    """
    años = np.asarray(años, dtype=float)
    datos = np.asarray(datos_normalizados, dtype=float)
    t = años - años.min()

    def bass_para_ajuste(t_arr, p, q):
        return bass_analitica(t_arr, p, q)

    try:
        popt, pcov = curve_fit(
            bass_para_ajuste, t, datos,
            p0=[0.01, 0.3],
            bounds=([1e-6, 1e-6], [1.0, 2.0]),
            maxfev=10000
        )
    except RuntimeError:
        # Fallback con parámetros iniciales diferentes
        popt, pcov = curve_fit(
            bass_para_ajuste, t, datos,
            p0=[0.005, 0.5],
            bounds=([1e-6, 1e-6], [1.0, 2.0]),
            maxfev=20000
        )

    p_opt, q_opt = popt
    F_ajustada = bass_analitica(t, p_opt, q_opt)

    return p_opt, q_opt, F_ajustada


def plot_bass(t, F, dFdt, p, q, titulo=None):
    """
    Grafica el modelo de Bass: curva S y campana de adopción.

    Parameters
    ----------
    t, F, dFdt : arrays del modelo
    p, q : parámetros
    titulo : str, optional

    Returns
    -------
    fig : matplotlib.figure.Figure
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Curva S (acumulada)
    ax1.plot(t, F * 100, color=viz.COLORS["primary"], linewidth=2.5)
    ax1.fill_between(t, 0, F * 100, color=viz.COLORS["primary"], alpha=0.1)
    ax1.axhline(y=50, color=viz.COLORS["danger"], linestyle='--', alpha=0.5,
                label="50% adopción")
    ax1.set_xlabel("Tiempo")
    ax1.set_ylabel("% adopción acumulada")
    ax1.set_title("Curva S — Adopción acumulada", fontweight="bold")
    ax1.legend()
    ax1.set_ylim(0, 105)

    # Campana (tasa)
    ax2.plot(t, dFdt * 100, color=viz.COLORS["accent"], linewidth=2.5)
    ax2.fill_between(t, 0, dFdt * 100, color=viz.COLORS["accent"], alpha=0.2)
    ax2.set_xlabel("Tiempo")
    ax2.set_ylabel("Tasa de adopción (%/periodo)")
    ax2.set_title("Campana — Nuevos adoptantes por periodo", fontweight="bold")

    sup = titulo or f"Modelo de Bass (p={p:.4f}, q={q:.3f})"
    fig.suptitle(sup, fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────
# REDES BIPARTITAS / ACTORES
# ─────────────────────────────────────────────────────────────────────

def analizar_red_bipartita(G):
    """
    Analiza una red bipartita generador-comercializador.

    Parameters
    ----------
    G : networkx.Graph
        Con atributo 'tipo' en cada nodo ('generador' o 'comercializador').

    Returns
    -------
    dict con claves:
        'proyeccion_gen'  : nx.Graph — proyección sobre generadores
        'proyeccion_com'  : nx.Graph — proyección sobre comercializadores
        'metricas'        : pd.DataFrame — métricas por nodo
    """
    generadores = {n for n, d in G.nodes(data=True) if d.get("tipo") == "generador"}
    comercializadores = {n for n, d in G.nodes(data=True)
                          if d.get("tipo") == "comercializador"}

    # Proyecciones
    proy_gen = nx.bipartite.projected_graph(G, generadores)
    proy_com = nx.bipartite.projected_graph(G, comercializadores)

    # Métricas
    grado = dict(G.degree())
    betweenness = nx.betweenness_centrality(G)

    # Volumen total por nodo
    volumen = {}
    for n in G.nodes():
        vol = sum(d.get("volumen_gwh", 0)
                  for _, _, d in G.edges(n, data=True))
        volumen[n] = round(vol, 1)

    registros = []
    for n in G.nodes():
        tipo = G.nodes[n].get("tipo", "desconocido")
        registros.append({
            "nodo": n,
            "tipo": tipo,
            "grado": grado[n],
            "betweenness": round(betweenness[n], 4),
            "volumen_gwh": volumen[n],
        })

    df = pd.DataFrame(registros).sort_values("volumen_gwh", ascending=False)

    return {
        "proyeccion_gen": proy_gen,
        "proyeccion_com": proy_com,
        "metricas": df,
    }


def visualizar_red_bipartita(G, ax=None):
    """
    Dibuja una red bipartita con generadores y comercializadores
    en colores diferentes y disposición bipartita.

    Parameters
    ----------
    G : networkx.Graph
        Con atributo 'tipo' en cada nodo.
    ax : matplotlib.axes.Axes, optional

    Returns
    -------
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    generadores = [n for n, d in G.nodes(data=True)
                    if d.get("tipo") == "generador"]
    comercializadores = [n for n, d in G.nodes(data=True)
                          if d.get("tipo") == "comercializador"]

    # Layout bipartito manual
    pos = {}
    for i, n in enumerate(sorted(generadores)):
        pos[n] = (0, -i * 1.2)
    for i, n in enumerate(sorted(comercializadores)):
        pos[n] = (3, -i * 1.2 - 0.5)

    # Aristas con grosor proporcional al volumen
    edge_widths = []
    for u, v, d in G.edges(data=True):
        vol = d.get("volumen_gwh", 100)
        edge_widths.append(max(0.5, vol / 300))

    nx.draw_networkx_edges(G, pos, width=edge_widths,
                           edge_color=viz.COLORS["edge_default"],
                           alpha=0.5, ax=ax)

    # Generadores
    nx.draw_networkx_nodes(G, pos, nodelist=generadores,
                           node_color=viz.COLORS["primary"],
                           node_size=700, ax=ax,
                           edgecolors="#1E293B", linewidths=1.5,
                           label="Generadores")

    # Comercializadores
    nx.draw_networkx_nodes(G, pos, nodelist=comercializadores,
                           node_color=viz.COLORS["accent"],
                           node_size=700, ax=ax,
                           edgecolors="#1E293B", linewidths=1.5,
                           label="Comercializadores")

    nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold",
                            font_color="#1E293B", ax=ax)

    ax.set_title("Red bipartita: Mercado mayorista",
                 fontsize=14, fontweight="bold")
    ax.legend(loc="upper right", fontsize=10)
    ax.axis("off")
    return ax


# ─────────────────────────────────────────────────────────────────────
# DETECCIÓN DE COMUNIDADES
# ─────────────────────────────────────────────────────────────────────

def detectar_comunidades(G, metodo='greedy'):
    """
    Detecta comunidades en una red.

    Parameters
    ----------
    G : networkx.Graph
    metodo : str
        'greedy' — Greedy modularity optimization (Clauset-Newman-Moore)

    Returns
    -------
    comunidades : list[set]
        Lista de conjuntos de nodos por comunidad.
    modularidad : float
        Valor Q de modularidad.
    """
    if metodo == 'greedy':
        comunidades = list(
            nx.community.greedy_modularity_communities(G)
        )
    else:
        raise ValueError(f"Método '{metodo}' no soportado. Use: 'greedy'.")

    modularidad = nx.community.modularity(G, comunidades)
    return comunidades, modularidad


def visualizar_comunidades(G, comunidades, layout=None, ax=None):
    """
    Dibuja la red con nodos coloreados por comunidad.

    Parameters
    ----------
    G : networkx.Graph
    comunidades : list[set]
    layout : dict, optional
    ax : matplotlib.axes.Axes, optional

    Returns
    -------
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    if layout is None:
        layout = nx.spring_layout(G, seed=42, k=1.5 / np.sqrt(max(len(G), 1)))

    # Paleta de colores para comunidades
    palette = [
        viz.COLORS["primary"], viz.COLORS["danger"], viz.COLORS["success"],
        viz.COLORS["accent"], viz.COLORS["secondary"], viz.COLORS["warning"],
        "#06B6D4", "#EC4899", "#8B5CF6", "#14B8A6",
    ]

    # Asignar color a cada nodo
    node_colors = {}
    for i, comunidad in enumerate(comunidades):
        color = palette[i % len(palette)]
        for nodo in comunidad:
            node_colors[nodo] = color

    color_list = [node_colors.get(n, viz.COLORS["node_default"])
                  for n in G.nodes()]

    nx.draw_networkx_edges(G, layout, edge_color=viz.COLORS["edge_default"],
                           width=0.8, alpha=0.4, ax=ax)
    nx.draw_networkx_nodes(G, layout, node_color=color_list,
                           node_size=200, ax=ax,
                           edgecolors="#334155", linewidths=0.8)
    nx.draw_networkx_labels(G, layout, font_size=7, ax=ax)

    ax.set_title(f"Comunidades detectadas: {len(comunidades)} grupos",
                 fontsize=14, fontweight="bold")
    ax.axis("off")
    return ax


# ─────────────────────────────────────────────────────────────────────
# FALLA EN CASCADA (MOTTER-LAI SIMPLIFICADO)
# ─────────────────────────────────────────────────────────────────────

def simular_falla_cascada(G, nodo_inicial, capacidad_factor=1.5, n_max=50):
    """
    Simulación simplificada del modelo de Motter-Lai para fallas en cascada.

    La carga de cada nodo es su betweenness centrality. La capacidad
    es capacidad_factor × carga_inicial. Si al remover nodos la carga
    redistribuida excede la capacidad, el nodo falla.

    Parameters
    ----------
    G : networkx.Graph
    nodo_inicial : str or int
        Nodo que falla inicialmente.
    capacidad_factor : float
        Factor de tolerancia (α). Capacidad = α × carga_inicial.
    n_max : int
        Máximo de pasos de cascada.

    Returns
    -------
    historia : list[set]
        Nodos fallados acumulados en cada paso.
    cargas : list[dict]
        Diccionario de cargas por nodo en cada paso.
    """
    H = G.copy()

    # Carga inicial = betweenness
    carga_inicial = nx.betweenness_centrality(H)
    capacidad = {n: capacidad_factor * max(carga_inicial[n], 1e-6)
                 for n in H.nodes()}

    fallados = {nodo_inicial}
    historia = [fallados.copy()]
    cargas_hist = [dict(carga_inicial)]

    for _ in range(n_max):
        # Remover nodos fallados
        H_temp = H.copy()
        H_temp.remove_nodes_from(fallados)

        if len(H_temp) == 0:
            break

        # Recalcular cargas
        nueva_carga = nx.betweenness_centrality(H_temp)
        cargas_hist.append(dict(nueva_carga))

        # Verificar sobrecarga
        nuevos_fallados = set()
        for nodo, carga in nueva_carga.items():
            if nodo not in fallados and carga > capacidad.get(nodo, float('inf')):
                nuevos_fallados.add(nodo)

        if not nuevos_fallados:
            break

        fallados = fallados | nuevos_fallados
        historia.append(fallados.copy())

    return historia, cargas_hist


def plot_falla_cascada(G, historia, layout=None):
    """
    Visualización paso a paso de una falla en cascada.

    Parameters
    ----------
    G : networkx.Graph
    historia : list[set]
    layout : dict, optional

    Returns
    -------
    fig : matplotlib.figure.Figure
    """
    if layout is None:
        layout = nx.spring_layout(G, seed=42, k=1.5 / np.sqrt(max(len(G), 1)))

    n_pasos = min(len(historia), 6)
    if n_pasos <= 3:
        cols = n_pasos
    else:
        cols = 3
    rows = (n_pasos + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))
    if n_pasos == 1:
        axes = np.array([axes])
    axes = np.array(axes).flatten()

    for idx in range(n_pasos):
        ax = axes[idx]
        fallados = historia[idx]
        viz.plot_cascade_step(G, layout, fallados, idx, ax=ax,
                              title=f"Paso {idx}: {len(fallados)} nodos fallados")

    for idx in range(n_pasos, len(axes)):
        axes[idx].set_visible(False)

    fig.suptitle("Falla en cascada (Motter-Lai)",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig
