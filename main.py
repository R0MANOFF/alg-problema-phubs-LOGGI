# Equanto existir vértice não associado a algum hub, faça:
# 	2.1. escolher o vertice V mais próximo
# 		2.1.1 V ainda não foi atribuido a nenhum hub
# 		2.1.2 V nao ultrapassa a capacidade do hub
# 	2.2. atribuir V ao respectivo hub
# 		2.2.1 atualizar a capacidade do hub
import copy
import read_json as rj
import read_txt as rt
from hubs import Vertice


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


#funcao para determinar qual hub tem a menor distancia para o vertice
#recebe lista dos indexes dos hubs
#retorna index do hub de menor distancia

#vertices_distancia = vertice[n].distancia[0]
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

    copy_indlist = ind_list[:]
    print(copy_indlist)
    # preenche uma lista com os objetos vertices
    vertices = []
    for v in range(list[0]):
        #id, id_real, linked, size
        vertice = Vertice(v, ids_list[v], 0, list[2][v], 0)
        vertices.append(vertice)
        vertices[v].distancias.append(list[3][v])


    for i in range(len(ind_list)):
        vertices[ind_list[i]].hub = 1
        vertices[ind_list[i]].linked = -1

    # for v in range(list[0]):
    #     Vertice.print_vertice(vertices[v])

    for v in range(list[0]):
        Vertice.print_vertice(vertices[v])


    print(len(vertices))
    f_index = []
    for i in range(len(vertices)):
        #se for um hub pula pro proximo
        #ir no vertice i veriricar qual a menor distancia dentre os tres hubs
        #enquanto o vertice nao estiver linkado
        #achou a menor distancia verificar se naquele hub ainda tem espaço
            #se tiver linka
            #se nao pula para o proximo hub
                #remove elemento da lista e chama a funcao q encontra o menor valor entre aquela nova lista
        # vertices_distancia = vertice[n].distancia[0]
        #lista de index que nao cabem mais nada
        if i not in ind_list:
            n = small_distance(ind_list, vertices[i].distancias[0])
            copy_indlist = ind_list[:]
            while vertices[i].linked == 0:
                if vertices[n].size >= vertices[i].size:  #se o size do hub for maior q o size do vertice
                    vertices[i].linked = n
                    vertices[n].size -= vertices[i].size
                else:
                    remove = copy_indlist.index(n)
                    copy_indlist.pop(remove)
                    n = small_distance(copy_indlist, vertices[i].distancias[0])
        else:
            print('hub')

    for v in range(list[0]):
        Vertice.print_vertice(vertices[v])
