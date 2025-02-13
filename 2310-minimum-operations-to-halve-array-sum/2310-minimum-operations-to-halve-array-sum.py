class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half=sum(nums)/2
        nums2=[-n for n in nums]
        heapify(nums2)
        op=0
        while half>0:
            x=-heappop(nums2)
            y=x/2.0
            half-=y
            heappush(nums2,-y) 
        
            op+=1
        print(nums2)
        return op
        
