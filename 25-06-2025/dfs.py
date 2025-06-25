'''
DFS:
    depth first search: is a graoh traversal algorithm that starts from a source node and explores as far s possiblr along each branch before backtracing
    uses stack (either expliciltu oy recursion) and goes deep into one path before trying other

'''
def dfs_iterative(graph,start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            if node in graph:
                stack.extend(reversed(graph[node]))
                
Graph = {
    'A' : ['B','C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'G' : ['H']
}
dfs_iterative(Graph,'A')