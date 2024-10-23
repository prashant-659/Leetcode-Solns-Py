class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in range(len(digits)):
            n=n*10+digits[i]
        r=n+1
        arr=[int(x) for x in str(r)]
        return arr
            
