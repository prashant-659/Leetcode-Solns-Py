class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        prereqMap={} # map every vourse->hashset of indirec prereqs
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs]=set()
                for prereq in adj[crs]:
                    prereqMap[crs]|=dfs(prereq) #union
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        
        for crs in range(numCourses):
            dfs(crs)

        res=[]
        for u, v in queries:

            res.append(u in prereqMap[v])
        return res
        
        
        

