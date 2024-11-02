class Solution:
    def isCircularSentence(self, s: str) -> bool:
        if not s:
            return False
        f1=s[0]
        l1=s[-1]
        flag=False
        if f1==l1:
            flag=True

        
        for i in range(1,len(s)):
            if s[i]==" ":
                l=s[i-1]
                f=s[i+1]
                if l!=f :
                    return False
            if flag==False:
                return False
        return True


            
            
