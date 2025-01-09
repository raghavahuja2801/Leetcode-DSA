import random

def karger_min_cut(graph):
    """
    Find a minimum cut in an undirected graph using Karger's algorithm.
    
    Parameters:
        graph (dict): A dictionary representing the graph, where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        int: The minimum cut value.
    """
    n = len(graph)

    while n > 2:
        u = random.choice(list(graph.keys()))  # Pick a random node
        v = random.choice(graph[u])  # Pick a random neighbor of u

        # Merge the nodes u and v
        graph[u].extend(graph[v])  # Add edges of v to u
        graph[u] = [x for x in graph[u] if x != u and x != v]  # Remove self-loops

        # Update neighbors of u and v
        for neighbor in graph[v]:
            graph[neighbor] = [u if x == v else x for x in graph[neighbor]]

        # Remove node v from the graph
        del graph[v]
        n -= 1

    # The minimum cut is the number of edges crossing the cut
    cut_edges = len(graph.popitem()[1])
    return cut_edges

# Example usage
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
print("Minimum cut:", karger_min_cut(graph))
