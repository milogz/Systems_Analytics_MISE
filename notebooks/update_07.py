import json
import uuid
import sys
import subprocess

def split_source(text):
    lines = text.split("\n")
    result = [line + "\n" for line in lines[:-1]]
    if lines[-1]:
        result.append(lines[-1])
    return result

def main():
    notebook_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_07_sintesis.ipynb"
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    cells = nb['cells']
    
    # 1. ADD code cell near the beginning
    new_code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "outputs": [],
        "source": split_source("from mise_utils import data_loader\nserie = data_loader.serie_anual_integrada()\ncap = data_loader.capacidad_por_tipo()\nprint('DATOS REALES BASE:')\nprint(f'  Generación 2024: {serie[serie.year==2024].generacion_GWh.values[0]/1000:.0f} TWh')\nprint(f'  Precio 2024: {serie[serie.year==2024].precio_avg.values[0]:.0f} COP/kWh')\nprint(f'  Capacidad total: {cap.capacidad_MW.sum():.0f} MW ({cap.iloc[0][\"Type\"]} = {cap.iloc[0][\"share_capacidad\"]:.0f}%)')")
    }
    cells.insert(2, new_code_cell)
    
    # After inserting at 2, old index 3 becomes 4.
    # 2. UPDATE executive summary (was cell 3, now cell 4)
    summary_text = """El SIN colombiano enfrenta un momento crítico de transición energética que demanda visión sistémica. Los hallazgos integrados (respaldados por 25 años de datos públicos verificados de XM) revelan que:
- El sistema es complejo, con múltiples generadores principales, mostrando una concentración moderada-alta y vulnerabilidades críticas en la red de transmisión.
- El ciclo endógeno de inversión-capacidad produce oscilaciones estructurales a lo largo de los años.
- La estrategia Diversificada es la más robusta bajo 4 escenarios.
- La dimensión de gobernanza (consulta previa, justicia energética) es el cuello de botella de la transición.

**El SIN necesita intervención en tres frentes simultáneos: infraestructura de red (reducir vulnerabilidades N-1), regulación de mercado (evitar lock-in térmico), y gobernanza social (legitimar la transición)**"""
    
    cells[4]['source'] = split_source(summary_text)
    
    # 3. ADD 'Dos miradas' section before the closing
    # "## 7.7 Cierre y Exportación del Informe" was at index 20.
    # Because we inserted 1 cell at index 2, old index 20 is now 21.
    # We want to insert before it, so at index 21.
    
    dos_miradas = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source("### 🔍 Dos miradas\n\n- **Convencional:** \"Recomendamos invertir en X MW de renovables al costo de $Y. Retorno esperado: Z%.\"\n- **Complejo:** \"Recomendamos una ESTRATEGIA ADAPTATIVA: (1) monitorear indicadores líderes (embalses, pipeline, margen), (2) definir umbrales de acción (embalse<40% → activar reserva), (3) ajustar la estrategia en función del estado del sistema. La diferencia entre un PLAN y una ESTRATEGIA ADAPTATIVA es que el segundo aprende del sistema.\"\n- **Diferencia:** \"El plan óptimo falla cuando el mundo cambia. La estrategia adaptativa evoluciona con el sistema. Esta es la esencia de la consultoría sistémica.\"")
    }
    cells.insert(21, dos_miradas)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        
    print("Notebook 07 modified.")
    
    subprocess.run(["python", "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--ExecutePreprocessor.timeout=180", notebook_path, "--output", "saga_07_sintesis.ipynb"], check=True)
    print("Notebook 07 executed.")

if __name__ == '__main__':
    main()
