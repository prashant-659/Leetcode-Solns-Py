class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divisionmap=defaultdict(list)
        for i, edges in enumerate(equations):
            divisionmap[edges[0]].append((edges[1],values[i]))

            divisionmap[edges[1]].append((edges[0],1/values[i]))
        
        print(divisionmap)
        def bfs(src, target):
            if src not in divisionmap or target not in divisionmap:
                return -1

            q=deque()
            q.append([src,1])
            
            visit=set()
            visit.add(src)
            while q:
                n, w=q.popleft()

                if n==target:
                    return w
                for nei, weight in divisionmap[n]:
                    if nei not in visit:
                        q.append([nei, weight*w])
                        visit.add(nei)
            return -1



        return [bfs(q[0],q[1]) for q in queries]