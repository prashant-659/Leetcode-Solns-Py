class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # table = [(a, i) for i, a in enumerate(nums)]
        # table.sort()

        # imin = float("inf")
        # res = 0
        # for a, i in table:
        #     res = max(res, i - imin)
        #     imin = min(imin, i)

        # return res

        stack=[]
        for i in range(len(nums)):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)

        res=0
        for j in range(len(nums)-1,-1,-1):
            while stack and nums[j]>=nums[stack[-1]]:
                res=max(res,j-stack[-1])
                stack.pop()
        return res     