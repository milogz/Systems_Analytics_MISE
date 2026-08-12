"""
Caso Colombia: Sistema Eléctrico Colombiano — MISE Systems Analytics
=====================================================================
Levantamiento integral del Sistema Interconectado Nacional (SIN),
incluyendo actores, cadena de valor, red de transmisión, datos
históricos y marco regulatorio.

Datos basados en fuentes públicas (XM, UPME, CREG, 2024).
Para análisis formales, siempre consultar fuentes oficiales.
"""

import numpy as np
import pandas as pd
import networkx as nx


# ─────────────────────────────────────────────────────────────────────
# 1. ACTORES: GENERADORES
# ─────────────────────────────────────────────────────────────────────

GENERADORES = {
    'EPM': {
        'nombre': 'Empresas Públicas de Medellín',
        'capacidad_MW': 5000,
        'hidro_MW': 4350, 'termico_MW': 433, 'solar_MW': 83, 'eolico_MW': 0,
        'plantas_principales': [
            'Hidroituango (1200 MW)', 'San Carlos (1240 MW)',
            'Guatapé (560 MW)', 'Porce II-III (605 MW)',
            'Playas (204 MW)', 'La Sierra gas (433 MW)',
        ],
        'propiedad': 'Municipio de Medellín',
        'tipo_propiedad': 'público',
        'region': 'Antioquia',
        'share_mercado': 0.24,
    },
    'Enel Colombia': {
        'nombre': 'Enel Colombia (ex-Emgesa/Codensa)',
        'capacidad_MW': 4011,
        'hidro_MW': 3097, 'termico_MW': 226, 'solar_MW': 688, 'eolico_MW': 0,
        'plantas_principales': [
            'Guavio (1250 MW)', 'Cadena Pagua (850 MW)',
            'Betania (540 MW)', 'El Paso solar (86 MW)',
            'Guayepo I-II solar (485 MW)', 'Termozipa carbón (226 MW)',
        ],
        'propiedad': 'Enel (Italia) + GEB',
        'tipo_propiedad': 'privado/mixto',
        'region': 'Cundinamarca',
        'share_mercado': 0.188,
    },
    'Isagen': {
        'nombre': 'Isagen S.A. E.S.P.',
        'capacidad_MW': 3032,
        'hidro_MW': 2732, 'termico_MW': 300, 'solar_MW': 0, 'eolico_MW': 0,
        'plantas_principales': [
            'Sogamoso (820 MW)', 'San Carlos (1240 MW compartido)',
            'Miel I (396 MW)', 'Jaguas (170 MW)',
            'Termocentro gas (300 MW)',
        ],
        'propiedad': 'Brookfield (Canadá)',
        'tipo_propiedad': 'privado',
        'region': 'Santander',
        'share_mercado': 0.142,
    },
    'Celsia': {
        'nombre': 'Celsia S.A. E.S.P. (Grupo Argos)',
        'capacidad_MW': 2175,
        'hidro_MW': 1480, 'termico_MW': 439, 'solar_MW': 256, 'eolico_MW': 0,
        'plantas_principales': [
            'Salvajina (270 MW)', 'Alto/Bajo Tuluá',
            'Tesorito gas (200 MW)', 'Meriléctrica gas (168 MW)',
            'Granjas solares (~256 MW)',
        ],
        'propiedad': 'Grupo Argos',
        'tipo_propiedad': 'privado',
        'region': 'Valle',
        'share_mercado': 0.102,
    },
    'AES Colombia': {
        'nombre': 'AES Colombia',
        'capacidad_MW': 1128,
        'hidro_MW': 1000, 'termico_MW': 0, 'solar_MW': 80, 'eolico_MW': 48,
        'plantas_principales': [
            'Chivor (1000 MW)', 'Castilla Solar (21 MW)',
            'San Fernando Solar (59 MW)',
        ],
        'propiedad': 'AES Corporation (USA)',
        'tipo_propiedad': 'privado',
        'region': 'Cundinamarca',
        'share_mercado': 0.053,
    },
    'TEBSA': {
        'nombre': 'Termobarranquilla S.A.',
        'capacidad_MW': 918,
        'hidro_MW': 0, 'termico_MW': 918, 'solar_MW': 0, 'eolico_MW': 0,
        'plantas_principales': ['TEBSA gas/dual (918 MW)'],
        'propiedad': 'Privado',
        'tipo_propiedad': 'privado',
        'region': 'Costa Caribe',
        'share_mercado': 0.043,
    },
    'Gecelca': {
        'nombre': 'Generadora y Comercializadora del Caribe',
        'capacidad_MW': 709,
        'hidro_MW': 0, 'termico_MW': 709, 'solar_MW': 0, 'eolico_MW': 0,
        'plantas_principales': [
            'Termoguajira carbón/gas (275 MW)',
            'Gecelca 3 y 3.2 carbón (434 MW)',
        ],
        'propiedad': 'Público',
        'tipo_propiedad': 'público',
        'region': 'Costa Caribe',
        'share_mercado': 0.033,
    },
    'Termocandelaria': {
        'nombre': 'Termocandelaria S.C.A.',
        'capacidad_MW': 566,
        'hidro_MW': 0, 'termico_MW': 566, 'solar_MW': 0, 'eolico_MW': 0,
        'plantas_principales': ['Termocandelaria gas CC (566 MW)'],
        'propiedad': 'Privado',
        'tipo_propiedad': 'privado',
        'region': 'Costa Caribe',
        'share_mercado': 0.026,
    },
    'Urrá': {
        'nombre': 'Urrá S.A. E.S.P.',
        'capacidad_MW': 360,
        'hidro_MW': 340, 'termico_MW': 0, 'solar_MW': 20, 'eolico_MW': 0,
        'plantas_principales': ['Urrá I hidro (340 MW)', 'Urrá Solar (20 MW)'],
        'propiedad': 'Público',
        'tipo_propiedad': 'público',
        'region': 'Córdoba',
        'share_mercado': 0.016,
    },
    'Termoflores': {
        'nombre': 'Prime Energía / Termoflores',
        'capacidad_MW': 500,
        'hidro_MW': 0, 'termico_MW': 500, 'solar_MW': 0, 'eolico_MW': 0,
        'plantas_principales': ['Flores I y IV gas CC (500 MW)'],
        'propiedad': 'Privado',
        'tipo_propiedad': 'privado',
        'region': 'Costa Caribe',
        'share_mercado': 0.023,
    },
}


