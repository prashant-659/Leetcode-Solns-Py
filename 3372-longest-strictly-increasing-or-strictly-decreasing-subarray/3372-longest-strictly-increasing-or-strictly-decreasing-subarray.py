class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def inc():
            size_=1
            max_size=float("-inf")

            for i in range(1,len(nums)):
                if nums[i]>nums[i-1]:
                    size_+=1
                else:
                    max_size=max(size_, max_size)
                    size_=1
            max_size = max(size_, max_size)
            return max_size
        
        def dec():
            size_=1
            max_size=float("-inf")

            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    size_+=1
                else:
                    max_size=max(size_, max_size)
                    size_=1
            max_size = max(size_, max_size)
            return max_size
        return max(inc(), dec())
        
        