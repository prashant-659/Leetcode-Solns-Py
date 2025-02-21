class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp=defaultdict(str)
        for src, dst in paths:
            mp[src]=dst
        for src in mp.keys():
            if mp[src] not in mp:
                return mp[src]
        