# ─────────────────────────────────────────────────────────────────────
# 2. ACTORES: TRANSMISIÓN
# ─────────────────────────────────────────────────────────────────────

TRANSMISORES = {
    'ISA Intercolombia': {
        'nombre': 'ISA Intercolombia (Ecopetrol)',
        'share_stn': 0.70,
        'km_lineas': 12000,
        'voltajes': ['500 kV', '230 kV'],
        'propiedad': 'Ecopetrol (51.4%)',
        'nota': 'Principal transportador del STN. Ecopetrol adquirió mayoría en 2021.',
    },
    'GEB': {
        'nombre': 'Grupo Energía Bogotá',
        'share_stn': 0.15,
        'km_lineas': 2500,
        'voltajes': ['230 kV', '115 kV'],
        'propiedad': 'Distrito de Bogotá + minoritarios',
    },
    'EPM Transmisión': {
        'nombre': 'EPM (transmisión)',
        'share_stn': 0.05,
        'km_lineas': 800,
        'voltajes': ['230 kV'],
        'propiedad': 'Municipio de Medellín',
    },
    'Transelca': {
        'nombre': 'Transelca S.A.',
        'share_stn': 0.07,
        'km_lineas': 1200,
        'voltajes': ['500 kV', '230 kV'],
        'propiedad': 'ISA Intercolombia',
        'nota': 'Transmisión en la Costa Caribe',
    },
}


# ─────────────────────────────────────────────────────────────────────
# 3. ACTORES: DISTRIBUCIÓN
# ─────────────────────────────────────────────────────────────────────

