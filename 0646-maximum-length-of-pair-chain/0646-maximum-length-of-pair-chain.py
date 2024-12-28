class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        LIS=[1]*len(pairs)
        pairs.sort()

        for i in range(len(pairs)-1,-1,-1):
            for j in range(i, len(pairs)):
                if pairs[i][1]<pairs[j][0]:
                    LIS[i]=max(LIS[i], 1+LIS[j])
        return max(LIS)