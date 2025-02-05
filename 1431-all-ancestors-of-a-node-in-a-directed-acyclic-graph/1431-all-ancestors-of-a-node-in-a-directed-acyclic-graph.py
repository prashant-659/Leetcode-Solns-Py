class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree=[0]*n
        graph=defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        for _,v in edges:
            indegree[v]+=1
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        ans=[set() for _ in range(n)]

        while q:
            node=q.popleft()

            for nei in graph[node]:
                ans[nei].add(node)
                ans[nei].update(ans[node])
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        ans=[sorted(list(s)) for s in ans]
        return ans

