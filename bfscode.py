from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start):
        visited = {node: False for node in self.graph}
        color = {node: "WHITE" for node in self.graph}
        queue = []

        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    color[neighbor] = "GRAY"
            color[current] = "BLACK"

        print("\nColors:", color)

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("BFS Traversal starting from vertex 2:")
graph.BFS(2)
