class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        i,j=0,0
        while i<len(word1) and j<len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
        if i<len(word1):
            ans.extend(word1[i:])
        if j<len(word2):
            ans.extend(word2[j:])
        return "".join(ans)