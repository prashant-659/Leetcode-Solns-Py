class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # count = 0
        # sums = 0
        # d = dict()
        # d[0] = 1
        
        # # for i in range(len(nums)):
        # #     sums += nums[i]
        # #     count += d.get(sums-k,0)
        # #     d[sums] = d.get(sums,0) + 1
        
        # # return(count)

        # count={}
        # csum=0
        # res=0
        # for n in nums:
        #     csum+=n
        #     if csum==k:
        #         res+=1
        #     if csum-k in count:
        #         res+=count[csum-k]
            
        #     if csum in count:
        #         count[csum]+=1
        #     else:
        #         count[csum]=1
        # return res

        prefix={0:1}
        res=curSum=0
        for i in range(len(nums)):
            curSum+=nums[i]
            diff=curSum-k
            res+=prefix.get(diff,0)
            prefix[curSum]=1+prefix.get(curSum,0)
        return res
