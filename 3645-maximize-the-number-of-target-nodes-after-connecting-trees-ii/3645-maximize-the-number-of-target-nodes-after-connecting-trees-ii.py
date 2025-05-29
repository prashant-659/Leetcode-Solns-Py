class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        tree1=defaultdict(list)
        tree2=defaultdict(list)

        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        
        vis=set()

        def bipartite(n, graph):
            red=set()
            blue=set()
            q=deque()
            q.append((True, n))
            visit=set()
            visit.add(n)

            while q:
                c, node=q.popleft()
                if c:
                    red.add(node)
                else:
                    blue.add(node)
                for nei in graph[node]:
                    if nei in visit:
                        continue
                    visit.add(nei)
                    q.append((not c, nei))
            return red, blue
        red1, blue1=bipartite(edges1[0][0], tree1)
        red2, blue2=bipartite(edges2[0][0], tree2)

        ans=[]
        maxi=max(len(red2), len(blue2))

        for i in sorted(tree1.keys()):
            if i in red1:
                ans.append(len(red1)+maxi)
            else:
                ans.append(len(blue1)+maxi)
        return ans

