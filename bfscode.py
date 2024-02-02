from collections import defaultdict
import random 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def generate_random_graph(self, num_nodes, num_edges):
        for _ in range(num_edges):
            u = random.randint(0, num_nodes - 1)
            v = random.randint(0, num_nodes - 1)
            self.add_edge(u, v)

 
    def BFS(self, start):
        visited = {node: False for node in self.graph}
        color = {node: "WHITE" for node in self.graph}
        queue = []
        print("\nBefore Bfs: ",color)
        queue.append(start)
        visited[start] = True
 
        while queue:
            print()
            current = queue.pop(0)
 
            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    color[neighbor] = "GRAY"
            color[current] = "BLACK"
            print(f" Itration for node {current}: ",color)
 
 

graph = Graph()

graph.generate_random_graph(10, 50)
 
print("BFS Traversal starting from vertex 2:")
graph.BFS(2)