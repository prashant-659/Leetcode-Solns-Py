class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # c=Counter(nums)
        # print(c)
        # prefix=[0]*(len(nums))
        # prefix[0]=nums[0] if nums[0]==1 else 0
        # for i in range(1,len(nums)):
        #     if nums[i]==1:
        #         prefix[i]=prefix[i-1]+1
        #     else:
        #         prefix[i]=prefix[i-1]-1
        # print(prefix)
        # res=0
        # max_res=-1
        # for i in range(1,len(prefix)-1):
            
        #     if prefix[i]==prefix[i+1]:
        #         res+=2
        #         max_res=max(res, max_res)
        #     else:
        #         res=0
        
        # print(max_res)
        max_len=0
        mp={0:-1}
        zeros=0
        ones=0
        for i in range(len(nums)):
            cur=nums[i]
            if cur==0:
                zeros+=1
            else:
                ones+=1
            diff=zeros-ones
            if diff in mp:
                max_len=max(max_len, i-mp[diff])
            else:
                mp[diff]=i
        return max_len   