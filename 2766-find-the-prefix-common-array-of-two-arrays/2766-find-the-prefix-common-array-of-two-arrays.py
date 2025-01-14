class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mp=defaultdict(int)
        op=[]
        for i in range(len(B)):
            ct=0
            mp[A[i]]=1+mp.get(A[i], 0)
            mp[B[i]]=1+mp.get(B[i], 0)
            for x in mp:
                if mp[x]==2:
                    ct+=1
            op.append(ct)

            
        return op


            
