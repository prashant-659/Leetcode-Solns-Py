class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe={}
        
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i]=True
            return safe[i]

        res=[]
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
        

        