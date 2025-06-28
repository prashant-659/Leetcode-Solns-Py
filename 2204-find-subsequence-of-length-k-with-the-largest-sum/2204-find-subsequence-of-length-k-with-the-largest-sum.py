class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sec=sorted(nums, reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sec[i])
        setans=Counter(ans)
        res=[]
        for i in range(len(nums)):
            if nums[i] in setans:
                res.append(nums[i])
                setans[nums[i]]-=1
                if setans[nums[i]]==0:
                    del setans[nums[i]]
        return res
