class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        ans, curr = 0, 1
        for i in range(n):
            if i + 1 < n and word[i] < word[i + 1]:
                curr += 1
            else:
                ans += 3 - curr
                curr = 1
        return ans