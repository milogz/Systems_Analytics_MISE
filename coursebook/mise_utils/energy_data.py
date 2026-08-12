"""
Datos sintéticos del sector energético colombiano
===================================================
Genera datasets realistas para los notebooks del curso, basados en
características conocidas del sistema eléctrico colombiano.

NOTA: Estos datos son SINTÉTICOS, diseñados para ser pedagógicamente
útiles. NO son datos oficiales del sector. Para análisis reales,
consultar las fuentes oficiales: XM (www.xm.com.co), UPME, CREG.
"""

import numpy as np
import pandas as pd
import networkx as nx


# ─────────────────────────────────────────────────────────────────────
# REFERENCIA INSTITUCIONAL COLOMBIANA
# ─────────────────────────────────────────────────────────────────────

INSTITUCIONES = {
    "XM": {
        "nombre_completo": "XM S.A. E.S.P.",
        "rol": "Operador del Sistema Interconectado Nacional (SIN) y administrador del Mercado de Energía Mayorista (MEM)",
        "funciones": "Despacho de generación, liquidación del mercado, gestión de restricciones de transmisión",
        "web": "www.xm.com.co"
    },
    "CREG": {
        "nombre_completo": "Comisión de Regulación de Energía y Gas",
        "rol": "Regulador del sector eléctrico y de gas natural",
        "funciones": "Define reglas del mercado, tarifas, mecanismos como el Cargo por Confiabilidad (CxC)",
        "web": "www.creg.gov.co"
    },
    "UPME": {
        "nombre_completo": "Unidad de Planeación Minero-Energética",
        "rol": "Planificador indicativo del sector",
        "funciones": "Planes de expansión de generación y transmisión, plan energético nacional",
        "web": "www.upme.gov.co"
    },
    "MME": {
        "nombre_completo": "Ministerio de Minas y Energía",
        "rol": "Formulador de política energética",
        "funciones": "Política pública, metas de transición energética, marco regulatorio general",
        "web": "www.minenergia.gov.co"
    },
    "ANLA": {
        "nombre_completo": "Autoridad Nacional de Licencias Ambientales",
        "rol": "Autoridad ambiental para grandes proyectos",
        "funciones": "Licencias ambientales, estudios de impacto, consulta previa",
        "web": "www.anla.gov.co"
    },
}


def print_instituciones():
    """Imprime una tabla de referencia de las instituciones del sector."""
    print("\n Instituciones del Sector Eléctrico Colombiano")
    print("=" * 65)
    for sigla, info in INSTITUCIONES.items():
        print(f"\n  {sigla} — {info['nombre_completo']}")
        print(f"  Rol: {info['rol']}")
        print(f"  Funciones: {info['funciones']}")
    print()


# ─────────────────────────────────────────────────────────────────────
# SEMANA 1: DATOS DE COMPLEJIDAD
# ─────────────────────────────────────────────────────────────────────

