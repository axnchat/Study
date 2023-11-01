""" Question:

You are given a weighted graph G, which can be directed or undirected, and a source vertex S. Write a Python function to implement Dijkstra's algorithm to find the shortest path from the source vertex S to all other vertices in the graph. Your function should return a dictionary that maps each vertex to its shortest distance from the source S.

The graph is represented as an adjacency list, where each key in the dictionary represents a vertex, and the corresponding value is a list of tuples. Each tuple represents a neighbor vertex and the weight of the edge connecting them. If there is no direct edge between two vertices, you can assume the weight as infinity.

Your code should handle both directed and undirected graphs, and it should also consider cases where there might be negative weights. """

from heapq import heappop,heappush
from math import inf

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
source = 'A'


def dijkstra_shortest_path(graph, source):
    distances_from_source = {}
    for vertex in graph:
        distances_from_source[vertex] = inf
    distances_from_source[source] = 0
    vertices_to_look = [(0,source)]

    while vertices_to_look:
        dist,vertex = heappop(vertices_to_look)
        for neigh,weight in graph[vertex] :
            new_distance = dist + weight
            if new_distance < distances_from_source[neigh]:
                distances_from_source[neigh] = new_distance
                heappush(vertices_to_look,(new_distance,neigh))
    
    return distances_from_source





result = dijkstra_shortest_path(graph, source)
print(result)

# Output:
# {
#    'A': 0,
#    'B': 1,
#    'C': 3,
#    'D': 4
# }
