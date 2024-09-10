class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if abs(target)>total or ((total+target)%2!=0):
            return 0
        s1_sum=(target+total)//2
        
        def countSubsets(targetSum):
            t=[[0]*(targetSum+1) for _ in range(len(nums)+1)]
            for i in range(len(nums)+1):
                t[i][0]=1
            
            for i in range(1,len(nums)+1):
                for j in range(targetSum+1):
                    if nums[i-1]<=j:
                        t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[len(nums)][targetSum]
        return countSubsets(s1_sum)