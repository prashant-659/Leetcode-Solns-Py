class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        new=[0]*len(nums)
        for i,n in enumerate(nums):
            new[i]=-1*n
        heapq.heapify(new)
        total=0
        for i in range(k):
            total-=new[0]
            heapreplace(new,new[0]//3)
        return total