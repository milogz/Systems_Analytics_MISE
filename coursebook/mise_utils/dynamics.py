"""
Soporte para Semanas 4-5: Dinámica de Sistemas — MISE Systems Analytics
=========================================================================
Infraestructura para construir, simular y analizar modelos de dinámica
de sistemas (System Dynamics) usando Python y scipy.

Filosofía: el estudiante define stocks, flujos y parámetros con funciones
de alto nivel. La integración numérica y la visualización ocurren
automáticamente.

NOTA: Este módulo NO es un reemplazo de Vensim o Stella. Es una
implementación pedagógica diseñada para que los estudiantes entiendan
la mecánica subyacente de los modelos SD.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from . import viz


# ─────────────────────────────────────────────────────────────────────
# MODELOS SD PRE-CONSTRUIDOS (Nivel 1 — Intuición)
# ─────────────────────────────────────────────────────────────────────

def modelo_banera(flujo_entrada=5.0, flujo_salida=3.0, stock_inicial=50.0,
                  T=20, dt=0.1):
    """
    Modelo más simple: una bañera con flujo de entrada y salida constantes.
    dS/dt = flujo_entrada - flujo_salida

    Returns
    -------
    dict con 't', 'stock', 'flujo_entrada', 'flujo_salida'
    """
    def ode(t, y):
        return [flujo_entrada - flujo_salida]

    sol = solve_ivp(ode, [0, T], [stock_inicial],
                    t_eval=np.arange(0, T, dt), method='RK45')

    return {
        't': sol.t,
        'stock': sol.y[0],
        'flujo_entrada': np.full_like(sol.t, flujo_entrada),
        'flujo_salida': np.full_like(sol.t, flujo_salida)
    }


def modelo_crecimiento_exponencial(r=0.05, N0=100.0, T=50, dt=0.1):
    """
    Loop de refuerzo puro: dN/dt = r * N
    Demuestra crecimiento exponencial.

    Parameters
    ----------
    r : float — tasa de crecimiento
    N0 : float — población/stock inicial
    """
    def ode(t, y):
        return [r * y[0]]

    sol = solve_ivp(ode, [0, T], [N0],
                    t_eval=np.arange(0, T, dt), method='RK45')

    return {'t': sol.t, 'N': sol.y[0], 'r': r}


def modelo_busqueda_objetivo(k=0.1, objetivo=100.0, S0=10.0, T=50, dt=0.1):
    """
    Loop de balance: dS/dt = k * (objetivo - S)
    Demuestra convergencia asintótica al objetivo.

    Parameters
    ----------
    k : float — velocidad de ajuste
    objetivo : float — valor objetivo
    S0 : float — valor inicial
    """
    def ode(t, y):
        return [k * (objetivo - y[0])]

    sol = solve_ivp(ode, [0, T], [S0],
                    t_eval=np.arange(0, T, dt), method='RK45')

    return {'t': sol.t, 'S': sol.y[0], 'objetivo': objetivo}


def modelo_ducha(k=0.5, objetivo=38.0, delay=3.0, T0=20.0, T=60, dt=0.1):
    """
    Loop de balance CON retardo: demuestra oscilaciones.
    Modelo: ajustas la llave de la ducha, pero el agua tarda 'delay'
    segundos en cambiar de temperatura.

    dT/dt = k * (objetivo - T_percibida)
    T_percibida = T(t - delay)

    Implementación con buffer de historia.

    Parameters
    ----------
    k : float — sensibilidad del ajuste
    objetivo : float — temperatura deseada
    delay : float — retardo en segundos
    T0 : float — temperatura inicial del agua
    """
    n_steps = int(T / dt)
    t_arr = np.linspace(0, T, n_steps)
    temp = np.zeros(n_steps)
    temp[0] = T0

    delay_steps = max(1, int(delay / dt))

    for i in range(1, n_steps):
        # Temperatura percibida = la de hace 'delay' segundos
        idx_retardado = max(0, i - delay_steps)
        t_percibida = temp[idx_retardado]

        # Ajuste basado en la percepción retardada
        ajuste = k * (objetivo - t_percibida)
        temp[i] = temp[i-1] + ajuste * dt

    return {'t': t_arr, 'temperatura': temp, 'objetivo': objetivo, 'delay': delay}


def plot_modelo_ducha(delay=3.0, k=0.5, objetivo=38.0, T0=20.0, T=60, ax=None):
    """
    Simula y grafica el modelo de la ducha con retardo.
    Muestra cómo el retardo genera oscilaciones alrededor del objetivo.
    """
    resultado = modelo_ducha(k=k, objetivo=objetivo, delay=delay, T0=T0, T=T)
    
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(12, 5))
    
    ax.plot(resultado['t'], resultado['temperatura'],
            color=viz.COLORS['primary'], linewidth=2,
            label=f'Temperatura (retardo = {delay:.1f}s)')
    ax.axhline(y=objetivo, color=viz.COLORS['accent'], linestyle='--',
               linewidth=1.5, label=f'Objetivo: {objetivo}°C')
    
    # Zona de confort
    ax.axhspan(objetivo - 2, objetivo + 2, alpha=0.1,
               color=viz.COLORS['accent'], label='Zona de confort (±2°C)')
    
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Temperatura (°C)')
    ax.set_title(f'La ducha con retardo: oscilaciones por delay de {delay:.1f}s',
                 fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(max(0, T0 - 5), objetivo + 25)
    
    plt.tight_layout()
    return ax


def modelo_beer_game(delay_entrega=4, delay_percepcion=2, demanda_base=100,
                     n_periodos=50, seed=42):
    """
    Beer Game simplificado: cadena de suministro con 3 eslabones.
    Demuestra el efecto látigo (bullwhip effect).

    Cada eslabón: stock (inventario), flujo de pedidos, delay de entrega.

    Returns
    -------
    pd.DataFrame con inventarios y pedidos de cada eslabón por período.
    """
    rng = np.random.default_rng(seed)

    # Demanda del consumidor final (escalón + ruido)
    demanda = np.full(n_periodos, demanda_base, dtype=float)
    # Escalón en t=10: demanda sube 20%
    demanda[10:] = demanda_base * 1.2
    demanda += rng.normal(0, 5, n_periodos)

    nombres = ['Tienda', 'Distribuidor', 'Fábrica']
    n_eslabones = len(nombres)

    inventario = np.zeros((n_eslabones, n_periodos))
    pedidos = np.zeros((n_eslabones, n_periodos))
    entregas = np.zeros((n_eslabones, n_periodos))

    # Condiciones iniciales
    for e in range(n_eslabones):
        inventario[e, 0] = demanda_base * 2  # 2 semanas de inventario

    for t in range(1, n_periodos):
        for e in range(n_eslabones):
            # Demanda que recibe este eslabón
            if e == 0:
                demanda_recibida = demanda[t]
            else:
                demanda_recibida = pedidos[e-1, t-1] if t > 0 else demanda_base

            # Entrega (con delay)
            t_pedido = max(0, t - delay_entrega)
            if e < n_eslabones - 1:
                entregas[e, t] = pedidos[e, t_pedido] if t_pedido > 0 else demanda_base
            else:
                # Fábrica produce con delay
                entregas[e, t] = pedidos[e, t_pedido] if t_pedido > 0 else demanda_base

            # Actualizar inventario
            inventario[e, t] = inventario[e, t-1] + entregas[e, t] - demanda_recibida

            # Política de pedidos: pedir para cubrir gap + ajuste
            inventario_deseado = demanda_base * 2
            gap = inventario_deseado - inventario[e, t]

            # Percepción retardada de la demanda
            t_perc = max(0, t - delay_percepcion)
            demanda_percibida = demanda[t_perc] if e == 0 else pedidos[e-1, t_perc] if t_perc > 0 else demanda_base

            pedidos[e, t] = max(0, demanda_percibida + 0.3 * gap)

    return pd.DataFrame({
        't': range(n_periodos),
        'demanda_consumidor': demanda,
        **{f'inventario_{nombres[e]}': inventario[e] for e in range(n_eslabones)},
        **{f'pedidos_{nombres[e]}': pedidos[e] for e in range(n_eslabones)},
    })


# ─────────────────────────────────────────────────────────────────────
# MODELOS DE ENERGÍA (Nivel 2 — Sector eléctrico colombiano)
# ─────────────────────────────────────────────────────────────────────

# Parámetros por defecto calibrados para Colombia
PARAMS_COLOMBIA_BASE = {
    # Stocks iniciales (año ~2010)
    'capacidad_inicial': 14000,      # MW instalados
    'pipeline_inicial': 2000,        # MW en construcción
    'demanda_inicial': 9500,         # MW de demanda pico

    # Tasas
    'tasa_crecimiento_demanda': 0.025,  # 2.5% anual
    'vida_util': 30,                    # años promedio de una planta
    'delay_construccion': 4,            # años

    # Mercado
    'precio_base': 150,              # COP/kWh (precio de equilibrio)
    'k_precio': 5.0,                 # sensibilidad precio-gap (no-lineal)
    'precio_techo': 600,             # COP/kWh

    # Inversión
    'sensibilidad_inversion': 50,    # MW nuevos por COP/kWh de gap de precio
    'precio_umbral_inversion': 180,  # COP/kWh mínimo para invertir
    'inversion_maxima': 1500,        # MW/año máximo
}


def modelo_inversion_capacidad(params=None, T=30, dt=0.1):
    """
    Modelo SD del ciclo inversión-capacidad en generación eléctrica.

    3 stocks:
    - Capacidad_Instalada (MW)
    - Pipeline_Construcción (MW en construcción)
    - Demanda (MW pico)

    Flujos:
    - inicio_proyectos: f(precio, gap) — inversión responde al precio
    - puesta_servicio: pipeline / delay_construcción
    - retiro: capacidad / vida_útil
    - crecimiento_demanda: demanda * tasa

    Auxiliar:
    - gap = (demanda - capacidad) / demanda
    - precio = precio_base * exp(k * gap)  [no-lineal]

    Returns
    -------
    pd.DataFrame con todas las variables por paso de tiempo.
    """
    p = {**PARAMS_COLOMBIA_BASE, **(params or {})}

    def ode(t, y):
        cap, pipe, dem = y

        # Gap de oferta-demanda (normalizado)
        gap = (dem - cap) / max(dem, 1)
        gap = np.clip(gap, -0.5, 0.5)

        # Precio de bolsa (no-lineal)
        precio = p['precio_base'] * np.exp(p['k_precio'] * gap)
        precio = min(precio, p['precio_techo'])

        # Inversión: responde al precio con función sigmoide
        if precio > p['precio_umbral_inversion']:
            inicio = p['sensibilidad_inversion'] * (precio - p['precio_umbral_inversion']) / 100
            inicio = min(inicio, p['inversion_maxima'])
        else:
            inicio = 0

        # Puesta en servicio: pipeline sale con delay
        puesta = pipe / p['delay_construccion']

        # Retiro de plantas viejas
        retiro = cap / p['vida_util']

        # Crecimiento de demanda
        crec_dem = dem * p['tasa_crecimiento_demanda']

        # ODEs: dStock/dt = entradas - salidas
        dcap = puesta - retiro
        dpipe = inicio - puesta
        ddem = crec_dem

        return [dcap, dpipe, ddem]

    y0 = [p['capacidad_inicial'], p['pipeline_inicial'], p['demanda_inicial']]
    t_eval = np.arange(0, T, dt)

    sol = solve_ivp(ode, [0, T], y0, t_eval=t_eval, method='RK45',
                    max_step=0.5)

    # Recalcular auxiliares
    cap, pipe, dem = sol.y
    gap = (dem - cap) / np.maximum(dem, 1)
    gap = np.clip(gap, -0.5, 0.5)
    precio = p['precio_base'] * np.exp(p['k_precio'] * gap)
    precio = np.minimum(precio, p['precio_techo'])

    margen = (cap - dem) / np.maximum(dem, 1) * 100  # % de margen

    return pd.DataFrame({
        't': sol.t,
        'año': 2010 + sol.t,
        'capacidad_MW': cap,
        'pipeline_MW': pipe,
        'demanda_MW': dem,
        'gap': gap,
        'precio_bolsa': precio,
        'margen_pct': margen,
    })


def modelo_inversion_con_cxc_fncer(params=None, T=30, dt=0.1):
    """
    Extensión del modelo inversión-capacidad con:
    - Cargo por Confiabilidad (CxC): ingreso fijo por MW de capacidad firme
    - FNCER (solar/eólica): stock adicional con dinámica propia

    5 stocks:
    - Capacidad_Termica (MW)
    - Pipeline_Termica (MW)
    - Capacidad_Renovable (MW)
    - Pipeline_Renovable (MW)
    - Demanda (MW)

    Returns
    -------
    pd.DataFrame con todas las variables.
    """
    defaults = {
        **PARAMS_COLOMBIA_BASE,
        # CxC
        'cxc_pago': 15,               # USD/kW-año (Cargo por Confiabilidad)
        'cxc_activo': True,

        # FNCER
        'cap_renovable_inicial': 500,  # MW
        'pipeline_renovable_inicial': 800,
        'costo_renovable': 40,         # USD/MWh (LCOE solar 2020)
        'tasa_aprendizaje_renovable': 0.03,  # reducción anual del costo
        'delay_construccion_renovable': 2,    # años (más rápido que térmico)
        'factor_planta_renovable': 0.22,      # factor de planta solar Colombia

        # Escenarios
        'precio_gas': 1.0,             # multiplicador (1.0 = base)
        'frecuencia_nino': 0.15,       # prob anual de El Niño severo
    }
    p = {**defaults, **(params or {})}

    def ode(t, y):
        cap_t, pipe_t, cap_r, pipe_r, dem = y

        # Capacidad efectiva total
        cap_firme_renovable = cap_r * p['factor_planta_renovable']
        cap_total = cap_t + cap_firme_renovable

        # Gap y precio
        gap = (dem - cap_total) / max(dem, 1)
        gap = np.clip(gap, -0.5, 0.5)

        # Precio afectado por gas
        precio = p['precio_base'] * p['precio_gas'] * np.exp(p['k_precio'] * gap)
        precio = min(precio, p['precio_techo'])

        # === INVERSIÓN TÉRMICA ===
        ingreso_cxc = p['cxc_pago'] * 1000 / 8760 if p['cxc_activo'] else 0  # COP/kWh equiv
        precio_efectivo_termico = precio + ingreso_cxc

        if precio_efectivo_termico > p['precio_umbral_inversion']:
            inicio_t = p['sensibilidad_inversion'] * (precio_efectivo_termico - p['precio_umbral_inversion']) / 100
            inicio_t = min(inicio_t, p['inversion_maxima'])
        else:
            inicio_t = 0

        puesta_t = pipe_t / p['delay_construccion']
        retiro_t = cap_t / p['vida_util']

        # === INVERSIÓN RENOVABLE ===
        # Costo decrece con aprendizaje
        costo_ren_actual = p['costo_renovable'] * (1 - p['tasa_aprendizaje_renovable']) ** t
        # Inversión renovable: si el costo cae debajo del precio, inversión crece
        atractivo_ren = max(0, precio - costo_ren_actual * 10)  # margen
        inicio_r = min(p['inversion_maxima'], atractivo_ren * 30 / 100)

        puesta_r = pipe_r / p['delay_construccion_renovable']
        retiro_r = cap_r / (p['vida_util'] * 1.2)  # renovables duran un poco más

        # Demanda
        crec_dem = dem * p['tasa_crecimiento_demanda']

        return [
            puesta_t - retiro_t,    # dCap_termica
            inicio_t - puesta_t,    # dPipeline_termica
            puesta_r - retiro_r,    # dCap_renovable
            inicio_r - puesta_r,    # dPipeline_renovable
            crec_dem,               # dDemanda
        ]

    y0 = [
        p['capacidad_inicial'], p['pipeline_inicial'],
        p['cap_renovable_inicial'], p['pipeline_renovable_inicial'],
        p['demanda_inicial']
    ]
    t_eval = np.arange(0, T, dt)

    sol = solve_ivp(ode, [0, T], y0, t_eval=t_eval, method='RK45',
                    max_step=0.5)

    cap_t, pipe_t, cap_r, pipe_r, dem = sol.y
    cap_total = cap_t + cap_r * p['factor_planta_renovable']
    gap = (dem - cap_total) / np.maximum(dem, 1)
    precio = p['precio_base'] * p['precio_gas'] * np.exp(p['k_precio'] * np.clip(gap, -0.5, 0.5))
    precio = np.minimum(precio, p['precio_techo'])
    share_renovable = cap_r / (cap_t + cap_r) * 100

    return pd.DataFrame({
        't': sol.t,
        'año': 2010 + sol.t,
        'capacidad_termica_MW': cap_t,
        'capacidad_renovable_MW': cap_r,
        'capacidad_total_efectiva_MW': cap_total,
        'pipeline_termica_MW': pipe_t,
        'pipeline_renovable_MW': pipe_r,
        'demanda_MW': dem,
        'precio_bolsa': precio,
        'share_renovable_pct': share_renovable,
        'gap': gap,
    })


# ─────────────────────────────────────────────────────────────────────
# ESCENARIOS Y ANÁLISIS DE ROBUSTEZ (Semana 5)
# ─────────────────────────────────────────────────────────────────────

ESCENARIOS_COLOMBIA = {
    'BAU': {
        'nombre': 'Business as Usual',
        'descripcion': 'Gas estable, solar gradual, demanda normal',
        'precio_gas': 1.0,
        'tasa_aprendizaje_renovable': 0.03,
        'tasa_crecimiento_demanda': 0.025,
        'frecuencia_nino': 0.15,
    },
    'Gas Shock': {
        'nombre': 'Crisis del Gas',
        'descripcion': 'Precio del gas ×3, restricciones de suministro',
        'precio_gas': 3.0,
        'tasa_aprendizaje_renovable': 0.03,
        'tasa_crecimiento_demanda': 0.02,
        'frecuencia_nino': 0.15,
    },
    'Solar Revolution': {
        'nombre': 'Revolución Solar',
        'descripcion': 'Costos solares caen 60%, adopción acelerada',
        'precio_gas': 1.0,
        'tasa_aprendizaje_renovable': 0.08,
        'tasa_crecimiento_demanda': 0.03,
        'frecuencia_nino': 0.10,
    },
    'Niño Extremo': {
        'nombre': 'El Niño Extremo + Demanda Alta',
        'descripcion': 'El Niño frecuente, demanda crece 4%, estrés hídrico',
        'precio_gas': 1.5,
        'tasa_aprendizaje_renovable': 0.03,
        'tasa_crecimiento_demanda': 0.04,
        'frecuencia_nino': 0.30,
    },
}

ESTRATEGIAS_INVERSION = {
    'Conservadora': {
        'nombre': 'Conservadora (Térmica dominante)',
        'sensibilidad_inversion': 70,
        'inversion_maxima': 2000,
        'cxc_activo': True,
    },
    'Agresiva Renovable': {
        'nombre': 'Agresiva Renovable',
        'sensibilidad_inversion': 30,
        'inversion_maxima': 800,
        'cap_renovable_inicial': 1500,
        'pipeline_renovable_inicial': 2000,
        'cxc_activo': False,
    },
    'Diversificada': {
        'nombre': 'Diversificada (Balance)',
        'sensibilidad_inversion': 50,
        'inversion_maxima': 1200,
        'cap_renovable_inicial': 1000,
        'pipeline_renovable_inicial': 1200,
        'cxc_activo': True,
    },
}


def simular_escenarios(modelo_fn=None, escenarios=None, estrategias=None,
                       T=25, dt=0.1):
    """
    Simula todas las combinaciones escenario × estrategia.

    Parameters
    ----------
    modelo_fn : callable, optional
        Función del modelo SD. Default: modelo_inversion_con_cxc_fncer
    escenarios : dict, optional
        {nombre: {params}}. Default: ESCENARIOS_COLOMBIA
    estrategias : dict, optional
        {nombre: {params}}. Default: ESTRATEGIAS_INVERSION

    Returns
    -------
    dict de DataFrames: {(escenario, estrategia): df_resultados}
    """
    if modelo_fn is None:
        modelo_fn = modelo_inversion_con_cxc_fncer
    if escenarios is None:
        escenarios = ESCENARIOS_COLOMBIA
    if estrategias is None:
        estrategias = ESTRATEGIAS_INVERSION

    resultados = {}

    for esc_nombre, esc_params in escenarios.items():
        for est_nombre, est_params in estrategias.items():
            # Combinar parámetros (escenario + estrategia)
            params_combinados = {}
            for k, v in esc_params.items():
                if k not in ('nombre', 'descripcion'):
                    params_combinados[k] = v
            for k, v in est_params.items():
                if k != 'nombre':
                    params_combinados[k] = v

            df = modelo_fn(params=params_combinados, T=T, dt=dt)
            resultados[(esc_nombre, est_nombre)] = df

    return resultados


def calcular_metricas_escenario(df, metrica='costo_promedio'):
    """
    Calcula una métrica de desempeño de una simulación.

    Parameters
    ----------
    df : pd.DataFrame — resultado de un modelo SD
    metrica : str
        'costo_promedio': precio promedio de bolsa
        'volatilidad': desviación estándar del precio
        'deficit_maximo': máximo gap positivo (demanda > capacidad)
        'share_renovable_final': % renovable al final

    Returns
    -------
    float
    """
    if metrica == 'costo_promedio':
        return df['precio_bolsa'].mean()
    elif metrica == 'volatilidad':
        return df['precio_bolsa'].std()
    elif metrica == 'deficit_maximo':
        return df['gap'].max() * 100  # como porcentaje
    elif metrica == 'share_renovable_final':
        if 'share_renovable_pct' in df.columns:
            return df['share_renovable_pct'].iloc[-1]
        return 0.0
    else:
        raise ValueError(f"Métrica desconocida: {metrica}")


def tabla_robustez(resultados, metrica='costo_promedio'):
    """
    Construye la tabla de robustez: estrategias × escenarios.

    Parameters
    ----------
    resultados : dict
        {(escenario, estrategia): df} — output de simular_escenarios()
    metrica : str
        Métrica a evaluar (ver calcular_metricas_escenario)

    Returns
    -------
    pd.DataFrame con escenarios como filas, estrategias como columnas,
    más columnas de 'max_regret' y 'estrategia_robusta' flag.
    """
    escenarios = sorted(set(k[0] for k in resultados.keys()))
    estrategias = sorted(set(k[1] for k in resultados.keys()))

    # Calcular desempeño
    tabla = pd.DataFrame(index=escenarios, columns=estrategias, dtype=float)
    for (esc, est), df in resultados.items():
        tabla.loc[esc, est] = calcular_metricas_escenario(df, metrica)

    # Calcular regret (distancia al mejor por escenario)
    if metrica in ('costo_promedio', 'volatilidad', 'deficit_maximo'):
        # Menor es mejor
        mejor_por_escenario = tabla.min(axis=1)
        regret = tabla.subtract(mejor_por_escenario, axis=0)
    else:
        # Mayor es mejor (share_renovable_final)
        mejor_por_escenario = tabla.max(axis=1)
        regret = mejor_por_escenario.values.reshape(-1, 1) - tabla.values
        regret = pd.DataFrame(regret, index=escenarios, columns=estrategias)

    # Minimax regret
    max_regret = regret.max(axis=0)

    # Agregar filas de resumen
    tabla.loc['MAX REGRET'] = max_regret
    tabla.loc['RANKING'] = max_regret.rank().astype(int)

    return tabla


def analisis_sensibilidad(modelo_fn=None, params_base=None,
                           parametros_variar=None, rango_pct=0.3,
                           metrica='costo_promedio', T=25, dt=0.1):
    """
    Análisis de sensibilidad one-at-a-time (OAT).

    Parameters
    ----------
    parametros_variar : list of str
        Nombres de parámetros a variar.
    rango_pct : float
        Fracción de variación (0.3 = ±30%).

    Returns
    -------
    pd.DataFrame con columnas: parametro, valor_bajo, valor_alto,
    metrica_bajo, metrica_alto, sensibilidad
    """
    if modelo_fn is None:
        modelo_fn = modelo_inversion_capacidad
    if params_base is None:
        params_base = PARAMS_COLOMBIA_BASE.copy()
    if parametros_variar is None:
        parametros_variar = [
            'delay_construccion', 'k_precio', 'tasa_crecimiento_demanda',
            'sensibilidad_inversion', 'vida_util', 'precio_base'
        ]

    # Caso base
    df_base = modelo_fn(params=params_base, T=T, dt=dt)
    metrica_base = calcular_metricas_escenario(df_base, metrica)

    resultados = []
    for param in parametros_variar:
        if param not in params_base:
            continue

        val_base = params_base[param]

        # Valor bajo y alto
        val_bajo = val_base * (1 - rango_pct)
        val_alto = val_base * (1 + rango_pct)

        # Simular bajo
        p_bajo = {**params_base, param: val_bajo}
        df_bajo = modelo_fn(params=p_bajo, T=T, dt=dt)
        m_bajo = calcular_metricas_escenario(df_bajo, metrica)

        # Simular alto
        p_alto = {**params_base, param: val_alto}
        df_alto = modelo_fn(params=p_alto, T=T, dt=dt)
        m_alto = calcular_metricas_escenario(df_alto, metrica)

        resultados.append({
            'parametro': param,
            'valor_bajo': round(val_bajo, 3),
            'valor_base': round(val_base, 3),
            'valor_alto': round(val_alto, 3),
            'metrica_bajo': round(m_bajo, 2),
            'metrica_base': round(metrica_base, 2),
            'metrica_alto': round(m_alto, 2),
            'rango': round(abs(m_alto - m_bajo), 2),
        })

    df_sens = pd.DataFrame(resultados)
    df_sens = df_sens.sort_values('rango', ascending=True)  # para tornado
    return df_sens


# ─────────────────────────────────────────────────────────────────────
# VISUALIZACIÓN SD
# ─────────────────────────────────────────────────────────────────────

def plot_modelo_basico(resultado, variables, titulo=None, ylabel=None,
                       ax=None):
    """Gráfico de series de tiempo de un modelo SD simple."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    colores = list(viz.COLORS.values())
    for i, var in enumerate(variables):
        if var in resultado:
            data = resultado[var] if isinstance(resultado, dict) else resultado[var].values
            t = resultado['t'] if isinstance(resultado, dict) else resultado['t'].values
            ax.plot(t, data, color=colores[i % len(colores)],
                    linewidth=2, label=var.replace('_', ' ').title())

    ax.legend()
    ax.set_xlabel('Tiempo')
    if ylabel:
        ax.set_ylabel(ylabel)
    if titulo:
        ax.set_title(titulo, fontweight='bold')
    return ax


