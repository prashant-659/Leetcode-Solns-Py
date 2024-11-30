from collections import defaultdict
class Solution:

    def __init__(self):
        self.adj=defaultdict(list)
        self.in_degree=defaultdict(int)
        self.out_degree=defaultdict(int)
    
    def start_node(self):
        start_node=None
        for node in self.out_degree:
            if self.out_degree[node]-self.in_degree[node]==1:
                return node
            
            if self.out_degree[node]>0:
                start_node=node
        return start_node

    def euler_path(self, cur, eulerian_path):

        while self.out_degree[cur]>0:
            self.out_degree[cur]-=1

            next_node=self.adj[cur][self.out_degree[cur]]

            self.euler_path(next_node, eulerian_path)
        eulerian_path.append(cur)


    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        for u, v in pairs:
            self.adj[u].append(v)
            self.out_degree[u]+=1
            self.in_degree[v]+=1
        start_node=self.start_node()

        eulerian_path=[]        
        self.euler_path(start_node,eulerian_path)

        res=[]
        for i in range(len(eulerian_path)-1, 0,-1):
            res.append([eulerian_path[i], eulerian_path[i-1]])

        return res