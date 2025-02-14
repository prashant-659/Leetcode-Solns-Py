class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen=set()
        res=0
        for n in words:
            if n[::-1] in seen:
                res += 1
                seen.remove(n[::-1])
            else:
                seen.add(n)
        return res
