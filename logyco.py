"""
LogiCo, una empresa de distribución y logística, enfrenta el desafío de optimizar su sistema de entrega de productos para aumentar la eficiencia y reducir costos. Con múltiples ubicaciones dispersas por una región específica, la planificación de rutas se vuelve compleja, especialmente al considerar variables temporales y costos asociados.

Para abordar este problema, LogiCo ha decidido utilizar el algoritmo de Dijkstra, ampliamente utilizado en la teoría de grafos, para encontrar rutas óptimas en su red de distribución y logística. En este enfoque, las ubicaciones clave, como almacenes, centros de distribución y tiendas se representan como nodos en un grafo, donde las aristas indican las rutas posibles entre ellos.

La novedad radica en la consideración de variables temporales y costos asociados a cada ruta. LogiCo incluirá aspectos como cierres viales por derrumbes, condiciones climáticas adversas y la presencia de peajes en la planificación de rutas. Estos factores cambiantes influirán en la elección de la ruta más corta y óptima, minimizando tanto la distancia recorrida como los costos asociados.

Al acotar el problema a una región específica, LogiCo puede tener en cuenta las características locales y adaptar sus decisiones de planificación en consecuencia. Esto incluye tener en cuenta los cierres viales temporales, la presencia de peajes en ciertas rutas y la variabilidad climática de la región. Considerando estos aspectos, el algoritmo de Dijkstra permitirá a LogiCo determinar las rutas más eficientes, minimizando los tiempos y costos de entrega.

Al utilizar el algoritmo de Dijkstra con variables temporales y costos, LogiCo logrará optimizar su sistema de distribución y logística. La capacidad de adaptarse a condiciones cambiantes en tiempo real permitirá a la empresa responder de manera eficiente a situaciones imprevistas, brindando un servicio de entrega rápido y rentable.
"""

import heapq
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_info in graph[current_node].items():
            distance = current_distance + edge_info['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def get_route(graph, start, end):
    distances = dijkstra(graph, start)
    route = [end]
    current_node = end

    while current_node != start:
        neighbors = graph[current_node]
        min_distance = float('inf')
        min_neighbor = None

        for neighbor, edge_info in neighbors.items():
            distance = distances[neighbor]
            if distance < min_distance:
                min_distance = distance
                min_neighbor = neighbor

        if min_neighbor is None:
            break

        route.append(min_neighbor)
        current_node = min_neighbor

    route.reverse()
    return route

# Ejemplo de grafo de distribución y logística con aspectos adicionales (incluyendo costos de peajes)
graph = {
    'Almacén A': {'Calle 1': {'weight': 5, 'peaje': False}, 'Carrera 1': {'weight': 2, 'peaje': False}},
    'Calle 1': {'Centro Distribución B': {'weight': 3, 'peaje': True, 'peaje_costo': 10}, 'Tienda C': {'weight': 4, 'peaje': False}},
    'Carrera 1': {'Centro Distribución B': {'weight': 1, 'peaje': False}, 'Tienda C': {'weight': 4, 'peaje': False}, 'Centro Distribución D': {'weight': 6, 'peaje': False}},
    'Centro Distribución B': {'Almacén A': {'weight': 1, 'peaje': False}, 'Tienda E': {'weight': 3, 'peaje': False}},
    'Tienda C': {'Centro Distribución D': {'weight': 2, 'peaje': False}, 'Tienda G': {'weight': 5, 'peaje': True, 'peaje_costo': 5}},
    'Centro Distribución D': {'Tienda E': {'weight': 2, 'peaje': False}, 'Tienda H': {'weight': 3, 'peaje': False}},
    'Tienda E': {'Tienda G': {'weight': 2, 'peaje': False}},
    'Tienda G': {'Tienda H': {'weight': 2, 'peaje': False}},
    'Tienda H': {}
}

locations = list(graph.keys())  # Lista de ubicaciones disponibles

# Solicitar al usuario ingresar la ubicación de origen
start_node = input("Ingrese la ubicación de origen (Opciones: {}): ".format(', '.join(locations)))
while start_node not in locations:
    print("Ubicación no válida. Intente nuevamente.")
    start_node = input("Ingrese la ubicación de origen (Opciones: {}): ".format(', '.join(locations)))

# Solicitar al usuario ingresar la ubicación de destino
end_node = input("Ingrese la ubicación de destino (Opciones: {}): ".format(', '.join(locations)))
while end_node not in locations:
    print("Ubicación no válida. Intente nuevamente.")
    end_node = input("Ingrese la ubicación de destino (Opciones: {}): ".format(', '.join(locations)))

distances = dijkstra(graph, start_node)
route = get_route(graph, start_node, end_node)

print("Distancias más cortas desde el nodo de inicio (" + start_node + "):")
for node, distance in distances.items():
    print("Nodo:", node, "- Distancia:", distance)

print("\nRuta óptima desde", start_node, "a", end_node, "con sus costos:")
total_cost = 0
for i in range(len(route)-1):
    current_node = route[i]
    next_node = route[i+1]
    edge_info = graph[current_node][next_node]
    cost = edge_info['peaje_costo'] if edge_info['peaje'] else 0
    total_cost += cost
    print("Desde", current_node, "hasta", next_node, "- Costo:", cost)

print("\nCosto total de la ruta:", total_cost)

# Imprimir el grafo
plt.figure(figsize=(10, 10))
pos = {
    'Almacén A': (1, 1),
    'Calle 1': (1, 3),
    'Carrera 1': (3, 1),
    'Centro Distribución B': (3, 3),
    'Tienda C': (3, 5),
    'Centro Distribución D': (5, 1),
    'Tienda E': (5, 3),
    'Tienda G': (5, 5),
    'Tienda H': (7, 3)
}
labels = {
    'Almacén A': 'Almacén A',
    'Calle 1': 'Calle 1',
    'Carrera 1': 'Carrera 1',
    'Centro Distribución B': 'Centro Distribución B',
    'Tienda C': 'Tienda C',
    'Centro Distribución D': 'Centro Distribución D',
    'Tienda E': 'Tienda E',
    'Tienda G': 'Tienda G',
    'Tienda H': 'Tienda H'
}

for node, neighbors in graph.items():
    x, y = pos[node]
    plt.scatter(x, y, color='blue')
    plt.text(x, y, labels[node], fontsize=10, ha='center', va='center')

    for neighbor, edge_info in neighbors.items():
        nx, ny = pos[neighbor]
        plt.plot([x, nx], [y, ny], color='black', alpha=0.5)

        if edge_info['peaje']:
            plt.text((x + nx) / 2, (y + ny) / 2, 'Peaje (Costo: ' + str(edge_info['peaje_costo']) + ')', fontsize=8, ha='center', va='center', color='red')

plt.title('Grafo de Distribución y Logística con Aspectos Adicionales (Peajes)')
plt.xticks([])
plt.yticks([])
plt.show()