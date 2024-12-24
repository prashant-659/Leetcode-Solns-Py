class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        trips = pairs = 0
        count = Counter()
        for i,a in enumerate(nums):
            trips += pairs - count[a] * (i - count[a])
            pairs += i - count[a]
            count[a] += 1
        return trips