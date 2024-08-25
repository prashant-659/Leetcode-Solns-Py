class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start,end=0,len(nums)-1

        # while start!=end:
        #     sum=nums[start]+nums[end]
        #     if sum>target:
        #         end-=1
        #     elif sum<target:
        #         start+=1
        #     else:
        #         return[start+1,end+1]






        start,end=0,len(nums)-1
        while start<end:
            sum_t=nums[start]+nums[end]

            if sum_t>target:
                end-=1
            elif sum_t<target:
                start+=1
            else:
                return [start+1,end+1]








        
