# Union-Find (Disjoint Set Union) implementation
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


# Kruskal's Algorithm Implementation
def kruskal_algorithm(num_nodes, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_nodes)

    mst = []  # To store the edges of the Minimum Spanning Tree
    mst_cost = 0  # To store the total cost of the MST

    for u, v, weight in edges:
        # Check if adding the edge creates a cycle
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost


# Example 1: Graph from the book
edges_example1 = [
    (0, 1, 4), (0, 7, 8),
    (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 5, 4), (2, 8, 2),
    (3, 4, 9), (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1), (6, 8, 6),
    (7, 8, 7)
]
num_nodes_image_example = 9

# Example 2: Custom graph
edges_custom_example = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
num_nodes_custom_example = 4

# Testing Kruskal's Algorithm on the Graph
print("Kruskal's Algorithm on Graph:")
mst_image, cost_image = kruskal_algorithm(num_nodes_image_example, edges_example1)
print("MST:", mst_image)
print("Total Cost:", cost_image)
print()

# Testing Kruskal's Algorithm on the Custom Graph
print("Kruskal's Algorithm on Custom Graph:")
mst_custom, cost_custom = kruskal_algorithm(num_nodes_custom_example, edges_custom_example)
print("MST:", mst_custom)
print("Total Cost:", cost_custom)
print()

#Test results:
#Kruskal's Algorithm on Graph:
#MST: [(6, 7, 1), (2, 8, 2), (5, 6, 2), (0, 1, 4), (2, 5, 4), (2, 3, 7), (0, 7, 8), (3, 4, 9)]
#Total Cost: 37

#Kruskal's Algorithm on Custom Graph:
#MST: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
#Total Cost: 19
