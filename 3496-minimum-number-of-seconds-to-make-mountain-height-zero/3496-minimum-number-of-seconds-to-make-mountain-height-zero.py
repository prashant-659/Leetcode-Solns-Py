class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workerTimes.sort(reverse = True)
        l = 0
        r = 10**18
        def find(k):
            l = 0
            r = k 
            ans  = 0
            while l<=r:
                mid = (l+r)//2
                if mid*(mid + 1) <= 2*k:
                    ans = mid 
                    l = mid + 1
                else : 
                    r = mid  - 1
            return ans
        def good(mid):
            rem = mountainHeight
            for t in workerTimes:
                # x*(x+1) <= mid/t
                rem-=find(mid//t)
            return rem<=0
        ans = r
        while l<=r:
            mid = (l+r)//2
            if good(mid):
                ans = mid 
                r = mid -1
            else:
                l = mid + 1
        return ans