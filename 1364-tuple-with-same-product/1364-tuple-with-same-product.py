class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp=defaultdict(int) #"n1*n2->count"
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i==j:
                    continue
                prod=nums[i]*nums[j]
                mp[prod]+=1

        # pairnct= lets say $6=1+2+3
        # 10=1+2+3+4
        res=0
        for cnt in mp.values():
            pairs=cnt*((cnt-1))//2 #formula based
            res+=8*pairs
        return res
