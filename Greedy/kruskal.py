class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_mst(n, edges):
    """
    Find the minimum spanning tree using Kruskal's algorithm.
    
    Parameters:
        n (int): The number of nodes in the graph.
        edges (list[tuple[int, int, int]]): A list of edges in the form (u, v, weight).
    
    Returns:
        int: The weight of the minimum spanning tree.
    """
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    uf = UnionFind(n)
    mst_weight = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight

    return mst_weight

# Example usage
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
print("Weight of MST:", kruskal_mst(n, edges))
