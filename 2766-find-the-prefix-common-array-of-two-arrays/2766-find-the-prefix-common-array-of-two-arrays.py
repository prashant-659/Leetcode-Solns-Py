class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        record=set()
        n=len(A)
        res=[0]*n

        for i in range(n):
            record.add(A[i])
            record.add(B[i])
            res[i]=(i+1)*2-len(record)
        return res

            