def generar_precios_bolsa(n_dias=730, seed=42):
    """
    Genera una serie sintética de precios de bolsa de energía eléctrica
    con características realistas: régimen base + episodios de estrés
    tipo El Niño con fat tails.

    La serie tiene dos regímenes:
    - Normal: precio ~180 COP/kWh con volatilidad moderada
    - Estrés (El Niño): precio sube a ~450 COP/kWh con picos >700

    Returns
    -------
    pd.DataFrame con columnas: fecha, precio_bolsa, nivel_embalse, es_nino
    """
    rng = np.random.default_rng(seed)

    fechas = pd.date_range("2015-01-01", periods=n_dias, freq="D")

    # Régimen base
    precio_base = 180.0
    volatilidad_base = 30.0

    # Simular El Niño (oct 2015 - abr 2016 ≈ días 270-480)
    es_nino = np.zeros(n_dias, dtype=bool)
    es_nino[270:480] = True

    # Nivel de embalses (normalizado 0-100%)
    embalse = np.zeros(n_dias)
    embalse[0] = 75.0  # Nivel inicial normal

    # Precios
    precios = np.zeros(n_dias)

    for t in range(n_dias):
        if es_nino[t]:
            # Durante El Niño: embalse baja, precios suben no linealmente
            delta_embalse = rng.normal(-0.15, 0.08)
            embalse[t] = max(15, embalse[t-1] + delta_embalse) if t > 0 else 60

            # Relación NO lineal embalse-precio (exponencial debajo de 40%)
            if embalse[t] < 40:
                factor_estres = np.exp(2.5 * (40 - embalse[t]) / 40)
            else:
                factor_estres = 1.0

            # Fat tails: usar distribución t-Student (colas pesadas)
            shock = rng.standard_t(df=3) * volatilidad_base * 2
            precios[t] = precio_base * factor_estres + shock
            precios[t] = max(50, min(900, precios[t]))
        else:
            # Normal: embalses se recuperan
            if t > 0:
                delta_embalse = rng.normal(0.05, 0.06)
                embalse[t] = min(95, max(30, embalse[t-1] + delta_embalse))
            else:
                embalse[t] = 75

            # Precios normales (lognormal para asimetría positiva)
            precios[t] = precio_base + rng.normal(0, volatilidad_base)
            precios[t] = max(50, precios[t])

    return pd.DataFrame({
        "fecha": fechas,
        "precio_bolsa": np.round(precios, 1),
        "nivel_embalse": np.round(embalse, 1),
        "es_nino": es_nino
    })


def generar_ciclo_inversion_capacidad(n_periodos=100, seed=42):
    """
    Genera datos del ciclo inversión-capacidad-precio en generación.
    Demuestra retroalimentación: precio alto → inversión → exceso de
    capacidad → precio bajo → no inversión → escasez → precio alto.

    Returns
    -------
    pd.DataFrame con columnas: t, precio, capacidad, inversion, demanda
    """
    rng = np.random.default_rng(seed)

    precio = np.zeros(n_periodos)
    capacidad = np.zeros(n_periodos)
    inversion = np.zeros(n_periodos)
    demanda = np.zeros(n_periodos)

    # Condiciones iniciales
    precio[0] = 150
    capacidad[0] = 15000  # MW
    demanda_base = 14000   # MW

    retardo_construccion = 5  # periodos

    for t in range(1, n_periodos):
        # Demanda crece linealmente + ruido
        demanda[t] = demanda_base + 50 * t + rng.normal(0, 200)

        # Precio depende del margen (capacidad - demanda)
        margen = (capacidad[t-1] - demanda[t]) / demanda[t]
        precio[t] = 120 * np.exp(-5 * margen) + rng.normal(0, 10)
        precio[t] = max(50, min(500, precio[t]))

        # Inversión responde al precio con retardo
        if t >= retardo_construccion:
            precio_pasado = precio[t - retardo_construccion]
            if precio_pasado > 180:
                inversion[t] = 0.8 * (precio_pasado - 180) + rng.normal(0, 30)
            else:
                inversion[t] = max(0, rng.normal(10, 10))
        else:
            inversion[t] = rng.normal(50, 20)

        inversion[t] = max(0, inversion[t])

        # Capacidad = anterior + inversión pasada - retiros
        retiro = rng.exponential(30)
        capacidad[t] = capacidad[t-1] + inversion[t] - retiro

    return pd.DataFrame({
        "t": range(n_periodos),
        "precio": np.round(precio, 1),
        "capacidad": np.round(capacidad, 0),
        "inversion": np.round(inversion, 1),
        "demanda": np.round(demanda, 0)
    })


# ─────────────────────────────────────────────────────────────────────
# SEMANA 2: RED DEL SIN (SIMPLIFICADA)
# ─────────────────────────────────────────────────────────────────────

