
class Vertice():
  def __init__(self, id, id_real, linked, size):
    self.id = id
    self.id_real = id_real
    self.linked = linked    #verifica se o vertice esta ligado a algum hub
    self.size = size
    self.distancias = []

  def print_vertice(self):
    print(self.id, self.id_real, self.linked, self.size, self.distancias)


class Hub():
  def __init__(self, id, capacity, vertices, distance):
    self.id = id
    self.capacity = capacity
    self.vertices = vertices
    self.distance = distance

  def print_hubs(self):
    print( self.id, self.capacity, self.vertices)