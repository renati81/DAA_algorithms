import heapq

# Define Dijkstra's algorithm
def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    predecessors = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if the distance is not optimal
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Function to reconstruct the shortest path
def get_shortest_path(predecessors, start, target):
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    return path if path[0] == start else None

# Graph from the uploaded example (as adjacency list)
example_graph = {
    's': [('t', 10), ('y', 5)],
    't': [('x', 1), ('y', 2)],
    'x': [('z', 4)],
    'y': [('t', 3), ('x', 9), ('z', 2)],
    'z': [('x', 6), ('s', 7)]
}

# Additional example graph
additional_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

# Testing the algorithm on the example graph
distances_example, predecessors_example = dijkstra(example_graph, 's')
example_paths = {node: (get_shortest_path(predecessors_example, 's', node), distances_example[node]) for node in example_graph.keys()}

# Testing the algorithm on the additional graph
distances_additional, predecessors_additional = dijkstra(additional_graph, 'A')
additional_paths = {node: (get_shortest_path(predecessors_additional, 'A', node), distances_additional[node]) for node in additional_graph.keys()}

# Display results for example graph
print("Example Graph:")
for node, (path, distance) in example_paths.items():
    print(f"Shortest path to {node}: {path}, Distance: {distance}")

# Display results for additional graph
print("\nAdditional Example Graph:")
for node, (path, distance) in additional_paths.items():
    print(f"Shortest path to {node}: {path}, Distance: {distance}")
