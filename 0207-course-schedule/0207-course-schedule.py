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

        # visit,cycle=set(),set()
        # res=[]
        # def dfs(crs):
        #     if crs in cycle:
        #         return False
        #     if crs in visit:
        #         return True
        #     cycle.add(crs)
        #     for child in graph[crs]:
        #         if not dfs(child):
        #             return False
        #     cycle.remove(crs)
        #     visit.add(crs)
        #     return True
        



            

        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True

        indegree=[0]*numCourses
        for i in range(len(graph)):
            for x in graph[i]:
                indegree[x]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            course=q.popleft()
            for nei in graph[course]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if max(indegree)!=0:
            return False
        return True
        