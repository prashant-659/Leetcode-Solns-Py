class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # n = len(nums) 
        # distinct_elements = len(set(nums)) 
        # count = 0 
        # left = 0 
        # right = 0 
        # counter = Counter() 

        # while right < n: 
        #     counter[nums[right]] += 1 
        #     while len(counter) == distinct_elements: 
        #         counter[nums[left]] -= 1 
        #         if counter[nums[left]] == 0: 
        #             del counter[nums[left]] 
        #         left += 1 
        #         count += n - right 
        #     right += 1 

        # return count     
        l=r=0
        ans=0
        k=len(set(nums))
        n=len(nums)
        new=Counter()
        for r in range(len(nums)):  
            new[nums[r]]+=1
            while len(new)==k:
                new[nums[l]]-=1
                if new[nums[l]]==0:
                    del new[nums[l]]
                l+=1
                ans+=n-r    
        return ans     