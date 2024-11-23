class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        if n>=10 and n<19:
            return True
        if n>=19 and n<27:
            return False
        if n>=27 and n<34:
            return True
        if n>=34 and n<40:
            return False
        if n>=40 and n<45:
            return True
        if n>=45 and n<49:
            return False
        return True
        
