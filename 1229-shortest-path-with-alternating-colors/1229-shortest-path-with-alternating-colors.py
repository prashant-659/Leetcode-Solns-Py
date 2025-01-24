class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)
        
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)
        
        ans=[-1 for i in range(n)]
        visit=set()
        q=deque()
        q.append([0,0, None]) #node, length, color
        visit.add((0, None))

        while q:
            node, length, edgeColor=q.popleft()
            if ans[node]==-1:
                ans[node]=length
            
            if edgeColor!="RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append((nei, length+1, "RED"))
            
            if edgeColor!="BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append((nei, length+1, "BLUE"))
        return ans
            