def crear_red_sin_simplificada():
    """
    Crea una red simplificada del Sistema de Transmisión Nacional (STN)
    de Colombia con ~55 nodos principales y ~75 aristas.

    La topología refleja las características conocidas del SIN:
    - Corredores inter-regionales con pocos caminos alternativos
    - Hubs en Antioquia, Cundinamarca y Costa
    - Periferia en La Guajira, Nariño, Amazonia
    - Carácter radial en ciertas regiones

    NOTA: Esta es una representación SIMPLIFICADA y PEDAGÓGICA.
    No es la red real del STN.

    Returns
    -------
    G : networkx.Graph
        Con atributos de nodo: 'region', 'tipo', 'lat', 'lon' (aprox.)
    """
    G = nx.Graph()

    # ── NODOS POR REGIÓN ──
    nodos = {
        # Antioquia (hub central)
        "Ancón Sur":      {"region": "Antioquia", "tipo": "hub",        "lat": 6.15, "lon": -75.60},
        "Envigado":       {"region": "Antioquia", "tipo": "distribución","lat": 6.17, "lon": -75.59},
        "Barbosa":        {"region": "Antioquia", "tipo": "generación", "lat": 6.44, "lon": -75.33},
        "Guatapé":        {"region": "Antioquia", "tipo": "generación", "lat": 6.23, "lon": -75.16},
        "Ituango":        {"region": "Antioquia", "tipo": "generación", "lat": 7.13, "lon": -75.75},
        "Porce III":      {"region": "Antioquia", "tipo": "generación", "lat": 6.80, "lon": -75.11},

        # Cundinamarca / Bogotá (hub central)
        "Bacatá":         {"region": "Cundinamarca", "tipo": "hub",      "lat": 4.85, "lon": -74.00},
        "Torca":          {"region": "Cundinamarca", "tipo": "distribución","lat": 4.78, "lon": -74.03},
        "Tunal":          {"region": "Cundinamarca", "tipo": "distribución","lat": 4.58, "lon": -74.13},
        "Chivor":         {"region": "Cundinamarca", "tipo": "generación","lat": 4.88, "lon": -73.37},
        "Guavio":         {"region": "Cundinamarca", "tipo": "generación","lat": 4.75, "lon": -73.50},

        # Valle del Cauca
        "Yumbo":          {"region": "Valle", "tipo": "hub",            "lat": 3.59, "lon": -76.50},
        "San Marcos":     {"region": "Valle", "tipo": "distribución",   "lat": 3.47, "lon": -76.45},
        "Salvajina":      {"region": "Valle", "tipo": "generación",     "lat": 2.80, "lon": -76.70},
        "Alto Anchicayá": {"region": "Valle", "tipo": "generación",     "lat": 3.60, "lon": -76.88},

        # Costa Caribe
        "Cerromatoso":    {"region": "Costa", "tipo": "hub",            "lat": 7.95, "lon": -75.60},
        "Barranquilla":   {"region": "Costa", "tipo": "distribución",   "lat": 10.96,"lon": -74.78},
        "Cartagena":      {"region": "Costa", "tipo": "distribución",   "lat": 10.39,"lon": -75.51},
        "Ternera":        {"region": "Costa", "tipo": "distribución",   "lat": 10.35,"lon": -75.48},
        "Tebsa":          {"region": "Costa", "tipo": "generación",     "lat": 10.94,"lon": -74.80},
        "Santa Marta":    {"region": "Costa", "tipo": "distribución",   "lat": 11.24,"lon": -74.20},

        # Santanderes
        "Bucaramanga":    {"region": "Santander", "tipo": "distribución","lat": 7.12, "lon": -73.12},
        "Sogamoso":       {"region": "Santander", "tipo": "generación",  "lat": 6.65, "lon": -73.35},
        "Barranca":       {"region": "Santander", "tipo": "distribución","lat": 7.07, "lon": -73.85},

        # Boyacá / Centro
        "Tunja":          {"region": "Boyacá", "tipo": "distribución",  "lat": 5.53, "lon": -73.36},
        "Paipa":          {"region": "Boyacá", "tipo": "generación",    "lat": 5.78, "lon": -73.11},

        # Tolima / Huila
        "Betania":        {"region": "Huila", "tipo": "generación",     "lat": 2.72, "lon": -75.44},
        "Ibagué":         {"region": "Tolima", "tipo": "distribución",  "lat": 4.44, "lon": -75.24},
        "El Quimbo":      {"region": "Huila", "tipo": "generación",     "lat": 2.42, "lon": -75.68},

        # Cauca / Nariño
        "Popayán":        {"region": "Cauca", "tipo": "distribución",   "lat": 2.44, "lon": -76.61},
        "Pasto":          {"region": "Nariño", "tipo": "distribución",  "lat": 1.21, "lon": -77.28},
        "Jamondino":      {"region": "Nariño", "tipo": "distribución",  "lat": 1.20, "lon": -77.30},

        # Eje Cafetero
        "La Virginia":    {"region": "Risaralda", "tipo": "distribución","lat": 4.90, "lon": -75.88},
        "La Rosa":        {"region": "Risaralda", "tipo": "distribución","lat": 4.87, "lon": -75.70},
        "Manizales":      {"region": "Caldas", "tipo": "distribución",  "lat": 5.07, "lon": -75.52},

        # La Guajira (nueva frontera renovable)
        "Cuestecitas":    {"region": "Guajira", "tipo": "distribución", "lat": 11.36,"lon": -72.62},
        "Colectora Guajira":{"region": "Guajira", "tipo": "colector",  "lat": 11.80,"lon": -72.20},
        "Windpeshi":      {"region": "Guajira", "tipo": "generación",  "lat": 12.00,"lon": -71.90},

        # Llanos
        "Villavicencio":  {"region": "Meta", "tipo": "distribución",   "lat": 4.15, "lon": -73.64},

        # Norte de Santander
        "Cúcuta":         {"region": "N. Santander", "tipo": "distribución","lat": 7.89, "lon": -72.50},

        # Cesar
        "Valledupar":     {"region": "Cesar", "tipo": "distribución",  "lat": 10.47,"lon": -73.25},
        "El Paso Solar":  {"region": "Cesar", "tipo": "generación",    "lat": 9.96, "lon": -73.75},

        # Córdoba
        "Urrá":           {"region": "Córdoba", "tipo": "generación",  "lat": 7.88, "lon": -76.27},

        # Magdalena Medio
        "Puerto Berrío":  {"region": "Antioquia", "tipo": "distribución","lat": 6.49, "lon": -74.40},

        # Caño Limón / Arauca
        "Arauca":         {"region": "Arauca", "tipo": "distribución", "lat": 7.09, "lon": -70.76},
    }

    for nombre, attrs in nodos.items():
        G.add_node(nombre, **attrs)

    # ── ARISTAS (LÍNEAS DE TRANSMISIÓN) ──
    aristas = [
        # Corredor Antioquia interno
        ("Ancón Sur", "Envigado"), ("Ancón Sur", "Barbosa"),
        ("Ancón Sur", "Guatapé"), ("Ancón Sur", "Porce III"),
        ("Porce III", "Ituango"), ("Barbosa", "Porce III"),
        ("Guatapé", "Porce III"),

        # Corredor Antioquia - Costa (crítico)
        ("Cerromatoso", "Urrá"),
        ("Porce III", "Cerromatoso"), ("Ancón Sur", "Cerromatoso"),
        ("Cerromatoso", "Barranquilla"), ("Cerromatoso", "Cartagena"),
        ("Cerromatoso", "Ternera"), ("Barranquilla", "Tebsa"),
        ("Barranquilla", "Santa Marta"),

        # Corredor Antioquia - Centro
        ("Ancón Sur", "La Virginia"), ("La Virginia", "La Rosa"),
        ("La Rosa", "Manizales"),
        ("Ancón Sur", "Puerto Berrío"),

        # Corredor Centro - Bogotá
        ("Puerto Berrío", "Barranca"), ("Barranca", "Bucaramanga"),
        ("Bucaramanga", "Sogamoso"),
        ("Sogamoso", "Bacatá"), ("Bacatá", "Torca"), ("Bacatá", "Tunal"),
        ("Bacatá", "Chivor"), ("Bacatá", "Guavio"),
        ("Bacatá", "Tunja"), ("Tunja", "Paipa"), ("Tunja", "Sogamoso"),

        # Corredor Bogotá - Sur
        ("Bacatá", "Ibagué"), ("Ibagué", "La Virginia"),
        ("Ibagué", "Betania"), ("Betania", "El Quimbo"),

        # Corredor Sur
        ("Yumbo", "San Marcos"), ("Yumbo", "Salvajina"),
        ("Yumbo", "Alto Anchicayá"), ("Yumbo", "La Virginia"),
        ("San Marcos", "Popayán"), ("Popayán", "Pasto"),
        ("Pasto", "Jamondino"), ("Betania", "Popayán"),

        # Corredor La Guajira
        ("Santa Marta", "Valledupar"), ("Valledupar", "Cuestecitas"),
        ("Cuestecitas", "Colectora Guajira"),
        ("Colectora Guajira", "Windpeshi"),
        ("Valledupar", "El Paso Solar"),

        # Corredor Llanos
        ("Bacatá", "Villavicencio"), ("Chivor", "Villavicencio"),

        # Corredor Norte de Santander
        ("Bucaramanga", "Cúcuta"), ("Cúcuta", "Arauca"),

        # Manizales - Bogotá
        ("Manizales", "Ibagué"),
    ]

    G.add_edges_from(aristas)

    return G


