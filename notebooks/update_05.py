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
    notebook_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_05_politica.ipynb"
    
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
        "source": split_source("from mise_utils import data_loader\nserie = data_loader.serie_anual_integrada()\nprint(f'Contexto real: precio 2024 = {serie[serie.year==2024].precio_avg.values[0]:.0f} COP/kWh')\nprint(f'Precio promedio histórico = {serie.precio_avg.mean():.0f} COP/kWh')\nprint(f'Los escenarios deben cubrir este rango de variabilidad real')")
    }
    cells.insert(2, new_code_cell)
    
    # After inserting at 2, old indices are shifted by 1.
    # Old cell 11 (code for robustez) is now at 12.
    # 2. ADD Dos miradas after robustness table
    dos_miradas_1 = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source("### 🔍 Dos miradas\n\n- **Convencional:** \"La estrategia de menor costo es [la que el modelo elija]. Recomendamos implementarla.\"\n- **Complejo:** \"La estrategia de menor ARREPENTIMIENTO MÁXIMO (minimax regret) puede ser diferente. Es robusta ante múltiples futuros posibles, no óptima para uno solo. Bajo incertidumbre profunda (Deep Uncertainty, Semana 5), optimizar para un escenario base da la recomendación equivocada en 3 de 4 futuros posibles.\"\n- **Diferencia:** \"Un consultor convencional optimiza. Un consultor de sistemas diseña para robustez.\"")
    }
    cells.insert(13, dos_miradas_1)
    
    # After inserting at 13, old indices are shifted by 2 overall for things after 13.
    # Old cell 13 (code for sensitivity) was at 14 (shifted by 1), now at 15 (shifted by 2).
    # We want to insert after it, so at index 16.
    dos_miradas_2 = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source("### 🔍 Dos miradas\n\n- **Convencional:** \"El parámetro X tiene mayor impacto — controlemos ese parámetro.\"\n- **Complejo:** \"La sensibilidad revela los PUNTOS DE APALANCAMIENTO del sistema (Meadows). No todos los parámetros sensibles son controlables, y no todos los controlables son sensibles. La intersección es donde debe actuar la política.\"\n- **Diferencia:** \"Un consultor convencional optimiza. Un consultor de sistemas diseña para robustez.\"")  # Note difference text says robustez here as per user prompt? Wait, user didn't specify difference for second one, but I can omit it or make something up. The user didn't specify a Diferencia for the second one, so I will only include Convencional and Complejo. Wait, I will just leave out Diferencia.
    }
    
    # Let's check prompt for dos miradas 2:
    # * Convencional: "El parámetro X tiene mayor impacto — controlemos ese parámetro."
    # * Complejo: "La sensibilidad revela los PUNTOS DE APALANCAMIENTO del sistema (Meadows)..."
    dos_miradas_2['source'] = split_source("### 🔍 Dos miradas\n\n- **Convencional:** \"El parámetro X tiene mayor impacto — controlemos ese parámetro.\"\n- **Complejo:** \"La sensibilidad revela los PUNTOS DE APALANCAMIENTO del sistema (Meadows). No todos los parámetros sensibles son controlables, y no todos los controlables son sensibles. La intersección es donde debe actuar la política.\"")
    cells.insert(16, dos_miradas_2)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        
    print("Notebook 05 modified.")
    
    subprocess.run(["python", "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--ExecutePreprocessor.timeout=180", notebook_path, "--output", "saga_05_politica.ipynb"], check=True)
    print("Notebook 05 executed.")

if __name__ == '__main__':
    main()
