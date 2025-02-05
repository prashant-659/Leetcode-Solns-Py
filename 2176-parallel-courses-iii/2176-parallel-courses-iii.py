class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        #kahns algo use with care and you can solve it but how?
        # 1->5, 1
        # 2->5, 2
        # 3->5, 3
        # 3->4, 4
        # 4->5, 5
        graph=defaultdict(list)
        indegree=[0]*(n+1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v]+=1
        q=deque()
        # dp={i:time[i-1] for i in range(1,n+1)}
        dp=[0]*(n+1)
        for i in range(1, n+1):
            dp[i]=time[i-1]
        for i in range(1,n+1):
            if indegree[i]==0:
                q.append(i)
        ans=0
        months=0
        while q:
            node=q.popleft()
            for nei in graph[node]:
                dp[nei]=max(dp[nei],dp[node]+time[nei-1])
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return max(dp)



    
        
        

