graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4','5'],
    '7' : ['8', '9','5'],
    '4' : ['6','3'],
    '6' : ['4'],
    '2' : ['3'],
    '8' : ['7'],
    '9' : ['7']
}

visit = []
queue = []
parent = {}

def bfs(visit, graph, node):
    visit.append(node)
    queue.append(node)
    parent[node] = None
    while queue:
        m = queue.pop(0)

        for neighbour in graph[m]:
            if neighbour not in visit:
                visit.append(neighbour)
                queue.append(neighbour)
                parent[neighbour] = m

# Driver Code
print("Enter Starting node : ")
src = input()
bfs(visit, graph,src)
path = [] 
print("Enter Destination node : ")
node = input()
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()
print(path)

    


