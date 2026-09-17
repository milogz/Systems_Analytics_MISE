"""
build_book.py — Ensambla el coursebook desde los archivos fuente.

Uso:
    python build_book.py          # Solo ensamblar
    python build_book.py --build  # Ensamblar + jupyter-book build

Los archivos fuente (marco_teorico/, notebooks/) son la fuente de verdad.
Este script copia lo necesario a coursebook/ y adapta headers para MyST.

Estructura por semana:
  - lectura.md          ← marco_teorico/semana_XX_*.md
  - notebook.ipynb      ← notebooks/semana_XX_*.ipynb (práctica computacional)
  - caso_colombia.ipynb ← notebooks/saga_XX_*.ipynb (aplicación al caso Colombia)
  - guia.md             ← ya vive en coursebook/ (guía semanal con lecturas y actividades)
"""
import shutil
import os
import sys
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK_DIR = os.path.join(ROOT, 'coursebook')

# ─────────────────────────────────────────────────────────────
# Mapping: chapter_name -> { md, ipynb, saga }
# md:    source markdown lecture in marco_teorico/
# ipynb: source practice notebook in notebooks/
# saga:  source saga notebook in notebooks/ (caso Colombia)
# Any of these can be None if not applicable for that week.
# ─────────────────────────────────────────────────────────────
CHAPTERS = {
    'preludio': {
        'md': 'marco_teorico/preludio_fundamentos.md',
        'ipynb': 'notebooks/preludio_fundamentos.ipynb',
        'saga': 'notebooks/saga_00_radiografia_datos.ipynb',
    },
    'semana_01': {
        'md': 'marco_teorico/semana_01_complejidad.md',
        'ipynb': 'notebooks/semana_01_complejidad.ipynb',
        'saga': 'notebooks/saga_01_identidad.ipynb',
    },
    'semana_02': {
        'md': 'marco_teorico/semana_02_redes_topologia.md',
        'ipynb': 'notebooks/semana_02_redes_topologia.ipynb',
        'saga': 'notebooks/saga_02_estructura_fisica.ipynb',
    },
    'semana_03': {
        'md': 'marco_teorico/semana_03_redes_dinamica_actores.md',
        'ipynb': 'notebooks/semana_03_redes_dinamica.ipynb',
        'saga': 'notebooks/saga_03_estructura_social.ipynb',
    },
    'semana_04': {
        'md': 'marco_teorico/semana_04_dinamica_sistemas.md',
        'ipynb': 'notebooks/semana_04_dinamica_sistemas.ipynb',
        'saga': 'notebooks/saga_04_dinamica.ipynb',
    },
    'semana_05': {
        'md': 'marco_teorico/semana_05_politicas_escenarios.md',
        'ipynb': 'notebooks/semana_05_politicas_escenarios.ipynb',
        'saga': 'notebooks/saga_05_politica.ipynb',
    },
    'semana_06': {
        'md': 'marco_teorico/semana_06_gobernanza_justicia.md',
        'ipynb': None,  # S6 integra herramientas de S2-S5, sin notebook nuevo
        'saga': 'notebooks/saga_06_gobernanza.ipynb',
    },
    'semana_07': {
        'md': 'marco_teorico/semana_07_integracion_proyecto.md',
        'ipynb': None,  # Semana taller
        'saga': 'notebooks/saga_07_sintesis.ipynb',
    },
    'semana_08': {
        'md': 'marco_teorico/semana_08_horizontes_cierre.md',
        'ipynb': None,  # Semana de presentaciones
        'saga': None,   # Sin saga — es la entrega final
    },
}

# Additional standalone pages
EXTRAS = {
    'caso_colombia': {
        'md': 'marco_teorico/caso_colombia_sistema_electrico.md',
        'dst_name': 'contexto.md',
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
    print("=" * 60)
    print("COURSE BOOK ASSEMBLER — Systems Analytics MISE")
    print("=" * 60)

    # 1. Copy chapters (lectura + notebook + caso_colombia)
    for chapter_name, sources in CHAPTERS.items():
        chapter_dir = os.path.join(BOOK_DIR, chapter_name)
        ensure_dir(chapter_dir)
        print(f"\n[{chapter_name}]")

        # Lectura (markdown)
        if sources.get('md'):
            md_src = os.path.join(ROOT, sources['md'])
            md_dst = os.path.join(chapter_dir, 'lectura.md')
            if os.path.exists(md_src):
                copy_md(md_src, md_dst)
            else:
                print(f"  WARN: {sources['md']} not found")

        # Práctica computacional (notebook)
        if sources.get('ipynb'):
            ipynb_src = os.path.join(ROOT, sources['ipynb'])
            ipynb_dst = os.path.join(chapter_dir, 'notebook.ipynb')
            if os.path.exists(ipynb_src):
                copy_notebook(ipynb_src, ipynb_dst)
            else:
                print(f"  WARN: {sources['ipynb']} not found")

        # Caso Colombia (saga notebook)
        if sources.get('saga'):
            saga_src = os.path.join(ROOT, sources['saga'])
            saga_dst = os.path.join(chapter_dir, 'caso_colombia.ipynb')
            if os.path.exists(saga_src):
                copy_notebook(saga_src, saga_dst)
            else:
                print(f"  WARN: {sources['saga']} not found")

    # 2. Copy extra standalone pages
    print(f"\n[extras]")
    for section_name, info in EXTRAS.items():
        section_dir = os.path.join(BOOK_DIR, section_name)
        ensure_dir(section_dir)
        md_src = os.path.join(ROOT, info['md'])
        md_dst = os.path.join(section_dir, info['dst_name'])
        if os.path.exists(md_src):
            copy_md(md_src, md_dst)
        else:
            print(f"  WARN: {info['md']} not found")

    # 3. Copy mise_utils
    copy_mise_utils()

    print(f"\n{'=' * 60}")
    print(f"Assembly complete. Book ready in: {BOOK_DIR}")
    print(f"{'=' * 60}")

    # 4. Optionally build
    if '--build' in sys.argv:
        print("\nBuilding book...")
        import subprocess
        jb_exe = shutil.which('jupyter-book')
        if jb_exe is None:
            import sysconfig
            scripts = sysconfig.get_path('scripts')
            jb_exe = os.path.join(scripts, 'jupyter-book')
        result = subprocess.run(
            [jb_exe, 'build', BOOK_DIR],
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
