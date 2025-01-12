class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hash=Counter(nums)
        res=0
        for x in hash:
            if (k>0 and x+k in hash) or (k==0 and hash[x]>1):
                res+=1 
                hash[x]-=1
                
        return res