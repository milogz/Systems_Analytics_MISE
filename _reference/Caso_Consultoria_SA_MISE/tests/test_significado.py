import unittest,tempfile
from contextlib import contextmanager
import uuid,shutil
from pathlib import Path
from unittest.mock import patch
import numpy as np
import pandas as pd
from sa_mise import datos,modelos,expediente

@contextmanager
def directorio_prueba():
    # mkdir normal evita el ACL especial de mkdtemp(mode=0700) en Python 3.14/Windows.
    base=Path(__file__).resolve().parents[1]/'.verificacion_tmp'/'fixtures'
    base.mkdir(parents=True,exist_ok=True)
    target=base/uuid.uuid4().hex
    target.mkdir()
    try:yield target
    finally:
        if target.resolve().parent!=base.resolve():raise ValueError('Ruta temporal inesperada')
        shutil.rmtree(target)

class PruebasSignificado(unittest.TestCase):
    def test_cobertura_parcial_excluida(self):
        raw=datos.leer_diario('xm_precio_bolsa_raw.csv')
        self.assertFalse(bool(datos.cobertura(raw).set_index('anio').loc[2025,'completo']))
        self.assertEqual(datos.precio_anual().anio.max(),2024)

    def test_bisiesto_y_conversion_potencia(self):
        b=datos.balance_descriptivo().set_index('anio').loc[2024]
        self.assertEqual(b.horas,8784)
        self.assertAlmostEqual(b.potencia_media_MW*8784/1000,b.generacion_GWh,places=6)
        self.assertGreater(b.demanda_pico_MW,11000)
        self.assertLess(b.demanda_pico_MW,13000)
        self.assertNotIn('margen_reserva_pct',b.index)

    def test_sin_clasificar_no_pierde_energia(self):
        r=datos.proxies_recursos()
        self.assertIn('SIN_CLASIFICAR',set(r.Type))
        self.assertAlmostEqual(r.max_produccion_horaria_observada_MW.sum(),r.groupby('Type').max_produccion_horaria_observada_MW.sum().sum(),places=6)
        self.assertNotIn('factor_planta',r)

    def test_hora_ausente_y_fecha_duplicada_detienen(self):
        d={'Date':['2024-01-01']};d.update({h:[1.] for h in datos.HORAS})
        with directorio_prueba() as td,patch.object(datos,'RAW',Path(td)):
            df=pd.DataFrame(d);df.loc[0,'Values_Hour24']=np.nan;df.to_csv(Path(td)/'x.csv',index=False)
            with self.assertRaises(ValueError):datos.leer_diario('x.csv')
            pd.concat([pd.DataFrame(d)]*2).to_csv(Path(td)/'x.csv',index=False)
            with self.assertRaises(ValueError):datos.leer_diario('x.csv')

    def test_hhi_rechaza_universo_incompleto(self):
        with self.assertRaises(ValueError):modelos.hhi_completo([.24,.188,.142])
        self.assertEqual(modelos.hhi_completo([.5,.5]),5000)

    def test_flujo_dc_balance_y_reactancia(self):
        g,p=modelos.red_docente();f=modelos.flujo_dc(g,p)
        for n in g:
            salida=f.loc[f.origen==n,'flujo_MW'].sum()-f.loc[f.destino==n,'flujo_MW'].sum()
            self.assertAlmostEqual(salida,p[n],places=7)
        g['A']['C']['x_pu']*=3
        self.assertFalse(np.allclose(f.flujo_MW,modelos.flujo_dc(g,p).flujo_MW))

    def test_balance_y_sequia_activa(self):
        normal=modelos.balance_embalse();seco=modelos.balance_embalse(factor_aportes=.35)
        self.assertGreater(seco.faltante_MWh.sum(),normal.faltante_MWh.sum())
        for factor in [0,.35,1,3]:
            b=modelos.balance_embalse(factor_aportes=factor)
            np.testing.assert_allclose(b.almacen_inicial_MWh+b.aportes_MWh_eq-b.hidro_MWh-b.vertimiento_MWh_eq,b.almacen_final_MWh,atol=1e-7)
            np.testing.assert_allclose(b.demanda_MWh,b.hidro_MWh+b.solar_MWh+b.termica_MWh+b.faltante_MWh,atol=1e-7)
            self.assertTrue(b.almacen_final_MWh.between(0,240000).all())

    def test_precio_capturado_pondera(self):
        self.assertEqual(modelos.precio_captura([100,300],[3,1]),150)

    def test_caja_no_construir_demora_y_sensibilidad(self):
        _,zero=modelos.caja_proyecto(capacidad_MW=0);self.assertEqual(zero,0)
        df,a=modelos.caja_proyecto();_,b=modelos.caja_proyecto(demora_anios=2)
        self.assertLess(b,a)
        self.assertEqual(df.capex_COP.iloc[0],64e9)
        _,c=modelos.caja_proyecto(precio_captura_COP_kWh=330)
        self.assertGreater(c,a)
        np.testing.assert_allclose(df.flujo_COP,df.ingreso_PPA_COP+df.ingreso_spot_COP-df.opex_COP-df.capex_COP)

    def test_regret_y_ganador_derivados(self):
        val,reg,summ=modelos.escenarios_negocio()
        self.assertTrue((reg.min(axis=1).abs()<1e-9).all())
        for a in val:
            self.assertAlmostEqual(summ.loc[a,'max_regret_miles_millones_COP'],max(val.max(axis=1)-val[a]))
        self.assertTrue(np.allclose(val['No construir'],0))

    def test_estado_se_conserva_y_exportacion_no_inventa(self):
        with directorio_prueba() as td,patch.object(expediente,'ROOT',Path(td)):
            expediente.registrar('grupo','evidencia','Dato del grupo','descripcion','fuente','transformacion','limite')
            with self.assertRaises(ValueError):expediente.exportar('grupo')
            for stage in expediente.ETAPAS[1:]:expediente.registrar('grupo',stage,'Ejemplo','exploracion','f','t','l')
            self.assertEqual(expediente.cargar('grupo')['etapas']['evidencia']['hallazgo'],'Dato del grupo')
            text=expediente.exportar('grupo').read_text(encoding='utf-8')
            self.assertIn('BORRADOR',text);self.assertIn('Dato del grupo',text)

if __name__=='__main__':unittest.main()
