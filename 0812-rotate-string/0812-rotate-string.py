class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for j,s1 in enumerate(s):
            if s1==goal[0]:
                if s[j:] +s[:j]==goal:
                    return True
        return False
        
        
        
