import math
import json

# LENDO ESTRUTURA DE DADOS E CONVERTENDO EM DICIONARIO
with open("newMap.json", encoding='utf-8') as meu_json:
	date_map = json.load(meu_json)

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # RAIO DA TERRA

    # GRAUS P/ RADIANOS
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # DIFERENÇA ENTRE AS COORDENADAS
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # CALCULANDO A DISTANCIA
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c * 1000

    return round(distance, 2)


def a_estrela(pontos, origem, destino):
    # Inicialização
    g = {}  # custo atual do ponto de origem até cada ponto
    h = {}  # estimativa de custo do ponto até o destino
    f = {}  # custo total (g + h) do ponto
    filhos = {}  # armazena o filho de cada ponto
    abertos = []  # lista de pontos abertos para explorar

    # Inicializa os custos com infinito, exceto para a origem
    for ponto in pontos:
        g[ponto['ponto']] = float('inf')
        h[ponto['ponto']] = calcular_distancia(ponto['lat'], ponto['lon'], pontos[destino - 1]['lat'], pontos[destino - 1]['lon'])
        f[ponto['ponto']] = float('inf')
    g[origem] = 0
    f[origem] = h[origem]
    abertos.append(origem)

    while abertos:
        # Seleciona o ponto com o menor custo total (f)
        atual = min(abertos, key=lambda ponto: f[ponto])

        if atual == destino:
            # Chegou ao ponto de destino
            caminho = []
            while atual in filhos:
                caminho.insert(0, atual)
                atual = filhos[atual]
                print(atual)
            caminho.insert(0, origem)
            return caminho

        abertos.remove(atual)

        for vizinho_str in pontos[atual - 1]['pontos_alcancaveis'].split(';'):
            if not vizinho_str:
                continue

            vizinho = int(vizinho_str)
            # print(vizinho)
            # print(filhos)
            # print(abertos)

            # Calcula o custo atualizado para o vizinho
            custo_atualizado = g[atual] + calcular_distancia(
                pontos[atual - 1]['lat'], pontos[atual - 1]['lon'],
                pontos[vizinho - 1]['lat'], pontos[vizinho - 1]['lon']
            )

            # print(custo_atualizado)

            if custo_atualizado < g[vizinho]:
                # Atualiza os custos e o filho do vizinho
                filhos[vizinho] = atual
                g[vizinho] = custo_atualizado
                f[vizinho] = g[vizinho] + h[vizinho]

                if vizinho not in abertos:
                    # Adiciona o vizinho à lista de pontos abertos
                    abertos.append(vizinho)

    # Não foi possível encontrar um caminho
    return None



print('\n1-Drogaria União \n2-Esquina Igreja \n3-Granja Leão \n4-GigaBites \n5-Drogaria PagMenos\n6-Paraiba\n7-Mercado Central\n8-Drogaria Globo\n9-Prime  Cell\n10-Subway\n11-Papelaria Globo\n12-Pub Pride\n13-Galeria dos Calçados\n14-Nortista\n15-Clinicou\n16-Impacto Kids\n17-Sobral\n18-Company Odonto\n19-DG Embalagens\n20-Armazem Zé Mendes\n21-Droga Vida')
origem = int(input('Escolha o ponto de origin: '))
destino = int(input('Escolha o ponto de destino: '))

caminho = a_estrela(date_map, origem, destino)

if caminho:
    print(f"Caminho mais curto de {origem} a {destino}: {caminho}")
else:
    print(f"Não foi possível encontrar um caminho de {origem} a {destino}")
