class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        res=[]

        for r in range(m):
            start=r*n 
            end=start+n#(-1)
            res.append(original[start:end])


        return res