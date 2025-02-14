class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=""
        arr=["a","b","c"]
        def backtrack(n,k, s):
            nonlocal res
            if len(s)==n:
                k-=1
                if k==0:
                    res=s
                    return 0
                return k
            
            for c in arr:
                if not s or s[-1]!=c:
                    k=backtrack(n, k, s+c)
                    if k==0:
                        return 0
            return k
        backtrack(n, k, "")
        return res 


