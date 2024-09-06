class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph=defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        res=[]
        q=deque()
        visit,cycle=set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in graph[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c)==False:
                return []
            
        return res
            
        
        