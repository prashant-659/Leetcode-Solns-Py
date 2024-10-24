class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:        
        store = []
        mid = sum(cost)//2
        for i, n in enumerate(nums):
            store.append((n, cost[i]))
        
        store.sort()
        for n, c in store:
            mid -= c
            if mid < 0:
                mid = n
                break

        total_cost = 0
        for n, c in store:
            total_cost += abs(mid - n)*c

        return(total_cost)