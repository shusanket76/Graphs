# bfs
from collections import deque

def breadthfirstSearch(graph, source):
    queue = deque()
    queue.append(source)
    while queue:
        node = queue.popleft()
        print(node)
        if node in graph:
            for x in graph[node]:
                queue.append(x)










graph = {
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}

a = breadthfirstSearch(graph, "a")
