class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(nums,k):
            l=0
            ans=0
            mp=defaultdict(int)
            for r in range(len(nums)):
                mp[nums[r]]+=1
                
                while len(mp)>k:
                    mp[nums[l]]-=1
                    if mp[nums[l]]==0:
                        del mp[nums[l]]
                    l+=1
                
                ans+=(r-l+1)
                
            return ans
        return count(nums, k)-count(nums,k-1)
