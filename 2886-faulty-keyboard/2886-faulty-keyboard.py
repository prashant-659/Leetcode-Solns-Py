class Solution:
    def finalString(self, s: str) -> str:
        #count_i=
        # res=""
        # for i in range(len(s)):
        #     if s[i]!="i":
        #         res+=s[i]
        #     else:
        #         res=res[::-1]


        # return res



        # counti=0
        # for i in range(len(s)):
        #     if s[i]=="i":
        #         counti+=1
        # res=""
        # sp=[]
        # sp=s.split("i")
        # places=0
        # for i in range(len(sp)):
        #     places+=1
        #     res+=sp[i][::-1]
        #     if i<=counti-1:
        #         break
                
        # for i in range(places,len(sp)):
        #     res+=sp[i]
            
        # return res

        stack = []
        for i in s:
            if i != 'i':
                stack.append(i)
            else:
                stack = stack[::-1]
        return ''.join(stack)
