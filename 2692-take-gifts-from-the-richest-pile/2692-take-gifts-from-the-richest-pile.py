class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i]*=-1
        heapq.heapify(gifts)

        for i in range(k):
            gift=heapq.heappop(gifts)
            gift=int(math.sqrt(-1*gift))
            heapq.heappush(gifts,-1* gift)
        return -1*sum(gifts)