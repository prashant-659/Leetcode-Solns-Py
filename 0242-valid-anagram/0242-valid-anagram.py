class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter1=Counter(s)
        counter2=Counter(t)
        return counter1==counter2
            