# codebasics
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}
        
        for x in edges:
            if x[0] in self.graph:
                self.graph[x[0]].append(x[1])
            else:
                self.graph[x[0]] = [x[1]]

    def getpaths(self, start,end):
        res = []

        def dfs(start, end, curr):
            curr.append(start)
            if start==end:
                res.append(curr[:])
                return 
            if start not in self.graph:
                return 
            node = self.graph[start]
            for x in node:
                dfs(x, end, curr)
                curr.pop()
            
        dfs(start, end, curr=[])
        return res

    def getshortestpath(self, start, end):
        
        def dfs(start, end, curr ):
            curr.append(start)
            if start==end:
                return curr[:]
            if start not in self.graph:
                return 
            shortest=None
            node = self.graph[start]
            for x in node:
                a = dfs(x, end, curr)
                if a is not None:
                    if shortest is None:
                        shortest = a[:]
                    else:
                        if len(shortest)<len(a):
                            shortest=a[:]
                curr.pop()
            return shortest
            
        curr = []
        return dfs(start, end,curr)



routes = [
    
    ("Mumbai", "Paris"), 
    ("Mumbai", "Dubai"), 
    ("Paris", "Dubai"), 
    ("Paris", "NewYork"), 
    ("Dubai", "NewYork"), 
    ("NewYork", "Tornoto"), 
]
a = Graph(routes)
b = a.getshortestpath("Paris","Tornoto")
print(b)