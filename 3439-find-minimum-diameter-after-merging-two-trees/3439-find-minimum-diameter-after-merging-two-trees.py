class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n=len(edges1)+1
        m=len(edges2)+1

        def buil_adj(edges):
            adj=defaultdict(list)
            for n1, n2 in edges:
                adj[n1].append(n2)
                adj[n2].append(n1)
            return adj

        adj1=buil_adj(edges1)
        adj2=buil_adj(edges2)

        #dfs(return [diameter, max_leaf_path])
        def getDiameter(cur, par, adj):
            
            max_d=0
            max_child_paths=[0,0]

            for nei in adj[cur]:
                if nei==par:
                    continue
                
                nei_d, nei_max_leaf_path=getDiameter(nei, cur, adj)
                max_d=max(max_d, nei_d)

                heapq.heappush(max_child_paths, nei_max_leaf_path)
                heappop(max_child_paths)
            max_d=max(max_d,sum(max_child_paths))
            return [max_d, 1+max(max_child_paths)]


        d1, _ =getDiameter(0,-1,adj1)
        d2, _ =getDiameter(0, -1, adj2)

        return max(d1, d2, 1+ceil(d1/2)+ceil(d2/2))