def crear_red_pequena_ejemplo():
    """
    Crea la red de 6 nodos del ejemplo pedagógico (Semana 2).
    Subestaciones A-F con las conexiones del tutorial.
    """
    G = nx.Graph()
    G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
    G.add_edges_from([
        ("A", "B"), ("A", "C"), ("A", "D"),
        ("B", "C"), ("B", "E"),
        ("C", "D"),
        ("D", "F")
    ])
    return G


# ─────────────────────────────────────────────────────────────────────
# SEMANA 3: DATOS DE ADOPCIÓN Y ACTORES
# ─────────────────────────────────────────────────────────────────────

def generar_adopcion_solar_colombia(seed=42):
    """
    Genera serie temporal sintética de adopción solar distribuida
    en Colombia 2015-2025, con curva S (patrón Bass).

    Basado en patrones conocidos:
    - <10 MW acumulados en 2017
    - Aceleración post Ley 1715 (2014) y Ley 2099 (2021)
    - ~800 MW acumulados y ~6000 instalaciones para 2024

    Returns
    -------
    pd.DataFrame con: año, capacidad_mw, instalaciones, tasa_crecimiento
    """
    rng = np.random.default_rng(seed)

    años = np.arange(2015, 2026)
    N_potencial = 3000  # MW potencial estimado

    # Parámetros Bass calibrados para coincidir con la narrativa
    p = 0.005   # coeficiente de innovación (bajo → arranque lento)
    q = 0.45    # coeficiente de imitación (alto → crecimiento social)

    # Resolver Bass analíticamente
    from scipy.optimize import fsolve

    F = np.zeros(len(años))
    for i, t in enumerate(años - 2015):
        # Solución analítica de Bass
        F[i] = (1 - np.exp(-(p + q) * t)) / (1 + (q / p) * np.exp(-(p + q) * t))

    capacidad = N_potencial * F + rng.normal(0, 10, len(años))
    capacidad = np.maximum(0, capacidad)
    capacidad = np.round(capacidad, 1)

    # Instalaciones (proporcional a capacidad, ~5 kW promedio)
    instalaciones = np.round(capacidad / 0.005 * (1 + rng.normal(0, 0.1, len(años))))
    instalaciones = np.maximum(0, instalaciones).astype(int)

    tasa = np.zeros(len(años))
    tasa[1:] = np.diff(capacidad) / np.maximum(capacidad[:-1], 1) * 100

    return pd.DataFrame({
        "año": años,
        "capacidad_mw": capacidad,
        "instalaciones": instalaciones,
        "tasa_crecimiento_pct": np.round(tasa, 1)
    })


