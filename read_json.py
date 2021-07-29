
import googlemaps
import json
import pandas as pd
from datetime import datetime



instancias = 10

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
    arc = ('arquivos/ids/dados-relacao-ids-' + time.strftime("%m-%d-%Y") + '.txt')
    with open(arc, 'w') as file:
        file.write(time.strftime("%m-%d-%Y-%H:%M\n"))
        file.write('CHAVE ---->  ID \n')
        i = 0
        for id in deliveries:
            file.write(str(i) + '\t ----> \t' + str(id['id']) + '\n')
            i = i + 1




def create_routes():
    arc = ('arquivos/distancia/dados-distancia-' + time.strftime("%m-%d-%Y") + '.txt')

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
                distancia, km = str(distancia).split()
                if km == 'm':
                    distancia = (float(distancia.replace(',', '.'))) * 1000
                file.write(str(distancia).replace(',', '.') + "\t\t\t\t\t")
            file.write('\n')









