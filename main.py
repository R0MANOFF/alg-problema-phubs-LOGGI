# Equanto existir vértice não associado a algum hub, faça:
# 	2.1. escolher o vertice V mais próximo
# 		2.1.1 V ainda não foi atribuido a nenhum hub
# 		2.1.2 V nao ultrapassa a capacidade do hub
# 	2.2. atribuir V ao respectivo hub
# 		2.2.1 atualizar a capacidade do hub

import read_json as rj
import read_txt as rt
from hubs import *

#funcao para descobrir quantos hubs vou precisar?
#faz a soma dos tamanhoa
#pega os maiores tamanhos
#subtrai do valor total
#se os hubs

def index(sizes):
    ind = []
    aux = sizes[:]
    n = biggest_value(aux)
    ind.append(n)
    aux[n] = 1

    for b in range(len(sizes)):
        if b not in ind:
            n = biggest_value(aux)
            if len(ind) < 3:
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


#funcao para ver se tem vertice não associado






def lowestvalue(arrayvalores):
    lv = 1
    print()
    if arrayvalores[0] > 1:
        lowerv = arrayvalores[0]
    else:
        lowerv = 10000000
    for i in range(len(arrayvalores)):
        if arrayvalores[i] < lowerv:
            if arrayvalores[i] > lv:
                lowerv = arrayvalores[i]

    return arrayvalores.index(lowerv)
#     retorna o index pro item ser removido



''' caixeiro viajante problem
def greedy(list_instance):

    for i in range(len(list_instance)):
        aux_instance = list_instance[i]['distancias'].copy()
        for n in range(len(aux_instance)):
            aux = aux_instance[n].strip("km ")
            aux_instance[n] = aux

    #criar um dicionario de listas e  retornar os menores valores
    array_valores = [[12.1, 34, 1, 45, 2.4], [4, 7, 8.9, 1, 56.2], [2.5, 65, 6.7, 1, 10], [5.2, 1, 72, 39, 6.2],
                     [1, 72, 1.9, 24, 50]]

    array_index = []
    for i in range(len(array_valores)):
        index = lowestvalue(array_valores[i])
        while(index not in array_index):
            for n in range(len(array_valores)):
                array_valores[n][index]= 1

            array_index.append(index)


    return array_index

'''





if __name__ == '__main__':

    # rj.create_relation()
    # rj.create_routes()


    # qntd instancias, capacidade total, tamanho de cada instancia(lista), distancias entrepontos(lista de listas)
    list_instance = []
    list = rt.reader_dist() #retorna distancias
    ids_list = rt.read_id(list[0]) #retorna os ids
    ind_list = index(list[2])


    # preenche uma lista com os objetos vertices
    vertices = []
    for v in range(list[0]):
        #id, id_real, linked, size
        vertice = Vertice(v, ids_list[v], 0, list[2][v], 0)
        vertices.append(vertice)
        vertices[v].distancias.append(list[3][v])
        #Vertice.print_vertice(vertices[v])


    for i in range(len(ind_list)):
        vertices[ind_list[i]].hub = 1
        vertices[ind_list[i]].linked = -1

    # for v in range(list[0]):
    #     Vertice.print_vertice(vertices[v])

    for i in range(len(ind_list)):
        aux = vertices[ind_list[i]].size
        #verificar se ainda tem um vetor para associar

    sum = 0
    for i in range(list[0]):
        if vertices[i].linked == 0:
            sum += 1





    #Vertice.print_vertice(vertices[hub_index])






'''
    veiculos = []
    qtd_veiculos = 6
    ids_real = []
    sizes = []
    distancias = []
    vertices = []
    for v in range(0, instancias):
        vertice = Vertice(v, ids_real[v], 0, sizes[v])
        vertices.append(vertice)
        vertices[v].distancias.append(distancias[v])
'''

'''
    path_taken = []


    # qntd instancias, capacidade total, tamanho de cada instancia(lista), distancias entrepontos(lista de listas)
    #list = [dt, inst, cp, sztotal, list_dist]
    tamL = list[1]
    capacity = list[2]
    sizeofeach = list[3]

    for i in range(len(list[4])):
        #print(instance)
        instance['ponto'] = i
        instance['distancias'] = list[4][i]
        #print(instance)
        list_instance.append(instance.copy())


    #print(list_instance)

    path_taken = greedy(list_instance)
    print(path_taken)
'''





