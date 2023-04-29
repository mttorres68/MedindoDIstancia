from numpy import sin, cos, arccos, pi, round
# import pandas as pd

map = [
    [1, 'Drogaria União', -6.76718620245407, -43.0215998069604, [2, 11]],
    [2, 'Esquina igreja', -6.76793880641175, -43.0215709496876, [1, 3, 12]],
    [3, 'Granja Leão', -6.76885845672127, -43.0214988132572, [2, 4]],
    [4, 'GigaBites', -6.76878643276312, -43.0204944028716, [3, 4, 12]],
    [5, 'Drogaria PagMenos', -6.76872141035052, -43.0196630496312, [4, 6, 13]],
    [6, 'Paraíba', -6.76868678971887, -43.0189560159711, [5, 7, 15]],
    [7, 'Mercado Central', -6.76857119285080, -43.0175800629520, [6, 8, 21]],
    [8, 'Drogaria Globo', -6.76797585186948, -43.0183128683907,	[9, 7, 19]],
    [9, 'Prime Cell', -6.76771042412166, -43.0185437798245,	[8, 15, 10, 18]],
    [10, 'Subway', -6.76695045067788, -43.019877359859,	[9, 11, 14, 16]],
    [11,' Papelaria Globo', -6.76705748127151, -43.020605549343, [1, 10, 12]],
    [12, 'Pub Pride', -6.76788306216676, -43.0205507817435,[2, 4, 11, 13]],
    [13, 'Galeria dos Calçados', -6.76781873207370,	-43.019768465694, [5, 12, 14]],
    [14, 'Nortista', -6.76764311827105,	-43.019781435176, [10, 13, 15]],
    [15, 'Clinicou', -6.76799199336188,	-43.019010568988, [6, 9, 14]],
    [16, 'Impacto Kids', -6.7663267823643, -43.0199349705603, [10, 17]],
    [17, 'Sobral', -6.76620190217362, -43.0185431941594, [16, 18]],
    [18, 'Company Odonto', -6.76716554683158, -43.0179304498840, [9, 17, 19]],
    [19, 'DG Embalagens', -6.76760120229613, -43.0174994812226, [8, 18, 20]],
    [20, 'Armazém Zé Mendes', -6.76828897917540, -43.0166349846579, [19, 21]],
    [21, 'Droga Vida', -6.76893716772531, -43.0170946317711, [7, 20]],
]

new_map = []


def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistEntPon(latitude1, longitude1, latitude2, longitude2, unit = 'kilometers'):
    
    theta = longitude1 - longitude2
    
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    
    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)

def loc_id(lista, id):
    for i in range(len(lista)):
        if id == lista[i][0]:
            return lista[i]

for i in range(len(map)):
    dist=[]
    for j in range(len(map[i][4])):
        id = map[i][4][j]
        dist.append( [map [map [i] [4] [j]-1] [1] ,getDistEntPon(map[i][2], map[i][3], loc_id(map,map[i][4][j])[2], loc_id(map,map[i][4][j])[3])*1000] )
        # print(dist)
    
    new_map.append([map[i][0],map[i][1],map[i][2],map[i][3],map[i][4], dist])
    

# print(loc_id(new_map, 8))
# print(map[20])

print(getDistEntPon(map[6][2], map[6][3], map[20][2], map[20][3]) * 10001)
print(new_map)
