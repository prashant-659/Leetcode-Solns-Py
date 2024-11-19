class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        i=0
        j=0
        res=0
        s={}
        maxi=0
        while j<len(nums):
            res+=nums[j]
            s[nums[j]]=s.get(nums[j],0)+1
            
            if j - i + 1 > k:
                res -= nums[i]
                s[nums[i]]-=1
                if s[nums[i]]==0:
                    del s[nums[i]]
                i += 1 

            if j-i+1==k:
                if len(s)>=m:
                    maxi=max(res,maxi)
            
            j+=1
        return maxi

                
# class Solution:
#     def maxSum(self, nums: List[int], m: int, k: int) -> int:
#         i = 0
#         res = 0
#         s = {}
#         maxi = 0

#         for j in range(len(nums)):
#             # Add nums[j] to the window
#             res += nums[j]
#             s[nums[j]] = s.get(nums[j], 0) + 1

#             # Shrink the window if its size exceeds k
#             if j - i + 1 > k:
#                 res -= nums[i]
#                 s[nums[i]] -= 1
#                 if s[nums[i]] == 0:  # Remove from map if count becomes 0
#                     del s[nums[i]]
#                 i += 1

#             # When the window size is exactly k, check the "almost unique" condition
#             if j - i + 1 == k:
#                 if len(s) >= m:  # At least `m` distinct elements
#                     maxi = max(maxi, res)

#         return maxi
