import streamlit as st
from algorithms.a_star import a_star_search
from components.grid_component import grid_selector
import numpy as np

st.set_page_config(page_title="Pathfinder Visualizer", layout="wide")

st.title("🧠 Algoritmos de Búsqueda de Caminos")
st.sidebar.markdown("### Configuración")
modo = st.sidebar.selectbox("Selecciona Algoritmo", ["A*", "Dijkstra (Próximamente)"])

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("##### Dibuja los muros en la cuadrícula y pulsa Confirmar")
    # Invocamos nuestro componente JS
    grid_result = grid_selector(rows=20, cols=20)

with col2:
    st.markdown("##### Resultados")
    if grid_result:
        # Definimos inicio y fin fijos por ahora para el MVP
        inicio = (0, 0)
        fin = (19, 19)
        
        if st.button("🚀 Ejecutar Búsqueda"):
            camino = a_star_search(grid_result, inicio, fin)
            
            if camino:
                st.success(f"¡Camino encontrado! Pasos: {len(camino)}")
                st.write(camino)
            else:
                st.error("No hay camino posible entre los puntos.")
