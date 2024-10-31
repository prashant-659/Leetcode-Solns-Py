class Solution:
    def possibleStringCount(self, word: str) -> int:
        count=0
        prev=""
        for c in word:
            if c == prev:
                count+=1
            prev=c
        return count+1