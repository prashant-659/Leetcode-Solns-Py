class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        n=len(pizzas)
        days=n//4
        l=(days+1)//2 #xmall
        s=sum(pizzas[:l])
        left=days-l
        l+=1
        while left>0:
            s+=pizzas[l]
            l+=2
            left-=1
        return s
        