from collections import deque

grafo = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [6],
    6: []
}


def dfs(grafo, inicio, visitados=None, ordem=None):
    if visitados is None:
        visitados = set()
    if ordem is None:
        ordem = []

    visitados.add(inicio)
    ordem.append(inicio)

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, ordem)
    return ordem

ordem_dfs = dfs(grafo, 1)
print("Ordem de visita (DFS) a partir de 1:", ordem_dfs)

def bfs(grafo, inicio):
    visitados = set([inicio])
    fila = deque([inicio])
    ordem = []

    while fila:
        vertice = fila.popleft()
        ordem.append(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    return ordem

ordem_bfs = bfs(grafo, 1)
print("Ordem de visita (BFS) a partir de 1:", ordem_bfs)
