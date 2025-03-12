class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posCt=0
        negCt=0
        for n in nums:
            if n<0:
                negCt+=1
            if n>0:
                posCt+=1
        return max(negCt, posCt)