# Pathfinder Visualizer

## Descripción General
Pathfinder Visualizer es una aplicación web *full-stack* diseñada para demostrar la ejecución del algoritmo de búsqueda A* (A-Star) en tiempo real. Construido sobre el framework Streamlit, el proyecto implementa un puente de comunicación bidireccional entre un backend analítico en Python y un frontend interactivo en Vanilla JavaScript, permitiendo la manipulación de cuadrículas espaciales y el cálculo algorítmico de alto rendimiento.

## Arquitectura Técnica
La aplicación sigue una arquitectura desacoplada utilizando *Streamlit Custom Components* para separar el estado de la interfaz de usuario del procesamiento matemático.

* **Frontend (HTML5 / CSS3 / Vanilla JS):**
    * Renderiza una cuadrícula dinámica de 20x20 mediante *CSS Grid*.
    * Gestiona la entrada del usuario (eventos del ratón) para la generación de obstáculos (muros) en tiempo real.
    * Implementa la API de componentes de Streamlit a través del protocolo `window.parent.postMessage` para enviar el estado de la matriz al backend mediante copias profundas (`JSON.parse(JSON.stringify())`).
    * Escucha las actualizaciones de estado desde Python para desencadenar animaciones de rutas asíncronas utilizando bucles no bloqueantes.

* **Backend (Python / Streamlit):**
    * Maneja la persistencia del estado de la sesión (`st.session_state`) y el diseño principal de la interfaz de usuario.
    * Recibe y procesa el array N-dimensional desde el frontend.
    * Ejecuta el algoritmo de búsqueda heurística de forma segura en el lado del servidor, evitando cuellos de botella en la renderización del cliente.

## Implementación Algorítmica: Búsqueda A*
La lógica central utiliza el algoritmo de búsqueda de rutas A*, conocido por su rendimiento y precisión en la navegación basada en cuadrículas espaciales. El algoritmo evalúa los nodos basándose en la función de coste estándar:

$$f(n) = g(n) + h(n)$$

* $g(n)$: El coste exacto del camino desde el nodo inicial hasta cualquier nodo $n$.
* $h(n)$: El coste estimado heurístico desde el nodo $n$ hasta el objetivo.

 En esta implementación, se utiliza la **Distancia de Manhattan** como función heurística, calculada como $|x_1 - x_2| + |y_1 - y_2|$, la cual es matemáticamente óptima para una cuadrícula de movimiento en 4 direcciones (sin desplazamiento diagonal).

La implementación depende del módulo `heapq` de Python para mantener una cola de prioridad (min-heap), asegurando una recuperación eficiente del nodo con la puntuación $f(n)$ más baja. La complejidad temporal es altamente dependiente de la heurística, pero generalmente opera en $O(E \log V)$ bajo condiciones óptimas, incluyendo el manejo estricto de colisiones contra los obstáculos definidos por el usuario.


Jose Luis Asenjo Tornero
