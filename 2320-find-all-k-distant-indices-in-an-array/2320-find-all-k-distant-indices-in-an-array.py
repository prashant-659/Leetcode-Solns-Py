class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        keyPos = [i for i, v in enumerate(nums) if v == key]
        ans = set()
        for pos in keyPos:
            start = max(0, pos - k)
            end = min(len(nums) - 1, pos + k)
            for i in range(start, end + 1):
                ans.add(i)
        return sorted(ans)