DISTRIBUIDORES = {
    'Enel Distribución': {
        'nombre': 'Enel Colombia (Codensa)',
        'region': 'Bogotá, Cundinamarca',
        'usuarios': 3_800_000,
        'add': 'Oriente',
    },
    'EPM Distribución': {
        'nombre': 'EPM',
        'region': 'Antioquia',
        'usuarios': 2_600_000,
        'add': 'Centro',
    },
    'Afinia': {
        'nombre': 'Afinia (Grupo EPM)',
        'region': 'Bolívar, Cesar, Córdoba, Sucre',
        'usuarios': 1_700_000,
        'add': 'Caribe',
    },
    'Air-e': {
        'nombre': 'Air-e',
        'region': 'Atlántico, Magdalena, La Guajira',
        'usuarios': 1_300_000,
        'add': 'Caribe',
    },
    'Celsia Distribución': {
        'nombre': 'Celsia (EPSA)',
        'region': 'Valle del Cauca, Tolima',
        'usuarios': 1_500_000,
        'add': 'Occidente',
    },
    'ESSA': {
        'nombre': 'ESSA',
        'region': 'Santander',
        'usuarios': 800_000,
        'add': 'Centro',
    },
    'CENS': {
        'nombre': 'CENS',
        'region': 'Norte de Santander',
        'usuarios': 500_000,
        'add': 'Centro',
    },
    'CHEC': {
        'nombre': 'CHEC (EPM)',
        'region': 'Caldas, Risaralda',
        'usuarios': 400_000,
        'add': 'Centro',
    },
    'Electrohuila': {
        'nombre': 'Electrohuila',
        'region': 'Huila',
        'usuarios': 350_000,
        'add': 'Oriente',
    },
    'CEO': {
        'nombre': 'Compañía Energética de Occidente',
        'region': 'Cauca',
        'usuarios': 300_000,
        'add': 'Occidente',
    },
    'Cedenar': {
        'nombre': 'Cedenar',
        'region': 'Nariño',
        'usuarios': 350_000,
        'add': 'Occidente',
    },
}


# ─────────────────────────────────────────────────────────────────────
# 4. INSTITUCIONES Y MARCO REGULATORIO
# ─────────────────────────────────────────────────────────────────────

INSTITUCIONES = {
    'MME': {
        'nombre': 'Ministerio de Minas y Energía',
        'rol': 'Formulación de política energética',
        'funciones': 'Política pública, metas de transición, diseño de subastas',
        'tipo_tascoi': 'Owner',
    },
    'CREG': {
        'nombre': 'Comisión de Regulación de Energía y Gas',
        'rol': 'Regulador técnico independiente',
        'funciones': 'Tarifas, reglas de mercado, CxC, acceso a redes',
        'tipo_tascoi': 'Owner',
    },
    'UPME': {
        'nombre': 'Unidad de Planeación Minero-Energética',
        'rol': 'Planificador indicativo del sector',
        'funciones': 'Planes de expansión G+T, proyecciones de demanda',
        'tipo_tascoi': 'Owner',
    },
    'XM': {
        'nombre': 'XM S.A. E.S.P.',
        'rol': 'Operador del sistema y administrador del mercado',
        'funciones': 'CND (despacho), ASIC (mercado), LAC (cuentas)',
        'tipo_tascoi': 'Actor',
    },
    'ANLA': {
        'nombre': 'Autoridad Nacional de Licencias Ambientales',
        'rol': 'Licenciamiento ambiental de grandes proyectos',
        'funciones': 'Licencias para G >= 10MW y T >= 198kV',
        'tipo_tascoi': 'Intervener',
    },
    'SIC': {
        'nombre': 'Superintendencia de Industria y Comercio',
        'rol': 'Autoridad de competencia',
        'funciones': 'Antimonopolio, abuso de posición dominante, fusiones',
        'tipo_tascoi': 'Intervener',
    },
    'SSPD': {
        'nombre': 'Superintendencia de Servicios Públicos',
        'rol': 'Supervisión de calidad del servicio',
        'funciones': 'Calidad, protección al usuario, base de datos SUI',
        'tipo_tascoi': 'Intervener',
    },
    'Congreso': {
        'nombre': 'Congreso de la República',
        'rol': 'Legislador',
        'funciones': 'Leyes 142, 143, 1715, 2099',
        'tipo_tascoi': 'Owner',
    },
}


