class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels=set("aeiou")
        
        res=[]
        prefix=[0]*(len(words))
        prefix[0]=1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        
        for i in range(1,len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]
        count=0
        for l, r in queries:
            if l==0:
                count=prefix[r]
                res.append(count)
            else:
                count=prefix[r]-prefix[l-1]
                res.append(count)
        return res
        