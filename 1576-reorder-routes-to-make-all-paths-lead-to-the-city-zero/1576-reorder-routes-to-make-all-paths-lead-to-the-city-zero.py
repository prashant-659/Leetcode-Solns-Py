# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         # edges=defaultdict(list)
#         # ori=defaultdict(int)
#         # for u, v in connections:
#         #     edges[u].append(v)
#         #     edges[v].append(u)
#         #     ori[u]=v
        
#         # q=deque([0])
#         # visit=set([0])
#         # ans=0
#         # while q:
#         #     city=q.popleft()
#         #     for nei in edges[city]:
#         #         if nei in visit:
#         #             continue
#         #         if ori[city]!=nei:
#         #             ans+=1
#         #         q.append(edges[nei])
#         #         visit.add(nei)
#         # return ans

#         edges = defaultdict(list)
#         ori = defaultdict(int)
#         for u, v in connections:
#             edges[u].append(v)
#             edges[v].append(u)
#             ori[u] = v  # Note: This overwrites if u has multiple edges

#         q = deque([0])
#         visit = set([0])
#         ans = 0

#         while q:
#             city = q.popleft()
#             for nei in edges[city]:
#                 if nei in visit:
#                     continue
#                 # Check if (city -> nei) is not an original edge
#                 if ori[city] != nei:  # Fixing the logic here as well
#                     ans += 1
#                 q.append(nei)  # Append the node, not the list
#                 visit.add(nei)
#         return ans
        
        






































class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = defaultdict(list)
        ori={(a,b) for a, b in connections} #

        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)


        q = deque([0])  
        visit = set()
        visit.add(0)
        ans = 0

        while q:
            city = q.popleft()
            for nei in edges[city]:
                if nei not in visit:   
                    if (city, nei) in ori:  
                        ans += 1
                    q.append(nei)
                    visit.add(nei)

        return ans