MARCO_REGULATORIO = {
    'leyes': [
        {'norma': 'Ley 142/1994', 'nombre': 'Servicios Públicos Domiciliarios',
         'impacto': 'Marco general: unbundling, subsidios cruzados, libre entrada privada, creación SSPD'},
        {'norma': 'Ley 143/1994', 'nombre': 'Ley Eléctrica',
         'impacto': 'Separación G-T-D-C, mercado mayorista, creación CREG/UPME/CND'},
        {'norma': 'Ley 1715/2014', 'nombre': 'FNCER',
         'impacto': 'Incentivos tributarios para renovables: 50% deducción renta, depreciación acelerada, exención IVA/aranceles'},
        {'norma': 'Ley 2099/2021', 'nombre': 'Transición Energética',
         'impacto': 'Extiende incentivos a H2 verde, almacenamiento, medición inteligente, crea FONENERGIA'},
    ],
    'resoluciones': [
        {'norma': 'CREG 024/1995', 'mecanismo': 'Bolsa de Energía',
         'descripcion': 'Mercado spot horario de precio marginal único'},
        {'norma': 'CREG 071/2006', 'mecanismo': 'Cargo por Confiabilidad (CxC)',
         'descripcion': 'Subastas de OEF: pago fijo por energía firme disponible en sequía'},
        {'norma': 'CREG 015/2018', 'mecanismo': 'Tarifa de distribución',
         'descripcion': 'Metodología tarifaria: WACC, base de activos BRAD, calidad SDIR/STIR'},
        {'norma': 'CREG 030/2018', 'mecanismo': 'Generación distribuida (AGPE)',
         'descripcion': 'Autogeneración a pequeña escala <= 1 MW, net metering'},
        {'norma': 'CREG 140/2017', 'mecanismo': 'Precio de escasez',
         'descripcion': 'Precio techo cuando embalses caen debajo de umbral'},
    ],
    'mecanismos_mercado': [
        {'nombre': 'Bolsa de Energía', 'tipo': 'Spot', 'operador': 'XM',
         'descripcion': 'Despacho económico por mérito. Precio marginal horario.'},
        {'nombre': 'Contratos Bilaterales', 'tipo': 'Forward/PPA', 'operador': 'Agentes',
         'descripcion': 'Cobertura de largo plazo. Regulados (SICEP) y no regulados.'},
        {'nombre': 'Cargo por Confiabilidad', 'tipo': 'Capacidad', 'operador': 'XM/CREG',
         'descripcion': 'Subasta competitiva de OEF (1-20 años). Activado por precio de escasez.'},
        {'nombre': 'Subastas FNCER', 'tipo': 'Renovables', 'operador': 'MME',
         'descripcion': 'PPAs a 15 años para solar/eólica. Subastas 2019, 2021.'},
    ],
}


# ─────────────────────────────────────────────────────────────────────
# 5. ANÁLISIS SISTÉMICO: TASCOI Y CATWOE
# ─────────────────────────────────────────────────────────────────────

TASCOI = {
    'T': {
        'nombre': 'Transformación',
        'definicion': 'El proceso que el sistema ejecuta',
        'aplicacion': ('Convertir recursos energéticos primarios (agua, gas, sol, viento) '
                       'en electricidad entregada al usuario final con calidad, '
                       'confiabilidad y precio justo'),
    },
    'A': {
        'nombre': 'Actores',
        'definicion': 'Quienes ejecutan la transformación',
        'aplicacion': ('Generadores (EPM, Enel, Isagen, Celsia, AES), '
                       'Transmisores (ISA/Ecopetrol, GEB), '
                       'Distribuidores (Codensa, EPM, ESSA, Air-e), '
                       'Comercializadores, XM (operador del sistema)'),
        'agentes': list(GENERADORES.keys()) + list(TRANSMISORES.keys()),
    },
    'S': {
        'nombre': 'Suppliers (Proveedores)',
        'definicion': 'Proveedores de insumos al sistema',
        'aplicacion': ('Ecopetrol (gas), importadores de carbón/gas, '
                       'constructores EPC, fabricantes de equipos, '
                       'banca (BID, Banco Mundial, IFC), consultores'),
    },
    'C': {
        'nombre': 'Customers (Clientes)',
        'definicion': 'Beneficiarios de la transformación',
        'aplicacion': ('~17.9M hogares (estratos 1-6), '
                       'usuarios no regulados (>55 kW), '
                       'exportación a Ecuador'),
        'usuarios_millones': 17.9,
    },
    'O': {
        'nombre': 'Owners (Dueños del sistema)',
        'definicion': 'Quienes pueden cambiar las reglas del sistema',
        'aplicacion': ('MME (política), CREG (regulación), '
                       'Congreso (leyes), UPME (planificación)'),
    },
    'I': {
        'nombre': 'Interveners (Intervinientes)',
        'definicion': 'Influyen sin ser parte formal de la operación',
        'aplicacion': ('ANLA (ambiental), comunidades (consulta previa), '
                       'banca multilateral, SIC (competencia), '
                       'gremios (ACOLGEN, ANDEG), sociedad civil, '
                       'SSPD (supervisión)'),
    },
}

