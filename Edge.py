
# Class pour arrete

class Edge:

    def __init__(self, org, dest, elem):
        self.origin = org
        self.destination = dest
        self.element = elem

    def getEndpoints(self):
        return (self.origin, self.destination)

    def opposite(self, x):
        if x == self.origin:
            return self.destination
        else:
            return self.origin 

    def getEdgeName(self):
        return self.element
        