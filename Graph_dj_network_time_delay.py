""" Question:

You are given a network with n nodes labeled from 1 to n and a list of travel times as directed edges. The travel times are represented as times, where times[i] = (u, v, w) means that there is a directed edge from node u to node v, and it takes w units of time for a signal to travel from node u to node v. Your task is to find out how long it will take for all nodes to receive the signal.

Write a Python function that takes the number of nodes n, the list of travel times times, and a source node k as input and returns the minimum time it takes for a signal to reach all nodes in the network. If it's impossible for all nodes to receive the signal, return -1. """
from math import inf
from heapq import heappop,heappush

n = 4
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
k = 2

def network_delay_time(n,times,k):
    graph = [[] for _ in range(n+1)]
    for source,dest,weight in times:
        graph[source].append([weight,dest])

    times_from_source = {}
    for i in range(n+1):
        times_from_source[i] = inf
    
    times_from_source[k] = 0

    nodes_to_explore = [(0,k)]
    max_time = -inf

    while nodes_to_explore:
        current_time,node = heappop(nodes_to_explore)
        for weight,vertex in graph[node]:
            new_time = current_time + weight
            if new_time <  times_from_source[vertex]:
                times_from_source[vertex] = new_time
                max_time = max(max_time,new_time)
                heappush(nodes_to_explore,(new_time,vertex))
    
    return max_time




result = network_delay_time(n, times, k)
print(result)

# Output:
# 2
