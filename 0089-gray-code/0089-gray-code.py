class Solution:
    def grayCode(self, n: int) -> List[int]:
        b, r = 1, [0]
        for _ in range(n):
            r += [i|b for i in reversed(r)]
            b <<= 1
        return r