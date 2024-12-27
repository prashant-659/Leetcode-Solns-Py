class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=Counter(magazine)
        c2=Counter(ransomNote)
        
        for r in ransomNote:
            if r not in c:
                return False
            else:
                if c[r]<c2[r]:
                    return False
        return True