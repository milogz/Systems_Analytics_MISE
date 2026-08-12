"""
build_book.py — Ensambla el coursebook desde los archivos fuente.

Uso:
    python build_book.py          # Solo ensamblar
    python build_book.py --build  # Ensamblar + jupyter-book build

Los archivos fuente (marco_teorico/, notebooks/) son la fuente de verdad.
Este script copia lo necesario a coursebook/ y adapta headers para MyST.
"""
import shutil
import os
import sys
import re
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK_DIR = os.path.join(ROOT, 'coursebook')

# Mapping: (source_md, source_ipynb) -> target_folder
CHAPTERS = {
    'preludio': {
        'md': 'marco_teorico/preludio_fundamentos.md',
        'ipynb': 'notebooks/preludio_fundamentos.ipynb',
    },
    'semana_01': {
        'md': 'marco_teorico/semana_01_complejidad.md',
        'ipynb': 'notebooks/semana_01_complejidad.ipynb',
    },
    'semana_02': {
        'md': 'marco_teorico/semana_02_redes_topologia.md',
        'ipynb': 'notebooks/semana_02_redes_topologia.ipynb',
    },
    'semana_03': {
        'md': 'marco_teorico/semana_03_redes_dinamica_actores.md',
        'ipynb': 'notebooks/semana_03_redes_dinamica.ipynb',
    },
    'semana_04': {
        'md': 'marco_teorico/semana_04_dinamica_sistemas.md',
        'ipynb': 'notebooks/semana_04_dinamica_sistemas.ipynb',
    },
    'semana_05': {
        'md': 'marco_teorico/semana_05_politicas_escenarios.md',
        'ipynb': 'notebooks/semana_05_politicas_escenarios.ipynb',
    },
}


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def copy_md(src, dst):
    """Copy markdown file, adding MyST-compatible frontmatter if missing."""
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    # If file already has frontmatter, leave it
    if content.startswith('---'):
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(content)
        return

    # Extract title from first # heading
    title_match = re.match(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else 'Lectura'

    # Remove emojis (if any slipped through)
    emoji_pattern = re.compile("[\U0001F300-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]")
    content = emoji_pattern.sub('', content)

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  MD: {os.path.basename(src)} -> {dst}")


def copy_notebook(src, dst):
    """Copy notebook, keeping outputs (pre-executed)."""
    shutil.copy2(src, dst)
    print(f"  NB: {os.path.basename(src)} -> {dst}")


def copy_mise_utils():
    """Copy mise_utils package into coursebook for notebook imports."""
    src_dir = os.path.join(ROOT, 'notebooks', 'mise_utils')
    dst_dir = os.path.join(BOOK_DIR, 'mise_utils')

    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    shutil.copytree(src_dir, dst_dir,
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    print(f"  UTILS: mise_utils/ -> coursebook/mise_utils/")


def main():
    print("=" * 50)
    print("COURSE BOOK ASSEMBLER")
    print("=" * 50)

    # 1. Copy chapters
    for chapter_name, sources in CHAPTERS.items():
        chapter_dir = os.path.join(BOOK_DIR, chapter_name)
        ensure_dir(chapter_dir)

        md_src = os.path.join(ROOT, sources['md'])
        md_dst = os.path.join(chapter_dir, 'lectura.md')
        if os.path.exists(md_src):
            copy_md(md_src, md_dst)
        else:
            print(f"  WARN: {sources['md']} not found")

        ipynb_src = os.path.join(ROOT, sources['ipynb'])
        ipynb_dst = os.path.join(chapter_dir, 'notebook.ipynb')
        if os.path.exists(ipynb_src):
            copy_notebook(ipynb_src, ipynb_dst)
        else:
            print(f"  WARN: {sources['ipynb']} not found")

    # 2. Copy mise_utils
    copy_mise_utils()

    # 3. Ensure cierre dir exists
    ensure_dir(os.path.join(BOOK_DIR, 'cierre'))

    print(f"\nAssembly complete. Book ready in: {BOOK_DIR}")

    # 4. Optionally build
    if '--build' in sys.argv:
        print("\nBuilding book...")
        import subprocess
        result = subprocess.run(
            [sys.executable, '-m', 'jupyter_book', 'build', BOOK_DIR],
            cwd=ROOT
        )
        if result.returncode == 0:
            print(f"\nBuild successful!")
            print(f"Open: {os.path.join(BOOK_DIR, '_build', 'html', 'index.html')}")
        else:
            print(f"\nBuild failed with code {result.returncode}")
            sys.exit(1)


if __name__ == '__main__':
    main()
