# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}
# Expected output: (is_bipartite, bipartition_sets)
# (True, (['A', 'D', 'E'], ['B', 'C', 'F']))

graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E'],
    'D': ['A', 'F'],
    'E': ['B', 'C'],
    'F': ['D', 'G'],
    'G': ['F', 'H'],
    'H': ['G', 'I'],
    'I': ['H', 'J'],
    'J': ['I']
}

# Expected output: (True, (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], []))
# The graph is bipartite with two empty sets indicating no bipartition.

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B'],
    'D': ['B', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F', 'H'],
    'H': ['G', 'I'],
    'I': ['H', 'J'],
    'J': ['I', 'A']
}

# Expected output: (False, None)
# The graph is not bipartite.


def checkBipartite(graph):
    
    visited = {}

    def dfs(node,flag):
        visited[node] = flag

        for child in graph[node]:
            if child in visited and visited[child] == flag:
                return False
            else:
                if child not in visited:
                    if not dfs(child,(flag+1)%2):
                        return False 
    
        return True

    result = True
    for node in graph:
        if node not in visited:
            result = result and dfs(node,0)
    
    left, right = [],[]
    if result == True:
        for key in visited.keys():
            if visited[key] == 0:
                left.append(key)
            else:
                right.append(key)
        return(True,left,right)
    
    return False

print(checkBipartite(graph))
print(checkBipartite(graph1))
print(checkBipartite(graph2))
