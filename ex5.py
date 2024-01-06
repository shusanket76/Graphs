def countcomponents(graph):
    path = set()
    stack =[]
    count = 0
    for x in graph:
        if x not in path:
            path.add(x)
            stack = []
            stack.append(x)
            while stack:
                node = stack.pop()
                if node in graph:
                    for y in graph[node]:
                        if y not in path:
                            path.add(y)
                            stack.append(y)
        
            count+=1
    return count





graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

a = countcomponents(graph)
print(a)