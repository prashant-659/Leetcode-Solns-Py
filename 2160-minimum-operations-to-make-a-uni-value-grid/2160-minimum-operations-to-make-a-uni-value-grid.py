class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li=[val for r in grid for val in r]
        li.sort()
        n=len(li)
        med=li[n//2]

        ops=0
        for num in li:
            diff=abs(med-num)
            if diff%x!=0:
                return -1
            ops+=diff//x
        return ops

