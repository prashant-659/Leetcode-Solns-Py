class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet=set(nums)
        
        N=len(nums[0])
        choices=["0","1"]
        def backtrack(cur):
            if len(cur)==N:
                cand= "".join(cur)
                if cand in numSet:
                    return False
                return cand
            for c in choices:
                cur.append(c)
                res=backtrack(cur)
                if res:
                    return res
                cur.pop()
        return backtrack([])