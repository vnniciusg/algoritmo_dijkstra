import sys
import heapq


def constroi_grafo(arquivo):
    with open(arquivo) as f:
        linhas = f.readlines()
    num_vertices, num_arestas = map(int, linhas[0].split())

    grafo = {}

    for linha in linhas[1:]:
        origem, peso, destino = map(int, linha.split())
        if origem not in grafo:
            grafo[origem] = []
        grafo[origem].append((destino, peso))

    return grafo


def dijkstra(grafo, origem):
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    visitados = set()

    while visitados != set(distancias):
        vertice_atual = None
        menor_distancia = sys.maxsize
        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancias[v]
        visitados.add(vertice_atual)

        for vizinho, peso in grafo[vertice_atual]:
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso
    return distancias


origem = 1

grafo = constroi_grafo("rotas_casa_faculdade.txt")
print("Grafo : ", grafo)

distancia_minima = dijkstra(grafo, origem)
for destino, distancia in distancia_minima.items():
    print(f"Caminho mais curto de {origem} para {destino}: {distancia}")
