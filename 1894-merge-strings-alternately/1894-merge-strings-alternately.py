class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i=0
        j=0
        res=[]
        while i<=len(w1)-1 and j<=len(w2)-1:
            res.append(w1[i])
            res.append(w2[j])
            i+=1
            j+=1
          
        if i<=len(w1)-1:
            res.append(w1[i:])
        elif j<=len(w2)-1:
            res.append(w2[j:])
        print(res)
        return "".join(res)