grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

print("Lista de Adjacência do Grafo:")
for cidade, vizinhos in grafo.items():
    print(f"{cidade}: {vizinhos}")

def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=" ")
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

from collections import deque
def bfs(grafo, inicio):
    visitados = set([inicio])
    fila = deque([inicio])
    while fila:
        atual = fila.popleft()
        print(atual, end=" ")
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

print("\n\nTravessia DFS a partir do vértice A:")
dfs(grafo, "A")

print("\n\nTravessia BFS a partir do vértice A:")
bfs(grafo, "A")
print()
