class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=[0]*(n)

        for i, a in enumerate(arr):
            if a != i:
                prefix[min(a, i)]+=1
                prefix[max(a,i)]-=1
        print(prefix)
        chunks=0
        cur=0
        for x in prefix:
            cur+=x
            if cur==0:
                chunks+=1
        return chunks


