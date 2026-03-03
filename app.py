import streamlit as st
import numpy as np
from algorithms.a_star import a_star_search
from components.grid_component import grid_selector

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Pathfinding Visualizer Pro",
    page_icon="🧠",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_status_code=True)

# --- INICIALIZACIÓN DEL ESTADO ---
# Usamos session_state para que el camino persista entre renders
if "camino" not in st.session_state:
    st.session_state.camino = []

# --- SIDEBAR (CONTROLES) ---
st.sidebar.title("🛠️ Configuración")
st.sidebar.markdown("---")
algoritmo = st.sidebar.selectbox(
    "Algoritmo de Búsqueda",
    ["A* (Heurística Manhattan)", "Dijkstra (Uniform Cost)"]
)

st.sidebar.info("""
**Instrucciones:**
1. Dibuja los muros en la cuadrícula (clic o arrastrar).
2. Haz clic en **'Confirmar Mapa'** dentro del recuadro.
3. Pulsa el botón **'🚀 Calcular Ruta'** abajo.
""")

if st.sidebar.button("🧹 Resetear Todo"):
    st.session_state.camino = []
    st.rerun()

# --- CUERPO PRINCIPAL ---
st.title("🧠 Visualizador de Algoritmos de Búsqueda")
st.write("Explora cómo la inteligencia artificial encuentra el camino más corto esquivando obstáculos.")

col1, col2 = st.columns([3, 1])

with col1:
    # Invocamos el componente personalizado de JavaScript
    # Enviamos el 'camino' actual para que JS lo dibuje si existe
    resultado_grid = grid_selector(
        rows=20, 
        cols=20, 
        path=st.session_state.camino,
        key="visualizador_principal"
    )

with col2:
    st.subheader("📊 Estadísticas")
    
    if st.button("🚀 Calcular Ruta"):
        if resultado_grid:
            # Definimos puntos de inicio (Top-Left) y fin (Bottom-Right)
            inicio = (0, 0)
            fin = (19, 19)
            
            # Ejecutamos la lógica de búsqueda en Python
            with st.spinner('Calculando ruta óptima...'):
                ruta = a_star_search(resultado_grid, inicio, fin)
            
            if ruta:
                st.session_state.camino = ruta
                st.success(f"✅ ¡Ruta encontrada!")
                st.metric("Longitud del camino", f"{len(ruta)} celdas")
                st.rerun() # Forzamos recarga para enviar la ruta al componente JS
            else:
                st.error("❌ No hay camino posible.")
                st.session_state.camino = []
        else:
            st.warning("⚠️ Primero dibuja muros y pulsa 'Confirmar' en la cuadrícula.")

    st.markdown("---")
    st.write("**Leyenda:**")
    st.markdown("- 🟩 **Inicio:** (0,0)")
    st.markdown("- 🟥 **Fin:** (19,19)")
    st.markdown("- 🟦 **Muros:** Bloquean el paso")
    st.markdown("- 🟨 **Ruta:** Camino más corto")

# --- FOOTER ---
st.markdown("---")
st.caption("Proyecto desarrollado con Streamlit (Python) y JavaScript Custom Components.")
