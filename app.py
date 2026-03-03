import streamlit as st
from algorithms.a_star import a_star_search
from components.grid_component import grid_selector

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Pathfinder Visualizer", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

if "camino" not in st.session_state:
    st.session_state.camino = []

st.title("🧠 Visualizador de Algoritmos: Pathfinder")
st.write("Dibuja obstáculos y observa cómo el algoritmo A* encuentra la ruta más eficiente.")

col_viz, col_ctrl = st.columns([3, 1])

with col_viz:
    grid_result = grid_selector(path=st.session_state.camino, key="grid_main")

with col_ctrl:
    st.subheader("Controles")
    
    # --- PANEL DE DIAGNÓSTICO ---
    if grid_result:
        muros_detectados = sum(sum(fila) for fila in grid_result)
        st.info(f"🧱 Muros detectados en Python: {muros_detectados}")
    else:
        st.info("Dibuja y pulsa Confirmar Mapa")

    if st.button("🚀 Calcular Ruta"):
        if grid_result:
            inicio, fin = (0, 0), (19, 19)
            with st.spinner('Calculando...'):
                ruta = a_star_search(grid_result, inicio, fin)
            
            if ruta:
                st.session_state.camino = ruta
                st.success(f"¡Ruta encontrada!")
                st.rerun() 
            else:
                st.error("No hay camino.")
                st.session_state.camino = []
                st.rerun()
        else:
            st.warning("Confirma el mapa en la cuadrícula.")

    if st.button("🧹 Resetear"):
        st.session_state.camino = []
        st.rerun()
