# class Solution:
#     def isAdditiveNumber(self, num: str) -> bool:
#         if len(num)<3:
#             return False

#         def helper(f, s , r):
#             if len(r)<max(len(f), len(s)):
#                 return False
#             if (f[0]=="0" and len(f)>1) or (s[0]=="0" and len(s)>1) :
#                 return False

#             f=int(first)
#             s=int(s)
#             res=str(f+s)
#             len_res=len(res)

#             if len(r)<len_res:
#                 return False
            
#             if res==r[0:len_res]:
#                 if len(r)==len_res:
#                     return True
                
#                 f=s
#                 s=res
#                 r=r[len_res:]
#                 return helper(str(f), str(s), r)
            
#             return False
            



            


        # idx1=0
        # for idx2 in range(idx1+1, len(num)):
        #     for idx3 in range(idx2+1, len(num)):
        #        first=num[idx1:idx2]
        #        second=num[idx2:idx3]
        #        remaining=num[idx3:]
        #        if helper(first, second, remaining): 
        #             return True

        # return False
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def helper(f, s, r):
            if len(r) < max(len(f), len(s)):
                return False
            
            if (f[0] == "0" and len(f) > 1) or (s[0] == "0" and len(s) > 1):
                return False
            
            f = int(f)
            s = int(s)
            res = str(f + s)
            len_res = len(res)
            
            if len(r) < len_res:
                return False
            
            if res == r[:len_res]:
                if len(r) == len_res:
                    return True
                
                f = s  
                s = int(res)  
                r = r[len_res:]
                return helper(str(f), str(s), r)
            
            return False

        for idx2 in range(1, len(num)):
            for idx3 in range(idx2 + 1, len(num) + 1):
                first = num[:idx2]
                second = num[idx2:idx3]
                remaining = num[idx3:]
                
                if helper(first, second, remaining):
                    return True

        return False
