class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            powof4=4**i
            if powof4==n:
                return True
            if powof4>n:
                return False
        return False