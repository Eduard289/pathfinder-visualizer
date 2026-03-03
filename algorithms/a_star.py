import heapq

def heuristic(a, b):
    # Usamos la distancia Manhattan para la cuadrícula
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """
    grid: Matriz de 0 (libre) y 1 (muro)
    start: Tupla (x, y)
    goal: Tupla (x, y)
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Cola de prioridad: (prioridad_total, costo_actual, nodo, camino)
    queue = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()

    while queue:
        (priority, cost, current, path) = heapq.heappop(queue)

        if current in visited:
            continue
        
        path = path + [current]
        
        if current == goal:
            return path

        visited.add(current)

        # Movimientos: Arriba, Abajo, Izquierda, Derecha
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    new_cost = cost + 1
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (priority, new_cost, neighbor, path))
    
    return None # No hay camino
