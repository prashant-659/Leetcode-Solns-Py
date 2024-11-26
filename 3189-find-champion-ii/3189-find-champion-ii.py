class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # graph=defaultdict(list)
        # for u, v in graph:
        #     graph[u].append(v)
        # allin=graph.keys()
        # val=-1
        # multiple=set()
        # for j in allin:
        #     for i in graph.values():
        #         if j in i:
        #             continue
        #         else:
        #             val=j
        #             multiple.add(val)
        
        
        # return val
        if not edges:
            return 0 if n==1 else -1
        s=set()

        for e in edges:
            s.add(e[1])
        if len(s)<n-1:
            return -1
        for i in range(n):
            if i not in s:
                return i
            



                
