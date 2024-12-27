class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag=Counter(magazine)
        ran=Counter(ransomNote)
        
        for r in ransomNote:
            if r not in mag:
                return False
            else:
                if mag[r]<ran[r]:
                    return False
        return True