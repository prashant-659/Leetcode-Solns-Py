class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # graph = collections.defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # queue = deque([source])
        # visited = set([source])
        
        # while queue:
        #     node = queue.popleft()
        #     if node == destination:
        #         return True
        #     for neighbor in graph[node]:
        #         if neighbor not in visited:
        #             visited.add(neighbor)
        #             queue.append(neighbor)
        
        # return False







        adjList=defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        # q=deque([source])
        visit=set()

        # while q:
        #     node=q.popleft()
        #     if node==destination:
        #         return True
        #     for nei in adjList[node]:
        #         if nei in visit:
        #             continue
        #         q.append(nei)
        #         visit.add(nei)
        # return False
        
        def dfs(node):

            
            if node==destination:
                return True

            visit.add(node)
            for nei in adjList[node]:
                if nei not in visit:
                    if dfs(nei):
                        return True
                

            return False
        return dfs(source)
