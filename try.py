"""
1. Definir el grafo:
    Crear una estructura de datos para representar el grafo, que contenga nodos y aristas.
    Identificar las ubicaciones relevantes de la empresa y asignar un identificador único a cada una.
    Definir las conexiones entre las ubicaciones mediante aristas, especificando el nodo de origen, el nodo de destino y el peso asociado (distancia o costo).
    Inicializar las estructuras de datos:

2. Crear una lista de nodos visitados y una lista de nodos no visitados.
    Asignar un valor de distancia inicialmente infinito a todos los nodos, excepto al nodo de origen, al cual se le asigna una distancia de 0.
    Implementar el algoritmo de Dijkstra:

3. Iniciar en el nodo de origen y marcarlo como visitado.
    Actualizar las distancias de los nodos adyacentes al nodo actual si se encuentra una ruta más corta.
    Elegir el nodo no visitado con la distancia más corta y marcarlo como visitado.
    Repetir el paso anterior hasta que se visiten todos los nodos o se llegue al nodo de destino, si es necesario.
4. Rastrear la ruta más corta: 
    Al finalizar el algoritmo, se obtendrán las distancias más cortas desde el nodo de origen a todos los demás nodos. Si se necesita encontrar una ruta específica, rastrear los nodos visitados desde el nodo de destino hasta el nodo de origen utilizando la información almacenada durante la ejecución del algoritmo.
5. Analizar y optimizar:
    Analizar los resultados obtenidos y considerar factores adicionales relevantes para optimizar el plan de distribución y logística, como restricciones de capacidad, horarios, preferencias de los clientes, entre otros.
    Realizar ajustes en el grafo o en los pesos de las aristas según sea necesario para mejorar la eficiencia y minimizar los costos asociados a la distribución.
"""

# Importar librerias
import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo
G = nx.Graph()

# Agregar nodos
G.add_node("Bodega Central", pos = (0, 0))
G.add_node("Tienda 1", pos = (0, 1))
G.add_node("Tienda 2", pos = (1, 0))
G.add_node("Tienda 3", pos = (1, 1))
G.add_node("Tienda 4", pos = (0, 2))
G.add_node("Tienda 5", pos = (2, 0))
G.add_node("Tienda 6", pos = (2, 1))
G.add_node("Tienda 7", pos = (1, 2))
G.add_node("Tienda 8", pos = (2, 2))
G.add_node("Tienda 9", pos = (0, 3))
G.add_node("Tienda 10", pos = (3, 0))

# Agregar aristas
G.add_edge("Bodega Central", "Tienda 1", weight = 1)
G.add_edge("Bodega Central", "Tienda 2", weight = 2)
G.add_edge("Bodega Central", "Tienda 3", weight = 3)
G.add_edge("Bodega Central", "Tienda 4", weight = 4)
G.add_edge("Bodega Central", "Tienda 5", weight = 5)
G.add_edge("Bodega Central", "Tienda 6", weight = 6)
G.add_edge("Bodega Central", "Tienda 7", weight = 7)
G.add_edge("Bodega Central", "Tienda 8", weight = 8)
G.add_edge("Bodega Central", "Tienda 9", weight = 9)
G.add_edge("Bodega Central", "Tienda 10", weight = 10)
G.add_edge("Tienda 1", "Tienda 2", weight = 11)
G.add_edge("Tienda 2", "Tienda 8", weight = 12)
G.add_edge("Tienda 3", "Tienda 7", weight = 13)
G.add_edge("Tienda 4", "Tienda 10", weight = 14)
G.add_edge("Tienda 10", "Tienda 5", weight = 15)
G.add_edge("Tienda 5", "Tienda 8", weight = 16)
G.add_edge("Tienda 9", "Tienda 7", weight = 17)
G.add_edge("Tienda 9", "Tienda 8", weight = 18)


# Obtener posiciones de los nodos
pos = nx.get_node_attributes(G, 'pos')

# Dibujar grafo
nx.draw(G, pos, with_labels = True)
# Obtener pesos de las aristas
labels = nx.get_edge_attributes(G, 'weight')
# Dibujar pesos de las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
plt.show()

# Algoritmo de Dijkstra
# Distancia mas corta entre Bodega Central y Tienda 1
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 1'))
# Distancia mas corta entre Bodega Central y Tienda 2
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 2'))
# Distancia mas corta entre Bodega Central y Tienda 3
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 3'))
# Distancia mas corta entre Bodega Central y Tienda 4
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 4'))
# Distancia mas corta entre Bodega Central y Tienda 5
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 5'))
# Distancia mas corta entre Bodega Central y Tienda 6
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 6'))
# Distancia mas corta entre Bodega Central y Tienda 7
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 7'))
# Distancia mas corta entre Bodega Central y Tienda 8
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 8'))
# Distancia mas corta entre Bodega Central y Tienda 9
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 9'))
# Distancia mas corta entre Bodega Central y Tienda 10
print(nx.dijkstra_path(G, 'Bodega Central', 'Tienda 10'))