CATWOE = {
    'C': 'Usuarios residenciales (~62% estratos 1-2), comerciales, industriales',
    'A': 'Generadores, transmisores, distribuidores, comercializadores, XM',
    'T': 'Recurso primario -> electricidad confiable en punto de entrega',
    'W': ('La electricidad es un servicio público esencial; el mercado debe '
          'garantizar eficiencia económica Y equidad social'),
    'O': 'Estado colombiano (MME, CREG, Congreso)',
    'E': ('Hidrología variable (El Niño), geografía difícil, '
          'conflicto armado, consulta previa, cambio climático, '
          'compromisos de París, restricciones fiscales'),
}


# ─────────────────────────────────────────────────────────────────────
# 6. DATOS HISTÓRICOS
# ─────────────────────────────────────────────────────────────────────

def datos_historicos_colombia():
    """
    Series anuales del sector eléctrico colombiano 2000-2024.
    Fuentes: XM, UPME (valores aproximados para uso pedagógico).

    Returns
    -------
    pd.DataFrame con columnas por año:
        capacidad_MW, hidro_MW, termico_MW, solar_MW, eolico_MW,
        demanda_max_MW, generacion_GWh, precio_bolsa_prom, evento
    """
    data = {
        'año': list(range(2000, 2025)),
        'capacidad_MW': [
            12810, 13050, 13200, 13300, 13350,
            13420, 13600, 13800, 14000, 14200,
            14416, 14600, 14800, 15000, 15200,
            15732, 16000, 16300, 16600, 17000,
            17485, 18000, 18500, 19500, 21369,
        ],
        'hidro_MW': [
            9870, 9950, 10000, 10050, 10100,
            9100, 9200, 9400, 9600, 9700,
            9440, 9500, 9600, 9700, 9800,
            10500, 10600, 10800, 11000, 11200,
            11940, 12000, 12100, 12200, 12450,
        ],
        'termico_MW': [
            2940, 3100, 3200, 3250, 3250,
            4300, 4380, 4380, 4380, 4480,
            4950, 5080, 5180, 5280, 5380,
            5190, 5350, 5450, 5500, 5600,
            5210, 5300, 5400, 5500, 5894,
        ],
        'solar_MW': [
            0, 0, 0, 0, 0, 10, 10, 10, 10, 10,
            16, 16, 16, 16, 20, 20, 30, 50, 100, 200,
            330, 700, 1000, 1500, 2068,
        ],
        'eolico_MW': [
            0, 0, 0, 0, 0, 20, 20, 20, 20, 20,
            20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
            20, 20, 50, 300, 511,
        ],
        'demanda_max_MW': [
            7800, 7900, 8000, 8100, 8300,
            8620, 8800, 9000, 9100, 9300,
            9480, 9600, 9700, 9800, 9900,
            10120, 10200, 10300, 10400, 10500,
            10330, 10600, 10800, 11000, 11190,
        ],
        'generacion_GWh': [
            42520, 43500, 44800, 46000, 47500,
            49210, 50800, 52500, 54000, 55500,
            56840, 58200, 59800, 61500, 63000,
            66080, 67500, 69000, 70500, 72000,
            70420, 72500, 74800, 77000, 82085,
        ],
        'precio_bolsa_prom': [
            45, 38, 42, 50, 55, 60, 70, 75, 90, 85,
            95, 100, 130, 110, 105, 280, 180, 120, 100, 95,
            80, 90, 150, 200, 180,
        ],
        'evento': [
            '', '', '', '', '',
            'Jepírachi eólico', '', '', '', '',
            '', '', '', '', '',
            'El Niño severo', '2016 post-Niño', '', 'Primera subasta FNCER', '',
            'COVID-19', '', 'Expansión solar', 'Ituango parcial + solar boom', 'Solar 2GW + eólico 0.5GW',
        ],
    }

    return pd.DataFrame(data)


