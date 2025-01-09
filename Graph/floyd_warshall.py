def floyd_warshall(graph, vertices):
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}

    for v in vertices:
        dist[v][v] = 0

    for v in graph:
        for u, weight in graph[v]:
            dist[v][u] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage
graph = {
    0: [(1, 3), (2, 8), (3, -4)],
    1: [(2, 1)],
    2: [(3, 7)],
    3: [(0, 2), (1, -5)]
}
vertices = [0, 1, 2, 3]
print("All pairs shortest paths:", floyd_warshall(graph, vertices))
