class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def helper(s, idx):
            num=0
            while idx<len(s):
                if s[idx]==".":
                    break
                else:
                    num=num*10+int(s[idx])

                idx+=1
            return [num, idx+1]
                
        
        l,r=0,0
        while l<len(version1) or r<len(version2):
            v1, l=helper(version1, l)
            v2, r=helper(version2, r)

            if v1>v2:
                return 1
            elif v2>v1:
                return -1
        return 0