def timeline_regulatorio():
    """
    Hitos regulatorios del sector eléctrico colombiano.

    Returns
    -------
    pd.DataFrame con: año, norma, nombre, impacto_sistemico
    """
    hitos = [
        (1991, 'Constitución 1991', 'Nueva Constitución',
         'Art. 365-370: servicios públicos como finalidad social del Estado'),
        (1992, 'El Apagón', 'Racionamiento de Gaviria',
         '14 meses de apagones (hasta 9h/día). Detonante de la reforma.'),
        (1994, 'Ley 142/1994', 'Servicios Públicos Domiciliarios',
         'Separación de actividades, subsidios cruzados, libre entrada privada'),
        (1994, 'Ley 143/1994', 'Ley Eléctrica',
         'Mercado mayorista, CREG, UPME, separación G-T-D-C'),
        (1995, 'CREG 024/1995', 'Bolsa de Energía',
         'Mercado spot horario con precio marginal único'),
        (1999, 'Cargo por Capacidad', 'Primer mecanismo de confiabilidad',
         'Pago fijo por MW disponible (reemplazado en 2006)'),
        (2006, 'CREG 071/2006', 'Cargo por Confiabilidad (CxC)',
         'Subastas de Obligaciones de Energía Firme (OEF). Transformación del mercado.'),
        (2014, 'Ley 1715/2014', 'FNCER',
         'Incentivos tributarios para renovables no convencionales'),
        (2015, 'El Niño 2015-16', 'Evento climático severo',
         'Precios ~800 COP/kWh. CxC probado exitosamente (sin racionamiento).'),
        (2018, 'CREG 030/2018', 'Generación distribuida',
         'Net metering para autogeneración <= 1 MW'),
        (2019, 'Primera subasta FNCER', 'Subastas renovables MME',
         'Contratos a 15 años para solar y eólica a gran escala'),
        (2021, 'Ley 2099/2021', 'Transición Energética',
         'H2 verde, almacenamiento, medición inteligente, FONENERGIA'),
        (2021, 'Ecopetrol adquiere ISA', 'Reestructuración',
         'Ecopetrol compra 51.4% de ISA. Integración energética estatal.'),
        (2024, 'Solar 2 GW', 'Hito renovable',
         '2,068 MW solares instalados. 1,380 MW agregados solo en 2024.'),
    ]

    return pd.DataFrame(hitos, columns=['año', 'norma', 'nombre', 'impacto_sistemico'])


# ─────────────────────────────────────────────────────────────────────
# 7. FÓRMULA TARIFARIA
# ─────────────────────────────────────────────────────────────────────

FORMULA_TARIFARIA = {
    'G': {'nombre': 'Generación', 'share_pct': 37, 'tipo': 'Competitivo',
           'descripcion': 'Costo promedio ponderado de contratos y bolsa'},
    'T': {'nombre': 'Transmisión', 'share_pct': 6, 'tipo': 'Regulado',
           'descripcion': 'Cargo STN uniforme nacional'},
    'D': {'nombre': 'Distribución', 'share_pct': 37, 'tipo': 'Regulado',
           'descripcion': 'Cargo STR+SDL regional por ADD (BRAD + WACC)'},
    'Cv': {'nombre': 'Comercialización', 'share_pct': 9, 'tipo': 'Regulado',
            'descripcion': 'Margen minorista: facturación, medición, cartera'},
    'PR': {'nombre': 'Pérdidas', 'share_pct': 7, 'tipo': 'Regulado',
            'descripcion': 'Pérdidas técnicas y no técnicas reconocidas'},
    'R': {'nombre': 'Restricciones', 'share_pct': 4, 'tipo': 'Regulado',
           'descripcion': 'Generación fuera de mérito por congestión de transmisión'},
}


SUBSIDIOS_ESTRATO = {
    1: {'nombre': 'Bajo-Bajo', 'share_usuarios': 0.21, 'subsidio_pct': 60},
    2: {'nombre': 'Bajo', 'share_usuarios': 0.41, 'subsidio_pct': 50},
    3: {'nombre': 'Medio-Bajo', 'share_usuarios': 0.21, 'subsidio_pct': 15},
    4: {'nombre': 'Medio', 'share_usuarios': 0.09, 'subsidio_pct': 0},
    5: {'nombre': 'Medio-Alto', 'share_usuarios': 0.035, 'subsidio_pct': -20},
    6: {'nombre': 'Alto', 'share_usuarios': 0.025, 'subsidio_pct': -20},
}


