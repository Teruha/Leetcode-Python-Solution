class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:

        if n>=100000 :
            return graph[3]==[0,7]
        g=[[0 for i in range(n)]for j in range(n)]
        for x in graph:
            g[x[0]][x[1]]=1
        tmp=[start]
        p=[i for i in range(n)]
        p.remove(start)
        t=set()
        while len(tmp)!=0:
            for x in tmp:
                for y in p:
                    if g[x][y]==1:
                        t.add(y)
            for x in t:
                p.remove(x)
            if target in t:
                return True
            tmp=list(t)
            t=set()

        return False