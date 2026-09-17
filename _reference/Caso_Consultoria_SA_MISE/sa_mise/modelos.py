"""Modelos ilustrativos: topología/DC, embalse energético, inversión y negocio."""
import numpy as np
import pandas as pd
import networkx as nx
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit

def red_docente():
    """5 barras ficticias; x pu en base 100 MVA; límite MW de ejercicio."""
    g=nx.Graph()
    for a,b,x,limit in [('A','B',.10,65),('A','C',.20,65),('B','C',.15,40),
                        ('B','D',.20,55),('C','E',.10,65),('D','E',.15,50)]:
        g.add_edge(a,b,x_pu=x,limite_MW=limit)
    return g,{'A':100.,'B':0.,'C':10.,'D':-55.,'E':-55.}

def flujo_dc(g,inyecciones,base_MVA=100.):
    """Caso balanceado conectado. DC sin pérdidas, sin Q ni límites de tensión."""
    if not nx.is_connected(g):raise ValueError('Islas: se requiere balance por isla y redispatch')
    nodes=list(g);p=np.array([inyecciones[n] for n in nodes],float)
    if not np.isclose(p.sum(),0,atol=1e-8):raise ValueError('Inyecciones no balanceadas')
    if base_MVA<=0:raise ValueError('Base positiva requerida')
    matrix=np.zeros((len(nodes),len(nodes)))
    for a,b,d in g.edges(data=True):
        if d['x_pu']<=0 or d['limite_MW']<=0:raise ValueError('Reactancia/límite inválido')
        i,j=nodes.index(a),nodes.index(b);v=1/d['x_pu']
        matrix[i,i]+=v;matrix[j,j]+=v;matrix[i,j]-=v;matrix[j,i]-=v
    theta=np.zeros(len(nodes));theta[1:]=np.linalg.solve(matrix[1:,1:],p[1:]/base_MVA)
    rows=[]
    for a,b,d in g.edges(data=True):
        f=base_MVA*(theta[nodes.index(a)]-theta[nodes.index(b)])/d['x_pu']
        rows.append({'origen':a,'destino':b,'flujo_MW':f,'limite_MW':d['limite_MW'],
                     'carga_pct':100*abs(f)/d['limite_MW']})
    return pd.DataFrame(rows)

def contingencias_dc(g,inyecciones):
    rows=[]
    for edge in list(g.edges):
        h=g.copy();h.remove_edge(*edge)
        connected=nx.is_connected(h)
        rows.append({'salida':'–'.join(edge),'conectado':connected,
                     'max_carga_pct':flujo_dc(h,inyecciones).carga_pct.max() if connected else np.nan,
                     'alcance':'DC despacho fijo; no certifica N-1 integral'})
    return pd.DataFrame(rows)

def hhi_completo(shares):
    s=np.asarray(shares,float)
    if (s<0).any() or not np.isclose(s.sum(),1,atol=1e-8):
        raise ValueError('HHI exige participaciones no negativas que sumen 1 en universo definido')
    return float(np.sum((100*s)**2))

def bass(t,p,q):
    z=np.exp(-(p+q)*np.asarray(t));return (1-z)/(1+(q/p)*z)

def experimento_bass(seed=42):
    """Recuperación de parámetros conocidos; no son observaciones colombianas."""
    t=np.arange(16);rng=np.random.default_rng(seed)
    y=np.clip(bass(t,.01,.35)+rng.normal(0,.006,len(t)),0,1)
    pars,_=curve_fit(bass,t,y,p0=[.02,.3],bounds=([.0001,.0001],[1,1]))
    return pd.DataFrame({'t':t,'fraccion_sintetica':y,'ajuste':bass(t,*pars)}),pars

def ciclo_inversion(delay=4.,sensibilidad=1.,T=30.):
    """Ajuste de capacidad a objetivo fijo; explora, no presupone oscilaciones."""
    if delay<=0 or sensibilidad<0 or T<=0:raise ValueError('Parámetros inválidos')
    objetivo=1000.;vida=30.
    def rhs(t,y):
        cap,pipe=y
        # MW/año: reposición + respuesta a brecha, nunca construcción negativa.
        inicio=max(0,objetivo/vida+sensibilidad*(objetivo-cap))
        puesta=pipe/delay;retiro=cap/vida
        return [puesta-retiro,inicio-puesta]
    sol=solve_ivp(rhs,[0,T],[700,50],t_eval=np.linspace(0,T,301),rtol=1e-8,atol=1e-9)
    if not sol.success:raise RuntimeError(sol.message)
    return pd.DataFrame({'anio_modelo':sol.t,'capacidad_MW':sol.y[0],
                         'pipeline_MW':sol.y[1],'objetivo_MW':objetivo})

