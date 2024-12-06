# class Solution:
#     def maxSubarrays(self, nums: List[int]) -> int:
#         min_and = reduce(and_, nums)
        
#         if min_and > 0 : return 1
        
#         count, mask = 0, 2**32-1

#         for n in nums:
#             mask &= n
#             if mask == 0:
#                 count += 1
#                 mask = 2**32-1

#         return count

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        score, ans = -1, 1
        for num in nums:
            score &= num
            if score == 0:
                score = -1
                ans += 1
        return 1 if ans == 1 else ans - 1