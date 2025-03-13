class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return (g := gcd(targetX, targetY)) and g & (g - 1) == 0