class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        # preMap=defaultdict(list)
        # visited=set()
        # for u, v in prerequisites:
        #     preMap[u].append(v)
            
        # def dfs(curr_course):
        #     if curr_course in visited:
        #         return False
        #     if preMap[curr_course]==[]:
        #         return True
        #     visited.add(curr_course)

        #     for pre in preMap[curr_course]:
        #         if not dfs(pre): return False

        #     visited.remove(curr_course)
        #     preMap[curr_course]=[]
        #     return True
        graph={i:[] for i in range(numCourses)}
        for u, v in prereq:
            graph[u].append(v)

        visit,cycle=set(),set()
        res=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for child in graph[crs]:
                if not dfs(child):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True
        



            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True