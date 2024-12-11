class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp=defaultdict(int)
        for w in words:
            mp[w]=1+mp.get(w,0)
        heap = [(-value, key) for key, value in mp.items()]
        heapq.heapify(heap)
        ans=[]
        for i in range(k):
            val, key=heapq.heappop(heap)
            ans.append(key)
        return ans


