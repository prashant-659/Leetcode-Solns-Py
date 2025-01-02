class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        l=len(nums)

        mp=defaultdict(lambda: float("inf"))
        for i in range(l):
            mp[i]=nums[i]

        ans=0
        baseSum=0

        i=0
        while True:
            if baseSum>=n:
                return ans
            
            elif mp[i]>baseSum+1:
                ans+=1
                baseSum+=baseSum+1
            else:
                baseSum+=mp[i]
                i+=1
