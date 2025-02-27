
grafo = {vertex: [] for vertex in range(1000)}

arestas = [
    (10, 200),
    (10, 500),
    (100, 300),
    (400, 600),
    (700, 800),
    (20, 30),
    (50, 60),
    (75, 125),
    (300, 750),
    (900, 950)
]

for u, v in arestas:
    grafo[u].append(v)
    grafo[v].append(u)

def get_vizinhos(vertice):
    return grafo.get(vertice, [])

print("Vizinhos do vértice 10:", get_vizinhos(10))

def aresta_existe(u, v):
    return v in grafo.get(u, [])

print("Existe aresta entre 10 e 500?", aresta_existe(10, 500))