def plot_ciclo_inversion(df, titulo=None):
    """
    Dashboard de 4 paneles para el modelo inversión-capacidad.
    Auto-detecta si el DataFrame proviene del modelo básico
    (capacidad_MW) o del modelo CxC+FNCER (capacidad_total_efectiva_MW).
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Auto-detectar tipo de modelo
    es_cxc = 'capacidad_total_efectiva_MW' in df.columns
    col_cap = 'capacidad_total_efectiva_MW' if es_cxc else 'capacidad_MW'

    # Panel 1: Capacidad vs Demanda
    ax = axes[0, 0]
    if es_cxc:
        ax.stackplot(df['año'],
                     df['capacidad_termica_MW'],
                     df['capacidad_renovable_MW'],
                     labels=['Térmica', 'Renovable'],
                     colors=[viz.COLORS['warning'], viz.COLORS['success']],
                     alpha=0.4)
        ax.plot(df['año'], df[col_cap], color=viz.COLORS['primary'],
                linewidth=2, label='Capacidad total efectiva')
    else:
        ax.plot(df['año'], df[col_cap], color=viz.COLORS['primary'],
                linewidth=2, label='Capacidad instalada')
    ax.plot(df['año'], df['demanda_MW'], color=viz.COLORS['danger'],
            linewidth=2, linestyle='--', label='Demanda')
    ax.legend(fontsize=9)
    ax.set_ylabel('MW')
    ax.set_title('Capacidad vs Demanda')

    # Panel 2: Precio
    ax = axes[0, 1]
    ax.plot(df['año'], df['precio_bolsa'], color=viz.COLORS['accent'],
            linewidth=2)
    ax.axhline(y=PARAMS_COLOMBIA_BASE['precio_base'], color='gray',
               linestyle=':', alpha=0.5, label='Precio equilibrio')
    ax.set_ylabel('COP/kWh')
    ax.set_title('Precio de Bolsa')
    ax.legend(fontsize=9)

    # Panel 3: Pipeline
    ax = axes[1, 0]
    if es_cxc:
        ax.plot(df['año'], df['pipeline_termica_MW'],
                color=viz.COLORS['warning'], linewidth=2, label='Pipeline térmica')
        ax.plot(df['año'], df['pipeline_renovable_MW'],
                color=viz.COLORS['success'], linewidth=2, label='Pipeline renovable')
        ax.legend(fontsize=9)
    else:
        ax.plot(df['año'], df['pipeline_MW'], color=viz.COLORS['secondary'],
                linewidth=2)
        ax.fill_between(df['año'], 0, df['pipeline_MW'],
                        color=viz.COLORS['secondary'], alpha=0.1)
    ax.set_ylabel('MW en construcción')
    ax.set_title('Pipeline de Proyectos')
    ax.set_xlabel('Año')

    # Panel 4: Margen o Share Renovable
    ax = axes[1, 1]
    if es_cxc and 'share_renovable_pct' in df.columns:
        ax.plot(df['año'], df['share_renovable_pct'],
                color=viz.COLORS['success'], linewidth=2)
        ax.fill_between(df['año'], 0, df['share_renovable_pct'],
                        color=viz.COLORS['success'], alpha=0.1)
        ax.set_ylabel('Participación renovable (%)')
        ax.set_title('Participación Renovable en la Matriz')
    elif 'margen_pct' in df.columns:
        ax.plot(df['año'], df['margen_pct'], color=viz.COLORS['success'],
                linewidth=2)
        ax.axhline(y=0, color=viz.COLORS['danger'], linestyle='--', alpha=0.7,
                   label='Margen = 0 (déficit)')
        ax.fill_between(df['año'], 0, df['margen_pct'],
                        where=df['margen_pct'] > 0, alpha=0.1,
                        color=viz.COLORS['success'])
        ax.fill_between(df['año'], 0, df['margen_pct'],
                        where=df['margen_pct'] < 0, alpha=0.1,
                        color=viz.COLORS['danger'])
        ax.set_ylabel('Margen de reserva (%)')
        ax.set_title('Margen de Reserva')
        ax.legend(fontsize=9)
    else:
        gap_pct = df['gap'] * 100
        ax.plot(df['año'], gap_pct, color=viz.COLORS['danger'], linewidth=2)
        ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
        ax.set_ylabel('Gap oferta-demanda (%)')
        ax.set_title('Brecha Oferta-Demanda')
    ax.set_xlabel('Año')

    if titulo:
        fig.suptitle(titulo, fontsize=16, fontweight='bold', y=1.02)

    plt.tight_layout()
    return fig, axes


def plot_escenarios_comparados(resultados, variable='precio_bolsa',
                                estrategia=None, titulo=None):
    """
    Compara una variable a través de múltiples escenarios.

    Parameters
    ----------
    resultados : dict — output de simular_escenarios()
    variable : str — columna a plotear
    estrategia : str, optional — filtrar por una estrategia
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    colores = [viz.COLORS['primary'], viz.COLORS['danger'],
               viz.COLORS['success'], viz.COLORS['accent']]

    i = 0
    for (esc, est), df in resultados.items():
        if estrategia and est != estrategia:
            continue
        label = f"{esc}" if estrategia else f"{esc} / {est}"
        ax.plot(df['año'], df[variable], color=colores[i % len(colores)],
                linewidth=2, label=label, alpha=0.8)
        i += 1

    ax.legend(fontsize=9, loc='best')
    ax.set_xlabel('Año')
    ax.set_ylabel(variable.replace('_', ' ').title())
    if titulo:
        ax.set_title(titulo, fontweight='bold')

    return fig, ax


