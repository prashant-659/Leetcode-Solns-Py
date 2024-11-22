class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        c=0
        mp=[[x,0] for x in range(lo,hi+1)]
        for i in range(lo,hi+1):
            steps=0
            while i>1:
                i=i//2 if i%2==0 else 3*i+1
                steps+=1
            mp[c][1]=steps
            c+=1

        mp.sort(key=lambda x : x[1])
        return mp[k-1][0]
            
            



