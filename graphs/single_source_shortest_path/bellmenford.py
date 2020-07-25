from collections import defaultdict
class Bellmenford:
    def __init__(self,count_of_vertices):
        self.solved = False
        self.vertices = count_of_vertices
        self.graph = defaultdict(dict)
        self.cycle = False # default making no cycle
    def addEdge(self,vertex1,vertex2, weight):
        self.graph[vertex1][vertex2] = weight
    def solve(self):
        if not self.solved:
            distances = [float('inf')]*self.vertices
            for _ in range(self.vertices -1):
                for key1 in self.graph.keys():
                    for key2 in self.graph[key1]:
                        if distances[key1]!=float('inf') and distances[key1] + self.graph[key1][key2] < distances[key2]:
                            distances[key2] = distances[key1]+ self.graph[key1][key2]
            
            for key1 in self.graph.keys():
                for key2 in self.graph[key1]:
                    if distances[key1]!=float('inf') and distances[key1] + self.graph[key1][key2] < distances[key2]:
                        self.cycle = True
                        break
            self.solved = True
        if self.cycle:
            print('it has a negative cycle in it')
            return []
        else:
            return distances