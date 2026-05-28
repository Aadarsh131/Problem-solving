from typing import Dict, List
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph:Dict = {}):
        self.graph = graph
    
    def add_edge(self, x,y,wt):
        if x not in self.graph: self.graph[x] = {}
        self.graph[x][y] = wt
    
    #doesn't work for negative weighted graph (as it will go on infinite loop over finding the minimum distance)
    def dijktras(self, src):
        dist = {x:float('inf') for x in self.graph.keys()}
        dist[src] = 0
    
        pq = [(0, src)]
        heapify(pq)

        while pq:
            curr_dist, curr_node = heappop(pq)
            
            for neighbour, weight in self.graph[curr_node].items():
                temp_dist = curr_dist + weight
                if temp_dist < dist[neighbour]:
                    dist[neighbour] = temp_dist
                    heappush(pq, (temp_dist, neighbour))

        return dist


graph = {'A': {'B': 3, 'C': 3},
         'B': {'A': 3, 'D': 3.5, 'E': 2.8},
         'C': {'A': 3, 'E': 2.8, 'F': 3.5},
         'D': {'B': 3.5, 'E': 3.1, 'G': 10},
         'E': {'B': 2.8, 'C': 2.8, 'D': 3.1, 'G': 7},
         'F': {'G': 2.5, 'C': 3.5},
         'G': {'F': 2.5, 'E': 7, 'D': 10}
        }

g = Graph(graph=graph)
print(g.graph)
print(g.dijktras('A'))