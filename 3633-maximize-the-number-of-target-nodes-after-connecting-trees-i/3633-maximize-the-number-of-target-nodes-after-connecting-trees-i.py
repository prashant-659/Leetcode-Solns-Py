class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        # Recursively get the number of targets from 'node' 
        def getNumTargets(node, parent, adj, k) -> int:
            if k <= 0:
                return 1

            count = 1
            for nei in adj[node]:
                if nei != parent:
                    count += getNumTargets(nei, node, adj, k-1)
            return count

        # Create graph 
        def getGraph(edges):
            adj = collections.defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj


        # Handle edge case
        if k == 0: return [1] * (len(edges1)+1)

        # Process Graph 1
        adj1 = getGraph(edges1)
        targets1 = {node: getNumTargets(node, -1, adj1, k) for node in adj1}
            
        # Process graph2, use k-1 since the connection from graph1 to graph2 takes one edge
        adj2 = getGraph(edges2)
        targets2 = {node: getNumTargets(node, -1, adj2, k - 1) for node in adj2}

        maxNumTargets2 = max(targets2.values())
        return [targets1[i] + maxNumTargets2 for i in range(len(edges1)+1)]
        