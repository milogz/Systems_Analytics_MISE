"""Transformaciones de extractos locales atribuidos a XM. Unidades explícitas."""
from pathlib import Path
import calendar
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'datos' / 'originales'
HORAS = [f'Values_Hour{i:02d}' for i in range(1, 25)]

def leer_diario(archivo, horario=True):
    df = pd.read_csv(RAW / archivo)
    df['fecha'] = pd.to_datetime(df['Date'], errors='raise')
    if df.fecha.duplicated().any():
        raise ValueError(f'{archivo}: varias filas por día; revisar universo antes de agregar')
    cols = HORAS if horario else ['Value']
    if not set(cols) <= set(df):
        raise ValueError(f'{archivo}: esquema incompleto')
    df[cols] = df[cols].apply(pd.to_numeric, errors='raise')
    if not np.isfinite(df[cols].to_numpy()).all():
        raise ValueError(f'{archivo}: faltantes/no finitos; no se imputan silenciosamente')
    return df.sort_values('fecha').reset_index(drop=True)

def cobertura(df):
    rows=[]
    for year,g in df.groupby(df.fecha.dt.year):
        expected=366 if calendar.isleap(int(year)) else 365
        rows.append({'anio':int(year),'dias_observados':len(g),'dias_calendario':expected,
                     'completo':len(g)==expected,'inicio':str(g.fecha.min().date()),
                     'fin':str(g.fecha.max().date())})
    return pd.DataFrame(rows)

def anios_completos(df, hasta=2024):
    allowed=cobertura(df).query('completo and anio <= @hasta').anio
    return df[df.fecha.dt.year.isin(allowed)].copy()

def precio_anual(hasta=2024):
    df=anios_completos(leer_diario('xm_precio_bolsa_raw.csv'),hasta)
    # Media de 24 cotizaciones por día. No está ponderada por energía vendida.
    df['precio_COP_kWh_nominal']=df[HORAS].mean(axis=1)
    return df.groupby(df.fecha.dt.year.rename('anio')).agg(
        precio_COP_kWh_nominal=('precio_COP_kWh_nominal','mean'),
        dias=('fecha','size')).reset_index()

def energia_anual(archivo='xm_generacion_raw.csv',hasta=2024):
    df=anios_completos(leer_diario(archivo),hasta)
    if (df[HORAS]<0).any().any():
        raise ValueError('Energía negativa: revisar definición del indicador')
    # La fuente declara energía de cada hora en kWh: suma, no promedio.
    df['energia_GWh']=df[HORAS].sum(axis=1)/1e6
    result=df.groupby(df.fecha.dt.year.rename('anio')).agg(
        energia_GWh=('energia_GWh','sum'),dias=('fecha','size')).reset_index()
    result['horas']=result.dias*24
    result['potencia_media_MW']=result.energia_GWh*1000/result.horas
    return result

def demanda_pico(hasta=2024):
    df=anios_completos(leer_diario('xm_demanda_max_raw.csv',False),hasta)
    # Value es kW de máxima potencia diaria; el máximo anual se convierte UNA vez.
    df['demanda_pico_MW']=df.Value/1000
    return df.groupby(df.fecha.dt.year.rename('anio')).demanda_pico_MW.max().reset_index()

def balance_descriptivo(hasta=2024):
    gen=energia_anual(hasta=hasta).rename(columns={'energia_GWh':'generacion_GWh'})
    dem=energia_anual('xm_demanda_comercial_raw.csv',hasta).rename(columns={'energia_GWh':'demanda_comercial_GWh'})
    df=gen.merge(dem[['anio','demanda_comercial_GWh']],on='anio',validate='one_to_one')
    df['diferencia_contable_GWh']=df.generacion_GWh-df.demanda_comercial_GWh
    # No inferimos margen de reserva ni desabastecimiento de esta diferencia.
    return df.merge(demanda_pico(hasta),on='anio',validate='one_to_one')

def precio_embalse_mensual(hasta=2024):
    p=anios_completos(leer_diario('xm_precio_bolsa_raw.csv'),hasta)
    e=anios_completos(leer_diario('xm_embalses_pct_raw.csv',False),hasta)
    if not e.Value.between(0,1).all():
        raise ValueError('Se esperaba fracción 0–1 de embalse; no se adivina la escala')
    p['precio_nominal_COP_kWh']=p[HORAS].mean(axis=1)
    e['embalse_pct']=e.Value*100
    p=p.groupby(p.fecha.dt.to_period('M')).precio_nominal_COP_kWh.mean()
    e=e.groupby(e.fecha.dt.to_period('M')).embalse_pct.mean()
    return pd.concat([p,e],axis=1,join='inner').dropna().rename_axis('mes').reset_index()

def proxies_recursos():
    df=pd.read_csv(RAW/'xm_capacidad_por_recurso.csv')
    df=df.rename(columns={'capacidad_MW':'max_produccion_horaria_observada_MW',
                          'gen_anual_GWh':'produccion_2024_GWh'})
    # Retiramos el factor de planta heredado: su denominador no es CEN validada.
    df=df.drop(columns=['factor_planta'],errors='ignore')
    df['Type']=df.Type.fillna('SIN_CLASIFICAR')
    df['CompanyCode']=df.CompanyCode.fillna('SIN_IDENTIFICAR')
    return df

def estimar_tendencia_demanda(fin_entrenamiento=2018,hasta=2024):
    df=demanda_pico(hasta)
    train=df[df.anio<=fin_entrenamiento].copy();test=df[df.anio>fin_entrenamiento].copy()
    if len(train)<3 or len(test)<1:
        raise ValueError('Se requiere entrenamiento y período de prueba separados')
    origin=int(train.anio.min())
    slope,intercept=np.polyfit(train.anio-origin,np.log(train.demanda_pico_MW),1)
    df['prediccion_MW']=np.exp(intercept+slope*(df.anio-origin))
    df['particion']=np.where(df.anio<=fin_entrenamiento,'entrenamiento','prueba')
    df['error_MW']=df.prediccion_MW-df.demanda_pico_MW
    metrics={k:float(np.abs(g.error_MW).mean()) for k,g in df.groupby('particion')}
    return df,{'crecimiento_estimado_anual':float(np.expm1(slope)),
               'MAE_MW':metrics,'fin_entrenamiento':fin_entrenamiento}
