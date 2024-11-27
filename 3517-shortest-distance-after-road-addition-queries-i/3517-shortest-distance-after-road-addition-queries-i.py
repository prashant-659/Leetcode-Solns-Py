class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # mp=defaultdict(list)
        # for i in range(0,n-1):
        #     mp[i].append(i+1)
        # ans=[]
        # for q1,q2 in queries:
        #     mp[q1].append(q2)

        #     q=deque()
        #     q.append((0,0))
        #     visited=set()
        #     visited.add(0)
        #     while q:
        #         node, s=q.popleft()
        #         if node==n-1:
        #             ans.append(s)
        #         for v in mp[node]:
        #             if v not in visited:
        #                 q.append((v,s+1))
        #                 visited.add(v)
        # return ans
        adj=[[i+1] for i in range(n)]
        def shortest_path():
            q=deque() #node, length
            q.append((0,0))
            visit=set()
            visit.add((0,0))

            while q:
                cur, length=q.popleft()
                if cur==n-1:
                    return length

                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length+1))
                        visit.add(nei)





        


        res=[]

        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        return res
