class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        res=0
        for num in range(low, high+1):
            num=str(num)
            numlen=len(num)
            if numlen%2:
                continue
            first=num[:numlen//2]
            sec=num[numlen//2:]
            j=0
            add1=add2=0
            while j<numlen//2:
                add1+=int(first[j])
                add2+=int(sec[j])
                j+=1
            if add1==add2:
                res+=1
        return res
            
