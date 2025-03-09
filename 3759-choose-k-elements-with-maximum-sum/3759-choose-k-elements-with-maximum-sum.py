class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums=[(nums1[i], nums2[i], i) for i in range(len(nums1))]
        nums.sort()
        q=[]
        sm=0
        ans=[0]*len(nums1)
        for i in range(len(nums1)):
            if i>0 and nums[i][0]==nums[i-1][0]:
                ans[nums[i][2]]=ans[nums[i-1][2]]
            else:
                ans[nums[i][2]]=(sm)
            heappush(q, nums[i][1])
            sm+=nums[i][1]
            if len(q)>k:
                sm-=heappop(q)
        return ans



        

