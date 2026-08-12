"""
Soporte para Semana 2: Redes y Topología — MISE Systems Analytics
===================================================================
Funciones de soporte para el notebook de la Semana 2.
Incluye: construcción de grafos, métricas de centralidad,
generadores de topologías, análisis de resiliencia y cascadas.

La filosofía es que el estudiante interactúa con funciones de alto
nivel y se concentra en los conceptos. La implementación detallada
vive aquí.
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from . import viz


# ─────────────────────────────────────────────────────────────────────
# CONSTRUCCIÓN DE GRAFOS
# ─────────────────────────────────────────────────────────────────────

def crear_red_aeropuertos(n=50, seed=42):
    """
    Red scale-free de rutas aéreas (Barabási-Albert).

    Los hubs con mayor grado se etiquetan con nombres de ciudades
    principales colombianas.

    Parameters
    ----------
    n : int
        Número de aeropuertos.
    seed : int
        Semilla para reproducibilidad.

    Returns
    -------
    nx.Graph
        Con atributo 'city' por nodo.
    """
    G = nx.barabasi_albert_graph(n, m=2, seed=seed)

    ciudades_principales = [
        "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
        "Bucaramanga", "Pereira", "Santa Marta", "Cúcuta", "Ibagué",
        "Villavicencio", "Manizales", "Pasto", "Neiva", "Montería",
    ]

    # Ordenar nodos por grado descendente
    nodos_por_grado = sorted(G.degree(), key=lambda x: x[1], reverse=True)

    for i, (nodo, _) in enumerate(nodos_por_grado):
        if i < len(ciudades_principales):
            G.nodes[nodo]["city"] = ciudades_principales[i]
        else:
            G.nodes[nodo]["city"] = f"Aero-{nodo}"

    return G


def crear_red_social_clase(n=30, seed=42):
    """
    Red small-world de una clase (Watts-Strogatz).

    Modela la red social de un salón de clase donde cada persona
    conoce a sus vecinos cercanos con algunas conexiones lejanas.

    Parameters
    ----------
    n : int
        Número de estudiantes.
    seed : int
        Semilla para reproducibilidad.

    Returns
    -------
    nx.Graph
        Con atributo 'nombre' por nodo.
    """
    G = nx.watts_strogatz_graph(n, k=4, p=0.3, seed=seed)

    nombres = [
        "Ana", "Carlos", "María", "Juan", "Laura", "Diego", "Sofía",
        "Andrés", "Valentina", "Daniel", "Isabella", "Sebastián",
        "Camila", "Felipe", "Gabriela", "Nicolás", "Mariana", "Tomás",
        "Daniela", "Alejandro", "Paula", "Santiago", "Sara", "Mateo",
        "Lucía", "Emilio", "Catalina", "Ricardo", "Natalia", "Esteban",
    ]

    for i, nodo in enumerate(G.nodes()):
        G.nodes[nodo]["nombre"] = nombres[i] if i < len(nombres) else f"Est-{i}"

    return G


# ─────────────────────────────────────────────────────────────────────
# MÉTRICAS DE CENTRALIDAD
# ─────────────────────────────────────────────────────────────────────

def calcular_todas_metricas(G):
    """
    Calcula las cuatro métricas principales de centralidad
    para cada nodo de la red.

    Parameters
    ----------
    G : nx.Graph

    Returns
    -------
    pd.DataFrame
        Columnas: nodo, grado, betweenness, closeness, clustering
    """
    degree = dict(G.degree())
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    clustering = nx.clustering(G)

    df = pd.DataFrame({
        "nodo": list(G.nodes()),
        "grado": [degree[n] for n in G.nodes()],
        "betweenness": [round(betweenness[n], 4) for n in G.nodes()],
        "closeness": [round(closeness[n], 4) for n in G.nodes()],
        "clustering": [round(clustering[n], 4) for n in G.nodes()],
    })

    return df.sort_values("grado", ascending=False).reset_index(drop=True)


def tabla_metricas_formateada(G, top_n=10):
    """
    Tabla estilizada con los top-n nodos por cada métrica.

    Parameters
    ----------
    G : nx.Graph
    top_n : int
        Número de nodos a mostrar en cada ranking.

    Returns
    -------
    pd.DataFrame
        Resumen formateado con top nodos por cada métrica.
    """
    df = calcular_todas_metricas(G)

    resultados = {}
    for metrica in ["grado", "betweenness", "closeness", "clustering"]:
        top = df.nlargest(top_n, metrica)[["nodo", metrica]].reset_index(drop=True)
        resultados[f"Top {metrica} (nodo)"] = top["nodo"].values
        resultados[f"Top {metrica} (valor)"] = top[metrica].values

    return pd.DataFrame(resultados)


# ─────────────────────────────────────────────────────────────────────
# GENERADORES DE TOPOLOGÍAS
# ─────────────────────────────────────────────────────────────────────

def generar_tres_topologias(n=200, seed=42):
    """
    Genera las tres topologías clásicas de redes para comparación.

    Parameters
    ----------
    n : int
        Número de nodos.
    seed : int

    Returns
    -------
    dict
        {'Erdős-Rényi': G_er, 'Barabási-Albert': G_ba, 'Watts-Strogatz': G_ws}
    """
    # Erdős-Rényi: conectividad esperada similar a las otras
    p = 6.0 / n  # grado medio ≈ 6
    G_er = nx.erdos_renyi_graph(n, p, seed=seed)

    # Barabási-Albert: m=3 → grado medio ≈ 6
    G_ba = nx.barabasi_albert_graph(n, m=3, seed=seed)

    # Watts-Strogatz: k=6 vecinos, p=0.1 reconexión
    G_ws = nx.watts_strogatz_graph(n, k=6, p=0.1, seed=seed)

    return {
        "Erdős-Rényi": G_er,
        "Barabási-Albert": G_ba,
        "Watts-Strogatz": G_ws,
    }


def comparar_topologias(redes_dict):
    """
    Genera una figura comparativa: 3×2 grid con visualización de la
    red (fila 1) y distribución de grado (fila 2) para cada topología.

    Parameters
    ----------
    redes_dict : dict
        {nombre: nx.Graph}

    Returns
    -------
    matplotlib.figure.Figure
    """
    nombres = list(redes_dict.keys())
    n_redes = len(nombres)

    colores_topo = {
        "Erdős-Rényi": viz.COLORS["erdos_renyi"],
        "Barabási-Albert": viz.COLORS["barabasi_albert"],
        "Watts-Strogatz": viz.COLORS["watts_strogatz"],
    }

    fig, axes = plt.subplots(2, n_redes, figsize=(6 * n_redes, 10))
    if n_redes == 1:
        axes = axes.reshape(2, 1)

    for i, nombre in enumerate(nombres):
        G = redes_dict[nombre]
        color = colores_topo.get(nombre, viz.COLORS["primary"])

        # Fila 1: Visualización de la red
        ax_net = axes[0, i]
        pos = nx.spring_layout(G, seed=42, k=1.5 / np.sqrt(len(G)))

        # Subconjunto para redes grandes (mejor visualización)
        if len(G) > 100:
            # Mostrar solo el componente gigante con spring layout
            largest_cc = max(nx.connected_components(G), key=len)
            H = G.subgraph(largest_cc).copy()
            pos_sub = nx.spring_layout(H, seed=42, k=2.0 / np.sqrt(len(H)))
            nx.draw_networkx_edges(H, pos_sub, ax=ax_net,
                                   edge_color=viz.COLORS["edge_default"],
                                   width=0.3, alpha=0.3)
            nx.draw_networkx_nodes(H, pos_sub, ax=ax_net,
                                   node_color=color, node_size=15,
                                   edgecolors="white", linewidths=0.3)
        else:
            nx.draw_networkx_edges(G, pos, ax=ax_net,
                                   edge_color=viz.COLORS["edge_default"],
                                   width=0.5, alpha=0.4)
            nx.draw_networkx_nodes(G, pos, ax=ax_net,
                                   node_color=color, node_size=30,
                                   edgecolors="white", linewidths=0.5)

        ax_net.set_title(nombre, fontsize=14, fontweight="bold", pad=10)
        n_nodes = G.number_of_nodes()
        n_edges = G.number_of_edges()
        ax_net.text(0.5, -0.05, f"n={n_nodes}, m={n_edges}",
                    transform=ax_net.transAxes, ha="center", fontsize=10,
                    color="#64748B")
        ax_net.axis("off")

        # Fila 2: Distribución de grado
        ax_deg = axes[1, i]
        degrees = [d for _, d in G.degree()]
        unique_k, counts = np.unique(degrees, return_counts=True)
        probs = counts / counts.sum()

        ax_deg.bar(unique_k, probs, color=color, alpha=0.7,
                   edgecolor="white", linewidth=0.5)
        ax_deg.set_xlabel("Grado $k$")
        ax_deg.set_ylabel("$P(k)$")
        ax_deg.set_title(f"Distribución de grado", fontsize=12)

        # Estadísticas
        k_mean = np.mean(degrees)
        k_max = np.max(degrees)
        ax_deg.text(0.95, 0.95, f"⟨k⟩ = {k_mean:.1f}\nk_max = {k_max}",
                    transform=ax_deg.transAxes, ha="right", va="top",
                    fontsize=10, bbox=dict(boxstyle="round,pad=0.4",
                                           facecolor="white", alpha=0.8))

    fig.suptitle("Comparación de Topologías de Red", fontsize=16,
                 fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


def tabla_comparacion_topologias(redes_dict):
    """
    Tabla comparativa de métricas clave para diferentes topologías.

    Parameters
    ----------
    redes_dict : dict
        {nombre: nx.Graph}

    Returns
    -------
    pd.DataFrame
    """
    filas = []
    for nombre, G in redes_dict.items():
        degrees = [d for _, d in G.degree()]
        # Componentes conectados
        if nx.is_connected(G):
            avg_path = round(nx.average_shortest_path_length(G), 3)
        else:
            largest_cc = max(nx.connected_components(G), key=len)
            H = G.subgraph(largest_cc)
            avg_path = round(nx.average_shortest_path_length(H), 3)

        filas.append({
            "Topología": nombre,
            "Nodos": G.number_of_nodes(),
            "Aristas": G.number_of_edges(),
            "⟨k⟩ Grado medio": round(np.mean(degrees), 2),
            "k_max": max(degrees),
            "Clustering": round(nx.average_clustering(G), 4),
            "Camino medio": avg_path,
            "Componentes": nx.number_connected_components(G),
        })

    return pd.DataFrame(filas).set_index("Topología")


# ─────────────────────────────────────────────────────────────────────
# ANÁLISIS DE RESILIENCIA
# ─────────────────────────────────────────────────────────────────────

def test_resiliencia(G, tipo_ataque="aleatorio", fracciones=None, seed=42):
    """
    Elimina nodos progresivamente y mide el tamaño del componente
    gigante como fracción del original.

    Parameters
    ----------
    G : nx.Graph
    tipo_ataque : str
        'aleatorio': nodos al azar.
        'dirigido_grado': nodos con mayor grado primero.
        'dirigido_betweenness': nodos con mayor betweenness primero.
    fracciones : array-like, optional
        Fracciones de nodos a remover. Default: np.arange(0, 0.81, 0.05).
    seed : int

    Returns
    -------
    pd.DataFrame
        Columnas: 'fraccion_removida', 'componente_gigante'
    """
    rng = np.random.default_rng(seed)

    if fracciones is None:
        fracciones = np.arange(0, 0.81, 0.05)

    n_total = G.number_of_nodes()

    # Determinar orden de eliminación
    if tipo_ataque == "aleatorio":
        orden = list(G.nodes())
        rng.shuffle(orden)
    elif tipo_ataque == "dirigido_grado":
        orden = sorted(G.nodes(), key=lambda n: G.degree(n), reverse=True)
    elif tipo_ataque == "dirigido_betweenness":
        bc = nx.betweenness_centrality(G)
        orden = sorted(G.nodes(), key=lambda n: bc[n], reverse=True)
    else:
        raise ValueError(f"tipo_ataque no reconocido: {tipo_ataque}")

    resultados = []
    G_work = G.copy()

    nodos_removidos = 0
    idx_fraccion = 0

    for nodo in orden:
        # Registrar estado en cada fracción objetivo
        while idx_fraccion < len(fracciones):
            f_target = fracciones[idx_fraccion]
            f_actual = nodos_removidos / n_total

            if f_actual >= f_target - 1e-9:
                # Calcular componente gigante
                if G_work.number_of_nodes() > 0:
                    giant = max(len(c) for c in nx.connected_components(G_work))
                    resultados.append({
                        "fraccion_removida": round(f_target, 3),
                        "componente_gigante": giant / n_total,
                    })
                else:
                    resultados.append({
                        "fraccion_removida": round(f_target, 3),
                        "componente_gigante": 0.0,
                    })
                idx_fraccion += 1
            else:
                break

        if idx_fraccion >= len(fracciones):
            break

        # Remover el nodo
        if nodo in G_work:
            G_work.remove_node(nodo)
            nodos_removidos += 1

    # Registrar cualquier fracción restante
    while idx_fraccion < len(fracciones):
        f_target = fracciones[idx_fraccion]
        if G_work.number_of_nodes() > 0:
            giant = max(len(c) for c in nx.connected_components(G_work))
            resultados.append({
                "fraccion_removida": round(f_target, 3),
                "componente_gigante": giant / n_total,
            })
        else:
            resultados.append({
                "fraccion_removida": round(f_target, 3),
                "componente_gigante": 0.0,
            })
        idx_fraccion += 1

    return pd.DataFrame(resultados)


def comparar_resiliencia(G, fracciones=None, seed=42):
    """
    Ejecuta ataques aleatorio vs dirigido (por grado) y genera
    una gráfica comparativa del tamaño del componente gigante.

    Parameters
    ----------
    G : nx.Graph
    fracciones : array-like, optional
    seed : int

    Returns
    -------
    matplotlib.figure.Figure
    """
    df_random = test_resiliencia(G, "aleatorio", fracciones, seed)
    df_grado = test_resiliencia(G, "dirigido_grado", fracciones, seed)
    df_betw = test_resiliencia(G, "dirigido_betweenness", fracciones, seed)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(df_random["fraccion_removida"], df_random["componente_gigante"],
            "o-", color=viz.COLORS["primary"], linewidth=2, markersize=6,
            label="Aleatorio", alpha=0.8)
    ax.plot(df_grado["fraccion_removida"], df_grado["componente_gigante"],
            "s-", color=viz.COLORS["danger"], linewidth=2, markersize=6,
            label="Dirigido (grado)", alpha=0.8)
    ax.plot(df_betw["fraccion_removida"], df_betw["componente_gigante"],
            "^-", color=viz.COLORS["warning"], linewidth=2, markersize=6,
            label="Dirigido (betweenness)", alpha=0.8)

    ax.set_xlabel("Fracción de nodos removidos")
    ax.set_ylabel("Tamaño componente gigante (fracción)")
    ax.set_title("Resiliencia: Ataque aleatorio vs. dirigido",
                 fontsize=14, fontweight="bold")
    ax.legend(loc="upper right", fontsize=11)
    ax.set_xlim(0, fracciones[-1] if fracciones is not None else 0.8)
    ax.set_ylim(-0.05, 1.05)

    # Línea de referencia
    ax.axhline(y=0.5, color="#94A3B8", linestyle="--", alpha=0.5)
    ax.text(0.02, 0.52, "50% de la red", fontsize=9, color="#64748B")

    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────
# SIMULACIÓN DE CASCADA (MOTTER-LAI)
# ─────────────────────────────────────────────────────────────────────

def simular_cascada(G, nodo_inicial, alpha=0.2, max_pasos=20):
    """
    Simulación de cascada tipo Motter-Lai.

    Modelo:
    - Carga de cada nodo = betweenness centrality.
    - Capacidad = (1 + alpha) * carga_inicial.
    - Cuando un nodo falla, la carga se redistribuye.
    - Si la nueva carga supera la capacidad, el nodo falla.

    Parameters
    ----------
    G : nx.Graph
    nodo_inicial : hashable
        Nodo que falla inicialmente.
    alpha : float
        Margen de tolerancia (0 = sin margen, 1 = 100% extra).
    max_pasos : int
        Máximo número de pasos de propagación.

    Returns
    -------
    list of dict
        [{step, failed_nodes, total_failed, active_nodes}]
    """
    G_work = G.copy()

    # Carga inicial = betweenness
    carga_inicial = nx.betweenness_centrality(G_work)

    # Capacidad = (1 + alpha) * carga_inicial
    capacidad = {v: (1 + alpha) * carga_inicial[v] for v in G_work}

    historial = []

    # Paso 0: falla del nodo inicial
    fallados_acumulados = {nodo_inicial}
    G_work.remove_node(nodo_inicial)

    historial.append({
        "step": 0,
        "failed_nodes": {nodo_inicial},
        "total_failed": 1,
        "active_nodes": G_work.number_of_nodes(),
    })

    # Pasos siguientes
    for paso in range(1, max_pasos + 1):
        if G_work.number_of_nodes() == 0:
            break

        # Recalcular carga después de las fallas
        carga_actual = nx.betweenness_centrality(G_work)

        # Detectar nodos sobrecargados
        nuevos_fallados = set()
        for v in list(G_work.nodes()):
            if carga_actual.get(v, 0) > capacidad.get(v, 0):
                nuevos_fallados.add(v)

        if not nuevos_fallados:
            break  # Cascada se detiene

        # Remover nodos sobrecargados
        fallados_acumulados |= nuevos_fallados
        for v in nuevos_fallados:
            G_work.remove_node(v)

        historial.append({
            "step": paso,
            "failed_nodes": nuevos_fallados,
            "total_failed": len(fallados_acumulados),
            "active_nodes": G_work.number_of_nodes(),
        })

    return historial


def plot_cascada_pasos(G, cascada_resultado, layout=None):
    """
    Genera una figura multi-panel mostrando la progresión de la cascada.

    Parameters
    ----------
    G : nx.Graph
        Grafo original (antes de la cascada).
    cascada_resultado : list of dict
        Resultado de simular_cascada().
    layout : dict, optional
        Posiciones de los nodos. Si None, se calcula spring_layout.

    Returns
    -------
    matplotlib.figure.Figure
    """
    if layout is None:
        layout = nx.spring_layout(G, seed=42, k=1.5 / np.sqrt(len(G)))

    n_pasos = len(cascada_resultado)
    n_cols = min(n_pasos, 4)
    n_rows = (n_pasos + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols,
                              figsize=(5 * n_cols, 5 * n_rows))

    if n_pasos == 1:
        axes = np.array([[axes]])
    elif n_rows == 1:
        axes = axes.reshape(1, -1)
    elif n_cols == 1:
        axes = axes.reshape(-1, 1)

    # Acumular todos los nodos fallados hasta cada paso
    fallados_hasta_paso = set()

    for idx, paso_info in enumerate(cascada_resultado):
        row, col = divmod(idx, n_cols)
        ax = axes[row, col]

        fallados_hasta_paso |= paso_info["failed_nodes"]

        viz.plot_cascade_step(
            G, layout, fallados_hasta_paso,
            step=paso_info["step"], ax=ax,
            title=f"Paso {paso_info['step']}: "
                  f"{paso_info['total_failed']} fallas totales"
        )

    # Ocultar axes sobrantes
    for idx in range(n_pasos, n_rows * n_cols):
        row, col = divmod(idx, n_cols)
        axes[row, col].axis("off")

    fig.suptitle("Propagación de la cascada (Motter-Lai)",
                 fontsize=16, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────
# MATRIZ DE ADYACENCIA
# ─────────────────────────────────────────────────────────────────────

def mostrar_matriz_adyacencia(G, ax=None):
    """
    Muestra la matriz de adyacencia del grafo como heatmap.

    Parameters
    ----------
    G : nx.Graph
    ax : matplotlib.axes.Axes, optional

    Returns
    -------
    matplotlib.axes.Axes
    """
    A = nx.to_numpy_array(G)
    nodos = list(G.nodes())

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 7))

    im = ax.imshow(A, cmap="Blues", interpolation="none", aspect="equal")
    ax.set_xticks(range(len(nodos)))
    ax.set_yticks(range(len(nodos)))

    if len(nodos) <= 20:
        ax.set_xticklabels(nodos, rotation=45, ha="right", fontsize=9)
        ax.set_yticklabels(nodos, fontsize=9)
    else:
        ax.set_xticklabels([])
        ax.set_yticklabels([])

    ax.set_title("Matriz de Adyacencia", fontsize=14, fontweight="bold")

    # Colorbar
    plt.colorbar(im, ax=ax, shrink=0.8, label="Conexión")

    # Agregar valores en celdas para redes pequeñas
    if len(nodos) <= 12:
        for i in range(len(nodos)):
            for j in range(len(nodos)):
                val = int(A[i, j])
                color = "white" if val == 1 else "#94A3B8"
                ax.text(j, i, str(val), ha="center", va="center",
                        fontsize=10, color=color, fontweight="bold")

    return ax


# ─────────────────────────────────────────────────────────────────────
# DISTRIBUCIÓN DE GRADO (LOG-LOG)
# ─────────────────────────────────────────────────────────────────────

def plot_grado_loglog(G, ax=None, color=None, label=None):
    """
    Distribución de grado en escala log-log para detectar
    leyes de potencia.

    Parameters
    ----------
    G : nx.Graph
    ax : matplotlib.axes.Axes, optional
    color : str, optional
    label : str, optional

    Returns
    -------
    matplotlib.axes.Axes
    """
    degrees = [d for _, d in G.degree()]
    unique_k, counts = np.unique(degrees, return_counts=True)
    probs = counts / counts.sum()

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))

    c = color or viz.COLORS["primary"]

    ax.scatter(unique_k, probs, color=c, s=60, alpha=0.7,
               label=label, edgecolors="white", linewidths=0.8,
               zorder=3)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Grado $k$ (escala log)")
    ax.set_ylabel("$P(k)$ (escala log)")
    ax.set_title("Distribución de grado (log-log)", fontsize=14,
                 fontweight="bold")

    if label:
        ax.legend()

    ax.grid(True, which="both", alpha=0.3, linewidth=0.5)

    return ax
