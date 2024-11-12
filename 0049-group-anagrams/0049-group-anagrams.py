class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        res=[]
        for i in range(len(strs)):
            new=''.join(sorted(strs[i]))
            if new not in mp:
                mp[new]=[]
            mp[new].append(strs[i])
        return list(mp.values())




