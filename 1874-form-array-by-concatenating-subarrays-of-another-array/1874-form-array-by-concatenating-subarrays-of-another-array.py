class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        def lps_(g):
            lps=[0]*len(g)
            i=1
            length=0
            while i<len(g):
                if g[i]==g[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    if length!=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        N=len(nums)
        i=0
        j=0
        G=len(groups)
        matches=0
        g=0

        while g<G and i<N:
            lps=lps_(groups[g])
            while i<N:
                if nums[i]==groups[g][j]:
                    i+=1
                    j+=1
                    if j==len(groups[g]):
                        j=lps[j-1]
                        matches+=1
                        break
                elif j==0:
                    i+=1
                else:
                    j=lps[j-1]
            g+=1
        return matches ==G
                



