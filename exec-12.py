
from collections import deque
cidade = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["B", "D", "F"],
    "F": ["E"]
}


def bfs_caminho_mais_curto(grafo, inicio, objetivo):

    fila = deque([inicio])

    visitados = {inicio}

    antecessor = {inicio: None}

    while fila:
        atual = fila.popleft()

        if atual == objetivo:
            return reconstruir_caminho(antecessor, inicio, objetivo)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                antecessor[vizinho] = atual
                fila.append(vizinho)

    return None
def reconstruir_caminho(antecessor, inicio, objetivo):

    caminho = []
    atual = objetivo
    while atual is not None:
        caminho.append(atual)
        atual = antecessor[atual]
    caminho.reverse()
    return caminho

inicio = "A"
objetivo = "F"

caminho = bfs_caminho_mais_curto(cidade, inicio, objetivo)
if caminho:
    print(f"Caminho mais curto de {inicio} até {objetivo}: {caminho}")
else:
    print(f"Não existe caminho entre {inicio} e {objetivo}.")
