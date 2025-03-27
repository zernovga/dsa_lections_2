from collections import deque

def isCyclic(self):
    inDegree = [0] * self.V
    q = deque()
    visited = 0
    for u in range(self.V):
        for v in self.adj[u]:
            inDegree[v] += 1
    for u in range(self.V):
        if inDegree[u] == 0:
            q.append(u)
    while q:
        u = q.popleft()
        visited += 1
        for v in self.adj[u]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                q.append(v)
    return visited != self.V