# class Solution:
#     def myAtoi(self, s: str) -> int:
#         # res=""
#         # isnegative=False
#         # for i, c in enumerate(s):
#         #     if c==" ":
#         #         continue
#         #     if c=="-" and len(res)==0:
#         #         isnegative=True
#         #     d=ord(c)>=ord("0") and ord(c)<=ord("9")
            
#         #     if ord(c)>=ord("0") and ord(c)<=ord("9"):
#         #         res+=c
#         # if isnegative and len(res)>0  :
#         #     res=int(res)
#         #     return res*-1
#         # return int(res) if len(res)>0 else 0
#         res=""
#         last_nonDigit=-1
#         last_pm=0
#         count=0
#         flag=False
#         for i in range(len(s)-1,-1):
#             c=s[i]
#             if (ord(c)>=ord("a") and ord(c)<=ord("z")) or (ord(c)>=ord("A") and ord(c)<=ord("Z")):
#                 last_nonDigit=len(s)+i
#             if c=="+" or c=="-" or c==".":
#                 last_pm=len(s)+i
#         if last_pm<last_nonDigit:
#             flag=True
#         for i in range(last_nonDigit):
#             c=s[i]
#             if c==" ":
#                 continue
#             if flag and c=="-":
#                 count=1
#                 flag=False
#             if ord(c)>=ord("0") and ord(c)<=ord("9"):
#                 res+=c
#         if count==1 and len(res)>0  :
class Solution(object):
    def myAtoi(self, s):
        num = '0123456789'
        res = ''
        for x in s:
            if x == ' ' and len(res) == 0:
                continue
            if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
                res += x
            elif x in num:
                res += x
            else:
                break
        if res == '' or res in '-+':
            return 0
        else:
# to avoid int casting simply run a loop and use ord(char) - ord('0')
            if int(res) < -(2**31):
                return -(2**31)
            elif int(res) > (2**31 - 1):
                return (2**31 - 1)
            else:
                return int(res)
            
            
        

        
            



