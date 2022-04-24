
# Class pour arrete

from re import U


class Edge():
    #edge is a string
    def __init__(self, u, v, edge):
        self.name = edge
        self.origin = u
        self.destination = v
    #return the Edge object's string
    def getKey(self):
        return self.name
    def getDestination(self):
        return self.destination
        