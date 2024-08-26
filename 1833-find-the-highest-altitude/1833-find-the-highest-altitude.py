class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #prefix sum based ques
        n=len(gain)
        maxalt=0
        curr=0
        for i in range(n):
            curr+=gain[i]
            maxalt=max(maxalt,curr)
        
            
        return maxalt
        

