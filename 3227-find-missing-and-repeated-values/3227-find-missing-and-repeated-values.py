class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dct = defaultdict(int)
        n = len(grid)**2 + 1
        for row in grid:
            for val in row:
                dct[val]+=  1
        l = [0,0]
        for i in range(1,n):
            val = dct.get(i,0)
            if val > 1:
                l[0] = i
            if val == 0:
                l[1] = i
        return l