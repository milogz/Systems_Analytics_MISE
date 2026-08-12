"""
Visualización compartida — MISE Systems Analytics
===================================================
Estilos, paletas de colores y funciones de visualización reutilizables
para todos los notebooks del curso.
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# ─────────────────────────────────────────────────────────────────────
# PALETA DE COLORES DEL CURSO
# ─────────────────────────────────────────────────────────────────────

COLORS = {
    # Colores principales
    "primary":     "#2563EB",   # Azul MISE
    "secondary":   "#7C3AED",   # Púrpura
    "accent":      "#F59E0B",   # Ámbar
    "success":     "#10B981",   # Verde
    "danger":      "#EF4444",   # Rojo
    "warning":     "#F97316",   # Naranja

    # Colores de estado para redes
    "node_default":   "#94A3B8",  # Gris azulado
    "node_active":    "#EF4444",  # Rojo (falla, contagio)
    "node_adopted":   "#10B981",  # Verde (adoptado)
    "node_hub":       "#F59E0B",  # Ámbar (hub/crítico)
    "edge_default":   "#CBD5E1",  # Gris claro
    "edge_active":    "#EF4444",  # Rojo

    # Colores para topologías
    "erdos_renyi":    "#3B82F6",  # Azul
    "barabasi_albert":"#EF4444",  # Rojo
    "watts_strogatz": "#10B981",  # Verde

    # Colores para niveles del notebook
    "level_1":  "#3B82F6",  # Azul — intuición
    "level_2":  "#F59E0B",  # Ámbar — energía
    "level_3":  "#7C3AED",  # Púrpura — profesional
}

# Colormaps
CMAP_HEAT = plt.cm.YlOrRd      # Para métricas de centralidad
CMAP_DIVERGING = plt.cm.RdYlBu  # Para comparaciones
CMAP_SEQUENTIAL = plt.cm.Blues   # Para intensidades


# ─────────────────────────────────────────────────────────────────────
# ESTILOS GLOBALES
# ─────────────────────────────────────────────────────────────────────

def apply_mise_style():
    """Aplica el estilo visual del curso a todos los gráficos."""
    plt.rcParams.update({
        # Fuentes
        "font.family": "sans-serif",
        "font.sans-serif": ["Inter", "Segoe UI", "Helvetica", "Arial"],
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,

        # Colores
        "axes.facecolor": "#FAFAFA",
        "figure.facecolor": "white",
        "axes.edgecolor": "#E2E8F0",
        "axes.grid": True,
        "grid.color": "#E2E8F0",
        "grid.alpha": 0.5,
        "grid.linewidth": 0.5,

        # Líneas
        "lines.linewidth": 2.0,
        "lines.markersize": 6,

        # Figuras
        "figure.figsize": (10, 6),
        "figure.dpi": 100,
        "savefig.dpi": 150,
        "savefig.bbox": "tight",

        # Leyenda
        "legend.framealpha": 0.9,
        "legend.edgecolor": "#E2E8F0",
        "legend.fontsize": 10,
    })


# ─────────────────────────────────────────────────────────────────────
# FUNCIONES DE VISUALIZACIÓN DE REDES
# ─────────────────────────────────────────────────────────────────────

def plot_network(G, metric_values=None, metric_name="Métrica",
                 node_size_factor=300, layout=None, ax=None,
                 show_labels=True, title=None, cmap=None,
                 highlight_nodes=None, highlight_color=None):
    """
    Dibuja una red con nodos coloreados por una métrica.

    Parameters
    ----------
    G : networkx.Graph
    metric_values : dict, optional
        {nodo: valor} para colorear nodos. Si None, todos del mismo color.
    metric_name : str
        Nombre de la métrica para la barra de color.
    node_size_factor : float
        Factor de escalamiento del tamaño de los nodos.
    layout : dict, optional
        Posiciones {nodo: (x, y)}. Si None, se usa spring_layout.
    ax : matplotlib.axes.Axes, optional
    show_labels : bool
    title : str, optional
    cmap : colormap, optional
    highlight_nodes : list, optional
        Nodos a resaltar con un borde especial.
    highlight_color : str, optional
    """
    import networkx as nx

    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    if layout is None:
        layout = nx.spring_layout(G, seed=42, k=1.5/np.sqrt(len(G)))

    if cmap is None:
        cmap = CMAP_HEAT

    # Nodos
    if metric_values is not None:
        node_list = list(G.nodes())
        values = [metric_values.get(n, 0) for n in node_list]
        node_sizes = [node_size_factor * (1 + 3 * v / max(values)) if max(values) > 0
                      else node_size_factor for v in values]

        nodes = nx.draw_networkx_nodes(
            G, layout, nodelist=node_list,
            node_color=values, cmap=cmap,
            node_size=node_sizes, ax=ax,
            edgecolors="#334155", linewidths=1.0
        )
        plt.colorbar(nodes, ax=ax, label=metric_name, shrink=0.8)
    else:
        nx.draw_networkx_nodes(
            G, layout, node_color=COLORS["primary"],
            node_size=node_size_factor, ax=ax,
            edgecolors="#334155", linewidths=1.0
        )

    # Resaltar nodos específicos
    if highlight_nodes:
        hc = highlight_color or COLORS["danger"]
        nx.draw_networkx_nodes(
            G, layout, nodelist=highlight_nodes,
            node_color=hc, node_size=node_size_factor * 1.5,
            ax=ax, edgecolors="#1E293B", linewidths=2.5
        )

    # Aristas
    nx.draw_networkx_edges(
        G, layout, edge_color=COLORS["edge_default"],
        width=1.0, alpha=0.6, ax=ax
    )

    # Etiquetas
    if show_labels:
        nx.draw_networkx_labels(
            G, layout, font_size=9, font_weight="bold",
            font_color="#1E293B", ax=ax
        )

    if title:
        ax.set_title(title, fontsize=14, fontweight="bold", pad=15)

    ax.axis("off")
    return ax


def plot_degree_distribution(G, ax=None, log_log=False, label=None,
                              color=None, title=None):
    """
    Dibuja la distribución de grado de una red.

    Parameters
    ----------
    G : networkx.Graph
    ax : matplotlib.axes.Axes, optional
    log_log : bool
        Si True, escala log-log para detectar leyes de potencia.
    label : str, optional
    color : str, optional
    title : str, optional
    """
    degrees = [d for _, d in G.degree()]
    unique, counts = np.unique(degrees, return_counts=True)
    probs = counts / counts.sum()

    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    c = color or COLORS["primary"]

    if log_log:
        ax.scatter(unique, probs, color=c, s=50, alpha=0.7,
                   label=label, edgecolors="white", linewidths=0.5)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("Grado $k$ (escala log)")
        ax.set_ylabel("$P(k)$ (escala log)")
    else:
        ax.bar(unique, probs, color=c, alpha=0.7, label=label,
               edgecolor="white", linewidth=0.5)
        ax.set_xlabel("Grado $k$")
        ax.set_ylabel("$P(k)$")

    if title:
        ax.set_title(title)
    if label:
        ax.legend()

    return ax


def plot_cascade_step(G, layout, failed_nodes, step, ax=None, title=None):
    """
    Dibuja el estado de una red durante una simulación de cascada.
    Nodos fallados se muestran en rojo; operativos en azul.
    """
    import networkx as nx

    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    active = [n for n in G.nodes() if n not in failed_nodes]

    # Aristas
    nx.draw_networkx_edges(G, layout, edge_color=COLORS["edge_default"],
                           width=0.8, alpha=0.4, ax=ax)

    # Nodos activos
    if active:
        nx.draw_networkx_nodes(G, layout, nodelist=active,
                               node_color=COLORS["primary"],
                               node_size=200, ax=ax,
                               edgecolors="#334155", linewidths=0.8)

    # Nodos fallados
    if failed_nodes:
        nx.draw_networkx_nodes(G, layout, nodelist=list(failed_nodes),
                               node_color=COLORS["danger"],
                               node_size=250, ax=ax,
                               edgecolors="#7F1D1D", linewidths=1.5)

    t = title or f"Paso {step}: {len(failed_nodes)} nodos fallados"
    ax.set_title(t, fontsize=12, fontweight="bold")
    ax.axis("off")
    return ax


# ─────────────────────────────────────────────────────────────────────
# FUNCIONES DE VISUALIZACIÓN DE SERIES DE TIEMPO
# ─────────────────────────────────────────────────────────────────────

def plot_time_series(t, y, xlabel="Tiempo", ylabel="Valor",
                     title=None, label=None, color=None, ax=None,
                     fill_between=False):
    """Dibuja una serie de tiempo con estilo MISE."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    c = color or COLORS["primary"]
    ax.plot(t, y, color=c, linewidth=2, label=label)

    if fill_between:
        ax.fill_between(t, 0, y, color=c, alpha=0.1)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    if label:
        ax.legend()

    return ax


