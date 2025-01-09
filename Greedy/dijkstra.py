import heapq

def dijkstra(graph, start):
    """
    Find the shortest paths from the start node to all other nodes using Dijkstra's algorithm.
    
    Parameters:
        graph (list[list[tuple]]): A graph represented as an adjacency list with (node, weight) tuples.
        start (int): The starting node.
    
    Returns:
        list[int]: The shortest distance to each node from the start.
    """
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    min_heap = [(0, start)]  # (distance, node)

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        if dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return distances

# Example usage
graph = [
    [(1, 4), (2, 1)],  # Node 0
    [(0, 4), (2, 2), (3, 5)],  # Node 1
    [(0, 1), (1, 2), (3, 8)],  # Node 2
    [(1, 5), (2, 8)]   # Node 3
]
start_node = 0
print("Shortest distances:", dijkstra(graph, start_node))
