class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # safe={}
        
        # def dfs(i):
        #     if i in safe:
        #         return safe[i]
        #     safe[i]=False
        #     for nei in graph[i]:
        #         if not dfs(nei):
        #             return safe[i]
        #     safe[i]=True
        #     return safe[i]

        # res=[]
        # for i in range(len(graph)):
        #     if dfs(i):
        #         res.append(i)
        # return res
        visited=[0]*len(graph)
        currPath=[0]*len(graph)

        def dfs(node):
            visited[node]=1
            currPath[node]=1
            for nei in graph[node]:
                if not visited[nei]:
                    ans=dfs(nei)
                    if ans==True:
                        return True
                else:
                    if currPath[nei]==1:
                        return True
            currPath[node]=0
            return False
        ans=[]
        for i in range(len(graph)):
            if not visited[i]:
                dfs(i)
        for i in range(len(currPath)):
            if currPath[i]==0:
                ans.append(i)
        return ans
            


        