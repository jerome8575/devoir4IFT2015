
# impémentation graphe adjacency matrix

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


class Graph_adjacency_matrix:


    def __init__(self, size):
        self.indexCount = 0
        self.indexDict = {}

        self.matrice = []

        for i in range(size):
            self.matrice.append([None for i in range(size)])

        self.size = size

        self.V_Set = set()

    

    def insert_vertex(self, x):

        self.indexDict[x] = self.indexCount
        self.indexCount += 1
        vertex = Vertex(x)
        self.V_Set.add(vertex)

        return vertex

    def insert_edge(self, u, v, x):
        edge = Edge(u, v, x)

        # insert in matrix

        indOrigin = self.indexDict[u.getKey()]
        indDest = self.indexDict[v.getKey()]

        self.matrice[indOrigin][indDest] = edge

        return edge

    def degree(self, v):

        count = 0

        indOrigin = self.indexDict[v.getKey()]
        for destination in self.matrice[indOrigin]:
            if destination  != None:
                count += 1

        return count

    def get_edge(self, u, v):
        indOrigin = self.indexDict[u.getKey()]
        indDest = self.indexDict[v.getKey()]

        return self.matrice[indOrigin][indDest]

    def edge_count(self):

        count = 0

        for row in self.matrice:
            for elem in row:
                if elem != None:
                    count += 1
        return count

    def vertex_count(self):

        return len(self.indexDict)

    def print_all_vertex(self):
        for row in self.matrice:
            for edge in row:
                if edge != None:
                    print("origin: " + edge.getOrigin().getKey() + " -> destination: " + edge.getDestination().getKey() + " Num vol: " + edge.getKey())

    def remove_vertex(self, v):

        indOrigin = self.indexDict[v.getKey()]
        for edge in self.matrice[indOrigin]:
            edge = None

        for row in self.matrice:
            row[indOrigin] = None

                


def main():
    #create Graph
    graph = Graph_adjacency_matrix(10)
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
    
main()


