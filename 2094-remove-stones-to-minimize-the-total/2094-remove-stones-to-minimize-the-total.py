class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-p for p in piles]
        heapify(piles)
        while k:
            x=-heappop(piles)
            x=math.ceil(x/2)
            heappush(piles,-x)
            k-=1
        return -sum(piles)
