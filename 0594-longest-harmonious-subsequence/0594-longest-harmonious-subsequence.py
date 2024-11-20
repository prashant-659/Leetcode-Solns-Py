# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         # mapped=defaultdict(int)
#         # 
#         # for i in nums:

#         nums.sort()
#         l,r=0,0
#         res=0
#         while r<len(nums):
#             while nums[r]-nums[l]>1:
#                 l+=1
#             if nums[r]-nums[l]==1:
#                 res=max(res,l-r+1)
#             r+=1
#         return res

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i,j,n,ans=0,0,len(nums),0
        while j<n: 
            while nums[j]-nums[i]>1: 
                i+=1
            if nums[j]-nums[i]==1: ans=max(ans,j-i+1)
            j+=1
        return ans
            


        