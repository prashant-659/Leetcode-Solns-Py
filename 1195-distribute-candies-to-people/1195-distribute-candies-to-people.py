class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*(num_people)
        num=0
        while candies>0:
            if candies>=(num+1):
                candies-=(num+1)
                res[num%num_people]+=num+1
            else:
                res[num%num_people]+=candies
                candies=0
            num+=1
        return res
                
        return res