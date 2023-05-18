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

  # CALCULANDO A DIFERENÇA ENTRE AS COORDENADAS
  delta_lat = lat2_rad - lat1_rad
  delta_lon = lon2_rad - lon1_rad

  # CALCULANDO A DISTANCIA
  a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  distance = R * c * 1000

  #RETORNA A DISTANCIA E ARREDONDA PARA DUAS CASAS DECIMAIS
  return round(distance, 2)


def a_estrela(pontos, origem, destino):
  # CUSTO ATUAL DO PONTO DE ORIGEM A CADA PONTO
  g = {}

  # DISTANCIA DO PONTO DE ORIGEM AO DE DESTINO
  h = {}

  # CUSTO TOTAL ( G + H ) 
  f = {}

  # ARMAZENA OS FILHOS
  filhos = {}

  # ARMAZENA OS PONTOS ABERTOS
  abertos = [] 

  # INICIALIZA OS CUSTOS COM INFINITO, EXCETO PARA A ORIGEM
  for ponto in pontos:
    g[ponto['ponto']] = float('inf')
    h[ponto['ponto']] = calcular_distancia(ponto['lat'], ponto['lon'], pontos[destino - 1]['lat'], pontos[destino - 1]['lon'])
    f[ponto['ponto']] = float('inf')
  g[origem] = 0
  f[origem] = h[origem]
  abertos.append(origem)

  while abertos:
    # SELECIONAR O PONTO COM MENOR CUSTO (f)
    atual = min(abertos, key=lambda ponto: f[ponto])

    # VERIFICA SE CHEGOU AO DESTINO FINAL
    if atual == destino:
      caminho = []
      while atual in filhos:
        caminho.insert(0, atual)
        atual = filhos[atual]
      caminho.insert(0, origem)
      return caminho

    abertos.remove(atual)

    for vizinho_str in pontos[atual - 1]['pontos_alcancaveis'].split(';'):
        if not vizinho_str:
            continue

        vizinho = int(vizinho_str)

        # CALCULA O CUSTO ATUALIZADO PARA O VIZINHO
        custo = g[atual] + calcular_distancia(
          pontos[atual - 1]['lat'], pontos[atual - 1]['lon'],
          pontos[vizinho - 1]['lat'], pontos[vizinho - 1]['lon']
        )

        if custo < g[vizinho]:
          # ATUALIZA OS CUSTOS E O FILHO DO VIZINHO
          filhos[vizinho] = atual
          g[vizinho] = custo
          f[vizinho] = g[vizinho] + h[vizinho]

          if vizinho not in abertos:
            # ADICIONA O VIZINHO À LISTA DE PONTOS ABERTOS
            abertos.append(vizinho)
    
    # O PONTO ATUAL JUNTO COM OS PONTOS VIZINHOS COM g, h e f
    print(f"**** Ponto Atual: {atual} ****")
    print("____ Pontos Visitados ____")
    for ponto in abertos:
      print(f"Ponto: {ponto}")
      print(f"g: {g[ponto]}, h: {h[ponto]}, f: {f[ponto]}")
      # print(filhos)
      print("")

  return None


print('\n1-Drogaria União \n2-Esquina Igreja \n3-Granja Leão \n4-GigaBites \n5-Drogaria PagMenos\n6-Paraiba\n7-Mercado Central\n8-Drogaria Globo\n9-Prime  Cell\n10-Subway\n11-Papelaria Globo\n12-Pub Pride\n13-Galeria dos Calçados\n14-Nortista\n15-Clinicou\n16-Impacto Kids\n17-Sobral\n18-Company Odonto\n19-DG Embalagens\n20-Armazém Zé Mendes\n21-Droga Vida')
origem = int(input('Escolha o ponto de origem: '))
destino = int(input('Escolha o ponto de destino: '))
print("\n")

encontrar_caminho = a_estrela(date_map, origem, destino)

if encontrar_caminho:
  print(f" O caminho mais curto de {origem} a {destino}: {encontrar_caminho}")
else:
  print(f"Localização falhou de {origem} a {destino}")
