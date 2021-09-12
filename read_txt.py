
def reader_dist():
    sizes = []
    distancias = []

    with open('arquivos/distancia/dados-distancia-200-rj-08-30-2021.txt', 'r') as f:
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
    with open('arquivos/ids/dados-relacao-ids-200-rj-08-30-2021.txt', 'r') as id:
        date = id.readline()
        ids = id.readlines()
        for id in range(1, instancias + 1):
            num, seta, id = ids[id].split()
            ids_list.append(id)

    return ids_list

