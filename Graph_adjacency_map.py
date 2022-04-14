class Vertex():
    #vertex is a string
    def __init__(self, vertex):
        self.vertex = vertex
    #return the Vertex object's string
    def getKey(self):
        return self.vertex
    
class Edge():
    #edge is a string
    def __init__(self, edge):
        self.edge = edge
    #return the Edge object's string
    def getKey(self):
        return self.edge


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
        e = Edge(x)
        MapOfu = self.Map[u.getKey()]
        MapOfu[v.getKey()] = e
        return e
    

def DFS(g, u, discovered):
    #This is just for the first node visited
    if u.getKey() not in discovered.keys():
        print("We start at " + u.getKey())
        discovered[u.getKey()] = Edge("ORIGIN")
    #We discovered all of the airports!
    if len(discovered.keys()) == len(g.V_Set):
        print("success!");return discovered
    #visit the first undiscovered adjacent vertex of u
    for v in g.V_Set:
        if ( v.getKey() not in discovered.keys() 
        and g.get_edge(u, v) != None ):
            e = g.get_edge(u, v)
            discovered[v.getKey()] = e
            print("We go to " + v.getKey())
            return DFS(g, v, discovered)
    #Dead end!, we need to backpropagate!
    #find the the origin vertex to backpropagate
    prev = None 
    for h in discovered.keys():
        h = Vertex(h)
        if g.get_edge(h, u) == discovered[u.getKey()]:
            prev = h
            print("We go back to " + prev.getKey())
            break
    #can't find the vertex to backpropagate
    if prev == None: 
        print("We failed to discover all the airports")
        return discovered
    #backpropagate
    return DFS(g, prev, discovered)


def main():
    #create Graph
    graph = Graph_adjacency_map()
    #add Vertices
    for v in {"BOS","JFK","MIA","DFW","ORD","LAX","SFO"}:
        graph.insert_vertex(v)
    #add Edges
    graph.insert_edge(Vertex("BOS"), Vertex("JFK"), 35)
    graph.insert_edge(Vertex("BOS"), Vertex("MIA"), 247)
    graph.insert_edge(Vertex("JFK"), Vertex("MIA"), 903)
    graph.insert_edge(Vertex("JFK"), Vertex("SFO"), 45)
    graph.insert_edge(Vertex("JFK"), Vertex("DFW"), 1387)
    graph.insert_edge(Vertex("MIA"), Vertex("DFW"), 523)
    graph.insert_edge(Vertex("MIA"), Vertex("LAX"), 411)
    graph.insert_edge(Vertex("DFW"), Vertex("ORD"), 335)
    graph.insert_edge(Vertex("ORD"), Vertex("DFW"), 877)
    graph.insert_edge(Vertex("DFW"), Vertex("LAX"), 49)
    graph.insert_edge(Vertex("LAX"), Vertex("ORD"), 120)
    #print graph
    graph.print_all_vertex()
    #get our search
    searchPath = DFS(graph, Vertex("BOS"), {})
    
main()