def balance_embalse(factor_aportes=1.,disponibilidad_termica=.9,solar_MW=30.,
                    ahorro_pct=0.,meses=24,almacen_inicial_MWh=120000.,
                    demanda_factor=1.):
    """Sistema ficticio. Almacén en MWh equivalentes de agua con conversión fija.
    Política miope: solar, hidro disponible, térmica, faltante mensual.
    No es despacho colombiano, precio de bolsa, ENFICC ni LOLE.
    """
    if factor_aportes<0 or not 0<=disponibilidad_termica<=1 or not 0<=ahorro_pct<1:
        raise ValueError('Supuestos fuera de dominio')
    if meses<1 or solar_MW<0 or demanda_factor<=0 or not 0<=almacen_inicial_MWh<=240000:
        raise ValueError('Estado/escala inválidos')
    store=float(almacen_inicial_MWh);rows=[]
    for i,date in enumerate(pd.date_range('2024-01-01',periods=meses,freq='MS')):
        hours=date.days_in_month*24
        demanda=160*hours*demanda_factor*(1-ahorro_pct)
        aportes=90000*(1+.45*np.sin(2*np.pi*(i-3)/12))*factor_aportes
        # Aportes medios sintéticos; almacenaje y límite de turbina por separado.
        water=store+aportes
        solar=min(demanda,solar_MW*.20*hours)
        hidro=min(water,100*hours,max(0,demanda-solar))
        termica=min(90*disponibilidad_termica*hours,max(0,demanda-solar-hidro))
        faltante=max(0,demanda-solar-hidro-termica)
        vertimiento=max(0,water-hidro-240000)
        end=water-hidro-vertimiento
        rows.append({'mes':str(date.date()),'horas':hours,'almacen_inicial_MWh':store,
          'aportes_MWh_eq':aportes,'hidro_MWh':hidro,'solar_MWh':solar,'termica_MWh':termica,
          'demanda_MWh':demanda,'faltante_MWh':faltante,'vertimiento_MWh_eq':vertimiento,
          'almacen_final_MWh':end,'costo_variable_COP':hidro*30000+termica*350000,
          'emisiones_termicas_tCO2':termica*.45})
        store=end
    return pd.DataFrame(rows)

def caja_proyecto(capacidad_MW=20.,factor_planta=.20,precio_captura_COP_kWh=230.,
                  fraccion_PPA=.60,precio_PPA_COP_kWh=240.,capex_COP_MW=3.2e9,
                  opex_COP_MW_anio=45e6,tasa_real=.10,vida_anios=20,demora_anios=0):
    """Flujo real sin deuda, antes de impuestos, COP constantes del ejercicio.
    PPA pay-as-produced: fracción de producción efectiva, sin obligación de volumen fijo.
    Sin ingreso CxC: no se presume asignación OEF ni ENFICC.
    CAPEX íntegro en t=0, demora retrasa la operación, horizonte de operación constante.
    """
    if capacidad_MW<0 or not 0<=factor_planta<=1 or not 0<=fraccion_PPA<=1 or tasa_real<=-1:
        raise ValueError('Supuestos financieros inválidos')
    if vida_anios<1 or demora_anios<0 or int(demora_anios)!=demora_anios:
        raise ValueError('Horizonte/demora inválidos')
    if capex_COP_MW<0 or opex_COP_MW_anio<0:raise ValueError('Costos negativos')
    n=int(vida_anios+demora_anios);rows=[]
    for t in range(n+1):
        energia=capacidad_MW*8760*factor_planta*(.995**(t-demora_anios-1)) if t>demora_anios else 0.
        ppa=energia*fraccion_PPA*1000*precio_PPA_COP_kWh
        spot=energia*(1-fraccion_PPA)*1000*precio_captura_COP_kWh
        opex=capacidad_MW*opex_COP_MW_anio if t>demora_anios else 0.
        capex=capacidad_MW*capex_COP_MW if t==0 else 0.
        flujo=ppa+spot-opex-capex
        rows.append({'anio':t,'energia_MWh':energia,'ingreso_PPA_COP':ppa,'ingreso_spot_COP':spot,
                     'opex_COP':opex,'capex_COP':capex,'flujo_COP':flujo,
                     'valor_presente_COP':flujo/(1+tasa_real)**t})
    df=pd.DataFrame(rows);return df,float(df.valor_presente_COP.sum())

def precio_captura(precio_COP_kWh,produccion_MWh):
    p=np.asarray(precio_COP_kWh,float);q=np.asarray(produccion_MWh,float)
    if p.shape!=q.shape or not np.isfinite(p).all() or not np.isfinite(q).all() or (q<0).any() or q.sum()<=0:
        raise ValueError('Series alineadas y energía positiva requeridas')
    return float(np.sum(p*q)/q.sum())

ESCENARIOS={
 'Referencia':{'factor_planta':.20,'precio_captura_COP_kWh':230.,'demora_anios':0},
 'Precio capturado bajo':{'factor_planta':.20,'precio_captura_COP_kWh':130.,'demora_anios':0},
 'Conexión tardía':{'factor_planta':.20,'precio_captura_COP_kWh':230.,'demora_anios':2},
 'Producción baja':{'factor_planta':.15,'precio_captura_COP_kWh':200.,'demora_anios':0},
}
ALTERNATIVAS={
 'No construir':{'capacidad_MW':0.,'fraccion_PPA':0.},
 'Solar 20 MW mercante':{'capacidad_MW':20.,'fraccion_PPA':0.},
 'Solar 20 MW PPA parcial':{'capacidad_MW':20.,'fraccion_PPA':.60},
}

def escenarios_negocio(escenarios=None,alternativas=None):
    scenarios=ESCENARIOS if escenarios is None else escenarios
    options=ALTERNATIVAS if alternativas is None else alternativas
    table=pd.DataFrame(index=scenarios,columns=options,dtype=float)
    for s,params in scenarios.items():
        for a,action in options.items():
            _,vpn=caja_proyecto(**params,**action)
            table.loc[s,a]=vpn/1e9
    # Mayor VPN es mejor; métrica comparable en miles de millones COP constantes.
    regret=table.rsub(table.max(axis=1),axis=0)
    summary=pd.DataFrame({'min_VPN_miles_millones_COP':table.min(),
                          'max_regret_miles_millones_COP':regret.max()})
    summary['admisible_financieramente']=summary.min_VPN_miles_millones_COP>=0
    return table,regret,summary.sort_values('max_regret_miles_millones_COP')
