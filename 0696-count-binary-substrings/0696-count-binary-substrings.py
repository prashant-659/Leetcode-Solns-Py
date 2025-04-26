class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur, prev, ans=1,0,0

        for i in range(1, len(s)):
            if s[i]==s[i-1]: cur+=1
            else:
                ans+=min(cur, prev)
                prev, cur=cur,1
        return ans+min(cur, prev)