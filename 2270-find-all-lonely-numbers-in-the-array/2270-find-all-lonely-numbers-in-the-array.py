class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        num=set(nums)
        arr=[]
        for n in nums:
            if (n-1) not in num and (n+1) not in num and c[n]==1:
                arr.append(n)
        return arr