class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i: [] for i in range(n)}
        
        for u, v in richer:
            graph[u].append(v)

        indegree = [0] * n
        for _, v in richer:
            indegree[v] += 1

        q = deque()
        ans = list(range(n))

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if quiet[ans[node]] < quiet[ans[nei]]:
                    ans[nei] = ans[node]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ans