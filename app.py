import streamlit as st
from algorithms.a_star import a_star_search
from components.grid_component import grid_selector

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Pathfinder Visualizer", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
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
    """, unsafe_allow_html=True)

# --- ESTADO DE LA SESIÓN ---
if "camino" not in st.session_state:
    st.session_state.camino = []

# --- ENCABEZADO Y CRÉDITOS ---
st.title("🧠 Visualizador de Algoritmos: Pathfinder")
st.markdown("**Desarrollado por Jose Luis Asenjo** 👨‍💻")

# --- INSTRUCCIONES DESPLEGABLES ---
with st.expander("📖 Instrucciones de uso", expanded=False):
    st.markdown("""
    1. **Dibuja los muros:** Haz clic o mantén pulsado el ratón sobre la cuadrícula para crear obstáculos negros.
    2. **Confirma el mapa:** Pulsa el botón azul que dice *'Confirmar Mapa y Enviar'* (debajo del dibujo).
    3. **Calcula la ruta:** Ve al panel de la derecha y pulsa *'🚀 Calcular Ruta'*.
    4. **Borrar todo:** Usa el botón negro de *'Limpiar'* debajo del mapa y luego el de *'🧹 Resetear'* a la derecha.
    """)

# --- DISEÑO A DOS COLUMNAS ---
col_viz, col_ctrl = st.columns([3, 1])

with col_viz:
    # Renderizamos la cuadrícula interactiva de JavaScript
    grid_result = grid_selector(path=st.session_state.camino, key="grid_main")

with col_ctrl:
    st.subheader("🛠️ Controles")
    
    # Panel de diagnóstico
    if grid_result:
        muros_detectados = sum(sum(fila) for fila in grid_result)
        st.info(f"🧱 Muros detectados en Python: {muros_detectados}")
    else:
        st.info("Dibuja y pulsa 'Confirmar Mapa y Enviar'")

    # --- BOTONES DE ACCIÓN ---
    if st.button("🚀 Calcular Ruta"):
        if grid_result:
            inicio = (0, 0)
            fin = (19, 19)
            
            with st.spinner('Calculando ruta óptima...'):
                ruta = a_star_search(grid_result, inicio, fin)
            
            if ruta:
                st.session_state.camino = ruta
                st.success(f"✅ ¡Ruta encontrada! ({len(ruta)} pasos)")
                st.rerun() 
            else:
                # AQUÍ ESTÁ EL ARREGLO DEL MENSAJE DE ERROR
                # Al no tener st.rerun() aquí, el error se queda en pantalla
                st.error("❌ Sin salida: Los muros bloquean todas las opciones posibles.")
                st.session_state.camino = []
        else:
            st.warning("⚠️ Primero confirma el mapa en la cuadrícula.")

    st.markdown("---")
    
    if st.button("🧹 Resetear"):
        st.session_state.camino = []
        st.rerun()

# --- CAJA DE COMENTARIOS TÉCNICOS ---
st.markdown("---")
st.subheader("💡 Sobre el Algoritmo y el Código")
st.info("""
**El Algoritmo A\* (A-Star):**
Es uno de los algoritmos de búsqueda de rutas más eficientes. Funciona evaluando dos valores para cada casilla: 
el coste real desde el inicio, y una estimación matemática (heurística de Manhattan) de la distancia hasta la meta. 
Esto le permite priorizar el camino más directo, esquivando obstáculos de forma inteligente sin probar opciones inútiles.

**Arquitectura del Proyecto:**
Esta aplicación utiliza un enfoque *Full-Stack* integrado. El Frontend interactivo (la cuadrícula de dibujo) está construido 
con **HTML, CSS y Vanilla JavaScript**, y se comunica bidireccionalmente en tiempo real mediante un *Custom Component* con el 
Backend en **Python** (Streamlit), donde reside la lógica pesada del algoritmo.
""")
