import json
import uuid

def split_source(text):
    lines = text.split('\n')
    result = [line + '\n' for line in lines[:-1]]
    if lines[-1]:
        result.append(lines[-1])
    return result

file_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_01_identidad.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb.get("cells", [])

# Find original cell 9 (the one with resumen_generacion)
idx_gen = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "code" and "colombia_sin.resumen_generacion()" in "".join(c["source"]):
        idx_gen = i
        break

if idx_gen != -1:
    # 1. Add code cell after cell 9
    new_code_source = """from mise_utils import data_loader
try:
    cap_recursos = data_loader.capacidad_por_recurso()
    print(f"Comparación: 10 generadores (hardcoded) vs {len(cap_recursos)} recursos (real)")
    display(cap_recursos.sort_values('capacidad_MW', ascending=False).head(10))
except Exception as e:
    print('Error cargando datos reales:', e)"""
    new_code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "outputs": [],
        "source": split_source(new_code_source)
    }
    cells.insert(idx_gen + 1, new_code_cell)

# Find where to add Dos miradas (after the Hallazgo clave cell about concentration)
idx_hallazgo = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "markdown" and "3 mayores generadores" in "".join(c["source"]):
        idx_hallazgo = i
        break

if idx_hallazgo != -1:
    # 2. Add Dos miradas after Hallazgo clave
    dos_miradas_source = """🔍 **Dos miradas**
* **Convencional:** 3 empresas concentran 60% — medido por HHI el mercado es moderadamente concentrado.
* **Complejo:** La concentración no es un número estático — es path-dependent (privatización 1994, fusiones 2000s). Un generador que también es distribuidor y comercializador (EPM) tiene poder de mercado invisible al HHI. Las interdependencias funcionales crean bucles de refuerzo que amplifican la concentración.
* **Diferencia:** El regulador que mira solo HHI pierde la dimensión dinámica y estructural del poder de mercado."""
    dos_miradas_cell = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source(dos_miradas_source)
    }
    cells.insert(idx_hallazgo + 1, dos_miradas_cell)

# 3. Add bridge markdown cell at the end
bridge_source = "Con la identidad del sistema establecida, la Saga 0 (Radiografía de Datos) nos mostró que los datos tienen estructura fat-tailed y relaciones no-lineales. Las siguientes sagas explorarán la topología de las redes (Saga 2) y la dinámica temporal (Saga 4)."
bridge_cell = {
    "cell_type": "markdown",
    "id": str(uuid.uuid4())[:8],
    "metadata": {},
    "source": split_source(bridge_source)
}
cells.append(bridge_cell)

nb["cells"] = cells

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")
