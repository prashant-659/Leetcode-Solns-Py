class Solution:
    def punishmentNumber(self, n: int) -> int:
        # res=[]
        # def backtrack(i):
        #     nonlocal res
        #     if i>n:   
        #         return
        #     backtrack(i+1)
        #     if i%9==0 or i%9==1:
        #         res.append(i*i)
            
        # backtrack(1)
        # ans=0
        # for num in res:
        #     nn=str(num)
        #     for i in range(1, len(nn)):  
        #         fp = int(nn[:i])   
        #         sp = int(nn[i:])  # Take s
        #         new = fp + sp  
        #         if new==n:
        #             ans+=num
        # return ans

        
        def can_form(n, square):
            s = str(square)

            def backtrack(idx, cur_sum):
                if idx == len(s):
                    return cur_sum == n  
                
                for i in range(idx + 1, len(s) + 1):  
                    part = int(s[idx:i])  
                    if backtrack(i, cur_sum + part):  
                        return True
                return False

            return backtrack(0, 0)

        ans = 0
        for i in range(1, n + 1):  
            square = i * i
            if can_form(i, square):  
                ans += square

        return ans

