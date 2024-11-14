class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        #TLE (80/81)
        # adj={src:[] for src, dst in tickets}

        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)
        
        # res=["JFK"]

        # def dfs(src):
        #     if len(res)==len(tickets)+1:
        #         return True
        #     if src not in adj:
        #         return False
            
        #     temp=list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)

        #         if dfs(v): 
        #             return True

        #         adj[src].insert(i,v)
        #         res.pop()

        #     return False
        # dfs("JFK")
        # return res

        def dfs(src):
            while len(edges[src])>0:
                dfs(edges[src].pop())
            res.insert(0,src)
        
        edges=collections.defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            edges[u].append(v)
            
        
        res=[]
        dfs("JFK")
        return res