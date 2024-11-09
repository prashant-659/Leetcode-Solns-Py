class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        diff = Counter()
        for x in nums:
            diff[x] += 0
            diff[x - k] += 1
            diff[x + k + 1] -= 1
        
        cur = 0
        res = 0
        for v in sorted(diff):
            cur += diff[v]
            res = max(res, cnt[v] + min(cur - cnt[v], numOperations))
        return res