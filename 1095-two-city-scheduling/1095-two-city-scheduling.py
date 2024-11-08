class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # refund=[]
        # mini=0
        # for A, B in costs:
        #     refund.append(B-A)
        #     mini+=A
        # refund.sort()
        # for i in range(len(costs)//2):
        #     mini+=refund[i]
        # return mini
        costs.sort(key = lambda x: x[0]-x[1])
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        return total
