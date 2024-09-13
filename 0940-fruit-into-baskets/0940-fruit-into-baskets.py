class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        # if len(fruits)==1:
        #     return 1 
        mp=defaultdict()
        i,j=0,0
        res=0
        while j<len(fruits):
            mp[fruits[j]]=1+mp.get(fruits[j],0) 
            while len(mp)>2:
                mp[fruits[i]]-=1
                if mp[fruits[i]]==0:
                    del mp[fruits[i]]
                i+=1
                
            if len(mp)<=2:
                res=max(res,j-i+1)
            j+=1
        return res

                    

