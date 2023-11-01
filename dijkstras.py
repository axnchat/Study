#1)Assign the start vertex a distance of 0 in a min heap
#2)Assign every other vertex a distance of infinity in a min heap
#3)Remove the vertex with the smallest distance from the min heap and set that to the current vertex
#4)For the current vertex, consider all of it’s adjacent vertices and calculate the distance to them by (distance to the current vertex) + (edge weight of current vertex to adjacent vertex). If this new distance is less than its current distance, replace the distance.
#5)Repeat 4 and 5 until the heap is empty
#6)After the heap is empty, return the distances
from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  # Finish dijkstras() below:
  while vertices_to_explore:
    current_distance,current_vertex = heappop(vertices_to_explore)
    for neighbor,edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore,(new_distance,neighbor))
  
  return distances
        
distances_from_a = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_a))

# Here are some common interview questions that involve Dijkstra's Algorithm:

# Single Source Shortest Path: You are given a weighted graph (can be both directed and undirected), and a source vertex. Write a code that returns the shortest path from the source vertex to all other vertices using Dijkstra's algorithm.

# Shortest Path to Specific Target: You are given a graph with weighted edges, a source vertex and a target vertex. Your task is to find the shortest path from the source to the target using Dijkstra's algorithm.

# Network Delay Time: You are given a network of n nodes labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node and w is the time it takes for a signal to travel from source to target. Write a code to find out how long it will take for all nodes to receive the signal. If it is impossible for all nodes to receive the signal, return -1 - a variant of a classic challenge that uses Dijkstra's algorithm.

# Cheapest Flights Within K Stops: There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w. Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1 - a more complex variation requiring adaptations to the classic Dijkstra's algorithm.

# Find the City With the Smallest Number of Neighbors at a Threshold Distance: You are given an edge list representing a weighted graph and a distance threshold. Each edge[i] = [from, to, weight] represents a bidirectional and weighted connection between cities 'from' and 'to'. Return the city with the smallest number of cities that are reachable through some path and whose distance (sum of weights) is at most the distanceThreshold. If there are multiple such cities, return the city with the greatest number - a tailored problem where you're not actually finding shortest paths per se, but leveraging similar traversal logic that Dijkstra’s algorithm employs.

# Remember, these are more interview-oriented questions and some of them might require you to modify the basic Dijkstra's algorithm to solve the problem.