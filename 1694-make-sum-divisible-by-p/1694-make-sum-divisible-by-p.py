class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # total=sum(nums)
        # remain=total%p
        # if remain==0:
        #     return 0
        # res=len(nums)
        # curr_sum=0
        # remain_to_idx={
        #     0:-1
        # }
        # for i, n in enumerate(nums):
        #     curr_sum=(curr_sum+n)%p
        #     prefix=(curr_sum-remain+p)%p
        #     if prefix in remain_to_idx:
        #         length=i-remain_to_idx[prefix]
        #         res=min(res,length)
        #     remain_to_idx[curr_sum]=i
        
        # return -1 if res==len(nums) else res
        mp=defaultdict(int)
        mp={0:-1}
        prefix_sum=0
        res=len(nums)
        total_sum=0

        for i in range(len(nums)):
            total_sum=(total_sum+nums[i])%p

        if total_sum==0:
            return 0
        
        for i in range(len(nums)):
            prefix_sum=(prefix_sum+nums[i])%p
            check=(prefix_sum-total_sum+p)%p
            if check in mp:
                res=min(res,i-mp[check])
            
            mp[prefix_sum]=i


        if res==len(nums):
            return -1
        return res
        