graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4', '5'],
    '7' : ['8', '9', '5'],
    '4' : ['6', '3'],
    '6' : ['4'],
    '2' : ['3'],
    '8' : ['7'],
    '9' : ['7']
}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]  # Create a new path by adding the start node
    if start == end:
        return [path]  # If start and end are the same, we've found a path

    if start not in graph:
        return []  # No path if the start node is not in the graph

    paths = []  # List to store all possible paths
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_paths = find_all_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)  # Append all new paths to the list of paths
    return paths

# Driver code
print("Enter Starting node : ")
src = input().strip()
print("Enter Destination node : ")
dest = input().strip()

# Find all paths from src to dest
all_paths = find_all_paths(graph, src, dest)
print(f"All possible paths from {src} to {dest}:")
for path in all_paths:
    print(" -> ".join(path))
