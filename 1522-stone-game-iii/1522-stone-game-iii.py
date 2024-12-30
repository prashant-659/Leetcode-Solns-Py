class Solution:
    def stoneGameIII(self, stoneVal: List[int]) -> str:
        n=len(stoneVal)
        dp={}
        
        def dfs(i):
            if i==n:
                return 0
            if i in dp:
                return dp[i]
            res=float("-inf")
            for j in range(i,min(i+3, n)):
                res=max(res,sum(stoneVal[i:j+1]) - dfs(j+1))
            dp[i]=res
            return res

      
        return "Alice" if dfs(0)>0 else ("Bob" if dfs(0)<0 else "Tie")
        
        
        
        
        
        
        
        
        
        