class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count=Counter(s1.split(" ") +s2.split(" "))
        
        
        # count=defaultdict(int)
        # for w in s1.split(" ") +s2.split(" "):
        #     count[w]+=1
        

        return [w for w, ct in count.items() if ct ==1]
        # res=[]
        # for w, cnt in count.items():
        #     if cnt==1:
        #         res.append(w)
        # return res
        
            