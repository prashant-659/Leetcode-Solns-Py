class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        pairs=0
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j]+nums[i]>=lower and nums[j]+nums[i]<=upper:
        #             pairs+=1
        # return pairs

        def binary_search(l,r,target):
            while l<=r:
                m=(l+r)//2

                if nums[m]>=target:
                    r=m-1
                else:
                    l=m+1
            return l

        r=len(nums)-1
        for i in range(len(nums)):
            low=lower-nums[i]
            up=upper-nums[i]
            pairs+=(binary_search(i+1,r, up+1)-
                   binary_search(i+1, r,low) )
        return pairs
