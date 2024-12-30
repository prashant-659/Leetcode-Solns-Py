class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count=defaultdict(int)
        # max_ct=0
        # res=0
        # for i in range(len(nums)):
        #     count[nums[i]]+=1
        #     if max_ct<count[nums[i]]:
        #         res=nums[i]
        #         max_ct=count[nums[i]]
        # return res

        # ct=0
        # res=0
        # for i in range(len(nums)):
        #     if ct==0:
        #         res=nums[i]
        #     ct+=(1 if nums[i]==res else -1)
        # return res

        while True:
            ele=random.choice(nums)
            if nums.count(ele)>len(nums)//2:
                return ele
