class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size=0
        end=0
        res=[]
        lastIndex=defaultdict()

        for i in range(len(s)):
            lastIndex[s[i]]=i
        for i in range(len(s)):
            size+=1
            end=max(end,lastIndex[s[i]])
            if i==end:
                res.append(size)
                size=0
        return  res



