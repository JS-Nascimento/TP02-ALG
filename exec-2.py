import networkx as nx
import matplotlib.pyplot as plt

cidade = {
    "Centro": ["Norte", "Sul", "Leste", "Oeste"],
    "Norte": ["Centro", "Leste", "Oeste"],
    "Sul": ["Centro", "Leste", "Sudoeste"],
    "Leste": ["Centro", "Norte", "Sul"],
    "Oeste": ["Centro", "Norte"],
    "Sudoeste": ["Sul"]
}

vertices = list(cidade.keys())
print("Bairros (vértices):", vertices)

arestas = set()
for bairro in cidade:
    for vizinho in cidade[bairro]:

        if (vizinho, bairro) not in arestas:
            arestas.add((bairro, vizinho))
print("Ruas (arestas):", arestas)

G = nx.Graph()

for bairro, vizinhos in cidade.items():
    for vizinho in vizinhos:
        G.add_edge(bairro, vizinho)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, edge_color='gray')
plt.title("Representação dos Bairros e Ruas da Cidade")
plt.show()
