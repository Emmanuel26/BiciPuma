import sys
infinity = sys.maxsize-1


class Vertex:
    def __init__(self, name):
        self.id = name
        self.la = 0
        self.lo = 0
        self.adjacent = {}
        self.pi = None
        self.key = infinity

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def adjacentList(self):
        return self.adjacent.keys()

    def getKey(self):
        return self.key

    def setKey(self, k):
        self.key = k
    
    
        
