# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         n=len(nums)
#         if n<2:
#             return 0

         
#         mini=min(nums)
#         maxi=max(nums)

#         bucket_size=math.ceil((maxi-mini)/n-1)

#         minOfBucket=[math.inf] *(n-1)
#         maxOfBucket=[-1]*(n-1)

#         for i in range(n):
#             if nums[i]==maxi or nums[i]==mini:
#                 continue
#             bucket_idx=math.ceil((nums[i]-mini)/bucket_size)
#             minOfBucket[bucket_idx]=min(minOfBucket[bucket_idx],nums[i])

#             maxOfBucket[bucket_idx]=max(maxOfBucket[bucket_idx], nums[i])

#         for i in range(n-1):
#             if maxOfBucket[i]==1:
#                 continue
#             maxGap=max(minOfBucket[i]-mini, maxGap)
#             mini=maxBucket[i]
#         maxGap=Gap(maxGap, maxi-mini)
#         return maxGap
import math
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        mini = min(nums)
        maxi = max(nums)

        # If all elements are the same, the maximum gap is 0
        if mini == maxi:
            return 0

        # Calculate the bucket size
        bucket_size = max(1, (maxi - mini) // (n - 1))
        bucket_count = (maxi - mini) // bucket_size + 1

        # Initialize buckets
        minOfBucket = [math.inf] * bucket_count
        maxOfBucket = [-1] * bucket_count

        # Distribute numbers into buckets
        for num in nums:
            if num == mini or num == maxi:
                continue
            bucket_idx = (num - mini) // bucket_size
            minOfBucket[bucket_idx] = min(minOfBucket[bucket_idx], num)
            maxOfBucket[bucket_idx] = max(maxOfBucket[bucket_idx], num)

        # Calculate the maximum gap
        maxGap = 0
        previous_max = mini
        for i in range(bucket_count):
            if maxOfBucket[i] == -1:
                continue
            maxGap = max(maxGap, minOfBucket[i] - previous_max)
            previous_max = maxOfBucket[i]

        # Compare the last bucket's max with the overall max
        maxGap = max(maxGap, maxi - previous_max)

        return maxGap