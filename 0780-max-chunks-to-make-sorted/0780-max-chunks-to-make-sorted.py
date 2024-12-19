class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # n=len(arr)
        # prefix=[0]*(n)

        # for i, a in enumerate(arr):
        #     if a != i:
        #         prefix[min(a, i)]+=1
        #         prefix[max(a,i)]-=1
        # print(prefix)
        # chunks=0
        # cur=0
        # for x in prefix:
        #     cur+=x
        #     if cur==0:
        #         chunks+=1
        # return chunks
        cur_max=-1
        res=0
        for i, n in enumerate(arr):
            cur_max=max(n, cur_max)

            if cur_max==i:
                res+=1
        return res
