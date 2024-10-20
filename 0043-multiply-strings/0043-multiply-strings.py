class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
        "8":8,"9":9,"0":0}
        l1=0
        l2=0
        s=1
        for i,j in enumerate(num1[::-1]): #conversion of string to numbers
            l1+=(d[j]*(10**i)) #345=5*1+4*10+3*100
        for i, j in enumerate(num2[::-1]):
            l2+=(d[j]*(10**i))
        s=l1*l2
        return str(s)