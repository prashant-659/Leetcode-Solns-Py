class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack=[0]*(len(nums)+1)

        top=0
        ans=0
        for n in nums:
            while stack[top]>n:
                top-=1
                ans+=1
            if stack[top]!=n:
                top+=1
                stack[top]=n
        return ans+top