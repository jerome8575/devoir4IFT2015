# impémentation graphe adjacency list


from Graph_adjacency_matrix import Graph_adjacency_matrix


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


class Graph_adjacency_list:

    def __init__(self):
        self.graph = []
        self.V_Set = set()

    def to_adjacency_matrix(self):
        graphMatrix = Graph_adjacency_matrix(15)
        
        # add vertices

        for node in self.graph:
            graphMatrix.insert_vertex(node.vertex)

        for node in self.graph:
            for edge in node.edges:
                graphMatrix.insert_edge(edge)


    def print_all_vertex(self):
        for node in self.graph:
            for edge in node.edges:
                print("origin: " + edge.getOrigin().getKey() + " -> destination: " + edge.getDestination().getKey() + " Num vol: " + edge.getKey())

    def vertex_count(self):
        return len(self.graph)

    def edge_count(self):
        count = 0
        for node in self.graph:
            count += len(node.edges)

        return count 

    def get_edge(self, u, v):
        for node in self.graph:
            if node.vertex.getKey() == u.getKey():
                for edge in node.edges:
                    if edge.getDestination().getKey() == v.getKey():
                        return edge
        return None 

    def degree(self, v):
        for node in self.graph:
            if node.vertex.getKey() == v.getKey():
                return len(node.edges)

    def insert_vertex(self, x):
        vertex = Vertex(x)
        self.V_Set.add(vertex)
        vertexNode = Node(vertex, [])
        self.graph.append(vertexNode)
        return vertex

    def insert_edge(self, u, v, x):
        edge = Edge(u, v, x)
        for node in self.graph:
            if node.vertex.getKey() == u.getKey():
                node.edges.append(edge)
        return edge

class Node:
    
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges


def DFS(g, u, discovered):
    #This is just for the first node visited
    if u.getKey() not in discovered.keys():
        print("We start at " + u.getKey())
        discovered[u.getKey()] = Edge(Vertex("u"), Vertex("v"), "ORIGIN")
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
    graph = Graph_adjacency_list()
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

    searchPath = DFS(graph, Vertex("BOS"), {})
    
main()
        

