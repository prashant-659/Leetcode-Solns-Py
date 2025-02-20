class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s=list(s)
        new=s.copy()
        for i in range(len(s)):
            s[i]=new[(i+k)%len(s)]
        return "".join(s)
        