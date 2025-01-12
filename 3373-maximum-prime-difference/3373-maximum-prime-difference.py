class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        hash=[]
        for j,n in enumerate(nums):
            if n>1:
                flag=True
                for i in range(2, int(n**0.5)+1):
                    if n%i==0:
                        flag=False
                        break
                if flag==True:
                    hash.append(j)
        print(hash)
        return hash[-1]-hash[0]
        