# ─────────────────────────────────────────────────────────────────────
# 8. GRAFOS DEL SISTEMA
# ─────────────────────────────────────────────────────────────────────

def crear_red_cadena_valor():
    """
    Grafo bipartito: empresas x eslabones de la cadena de valor.
    Muestra integración vertical y concentración.

    Returns
    -------
    nx.DiGraph con nodos tipo 'empresa' y 'eslabon', aristas de participación
    """
    G = nx.DiGraph()

    # Eslabones
    eslabones = ['Generación', 'Transmisión', 'Distribución', 'Comercialización']
    for e in eslabones:
        G.add_node(e, tipo='eslabon', bipartite=0)

    # Empresas y sus participaciones
    participaciones = {
        'EPM': ['Generación', 'Distribución', 'Comercialización'],
        'Enel': ['Generación', 'Distribución', 'Comercialización'],
        'Isagen': ['Generación', 'Comercialización'],
        'Celsia': ['Generación', 'Distribución', 'Comercialización'],
        'AES': ['Generación', 'Comercialización'],
        'ISA/Ecopetrol': ['Transmisión'],
        'GEB': ['Transmisión', 'Distribución'],
        'TEBSA': ['Generación'],
        'Gecelca': ['Generación', 'Comercialización'],
        'Urrá': ['Generación'],
        'Air-e': ['Distribución', 'Comercialización'],
        'Afinia (EPM)': ['Distribución', 'Comercialización'],
        'ESSA': ['Distribución', 'Comercialización'],
        'CHEC (EPM)': ['Distribución', 'Comercialización'],
        'Vatia': ['Comercialización'],
    }

    for empresa, eslabs in participaciones.items():
        cap = GENERADORES.get(empresa, {}).get('capacidad_MW', 0)
        G.add_node(empresa, tipo='empresa', bipartite=1,
                   capacidad_MW=cap)
        for esl in eslabs:
            G.add_edge(empresa, esl)

    return G


def crear_red_institucional():
    """
    Red TASCOI: actores institucionales y sus relaciones.
    Nodos = instituciones, aristas = relaciones de regulación/supervisión.

    Returns
    -------
    nx.DiGraph con atributos de rol TASCOI
    """
    G = nx.DiGraph()

    for sigla, info in INSTITUCIONES.items():
        G.add_node(sigla, **info)

    # Relaciones institucionales
    relaciones = [
        ('Congreso', 'MME', 'legisla_para'),
        ('MME', 'CREG', 'nombra_comisionados'),
        ('MME', 'UPME', 'define_politica'),
        ('CREG', 'XM', 'regula'),
        ('CREG', 'Generadores', 'regula_mercado'),
        ('CREG', 'Distribuidores', 'fija_tarifas'),
        ('UPME', 'XM', 'planifica_expansion'),
        ('XM', 'Generadores', 'despacha'),
        ('XM', 'Transmisores', 'opera_red'),
        ('ANLA', 'Generadores', 'licencia_ambiental'),
        ('SIC', 'Generadores', 'vigila_competencia'),
        ('SIC', 'Comercializadores', 'vigila_competencia'),
        ('SSPD', 'Distribuidores', 'supervisa_calidad'),
        ('SSPD', 'Comercializadores', 'supervisa_servicio'),
    ]

    # Agregar nodos de categoría si no existen
    for cat in ['Generadores', 'Distribuidores', 'Transmisores', 'Comercializadores']:
        if cat not in G:
            G.add_node(cat, nombre=cat, rol='Agente del mercado',
                       tipo_tascoi='Actor')

    for origen, destino, relacion in relaciones:
        G.add_edge(origen, destino, relacion=relacion)

    return G


