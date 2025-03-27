class Graph(object):
    def __init__(self, size):
        self.incMatrix = []
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Та же вершина {v1} и {v2}")
            return
        newEdge = [1 if i == v1 or i == v2 else 0 for i in range(self.size)]
        self.incMatrix.append(newEdge)

    def __len__(self):
        return self.size

    def remove_edge(self, v1, v2):
        for e in range(len(self.incMatrix)):
            if self.incMatrix[e][v1] and self.incMatrix[e][v2]:
                self.incMatrix.pop(e)
                return
        print(f"Нет ребра между {v1} и {v2}")