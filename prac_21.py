import sys

def prim(graph, n):
    selected = [False] * n
    selected[0] = True  # start from vertex 0

    edges_count = 0
    mst_cost = 0

    print("Edges in MST:")

    while edges_count < n - 1:
        min_edge = sys.maxsize
        x = y = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_edge:
                            min_edge = graph[i][j]
                            x, y = i, j

        print(x, "-", y, ":", graph[x][y])
        mst_cost += graph[x][y]
        selected[y] = True
        edges_count += 1

    print("Total Cost:", mst_cost)


# Driver Code
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph, 5)