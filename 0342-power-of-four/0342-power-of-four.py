class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            if 4**i==n:
                return True
            if 4**i>n:
                return False
        return False

        