def comparison_histograms(data_dict, xlabel="Valor", ylabel="Frecuencia",
                           title=None, bins=50, density=True, ax=None):
    """
    Compara histogramas de múltiples distribuciones.

    Parameters
    ----------
    data_dict : dict
        {nombre: array_de_datos}
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    colors = list(COLORS.values())
    for i, (name, data) in enumerate(data_dict.items()):
        ax.hist(data, bins=bins, density=density, alpha=0.5,
                color=colors[i % len(colors)], label=name,
                edgecolor="white", linewidth=0.5)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    ax.legend()
    return ax


# ─────────────────────────────────────────────────────────────────────
# WIDGETS Y DASHBOARDS
# ─────────────────────────────────────────────────────────────────────

def create_slider(description, min_val, max_val, step, value=None,
                  continuous_update=False):
    """Crea un slider con estilo consistente."""
    try:
        import ipywidgets as widgets
        return widgets.FloatSlider(
            value=value or (min_val + max_val) / 2,
            min=min_val, max=max_val, step=step,
            description=description,
            continuous_update=continuous_update,
            style={"description_width": "initial"},
            layout=widgets.Layout(width="500px")
        )
    except ImportError:
        print("[WARN] ipywidgets no disponible. Instale con: pip install ipywidgets")
        return None


def create_dropdown(description, options, value=None):
    """Crea un dropdown con estilo consistente."""
    try:
        import ipywidgets as widgets
        return widgets.Dropdown(
            options=options,
            value=value or options[0],
            description=description,
            style={"description_width": "initial"},
            layout=widgets.Layout(width="400px")
        )
    except ImportError:
        print("[WARN] ipywidgets no disponible.")
        return None


# ─────────────────────────────────────────────────────────────────────
# HELPERS DE FORMATO
# ─────────────────────────────────────────────────────────────────────

def section_header(level, title, emoji=""):
    """Imprime un encabezado de sección formateado."""
    if level == 1:
        print(f"\n{'='*60}")
        print(f"  {emoji} {title}")
        print(f"{'='*60}\n")
    elif level == 2:
        print(f"\n{'─'*50}")
        print(f"  {emoji} {title}")
        print(f"{'─'*50}\n")
    else:
        print(f"\n  {emoji} {title}")
        print(f"  {'·'*40}\n")


def metrics_table(data_dict, title=None):
    """
    Imprime una tabla formateada de métricas.

    Parameters
    ----------
    data_dict : dict
        {nombre_columna: {fila: valor}}
    """
    try:
        import pandas as pd
        df = pd.DataFrame(data_dict)
        if title:
            print(f"\n   {title}")
            print(f"  {'─'*40}")
        print(df.to_string())
        return df
    except ImportError:
        for key, values in data_dict.items():
            print(f"\n{key}:")
            for k, v in values.items():
                print(f"  {k}: {v}")


# Aplicar estilo al importar
apply_mise_style()
