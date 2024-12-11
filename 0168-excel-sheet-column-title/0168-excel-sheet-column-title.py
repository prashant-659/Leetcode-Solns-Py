class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        res=[]
        while n:
            n-=1
            cur=n%26
            n=int(n/26)

            res.append(chr(cur+ord('A')))
        return ''.join(res[::-1])

