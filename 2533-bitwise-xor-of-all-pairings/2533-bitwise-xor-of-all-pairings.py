class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)&1==0 and len(nums2)&1==0:
            return 0
        elif len(nums1)%2 and len(nums2)%2==0:
            res=0
            for n in nums2:
                res^=n
            return res^0
        elif len(nums2)%2 and len(nums1)%2==0:
            res=0
            for n in nums1:
                res^=n
            return res^0
        else:
            res=0
            for n in nums1:
                res^=n
            for n in nums2:
                res^=n
            return res^0

        

