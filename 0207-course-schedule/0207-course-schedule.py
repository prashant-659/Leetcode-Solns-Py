class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        visited=set()
        for u, v in prerequisites:
            preMap[u].append(v)
            
        def dfs(curr_course):
            if curr_course in visited:
                return False
            if preMap[curr_course]==[]:
                return True
            visited.add(curr_course)

            for pre in preMap[curr_course]:
                if not dfs(pre): return False

            visited.remove(curr_course)
            preMap[curr_course]=[]
            return True


            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True