class Solution:
    def minSwaps(self, s: str) -> int:
        stacksize=0
        for b in s:
            if b=="[":
                stacksize+=1
            else:
                if stacksize>0:
                    stacksize-=1
        return (stacksize+1)//2

        
        
