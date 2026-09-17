"""Ejecuta un notebook con IPython en proceso aislado, sin servidor ni puertos.

Alternativa explícita para entornos que no permiten crear el archivo seguro de
conexión de Jupyter. Captura texto, tablas y figuras; no prueba transporte kernel.
"""
from pathlib import Path
import sys,nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output
import matplotlib
matplotlib.use('module://matplotlib_inline.backend_inline')
from matplotlib_inline.backend_inline import configure_inline_support
from matplotlib_inline.config import InlineBackend

def main():
    path=Path(sys.argv[1]).resolve()
    nb=nbformat.read(path,as_version=4)
    shell=InteractiveShell.instance()
    InlineBackend.instance().shell=shell
    configure_inline_support(shell,'module://matplotlib_inline.backend_inline')
    count=0
    for cell in nb.cells:
        if cell.cell_type!='code':continue
        count+=1
        with capture_output() as captured:
            result=shell.run_cell(cell.source,store_history=True)
        if result.error_before_exec or result.error_in_exec:
            raise RuntimeError(f'{path.name}, celda {count}: {result.error_before_exec or result.error_in_exec}')
        outputs=[]
        if captured.stdout:outputs.append(nbformat.v4.new_output('stream',name='stdout',text=captured.stdout))
        if captured.stderr:outputs.append(nbformat.v4.new_output('stream',name='stderr',text=captured.stderr))
        for output in captured.outputs:
            outputs.append(nbformat.v4.new_output('display_data',data=output.data,metadata=output.metadata))
        cell.outputs=outputs;cell.execution_count=count
    nbformat.validate(nb);nbformat.write(nb,path)
    print(f'IPython local: {path.name}, {count} celdas',flush=True)

if __name__=='__main__':main()
