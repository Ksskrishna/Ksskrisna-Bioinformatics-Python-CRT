'''
a graph is a pair g = (v.e), where v is a set whose elements are called vertices, and E is a set of two sets of vertices, whose elements are called edges

the vertices x and y of an edge (x,y) are called end points of the edge, the edge is said to join x ans y 
graph operations
    add vertex
    add edge
    remove vertex
    remove edge
    display graph
    traversal
    view edges
    get neighbour edges

A -> ['B','C']
A -> ['B','C']

'''
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])
g= Graph()
g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('C','D')
g.add_edge('D','E')
g.add_edge('E','F')
g.add_edge('F','G')
g.display()

