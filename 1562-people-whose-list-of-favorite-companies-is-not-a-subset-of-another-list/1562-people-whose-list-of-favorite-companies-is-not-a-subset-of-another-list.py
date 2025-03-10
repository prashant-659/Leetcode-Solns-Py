class Solution:
    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        mp={i:set(v) for i, v in enumerate(A)}
        res=[]
        # for i in range(len(favoriteCompanies[0])):
        #     mp.add(favoriteCompanies[0][i])
        for i in range(len(A)):
            flag=True
            for j,com in enumerate(A):
                if i==j:
                    continue
                if not (mp[i]-mp[j]):
                    flag=False
                    break
            if flag:
                res.append(i)
        return res

                
        



            
