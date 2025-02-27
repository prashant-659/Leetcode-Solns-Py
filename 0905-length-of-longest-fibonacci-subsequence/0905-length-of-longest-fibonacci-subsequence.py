class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        maxi=-1
        arr_map={n: i for i, n in enumerate(arr)}
        dp={}#(i, j)->;ength of longest subseq
        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev,cur=arr[i], arr[j]
                nxt=prev+cur
                length=2
                if nxt in arr_map:
                    length=1+dp[(j, arr_map[nxt])]
                    maxi=max(maxi, length)
                dp[(i,j)]=length
        return maxi if maxi>2 else 0


