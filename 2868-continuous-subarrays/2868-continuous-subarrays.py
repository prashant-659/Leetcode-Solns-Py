class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxQ=deque()
        minQ=deque()
        ans=0
        n=len(nums)
        l,r=0,0

        while r<n:
            while maxQ and nums[r]>maxQ[-1]:
                maxQ.pop()
            while minQ and nums[r]<minQ[-1]:
                minQ.pop()
            maxQ.append(nums[r])
            minQ.append(nums[r])

            while maxQ and minQ and maxQ[0]-minQ[0]>2:
                if maxQ[0]==nums[l]:
                    maxQ.popleft()

                if minQ[0]==nums[l]:
                    minQ.popleft()
                l+=1
            ans+=r-l+1
            r+=1
        return ans

        