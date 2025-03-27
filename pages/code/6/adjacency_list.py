class AdjNode:
  def __init__(self, value):
    self.vertex = value
    self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
        
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_graph(self):
        for i in range(self.V):
        print("Вершина " + str(i) + ":", end="")
        temp = self.graph[i]
        while temp:
            print(f" -> {temp.vertex}", end="")
            temp = temp.next
        print(" \n")