def plot_tornado(df_sensibilidad, metrica_nombre='Precio promedio',
                 titulo=None):
    """
    Diagrama tornado a partir de análisis de sensibilidad.

    Parameters
    ----------
    df_sensibilidad : pd.DataFrame — output de analisis_sensibilidad()
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, max(4, len(df_sensibilidad) * 0.6)))

    centro = df_sensibilidad['metrica_base'].iloc[0]
    y_pos = range(len(df_sensibilidad))

    # Barras hacia la izquierda (valor bajo)
    izq = df_sensibilidad['metrica_bajo'].values - centro
    # Barras hacia la derecha (valor alto)
    der = df_sensibilidad['metrica_alto'].values - centro

    ax.barh(y_pos, der, left=centro, color=viz.COLORS['danger'],
            alpha=0.7, label='Parámetro +30%', height=0.4)
    ax.barh(y_pos, izq, left=centro, color=viz.COLORS['primary'],
            alpha=0.7, label='Parámetro −30%', height=0.4)

    ax.set_yticks(y_pos)
    labels = [p.replace('_', ' ').title() for p in df_sensibilidad['parametro']]
    ax.set_yticklabels(labels)
    ax.axvline(x=centro, color='black', linewidth=1, linestyle='--')
    ax.set_xlabel(metrica_nombre)
    ax.legend(fontsize=9)

    if titulo:
        ax.set_title(titulo, fontweight='bold')

    plt.tight_layout()
    return fig, ax


def plot_tabla_robustez(tabla_df, metrica_nombre='Precio promedio',
                        titulo=None):
    """Visualización estilizada de la tabla de robustez como heatmap."""
    # Excluir filas de resumen para el heatmap
    datos = tabla_df.iloc[:-2].astype(float)

    fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    im = ax.imshow(datos.values, cmap='RdYlGn_r', aspect='auto')
    plt.colorbar(im, ax=ax, label=metrica_nombre, shrink=0.8)

    ax.set_xticks(range(len(datos.columns)))
    ax.set_xticklabels(datos.columns, rotation=30, ha='right')
    ax.set_yticks(range(len(datos.index)))
    ax.set_yticklabels(datos.index)

    # Anotar valores
    for i in range(len(datos.index)):
        for j in range(len(datos.columns)):
            val = datos.iloc[i, j]
            ax.text(j, i, f'{val:.0f}', ha='center', va='center',
                    fontsize=10, fontweight='bold',
                    color='white' if val > datos.values.mean() else 'black')

    if titulo:
        ax.set_title(titulo, fontweight='bold', pad=15)

    plt.tight_layout()
    return fig, ax


def simular_adopcion_simple(subsidio=0.0, costo_base=100.0, mercado_potencial=1000.0,
                            tasa_innovacion=0.01, tasa_imitacion=0.3,
                            T=25, dt=0.1):
    """
    Modelo SD simplificado de adopción tecnológica con subsidio.
    Basado en Bass con efecto del subsidio sobre la tasa de adopción.
    
    El subsidio reduce el costo efectivo, lo que incrementa tanto
    la tasa de innovación como la de imitación.
    
    Parameters
    ----------
    subsidio : float — fracción de subsidio (0 = sin subsidio, 0.5 = 50%)
    costo_base : float — costo unitario de referencia
    mercado_potencial : float — número total de adoptantes potenciales
    tasa_innovacion : float — p de Bass (adopción espontánea)
    tasa_imitacion : float — q de Bass (adopción por imitación)
    T : float — horizonte de simulación (años)
    dt : float — paso temporal
    """
    n_steps = int(T / dt)
    t = np.linspace(0, T, n_steps)
    adoptantes = np.zeros(n_steps)
    adoptantes[0] = mercado_potencial * 0.001  # semilla inicial
    
    # El subsidio amplifica las tasas de adopción
    factor_subsidio = 1.0 + 2.0 * subsidio  # 20% subsidio -> 1.4x
    p_eff = tasa_innovacion * factor_subsidio
    q_eff = tasa_imitacion * factor_subsidio
    costo_eff = costo_base * (1.0 - subsidio)
    
    for i in range(1, n_steps):
        F = adoptantes[i-1] / mercado_potencial
        dA = (p_eff + q_eff * F) * (mercado_potencial - adoptantes[i-1]) * dt
        adoptantes[i] = adoptantes[i-1] + dA
    
    return {
        't': t,
        'adoptantes': adoptantes,
        'mercado_potencial': mercado_potencial,
        'subsidio': subsidio,
        'costo_efectivo': costo_eff,
        'penetracion': adoptantes / mercado_potencial,
    }


def plot_comparacion_adopcion(resultado_sin, resultado_con, ax=None):
    """
    Compara curvas de adopción con y sin subsidio.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Panel 1: Adoptantes acumulados
    ax1 = axes[0]
    ax1.plot(resultado_sin['t'], resultado_sin['adoptantes'],
             color=viz.COLORS['node_default'], linewidth=2, linestyle='--',
             label='Sin subsidio')
    ax1.plot(resultado_con['t'], resultado_con['adoptantes'],
             color=viz.COLORS['primary'], linewidth=2.5,
             label=f'Con subsidio ({resultado_con["subsidio"]*100:.0f}%)')
    ax1.axhline(y=resultado_sin['mercado_potencial'], color='gray',
                linestyle=':', alpha=0.5, label='Mercado potencial')
    ax1.set_xlabel('Tiempo (anos)')
    ax1.set_ylabel('Adoptantes acumulados')
    ax1.set_title('Adopcion acumulada: efecto del subsidio',
                  fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    
    # Panel 2: Penetración (%)
    ax2 = axes[1]
    ax2.plot(resultado_sin['t'], resultado_sin['penetracion'] * 100,
             color=viz.COLORS['node_default'], linewidth=2, linestyle='--',
             label='Sin subsidio')
    ax2.plot(resultado_con['t'], resultado_con['penetracion'] * 100,
             color=viz.COLORS['primary'], linewidth=2.5,
             label=f'Con subsidio ({resultado_con["subsidio"]*100:.0f}%)')
    
    # Marcar cuando se alcanza 50% penetración
    for res, style, lbl in [(resultado_sin, '--', 'sin'), (resultado_con, '-', 'con')]:
        idx50 = np.argmax(res['penetracion'] >= 0.5)
        if idx50 > 0:
            t50 = res['t'][idx50]
            ax2.axvline(x=t50, color=viz.COLORS['accent'] if lbl == 'con' else 'gray',
                        linestyle=':', alpha=0.6)
            ax2.annotate(f't50 = {t50:.1f} anos',
                         xy=(t50, 50), fontsize=9,
                         ha='left', va='bottom')
    
    ax2.set_xlabel('Tiempo (anos)')
    ax2.set_ylabel('Penetracion (%)')
    ax2.set_title('Curva S de penetracion',
                  fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.set_ylim(0, 105)
    
    plt.tight_layout()
    return axes
