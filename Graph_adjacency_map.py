
class Vertex():
    #vertex is a string
    def __init__(self, vertex):
        self.vertex = vertex
    #return the Vertex object's string
    def getKey(self):
        return self.vertex

class Edge():
    #edge is a string
    def __init__(self, u, v, edge):
        self.name = str(edge)
        self.origin = u
        self.destination = v
    #return the Edge object's string
    def getKey(self):
        return self.name
    def getDestination(self):
        return self.destination
    def getOrigin(self):
        return self.origin


class Graph_adjacency_map():
    def __init__(self):
        self.Map = {}
        self.V_Set = set()

    def remove_edge(self,e): 
        for verMap in self.Map:
            for j in verMap:
                if verMap[j] == e:
                    verMap.pop(j)

    def print_all_vertex(self):
        for u in self.Map.keys():
            MapOfU = self.Map[u]
            for v in MapOfU.keys():
                e = str(MapOfU[v].getKey())
                print("u = " + u + " v = " + v + 
                " edge = " + e)

    def vertex_count(self): 
        return len(V_Set)

    def edge_count(self): 
        c = 0
        for subMap in self.Map:
            c += len(subMap)
        return c

    def get_edge(self, u, v): 
        if u.getKey() in self.Map.keys():
            MapU = self.Map[u.getKey()]
            if v.getKey() in MapU.keys():
                return MapU[v.getKey()]
        return None

    def degree(self, v): 
        if v.getKey() in MapU.keys():
                return len(MapU[v.getKey()])
        return 0
        
    def insert_vertex(self, x): 
        #create new vertex object u
        u = Vertex(x)
        #add vertex u to V_Set
        self.V_Set.add(u)
        #create a submap for u in Map
        self.Map[u.getKey()] = {}

    def insert_edge(self, u, v, x):
        e = Edge(Vertex(u), Vertex(v), x)
        MapOfu = self.Map[u.getKey()]
        MapOfu[v.getKey()] = e
        return e
    

