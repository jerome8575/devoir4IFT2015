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



