"""
saga.py — Utilidades para la Saga Colombia (DSS del Sistema Eléctrico)

Funciones de persistencia, resumen ejecutivo y dashboard unificado
para la serie de notebooks aplicados del proyecto integrador.
"""
import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mise_utils import viz

# Directorio de persistencia (relativo al notebook)
_SAGA_DIR = os.path.join(os.path.dirname(__file__), '..', '.saga_state')


def save_state(state_dict, nombre='saga'):
    """Persiste el estado acumulado de la saga como pickle."""
    os.makedirs(_SAGA_DIR, exist_ok=True)
    path = os.path.join(_SAGA_DIR, f'{nombre}.pkl')
    with open(path, 'wb') as f:
        pickle.dump(state_dict, f)
    print(f"  Estado guardado: {path}")
    return path


def load_state(nombre='saga'):
    """Carga el estado acumulado de la saga."""
    path = os.path.join(_SAGA_DIR, f'{nombre}.pkl')
    if not os.path.exists(path):
        print(f"  No se encontro estado previo ({nombre}). Iniciando vacio.")
        return {}
    try:
        with open(path, 'rb') as f:
            state = pickle.load(f)
        capas = [k for k in state.keys()]
        print(f"  Estado cargado: {path} ({len(capas)} capas: {capas})")
        return state
    except Exception as e:
        print(f"  Advertencia: no se pudo cargar {path} ({e}). Iniciando vacio.")
        return {}


def tabla_resumen_ejecutivo(state):
    """
    Genera tabla-resumen de hallazgos clave de cada capa de la saga.

    Returns
    -------
    pd.DataFrame con columnas: Capa, Hallazgo Principal, Indicador Clave, Alerta
    """
    filas = []

    if 'identidad' in state:
        s = state['identidad']
        filas.append({
            'Capa': 'Identidad del Sistema',
            'Hallazgo': s.get('hallazgo', 'SIN con 10+ generadores, 4 transmisores, mercado desintegrado verticalmente'),
            'Indicador': s.get('indicador', f"{s.get('n_generadores', '?')} generadores, {s.get('capacidad_total_MW', '?')} MW"),
            'Alerta': s.get('alerta', 'Concentracion en top 3 generadores'),
        })

    if 'red_fisica' in state:
        s = state['red_fisica']
        filas.append({
            'Capa': 'Red Fisica (STN)',
            'Hallazgo': s.get('hallazgo', 'Red con nodos criticos de alta betweenness'),
            'Indicador': s.get('indicador', f"N-1 criticos: {s.get('n1_criticos', '?')}"),
            'Alerta': s.get('alerta', 'Vulnerabilidad a ataque dirigido'),
        })

    if 'red_social' in state:
        s = state['red_social']
        filas.append({
            'Capa': 'Red Social y Mercado',
            'Hallazgo': s.get('hallazgo', 'Mercado con comunidades detectables'),
            'Indicador': s.get('indicador', f"Comunidades: {s.get('n_comunidades', '?')}"),
            'Alerta': s.get('alerta', 'Concentracion de mercado'),
        })

    if 'dinamica' in state:
        s = state['dinamica']
        filas.append({
            'Capa': 'Dinamica del Sistema',
            'Hallazgo': s.get('hallazgo', 'Oscilaciones endogenas por retardo constructor'),
            'Indicador': s.get('indicador', f"Periodo: ~{s.get('periodo_oscilacion', '?')} anos"),
            'Alerta': s.get('alerta', 'Ciclo precio-capacidad persistente'),
        })

    if 'politica' in state:
        s = state['politica']
        filas.append({
            'Capa': 'Politica y Escenarios',
            'Hallazgo': s.get('hallazgo', 'Estrategia robusta identificada'),
            'Indicador': s.get('indicador', f"Estrategia: {s.get('estrategia_robusta', '?')}"),
            'Alerta': s.get('alerta', 'Lock-in termico bajo CxC'),
        })

    if 'gobernanza' in state:
        s = state['gobernanza']
        filas.append({
            'Capa': 'Gobernanza y Justicia',
            'Hallazgo': s.get('hallazgo', 'Dimensiones fuera del modelo cuantitativo'),
            'Indicador': s.get('indicador', 'Ostrom + Sovacool'),
            'Alerta': s.get('alerta', 'Consulta previa como dinamica sistemica'),
        })

    if not filas:
        return pd.DataFrame(columns=['Capa', 'Hallazgo', 'Indicador', 'Alerta'])

    return pd.DataFrame(filas)


