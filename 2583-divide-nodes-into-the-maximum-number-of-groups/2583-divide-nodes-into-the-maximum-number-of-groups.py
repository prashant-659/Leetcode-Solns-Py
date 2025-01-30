class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def get_connected_component(src):
            q=deque([src]) #node, group
            component=set([src]) #node->length from src+1

            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue
                    q.append((nei))
                    component.add(nei)
                    visit.add(nei)
            return component
        


        def longest_path(src):
            q=deque([(src,1)]) #node, group
            dist={src:1} #node->length from src+1

            while q:
                node, length=q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] ==length:
                            return -1
                        continue
                    q.append((nei, length+1))
                    dist[nei]=length+1
            return max(dist.values())
                

        visit=set()
        res=0
        for i in range(1,n+1):
            if i in visit:
                continue
            visit.add(i)

            component=get_connected_component(i)
            max_cnt=0

            for src in component:
                length=longest_path(src)
                if length==-1:
                    return -1
                

                max_cnt=max(max_cnt, length)

            res+=max_cnt
        return res
        # rank=[0]*(n+1)
        # par=[i for i in range(n+1)]

        # def find(n):
        #     p=par[n]

        #     while p!=par[p]:
        #         p=par[par[p]]
        #         p=par[p]
        #     return p
        # def union(n1, n2):
        #     p1=find(n1)
        #     p2=find(n2)
        #     if p1==p2:
        #         return False
        #     if rank[p1]>rank[p2]:
        #         par[p2]=p1
        #         rank[p1]+=rank[p1]
        #     elif rank[p2]>rank[p1]:
        #         par[p1]=p2
        #         rank[p2]+=rank[p1]
        #     return True
        # res=0
        # for n1,n2 in edges:
        #     if not union(n1,n2):
        #         res+=1
            
        # return res
        


