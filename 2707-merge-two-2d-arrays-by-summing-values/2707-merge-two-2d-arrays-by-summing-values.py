class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=[]
        mp=defaultdict(int)
        for a, b in nums1:
            mp[a]=b
        for a, b in nums2:
            if a in mp:
                mp[a]+=b
            else:
                mp[a]=b
        for key, val in mp.items():
            res.append([key, val])
        res.sort()
        return res

