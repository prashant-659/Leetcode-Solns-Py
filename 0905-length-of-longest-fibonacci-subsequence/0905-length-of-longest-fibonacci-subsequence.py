class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        maxi=-1
        arrs=set(arr)
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                prev,cur=arr[i], arr[j]
                nxt=prev+cur
                l=2
                while nxt in arrs:
                    l+=1
                    prev, cur=cur, nxt
                    nxt=prev+cur
                maxi=max(maxi, l)
        return maxi if maxi>2 else 0


