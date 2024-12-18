class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return []
        res=[]
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                res.append(n)
            nums[n-1]=-nums[n-1]
            
        return res

            








    
        print(res)