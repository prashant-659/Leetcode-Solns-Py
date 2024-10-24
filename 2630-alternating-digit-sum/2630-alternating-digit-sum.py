class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res=0
        ptr=0
        l=[]
        while n>0:
            temp=n%10
            l.append(temp)
            n=n//10
        for i in range(len(l)-1,-1,-1):
            if ptr%2==0:
                res+=l[i]
            else:
                res+=(-1*l[i])
            ptr+=1
        return res

