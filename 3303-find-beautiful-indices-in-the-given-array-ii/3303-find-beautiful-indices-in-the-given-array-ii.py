from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def lps(pattern: str) -> List[int]:
            lps = [0] * len(pattern)
            i, length = 1, 0
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def matching(text: str, pattern: str, lps: List[int]) -> List[int]:
            res = []
            n, m = len(text), len(pattern)
            i, j = 0, 0
            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                    if j == m:
                        res.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res

        if not a or not b:  # Handle edge cases where patterns are empty
            return []

        lps1 = lps(a)
        lps2 = lps(b)
        
        res1 = matching(s, a, lps1)
        res2 = matching(s, b, lps2)

        i, j = 0, 0
        ans = []
        while i < len(res1) and j < len(res2):
            if abs(res1[i] - res2[j]) <= k:
                ans.append(res1[i])
                i += 1  # Increment `i` to avoid duplicates
            elif res2[j] - res1[i] > k:
                i += 1
            else:
                j += 1
        return ans
