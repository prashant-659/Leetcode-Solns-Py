class Solution:
    def maximumLength(self, s: str)-> int:
        groups=defaultdict(list)
        res=-1
        n=len(s)

        prev=None
        curCount=0

        for c in s + '.':
            if c!=prev:
                if prev!= None:
                    groups[prev].append(curCount)
                    groups[prev]=sorted(groups[prev], reverse=True)[:3]

                prev=c
                curCount=1
            else:
                curCount+=1

        for c in string.ascii_lowercase:
            if c not in groups:
                continue
            
            group_len=groups[c]

            no_of_groups=len(group_len)

            ans=group_len[0]-2

            if no_of_groups==2:
                x, y=group_len

                if y>=x-1:
                    ans=max(ans,x-1)
            elif no_of_groups==3:
                x,y,z=group_len

                if x==y==z:
                    ans=max(ans,x)
                
                elif y>=x-1:
                    ans=max(ans,x-1)
            if ans>0:
                res=max(ans,res)
        return res
                