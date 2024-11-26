class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming=[0]*n
        for u, v in edges:
            incoming[v]+=1

        champions=[]
        for i, incoming_cnt in enumerate(incoming):
                if not incoming_cnt:     
                    champions.append(i)
        
        
        if len(champions)>1:
            return -1
        return champions[0]
        # if not edges:
        #     return 0 if n==1 else -1
        # s=set()

        # for e in edges:
        #     s.add(e[1])
        # if len(s)<n-1:
        #     return -1
        # for i in range(n):
        #     if i not in s:
        #         return i
            



                
