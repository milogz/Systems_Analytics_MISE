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
    notebook_path = r"c:\Users\ch.gomez171\Documents\GitHub\Systems_Analytics_MISE\notebooks\saga_06_gobernanza.ipynb"
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    cells = nb['cells']
    
    # 1. ADD 'Dos miradas' after Ostrom analysis (cell 8)
    dos_miradas_1 = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source("### 🔍 Dos miradas\n\n- **Convencional:** \"El marco regulatorio cumple con mejores prácticas (separación de funciones, mercado competitivo)\"\n- **Complejo:** \"La gobernanza policéntrica (Ostrom) revela que el SIN cumple bien los principios técnicos (monitoreo, límites) pero falla en representación de comunidades locales y mecanismos de resolución de conflictos. El caso Windpeshi demuestra que la 'eficiencia' del marco regulatorio se mide diferente según la capa del sistema.\"\n- **Diferencia:** \"Una transición energética técnicamente óptima fracasa si no resuelve la dimensión social. La complejidad está en las interacciones ENTRE capas, no dentro de cada capa.\"")
    }
    cells.insert(9, dos_miradas_1)
    
    # 2. ADD 'Dos miradas' after multi-layer analysis (was cell 18, now 19)
    dos_miradas_2 = {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": split_source("### 🔍 Dos miradas\n\n- **Convencional:** \"Cada dimensión (técnica, económica, social, ambiental) se analiza por separado\"\n- **Complejo:** \"El análisis multi-capa revela que la gobernanza es la META-CAPA: determina cómo se diseñan las redes, cómo reaccionan los actores, cómo fluye la información. Las crisis emergen cuando las capas están desacopladas.\"")
    }
    cells.insert(20, dos_miradas_2)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        
    print("Notebook 06 modified.")
    
    subprocess.run(["python", "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--ExecutePreprocessor.timeout=180", notebook_path, "--output", "saga_06_gobernanza.ipynb"], check=True)
    print("Notebook 06 executed.")

if __name__ == '__main__':
    main()
