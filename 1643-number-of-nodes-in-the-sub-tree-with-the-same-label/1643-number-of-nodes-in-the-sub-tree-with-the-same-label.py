class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans=[0]*n
        print(graph)
        def dfs(index, parent):
            count=Counter()

            for edge in graph[index]:
                if edge!=parent:
                    count+=dfs(edge, index)
            count[labels[index]]+=1
            ans[index]=count[labels[index]]
            return count
        dfs(0,-1)
        return ans
            