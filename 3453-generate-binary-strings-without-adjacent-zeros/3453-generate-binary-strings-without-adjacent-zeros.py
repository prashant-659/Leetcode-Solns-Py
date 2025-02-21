class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        
        def backtrack(i,res):
            if i==n:
                ans.append("".join(res))
                return 
            if i==0 or res[-1]=="1":
                res.append("0")
                backtrack(i+1, res)
                res.pop()
            res.append("1")
            backtrack(i+1, res)
            res.pop()
        backtrack(0, [])
        return ans