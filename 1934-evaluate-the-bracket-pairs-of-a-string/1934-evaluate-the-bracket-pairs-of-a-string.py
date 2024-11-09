class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp={}
        for x, y in knowledge:
            if x not in mp:
                mp[x]=y
        t=s.split("(")
        ans=t[0]

        for i in range(1,len(t)):
            a,b=t[i].split(")")
            ans+=mp.get(a,"?")+b
        return ans
            
