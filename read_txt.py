
def reader_dist():
    sizes = []
    distancias = []

    with open('arquivos/distancia/dados-distancia-07-28-2021.txt', 'r') as f:
      linhas = f.readlines()
      date = linhas[0]

      instancias = int(linhas[1])
      capacity = int(linhas[2])

      for i in range(3, instancias + 3):
          sizes.append(int(linhas[i]))

      for item in range(instancias + 3, len(linhas)):
          distancias.append((linhas[item]).replace('\t\t\t\t\t', ' ').replace('\n', '').split())

    list = [instancias, capacity, sizes, distancias]
    return list



def read_id(instancias):
    ids_list = []
    with open('arquivos/ids/dados-relacao-ids-07-28-2021.txt', 'r') as id:
        date = id.readline()
        ids = id.readlines()
        for id in range(1, instancias + 1):
            num, seta, id = ids[id].split()
            ids_list.append(id)

    return ids_list


'''
          dt = f.readline().strip('\n')
          inst = f.readline().strip('\n')
          cp = f.readline().strip('\n')
          sztotal = f.readlines(22)
          for index in range(len(sztotal)):
              sztotal[index] = sztotal[index].rstrip('\n')

          

        #lendo a matriz de distancia
          aux_distan = f.readlines()
          n = len(aux_distan)
          i = 0
          list_dist = []
          while i < n:
              vet_aux = aux_distan[i]
              vet_aux = vet_aux.split('\t')
              i+=1
              list_dist.append(vet_aux)

          # data arq, qntd instancias, capacidade total, tamanho de cada instancia(lista), distancias entrepontos(lista de listas)
          list = [dt, inst, cp, sztotal, list_dist]
          return list 
'''
