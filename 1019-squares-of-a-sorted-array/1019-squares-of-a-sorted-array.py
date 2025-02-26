class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0, len(nums)-1
        arr=[]
        while l<=r:
            left=nums[l]**2
            right=nums[r]**2
            if left>=right:
                arr.append(left)
                l+=1
            elif right>=left:
                arr.append(right)
                r-=1
            
        return arr[::-1]
            
