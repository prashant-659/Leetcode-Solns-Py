class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        def isPalindrome(s,l, r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        l,r=0, len(s)-1
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1

            else: 
                return isPalindrome(s,l,r-1) or isPalindrome(s, l+1, r)
        return True
                