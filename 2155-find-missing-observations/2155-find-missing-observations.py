class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        totalSum=mean*(m+n)
        missing_sum=totalSum-sum(rolls)

        if missing_sum >6 *n or missing_sum<n:
            return []
        res=[]
        while n:
            dice=min(6, missing_sum-n+1)
            res.append(dice)
            
            missing_sum-=dice
            n-=1
        return res