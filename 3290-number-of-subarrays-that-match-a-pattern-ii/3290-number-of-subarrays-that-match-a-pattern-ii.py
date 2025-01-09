class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        res=[]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                res.append("a")
            elif nums[i-1]==nums[i]:
                res.append("e")
            else:
                res.append("d")
        for i in range(len(pattern)):
            if pattern[i]==1:
                pattern[i]="a"
            elif pattern[i]==0:
                pattern[i]="e"
            else:
                pattern[i]="d"

        lps=[0]*len(pattern)
        i=1
        length=0
        while i<len(pattern):
            if pattern[i]==pattern[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
                    
        i,j=0,0
        m=len(pattern)
        ans=0
        while i<len(res):
            if res[i]==pattern[j]:
                i+=1
                j+=1
                if j==m:
                    ans+=1
                    j=lps[j-1]
            elif pattern[j]!=res[i]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return ans
        