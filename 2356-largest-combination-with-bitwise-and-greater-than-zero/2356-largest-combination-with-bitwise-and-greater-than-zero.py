class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
    #     # count=[0]*32
    #     for n in candidates:
    #         i=0
    #         while n>0:
    #             count[i]+=1&n
    #             i+=1
    #             n=n>>1 #right shift
    #     return max(count)
        res=0
        for i in range(32):
            
            cnt=0
            for n in candidates:
                cnt+=1 if (1<<i) & n else 0
            res=max(res,cnt)
                    


        return res
               
