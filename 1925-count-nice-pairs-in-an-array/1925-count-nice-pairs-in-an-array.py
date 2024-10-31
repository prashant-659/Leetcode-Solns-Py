class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            x=str(x)
            x=x[::-1]
            return int(x)
        MOD = int(1e9 + 7)
        ct=0
        set1=set()
        mp=defaultdict(int)
        for i in range(len(nums)):
            diff=nums[i]-rev(nums[i])
            if diff in mp:
                ct+=mp[diff]
            mp[diff]=1+mp.get(diff,0)
            
        return ct%MOD

