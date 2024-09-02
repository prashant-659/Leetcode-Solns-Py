class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum=0
        for i in range(len(chalk)):
            chalk_sum+=chalk[i]
            if chalk_sum>k:
                break
        new_k=k%chalk_sum
        for i in range(len(chalk)):
            if new_k<chalk[i]:
                return i
            else:
                new_k-=chalk[i]
        return 0
        
        
            