from collections import defaultdict

# Recursive DFS Implementation
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"Visited: {start}")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

# Iterative DFS Implementation
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)
            # Add neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# Example 1: Graph from the image
graph_example1 = {
    'u': ['v', 'x'],
    'v': ['y'],
    'x': ['v'],
    'y': ['x'],
    'w': ['y', 'z'],
    'z': ['z']
}

# Example 2: Custom graph
custom_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Testing Recursive DFS on Example1 Graph
print("Recursive DFS on Example1 Graph:")
visited_recursive = dfs_recursive(graph_example1, 'u')
print()

# Testing Iterative DFS Example1 Graph
print("Iterative DFS on Example1 Graph:")
visited_iterative = dfs_iterative(graph_example1, 'u')
print()

# Testing Recursive DFS on Custom Graph
print("Recursive DFS on Custom Graph:")
visited_custom_recursive = dfs_recursive(custom_graph, 'A')
print()

# Testing Iterative DFS on Custom Graph
print("Iterative DFS on Custom Graph:")
visited_custom_iterative = dfs_iterative(custom_graph, 'A')
print()

# Test results:
#Recursive DFS on Example1 Graph:
#Visited: u
#Visited: v
#Visited: y
#Visited: x

#Iterative DFS on Example1 Graph:
#Visited: u
#Visited: v
#Visited: y
#Visited: x

#Recursive DFS on Custom Graph:
#Visited: A
#Visited: B
#Visited: D
#Visited: E
#Visited: F
#Visited: C

Iterative DFS on Custom Graph:
Visited: A
Visited: B
Visited: D
Visited: E
Visited: F
Visited: C
