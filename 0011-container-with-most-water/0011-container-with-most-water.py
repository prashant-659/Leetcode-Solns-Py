class Solution:
    def maxArea(self, height: List[int]) -> int:
#         left=[0]*len(height)
#         left[0]=height[0]
#         right=[0]*len(height)
#         right[-1]=height[-1]
#         for i in range(1,len(height)):
#             left[i]=max(left[i-1], height[i])
        
#         for i in range(len(height)-2,-1,-1):
#             right[i]=max(right[i+1], height[i])
#         print(left, right)
        l,r=0, len(height)-1
        area=0
        while l<r:
            area=max(area, min(height[l], height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area
        