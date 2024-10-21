class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        # n=len(s)
        # l=0
        # ct=0
        # res=[]
        # for i in range(n):
        #     for r in range(1,len(s)):
        #         substr=s[l:r]
        #         ch=s[r]
        #         if ch in substr:
        #             ct+=1
        #         if ct>=k:
        #             res.append(substr)
        # return len(res)
                
        ans=0
        for i in range(len(s)):
            freq=[0]*26

            for j in range(i, len(s)):
                freq[ord(s[j])-ord('a')]+=1
                if freq[ord(s[j])-ord('a')]==k:
                    ans+=len(s)-j
                    break
        return ans