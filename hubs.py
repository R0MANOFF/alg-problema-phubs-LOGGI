
class Vertice():
  def __init__(self, id, id_real, linked, size, hub):
    self.id = id
    self.id_real = id_real
    self.linked = linked    #verifica se o vertice esta ligado a algum hub
    self.size = size
    self.hub = hub       #verifica se é hub ou não
    self.distancias = []

  def print_vertice(self):
    print(self.id, self.id_real, self.linked, self.size, self.distancias, self.hub)

  def menor_size(self, size, size2):
    if self.size <= self.size:
      return 1
    else:
      return 0

class Hub():
  def __init__(self, id, capacity, vertices, distance):
    self.id = id
    self.capacity = capacity
    self.vertices = vertices
    self.distance = distance

  def print_hubs(self):
    print( self.id, self.capacity, self.vertices)