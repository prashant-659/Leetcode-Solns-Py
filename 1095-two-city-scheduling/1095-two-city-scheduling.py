class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund=[]
        mini=0
        for A, B in costs:
            refund.append(B-A)
            mini+=A
        refund.sort()
        for i in range(len(costs)//2):
            mini+=refund[i]
        return mini
