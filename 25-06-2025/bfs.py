'''
BFS traversal:
    BFS is an algorithm where we start from the selected node 
    and traverse the graph level-wise or layer-wise thus exploring the neighbour nodes
    (which are directly connected to starting node), and then moving onti next level neighbor nodes
    as the name suggests: 
        we first move horizontally and visit all the nodes of the current layer
        then move to the next layer

'''
def bfs_iterative(graph,start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
    return bfs_iterative(graph,start)
graph = {

    'A': ['B','C'],
    'B': ['D'],
    'C': ['E']
}
bfs_iterative(graph,'A')