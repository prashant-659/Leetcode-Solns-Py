class Solution:
    def finalString(self, s: str) -> str:
        #count_i=
        res=""
        for i in range(len(s)):
            if s[i]!="i":
                res+=s[i]
            else:
                res=res[::-1]


        return res


