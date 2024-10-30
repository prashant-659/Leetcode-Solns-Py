class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # nums1=list(set(nums)
        # max_ele=max(nums1)
        # rem=0
        # index=nums.index(max_ele)
        
        # max_ele=max(nums1)
        # for i in range(1,index+1):
        #     if nums1[i]<nums[i-1]:
        #         rem+=1
        # for i in range(len(nums)-2,index,-1):
        #     if nums[i]>nums[i+1]:
        #         rem+=1
        # return rem+1 if len(nums)>3 else rem
        n=len(nums)
        LIS_L=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    LIS_L[i]=max(LIS_L[i],1+LIS_L[j])
        LDS_R=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    LDS_R[i]=max(LDS_R[i],1+LDS_R[j])
        max_score=n
        for i in range(1,n-1):
            if min(LIS_L[i], LDS_R[i])>1:
                max_score=min(max_score,n-LIS_L[i]-LDS_R[i]+1)
        return max_score
