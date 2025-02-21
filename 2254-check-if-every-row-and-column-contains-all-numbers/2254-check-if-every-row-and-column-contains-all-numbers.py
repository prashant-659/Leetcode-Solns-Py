class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        lst=[i+1 for i in range(n)]

        for r in  range(n):
            if sorted(matrix[r])!=lst:
                return False
        # for r in range(n):
        #     if sorted(matrix[c])!=lst:
        #         return False
        for c in range(n):
            cols=[matrix[r][c] for r in range(n)]
            if sorted(cols)!=lst:
                return False
        return True

        

