class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=deque([0])
        visit=set(range(len(rooms)))
        
        while q:
            v=q.popleft()
            if v in visit:
                visit.remove(v)
                q.extend(rooms[v])
        return not visit

        