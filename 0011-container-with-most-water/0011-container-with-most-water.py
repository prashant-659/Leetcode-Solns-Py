class Solution:
    def maxArea(self, h: List[int]) -> int:
        # l,r=0,len(height)-1
        # area=0
        # while l<r:
        #     area=max(area,min(height[l],height[r])*(r-l))
        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #         r-=1
            
        # return area
        l=0
        r=len(h)-1
        #max_area=0
        curr_area=0
        while l<r:
            curr_area=max(curr_area,min(h[l],h[r])*(r-l))
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return curr_area