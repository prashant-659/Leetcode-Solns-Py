class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        total=sum(nums)

        subSets=[0]*k
        nums.sort(reverse=True)
        reqSum=total//k
        def backtrack(i):
            if i==len(nums):
                return True
            for j in range(k):
                if subSets[j]+nums[i]<=reqSum:
                    subSets[j]+=nums[i]
                    if backtrack(i+1):
                        return True
                    subSets[j]-=nums[i]

                    if subSets[j]==0:
                        break
            return False
        return backtrack(0)