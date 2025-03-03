from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    visitados.add(inicio)

    ordem_visita = []

    while fila:
        vertice_atual = fila.popleft()
        ordem_visita.append(vertice_atual)

        for vizinho in grafo[vertice_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return ordem_visita

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

resultado_bfs = bfs(grafo, "A")
print("Ordem de visita (BFS) a partir de A:", resultado_bfs)
