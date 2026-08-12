"""
Soporte para Preludio: Fundamentos Científicos — MISE Systems Analytics
========================================================================
Simulaciones y visualizaciones de los pilares matemáticos de la ciencia
de sistemas complejos: caos, atractores, bifurcaciones, sincronización,
transiciones de fase en redes, criticidad auto-organizada.

Diseñado para impacto visual y narrativo — columna vertebral de video
introductorio.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from . import viz


# ─────────────────────────────────────────────────────────────────────
# 1. PROBLEMA DE TRES CUERPOS
# ─────────────────────────────────────────────────────────────────────

def tres_cuerpos(T=20, dt=0.001, seed=42):
    """
    Simula el problema gravitacional de tres cuerpos en 2D.
    Demuestra la complejidad e impredecibilidad de las trayectorias.

    Returns
    -------
    dict con 'pos' (3, n_steps, 2) array de posiciones, 't' array
    """
    rng = np.random.default_rng(seed)

    # Masas y condiciones iniciales (configuración tipo "figure-8" perturbada)
    m = np.array([1.0, 1.0, 1.0])

    # Posiciones iniciales (triángulo)
    r = np.array([
        [-0.97000436, 0.24308753],
        [0.97000436, -0.24308753],
        [0.0, 0.0],
    ])

    # Velocidades iniciales (solución periódica perturbada)
    v = np.array([
        [0.4662036850, 0.4323657300],
        [0.4662036850, 0.4323657300],
        [-0.9324073700, -0.8647314600],
    ])

    # Perturbar ligeramente para generar caos
    r += rng.normal(0, 0.01, r.shape)

    G = 1.0
    softening = 0.01  # evitar singularidades

    def derivs(t, state):
        pos = state[:6].reshape(3, 2)
        vel = state[6:].reshape(3, 2)
        acc = np.zeros_like(pos)

        for i in range(3):
            for j in range(3):
                if i != j:
                    rij = pos[j] - pos[i]
                    dist = np.sqrt(np.sum(rij**2) + softening**2)
                    acc[i] += G * m[j] * rij / dist**3

        return np.concatenate([vel.flatten(), acc.flatten()])

    state0 = np.concatenate([r.flatten(), v.flatten()])
    t_eval = np.arange(0, T, dt)

    sol = solve_ivp(derivs, [0, T], state0, t_eval=t_eval,
                    method='RK45', rtol=1e-10, atol=1e-10)

    pos = sol.y[:6].reshape(3, 2, -1).transpose(0, 2, 1)  # (3, n_steps, 2)

    return {'pos': pos, 't': sol.t, 'masas': m}


def plot_tres_cuerpos(resultado, trail_length=500, titulo=None):
    """
    Visualización del problema de tres cuerpos con estelas.
    """
    pos = resultado['pos']
    colores = [viz.COLORS['primary'], viz.COLORS['danger'], viz.COLORS['success']]
    nombres = ['Cuerpo 1', 'Cuerpo 2', 'Cuerpo 3']

    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_aspect('equal')

    for i in range(3):
        ax.plot(pos[i, :, 0], pos[i, :, 1], color=colores[i],
                alpha=0.3, linewidth=0.5)
        # Últimos puntos con más opacidad
        n = min(trail_length, pos.shape[1])
        ax.plot(pos[i, -n:, 0], pos[i, -n:, 1], color=colores[i],
                alpha=0.8, linewidth=1.5, label=nombres[i])
        # Posición final
        ax.plot(pos[i, -1, 0], pos[i, -1, 1], 'o', color=colores[i],
                markersize=10, zorder=5)

    ax.legend(fontsize=11)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if titulo:
        ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    return fig, ax


def plot_tres_cuerpos_frames(resultado, n_frames=6):
    """
    Múltiples snapshots mostrando la evolución temporal.
    Útil para narrativa de video.
    """
    pos = resultado['pos']
    t = resultado['t']
    n_steps = pos.shape[1]
    indices = np.linspace(0, n_steps - 1, n_frames, dtype=int)
    colores = [viz.COLORS['primary'], viz.COLORS['danger'], viz.COLORS['success']]

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for idx, (frame_idx, ax) in enumerate(zip(indices, axes)):
        ax.set_aspect('equal')
        for i in range(3):
            # Estela hasta este punto
            ax.plot(pos[i, :frame_idx+1, 0], pos[i, :frame_idx+1, 1],
                    color=colores[i], alpha=0.3, linewidth=0.5)
            # Posición actual
            ax.plot(pos[i, frame_idx, 0], pos[i, frame_idx, 1], 'o',
                    color=colores[i], markersize=8)

        ax.set_title(f't = {t[frame_idx]:.1f}', fontsize=11)
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.grid(True, alpha=0.2)

    fig.suptitle('Problema de Tres Cuerpos — Evolución Temporal',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig, axes


# ─────────────────────────────────────────────────────────────────────
# 2. ECUACIÓN LOGÍSTICA Y BIFURCACIONES
# ─────────────────────────────────────────────────────────────────────

def iterar_logistica(r, x0=0.5, n=100):
    """
    Itera el mapa logístico x_{n+1} = r * x_n * (1 - x_n).

    Returns
    -------
    np.array de longitud n+1
    """
    x = np.zeros(n + 1)
    x[0] = x0
    for i in range(n):
        x[i + 1] = r * x[i] * (1 - x[i])
    return x


def diagrama_bifurcacion(r_min=2.5, r_max=4.0, n_r=2000,
                          n_iter=300, n_last=100, x0=0.5):
    """
    Calcula el diagrama de bifurcación del mapa logístico.

    Parameters
    ----------
    n_r : int — número de valores de r a evaluar
    n_iter : int — iteraciones totales (para que el transitorio muera)
    n_last : int — últimas iteraciones a graficar (estado estacionario)

    Returns
    -------
    dict con 'r_values' y 'x_values' (arrays para scatter plot)
    """
    r_values = []
    x_values = []

    for r in np.linspace(r_min, r_max, n_r):
        x = x0
        # Iterar para pasar el transitorio
        for _ in range(n_iter):
            x = r * x * (1 - x)
        # Guardar los últimos n_last valores
        for _ in range(n_last):
            x = r * x * (1 - x)
            r_values.append(r)
            x_values.append(x)

    return {'r_values': np.array(r_values), 'x_values': np.array(x_values)}


def plot_bifurcacion(bif_data, titulo=None, ax=None):
    """Diagrama de bifurcación con estilo MISE."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    else:
        fig = ax.figure

    ax.scatter(bif_data['r_values'], bif_data['x_values'],
               s=0.01, c=viz.COLORS['primary'], alpha=0.3)

    ax.set_xlabel('Parámetro r', fontsize=12)
    ax.set_ylabel('$x^*$ (valores estacionarios)', fontsize=12)
    if titulo:
        ax.set_title(titulo, fontsize=14, fontweight='bold')

    # Anotar regiones
    ax.axvline(x=3.0, color=viz.COLORS['accent'], linestyle='--',
               alpha=0.4, linewidth=1)
    ax.axvline(x=3.57, color=viz.COLORS['danger'], linestyle='--',
               alpha=0.4, linewidth=1)

    ax.text(2.6, 0.95, 'Punto fijo\nestable', fontsize=9, color='gray',
            ha='center')
    ax.text(3.28, 0.95, 'Doblamiento\nde período', fontsize=9,
            color=viz.COLORS['accent'], ha='center')
    ax.text(3.8, 0.95, 'CAOS', fontsize=11, color=viz.COLORS['danger'],
            ha='center', fontweight='bold')

    return fig, ax


