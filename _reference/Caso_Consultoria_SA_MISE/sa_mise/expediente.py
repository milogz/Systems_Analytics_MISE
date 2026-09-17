"""Persistencia JSON explícita; nunca inventa capas ni conclusiones faltantes."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
ETAPAS=['evidencia','identidad','infraestructura','mercado','dinamica','decision','gobernanza']
NIVELES={'descripcion','exploracion','evaluacion_condicionada'}

def ruta(caso):
    if not re.fullmatch(r'[A-Za-z0-9_-]+',caso):raise ValueError('Identificador de caso inválido')
    return ROOT/'entregas'/caso/'expediente.json'

def cargar(caso='ejemplo_docente'):
    p=ruta(caso)
    if not p.exists():return {'version':2,'caso':caso,'etapas':{}}
    state=json.loads(p.read_text(encoding='utf-8'))
    if state.get('version')!=2 or state.get('caso')!=caso or not isinstance(state.get('etapas'),dict):
        raise ValueError('Estado incompatible; no se reemplaza silenciosamente')
    return state

def registrar(caso,etapa,hallazgo,nivel,fuente,transformacion,limite,decision_estudiante='POR COMPLETAR'):
    if etapa not in ETAPAS or nivel not in NIVELES:raise ValueError('Etapa/nivel desconocido')
    if not all(isinstance(v,str) and v.strip() for v in [hallazgo,fuente,transformacion,limite]):
        raise ValueError('Faltan evidencia, transformación o límite')
    state=cargar(caso)
    state['etapas'][etapa]={'hallazgo':hallazgo,'nivel':nivel,'fuente':fuente,
        'transformacion':transformacion,'limite':limite,'decision_estudiante':decision_estudiante}
    p=ruta(caso);p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_suffix('.tmp');temp.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
    temp.replace(p)
    return state

def exportar(caso='ejemplo_docente'):
    state=cargar(caso);missing=set(ETAPAS)-set(state['etapas'])
    if missing:raise ValueError('Faltan etapas: '+', '.join(sorted(missing)))
    pending=[k for k,v in state['etapas'].items() if v['decision_estudiante']=='POR COMPLETAR']
    title='BORRADOR DOCENTE — NO ES UNA RECOMENDACIÓN' if pending else 'Informe para revisión'
    lines=[f'# {title}',f'\nCaso: {caso}. Versión de esquema: 2.',
           '\nLas cifras exploratorias no describen una inversión real. Validar fuentes y competencias antes de decidir.']
    for k in ETAPAS:
        lines.append(f'\n## {k.title()}')
        for field,value in state['etapas'][k].items():lines.append(f'\n**{field}:** {value}')
    lines.append('\n## Decisión y revisión humana\nIntegrar alternativas, responsables, costos, umbrales y evidencia adversa. El software no aprueba el proyecto.')
    p=ruta(caso).with_name('informe.md');p.write_text('\n'.join(lines),encoding='utf-8')
    return p
