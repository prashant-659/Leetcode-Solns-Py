class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R=len(mat)
        C=len(mat[0])

        mat_to_pos={}
        for r in range(R):
            for c in range(C):
                mat_to_pos[mat[r][c]]=(r,c)

        row_cnt=[0]*R
        col_cnt=[0]*C

        for i in range(len(arr)):
            r,c =mat_to_pos[arr[i]]
            row_cnt[r]+=1
            col_cnt[c]+=1
             
            if col_cnt[c]==R or row_cnt[r]==C:
                return i
