class Solution:
    def isBalanced(self, num: str) -> bool:
        evensum=0
        oddsum=0
        for i,s in enumerate(num):
            if i%2==0: #evensum
                evensum+=int(s)
            else:
                oddsum+=int(s)
        return evensum==oddsum
            