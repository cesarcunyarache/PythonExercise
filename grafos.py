import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo vacío para representar la red de transporte
G = nx.Graph()

# Agregar estaciones como nodos
estaciones = ["A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(estaciones)

# Definir las conexiones entre las estaciones como aristas con sus respectivas distancias
conexiones = [
    ("A", "B", {"distancia": 5}),
    ("B", "C", {"distancia": 7}),
    ("C", "D", {"distancia": 3}),
    ("D", "A", {"distancia": 8}),
    ("A", "E", {"distancia": 6}),
    ("B", "F", {"distancia": 4}),
    ("C", "G", {"distancia": 5}),
    ("E", "F", {"distancia": 9}),
    ("F", "G", {"distancia": 8}),
    ("G", "D", {"distancia": 2})
]
G.add_edges_from(conexiones)

# Calcular la ruta más corta usando el algoritmo de Dijkstra
shortest_path = nx.shortest_path(G, source="A", target="C", weight="distancia")

# Obtener las posiciones de los nodos para la visualización
pos = nx.spring_layout(G)

# Dibujar el grafo con las distancias
nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, node_size=1500)

# Dibujar las distancias como etiquetas en las aristas
edge_labels = {(n1, n2): d["distancia"] for n1, n2, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=8)

# Dibujar la ruta más corta
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1])
                                         for i in range(len(shortest_path) - 1)],
                       edge_color='red', width=2)

# Mostrar el gráfico
plt.show()
