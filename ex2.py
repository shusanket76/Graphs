def depthfirstSearch(graph, source):
    res = []

    def dfs(source):
        res.append(source)
        if source not in graph:
            return 
        node = graph[source]
        for x in node:
            
            dfs(x)
    dfs(source)
    return res
# ===========================================================================================================

# by using stack
def depthfirstSearch2(graph, source):
    stack  = []
    res = []
    stack.append(source)
    while stack:
        node = stack.pop()
        if node:
            res.append(node)
            if node in graph:
                for x in graph[node]:
                    stack.append(x)
    return res
            




graph = {
    "a":["b","c"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}
a  = depthfirstSearch2(graph, "a")
print(a)