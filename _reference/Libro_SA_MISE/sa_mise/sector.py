"""Experimentos sectoriales docentes y análisis descriptivo; no modelo del SIN."""
import numpy as np
import pandas as pd
from . import datos

def perfiles_horarios(anio=2024):
    """Alineación diaria exacta; energía horaria kWh a potencia media horaria MW."""
    p=datos.anios_completos(datos.leer_diario('xm_precio_bolsa_raw.csv'),anio)
    d=datos.anios_completos(datos.leer_diario('xm_demanda_comercial_raw.csv'),anio)
    p=p[p.fecha.dt.year==anio].set_index('fecha');d=d[d.fecha.dt.year==anio].set_index('fecha')
    if p.empty or not p.index.equals(d.index):raise ValueError('Año completo y fechas alineadas requeridos')
    energy=d[datos.HORAS].to_numpy();price=p[datos.HORAS].to_numpy()
    return pd.DataFrame({'hora_intervalo':np.arange(1,25),
        'potencia_media_demanda_comercial_MW':energy.mean(axis=0)/1000,
        'precio_medio_nominal_COP_kWh':price.mean(axis=0)}),{
        'dias':len(p),'precio_medio_nominal_COP_kWh':float(price.mean()),
        'precio_ponderado_demanda_comercial_COP_kWh':float((price*energy).sum()/energy.sum())}

def asociacion_hidrologica():
    """Asociación mensual observada y con efectos aditivos de año/mes retirados."""
    df=datos.precio_embalse_mensual()
    if (df.precio_nominal_COP_kWh<=0).any():raise ValueError('Log requiere precios positivos')
    df['anio']=df.mes.dt.year;df['mes_calendario']=df.mes.dt.month
    df['log_precio']=np.log(df.precio_nominal_COP_kWh)
    controles=pd.get_dummies(df[['anio','mes_calendario']].astype(str),drop_first=True,dtype=float)
    X=np.column_stack([np.ones(len(df)),controles.to_numpy()])
    for variable in ['log_precio','embalse_pct']:
        y=df[variable].to_numpy();df[variable+'_residuo']=y-X@np.linalg.lstsq(X,y,rcond=None)[0]
    resumen={'meses':len(df),
      'correlacion_bruta':float(df.log_precio.corr(df.embalse_pct)),
      'correlacion_residual':float(df.log_precio_residuo.corr(df.embalse_pct_residuo)),
      'interpretacion':'Asociación; controles aditivos no identifican causalidad ni corrigen toda no estacionariedad'}
    return df,resumen

def aportes_docentes(n=24):
    if n<1:raise ValueError('Horizonte positivo')
    return 90000*(1+.65*np.sin(2*np.pi*(np.arange(n)-3)/12))

def sistema_docente(aportes=None,solar_extra_MW=0.,termica_disponible=.9,
                    reduccion_demanda=0.,reserva_MWh=0.,stock_inicial=120000.):
    """Balance mensual en MWh equivalentes. Reserva guía hidro; no despacho óptimo.
    La reserva se aplica al agua disponible antes de turbinar; térmica cubre después.
    Aportes sintéticos nunca se escalan desde porcentaje observado de embalse.
    """
    a=aportes_docentes() if aportes is None else np.asarray(aportes,float)
    if a.ndim!=1 or len(a)<1 or not np.isfinite(a).all() or (a<0).any():raise ValueError('Aportes inválidos')
    solar_adicional=np.broadcast_to(np.asarray(solar_extra_MW,float),a.shape)
    if not np.isfinite(solar_adicional).all() or (solar_adicional<0).any() or not 0<=termica_disponible<=1 or not 0<=reduccion_demanda<1:
        raise ValueError('Intervención fuera de dominio')
    if not 0<=stock_inicial<=240000 or not 0<=reserva_MWh<=240000:raise ValueError('Stock/reserva inválido')
    rows=[];stock=float(stock_inicial)
    for fecha,aporte,adicional in zip(pd.date_range('2024-01-01',periods=len(a),freq='MS'),a,solar_adicional):
        horas=fecha.days_in_month*24;demanda_bruta=160*horas
        ahorro=demanda_bruta*reduccion_demanda;demanda=demanda_bruta-ahorro
        solar=min(demanda,(30+adicional)*.2*horas)
        agua=stock+aporte
        hidro=min(max(0,agua-reserva_MWh),100*horas,max(0,demanda-solar))
        termica=min(90*termica_disponible*horas,max(0,demanda-solar-hidro))
        faltante=max(0,demanda-solar-hidro-termica)
        vertimiento=max(0,agua-hidro-240000);fin=agua-hidro-vertimiento
        rows.append({'mes':str(fecha.date()),'horas':horas,'stock_inicial_MWh_eq':stock,
          'aporte_MWh_eq':aporte,'hidro_MWh':hidro,'solar_MWh':solar,'termica_MWh':termica,
          'demanda_bruta_MWh':demanda_bruta,'ahorro_MWh':ahorro,'demanda_neta_MWh':demanda,
          'faltante_MWh':faltante,'vertimiento_MWh_eq':vertimiento,'stock_final_MWh_eq':fin,
          'costo_variable_COP':hidro*30000+termica*350000,
          'emisiones_termicas_tCO2':termica*.45})
        stock=fin
    return pd.DataFrame(rows)

def comparar_respuestas():
    """Misma base, 24 meses, escenarios sin probabilidades. Costos docentes sin VPN.
    Costos comparados: variable + implementación. No incluye toda infraestructura,
    valor terminal, costo del faltante ni optimización. No llama costo social a suma.
    """
    a=aportes_docentes()
    escenarios={'Referencia':(a,.9),'Aportes al 45%':(a*.45,.9),
                 'Sequía y térmica al 55%':(a*.45,.55),'Mismo aporte desplazado':(np.roll(a,4),.9)}
    alternativas={
      'Base':({},0.),
      'Solar adicional 20 MW':({'solar_extra_MW':20.},20*3.2e9+2*20*45e6),
      'Reducción de demanda 5%':({'reduccion_demanda':.05},12e9),
      'Reserva operativa 60000 MWh':({'reserva_MWh':60000.},0.),
      'Solar + reducción de demanda':({'solar_extra_MW':20.,'reduccion_demanda':.05},20*3.2e9+2*20*45e6+12e9)}
    rows=[]
    for escenario,(aportes,disponibilidad) in escenarios.items():
        for alternativa,(parametros,costo) in alternativas.items():
            d=sistema_docente(aportes,termica_disponible=disponibilidad,**parametros)
            rows.append({'escenario':escenario,'alternativa':alternativa,
              'faltante_MWh':d.faltante_MWh.sum(),'ahorro_MWh':d.ahorro_MWh.sum(),
              'termica_MWh':d.termica_MWh.sum(),'stock_final_MWh_eq':d.stock_final_MWh_eq.iloc[-1],
              'vertimiento_MWh_eq':d.vertimiento_MWh_eq.sum(),
              'costo_variable_COP':d.costo_variable_COP.sum(),'costo_intervencion_COP':costo,
              'costo_parcial_COP':d.costo_variable_COP.sum()+costo,
              'emisiones_termicas_tCO2':d.emisiones_termicas_tCO2.sum()})
    return pd.DataFrame(rows)
