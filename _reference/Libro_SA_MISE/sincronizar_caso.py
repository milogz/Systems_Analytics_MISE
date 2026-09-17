"""Actualiza únicamente componentes comunes; conserva contenidos y entregas del caso."""
from pathlib import Path
import shutil,hashlib,json
root=Path(__file__).resolve().parent
target=root.parent/'Caso Consultoria Sistemica SA-MISE'
if not (target/'MANIFIESTO.json').exists():raise SystemExit('Falta la carpeta hermana del caso')
records={}
for folder in ['sa_mise','datos','tests']:
    for p in (root/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            relative=p.relative_to(root);q=target/relative;q.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(p,q);records[str(relative)]=hashlib.sha256(q.read_bytes()).hexdigest()
for name in ['ejecutar_local.py','verificar.py','construir.py','MAPA_EDITORIAL.md','requirements.txt','FUENTES.md','ALINEACION_CURRICULAR.md','BITACORA_REVISION.md','docente/GUIA_FACILITACION.md']:
    p=root/name;q=target/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
    records[name]=hashlib.sha256(q.read_bytes()).hexdigest()
(target/'COMPONENTES_GENERADOS.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Componentes comunes sincronizados; contenido y entregas del caso conservados')
