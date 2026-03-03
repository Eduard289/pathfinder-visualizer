import streamlit as st
from algorithms.a_star import a_star_search
from components.grid_component import grid_selector

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Pathfinding Visualizer Pro",
    page_icon="🧠",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS (CORREGIDO) ---
# Cambiamos unsafe_allow_status_code por unsafe_allow_html
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        height: 3em; 
        background-color: #007bff; 
        color: white; 
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True) # Parámetro corregido aquí

# --- INICIALIZACIÓN DEL ESTADO ---
# Mantenemos el camino en la sesión para que persista tras el cálculo
if "camino" not in st.session_state:
    st.session_state.camino = []

# --- SIDEBAR / PANEL DE CONTROL ---
st.sidebar.title("🛠️ Configuración")
st.sidebar.markdown("---")
st.sidebar.info("""
**Instrucciones:**
1. Dibuja los muros en la cuadrícula (clic o arrastrar).
2. Haz clic en **'Confirmar Mapa'** bajo el lienzo.
3. Pulsa el botón **'🚀 Calcular Ruta'**.
""")

if st.sidebar.button("🧹 Resetear"):
    st.session_state.camino = []
    st.rerun()

# --- CUERPO PRINCIPAL ---
st.title("🧠 Visualizador de Algoritmos: Pathfinder")
st.write("Dibuja obstáculos y observa cómo el algoritmo A* encuentra la ruta más eficiente.")

col_visual, col_ctrl = st.columns([3, 1])

with col_visual:
    # Llamamos al componente de JS pasando el camino actual
    grid_result = grid_selector(
        path=st.session_state.camino,
        key="main_grid"
    )

with col_ctrl:
    st.subheader("📊 Ejecución")
    
    if st.button("🚀 Calcular Ruta"):
        if grid_result:
            inicio = (0, 0)
            fin = (19, 19)
            
            # Ejecutamos la lógica de búsqueda en Python
            with st.spinner('Procesando...'):
                ruta = a_star_search(grid_result, inicio, fin)
            
            if ruta:
                st.session_state.camino = ruta
                st.success(f"✅ ¡Éxito!")
                st.metric("Pasos", len(ruta))
                st.rerun() # Recarga para enviar la ruta al componente
            else:
                st.error("❌ Sin salida")
                st.session_state.camino = []
        else:
            st.warning("⚠️ Confirma el mapa primero.")

st.markdown("---")
st.caption("Hecho con Streamlit y Custom Components (HTML/JS).  Jose Luis Asenjo")
