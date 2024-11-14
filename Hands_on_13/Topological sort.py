from collections import defaultdict

def topological_sort(graph):
    # A set to track visited nodes
    visited = set()
    # A list to store the topological order
    stack = []

    # Recursive DFS function
    def dfs(node):
        if node not in visited:
            visited.add(node)
            # Visit all the neighbors
            for neighbor in graph[node]:
                dfs(neighbor)
            # Add to stack after visiting all neighbors
            stack.append(node)

    # Perform DFS for each node in the graph
    for vertex in graph:
        dfs(vertex)

    # Reverse the stack to get the topological order
    return stack[::-1]


# Example 1
graph_example1 = {
    "undershorts": ["pants", "shoes"],
    "pants": ["belt", "shoes"],
    "belt": ["jacket"],
    "shirt": ["tie", "belt"],
    "tie": ["jacket"],
    "jacket": [],
    "socks": ["shoes"],
    "shoes": [],
    "watch": []
}

# Perform topological sort
result_example1 = topological_sort(graph_example1)

# Example 2: Custom graph
custom_graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H"],
    "F": ["H"],
    "G": ["A", "B"],
    "H": []
}

# Perform topological sort
result_custom_graph = topological_sort(custom_graph)

# Print the results
print("Topological Sort:", result_example1)
print("\nTopological Sort:", result_custom_graph)

#Test results:
#Topological Sort: ['watch', 'socks', 'shirt', 'tie', 'undershorts', 'pants', 'shoes', 'belt', 'jacket']

#Topological Sort: ['G', 'B', 'D', 'F', 'A', 'C', 'E', 'H']
