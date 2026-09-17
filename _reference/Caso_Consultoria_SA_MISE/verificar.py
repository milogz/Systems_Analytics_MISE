"""Ejecuta notebooks con kernels nuevos, pruebas semánticas y reensambla."""
from pathlib import Path
import json,subprocess,sys,importlib.metadata,os
import nbformat
from nbclient import NotebookClient
ROOT=Path(__file__).resolve().parent

def main():
    runtime=ROOT/'.verificacion_tmp';runtime.mkdir(exist_ok=True)
    for key in ['TEMP','TMP','TMPDIR','JUPYTER_RUNTIME_DIR','IPYTHONDIR']:
        target=runtime/key;target.mkdir(exist_ok=True);os.environ[key]=str(target)
    result=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT)
    if result.returncode:raise SystemExit(result.returncode)
    records=[]
    for p in sorted((ROOT/'practica_computacional').glob('*.ipynb')):
        if '--local' in sys.argv:
            subprocess.run([sys.executable,str(ROOT/'ejecutar_local.py'),str(p)],cwd=ROOT,check=True)
            nb=nbformat.read(p,as_version=4)
            records.append({'archivo':p.name,'celdas_codigo':sum(c.cell_type=='code' for c in nb.cells),'errores':0})
            continue
        nb=nbformat.read(p,as_version=4)
        client=NotebookClient(nb,timeout=180,kernel_name='python3',
                              resources={'metadata':{'path':str(ROOT)}})
        client.execute()
        errors=[o for c in nb.cells if c.cell_type=='code' for o in c.get('outputs',[]) if o.output_type=='error']
        if errors:raise RuntimeError(str(errors))
        nbformat.write(nb,p)
        records.append({'archivo':p.name,'celdas_codigo':sum(c.cell_type=='code' for c in nb.cells),'errores':0})
        print('Verificado:',p.name,flush=True)
    subprocess.run([sys.executable,str(ROOT/'construir.py')],cwd=ROOT,check=True)
    payload={'python':sys.version,'dependencias':{m:importlib.metadata.version(m) for m in ['numpy','pandas','scipy','networkx','matplotlib','nbformat','nbclient']},
             'practicas':records,'pruebas_semanticas':'superadas',
             'motor':'IPython local, proceso nuevo por notebook' if '--local' in sys.argv else 'Jupyter NotebookClient, kernel nuevo por notebook',
             'alcance':'Ejecución y consistencia del material docente; no certificación de datos externos ni modelo del SIN. El modo local no prueba transporte ni interfaz Jupyter.'}
    (ROOT/'VERIFICACION.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
