class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # while part in s:
        #     s=s.replace(part,"",1)
        # return s
        lps=[0]*len(part)
        length=0
        i=1
        while i<len(part):
            if part[i]==part[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
        stack=[("",0)]
        for ch in s:
            k=stack[-1][1]
            while k and part[k]!=ch:
                k=lps[k-1]
            if part[k]==ch:
                k+=1
            stack.append((ch,k))
            if k==len(part):
                for _ in range(len(part)):
                    stack.pop()
        return "".join(x for x,_ in stack)
            