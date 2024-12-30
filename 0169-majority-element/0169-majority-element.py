class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)
        max_ct=0
        res=0
        for i in range(len(nums)):
            count[nums[i]]+=1
            if max_ct<count[nums[i]]:
                res=nums[i]
                max_ct=count[nums[i]]
        return res
