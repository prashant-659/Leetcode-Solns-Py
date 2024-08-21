class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        # for word in words:
        #     if word==word[::-1]:
        #         return word
        # return ""

        for w in words:
            if self.isPalindromeornot(w):
                return w
        return ""

    def isPalindromeornot(self,s):
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
