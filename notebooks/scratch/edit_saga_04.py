import json
import uuid

def split_source(text):
    lines = text.split('\n')
    result = [line + '\n' for line in lines[:-1]]
    if lines[-1]:
        result.append(lines[-1])
    return result

file_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_04_dinamica.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb.get("cells", [])

# Replace Cell 3
idx_cell3 = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "code" and "colombia_sin.datos_historicos_colombia()" in "".join(c["source"]):
        idx_cell3 = i
        break

if idx_cell3 != -1:
    new_cell3_source = """from mise_utils import data_loader
hist = data_loader.serie_anual_integrada()
display(hist.head())

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(hist['year'], hist['generacion_GWh'], color=viz.COLORS.get('primary', 'blue'), linewidth=2, label='Generación (GWh)')
ax1.plot(hist['year'], hist['demanda_max_MW'], color=viz.COLORS.get('secondary', 'green'), linewidth=2, linestyle='--', label='Demanda Máxima (MW)')
ax1.set_xlabel('Año')
ax1.set_ylabel('GWh / MW', color=viz.COLORS.get('primary', 'blue'))

ax2 = ax1.twinx()
ax2.plot(hist['year'], hist['precio_avg'], color=viz.COLORS.get('danger', 'red'), linewidth=1.5, label='Precio Promedio')
ax2.set_ylabel('Precio', color=viz.COLORS.get('danger', 'red'))

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.title('Evolución histórica con Datos Reales XM', fontweight='bold')
plt.show()"""
    cells[idx_cell3]["source"] = split_source(new_cell3_source)

# Replace Cell 4 (markdown)
idx_cell4 = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "markdown" and "Los datos históricos revelan un patrón cíclico claro" in "".join(c["source"]):
        idx_cell4 = i
        break
if idx_cell4 != -1:
    cells[idx_cell4]["source"] = split_source("**Hallazgo Clave:** Los datos reales (Saga 0) confirman: curtosis=22, ciclos de 7-12 años, relación exponencial embalse-precio.")

# Replace Cell 18 (validation plot)
idx_cell18 = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "code" and "Validación Cualitativa: Modelo vs Historia" in "".join(c["source"]):
        idx_cell18 = i
        break
if idx_cell18 != -1:
    new_cell18_source = """from mise_utils import data_loader
precio_real = data_loader.precio_bolsa_anual()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(precio_real['year'], precio_real['precio_promedio'], color=viz.COLORS.get('primary', 'blue'), linewidth=2, label='Precio Real (XM)')

if 'año' in df_cxc.columns and 'precio' in df_cxc.columns:
    # Ajustar para alinear años de inicio, asumiendo que df_cxc empieza en 0 y lo mapeamos a 2000
    años_modelo = df_cxc['año']
    if años_modelo.min() < 1900:
        años_modelo = años_modelo + 2000
    ax.plot(años_modelo, df_cxc['precio'], color=viz.COLORS.get('accent', 'orange'), linewidth=2, linestyle='--', label='Precio (Modelo)')

ax.set_xlabel('Año')
ax.set_ylabel('Precio')
ax.set_title('Validación: Precio Real vs Modelo SD', fontweight='bold')
ax.legend()
plt.show()"""
    cells[idx_cell18]["source"] = split_source(new_cell18_source)

# ADD Dos miradas after cell 7 (model intro)
idx_cell7 = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "markdown" and "El modelo reproduce oscilaciones endógenas" in "".join(c["source"]):
        idx_cell7 = i
        break
if idx_cell7 != -1:
    dos_miradas1_source = """🔍 **Dos miradas**
* **Convencional:** La capacidad crece linealmente con la inversión. Proyectemos con tendencia.
* **Complejo:** Las oscilaciones son ENDÓGENAS — emergen del retardo de construcción + retroalimentación no-lineal precio-inversión. No necesitas El Niño para tener crisis: la crisis es una propiedad emergente del sistema.
* **Diferencia:** UPME proyecta linealmente. El modelo SD predice oscilaciones que ninguna regresión lineal captura."""
    cells.insert(idx_cell7 + 1, {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source(dos_miradas1_source)
    })

# ADD Dos miradas after CxC analysis (cell 16)
idx_cell16 = -1
for i, c in enumerate(cells):
    if c["cell_type"] == "markdown" and "El CxC reduce la volatilidad" in "".join(c["source"]):
        idx_cell16 = i
        break
if idx_cell16 != -1:
    dos_miradas2_source = """🔍 **Dos miradas**
* **Convencional:** El CxC estabiliza precios — es una buena política.
* **Complejo:** El CxC crea un loop de estabilización que puede generar lock-in térmico. La señal de precio de mercado se amortigua, pero la dependencia estructural a gas/carbón se consolida. Es un 'Fixes that Fail' de los arquetipos de SD."""
    cells.insert(idx_cell16 + 1, {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source(dos_miradas2_source)
    })

nb["cells"] = cells

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")
