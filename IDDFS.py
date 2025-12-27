from collections import defaultdict

# Function to perform Depth Limited Search (DLS)
def DLS(graph, node, goal, depth, visited, current_level):
    if depth == 0:
        current_level.add(node)
        return node == goal

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if DLS(graph, neighbor, goal, depth - 1, visited, current_level):
                return True

    visited.remove(node)  # backtracking step
    return False

# Function to perform Iterative Deepening Depth-First Search (IDDFS)
def IDDFS(graph, start, goal, max_depth):
    previous_level = set()
    last_level = set()
    for depth in range(max_depth + 1):
        visited = set()
        current_level = set()
        print(f"Exploring depth: {depth}")
        DLS(graph, start, goal, depth, visited, current_level)
        combined_levels = sorted(previous_level.union(current_level))
        print(f"Nodes up to depth {depth}: {combined_levels}")
        previous_level = previous_level.union(current_level)
        if not current_level:
            last_level = previous_level  # Track the last level with nodes
            break
        if goal in current_level:
            print(f"Goal node {goal} found at depth {depth}")
            return combined_levels

    print(f"All nodes up to the last explored depth: {sorted(last_level)}")
    return sorted(last_level)

# Input the graph
def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Since the graph is undirected
    return graph

# Input data
nodes, edges_count = 9, 7
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (6, 8)
]

# Build the graph
graph = build_graph(edges)

# Starting node and goal node
start_node = 1
goal_node = 6

# Maximum depth to search
max_depth = nodes  # Set to the total number of nodes (worst case)

# Run IDDFS
final_nodes = IDDFS(graph, start_node, goal_node, max_depth)

# Output result
if final_nodes:
    print(f"Nodes up to final depth containing goal node {goal_node}: {final_nodes}")
else:
    print(f"No path exists to goal node {goal_node}.")
