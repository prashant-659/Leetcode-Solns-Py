class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp=defaultdict(int) #"n1*n2->count"
        pair_cnt=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i==j:
                    continue
                prod=nums[i]*nums[j]
                pair_cnt[prod] +=mp[prod]
                mp[prod]+=1
        res=0
        for val in pair_cnt.values():
            res+=8*val
        return res

