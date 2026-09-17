"""Ensambla lecturas + prácticas. No toca la edición anterior ni publica en red."""
from pathlib import Path
import nbformat
ROOT=Path(__file__).resolve().parent

def main():
    lectures=sorted((ROOT/'marco_teorico').glob('*.md'))
    practices=sorted((ROOT/'practica_computacional').glob('*.ipynb'))
    if not lectures or len(lectures)!=len(practices):
        raise ValueError('Cada lectura requiere una práctica')
    out=ROOT/'cuadernos_integrados';out.mkdir(exist_ok=True)
    import json
    units=json.loads((ROOT/'MANIFIESTO.json').read_text(encoding='utf-8'))['unidades']
    if len(units)!=len(lectures):raise ValueError('Manifiesto incompleto')
    pairs=[(ROOT/'marco_teorico'/u['lectura'],ROOT/'practica_computacional'/u['practica']) for u in units]
    if set(lectures)!={a for a,b in pairs} or set(practices)!={b for a,b in pairs}:
        raise ValueError('Fuentes y manifiesto no coinciden')
    for lecture,practice in pairs:
        nb=nbformat.read(practice,as_version=4)
        nb.cells=[nbformat.v4.new_markdown_cell(lecture.read_text(encoding='utf-8'))]+nb.cells
        nbformat.validate(nb)
        nbformat.write(nb,out/practice.name)
        print(f'Integrado: {practice.name}')
    chapters='\n'.join('  - file: cuadernos_integrados/'+p.stem for p in practices)
    appendices=['FUENTES','datos/CONTRATO_DATOS','BITACORA_REVISION']
    if (ROOT/'ALINEACION_CURRICULAR.md').exists():appendices.append('ALINEACION_CURRICULAR')
    if (ROOT/'DOSSIER.md').exists():appendices=['DOSSIER','RUBRICA_Y_ENTREGAS','ANEXO_NEGOCIO']+appendices
    toc='format: jb-book\nroot: intro\nchapters:\n'+chapters+'\n'+''.join('  - file: '+x+'\n' for x in appendices)
    (ROOT/'_toc.yml').write_text(toc,encoding='utf-8')

if __name__=='__main__':main()
