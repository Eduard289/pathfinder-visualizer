import os
import streamlit.components.v1 as _components

# Obtenemos la ruta absoluta del directorio donde se encuentra este archivo
# para localizar el index.html que contiene el Canvas de JavaScript
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Declaramos el componente de Streamlit
# Durante el desarrollo podrías usar url="http://localhost:3001" si usas un servidor node,
# pero para producción y facilidad usamos el path directo al archivo.
_component_func = _components.declare_component(
    "grid_selector",
    path=PARENT_DIR
)

def grid_selector(rows=20, cols=20, path=None, key=None):
    """
    Crea una cuadrícula interactiva mediante JavaScript.
    
    Args:
        rows (int): Número de filas de la cuadrícula.
        cols (int): Número de columnas de la cuadrícula.
        path (list): Lista de tuplas [(r, c), ...] calculadas por Python para dibujar.
        key (str): Un identificador único para el componente en Streamlit.
        
    Returns:
        list: Una matriz bidimensional (lista de listas) donde 0 es libre y 1 es muro.
    """
    
    # Llamamos a la función del componente pasando los argumentos que 
    # JavaScript recibirá en 'window.addEventListener("message", ...)'
    component_value = _component_func(
        rows=rows, 
        cols=cols, 
        path=path, 
        key=key, 
        default=[]
    )
    
    return component_value
