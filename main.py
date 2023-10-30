import sys
import heapq


def constroi_grafo(arquivo):
    with open(arquivo) as f:
        lines = f.readlines()
    num_vertices, num_arestas = map(int, lines[0].split())

    grafo = {}

    for line in lines[1:]:
        valores = line.split()
        if len(valores) >= 3:
            origem, peso, destino = map(int, valores)

        if origem not in grafo:
            grafo[origem] = {}
        grafo[origem][destino] = peso
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

        for vizinho, peso in grafo[vertice_atual].items():
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso
    return distancias


origem = 1

grafo = constroi_grafo("rotas_casa_faculdade.txt")

distancia_minima = dijkstra(grafo, origem)
for destino, distancia in distancia_minima.items():
    print(f"Caminho mais curto de {origem} para {destino}: {distancia}")