def dashboard_dss(state, titulo='DSS del Sistema Electrico Colombiano'):
    """
    Dashboard unificado de 6 paneles (uno por capa de la saga).
    Usa los artefactos guardados en cada saga para producir
    una vista ejecutiva integrada.
    """
    n_capas = min(6, len([k for k in state.keys()
                          if k in ('identidad', 'red_fisica', 'red_social',
                                   'dinamica', 'politica', 'gobernanza')]))
    if n_capas == 0:
        print("No hay capas en el estado. Ejecute al menos una saga.")
        return None

    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle(titulo, fontsize=18, fontweight='bold', y=0.98)

    panel_map = {
        'identidad': (0, 0),
        'red_fisica': (0, 1),
        'red_social': (0, 2),
        'dinamica': (1, 0),
        'politica': (1, 1),
        'gobernanza': (1, 2),
    }

    titulos_panel = {
        'identidad': 'Identidad del Sistema',
        'red_fisica': 'Estructura Fisica (STN)',
        'red_social': 'Estructura Social',
        'dinamica': 'Dinamica Temporal',
        'politica': 'Politica y Robustez',
        'gobernanza': 'Gobernanza',
    }

    def _panel_texto(ax, s):
        """Panel fallback: muestra hallazgo, indicador y alerta."""
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        # Hallazgo
        hallazgo = s.get('hallazgo', 'Analisis completo')
        ax.text(0.5, 0.75, hallazgo, ha='center', va='center',
                fontsize=9, fontweight='bold', wrap=True,
                transform=ax.transAxes)
        # Indicador
        indicador = s.get('indicador', '')
        if indicador:
            ax.text(0.5, 0.45, indicador, ha='center', va='center',
                    fontsize=10, color=viz.COLORS['primary'],
                    fontweight='bold', transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor=viz.COLORS['primary'], alpha=0.1))
        # Alerta
        alerta = s.get('alerta', '')
        if alerta:
            ax.text(0.5, 0.18, f"ALERTA: {alerta}", ha='center', va='center',
                    fontsize=8, color=viz.COLORS['danger'], style='italic',
                    wrap=True, transform=ax.transAxes)

    for capa, (row, col) in panel_map.items():
        ax = axes[row, col]
        ax.set_title(titulos_panel[capa], fontweight='bold', fontsize=12)

        if capa not in state:
            ax.text(0.5, 0.5, 'Pendiente', ha='center', va='center',
                    fontsize=14, color='gray', alpha=0.5,
                    transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
            continue

        s = state[capa]
        plotted = False

        # Panel: Identidad — timeline regulatorio
        if capa == 'identidad' and 'timeline_df' in s:
            df = s['timeline_df']
            n = min(len(df), 12)
            colors_t = [viz.COLORS['primary']] * n
            ax.barh(range(n), df['año'].values[:n], color=colors_t, alpha=0.7)
            ax.set_yticks(range(n))
            ax.set_yticklabels(df['norma'].values[:n], fontsize=7)
            ax.set_xlabel('Hitos regulatorios')
            plotted = True

        # Panel: Red fisica — betweenness ranking
        elif capa == 'red_fisica' and 'metricas_top' in s:
            df = s['metricas_top']
            if 'betweenness' in df.columns:
                top = df.head(10)
                ax.barh(range(len(top)), top['betweenness'].values,
                        color=viz.COLORS['danger'], alpha=0.7)
                ax.set_yticks(range(len(top)))
                ax.set_yticklabels(top.index, fontsize=7)
                ax.set_xlabel('Betweenness Centrality')
                ax.invert_yaxis()
                plotted = True

        # Panel: Red social — HHI gauge
        elif capa == 'red_social' and 'hhi' in s:
            hhi = s['hhi']
            # Simple gauge via horizontal bar
            ax.barh(['HHI'], [hhi], color=viz.COLORS['warning'], alpha=0.7, height=0.4)
            ax.axvline(x=1500, color='orange', linestyle='--', alpha=0.6, label='Moderado')
            ax.axvline(x=2500, color=viz.COLORS['danger'], linestyle='--', alpha=0.6, label='Concentrado')
            ax.set_xlim(0, max(4000, hhi * 1.2))
            ax.legend(fontsize=8)
            ax.set_xlabel('Indice Herfindahl-Hirschman')
            # Add context text
            if hhi < 1500:
                nivel = 'Competitivo'
            elif hhi < 2500:
                nivel = 'Moderadamente concentrado'
            else:
                nivel = 'Altamente concentrado'
            ax.text(hhi + 50, 0, f'{hhi:.0f} ({nivel})',
                    va='center', fontsize=9, fontweight='bold')
            plotted = True

        # Panel: Dinamica — capacidad vs demanda
        elif capa == 'dinamica' and 'df_ciclo' in s:
            df = s['df_ciclo']
            col_cap = ('capacidad_total_efectiva_MW'
                       if 'capacidad_total_efectiva_MW' in df.columns
                       else 'capacidad_MW')
            ax.plot(df['año'], df[col_cap], color=viz.COLORS['primary'],
                    linewidth=1.5, label='Capacidad')
            ax.plot(df['año'], df['demanda_MW'], color=viz.COLORS['danger'],
                    linewidth=1.5, linestyle='--', label='Demanda')
            ax.set_xlabel('Ano')
            ax.set_ylabel('MW')
            ax.legend(fontsize=8)
            plotted = True

        # Panel: Politica — heatmap de robustez
        elif capa == 'politica' and 'tabla_robustez' in s:
            tbl = s['tabla_robustez']
            try:
                data_rows = tbl.drop(index=['MAX REGRET', 'RANKING'], errors='ignore')
                im = ax.imshow(data_rows.values.astype(float),
                               cmap='RdYlGn_r', aspect='auto')
                ax.set_xticks(range(len(data_rows.columns)))
                ax.set_xticklabels(data_rows.columns, fontsize=7, rotation=45)
                ax.set_yticks(range(len(data_rows)))
                ax.set_yticklabels(data_rows.index, fontsize=7)
                plotted = True
            except Exception:
                pass

        # Fallback: texto ejecutivo formateado
        if not plotted:
            _panel_texto(ax, s)

    plt.tight_layout()
    return fig


def export_report(state, titulo='Informe de Consultoria Sistemica'):
    """
    Genera un informe en formato markdown a partir del estado de la saga.

    Returns
    -------
    str : texto markdown del informe
    """
    lines = [f'# {titulo}\n']
    lines.append(f'## Resumen Ejecutivo\n')

    tabla = tabla_resumen_ejecutivo(state)
    if len(tabla) > 0:
        lines.append(tabla.to_markdown(index=False))
        lines.append('\n')

    capas_orden = ['identidad', 'red_fisica', 'red_social',
                   'dinamica', 'politica', 'gobernanza']
    titulos = {
        'identidad': 'Identidad del Sistema',
        'red_fisica': 'Analisis de Red Fisica',
        'red_social': 'Analisis de Red Social y Mercado',
        'dinamica': 'Dinamica del Sistema',
        'politica': 'Analisis de Politica y Escenarios',
        'gobernanza': 'Gobernanza y Justicia Energetica',
    }

    for capa in capas_orden:
        if capa not in state:
            continue
        s = state[capa]
        lines.append(f'\n## {titulos[capa]}\n')
        lines.append(f"**Hallazgo principal:** {s.get('hallazgo', 'N/A')}\n")
        lines.append(f"**Indicador clave:** {s.get('indicador', 'N/A')}\n")
        lines.append(f"**Alerta:** {s.get('alerta', 'N/A')}\n")

        if 'narrativa' in s:
            lines.append(f"\n{s['narrativa']}\n")

    lines.append('\n## Limitaciones\n')
    lines.append('- Modelo SD con supuestos agregados (no resuelve flujo de potencia AC)\n')
    lines.append('- Datos sinteticos pedagogicos (consultar XM/UPME para datos operacionales)\n')
    lines.append('- Dimension social capturada cualitativamente\n')

    return '\n'.join(lines)
