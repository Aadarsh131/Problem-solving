from pprint import pprint
from typing import Dict

class Graph:
    def __init__(self,vertices: int):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def addEdge(self, x: int ,y: int):
       self.graph[x].append(y)
       self.graph[y].append(x)

class WeightedGraph:
    def __init__(self):
        self.wgraph: Dict[str, list[tuple[str,int]]] = {}

    def addEdge(self, u,v,isBidirectional, wt):
        if u not in self.wgraph: self.wgraph[u] = []
        self.wgraph[u].append((v,wt))
        if isBidirectional:
            if v not in self.wgraph: self.wgraph[v] = []
            self.wgraph[v].append((u,wt))

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(1,2)
print(g.graph)



wg = WeightedGraph()
wg.addEdge('A','B',True,20)
wg.addEdge('B','D',True,40)
wg.addEdge('A','C',True,10)
wg.addEdge('C','D',True,40)
wg.addEdge('A','D',False,50)
print(wg.wgraph)
pprint(wg.wgraph,indent=2)