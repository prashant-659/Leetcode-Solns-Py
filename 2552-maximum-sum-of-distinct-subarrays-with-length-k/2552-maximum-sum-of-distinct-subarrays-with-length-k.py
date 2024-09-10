class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #mp=Counter(nums)
        # mp={nums[j]:0 for j in range(len(nums))}
        # for i in range(len(nums)):
        #     if i not in mp:
        #         mp[i]=nums[i]
        #     else:
        #         mp[i]=1+mp[i]
        i = 0
        j = 0
        curr_sum = 0
        ans = 0
        freq_map = defaultdict(int)
        
        while j < len(nums):
            curr_sum += nums[j]
            freq_map[nums[j]] += 1
            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if len(freq_map) == k:
                    ans = max(ans, curr_sum)
                    print(ans, end=" ")
                
                if nums[i] in freq_map:
                    freq_map[nums[i]] -= 1
                    if freq_map[nums[i]] == 0:
                        del freq_map[nums[i]]
                
                curr_sum -= nums[i]
                i += 1
                j += 1
        
        return ans



 
               
            
        