"""
data_loader.py — Carga de datos reales del SIN colombiano.

Fuente: API pública de XM (servapibi.xm.com.co).
Datos descargados offline como CSVs en notebooks/data/.

Cada función devuelve un DataFrame limpio con tipos correctos,
listo para análisis. Si los CSVs no existen, levanta FileNotFoundError
con instrucciones de descarga.
"""

import pandas as pd
import numpy as np
import os

# Ruta a la carpeta de datos (relativa a este módulo)
_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def _resolve(filename):
    """Resuelve la ruta absoluta de un archivo de datos."""
    path = os.path.join(_DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"No se encontró {filename} en {_DATA_DIR}.\n"
            f"Ejecuta el script de descarga: scratch/download_xm_data.py"
        )
    return path


# ─────────────────────────────────────────────────────────
# PRECIO DE BOLSA
# ─────────────────────────────────────────────────────────

def precio_bolsa_mensual():
    """Precio promedio mensual de bolsa nacional (COP/kWh), 2000-2025.
    
    Returns:
        DataFrame con columnas: year, month, monthly_avg, monthly_max, monthly_min, days
    """
    df = pd.read_csv(_resolve('xm_precio_bolsa_mensual.csv'))
    df['fecha'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    return df


def precio_bolsa_anual():
    """Precio promedio anual de bolsa nacional (COP/kWh), 2000-2025.
    
    Returns:
        DataFrame con columnas: year, precio_promedio, precio_max, precio_min
    """
    return pd.read_csv(_resolve('xm_precio_bolsa_anual.csv'))


def precio_bolsa_diario():
    """Precio de bolsa por hora y día (COP/kWh), 2000-2025.
    
    Cada fila es un día; columnas Values_Hour01..Values_Hour24.
    
    Returns:
        DataFrame con columnas: Date, Values_Hour01..24, daily_avg, daily_max, daily_min
    """
    df = pd.read_csv(_resolve('xm_precio_bolsa_raw.csv'))
    hour_cols = [c for c in df.columns if c.startswith('Values_Hour')]
    for c in hour_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df['daily_avg'] = df[hour_cols].mean(axis=1)
    df['daily_max'] = df[hour_cols].max(axis=1)
    df['daily_min'] = df[hour_cols].min(axis=1)
    df['fecha'] = pd.to_datetime(df['Date'])
    return df


# ─────────────────────────────────────────────────────────
# GENERACIÓN
# ─────────────────────────────────────────────────────────

def generacion_mensual():
    """Generación total mensual del SIN (kWh), 2000-2025.
    
    Returns:
        DataFrame con columnas: year, month, monthly_avg, monthly_max, monthly_min, monthly_sum, days
    """
    df = pd.read_csv(_resolve('xm_generacion_mensual.csv'))
    df['fecha'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    df['generacion_GWh'] = df['monthly_sum'] / 1e6
    return df


def generacion_anual():
    """Generación total anual del SIN (GWh), 2000-2025.
    
    Returns:
        DataFrame con columnas: year, generacion_GWh
    """
    return pd.read_csv(_resolve('xm_generacion_anual.csv'))


# ─────────────────────────────────────────────────────────
# DEMANDA
# ─────────────────────────────────────────────────────────

def demanda_max_anual():
    """Demanda máxima de potencia anual (kW → MW), 2000-2025.
    
    Returns:
        DataFrame con columnas: year, demanda_max_MW
    """
    df = pd.read_csv(_resolve('xm_demanda_max_anual.csv'))
    # Los datos vienen en kW, convertir a MW
    df['demanda_max_MW'] = df['demanda_max_MW'] / 1000
    return df


def demanda_comercial_anual():
    """Demanda comercial total anual (GWh), 2010-2025.
    
    Returns:
        DataFrame con columnas: year, demanda_GWh
    """
    return pd.read_csv(_resolve('xm_demanda_comercial_anual.csv'))


# ─────────────────────────────────────────────────────────
# EMBALSES (HIDROLOGÍA)
# ─────────────────────────────────────────────────────────

def embalses_diario():
    """Nivel agregado diario de embalses (fracción 0-1), 2003-2025.
    
    Returns:
        DataFrame con columnas: fecha, embalse_pct (0-100)
    """
    df = pd.read_csv(_resolve('xm_embalses_pct_raw.csv'))
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df['fecha'] = pd.to_datetime(df['Date'])
    df['embalse_pct'] = df['Value'] * 100  # 0.74 → 74%
    return df[['fecha', 'embalse_pct']].dropna()


def embalses_mensual():
    """Nivel promedio mensual de embalses (%), 2003-2025.
    
    Returns:
        DataFrame con columnas: year, month, embalse_avg, embalse_min
    """
    df = pd.read_csv(_resolve('xm_embalses_pct_mensual.csv'))
    # Convertir a porcentaje si viene como fracción
    for col in ['embalse_avg', 'embalse_min']:
        if col in df.columns and df[col].max() < 2:
            df[col] = df[col] * 100
    df['fecha'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    return df


# ─────────────────────────────────────────────────────────
# PLANTAS / RECURSOS
# ─────────────────────────────────────────────────────────

def plantas():
    """Listado de plantas/recursos del SIN con atributos.
    
    Returns:
        DataFrame con columnas: Code, Name, Type, Disp, RecType,
                                CompanyCode, EnerSource, OperStartdate, State
    """
    df = pd.read_csv(_resolve('xm_recursos_plantas.csv'))
    # Normalizar tipos
    if 'Type' in df.columns:
        df['Type'] = df['Type'].str.upper()
    if 'OperStartdate' in df.columns:
        df['OperStartdate'] = pd.to_datetime(df['OperStartdate'], errors='coerce')
    return df


def plantas_resumen():
    """Resumen de plantas por tipo y fuente de energía.
    
    Returns:
        DataFrame con columnas: Type, EnerSource, n_plantas
    """
    df = plantas()
    return (df.groupby(['Type', 'EnerSource'])
              .size()
              .reset_index(name='n_plantas')
              .sort_values('n_plantas', ascending=False))


def capacidad_por_recurso():
    """Capacidad estimada por recurso (MW) con atributos de planta.
    
    La capacidad se estima como el máximo de generación horaria
    observada en 2024 (proxy para capacidad instalada).
    
    Returns:
        DataFrame con columnas: Code, Name, Type, EnerSource, CompanyCode,
                                capacidad_MW, gen_anual_GWh, factor_planta
    """
    return pd.read_csv(_resolve('xm_capacidad_por_recurso.csv'))


def capacidad_por_tipo():
    """Capacidad agregada por tipo de tecnología.
    
    Returns:
        DataFrame con columnas: Type, n_plantas, capacidad_MW, share_capacidad,
                                capacidad_promedio_MW, factor_planta_avg
    """
    df = capacidad_por_recurso()
    result = df.groupby('Type').agg(
        n_plantas=('Code', 'count'),
        capacidad_MW=('capacidad_MW', 'sum'),
        capacidad_promedio_MW=('capacidad_MW', 'mean'),
        factor_planta_avg=('factor_planta', 'mean')
    ).sort_values('capacidad_MW', ascending=False).reset_index()
    result['share_capacidad'] = result['capacidad_MW'] / result['capacidad_MW'].sum() * 100
    return result


def capacidad_por_fuente():
    """Capacidad agregada por fuente de energía.
    
    Returns:
        DataFrame con columnas: EnerSource, n_plantas, capacidad_MW, share_capacidad
    """
    df = capacidad_por_recurso()
    result = df.groupby('EnerSource').agg(
        n_plantas=('Code', 'count'),
        capacidad_MW=('capacidad_MW', 'sum'),
    ).sort_values('capacidad_MW', ascending=False).reset_index()
    result['share_capacidad'] = result['capacidad_MW'] / result['capacidad_MW'].sum() * 100
    return result


# ─────────────────────────────────────────────────────────
# SERIE INTEGRADA (para calibración del modelo SD)
# ─────────────────────────────────────────────────────────

def serie_anual_integrada():
    """Serie anual integrada con precio, generación, demanda máxima.
    
    Combina todas las fuentes en un solo DataFrame anual para
    facilitar la calibración del modelo de dinámica de sistemas.
    
    Returns:
        DataFrame con columnas: year, precio_avg, precio_max, precio_min,
                                generacion_GWh, demanda_max_MW, demanda_GWh,
                                margen_reserva_pct
    """
    # Precio
    precio = precio_bolsa_anual()
    
    # Generación
    gen = generacion_anual()
    
    # Demanda max
    try:
        dem_max = demanda_max_anual()
    except FileNotFoundError:
        dem_max = pd.DataFrame()
    
    # Demanda comercial
    try:
        dem_com = demanda_comercial_anual()
    except FileNotFoundError:
        dem_com = pd.DataFrame()
    
    # Merge
    df = precio.rename(columns={
        'precio_promedio': 'precio_avg',
    })
    df = df.merge(gen, on='year', how='outer')
    
    if len(dem_max) > 0:
        df = df.merge(dem_max, on='year', how='left')
    
    if len(dem_com) > 0:
        df = df.merge(dem_com, on='year', how='left')
    
    # Calcular margen de reserva aproximado
    # diferencia_contable_pct = (generación_disponible - demanda) / demanda
    # Para esto necesitamos restar la demanda comercial de la generación
    if 'demanda_GWh' in df.columns and 'generacion_GWh' in df.columns:
        mask = df['demanda_GWh'].notna() & (df['demanda_GWh'] > 0)
        df.loc[mask, 'diferencia_contable_pct'] = (
            (df.loc[mask, 'generacion_GWh'] - df.loc[mask, 'demanda_GWh']) / df.loc[mask, 'demanda_GWh']
        ) * 100
    
    # Llenar NaN si quedan en años extremos
    df['diferencia_contable_pct'] = df['diferencia_contable_pct'].fillna(10.0)
    
    return df.sort_values('year').reset_index(drop=True)
