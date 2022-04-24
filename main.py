import Graph_adjacency_map
import Graph_adjacency_list
import Graph_adjacency_matrix

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
    Graphs = [Graph_adjacency_matrix(10), Graph_adjacency_list(), Graph_adjacency_list()]
    for graph in Graphs:
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

    print(DFS(Graphs[0], Vertex("BOS"), {}))
    print(DFS(Graphs[1], Vertex("BOS"), {}))
    print(DFS(Graphs[2], Vertex("BOS"), {}))
    
main()


