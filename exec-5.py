from collections import deque

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "E"],
    "E": ["C", "D"]
}

print("Vizinhos de cada centro (grafo não ponderado):")
for centro in grafo:
    print(f"{centro}: {grafo[centro]}")

grafo_ponderado = {
    "A": [("B", 10), ("C", 15)],
    "B": [("A", 10), ("D", 12)],
    "C": [("A", 15), ("E", 10)],
    "D": [("B", 12), ("E", 5)],
    "E": [("C", 10), ("D", 5)]
}

print("\nVizinhos de cada centro (grafo ponderado):")
for centro in grafo_ponderado:
    vizinhos = ", ".join([f"{vizinho} ({peso} min)" for vizinho, peso in grafo_ponderado[centro]])
    print(f"{centro}: {vizinhos}")

def bfs_caminho(grafo, inicio, objetivo):

    visitados = set()
    fila = deque([(inicio, [inicio])])

    while fila:
        atual, caminho = fila.popleft()
        if atual == objetivo:
            return caminho
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    return None

caminho = bfs_caminho(grafo, "A", "E")
print("\nCaminho mais curto (em número de conexões) de A até E (BFS):", caminho)