def crear_red_mercado_mayorista():
    """
    Red del mercado de energía mayorista (MEM).
    Generadores conectados a XM (bolsa) y a comercializadores (contratos).

    Returns
    -------
    nx.DiGraph con flujos de energía y pagos
    """
    G = nx.DiGraph()

    # XM como nodo central
    G.add_node('XM (Bolsa)', tipo='operador', capacidad_MW=0)

    # Generadores
    for gen, info in GENERADORES.items():
        G.add_node(gen, tipo='generador', **{k: v for k, v in info.items()
                   if k in ('capacidad_MW', 'region', 'share_mercado')})
        G.add_edge(gen, 'XM (Bolsa)', tipo='oferta_bolsa',
                   capacidad_MW=info['capacidad_MW'])

    # Comercializadores principales
    comers = ['EPM Comercial', 'Enel Comercial', 'Celsia Comercial',
              'Vatia', 'Isagen Comercial', 'Air-e Comercial']
    for com in comers:
        G.add_node(com, tipo='comercializador')
        G.add_edge('XM (Bolsa)', com, tipo='compra_bolsa')

    # Contratos bilaterales (algunos ejemplos)
    contratos = [
        ('EPM', 'EPM Comercial'),
        ('Enel Colombia', 'Enel Comercial'),
        ('Celsia', 'Celsia Comercial'),
        ('Isagen', 'Isagen Comercial'),
        ('Isagen', 'Vatia'),
    ]
    for gen, com in contratos:
        G.add_edge(gen, com, tipo='contrato_bilateral')

    return G


# ─────────────────────────────────────────────────────────────────────
# 9. FUNCIONES DE RESUMEN
# ─────────────────────────────────────────────────────────────────────

def resumen_generacion():
    """DataFrame resumen de generadores por capacidad."""
    rows = []
    for gen, info in GENERADORES.items():
        rows.append({
            'Empresa': gen,
            'Capacidad (MW)': info['capacidad_MW'],
            'Hidro (MW)': info['hidro_MW'],
            'Térmico (MW)': info['termico_MW'],
            'Solar (MW)': info['solar_MW'],
            'Eólico (MW)': info['eolico_MW'],
            'Propiedad': info['propiedad'],
            'Share (%)': round(info['share_mercado'] * 100, 1),
        })
    df = pd.DataFrame(rows)
    df = df.sort_values('Capacidad (MW)', ascending=False).reset_index(drop=True)
    return df


def resumen_distribucion():
    """DataFrame resumen de distribuidores por usuarios."""
    rows = []
    for dist, info in DISTRIBUIDORES.items():
        rows.append({
            'Operador': info['nombre'],
            'Región': info['region'],
            'Usuarios': info['usuarios'],
            'ADD': info['add'],
        })
    df = pd.DataFrame(rows)
    df = df.sort_values('Usuarios', ascending=False).reset_index(drop=True)
    return df


def resumen_tascoi():
    """DataFrame del análisis TASCOI."""
    rows = []
    for letra, info in TASCOI.items():
        rows.append({
            'Letra': letra,
            'Elemento': info['nombre'],
            'Definición': info['definicion'],
            'Aplicación al SIN': info['aplicacion'],
        })
    return pd.DataFrame(rows)


def print_sistema():
    """Imprime un resumen ejecutivo del sistema eléctrico colombiano."""
    total = sum(g['capacidad_MW'] for g in GENERADORES.values())
    hidro = sum(g['hidro_MW'] for g in GENERADORES.values())
    termico = sum(g['termico_MW'] for g in GENERADORES.values())
    solar = sum(g['solar_MW'] for g in GENERADORES.values())
    eolico = sum(g['eolico_MW'] for g in GENERADORES.values())
    usuarios = sum(d['usuarios'] for d in DISTRIBUIDORES.values())

    print("=" * 65)
    print("  SISTEMA ELÉCTRICO COLOMBIANO — Resumen 2024")
    print("=" * 65)
    print(f"\n  Capacidad instalada total: {total:,.0f} MW")
    print(f"    Hidro:    {hidro:,.0f} MW ({hidro/total*100:.1f}%)")
    print(f"    Térmico:  {termico:,.0f} MW ({termico/total*100:.1f}%)")
    print(f"    Solar:    {solar:,.0f} MW ({solar/total*100:.1f}%)")
    print(f"    Eólico:   {eolico:,.0f} MW ({eolico/total*100:.1f}%)")
    print(f"\n  Generadores principales: {len(GENERADORES)}")
    print(f"  Distribuidores: {len(DISTRIBUIDORES)}")
    print(f"  Usuarios totales: ~{usuarios/1e6:.1f} millones")
    print(f"\n  Demanda máxima 2024: ~11,190 MW")
    print(f"  Generación 2024: ~82,085 GWh")
    print("=" * 65)
