import json
import uuid

def split_source(text):
    lines = text.split('\n')
    result = [line + '\n' for line in lines[:-1]]
    if lines[-1]:
        result.append(lines[-1])
    return result

file_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_03_estructura_social.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb.get("cells", [])

# Find where to add Dos miradas (after cell 5 - "La CREG y el MME")
idx_creg = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "markdown" and "La CREG y el MME son los nodos" in "".join(c["source"]):
        idx_creg = i
        break

if idx_creg != -1:
    dos_miradas_source = """🔍 **Dos miradas**
* **Convencional:** 8 institutions with defined regulatory roles.
* **Complejo:** Betweenness centrality reveals who actually controls information/power flows — and it's not always the most connected actor. XM as operator sits in the middle of all market information."""
    dos_miradas_cell = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source(dos_miradas_source)
    }
    cells.insert(idx_creg + 1, dos_miradas_cell)

nb["cells"] = cells

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")
