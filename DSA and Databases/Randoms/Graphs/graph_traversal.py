from pprint import pprint
from collections import deque

class Queue:
    def __init__(self, l: list):
        self.queue = l 
    
    def enque(self,n):
        self.queue.append(n)
    
    def deque(self)-> int:
        if len(self.queue) == 0:
            print('Queue is empty')
            return -1
        else:
            return self.queue.pop(0)
  

class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]
        self.V = vertices

    def addEdge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, src):
        hasVisited = {}
        q = Queue([])
        l = []

        q.enque(src)      
        hasVisited[src] = True

        while(len(q.queue)!=0):
            a = q.deque()
            l.append(a)

            for i in self.graph[a]:
                if i not in hasVisited.keys():
                    q.enque(i)
                    hasVisited[i] = True
        return l

g = Graph(5)
g.addEdge(1,0)
g.addEdge(1,3)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,4)

print(g.graph)
print(g.bfs(2))

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)

print(g.bfs(0))