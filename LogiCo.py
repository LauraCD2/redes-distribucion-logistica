"""La empresa LogiCo ha decidido optimizar su sistema de distribución y logística para mejorar la eficiencia en la entrega de productos a sus clientes. Actualmente, la empresa tiene varios almacenes, centros de distribución, tiendas y clientes dispersos por todo el país, lo que dificulta la planificación de rutas y la minimización de los costos asociados.

Para abordar esta problemática, LogiCo ha decidido utilizar conceptos de matemáticas discretas y aplicar el algoritmo de Dijkstra, que es ampliamente utilizado en la teoría de grafos. 

En este enfoque, se modelarán las ubicaciones de los almacenes, centros de distribución, tiendas y clientes como nodos en un grafo, donde las aristas representarán las rutas posibles entre estos puntos.

El objetivo principal de LogiCo es encontrar la ruta más corta para la entrega de productos, ya sea minimizando la distancia recorrida o los costos asociados, considerando también otros factores relevantes, como el tiempo estimado de entrega y la disponibilidad de recursos. Para lograr esto, el algoritmo de Dijkstra es una herramienta poderosa y versátil.

El algoritmo de Dijkstra, desarrollado por el matemático Edsger Dijkstra, permite encontrar la ruta más corta desde un nodo de origen hasta todos los demás nodos del grafo. Aplicando este algoritmo en el contexto de LogiCo, la empresa podrá determinar las rutas óptimas para la entrega de productos, considerando las distancias y los costos asociados a cada una.

Al utilizar el algoritmo de Dijkstra, LogiCo podrá planificar las rutas de manera eficiente, minimizando los tiempos y costos de entrega.
"""

# Importar librerías
import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo
G = nx.Graph()

# Crear nodos
G.add_node('Almacén 1', pos=(0, 0))
G.add_node('Almacén 2', pos=(1, 3))
G.add_node('Almacén 3', pos=(2, 2))
G.add_node('Almacén 4', pos=(3, 6))
G.add_node('Almacén 5', pos=(4, 7))
G.add_node('Almacén 6', pos=(5, 2))

# Crear aristas
G.add_edge('Almacén 1', 'Almacén 2', weight=1)
G.add_edge('Almacén 1', 'Almacén 3', weight=2)
G.add_edge('Almacén 2', 'Almacén 3', weight=3)
G.add_edge('Almacén 2', 'Almacén 1', weight=1)
G.add_edge('Almacén 3', 'Almacén 1', weight=2)
G.add_edge('Almacén 4', 'Almacén 2', weight=3)
G.add_edge('Almacén 4', 'Almacén 6', weight=4)
G.add_edge('Almacén 5', 'Almacén 3', weight=5)
G.add_edge('Almacén 5', 'Almacén 6', weight=6)

# Obtener posiciones de nodos
pos = nx.get_node_attributes(G, 'pos')

# Obtener pesos de aristas
weights = nx.get_edge_attributes(G, 'weight')

# Dibujar grafo
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
plt.show()

# Obtener ruta más corta
ruta_corta = nx.shortest_path(G, 'Almacén 5', 'Almacén 3', weight='weight')
distancia_corta = nx.shortest_path_length(G, 'Almacén 5', 'Almacén 3', weight='weight')
print("Ruta más corta:", ruta_corta)
print("Distancia más corta:", distancia_corta)

# Obtener ruta más larga
G_inverse_weights = nx.Graph()
for u, v, w in G.edges(data='weight'):
    G_inverse_weights.add_edge(u, v, weight=1/w)

ruta_larga = nx.shortest_path(G_inverse_weights, 'Almacén 5', 'Almacén 3', weight='weight')
distancia_larga = nx.shortest_path_length(G_inverse_weights, 'Almacén 5', 'Almacén 3', weight='weight')
print("Ruta más larga:", ruta_larga)
print("Distancia más larga:", distancia_larga)
