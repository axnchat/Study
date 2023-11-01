# Define a graph using an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Initialize a set to keep track of visited nodes.
visited = set()

def dfs(node):
    # If the node hasn't been visited yet, visit it.
    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        # Visit all neighboring nodes recursively.
        for neighbor in graph[node]:
            dfs(neighbor)

# Start DFS from a specific node (e.g., 'A').
start_node = 'A'
print("Depth-First Search starting from node", start_node, ":")
dfs(start_node)
