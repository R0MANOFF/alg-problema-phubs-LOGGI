import pandas as pd
import json
from openpyxl import Workbook
from datetime import datetime
from math import acos, sin, cos, radians, asin, sqrt
# # # ler dataset (JSON) e salvar id, lng e lat
# # conectar com api do google para obter ditancias
# #  salvar distancias em uma matriz que será exportada como .xlsx


colunas = ['Id-Origem', 'Lat-Origem', 'Lng-Origem', 'Id-Destino',
            'Lat-Destino', 'Lng-Destino', 'Distancia', 'Demanda']
matriz = pd.DataFrame(columns=colunas)

def distancia_p(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def distancia_pontos(p1, p2):
  p1 = (radians(p1[0]), radians(p1[1]))
  p2 = (radians(p2[0]), radians(p2[1]))
  distancia = acos(sin(p1[0]) * sin(p2[0]) + cos(p1[0]) * cos(p2[0]) * cos(p1[1] - p2[1])) #eh pra isso ai dar a distancia euclidiana fé

  return distancia


def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)


data = ler_json('arquivo.json')
deliveries = data['deliveries']

for location in deliveries:
    for comp in deliveries:
        id_origem = location['id']
        lat_origem = location['point']['lat']
        lng_origem = location['point']['lng']
        id_destino = comp['id']
        lat_destino = comp['point']['lat']
        lng_destino = comp['point']['lng']
        demanda = comp['size']
        #demandaTotal = sum(int(demanda))
        #print(demandaTotal)
        distancia = distancia_p(lng_origem, lat_origem, lng_destino, lat_destino)
        temp = pd.DataFrame([[id_origem, lat_origem, lng_origem, id_destino,
                            lat_destino, lng_destino, distancia, demanda]], columns=colunas)
        matriz = matriz.append(temp, ignore_index=True)

#print(matriz)


matriz.to_csv(r'pandas.txt', header=None, index='False', sep=' ', mode='a')

time = datetime.now()
print(time)
#escrever = pd.ExcelWriter(f'dados-distancia-{time}.xlsx')
#matriz.to_excel(escrever, 'MATRIZ', index=False)
#escrever.save()
