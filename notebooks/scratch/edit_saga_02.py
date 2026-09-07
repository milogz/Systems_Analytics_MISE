import json
import uuid

def split_source(text):
    lines = text.split('\n')
    result = [line + '\n' for line in lines[:-1]]
    if lines[-1]:
        result.append(lines[-1])
    return result

file_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_02_estructura_fisica.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb.get("cells", [])

# Find where it creates networks (Cell 3)
idx_crear = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "code" and "crear_red_sin_simplificada" in "".join(c["source"]):
        idx_crear = i
        break

if idx_crear != -1:
    new_code_source = """from mise_utils import data_loader
import networkx as nx
import matplotlib.pyplot as plt

try:
    plantas_df = data_loader.capacidad_por_recurso().dropna(subset=['CompanyCode', 'capacidad_MW'])
    G_plantas = nx.Graph()
    for _, row in plantas_df.iterrows():
        G_plantas.add_node(row['Code'], name=row['Name'], capacity=row['capacidad_MW'], company=row['CompanyCode'])
    
    # Conectar plantas de la misma empresa
    companies = plantas_df['CompanyCode'].unique()
    for comp in companies:
        comp_plants = plantas_df[plantas_df['CompanyCode'] == comp]['Code'].tolist()
        for i in range(len(comp_plants)):
            for j in range(i+1, len(comp_plants)):
                G_plantas.add_edge(comp_plants[i], comp_plants[j])
    
    print(f"Red de Plantas Reales: {G_plantas.number_of_nodes()} nodos, {G_plantas.number_of_edges()} enlaces (conectadas por empresa)")
except Exception as e:
    print('Error creando red de plantas:', e)"""
    new_code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "outputs": [],
        "source": split_source(new_code_source)
    }
    cells.insert(idx_crear + 1, new_code_cell)


# Find where to add Dos miradas (after network metrics, cell 9 or 12)
idx_metrics = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "markdown" and "Las subestaciones San_Carlos" in "".join(c["source"]):
        idx_metrics = i
        break

if idx_metrics != -1:
    dos_miradas_source = """🔍 **Dos miradas**
* **Convencional:** The network has X nodes and Y edges, average degree Z.
* **Complejo:** The degree distribution reveals heterogeneity — a few hub nodes (large hydro plants of EPM/ISAGEN) concentrate connectivity. The network is resilient to random failures but fragile to targeted attacks on hubs (scale-free property).
* **Diferencia:** Uniform redundancy planning wastes resources. Complex analysis directs investment to protect the critical hubs."""
    dos_miradas_cell = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source(dos_miradas_source)
    }
    cells.insert(idx_metrics + 1, dos_miradas_cell)

nb["cells"] = cells

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")
