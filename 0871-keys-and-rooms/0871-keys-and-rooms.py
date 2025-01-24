class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # q=deque([0])
        # visit=set(range(len(rooms)))
        
        # while q:
        #     v=q.popleft()
        #     if v in visit:
        #         visit.remove(v)
        #         q.extend(rooms[v])
        # return not visit

        visited=[False]*len(rooms)
        def dfs( source, visited):
            visited[source]=True
            for nei in rooms[source]:
                if not visited[nei]:
                    dfs(nei, visited)
        dfs(0, visited)
        for i in range(len(rooms)):
            if visited[i]==False:
                return False
        return True
            