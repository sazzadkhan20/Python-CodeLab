graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8','9'],
    '4' : ['6'],
    '6' : [],
    '2' : [],
    '8' : [],
    '9' : []
}
visit = []
queue = []

def bfs(visit,graph,node):
    visit.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visit:
                visit.append(neighbour)
                queue.append(neighbour)



#Driver Code
print("Following BFS is : ")
bfs(visit,graph,'5')