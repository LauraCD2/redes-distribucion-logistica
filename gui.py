##Aqui va la gui

import tkinter as tk
from tkinter import scrolledtext
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def print_graph(distance_matrix):
    G = nx.Graph()

    # Agregar nodos al grafo
    cities = len(distance_matrix)
    G.add_nodes_from(range(1, cities + 1))

    # Agregar aristas al grafo
    for i in range(cities):
        for j in range(i + 1, cities):
            weight = distance_matrix[i][j]
            if weight > 0:
                G.add_edge(i + 1, j + 1, weight=weight)

    # Obtener posición de los nodos para visualización
    pos = nx.spring_layout(G)

    # Obtener los pesos de las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Dibujar el grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='red')

    # Mostrar el grafo
    plt.title('Grafo de Ciudades')
    plt.axis('off')
    plt.show()

def run_algorithm():
    # Aquí va el código para ejecutar el algoritmo y obtener la matriz de distancia modificada 'temp1'
    # ...

    # Imprimir el gráfico y la salida
    print_graph(temp1)

    # Mostrar la salida en el cuadro de texto
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Tiempo en minutos: {}\n".format(hamiltonian_cycle))
    output_text.insert(tk.END, "Camino Óptimo: {}\n".format(final_path))
    output_text.insert(tk.END, "Días gastados: {}\n".format(dias))

# Crear la ventana principal
window = tk.Tk()
window.title("Visualización del Grafo y Salida")
window.geometry("800x600")

# Crear el área para mostrar el gráfico
graph_canvas = tk.Canvas(window, width=600, height=400)
graph_canvas.pack(side=tk.TOP, padx=10, pady=10)

# Crear el cuadro de texto para la salida
output_text = scrolledtext.ScrolledText(window, width=80, height=10)
output_text.pack(side=tk.BOTTOM, padx=10, pady=10)

# Botón para ejecutar el algoritmo
run_button = tk.Button(window, text="Ejecutar algoritmo", command=run_algorithm)
run_button.pack(side=tk.TOP, pady=10)

# Función para dibujar el gráfico en el área correspondiente
def draw_graph():
    graph_canvas.delete("all")  # Limpiar el lienzo antes de dibujar el nuevo gráfico
    plt.close()  # Cerrar la ventana de matplotlib para evitar superposiciones

    # Obtener la figura del gráfico como una imagen de mapa de bits
    figure = plt.figure(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(figure, master=graph_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Ejecutar la función de dibujo del gráfico inicialmente
draw_graph()

# Ejecutar el bucle principal de la GUI
window.mainloop()