import heapq

def prim(graph, start):
    mst = []
    visited = set()
    pq = [(0, start)]  # (weight, node)
    total_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if node not in visited:
            visited.add(node)
            mst.append((node, weight))
            total_weight += weight

            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor))

    return mst, total_weight

# Example usage
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 1)],
    2: [(0, 3), (1, 1)]
}
start = 0
mst, total_weight = prim(graph, start)
print("Minimum Spanning Tree:", mst)
print("Total weight:", total_weight)
