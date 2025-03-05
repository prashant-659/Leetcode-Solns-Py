class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(comb):
            if len(comb)==len(nums):
                res.append(comb[:])
                return
            
            for n in nums:
                if n not in comb:
                    comb.append(n)
                    dfs(comb)
                    comb.pop()
            
        dfs([])
        return res
