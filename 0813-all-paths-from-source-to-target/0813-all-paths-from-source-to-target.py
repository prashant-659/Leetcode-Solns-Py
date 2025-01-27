class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # edges={i:graph[i] for i in range(len(graph))}

        # res=[] 
        # stack=[(0,[0])]
        # while stack:
        #     node, path=stack.pop()
        #     if node==len(graph)-1:
        #         res.append(path)
            
        #     for nei in edges[node]:
        #         stack.append((nei, path+[nei]))
        # return res
        result=[]
        def dfs(node, path):

        # If the current node is the target, add the path to the result
            if node == len(graph)-1:
                result.append(path.copy())
                return
            
            # Explore all neighbors
            for neighbor in graph[node]:
                path.append(neighbor)  # Add the neighbor to the current path
                dfs(neighbor, path)    # Recursively explore
                path.pop() 
        dfs(0, [0])     # Start DFS from node 0 with the initial path [0]
        return result