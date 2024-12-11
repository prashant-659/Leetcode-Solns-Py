class Solution:
    def frequencySort(self, s: str) -> str:
        mp=Counter(s)
        heap=[(-val, key) for key, val in mp.items()]
        heapq.heapify(heap)
        ans=[]
        while heap:
            val, key=heapq.heappop(heap)

            for i in range(-val):
                ans.append(key)
        return "".join(ans)