class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # s,c,z,m=0,0,0,float('inf')
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]<0:
        #             c+=1
        #         if matrix[i][j]==0:
        #             z=1
        #         s+=abs(matrix[i][j])
        #         m=min(m,abs(matrix[i][j]))
                
        # if c%2==0 or z>0:
        #     return s
        # else:
        #     return s-m*2
        res=0

        neg_ct=0
        mat_min=inf
        for row in matrix:
            for n in row:
                res+=abs(n)
                mat_min=min(mat_min, abs(n))
                if n<0:
                    neg_ct+=1


        if neg_ct&1:
            res-=2*mat_min

        return res