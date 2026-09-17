"""Actualizar copia derivada del paquete del caso desde el libro; no edita originales."""
from pathlib import Path
import shutil,hashlib
ROOT=Path(__file__).resolve().parent
source=ROOT/'Libro SA-MISE'/'sa_mise'
target=ROOT/'Caso Consultoria Sistemica SA-MISE'/'sa_mise'
if not source.is_dir() or not target.is_dir():raise SystemExit('Ubique este script junto a las dos carpetas nuevas')
for p in source.glob('*.py'):
    dst=target/p.name;shutil.copy2(p,dst)
    assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(dst.read_bytes()).digest()
print('Copia del caso sincronizada desde el libro.')