def crear_red_mercado_mayorista(seed=42):
    """
    Crea una red bipartita sintética del mercado mayorista colombiano.
    Nodos: generadores + comercializadores
    Aristas: contratos bilaterales (ponderados por GWh)

    Returns
    -------
    G : networkx.Graph
        Con atributos: 'tipo' ('generador' o 'comercializador'),
        'capacidad_mw' (generadores), 'demanda_gwh' (comercializadores)
    """
    rng = np.random.default_rng(seed)

    G = nx.Graph()

    generadores = {
        "EPM":       {"capacidad_mw": 3500, "tecnologia": "hidro"},
        "Enel":      {"capacidad_mw": 3200, "tecnologia": "hidro+térmica"},
        "ISAGEN":    {"capacidad_mw": 3000, "tecnologia": "hidro"},
        "Celsia":    {"capacidad_mw": 2000, "tecnologia": "hidro+solar"},
        "AES":       {"capacidad_mw": 1200, "tecnologia": "térmica"},
        "Gecelca":   {"capacidad_mw": 800,  "tecnologia": "térmica"},
        "TermoCandelaria":{"capacidad_mw": 350, "tecnologia": "térmica"},
        "Proelectrica":   {"capacidad_mw": 200, "tecnologia": "térmica"},
        "Solar Guajira":  {"capacidad_mw": 400, "tecnologia": "solar+eólica"},
        "Otros Gen":      {"capacidad_mw": 600, "tecnologia": "mixta"},
    }

    comercializadores = {
        "Codensa/Enel":   {"demanda_gwh": 14000, "cobertura": "Bogotá"},
        "EPM Comercial":  {"demanda_gwh": 10000, "cobertura": "Antioquia"},
        "Celsia Comercial":{"demanda_gwh": 5000, "cobertura": "Valle+Costa"},
        "Vatia":          {"demanda_gwh": 4000, "cobertura": "Nacional"},
        "Electricaribe":  {"demanda_gwh": 7000, "cobertura": "Costa Caribe"},
        "ESSA":           {"demanda_gwh": 3000, "cobertura": "Santander"},
        "CHEC":           {"demanda_gwh": 2000, "cobertura": "Caldas"},
        "Otros Com":      {"demanda_gwh": 5000, "cobertura": "Nacional"},
    }

    for name, attrs in generadores.items():
        G.add_node(name, tipo="generador", **attrs)

    for name, attrs in comercializadores.items():
        G.add_node(name, tipo="comercializador", **attrs)

    # Crear contratos (aristas ponderadas)
    gen_names = list(generadores.keys())
    com_names = list(comercializadores.keys())

    for gen in gen_names:
        # Cada generador tiene contratos con 2-5 comercializadores
        n_contratos = rng.integers(2, min(6, len(com_names) + 1))
        partners = rng.choice(com_names, size=n_contratos, replace=False)
        cap = generadores[gen]["capacidad_mw"]

        for com in partners:
            # Volumen proporcional a capacidad del generador y demanda del com
            dem = comercializadores[com]["demanda_gwh"]
            volumen = rng.uniform(0.1, 1.0) * cap * 0.5
            G.add_edge(gen, com, volumen_gwh=round(volumen, 1))

    return G


def crear_red_barrio(n_casas=100, tipo="small_world", seed=42):
    """
    Crea una red social de un barrio para simulaciones de adopción.

    Parameters
    ----------
    n_casas : int
    tipo : str
        'small_world' (Watts-Strogatz), 'grid' (lattice), 'random'
    seed : int

    Returns
    -------
    G : networkx.Graph
        Con atributo 'ingreso' por nodo (alto/medio/bajo)
    """
    rng = np.random.default_rng(seed)

    if tipo == "small_world":
        G = nx.watts_strogatz_graph(n_casas, k=6, p=0.1, seed=seed)
    elif tipo == "grid":
        side = int(np.sqrt(n_casas))
        G = nx.grid_2d_graph(side, side)
        G = nx.convert_node_labels_to_integers(G)
    else:
        G = nx.erdos_renyi_graph(n_casas, p=0.06, seed=seed)

    # Asignar ingresos (afecta umbral de adopción)
    for node in G.nodes():
        r = rng.random()
        if r < 0.2:
            G.nodes[node]["ingreso"] = "alto"
        elif r < 0.7:
            G.nodes[node]["ingreso"] = "medio"
        else:
            G.nodes[node]["ingreso"] = "bajo"

    return G
