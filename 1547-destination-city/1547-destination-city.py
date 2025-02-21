class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp=defaultdict(list)
        for src, dst in paths:
            mp[src].append(dst)
        for src in mp.keys():
            if mp[src][0] not in mp:
                return "".join(mp[src][0])
        
