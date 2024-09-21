class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        # for i in range(n+1):
        #     if n==1 or n//10==1:
        def dfs(cur):
            if cur>n:
                return
            
            res.append(cur)
            cur*=10
            for i in range(10):
                dfs(cur+i)

        for i in range(1,10):
            dfs(i)
        return res
