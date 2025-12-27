def dfs_all_paths(graph, current, destination, path, weight, all_paths):

    path.append(current)

    if current == destination:
        all_paths.append((path[:], weight))
    else:
        for neighbor, edge_weight in graph[current]:
            if neighbor not in path:  
                dfs_all_paths(graph, neighbor, destination, path, weight + edge_weight, all_paths)

    path.pop()

def find_all_paths(graph, start, end):
    all_paths = []  
    dfs_all_paths(graph, start, end, [], 0, all_paths)
    return all_paths

def get_shortest_paths(all_paths):
    min_weight = min(path[1] for path in all_paths)
    shortest_paths = [path for path in all_paths if path[1] == min_weight]
    return shortest_paths, min_weight

graph = {
    1: [(2, 3), (3, 4)],
    2: [(4, 7)],
    3: [(2, 2), (4, 1), (5, 2)],
    4: [(5, 1), (6, 4)],
    5: [(6, 3)],
    6: []
}


start,end = 1, 6
all_paths = find_all_paths(graph, start, end)
shortest_paths, min_weight = get_shortest_paths(all_paths)

print("All Possible Paths:")
for path, weight in all_paths:
    print(f"Path: {path}, Weight: {weight}")

print("\nAll Shortest Paths:")
for path, weight in shortest_paths:
    print(f"Path: {path}, Weight: {weight}\n")

print("\nTotal Weight of Shortest Paths:", min_weight)
