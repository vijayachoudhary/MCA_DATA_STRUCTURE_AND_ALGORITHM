class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

        return True


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    dsu = DSU(n)

    mst = []
    cost = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            cost += w

    return mst, cost


# Driver Code
n = 5  # number of vertices

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

mst, cost = kruskal(n, edges)

print("Edges in MST:")
for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Total Cost:", cost)