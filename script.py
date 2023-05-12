from numpy import sin, cos, arccos, pi, round
import math
import json
# import pandas as pd

# LENDO ESTRUTURA DE DADOS E CONVERTENDO EM DICIONARIO
with open("map.json", encoding='utf-8') as meu_json:
	date_map = json.load(meu_json)
        
print(date_map)
print(date_map[1]['lat'], date_map[3]['lat'])

def distancia(lat1, lon1, lat2, lon2):
    r = 6371000  # raio da Terra em metros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c




for i in date_map:
    pontos_alcancaveis = list(map(int, i['pontos_alcancaveis'].split(';')))

    
    # print(f"Ponto {i['ponto']} alcança os pontos: {pontos_alcancaveis}")///


