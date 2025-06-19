import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        vs = defaultdict(list)
        for u, v in edges:
            if vals[v] > 0:
                vs[u].append(vals[v])
            if vals[u] > 0:
                vs[v].append(vals[u])
        
        return max(
            value + sum(heapq.nlargest(k, vs[u]))
            for u, value in enumerate(vals)
        )