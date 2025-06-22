class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            cur=""
            while j<len(s) and j<i+k:
                cur+=s[j]
                j+=1
            i=j
            ans.append(cur)
        
        if len(ans[-1])<k:
            for i in range(k-len(ans[-1])):
                ans[-1]+=fill
        return ans

