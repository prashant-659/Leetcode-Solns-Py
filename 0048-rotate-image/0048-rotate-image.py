class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R=len(matrix)
        C=len(matrix[0])
        for r in range(R):
            for c in range(r, C):
                temp=matrix[r][c]
                matrix[r][c]=matrix[c][r]
                matrix[c][r]=temp
        for r in matrix:
            r.reverse()
        
        