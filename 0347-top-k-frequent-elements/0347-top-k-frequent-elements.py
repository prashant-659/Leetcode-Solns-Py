class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count={}
        freq=[[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

            
                
                
            
        # for key,val in enumerate(nums):
        #     if key in mapped:
        #         count+=1
        #     mapped[val]=
            
        
        ct=Counter(nums)
        ct.sort(key=lambda x: x.values(),reverse=True)
        res=list(ct.keys())
        res=[]
        return res[0:k]


