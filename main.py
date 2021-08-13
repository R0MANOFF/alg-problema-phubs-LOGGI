import copy
#import read_json as rj
import read_txt as rt
from hubs import Vertice, Hub
import random


def not_linked(vertices):
    contador = 0
    for z in range(len(vertices)):
        if vertices[z].linked != 0:
            contador += 1

    if contador == len(vertices):
        return 1
    else:
        return 0


def indexx(sizes):
    ind = []
    n = random.randrange(10)
    ind.append(n)

    while len(ind) < 2:
        x = random.randrange(10)
        if x not in ind:
            ind.append(x)

    return ind    #retorna lista de index dos maiores valores


'''

def indexx(sizes):
    ind = []
    aux = sizes[:]
    n = biggest_value(aux)
    ind.append(n)
    aux[n] = 1

    for b in range(len(sizes)):
        if b not in ind:
            n = biggest_value(aux)
            if len(ind) < 2:
                ind.append(n)
                aux[n] = 1

    return ind    #retorna lista de index dos maiores valores




def biggest_value(sizes): #choose hub with the biggest size
    biggest = 0;
    index = 0
    for i in range(len(sizes)):
        if int(sizes[i]) >= biggest:
            biggest = int(sizes[i])
            index = i

    return index
    #retorna index
'''

def small_distance(hubs_index, vertices_distancia):
    lowest = float(1000)
    indice = 0
    for i in range(len(hubs_index)):
        if float(vertices_distancia[hubs_index[i]]) < lowest and float(vertices_distancia[hubs_index[i]]) > -1:
            lowest = float(vertices_distancia[hubs_index[i]])
            indice = hubs_index[i]

    return indice





if __name__ == '__main__':

    # rj.create_relation()
    # rj.create_routes()


    # qntd instancias, capacidade total, tamanho de cada instancia(lista), distancias entrepontos(lista de listas)
    list_instance = []
    list = rt.reader_dist() #retorna distancias
    ids_list = rt.read_id(list[0]) #retorna os ids
    ind_list = indexx(list[2])
    vertices = []
    caps = []



    for v in range(list[0]):
        #id, id_real, linked, size
        vertice = Vertice(v, ids_list[v], 0, list[2][v], 0)
        vertices.append(vertice)
        vertices[v].distancias.append(list[3][v])


    for i in range(len(ind_list)):
        vertices[ind_list[i]].hub = 1
        vertices[ind_list[i]].linked = -1
        vertices[ind_list[i]].size = int(list[1])
        caps.append(vertices[ind_list[i]].size)


    for v in range(list[0]):
        Vertice.print_vertice(vertices[v])


    for i in range(len(vertices)):
        x = 0
        if i not in ind_list:
            n = small_distance(ind_list, vertices[i].distancias[0])
            copy_indlist = ind_list.copy()
            while vertices[i].linked == 0 and x < len(ind_list):
                x += 1
                if vertices[n].size >= vertices[i].size:  #se o size do hub for maior q o size do vertice
                    vertices[i].linked = n
                    vertices[n].size -= vertices[i].size
                else:
                    remove = copy_indlist.index(n)
                    copy_indlist.pop(remove)
                    n = small_distance(copy_indlist, vertices[i].distancias[0])




    vert = [] #vertices ligados ao hub
    sum_distance = [] 
    sum = 0
    for i in range(len(ind_list)):
        aux = []
        sum_distance_aux = 0
        for j in range(len(ids_list)):
            if vertices[j].linked == ind_list[i]:
                aux.append(j)
                sum_distance_aux += float(vertices[j].distancias[0][ind_list[i]])
                sum += float(vertices[j].distancias[0][ind_list[i]])
        sum_distance.append(sum_distance_aux)
        vert.append(aux)

    
    ids = []
    for x in range(len(ind_list)):
        ids.append(vertices[ind_list[x]].id)


    hubs = []
    for i in range(len(ind_list)):
        hub = Hub(ids[i], caps[i], vert[i], sum_distance[i])
        hubs.append(hub)

    print('Soma total:', sum)
    print("Hub / Size do Hub / No's Conectados /Distancia total")
    for h in range(len(ind_list)):
        Hub.print_hubs(hubs[h])
    
    
    h1 = len(hubs)    

    for i in range(h1-1): #vai comparar o vetor atual com o proximo 
        for j in range(len(hubs[i].vertices)): #percorrer array de indices
            for k in range(len(hubs[i+1].vertices)): 
                indi_vertice_1 = hubs[i].vertices[j]
                indi_vertice_2 = hubs[i+1].vertices[k]
                indi_hubs = ids.copy()

                #calcular o custo
                n = float(vertices[indi_vertice_1].distancias[0][indi_hubs[i]]) #recebe distancia do ponto p para o hub h
                n2 = float(vertices[indi_vertice_2].distancias[0][indi_hubs[i]])
                aux_sum = hubs[i].distance
                aux_sum = aux_sum - n + n2
                
                n = float(vertices[indi_vertice_1].distancias[0][indi_hubs[i+1]])
                n2 = float(vertices[indi_vertice_2].distancias[0][indi_hubs[i+1]])
                aux_sum2 = hubs[i+1].distance
                aux_sum2 = aux_sum2 + n - n2
                
                aux_sum = aux_sum + aux_sum2
                if aux_sum < sum:
                    hubs[i].vertices[j] = indi_vertice_2
                    print('\n',indi_vertice_1,'\n')
                    hubs[i+1].vertices[k] = indi_vertice_1
                    print('\n',indi_vertice_2,'\n')
                    sum = aux_sum
                    print(sum)
        

    print('-'*50)
    print('Soma total:', sum)
    print("Hub / Size do Hub / No's Conectados /Distancia total")
    for h in range(len(ind_list)):
        Hub.print_hubs(hubs[h])  
    print('-'*50)
            
            
            

'''
    for i in range(h1):
        if len(hubs) == 2:
            for j in range(len(hubs[1].vertices)):
                aux = hubs[0].vertices[i]
                aux2 = hubs[1].vertices[j]
                a_dist = hubs[0].distance
                b_dist = hubs[1].distance

                indices_hub = ids.copy()
                indices_vertices = [aux, aux2]
                n = small_distance(indices_hub, vertices[indices_vertices[i]].distancias[0])
                print(n)


                hubs[0].vertices[i] = aux2
                hubs[1].vertices[j] = aux
                #somar a distancia novamente
                
                #diminuir distancia daquele indice da distancia total e somar a do novo indice associado e se for menor trocar a distancia total
                print(vertices[aux].distancias[0])
                print(vertices[aux2].distancias[0])
                break
            break
'''
    

        
      













