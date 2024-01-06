def undirected_path(edges, source, destination):
    hasmap={}
    def buildgraph(edges):
        for x in edges:
            if x[0] in hasmap:
                hasmap[x[0]].append(x[1])
            else:
                hasmap[x[0]]=[x[1]]
            if x[1] in hasmap:
                hasmap[x[1]].append(x[0])
            else:
                hasmap[x[1]] = [x[0]]
        
    
    path = set()
    def has_path(source, destination):
        if source ==destination:
            return True
        if source in path:
            return False
        if source not in hasmap:
            return False
        path.add(source)
        
        node = hasmap[source]
        for x in node:
                a = has_path(x, destination) 
                if a is True:
                    return True
        return False

        


    a = buildgraph(edges)
    b = has_path(source, destination)
    print(b)


edges = [
    ["i","j"],
    ["k","i"],
    ["m","k"],
    ["k","l"],
    ["o","n"]
]


a  = undirected_path(edges,"j","m")
