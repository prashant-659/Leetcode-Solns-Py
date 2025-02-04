class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballcolors={}
        col_ct={}
        colorset=set()
        ans=[]
        for x,y in queries:
            if x in ballcolors:
                old_col=ballcolors[x]
                col_ct[old_col]-=1
                if col_ct[old_col]==0:
                    colorset.remove(old_col)
            ballcolors[x]=y
            if y in col_ct:
                col_ct[y]+=1
            else:
                col_ct[y]=1
            colorset.add(y)

            ans.append(len(colorset))
        return ans
           

