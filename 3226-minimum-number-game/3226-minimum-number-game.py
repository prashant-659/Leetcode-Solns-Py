class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # nums.sort() #O(nlogn)
        # l=0
        # r=1
        # while r<len(nums):
        #     nums[l],nums[r]=nums[r],nums[l]
        #     l+=2
        #     r+=2
        # return nums

        heapify(nums)
        arr=[]
        while nums:
            a,b=heappop(nums),heappop(nums)
            arr.append(b)
            arr.append(a)
        return arr