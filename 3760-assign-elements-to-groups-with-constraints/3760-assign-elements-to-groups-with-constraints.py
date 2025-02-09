class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        # ele=[(i,elements[i]) for i in range(len(elements))]
        # ele.sort()
        # assign=[-1]*len(groups)
        # check={}
        # while ele:
        #     j,e=heapq.heappop(ele)
        #     for i in range(len(groups)):
        #         if groups[i]%e==0:
        #             if assign[i]==-1:
        #                 assign[i]=j
                                    
        # return assign
        mp={}
        max_num=max(groups)
        for i, el in enumerate(elements):
            n=el
            if el not in mp:
                while el<=max_num:
                    if el not in mp:
                        mp[el]=i
                    el+=n
        res=[]
        for g in groups:
            if g not in mp:
                res.append(-1)
            else:
                res.append(mp[g])
        return res
