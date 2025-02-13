class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half=sum(nums)/2
        nums2=[-n for n in nums]
        heapify(nums2)
        op=0
        while half>0:
            x=-heappop(nums2)
            x=x/2.0
            half-=x
            heappush(nums2,-x) 
            op+=1
        return op
        
