import streamlit as st
from algorithms.a_star import a_star_search
from components.grid_component import grid_selector

# Configuración inicial de la página
st.set_page_config(page_title="Pathfinder Visualizer", layout="wide")

# Inyección de CSS corregida
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True) # Parámetro corregido para evitar el TypeError

# Estado de la sesión para el camino
if "camino" not in st.session_state:
    st.session_state.camino = []

st.title("🧠 Visualizador de Algoritmos: Pathfinder")
st.write("Dibuja obstáculos y observa cómo el algoritmo A* encuentra la ruta más eficiente.")

col_viz, col_ctrl = st.columns([3, 1])

with col_viz:
    # Invocación del componente. Si falla aquí, revisa la estructura de carpetas
    grid_result = grid_selector(path=st.session_state.camino, key="grid_main")

with col_ctrl:
    st.subheader("Controles")
    if st.button("🚀 Calcular Ruta"):
        if grid_result:
            inicio, fin = (0, 0), (19, 19)
            with st.spinner('Calculando...'):
                ruta = a_star_search(grid_result, inicio, fin) # Lógica en algorithms/a_star.py
            
            if ruta:
                st.session_state.camino = ruta
                st.success(f"Ruta encontrada: {len(ruta)} pasos")
                st.rerun() # Forzar render para enviar el camino al componente
            else:
                st.error("No hay camino posible.")
        else:
            st.warning("Dibuja muros y pulsa 'Confirmar' en la cuadrícula.")

    if st.button("🧹 Resetear"):
        st.session_state.camino = []
        st.rerun()
