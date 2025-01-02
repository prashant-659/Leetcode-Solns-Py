class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        mp=defaultdict()
        vowels=set("aeiou")
        i=0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                mp[i]=1
            else:
                mp[i]=0
        

            i+=1
        res=[]
        prefix=[0]*(len(words))
        prefix[0]=1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        print(mp)
        for i in range(1,len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]
        count=0
        prefix=prefix
        print(prefix)
        for l, r in queries:
            if l==0:
                count=prefix[r]
                res.append(count)
            elif l==r:
                count=prefix[r]-prefix[l-1]
                res.append(count)
            else:
                count=prefix[r]-prefix[l-1]
                res.append(count)
        return res
        