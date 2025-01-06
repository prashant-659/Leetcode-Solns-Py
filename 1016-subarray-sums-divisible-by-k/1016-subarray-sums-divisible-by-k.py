class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # l=0
        # prefix=[0]*len(nums)
        # prefix[0]=nums[0]
        # for i in range(1, len(nums)):
        #     prefix[i]=nums[i]+prefix[i-1]
        res=0
        prefix_sum=0
        prefix_cnt=defaultdict(int)
        prefix_cnt[0]=1

        for n in nums:
            prefix_sum+=n
            remain=prefix_sum%k

            res+=prefix_cnt[remain]
            prefix_cnt[remain]+=1
        return res