# coding: utf-8

import googlemaps
import json
import pandas as pd
import numpy as np
from openpyxl import Workbook
from datetime import datetime

# # 50 primeiras instancias do arq cvrp1-rj-90.json
#  criar um arquivo com os ids da instância  e as id dos pontos da base
# média de tempo de execução com 50 instâncias (7 minutos)
instancias = 50

gmaps = googlemaps.Client(key='AIzaSyDWH2mM7H8NT0QEtJt79lg6jg_ourgB0Cw')

colunas = ['Distancia']
matriz = pd.DataFrame(columns=colunas)


def ler_json(arq_json):
    with open(arq_json, 'r') as f:
        return json.load(f)



data = ler_json('arquivo.json')

capacity = data['vehicle_capacity']
deliveries = data['deliveries']

time = datetime.now()


def create_relation():
    arc = ('arquivos/dados-relacao-ids-' + time.strftime("%m-%d-%Y") + '.txt')
    with open(arc, 'w') as file:
        file.write(time.strftime("%m-%d-%Y-%H:%M\n"))
        file.write('CHAVE ---->  ID \n')
        i = 0
        for id in deliveries:
            file.write(str(i) + '\t ----> \t' + str(id['id']) + '\n')
            i = i + 1
        print(i)



def create_routes():
    arc = ('arquivos/dados-distancia-' + time.strftime("%m-%d-%Y") + '.txt')

    with open(arc, 'w') as file:
        file.write(time.strftime("%m-%d-%Y-%H:%M\n"))
        file.write(str(instancias) + '\n')
        file.write(str(capacity) + "\n")
        for size in deliveries:
            file.write(str(size['size']) + "\n")
        for location in deliveries:
            for comp in deliveries:
                consulta = gmaps.distance_matrix(
                    (location['point']['lat'], location['point']['lng']),
                    (comp['point']['lat'], comp['point']['lng']))
                distancia = consulta['rows'][0]['elements'][0]['distance']['text']
                file.write(str(distancia) + "\t\t\t\t\t")
            file.write('\n')


if __name__ == '__main__':
    create_relation()
    create_routes()