# class Solution:
#     def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
#         # graph=defaultdict(list)
#         # reverse=defaultdict(list)

#         # for a, b in invocations:
#         #     graph[a].append(a)
#         #     reverse[b].append(a)

#         # remove=set()

#         # for m in range(n):
#         #     if len(reverse[m])==0:
#         #         remove.add(m)
        
#         # sus = [m for m in range(n) if m not in remove]
#         # sus_m=set(sus[:k])
#         # invoke=set()
#         # for sm in sus_m:
#         #     if sm in graph:
#         #         invoke.update(graph[sm])


#         # rem=[m for m in range(n) if m not in invoke]
#         # return rem

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        def dfs(node):
            if node not in suspicious:
                suspicious.add(node)
            
                for child in graph[node]:
                    dfs(child)
            
        graph = [[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
            
        suspicious = set()
        dfs(k)
        
        connected_compontent = True     
        for u,v in invocations:
            if v in suspicious and u not in suspicious:
                connected_compontent = False
        
        ans = set(range(n))
        return ans-suspicious if connected_compontent else ans