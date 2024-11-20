def bellman_ford(graph, start):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}

    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle.")

    return distances, predecessors

# Function to reconstruct the shortest path
def get_shortest_path(predecessors, start, target):
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    return path if path[0] == start else None

# Graph from the example (as adjacency list)
example_graph = {
    'v0': [('v1', 0), ('v2', 5), ('v3', 0), ('v4', 0)],
    'v1': [('v5', -1)],
    'v2': [('v5', 1)],
    'v3': [('v2', 3), ('v4', -3)],
    'v4': [('v1', -1)],
    'v5': []
}

# Additional example graph
additional_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', -2), ('D', 2)],
    'C': [('D', 3)],
    'D': [('A', -4)]
}

# Testing the algorithm on the example graph
try:
    distances_example, predecessors_example = bellman_ford(example_graph, 'v0')
    example_paths = {node: (get_shortest_path(predecessors_example, 'v0', node), distances_example[node]) for node in example_graph.keys()}
except ValueError as e:
    example_paths = str(e)

# Testing the algorithm on the additional graph
try:
    distances_additional, predecessors_additional = bellman_ford(additional_graph, 'A')
    additional_paths = {node: (get_shortest_path(predecessors_additional, 'A', node), distances_additional[node]) for node in additional_graph.keys()}
except ValueError as e:
    additional_paths = str(e)

# Print the results
print("Example Graph:")
if isinstance(example_paths, str):
    print(example_paths)
else:
    for node, (path, distance) in example_paths.items():
        print(f"Shortest path to {node}: {path}, Distance: {distance}")

print("\nAdditional Example Graph:")
if isinstance(additional_paths, str):
    print(additional_paths)
else:
    for node, (path, distance) in additional_paths.items():
        print(f"Shortest path to {node}: {path}, Distance: {distance}")

#output:
#Example Graph:
#Shortest path to v0: ['v0'], Distance: 0
#Shortest path to v1: ['v0', 'v3', 'v4', 'v1'], Distance: -4
#Shortest path to v2: ['v0', 'v3', 'v2'], Distance: 3
#Shortest path to v3: ['v0', 'v3'], Distance: 0
#Shortest path to v4: ['v0', 'v3', 'v4'], Distance: -3
#Shortest path to v5: ['v0', 'v3', 'v4', 'v1', 'v5'], Distance: -5

#Additional Example Graph:
#Shortest path to A: ['A'], Distance: 0
#Shortest path to B: ['A', 'B'], Distance: 4
#Shortest path to C: ['A', 'C'], Distance: 2
#Shortest path to D: ['A', 'C', 'D'], Distance: 5

