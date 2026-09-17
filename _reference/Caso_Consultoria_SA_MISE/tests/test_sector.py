import unittest
import numpy as np
from sa_mise import sector

class PruebasSector(unittest.TestCase):
    def test_balances_y_extremos(self):
        for a in [np.zeros(24),sector.aportes_docentes(),np.full(24,1e6)]:
            for reserva in [0,60000]:
                d=sector.sistema_docente(a,reserva_MWh=reserva)
                np.testing.assert_allclose(d.stock_inicial_MWh_eq+d.aporte_MWh_eq-d.hidro_MWh-d.vertimiento_MWh_eq,d.stock_final_MWh_eq,atol=1e-8)
                np.testing.assert_allclose(d.demanda_neta_MWh,d.solar_MWh+d.hidro_MWh+d.termica_MWh+d.faltante_MWh)
                self.assertTrue(d.stock_final_MWh_eq.between(0,240000).all())
                self.assertEqual(d.horas.iloc[1],696)
    def test_demora_solo_cambia_capacidad_desde_mes_trece(self):
        a=sector.aportes_docentes()*.45
        base=sector.sistema_docente(a)
        tarde=sector.sistema_docente(a,solar_extra_MW=np.r_[np.zeros(12),np.full(12,20)])
        np.testing.assert_allclose(base.select_dtypes('number').iloc[:12],tarde.select_dtypes('number').iloc[:12])
        self.assertGreater(tarde.solar_MWh.iloc[12:].sum(),base.solar_MWh.iloc[12:].sum())
    def test_secuencia_mismo_total_no_implica_mismo_vertimiento(self):
        a=sector.aportes_docentes();b=np.zeros(24);b[[0,1,12,13]]=a.sum()/4
        self.assertAlmostEqual(a.sum(),b.sum())
        self.assertGreater(sector.sistema_docente(b).vertimiento_MWh_eq.sum(),sector.sistema_docente(a).vertimiento_MWh_eq.sum())
    def test_perfil_y_ponderacion(self):
        d,m=sector.perfiles_horarios()
        self.assertEqual(len(d),24);self.assertEqual(m['dias'],366)
        self.assertGreater(d.potencia_media_demanda_comercial_MW.min(),0)
        self.assertAlmostEqual(d.precio_medio_nominal_COP_kWh.mean(),m['precio_medio_nominal_COP_kWh'])
    def test_residuos_controles(self):
        d,_=sector.asociacion_hidrologica()
        for col in ['log_precio_residuo','embalse_pct_residuo']:
            self.assertLess(abs(d[col].mean()),1e-8)
            self.assertLess(d.groupby('anio')[col].mean().abs().max(),1e-8)
    def test_costos_y_base_comparables(self):
        d=sector.comparar_respuestas()
        self.assertEqual(len(d),20)
        self.assertTrue((d[d.alternativa=='Base'].costo_intervencion_COP==0).all())
        self.assertTrue((d[d.alternativa=='Solar adicional 20 MW'].costo_intervencion_COP>64e9).all())
        np.testing.assert_allclose(d.costo_variable_COP+d.costo_intervencion_COP,d.costo_parcial_COP)

if __name__=='__main__':unittest.main()
