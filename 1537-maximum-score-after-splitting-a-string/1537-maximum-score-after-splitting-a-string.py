class Solution:
    def maxScore(self, s: str) -> int:
        # prefix=[0]*(len(s))
        # prefix[0]=int(s[0])
        # for i in range(1,len(s)):
        #     prefix[len(s)-i-2]=int(s[i])+prefix[len(s)-i-1]
        
        # prefix2=[0]*(len(s))
        # prefix2[0]=1 if s[0]=="0" else 0
    
        # for i in range(1,len(s)):
        #     if s[i]=="0":
        #         prefix2[i]=1+prefix2[i-1]

        # ct=0
        # print(prefix2, prefix)
        # max_ct=-1
        
        # for i in range(len(s)):
        #     ct=prefix2[i]+prefix[len(s)-i-1]
        #     max_ct=max(ct, max_ct)
        # return max_ct
        
        zeroes=0
        ones=s.count("1")
        res=0

        for i in range(len(s)-1):
            if s[i]=="0":
                zeroes+=1
            else:
                ones-=1
            res=max(res, ones+zeroes)
        
        
        
        return res

