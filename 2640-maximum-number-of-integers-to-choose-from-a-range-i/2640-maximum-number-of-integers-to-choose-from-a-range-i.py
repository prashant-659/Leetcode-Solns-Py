class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        visit=set()
        for i in range(len(banned)):
            if banned[i]<=n:
                visit.add(banned[i])
        cur=0
        sum_=0
        for i in range(1,n+1):
            
            if i not in visit:
                
                if sum_+i>maxSum:
                    break
                sum_+=i
                cur+=1
                
            
        return cur





