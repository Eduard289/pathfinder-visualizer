import os
import streamlit.components.v1 as components

# 1. Localización del frontend:
# Obtenemos la ruta de la carpeta donde está este archivo .py
parent_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Declaración del componente:
# Buscamos el archivo 'index.html' en esa misma carpeta
_component_func = components.declare_component(
    "grid_selector",
    path=parent_dir
)

# 3. Función de interfaz para app.py:
def grid_selector(path=None, key=None):
    """
    Se comunica con el JavaScript del index.html.
    - path: Lista de coordenadas del camino calculado en Python.
    - key: Identificador único para Streamlit.
    """
    return _component_func(path=path, key=key, default=[])
