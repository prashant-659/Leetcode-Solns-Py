class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        l=0
        cnt=1
        dp=[cnt]
        mod=10**9+7
        minq, maxq=deque(),deque()
        for r in range(len(nums)):
            while minq and nums[r]<nums[minq[-1]]:
                minq.pop()
            while maxq and nums[r]>nums[maxq[-1]]:
                maxq.pop()
            minq.append(r)
            maxq.append(r)

            while nums[maxq[0]]-nums[minq[0]]>k:
                cnt-=dp[l]
                l+=1
                if l>minq[0]:
                    minq.popleft()
                if l>maxq[0]:
                    maxq.popleft()
            dp.append(cnt)
            cnt*=2
            cnt%=mod
            
        return dp[-1]%mod
                
