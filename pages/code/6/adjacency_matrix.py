class Graph(object):
    def __init__(self, size):
        self.adjMatrix = [[0] * size for i in range(size)]
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Та же вершина {v1} и {v2}")
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __len__(self):
        return self.size

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"Нет ребра между {v1} и {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(f'{val:4d}')
            print()