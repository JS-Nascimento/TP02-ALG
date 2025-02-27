
grafo = {
    "Centro": ["Bairro A", "Bairro B"],
    "Bairro A": ["Centro", "Bairro C"],
    "Bairro B": ["Centro", "Bairro C"],
    "Bairro C": ["Bairro A", "Bairro B", "Bairro D"],
    "Bairro D": ["Bairro C"]
}

def get_vizinhos(bairro):
    """
    Retorna a lista de bairros vizinhos (conectados diretamente) ao bairro informado.
    Se o bairro não existir no grafo, retorna uma lista vazia.
    """
    return grafo.get(bairro, [])

bairro_consulta = "Bairro A"
print(f"Vizinhos de {bairro_consulta}:", get_vizinhos(bairro_consulta))
