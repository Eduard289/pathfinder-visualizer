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
        border: 1px solid white;
    }
    </style>
    """, unsafe_allow_html=True) # Corregido: parámetro oficial de Streamlit

# --- INICIALIZACIÓN DEL ESTADO ---
# Mantenemos el camino en la sesión para que JavaScript pueda leerlo tras el cálculo
if "camino" not in st.session_state:
    st.session_state.camino = []

# --- SIDEBAR / CONTROLES ---
st.sidebar.title("🛠️ Panel de Control")
st.sidebar.markdown("---")

st.sidebar.info("""
**Guía de uso:**
1. **Dibuja**: Haz clic o arrastra en la cuadrícula para crear muros azules.
2. **Sincroniza**: Pulsa el botón **'Confirmar Mapa'** que aparece bajo la cuadrícula.
3. **Ejecuta**: Pulsa el botón azul de la derecha **'🚀 Calcular Ruta'**.
""")

if st.sidebar.button("🧹 Limpiar Todo"):
    st.session_state.camino = []
    st.rerun()

# --- CUERPO PRINCIPAL ---
st.title("🧠 Pathfinder Visualizer: Algoritmo A*")
st.write("Visualización interactiva de búsqueda de caminos en tiempo real usando Python y JavaScript.")

# Layout de dos columnas: Mapa y Estadísticas
col_mapa, col_stats = st.columns([3, 1])

with col_mapa:
    # Llamada al componente personalizado
    # 'grid_result' recibe la matriz de muros desde JavaScript
    grid_result = grid_selector(
        path=st.session_state.camino,
        key="main_grid_component"
    )

with col_stats:
    st.subheader("📊 Ejecución")
    
    if st.button("🚀 Calcular Ruta"):
        if grid_result:
            # Definimos los puntos de inicio (arriba-izquierda) y fin (abajo-derecha)
            inicio = (0, 0)
            fin = (19, 19)
            
            # Ejecutamos el algoritmo A* definido en algorithms/a_star.py
            with st.spinner('Buscando el camino más corto...'):
                resultado_ruta = a_star_search(grid_result, inicio, fin)
            
            if resultado_ruta:
                st.session_state.camino = resultado_ruta
                st.success("✅ ¡Ruta encontrada!")
                st.metric("Celdas recorridas", len(resultado_ruta))
                st.rerun() # Recarga para que el componente JS reciba el nuevo path
            else:
                st.error("❌ No existe un camino posible.")
                st.session_state.camino = []
        else:
            st.warning("⚠️ Debes confirmar el mapa en la cuadrícula antes de calcular.")

    st.markdown("---")
    st.write("**Leyenda Visual:**")
    st.write("🟩 Inicio | 🟥 Fin")
    st.write("🟦 Muro (Bloqueado)")
    st.write("🟨 Ruta Óptima")

# --- FOOTER ---
st.markdown("---")
st.caption("Desarrollado con Streamlit y Custom Components (HTML5 Canvas/JS).")
