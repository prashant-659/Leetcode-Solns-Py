class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l_ct=r_ct=max_len=0

        
        i=0
        while i<len(s):
            if s[i]=="(":
                l_ct+=1
            else:
                r_ct+=1
            if l_ct==r_ct:
                max_len=max(max_len, l_ct+r_ct)
            elif r_ct>l_ct:
                l_ct=r_ct=0
            i+=1

        l_ct=r_ct=0
        i=len(s)-1
        while i>=0:
            if s[i]=="(":
                l_ct+=1
            else:
                r_ct+=1
            
            if l_ct==r_ct:
                max_len=max(max_len, l_ct+r_ct)
            elif r_ct<l_ct:
                l_ct=r_ct=0
            i-=1
        return max_len
