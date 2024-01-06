def largestcomponent(graph):
    res = [0]
    path = set()
    for x in graph:
        if x not in path:
            path.add(x)
            count = 0
            stack = []
            stack.append(x)
            while stack:
                count+=1
                node = stack.pop()
                if node in graph:
                    for y in graph[node]:
                        if y not in path:
                            path.add(y)
                            stack.append(y)
            res[0] = max(res[0], count)
    return res[0]

graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}


a = largestcomponent(graph)
print(a)