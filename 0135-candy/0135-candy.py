class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies=[1]*len(ratings)
        for i in range(1,len(ratings)): #left to right greedy
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i], 1+candies[i+1])
        return sum(candies)