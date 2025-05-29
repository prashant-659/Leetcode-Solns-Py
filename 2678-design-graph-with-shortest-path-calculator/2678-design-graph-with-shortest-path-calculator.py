class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.mat=[[inf]*n for _ in range(n)]

        for u, v, cost in edges:
            self.mat[u][v]=cost
        for i in range(n):
            self.mat[i][i]=0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.mat[j][k]=min(self.mat[j][k], self.mat[j][i]+self.mat[i][k])

                    

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost=edge
        n=len(self.mat)
        for i in range(n):
            for j in range(n):
                self.mat[i][j]=min(self.mat[i][j], self.mat[i][u]+self.mat[v][j]+cost)


    def shortestPath(self, node1: int, node2: int) -> int:
        if self.mat[node1][node2]==inf:
            return -1
        return self.mat[node1][node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)