class Solution:
    def trailingZeroes(self, n: int) -> int:
        countof0=0
        powerof5=5
        while n//powerof5:
            
            
            countof0+=n//powerof5
            powerof5*=5
            
        return countof0
            