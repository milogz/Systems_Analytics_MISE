"""Control de coherencia editorial y presencia de salidas verificadas."""
from pathlib import Path
import json,nbformat
root=Path(__file__).resolve().parent
records={}
for folder in [root,root.parent/'Caso Consultoria Sistemica SA-MISE']:
    manifest=json.loads((folder/'MANIFIESTO.json').read_text(encoding='utf-8'))
    verification=json.loads((folder/'VERIFICACION.json').read_text(encoding='utf-8'))
    assert len(manifest['unidades'])==len(verification['practicas'])
    for unit in manifest['unidades']:
        source=nbformat.read(folder/'practica_computacional'/unit['practica'],as_version=4)
        assembled=nbformat.read(folder/'cuadernos_integrados'/unit['practica'],as_version=4)
        assert assembled.cells[0].source==(folder/'marco_teorico'/unit['lectura']).read_text(encoding='utf-8')
        assert len(assembled.cells)==len(source.cells)+1
        assert all(c.execution_count is not None for c in source.cells if c.cell_type=='code')
    records[folder.name]={'unidades':len(manifest['unidades']),'motor':verification['motor'],'coherencia':'superada'}
(root/'CONTROL_ENTREGA.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(records,ensure_ascii=False))
