import heapq

def a_star_search(graph, start, goal):
    # Priority queue: (f_score, current_node, path, cost_so_far)
    priority_queue = [(graph[start]["heuristic"], start, [start], 0)]
    visited = set()  # Track visited nodes
    while priority_queue:
        f_score, current_node, path, cost_so_far = heapq.heappop(priority_queue)
        # If we reached the goal, return the path and total cost
        if current_node == goal:
            return path, cost_so_far
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node]["edges"].items():
            if neighbor not in visited:
                # Calculate the g_score (actual cost so far) and f_score (g_score + heuristic)
                g_score = cost_so_far + weight
                f_score = g_score + graph[neighbor]["heuristic"]
                heapq.heappush(priority_queue, (f_score, neighbor, path + [neighbor], g_score))
    return None, float('inf')  # Return if no path is found
 
# Graph definition (your example)
graph = {
    "A": {
        "edges": {"B": 2, "C": 3},
        "heuristic": 14
    },
    "B": {
        "edges": {"D": 10, "E": 3},
        "heuristic": 12
    },
    "C": {
        "edges": {"F": 2, "H": 8},
        "heuristic": 10
    },
    "D": {
        "edges": {},
        "heuristic": 50
    },
    "E": {
        "edges": {"G": 2},
        "heuristic": 8
    },
    "F": {
        "edges": {"G": 3},
        "heuristic": 7
    },
    "G": {
        "edges": {},
        "heuristic": 0
    },
    "H": {
        "edges": {},
        "heuristic": 20
    }
}
 
# Run A* to find the shortest path and cost to reach G from A
path, cost = a_star_search(graph, "A", "G")
print("Path:", path)
print("Cost:", cost)