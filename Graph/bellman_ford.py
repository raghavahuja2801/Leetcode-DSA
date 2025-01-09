def bellman_ford(graph, vertices, start):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Check for negative weight cycle
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative weight cycle")
                return None

    return distances

# Example usage
graph = {
    0: [(1, -1), (2, 4)],
    1: [(2, 3), (3, 2), (4, 2)],
    2: [(3, 5)],
    3: [(4, -3)],
    4: []
}
vertices = [0, 1, 2, 3, 4]
start = 0
print("Shortest distances from node 0:", bellman_ford(graph, vertices, start))
