import heapq

def prim_mst(graph):
    """
    Find the minimum spanning tree using Prim's algorithm.
    
    Parameters:
        graph (list[list[tuple]]): A graph represented as an adjacency list with (node, weight) tuples.
    
    Returns:
        int: The weight of the minimum spanning tree.
    """
    n = len(graph)
    mst_weight = 0
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if visited[node]:
            continue

        visited[node] = True
        mst_weight += weight

        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst_weight

# Example usage
graph = [
    [(1, 2), (3, 1)],  # Node 0
    [(0, 2), (2, 3)],  # Node 1
    [(1, 3), (3, 4)],  # Node 2
    [(0, 1), (2, 4)]   # Node 3
]
print("Weight of MST:", prim_mst(graph))
