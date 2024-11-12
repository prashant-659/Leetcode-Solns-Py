class Solution:
    def maximumSetSize(self, A: List[int], B: List[int]) -> int:
        N = len(A) // 2
        A = set(A)
        B = set(B)
        onlyA = min(len(A - B), N)
        onlyB = min(len(B - A), N)
        both = min(len(A & B), 2 * N - onlyA - onlyB)
        return onlyA + onlyB + both