
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        start = 0
        substring = {}
        maxLength = 0

        for end in range(len(s)):
            if s[end] in substring:
                substring[s[end]] += 1
            else:
                substring[s[end]] = 1

            while substring[s[end]] > 2:
                substring[s[start]] -= 1
                start += 1
            maxLength = max(maxLength, end - start + 1)
                
        
        return maxLength

                




