class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l=0
        sum_=0
        for i in range(3,len(arr)+1,2):
            for j in range(0,len(arr)-i+1):
                sum_+=sum(arr[j:j+i])
        sum_=sum_+sum(arr)
        return sum_
