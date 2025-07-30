class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # max_val=res=curr=0
        # for i in range(len(nums)):
        #     if max_val<nums[i]:
        #         max_val=nums[i]
        #         res=curr=0
        #     if max_val==nums[i]:
        #         curr+=1
        #         res=max(curr,res)
        #     else:
        #         curr=0
        # return res

        #find max amd increse size if they are consecutive
        # target=max(nums)
        # size=0
        # res=0
        # for n in nums:
        #     if n==target:
        #         size+=1
        #     else:
        #         size=0
        #     res=max(res,size)
        # return res

        #NeetCode IO
        #1 If n< curr_max, n & curr_max < curr_max
        #1 If n== curr_max, n & curr_max = curr_max
        #1 If n> curr_max, n & curr_max < curr_max
        size, res=0,0
        cur_max=0
        for n in nums:
            if n>cur_max:
                cur_max=n
                size=1
                res=0
            elif n==cur_max:
                size+=1
            else:
                size=0
            res=max(res,size)
        return res