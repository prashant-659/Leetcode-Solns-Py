class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def back(i, cur):
            if i==len(nums):
                return cur
            include=back(i+1, cur^nums[i])

            exclude=back(i+1, cur)
            return include + exclude
        
        return back(0,0)
            