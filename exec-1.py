import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    "Alice": ["Bob", "Carlos"],
    "Bob": ["Alice", "Diana"],
    "Carlos": ["Alice", "Diana", "Eduardo"],
    "Diana": ["Bob", "Carlos"],
    "Eduardo": ["Carlos"]
}

vertices = list(grafo.keys())

arestas = set()
for usuario in grafo:
    for amigo in grafo[usuario]:
        if (amigo, usuario) not in arestas:
            arestas.add((usuario, amigo))

print("Vértices:", vertices)
print("Arestas:", arestas)
G = nx.Graph()

for usuario, amigos in grafo.items():
    for amigo in amigos:
        G.add_edge(usuario, amigo)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, edge_color='gray')

plt.show()
