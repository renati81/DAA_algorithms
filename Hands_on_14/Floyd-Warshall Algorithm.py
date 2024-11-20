def floyd_warshall(graph):
    # Initialize distances matrix (copy of the input graph matrix)
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    next_vertex = [[None if graph[i][j] == float('infinity') else j for j in range(n)] for i in range(n)]

    # Perform the algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex

# Function to reconstruct the shortest path
def reconstruct_path(next_vertex, u, v):
    if next_vertex[u][v] is None:
        return None
    path = [u]
    while u != v:
        u = next_vertex[u][v]
        path.append(u)
    return path

# Graph from the example (as adjacency matrix)
example_graph = [
    [0, 3, float('infinity'), 8, -4],
    [float('infinity'), 0, float('infinity'), 1, 7],
    [float('infinity'), 4, 0, float('infinity'), float('infinity')],
    [2, float('infinity'), -5, 0, float('infinity')],
    [float('infinity'), float('infinity'), float('infinity'), 6, 0]
]

# Additional example graph (as adjacency matrix)
additional_graph = [
    [0, 2, float('infinity'), 1],
    [float('infinity'), 0, 3, float('infinity')],
    [float('infinity'), float('infinity'), 0, -2],
    [float('infinity'), 1, float('infinity'), 0]
]

# Testing Floyd-Warshall on the example graph
distances_example, next_example = floyd_warshall(example_graph)

# Testing Floyd-Warshall on the additional example graph
distances_additional, next_additional = floyd_warshall(additional_graph)

# Reconstructing paths for the example graph
example_paths = {}
for i in range(len(example_graph)):
    for j in range(len(example_graph)):
        example_paths[(i, j)] = reconstruct_path(next_example, i, j)

# Reconstructing paths for the additional graph
additional_paths = {}
for i in range(len(additional_graph)):
    for j in range(len(additional_graph)):
        additional_paths[(i, j)] = reconstruct_path(next_additional, i, j)

# Displaying results for the example graph
print("Example Graph Shortest Path Matrix:")
for row in distances_example:
    print(row)

print("\nExample Graph Paths:")
for (u, v), path in example_paths.items():
    print(f"Path from {u} to {v}: {path}")

# Displaying results for the additional graph
print("\nAdditional Graph Shortest Path Matrix:")
for row in distances_additional:
    print(row)

print("\nAdditional Graph Paths:")
for (u, v), path in additional_paths.items():
    print(f"Path from {u} to {v}: {path}")
