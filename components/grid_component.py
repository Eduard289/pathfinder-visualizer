import streamlit.components.v1 as components
import os

# Ruta al directorio donde estará nuestro HTML/JS
parent_dir = os.path.dirname(os.path.abspath(__file__))

def grid_selector(rows=20, cols=20, key=None):
    """
    Crea una cuadrícula interactiva de JS.
    Retorna la matriz de muros (0 y 1).
    """
    # En desarrollo, podemos apuntar a una URL (port 3001) o al archivo index.html
    # Para simplificar ahora, usaremos el método de declarar el HTML directamente
    
    _component_func = components.declare_component(
        "grid_selector",
        path=parent_dir # Aquí buscaremos el index.html
    )
    
    return _component_func(rows=rows, cols=cols, key=key, default=[])
