class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # nums.sort()
        # l=0
        # total=0
        # r=0
        # max_ct=1
        # while r < len(nums):
        #     total+=nums[r]

        #     while nums[r]*(r-l+1)-total>numOperations*k:
        #         total-=nums[l]
        #         l+=1

        #     max_ct=max(max_ct,r-l+1)
        #     r+=1
        # return max_ct
            
        # # for i in range(len(nums)):
        # #     if nums[i]-nums[i-1]<=k or nums[i]-nums[i-1]>=-k:
        # #         ct+=1
        # #         max_ct=max(ct,max_ct)
        # #     else:
        # #         ct=0
        # # return ct
        max_num = max(nums) 
        size = max_num + k + 2 
        freq = [0] * size 
        for num in nums: 
            freq[num] += 1 
        pre = [0] * size 
        pre[0] = freq[0] 
        for i in range(1, size): 
            pre[i] = pre[i - 1] + freq[i] 
        result = 0 
        for x in range(size):
            if freq[x] == 0 and numOperations == 0:
                continue 
            left = max(0, x - k) 
            right = min(size - 1, x + k) 
            totalInRange = pre[right] - (pre[left - 1] if left > 0 else 0) 
            canAdjust = totalInRange - freq[x] 
            total = freq[x] + min(numOperations, canAdjust) 
            result = max(result, int(total))
        return result
        
            
            
            
            
            
               