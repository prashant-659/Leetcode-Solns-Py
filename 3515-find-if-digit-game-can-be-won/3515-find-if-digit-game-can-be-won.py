class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        canWin=True
        sum_single=0
        sum_double=0
        for num in nums:
            if num<=9:
                sum_single+=num
            else:
                sum_double+=num
        if sum_double==sum_single:
            canWin=False
        return canWin