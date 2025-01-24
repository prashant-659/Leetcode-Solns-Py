class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edges={i:graph[i] for i in range(len(graph))}

        res=[] 
        stack=[(0,[0])]
        while stack:
            node, path=stack.pop()
            if node==len(graph)-1:
                res.append(path)
            
            for nei in edges[node]:
                stack.append((nei, path+[nei]))
        return res