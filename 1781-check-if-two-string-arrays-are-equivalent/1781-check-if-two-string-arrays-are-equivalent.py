class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for c in word1:
            s1+=c
        for c in word2:
            s2+=c
        return s1==s2