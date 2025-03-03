def detectar_ciclos(grafo):

    visitados = set()
    rec_stack = set()
    ciclos = []

    def dfs(conta, caminho):
        visitados.add(conta)
        rec_stack.add(conta)
        caminho.append(conta)

        for vizinho in grafo.get(conta, []):
            if vizinho not in visitados:
                dfs(vizinho, caminho)
            elif vizinho in rec_stack:

                indice = caminho.index(vizinho)
                ciclo = caminho[indice:].copy()
                ciclos.append(ciclo)

        rec_stack.remove(conta)
        caminho.pop()

    for conta in grafo:
        if conta not in visitados:
            dfs(conta, [])

    return ciclos

transacoes = {
    "ContaA": ["ContaB"],
    "ContaB": ["ContaC"],
    "ContaC": ["ContaD"],
    "ContaD": ["ContaA"],
    "ContaE": ["ContaF"],
    "ContaF": ["ContaG"],
    "ContaG": ["ContaE"],
    "ContaH": ["ContaI"],

}

instituicoes = {
    "ContaA": "Banco do Brasil",
    "ContaB": "Bradesco",
    "ContaC": "Itaú",
    "ContaD": "Banco do Brasil",
    "ContaE": "Bradesco",
    "ContaF": "Itaú",
    "ContaG": "Santander",
    "ContaH": "Caixa",
    "ContaI": "Caixa"
}

ciclos_encontrados = detectar_ciclos(transacoes)

print("Ciclos detectados:")
for ciclo in ciclos_encontrados:
    print(" -> ".join(ciclo))

def priorizar_ciclos(ciclos, instituicoes):

    ciclos_prioritarios = []
    for ciclo in ciclos:
        bancos_no_ciclo = {instituicoes[conta] for conta in ciclo if conta in instituicoes}
        if len(bancos_no_ciclo) > 1:
            ciclos_prioritarios.append((ciclo, bancos_no_ciclo))
    return ciclos_prioritarios

ciclos_prioritarios = priorizar_ciclos(ciclos_encontrados, instituicoes)
print("\nCiclos prioritários (envolvendo múltiplos bancos):")
for ciclo, bancos in ciclos_prioritarios:
    print(f"Ciclo: {' -> '.join(ciclo)} | Bancos envolvidos: {', '.join(bancos)}")
