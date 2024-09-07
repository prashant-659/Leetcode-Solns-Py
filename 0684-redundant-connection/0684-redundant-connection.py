class Solution(object):
    def findRedundantConnection(self, edges):
        # graph = collections.defaultdict(set)

        # def dfs(source, target):
        #     if source not in seen:
        #         seen.add(source)
        #         if source == target: return True
        #         return any(dfs(nei, target) for nei in graph[source])

        # for u, v in edges:
        #     seen = set()
        #     if u in graph and v in graph and dfs(u, v):
        #         return u, v
        #     graph[u].add(v)
        #     graph[v].add(u)

        par=[i for i in range(len(edges)+1) ]
        rank=[1]*(len(edges)+1)

        def find(n1):
            p=par[n1]

            while p!=par[p]:
                p=par[par[p]] #path compression
                p=par[p]
            return p
                
        def union(n1,n2):
            p1,p2=find(n1), find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

                
