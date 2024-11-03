class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visit=set()
        res=[s]
        def dfs(s,a,b):
            #base case 
            if s in visit:
                return
            visit.add(s)
            ans=""
            for i in range(len(s)):
                if i%2!=0:
                    ans+=str((int(s[i])+a)%10)
                else:
                    ans+=s[i]
            if ans<res[0]:
                res[0]=ans
            dfs(ans,a,b)
            s=s[b:]+s[:b]
            if s<res[0]:
                res[0]=s
            dfs(s,a,b)
            return
        dfs(s,a,b)
        return res[0]



