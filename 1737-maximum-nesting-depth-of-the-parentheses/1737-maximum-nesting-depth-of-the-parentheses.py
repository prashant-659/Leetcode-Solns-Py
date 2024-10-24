class Solution:
    def maxDepth(self, s: str) -> int:
        counter=0
        max_coun=0
        for i in s:
            if i=='(':
                counter+=1
                max_coun=max(counter,max_coun)
            elif i==')':
                counter-=1
        return max_coun
            
