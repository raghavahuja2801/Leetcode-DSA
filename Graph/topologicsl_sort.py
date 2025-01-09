from collections import defaultdict

def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    stack = [node for node in graph if in_degree[node] == 0]
    topo_order = []

    while stack:
        node = stack.pop()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)
    
    return topo_order if len(topo_order) == len(graph) else "Cycle detected!"

# Example usage
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}
print("Topological Sort:", topological_sort(graph))