def plot_logistica_regimenes(x0=0.5, n=80):
    """
    Panel de 4 gráficos mostrando los regímenes de la ecuación logística.
    Ideal para explicar intuitivamente a público general.
    """
    configs = [
        (2.8, 'Equilibrio estable (r=2.8)',
         'La población converge a un valor fijo'),
        (3.3, 'Ciclo de período 2 (r=3.3)',
         'La población oscila entre dos valores'),
        (3.5, 'Ciclo de período 4 (r=3.5)',
         'Oscilación más compleja: 4 valores'),
        (3.9, 'Caos (r=3.9)',
         'Comportamiento aparentemente aleatorio\n— pero es determinista'),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    colores = [viz.COLORS['success'], viz.COLORS['primary'],
               viz.COLORS['accent'], viz.COLORS['danger']]

    for (r, titulo, subtitulo), ax, color in zip(configs, axes.flatten(), colores):
        x = iterar_logistica(r, x0, n)
        ax.plot(range(len(x)), x, color=color, linewidth=1.5, alpha=0.8)
        ax.scatter(range(len(x)), x, color=color, s=8, alpha=0.6, zorder=3)
        ax.set_title(titulo, fontsize=12, fontweight='bold')
        ax.text(0.02, 0.02, subtitulo, transform=ax.transAxes,
                fontsize=9, color='gray', va='bottom')
        ax.set_xlabel('Iteración n')
        ax.set_ylabel('$x_n$')
        ax.set_ylim(-0.05, 1.05)

    fig.suptitle('Ecuación Logística: $x_{n+1} = r \\cdot x_n \\cdot (1-x_n)$',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig, axes


# ─────────────────────────────────────────────────────────────────────
# 3. ATRACTOR DE LORENZ
# ─────────────────────────────────────────────────────────────────────

def lorenz_attractor(sigma=10, rho=28, beta=8/3, T=50, y0=None,
                     y0_perturbado=None, dt=0.01):
    """
    Integra el sistema de Lorenz.

    dx/dt = sigma * (y - x)
    dy/dt = x * (rho - z) - y
    dz/dt = x * y - beta * z

    Parameters
    ----------
    y0 : array-like, optional — condición inicial [x0, y0, z0]
    y0_perturbado : array-like, optional — segunda CI para comparar divergencia

    Returns
    -------
    dict con 'sol1' (t, x, y, z) y opcionalmente 'sol2'
    """
    if y0 is None:
        y0 = [1.0, 1.0, 1.0]

    def lorenz(t, state):
        x, y, z = state
        return [
            sigma * (y - x),
            x * (rho - z) - y,
            x * y - beta * z
        ]

    t_eval = np.arange(0, T, dt)

    sol1 = solve_ivp(lorenz, [0, T], y0, t_eval=t_eval, method='RK45',
                     rtol=1e-10, atol=1e-10)

    result = {
        'sol1': {'t': sol1.t, 'x': sol1.y[0], 'y': sol1.y[1], 'z': sol1.y[2]},
        'params': {'sigma': sigma, 'rho': rho, 'beta': beta},
    }

    if y0_perturbado is not None:
        sol2 = solve_ivp(lorenz, [0, T], y0_perturbado, t_eval=t_eval,
                         method='RK45', rtol=1e-10, atol=1e-10)
        result['sol2'] = {'t': sol2.t, 'x': sol2.y[0], 'y': sol2.y[1], 'z': sol2.y[2]}

    return result


def plot_lorenz_3d(resultado, titulo=None):
    """Visualización 3D del atractor de Lorenz."""
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    s1 = resultado['sol1']
    ax.plot(s1['x'], s1['y'], s1['z'], color=viz.COLORS['primary'],
            linewidth=0.4, alpha=0.7)

    if 'sol2' in resultado:
        s2 = resultado['sol2']
        ax.plot(s2['x'], s2['y'], s2['z'], color=viz.COLORS['danger'],
                linewidth=0.4, alpha=0.7)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    if titulo:
        ax.set_title(titulo, fontsize=14, fontweight='bold')

    ax.view_init(elev=25, azim=130)
    return fig, ax


def plot_lorenz_divergencia(resultado, variable='x', titulo=None):
    """
    Muestra cómo dos trayectorias cercanas divergen en el tiempo.
    Ideal para demostrar sensibilidad a condiciones iniciales.
    """
    if 'sol2' not in resultado:
        raise ValueError("Necesitas pasar y0_perturbado para ver divergencia")

    fig, axes = plt.subplots(2, 1, figsize=(14, 8), height_ratios=[2, 1])

    s1 = resultado['sol1']
    s2 = resultado['sol2']

    # Panel superior: ambas series
    ax = axes[0]
    ax.plot(s1['t'], s1[variable], color=viz.COLORS['primary'],
            linewidth=0.8, label='Trayectoria 1', alpha=0.8)
    ax.plot(s2['t'], s2[variable], color=viz.COLORS['danger'],
            linewidth=0.8, label='Trayectoria 2', alpha=0.8)
    ax.legend(fontsize=10)
    ax.set_ylabel(f'{variable}(t)')
    ax.set_title(titulo or 'Divergencia de trayectorias — Sistema de Lorenz',
                 fontsize=13, fontweight='bold')

    # Panel inferior: distancia entre trayectorias
    ax = axes[1]
    dist = np.sqrt((s1['x'] - s2['x'])**2 +
                   (s1['y'] - s2['y'])**2 +
                   (s1['z'] - s2['z'])**2)
    ax.semilogy(s1['t'], dist, color=viz.COLORS['accent'], linewidth=1.5)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Distancia (log)')
    ax.set_title('Separación exponencial', fontsize=11)
    ax.axhline(y=dist[0], color='gray', linestyle=':', alpha=0.5,
               label=f'Perturbación inicial: {dist[0]:.1e}')
    ax.legend(fontsize=9)

    plt.tight_layout()
    return fig, axes


# ─────────────────────────────────────────────────────────────────────
# 4. PÉNDULO SIMPLE vs PÉNDULO DOBLE
# ─────────────────────────────────────────────────────────────────────

def pendulo_simple(theta0=2.5, omega0=0.0, T=20, dt=0.01, g=9.81, L=1.0):
    """
    Péndulo simple (no-linealizado): d²θ/dt² = -(g/L)*sin(θ)

    Returns
    -------
    dict con 't', 'theta', 'omega'
    """
    def ode(t, y):
        theta, omega = y
        return [omega, -(g / L) * np.sin(theta)]

    t_eval = np.arange(0, T, dt)
    sol = solve_ivp(ode, [0, T], [theta0, omega0], t_eval=t_eval,
                    method='RK45')

    return {'t': sol.t, 'theta': sol.y[0], 'omega': sol.y[1]}


def pendulo_doble(theta1_0=2.0, theta2_0=2.0, omega1_0=0.0, omega2_0=0.0,
                  T=20, dt=0.005, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
    """
    Péndulo doble: sistema caótico de 4 dimensiones.

    Returns
    -------
    dict con 't', 'theta1', 'theta2', 'omega1', 'omega2',
    'x1', 'y1', 'x2', 'y2' (coordenadas cartesianas)
    """
    def ode(t, y):
        t1, t2, w1, w2 = y
        dt_ = t1 - t2
        M = m1 + m2

        den1 = M * L1 - m2 * L1 * np.cos(dt_)**2
        den2 = (L2 / L1) * den1

        dw1 = (-m2 * L1 * w1**2 * np.sin(dt_) * np.cos(dt_)
               + m2 * g * np.sin(t2) * np.cos(dt_)
               - m2 * L2 * w2**2 * np.sin(dt_)
               - M * g * np.sin(t1)) / den1

        dw2 = (m2 * L2 * w2**2 * np.sin(dt_) * np.cos(dt_)
               + M * g * np.sin(t1) * np.cos(dt_)
               + M * L1 * w1**2 * np.sin(dt_)
               - M * g * np.sin(t2)) / den2

        return [w1, w2, dw1, dw2]

    t_eval = np.arange(0, T, dt)
    sol = solve_ivp(ode, [0, T], [theta1_0, theta2_0, omega1_0, omega2_0],
                    t_eval=t_eval, method='RK45', rtol=1e-10, atol=1e-10)

    t1, t2 = sol.y[0], sol.y[1]

    return {
        't': sol.t,
        'theta1': t1, 'theta2': t2,
        'omega1': sol.y[2], 'omega2': sol.y[3],
        'x1': L1 * np.sin(t1),
        'y1': -L1 * np.cos(t1),
        'x2': L1 * np.sin(t1) + L2 * np.sin(t2),
        'y2': -L1 * np.cos(t1) - L2 * np.cos(t2),
    }


def plot_pendulos_comparacion(perturbacion=0.001, T=15):
    """
    Compara péndulo simple (predecible) vs péndulo doble (caótico).
    Dos CIs casi idénticas → divergencia solo en el doble.
    """
    # Péndulo simple: dos CIs cercanas
    ps1 = pendulo_simple(theta0=2.0, T=T)
    ps2 = pendulo_simple(theta0=2.0 + perturbacion, T=T)

    # Péndulo doble: dos CIs cercanas
    pd1 = pendulo_doble(theta1_0=2.0, theta2_0=2.0, T=T)
    pd2 = pendulo_doble(theta1_0=2.0 + perturbacion, theta2_0=2.0, T=T)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Péndulo simple: series temporales
    ax = axes[0, 0]
    ax.plot(ps1['t'], ps1['theta'], color=viz.COLORS['primary'],
            linewidth=1.5, label='CI original')
    ax.plot(ps2['t'], ps2['theta'], color=viz.COLORS['danger'],
            linewidth=1.5, linestyle='--', label=f'CI + {perturbacion}°')
    ax.set_title('Péndulo Simple — θ(t)', fontweight='bold')
    ax.set_ylabel('θ (rad)')
    ax.legend(fontsize=9)

    # Péndulo simple: espacio de fases
    ax = axes[0, 1]
    ax.plot(ps1['theta'], ps1['omega'], color=viz.COLORS['primary'], linewidth=1)
    ax.plot(ps2['theta'], ps2['omega'], color=viz.COLORS['danger'],
            linewidth=1, linestyle='--')
    ax.set_title('Péndulo Simple — Espacio de Fases', fontweight='bold')
    ax.set_xlabel('θ')
    ax.set_ylabel('ω')

    # Péndulo doble: series temporales
    ax = axes[1, 0]
    ax.plot(pd1['t'], pd1['theta2'], color=viz.COLORS['primary'],
            linewidth=1, label='CI original')
    ax.plot(pd2['t'], pd2['theta2'], color=viz.COLORS['danger'],
            linewidth=1, label=f'CI + {perturbacion}°')
    ax.set_title('Péndulo Doble — θ₂(t)', fontweight='bold')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('θ₂ (rad)')
    ax.legend(fontsize=9)

    # Péndulo doble: trayectoria del extremo
    ax = axes[1, 1]
    ax.plot(pd1['x2'], pd1['y2'], color=viz.COLORS['primary'],
            linewidth=0.5, alpha=0.6, label='CI original')
    ax.plot(pd2['x2'], pd2['y2'], color=viz.COLORS['danger'],
            linewidth=0.5, alpha=0.6, label=f'CI + {perturbacion}°')
    ax.set_title('Péndulo Doble — Trayectoria del extremo', fontweight='bold')
    ax.set_aspect('equal')
    ax.legend(fontsize=9)

    fig.suptitle(f'Predecible vs Caótico (perturbación = {perturbacion}°)',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig, axes


# ─────────────────────────────────────────────────────────────────────
# 5. SINCRONIZACIÓN: MODELO DE KURAMOTO
# ─────────────────────────────────────────────────────────────────────

def kuramoto(N=50, K=0.0, T=30, dt=0.05, omega_spread=1.0, seed=42):
    """
    Modelo de Kuramoto: N osciladores acoplados.

    dθ_i/dt = ω_i + (K/N) * Σ sin(θ_j - θ_i)

    Parameters
    ----------
    N : int — número de osciladores
    K : float — fuerza de acoplamiento
    omega_spread : float — dispersión de frecuencias naturales

    Returns
    -------
    dict con 't', 'phases' (N, n_steps), 'order_parameter' (n_steps),
    'frequencies' (N,)
    """
    rng = np.random.default_rng(seed)

    # Frecuencias naturales (distribución Lorentziana)
    omega = rng.standard_cauchy(N) * omega_spread * 0.3
    omega = np.clip(omega, -3 * omega_spread, 3 * omega_spread)

    # Fases iniciales (uniformes en [0, 2π])
    theta0 = rng.uniform(0, 2 * np.pi, N)

    n_steps = int(T / dt)
    phases = np.zeros((N, n_steps))
    phases[:, 0] = theta0
    order_param = np.zeros(n_steps)

    for step in range(n_steps):
        theta = phases[:, step]
        # Order parameter
        z = np.mean(np.exp(1j * theta))
        order_param[step] = np.abs(z)

        if step < n_steps - 1:
            # Euler integration
            coupling = np.zeros(N)
            for i in range(N):
                coupling[i] = (K / N) * np.sum(np.sin(theta - theta[i]))

            phases[:, step + 1] = theta + (omega + coupling) * dt

    return {
        't': np.arange(n_steps) * dt,
        'phases': phases,
        'order_parameter': order_param,
        'frequencies': omega,
        'K': K, 'N': N,
    }


def plot_kuramoto_transicion(K_values=None, N=50, T=30, seed=42):
    """
    Muestra la transición de desorden a sincronización al aumentar K.
    """
    if K_values is None:
        K_values = [0.0, 1.0, 3.0, 8.0]

    fig, axes = plt.subplots(2, len(K_values), figsize=(4 * len(K_values), 8))

    for col, K in enumerate(K_values):
        res = kuramoto(N=N, K=K, T=T, seed=seed)

        # Fila superior: fases en el tiempo (cada oscilador)
        ax = axes[0, col]
        for i in range(min(N, 20)):  # Mostrar máximo 20 líneas
            ax.plot(res['t'], np.mod(res['phases'][i], 2 * np.pi),
                    linewidth=0.5, alpha=0.4)
        ax.set_title(f'K = {K}', fontweight='bold')
        ax.set_ylabel('Fase θ (mod 2π)' if col == 0 else '')
        ax.set_ylim(0, 2 * np.pi)

        # Fila inferior: order parameter
        ax = axes[1, col]
        ax.plot(res['t'], res['order_parameter'],
                color=viz.COLORS['primary'], linewidth=2)
        ax.set_ylim(0, 1.05)
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Orden r(t)' if col == 0 else '')
        r_final = np.mean(res['order_parameter'][-100:])
        ax.axhline(y=r_final, color=viz.COLORS['danger'], linestyle='--',
                   alpha=0.5)
        ax.text(0.95, 0.95, f'r = {r_final:.2f}', transform=ax.transAxes,
                ha='right', va='top', fontsize=11, fontweight='bold',
                color=viz.COLORS['danger'])

    fig.suptitle('Sincronización de Kuramoto: de desorden a orden',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig, axes


# ─────────────────────────────────────────────────────────────────────
# 6. TRANSICIONES DE FASE EN REDES
# ─────────────────────────────────────────────────────────────────────

def percolacion_red(n=500, p_range=None, n_muestras=20, seed=42):
    """
    Mide el tamaño del componente gigante en redes Erdős-Rényi
    al variar la probabilidad de conexión p.

    Demuestra la transición de fase en p_c ≈ 1/N.

    Returns
    -------
    dict con 'p_values', 'gc_mean', 'gc_std', 'p_critico'
    """
    import networkx as nx

    if p_range is None:
        p_range = np.linspace(0, 5.0 / n, 60)

    rng = np.random.default_rng(seed)
    gc_mean = []
    gc_std = []

    for p in p_range:
        gc_sizes = []
        for _ in range(n_muestras):
            G = nx.erdos_renyi_graph(n, p, seed=int(rng.integers(1e9)))
            if len(G) > 0:
                largest_cc = max(nx.connected_components(G), key=len)
                gc_sizes.append(len(largest_cc) / n)
            else:
                gc_sizes.append(0)
        gc_mean.append(np.mean(gc_sizes))
        gc_std.append(np.std(gc_sizes))

    return {
        'p_values': p_range,
        'gc_mean': np.array(gc_mean),
        'gc_std': np.array(gc_std),
        'p_critico': 1.0 / n,
        'n': n,
    }


def plot_percolacion(resultado, titulo=None):
    """Gráfico de transición de fase con zona crítica marcada."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    p = resultado['p_values']
    gc = resultado['gc_mean']
    gc_std = resultado['gc_std']
    pc = resultado['p_critico']

    ax.plot(p * resultado['n'], gc, color=viz.COLORS['primary'],
            linewidth=2.5)
    ax.fill_between(p * resultado['n'], gc - gc_std, gc + gc_std,
                    color=viz.COLORS['primary'], alpha=0.15)

    ax.axvline(x=1.0, color=viz.COLORS['danger'], linestyle='--',
               linewidth=2, label=f'$p_c = 1/N$ (transición)')

    ax.set_xlabel('$\\langle k \\rangle = p \\cdot N$ (grado promedio)',
                  fontsize=12)
    ax.set_ylabel('Fracción en componente gigante', fontsize=12)
    ax.legend(fontsize=11)
    ax.set_title(titulo or 'Transición de Fase en Red Erdős-Rényi',
                 fontsize=14, fontweight='bold')

    # Anotaciones
    ax.text(0.3, 0.8, 'Fragmentado', fontsize=11, color='gray',
            transform=ax.transAxes)
    ax.text(0.7, 0.2, 'Conectado', fontsize=11,
            color=viz.COLORS['primary'], transform=ax.transAxes,
            fontweight='bold')

    return fig, ax


# ─────────────────────────────────────────────────────────────────────
# 7. CRITICIDAD AUTO-ORGANIZADA (SOC) — Pila de Arena BTW
# ─────────────────────────────────────────────────────────────────────

def sandpile_btw(grid_size=50, n_grains=5000, seed=42):
    """
    Modelo BTW (Bak-Tang-Wiesenfeld) de pila de arena.
    Demuestra criticidad auto-organizada.

    Returns
    -------
    dict con 'grid' (estado final), 'avalanche_sizes' (lista de tamaños),
    'avalanche_history' (lista de grids para animación)
    """
    rng = np.random.default_rng(seed)
    grid = np.zeros((grid_size, grid_size), dtype=int)
    threshold = 4
    avalanche_sizes = []
    history_snapshots = []

    for grain in range(n_grains):
        # Agregar grano aleatorio
        i, j = rng.integers(0, grid_size, 2)
        grid[i, j] += 1

        # Toppling cascade
        cascade_size = 0
        while np.any(grid >= threshold):
            unstable = np.where(grid >= threshold)
            for ui, uj in zip(unstable[0], unstable[1]):
                if grid[ui, uj] >= threshold:
                    grid[ui, uj] -= 4
                    cascade_size += 1
                    # Distribuir a vecinos
                    if ui > 0:
                        grid[ui - 1, uj] += 1
                    if ui < grid_size - 1:
                        grid[ui + 1, uj] += 1
                    if uj > 0:
                        grid[ui, uj - 1] += 1
                    if uj < grid_size - 1:
                        grid[ui, uj + 1] += 1

        if cascade_size > 0:
            avalanche_sizes.append(cascade_size)

        # Guardar snapshots periódicos
        if grain % (n_grains // 10) == 0:
            history_snapshots.append(grid.copy())

    return {
        'grid': grid,
        'avalanche_sizes': avalanche_sizes,
        'history': history_snapshots,
    }


def plot_sandpile(resultado, titulo=None):
    """Pila de arena: estado final + distribución de avalanchas."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Grid
    ax = axes[0]
    im = ax.imshow(resultado['grid'], cmap='YlOrRd', interpolation='nearest')
    plt.colorbar(im, ax=ax, label='Granos de arena', shrink=0.8)
    ax.set_title('Estado de la pila de arena', fontweight='bold')

    # Distribución de avalanchas (log-log)
    ax = axes[1]
    sizes = resultado['avalanche_sizes']
    if len(sizes) > 0:
        bins = np.logspace(0, np.log10(max(sizes) + 1), 30)
        counts, edges = np.histogram(sizes, bins=bins)
        centers = (edges[:-1] + edges[1:]) / 2
        mask = counts > 0
        ax.loglog(centers[mask], counts[mask], 'o',
                  color=viz.COLORS['primary'], markersize=5, alpha=0.7)

        # Fit line
        log_x = np.log10(centers[mask])
        log_y = np.log10(counts[mask])
        if len(log_x) > 2:
            coeffs = np.polyfit(log_x, log_y, 1)
            ax.loglog(centers[mask], 10**(coeffs[0] * log_x + coeffs[1]),
                      '--', color=viz.COLORS['danger'], linewidth=2,
                      label=f'Pendiente ≈ {coeffs[0]:.2f}')

    ax.set_xlabel('Tamaño de avalancha', fontsize=12)
    ax.set_ylabel('Frecuencia', fontsize=12)
    ax.set_title('Distribución de avalanchas (log-log)', fontweight='bold')
    ax.legend(fontsize=10)

    if titulo:
        fig.suptitle(titulo, fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    return fig, axes


# ─────────────────────────────────────────────────────────────────────
# 8. CLASIFICACIÓN DE PUNTOS FIJOS (Tabla de Strogatz)
# ─────────────────────────────────────────────────────────────────────

def clasificar_punto_fijo(J):
    """
    Dado un Jacobiano 2×2, retorna el tipo de punto fijo.

    Parameters
    ----------
    J : array-like (2,2) — matriz Jacobiana

    Returns
    -------
    dict con 'eigenvalues', 'tipo', 'estabilidad', 'descripcion'
    """
    J = np.array(J, dtype=float)
    eigenvalues = np.linalg.eigvals(J)

    real_parts = eigenvalues.real
    imag_parts = eigenvalues.imag

    has_imag = np.any(np.abs(imag_parts) > 1e-10)

    if has_imag:
        if np.all(real_parts < -1e-10):
            tipo = 'Espiral estable'
            estabilidad = 'Estable'
            desc = 'Las trayectorias espiralan hacia el punto fijo (oscilaciones amortiguadas)'
        elif np.all(real_parts > 1e-10):
            tipo = 'Espiral inestable'
            estabilidad = 'Inestable'
            desc = 'Las trayectorias espiralan alejándose del punto fijo'
        else:
            tipo = 'Centro'
            estabilidad = 'Neutral'
            desc = 'Órbitas cerradas alrededor del punto fijo (oscilaciones puras)'
    else:
        if np.all(real_parts < -1e-10):
            tipo = 'Nodo estable'
            estabilidad = 'Estable'
            desc = 'Las trayectorias convergen monotónicamente al punto fijo'
        elif np.all(real_parts > 1e-10):
            tipo = 'Nodo inestable'
            estabilidad = 'Inestable'
            desc = 'Las trayectorias divergen monotónicamente del punto fijo'
        elif real_parts[0] * real_parts[1] < 0:
            tipo = 'Punto silla'
            estabilidad = 'Inestable'
            desc = 'Atrae en una dirección, repele en otra'
        else:
            tipo = 'Degenerado'
            estabilidad = 'Indeterminado'
            desc = 'Caso límite — requiere análisis no-lineal'

    return {
        'eigenvalues': eigenvalues,
        'tipo': tipo,
        'estabilidad': estabilidad,
        'descripcion': desc,
    }


def tabla_strogatz_visual():
    """
    Genera la tabla visual de clasificación de puntos fijos en 2D.
    Retorna un DataFrame para mostrar en el notebook.
    """
    import pandas as pd

    data = [
        {'λ₁, λ₂': 'Reales, ambos < 0', 'Tipo': 'Nodo estable',
         'Comportamiento': 'Convergencia monotónica', 'Ejemplo': 'Amortiguamiento sobredamped'},
        {'λ₁, λ₂': 'Reales, ambos > 0', 'Tipo': 'Nodo inestable',
         'Comportamiento': 'Divergencia monotónica', 'Ejemplo': 'Explosión exponencial'},
        {'λ₁, λ₂': 'Reales, signos opuestos', 'Tipo': 'Punto silla',
         'Comportamiento': 'Atrae y repele', 'Ejemplo': 'Equilibrio de mercado inestable'},
        {'λ₁, λ₂': 'Complejos, Re < 0', 'Tipo': 'Espiral estable',
         'Comportamiento': 'Oscilaciones amortiguadas', 'Ejemplo': 'Precio que oscila y converge'},
        {'λ₁, λ₂': 'Complejos, Re > 0', 'Tipo': 'Espiral inestable',
         'Comportamiento': 'Oscilaciones crecientes', 'Ejemplo': 'Ciclo inversión sin control'},
        {'λ₁, λ₂': 'Imaginarios puros', 'Tipo': 'Centro',
         'Comportamiento': 'Oscilaciones perpetuas', 'Ejemplo': 'Péndulo sin fricción'},
    ]

    return pd.DataFrame(data)
