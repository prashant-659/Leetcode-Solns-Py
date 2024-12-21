class Solution:
    def dfs(self, graph, values, k, count, cur, parent=-1):
        total=values[cur]
        for nei in graph[cur]:
            if nei!=parent:
                total+=self.dfs(graph, values, k, count, nei, cur)
        total%=k
        if total==0:
            count[0]+=1
        return total


    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph=defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        ct=[0]
        self.dfs(graph, values, k, ct, 0)
        return ct[0]
            